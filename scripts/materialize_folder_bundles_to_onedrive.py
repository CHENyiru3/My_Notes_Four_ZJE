#!/usr/bin/env python3
"""Create OneDrive folder bundles from available migrated resources.

This script never creates ZIP files. It reconstructs `folder_bundle` manifest
entries by copying Git-tracked Markdown files and already-migrated OneDrive
single files into the bundle folder path declared in the manifest.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import date
from pathlib import Path

from resource_manifest import MANIFEST_PATH, ROOT, payload_has_local_data, read_manifest, write_manifest

ONEDRIVE_ROOT = Path("/Users/eric_yiru/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource")
MANIFEST_COPY = ONEDRIVE_ROOT / "MANIFESTS" / "resource_manifest.yml"
LOG_PATH = ONEDRIVE_ROOT / "MANIFESTS" / "migration_log.md"
IGNORED_NAMES = {".DS_Store", "__MACOSX"}


def inside_onedrive(path: Path) -> Path:
    root = ONEDRIVE_ROOT.resolve(strict=False)
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Refusing to write outside ZJE_resource: {path}") from exc
    return resolved


def content_page_for(resource: dict[str, object]) -> Path | None:
    for source in resource.get("website_sources", []):
        source_text = str(source)
        if source_text.startswith("ZJE_Collection/zip_contents/") and source_text.endswith(".md"):
            return ROOT / source_text
    return None


def listed_members(path: Path) -> list[str]:
    members: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- "):
            continue
        member = line[2:].strip()
        parts = Path(member).parts
        if not member or any(part in IGNORED_NAMES for part in parts):
            continue
        members.append(member)
    return members


def one_drive_file_sources(resources: list[dict[str, object]]) -> dict[tuple[str, str, str], Path]:
    sources: dict[tuple[str, str, str], Path] = {}
    for resource in resources:
        if resource.get("resource_type") != "individual_file":
            continue
        key = (str(resource["course"]), str(resource["contributor"]), str(resource["title"]))
        sources[key] = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
    return sources


def repo_source(resource: dict[str, object], member: str) -> Path | None:
    parts = Path(member).parts
    if len(parts) < 2:
        return None
    rel_inside_bundle = Path(*parts[1:])
    candidate = ROOT / "ZJE_Collection" / str(resource["course"]) / str(resource["contributor"]) / rel_inside_bundle
    return candidate if candidate.is_file() and payload_has_local_data(candidate) else None


def one_drive_source(
    resource: dict[str, object],
    member: str,
    file_sources: dict[tuple[str, str, str], Path],
) -> Path | None:
    title = Path(member).name
    course = str(resource["course"])
    contributor = str(resource["contributor"])
    for key in [
        (course, contributor, title),
        (course, "Yiru", title),
        (course, "Yue", title),
    ]:
        candidate = file_sources.get(key)
        if candidate and candidate.is_file() and payload_has_local_data(candidate):
            return candidate
    return None


def resolve_bundle_members(
    resource: dict[str, object],
    resources: list[dict[str, object]],
) -> tuple[list[tuple[Path, Path]], list[str]]:
    content_page = content_page_for(resource)
    if content_page is None or not content_page.exists():
        return [], ["missing contents page"]

    file_sources = one_drive_file_sources(resources)
    resolved: list[tuple[Path, Path]] = []
    missing: list[str] = []
    for member in listed_members(content_page):
        parts = Path(member).parts
        rel_inside_bundle = Path(*parts[1:]) if len(parts) > 1 else Path(member)
        source = repo_source(resource, member)
        if source is None:
            source = one_drive_source(resource, member, file_sources)
        if source is None:
            missing.append(member)
            continue
        resolved.append((source, rel_inside_bundle))
    return resolved, missing


def folder_size(path: Path) -> int:
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def copy_bundle(dest: Path, members: list[tuple[Path, Path]], force: bool) -> int:
    dest = inside_onedrive(dest)
    copied = 0
    dest.mkdir(parents=True, exist_ok=True)
    for source, rel in members:
        target = inside_onedrive(dest / rel)
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not force:
            continue
        shutil.copy2(source, target)
        copied += 1
    return copied


def update_resource(resource: dict[str, object], dest: Path) -> None:
    resource["migrated_at"] = date.today().isoformat()
    resource["size_bytes"] = folder_size(dest)
    resource["checksum_sha256"] = ""
    marker = f"Folder bundle materialized directly in OneDrive at `{dest.relative_to(ONEDRIVE_ROOT)}`."
    notes = str(resource.get("notes", ""))
    resource["notes"] = f"{notes} {marker}".strip() if marker not in notes else notes


def selected_bundles(resources: list[dict[str, object]], ids: list[str]) -> list[dict[str, object]]:
    wanted = set(ids)
    selected = [
        resource
        for resource in resources
        if resource.get("resource_type") == "folder_bundle"
        and (not ids or str(resource["id"]) in wanted)
    ]
    missing = wanted - {str(resource["id"]) for resource in selected}
    if missing:
        raise ValueError(f"Unknown folder bundle ids: {', '.join(sorted(missing))}")
    return selected


def persist(resources: list[dict[str, object]], log_entries: list[str]) -> None:
    write_manifest(resources, MANIFEST_PATH)
    MANIFEST_COPY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MANIFEST_PATH, MANIFEST_COPY)
    if log_entries:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with LOG_PATH.open("a", encoding="utf-8") as fh:
            fh.write(f"\n## {date.today().isoformat()} folder bundle materialization\n\n")
            for entry in log_entries:
                fh.write(f"- {entry}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resource_ids", nargs="*", help="Folder bundle ids. Defaults to all folder bundles.")
    parser.add_argument("--execute", action="store_true", help="Copy available bundle files into OneDrive and update the manifest.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files in bundle folders.")
    args = parser.parse_args()

    resources = read_manifest()
    bundles = selected_bundles(resources, args.resource_ids)
    log_entries: list[str] = []
    incomplete = 0

    for resource in bundles:
        rid = str(resource["id"])
        dest = inside_onedrive(ONEDRIVE_ROOT / str(resource["local_onedrive_path"]))
        members, missing = resolve_bundle_members(resource, resources)
        if missing:
            incomplete += 1
            print(f"SKIP {rid}: {len(missing)} listed files are not available locally")
            for member in missing[:10]:
                print(f"  missing: {member}")
            if len(missing) > 10:
                print(f"  ... {len(missing) - 10} more")
            continue
        if not members:
            incomplete += 1
            print(f"SKIP {rid}: no files listed")
            continue

        print(f"{'COPY' if args.execute else 'PLAN'} {rid}: {len(members)} files -> {dest}")
        if args.execute:
            copied = copy_bundle(dest, members, args.force)
            update_resource(resource, dest)
            log_entries.append(f"`{rid}` materialized at `{dest.relative_to(ONEDRIVE_ROOT)}` ({copied} copied files)")

    if args.execute:
        persist(resources, log_entries)
    if incomplete:
        print(f"Incomplete folder bundles: {incomplete}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
