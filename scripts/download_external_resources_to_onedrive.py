#!/usr/bin/env python3
"""Download external manifest resources directly into the OneDrive tree.

This helper intentionally refuses to write outside ZJE_resource. It is meant
for legacy Google Drive resources after the maintainer decides they can be
mirrored into OneDrive.
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

from resource_manifest import MANIFEST_PATH, read_manifest, write_manifest

ONEDRIVE_ROOT = Path("/Users/eric_yiru/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource")
MANIFEST_COPY = ONEDRIVE_ROOT / "MANIFESTS" / "resource_manifest.yml"
LOG_PATH = ONEDRIVE_ROOT / "MANIFESTS" / "migration_log.md"
MIN_COURSE_PACKAGE_BYTES = 1024 * 1024


def inside_onedrive(path: Path) -> Path:
    resolved_root = ONEDRIVE_ROOT.resolve(strict=False)
    resolved_path = path.resolve(strict=False)
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"Refusing to write outside ZJE_resource: {path}") from exc
    return resolved_path


def is_google_drive(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    return host.endswith("drive.google.com") or host.endswith("docs.google.com")


def is_google_folder(url: str) -> bool:
    return "/drive/folders/" in url


def filename_from_url(url: str, fallback: str) -> str:
    parsed = urlparse(url)
    name = Path(unquote(parsed.path)).name
    if name and "." in name:
        return name
    return fallback


def destination_for(resource: dict[str, object]) -> Path:
    rel = str(resource.get("local_onedrive_path", ""))
    if not rel:
        raise ValueError(f"{resource.get('id')}: missing local_onedrive_path")
    dest = ONEDRIVE_ROOT / rel

    resource_type = str(resource.get("resource_type", ""))
    source_url = str(resource.get("original_source_url", ""))
    if resource_type in {"course_package", "folder_bundle"}:
        dest = ONEDRIVE_ROOT / rel
    elif dest.suffix:
        dest = dest
    else:
        dest = dest / filename_from_url(source_url, f"{resource['id']}__download")

    return inside_onedrive(dest)


def path_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_google_download(url: str, dest: Path, execute: bool) -> list[str]:
    gdown = shutil.which("gdown")
    if gdown:
        base_cmd = [gdown]
    else:
        base_cmd = [sys.executable, "-m", "gdown"]

    if is_google_folder(url):
        cmd = [*base_cmd, "--folder", url, "--output", str(dest)]
        cwd = ONEDRIVE_ROOT
    else:
        cmd = [*base_cmd, "--fuzzy", "--continue", url]
        cwd = dest

    if execute:
        dest.mkdir(parents=True, exist_ok=True)
        subprocess.run(cmd, cwd=cwd, check=True)
    return cmd


def run_direct_download(url: str, dest: Path, execute: bool) -> list[str]:
    curl = shutil.which("curl")
    if not curl:
        raise RuntimeError("curl is required for non-Google direct downloads.")

    if dest.suffix:
        target = dest
    else:
        target = dest / filename_from_url(url, "downloaded_resource")
    target = inside_onedrive(target)
    cmd = [curl, "--location", "--fail", "--output", str(target), url]
    if execute:
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(cmd, check=True)
    return cmd


def select_resources(resources: list[dict[str, object]], ids: list[str], include_folder_urls: bool) -> list[dict[str, object]]:
    selected: list[dict[str, object]] = []
    wanted = set(ids)
    for resource in resources:
        rid = str(resource["id"])
        source_url = str(resource.get("original_source_url", ""))
        if ids and rid not in wanted:
            continue
        if not source_url:
            continue
        if is_google_folder(source_url) and not include_folder_urls and not ids:
            continue
        selected.append(resource)
    return selected


def update_after_download(resource: dict[str, object], dest: Path) -> None:
    resource["migrated_at"] = date.today().isoformat()
    resource["size_bytes"] = path_size(dest) if dest.exists() else None
    if dest.is_file():
        resource["checksum_sha256"] = sha256_file(dest)
    notes = str(resource.get("notes", ""))
    marker = f"Downloaded directly to OneDrive path `{dest.relative_to(ONEDRIVE_ROOT)}`."
    resource["notes"] = f"{notes} {marker}".strip() if marker not in notes else notes


def has_completed_payload(path: Path, resource: dict[str, object] | None = None) -> bool:
    min_bytes = 0
    if resource and str(resource.get("resource_type", "")) == "course_package":
        min_bytes = MIN_COURSE_PACKAGE_BYTES

    if path.is_file():
        return not path.name.endswith(".part") and path.stat().st_size >= min_bytes
    if not path.is_dir():
        return False
    for item in path.rglob("*"):
        if item.is_file() and not item.name.endswith(".part") and item.stat().st_size >= min_bytes:
            return True
    return False


def append_log(entries: list[tuple[str, Path, list[str]]], failures: list[tuple[str, Path, str]]) -> None:
    if not entries and not failures:
        return
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {date.today().isoformat()} external direct download\n\n")
        for rid, dest, cmd in entries:
            fh.write(f"- `{rid}` -> `{dest.relative_to(ONEDRIVE_ROOT)}` via `{' '.join(cmd)}`\n")
        if failures:
            fh.write("\nFailures:\n")
            for rid, dest, error in failures:
                fh.write(f"- `{rid}` -> `{dest.relative_to(ONEDRIVE_ROOT)}` failed: {error}\n")


def persist_progress(
    resources: list[dict[str, object]],
    entries: list[tuple[str, Path, list[str]]],
    failures: list[tuple[str, Path, str]],
) -> None:
    write_manifest(resources, MANIFEST_PATH)
    MANIFEST_COPY.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MANIFEST_PATH, MANIFEST_COPY)
    append_log(entries, failures)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resource_ids", nargs="*", help="Manifest resource ids to download. If omitted, downloads all external file URLs except shared folder URLs.")
    parser.add_argument("--execute", action="store_true", help="Actually run downloads. Without this flag, only print the plan.")
    parser.add_argument("--include-folder-urls", action="store_true", help="Include Google Drive folder URLs when no resource ids are specified.")
    parser.add_argument("--record-existing", action="store_true", help="Record already-downloaded OneDrive payloads in the manifest without downloading anything.")
    parser.add_argument("--retries", type=int, default=3, help="Number of attempts for each executed download.")
    parser.add_argument("--stop-on-error", action="store_true", help="Stop at the first failed download instead of continuing to later resources.")
    args = parser.parse_args()

    resources = read_manifest()
    selected = select_resources(resources, args.resource_ids, args.include_folder_urls)
    if not selected:
        print("No matching external resources selected.")
        return 0

    completed: list[tuple[str, Path, list[str]]] = []
    failures: list[tuple[str, Path, str]] = []

    if args.record_existing:
        for resource in selected:
            rid = str(resource["id"])
            dest = destination_for(resource)
            if has_completed_payload(dest, resource):
                update_after_download(resource, dest)
                completed.append((rid, dest, ["record-existing"]))
                print(f"RECORDED {rid}: {dest}")
            else:
                print(f"SKIP {rid}: no completed payload at {dest}")
        persist_progress(resources, completed, failures)
        return 0

    for resource in selected:
        rid = str(resource["id"])
        url = str(resource["original_source_url"])
        dest = destination_for(resource)
        if args.execute and has_completed_payload(dest, resource):
            update_after_download(resource, dest)
            entry = (rid, dest, ["already-present"])
            completed.append(entry)
            persist_progress(resources, [entry], [])
            print(f"SKIP {rid}: completed payload already exists at {dest}")
            continue
        attempts = max(1, args.retries if args.execute else 1)
        for attempt in range(1, attempts + 1):
            try:
                if is_google_drive(url):
                    cmd = run_google_download(url, dest, args.execute)
                else:
                    cmd = run_direct_download(url, dest, args.execute)
                print(f"{'EXEC' if args.execute else 'PLAN'} {rid}: {url} -> {dest}")
                print("  " + " ".join(cmd))
                if args.execute:
                    if not has_completed_payload(dest, resource):
                        raise RuntimeError(f"download finished without a valid completed payload at {dest}")
                    update_after_download(resource, dest)
                    entry = (rid, dest, cmd)
                    completed.append(entry)
                    persist_progress(resources, [entry], [])
                break
            except Exception as exc:
                message = str(exc)
                if attempt < attempts:
                    print(f"RETRY {rid}: attempt {attempt} failed: {message}", file=sys.stderr)
                    continue
                print(f"FAIL {rid}: {url} -> {dest}: {message}", file=sys.stderr)
                failure = (rid, dest, message)
                failures.append(failure)
                if args.execute:
                    persist_progress(resources, [], [failure])
                if args.stop_on_error:
                    break
        if failures and args.stop_on_error:
            break

    if args.execute:
        persist_progress(resources, [], [])

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
