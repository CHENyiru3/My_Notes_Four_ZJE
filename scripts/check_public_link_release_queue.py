#!/usr/bin/env python3
"""Preflight-check filled rows in the public OneDrive link release queue."""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import REPORT_DIR, is_public_onedrive_url, payload_integrity_issues, read_manifest

DEFAULT_QUEUE = REPORT_DIR / "public_link_release_queue.csv"
REQUIRED_COLUMNS = {"id", "public_url_to_fill", "public_link_released_at_to_fill"}


@dataclass(frozen=True)
class QueueUpdate:
    row_number: int
    rid: str
    url: str
    released_at: str


def valid_release_date(value: str) -> bool:
    parts = value.split("-")
    if len(parts) != 3:
        return False
    try:
        year, month, day = (int(part) for part in parts)
        date(year, month, day)
    except ValueError:
        return False
    return True


def payload_errors(resource: dict[str, object]) -> list[str]:
    path = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
    errors: list[str] = []
    for issue_path, issue in payload_integrity_issues(path):
        if issue_path == path:
            errors.append(f"{issue}: {resource['local_onedrive_path']}")
        else:
            errors.append(f"{issue}: {issue_path.relative_to(ONEDRIVE_ROOT).as_posix()}")
    return errors


def collect_queue_updates(
    queue_path: Path,
    resources: list[dict[str, object]],
    *,
    allow_released: bool = False,
) -> tuple[list[QueueUpdate], list[str]]:
    errors: list[str] = []
    updates: list[QueueUpdate] = []
    by_id = {str(resource["id"]): resource for resource in resources}
    seen_ids: dict[str, int] = {}
    seen_urls: dict[str, str] = {}
    existing_released_urls = {
        str(resource.get("public_url", "")).strip(): str(resource["id"])
        for resource in resources
        if str(resource.get("public_url_status", "")) == "released"
        and str(resource.get("public_url", "")).strip()
    }

    if not queue_path.exists():
        return [], [f"missing queue CSV: {queue_path}"]

    with queue_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = set(reader.fieldnames or [])
        missing_columns = sorted(REQUIRED_COLUMNS - fieldnames)
        if missing_columns:
            return [], [f"{queue_path}: missing required column(s): {', '.join(missing_columns)}"]

        for row_number, row in enumerate(reader, start=2):
            rid = (row.get("id") or "").strip()
            url = (row.get("public_url_to_fill") or "").strip()
            released_at = (row.get("public_link_released_at_to_fill") or "").strip()
            if not url:
                continue

            if not rid:
                errors.append(f"row {row_number}: public_url_to_fill is set but id is empty")
                continue
            if rid not in by_id:
                errors.append(f"row {row_number}: unknown resource id {rid!r}")
                continue
            if rid in seen_ids:
                errors.append(f"row {row_number} {rid}: duplicate filled queue row; first seen on row {seen_ids[rid]}")
                continue
            seen_ids[rid] = row_number

            resource = by_id[rid]
            status = str(resource.get("public_url_status", ""))
            if status == "retired":
                errors.append(f"row {row_number} {rid}: retired resources cannot be released")
                continue
            if status == "released" and not allow_released:
                errors.append(f"row {row_number} {rid}: resource is already released; use --allow-released to replace the link")
                continue
            if status != "pending" and not (status == "released" and allow_released):
                errors.append(f"row {row_number} {rid}: resource status is {status!r}, expected 'pending'")
                continue
            local_payload_errors = payload_errors(resource)
            if local_payload_errors:
                errors.append(f"row {row_number} {rid}: OneDrive payload is unavailable ({local_payload_errors[0]})")
                continue
            if not is_public_onedrive_url(url):
                errors.append(f"row {row_number} {rid}: public URL must be a public OneDrive/SharePoint URL")
                continue
            if url in seen_urls and seen_urls[url] != rid:
                errors.append(f"row {row_number} {rid}: public URL duplicates queue row for {seen_urls[url]}")
                continue
            seen_urls[url] = rid
            existing_url_owner = existing_released_urls.get(url)
            if existing_url_owner and existing_url_owner != rid:
                errors.append(f"row {row_number} {rid}: public URL is already used by released resource {existing_url_owner}")
                continue
            if not released_at:
                released_at = date.today().isoformat()
            if not valid_release_date(released_at):
                errors.append(f"row {row_number} {rid}: release date must use YYYY-MM-DD")
                continue
            updates.append(QueueUpdate(row_number=row_number, rid=rid, url=url, released_at=released_at))

    return updates, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, default=DEFAULT_QUEUE, help="CSV queue to validate.")
    parser.add_argument("--require-filled", action="store_true", help="Fail if no public_url_to_fill values are present.")
    parser.add_argument("--allow-released", action="store_true", help="Allow filled rows to replace already released links.")
    args = parser.parse_args()

    resources = read_manifest()
    updates, errors = collect_queue_updates(
        args.queue,
        resources,
        allow_released=args.allow_released,
    )
    if args.require_filled and not updates and not errors:
        errors.append(f"no filled public_url_to_fill values found in {args.queue}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Public link release queue OK: {len(updates)} filled row(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
