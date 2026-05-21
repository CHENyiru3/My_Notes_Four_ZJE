#!/usr/bin/env python3
"""Check whether manifest payload paths exist in the local OneDrive tree."""

from __future__ import annotations

import sys
from pathlib import Path

from materialize_folder_bundles_to_onedrive import resolve_bundle_members
from resource_manifest import payload_integrity_issues, read_manifest

ONEDRIVE_ROOT = Path("/Users/eric_yiru/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource")


def main() -> int:
    zip_files = sorted(path.relative_to(ONEDRIVE_ROOT).as_posix() for path in ONEDRIVE_ROOT.rglob("*.zip"))
    missing: list[tuple[str, str, str]] = []
    unavailable: list[tuple[str, str, str, int, str]] = []
    ready_bundles: list[tuple[str, int]] = []
    source_required: list[tuple[str, int]] = []
    present = 0
    resources = read_manifest()
    for resource in resources:
        if resource["public_url_status"] == "retired":
            continue
        path = ONEDRIVE_ROOT / resource["local_onedrive_path"]
        issues = payload_integrity_issues(path)
        if not issues:
            present += 1
        else:
            if any(issue == "missing" and issue_path == path for issue_path, issue in issues):
                missing.append((resource["id"], resource["resource_type"], resource["local_onedrive_path"]))
            else:
                first_path, first_issue = issues[0]
                unavailable.append(
                    (
                        resource["id"],
                        resource["resource_type"],
                        resource["local_onedrive_path"],
                        len(issues),
                        first_path.relative_to(ONEDRIVE_ROOT).as_posix() + f" ({first_issue})",
                    )
                )
            if resource["resource_type"] == "folder_bundle" and any(issue == "missing" and issue_path == path for issue_path, issue in issues):
                members, missing_members = resolve_bundle_members(resource, resources)
                if missing_members:
                    source_required.append((resource["id"], len(missing_members)))
                elif members:
                    ready_bundles.append((resource["id"], len(members)))

    if missing or unavailable or zip_files:
        print(f"OneDrive payloads present: {present}")
        print(f"OneDrive payloads missing: {len(missing)}")
        print(f"OneDrive payloads unavailable: {len(unavailable)}")
        print(f"OneDrive ZIP files found: {len(zip_files)}")
        for rid, resource_type, path in missing:
            print(f"MISSING {rid} ({resource_type}): {path}")
        for rid, resource_type, path, count, first_issue in unavailable:
            print(f"UNAVAILABLE {rid} ({resource_type}): {path} [{count} issue(s); first: {first_issue}]")
        for path in zip_files:
            print(f"ZIP_FILE {path}")
        if ready_bundles:
            print("\nFolder bundles ready to materialize from available local sources:")
            for rid, count in ready_bundles:
                print(f"READY {rid}: {count} listed files")
        if source_required:
            print("\nFolder bundles requiring original source files:")
            for rid, count in source_required:
                print(f"SOURCE_REQUIRED {rid}: {count} missing listed files")
        return 1

    print(f"OneDrive payloads OK: {present} resources; no ZIP files found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
