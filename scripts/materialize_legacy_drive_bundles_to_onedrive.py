#!/usr/bin/env python3
"""Materialize source-required folder bundles from downloaded legacy Drive ZIPs.

This is a recovery helper for the resource migration. It consumes ZIP files
downloaded directly into the OneDrive `INCOMING/checked` area and extracts their
contents into the folder-bundle paths declared in the resource manifest. It does
not create release ZIPs.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import zipfile
from datetime import date
from pathlib import Path

from materialize_folder_bundles_to_onedrive import (
    LOG_PATH,
    MANIFEST_COPY,
    ONEDRIVE_ROOT,
    folder_size,
    inside_onedrive,
)
from resource_manifest import MANIFEST_PATH, read_manifest, write_manifest

INCOMING_DIR = (
    ONEDRIVE_ROOT
    / "INCOMING"
    / "checked"
    / "google_drive_uploads_2026-05-20"
    / "From_Xiaoran_etal_22"
)

SOURCE_ZIPS = {
    "zip-bg-maps-xiaoran-etal": "BG导图合集_lxrwyqlxf.zip",
    "zip-ifbs-mindmap-xiaoran-etal": "思维导图IFBS_lxr.zip",
    "zip-in-lxfwyqlxr": "IN_lxfwyqlxr.zip",
    "zip-mbe-lxrwyalxf": "MBE_lxrwyalxf.zip",
    "zip-pon-review-lxrwyqlxf": "pon复习资料_lxrwyqlxf.zip",
}

IGNORED_PARTS = {"__MACOSX", ".DS_Store"}


def selected_resources(resources: list[dict[str, object]], ids: list[str]) -> list[dict[str, object]]:
    wanted = set(ids) if ids else set(SOURCE_ZIPS)
    selected = [
        resource
        for resource in resources
        if str(resource["id"]) in wanted
    ]
    missing = wanted - {str(resource["id"]) for resource in selected}
    if missing:
        raise ValueError(f"Unknown legacy bundle ids: {', '.join(sorted(missing))}")
    return selected


def safe_member_path(name: str) -> Path | None:
    rel = Path(name)
    if rel.is_absolute() or ".." in rel.parts:
        return None
    if any(part in IGNORED_PARTS for part in rel.parts):
        return None
    return rel


def extract_zip(zip_path: Path, dest: Path, force: bool) -> int:
    dest = inside_onedrive(dest)
    copied = 0
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            rel = safe_member_path(info.filename)
            if rel is None or info.is_dir():
                continue
            target = inside_onedrive(dest / rel)
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and not force:
                continue
            with zf.open(info) as src, target.open("wb") as out:
                shutil.copyfileobj(src, out)
            copied += 1
    return copied


def update_resource(resource: dict[str, object], dest: Path, source_zip: Path) -> None:
    resource["migrated_at"] = date.today().isoformat()
    resource["size_bytes"] = folder_size(dest)
    resource["checksum_sha256"] = ""
    marker = (
        "Folder bundle recovered from legacy Google Drive source archive "
        f"`{source_zip.name}` and materialized directly in OneDrive at "
        f"`{dest.relative_to(ONEDRIVE_ROOT)}`."
    )
    notes = str(resource.get("notes", ""))
    resource["notes"] = f"{notes} {marker}".strip() if marker not in notes else notes


def persist(resources: list[dict[str, object]], log_entries: list[str]) -> None:
    write_manifest(resources, MANIFEST_PATH)
    MANIFEST_COPY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MANIFEST_PATH, MANIFEST_COPY)
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {date.today().isoformat()} legacy Drive folder bundle recovery\n\n")
        for entry in log_entries:
            fh.write(f"- {entry}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resource_ids", nargs="*", help="Legacy folder bundle ids. Defaults to all known source-required bundles.")
    parser.add_argument("--execute", action="store_true", help="Extract source ZIPs into OneDrive and update the manifest.")
    parser.add_argument("--force", action="store_true", help="Overwrite files already present in target bundle folders.")
    args = parser.parse_args()

    resources = read_manifest()
    selected = selected_resources(resources, args.resource_ids)
    log_entries: list[str] = []
    missing_sources = 0

    for resource in selected:
        rid = str(resource["id"])
        source_name = SOURCE_ZIPS.get(rid)
        if source_name is None:
            raise ValueError(f"No legacy source ZIP mapping for {rid}")
        source_zip = inside_onedrive(INCOMING_DIR / source_name)
        dest = inside_onedrive(ONEDRIVE_ROOT / str(resource["local_onedrive_path"]))

        if not source_zip.is_file():
            missing_sources += 1
            print(f"SKIP {rid}: source ZIP not found at {source_zip}")
            continue

        with zipfile.ZipFile(source_zip) as zf:
            file_count = sum(
                1
                for info in zf.infolist()
                if not info.is_dir() and safe_member_path(info.filename) is not None
            )
        print(f"{'EXTRACT' if args.execute else 'PLAN'} {rid}: {file_count} files -> {dest}")
        if args.execute:
            copied = extract_zip(source_zip, dest, args.force)
            update_resource(resource, dest, source_zip)
            log_entries.append(
                f"`{rid}` recovered from `INCOMING/checked/google_drive_uploads_2026-05-20/From_Xiaoran_etal_22/{source_zip.name}` "
                f"to `{dest.relative_to(ONEDRIVE_ROOT)}` ({copied} copied files)"
            )

    if args.execute:
        persist(resources, log_entries)
    return 1 if missing_sources else 0


if __name__ == "__main__":
    sys.exit(main())
