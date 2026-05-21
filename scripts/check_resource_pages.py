#!/usr/bin/env python3
"""Validate generated public resource pages against the manifest."""

from __future__ import annotations

import csv
import sys

from resource_manifest import DOCS_DIR, RESOURCE_DIR, is_public_resource_url, read_manifest
from generate_resource_pages import markdown_url

DOWNLOAD_CSV = RESOURCE_DIR / "download_links.csv"
DOWNLOAD_INDEX = RESOURCE_DIR / "index.md"
PACKAGE_INDEX = DOCS_DIR / "ZIPS_INDEX.md"
PUBLIC_PAGE_FORBIDDEN_TEXT = [
    "original_source_url",
    "local_onedrive_path",
    "drive.google.com",
    "docs.google.com",
    "OneDrive-InternationalCampus",
    "/Users/eric_yiru",
    "OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource",
    "ZJE_Collection/resources/resource_manifest.yml",
]


def read_csv_rows() -> list[dict[str, str]]:
    with DOWNLOAD_CSV.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    errors: list[str] = []
    resources = read_manifest()
    by_id = {str(resource["id"]): resource for resource in resources}
    released = {
        str(resource["id"]): resource
        for resource in resources
        if resource["public_url_status"] == "released"
    }
    released_packages = {
        rid: resource
        for rid, resource in released.items()
        if resource["resource_type"] in {"course_package", "folder_bundle"}
    }

    if not DOWNLOAD_CSV.exists():
        errors.append(f"missing generated file: {DOWNLOAD_CSV}")
        rows: list[dict[str, str]] = []
    else:
        rows = read_csv_rows()

    csv_ids = {row.get("id", "") for row in rows}
    if csv_ids != set(released):
        missing = sorted(set(released) - csv_ids)
        extra = sorted(csv_ids - set(released))
        if missing:
            errors.append(f"download_links.csv missing released resources: {missing}")
        if extra:
            errors.append(f"download_links.csv contains non-released resources: {extra}")

    for row in rows:
        rid = row.get("id", "")
        resource = by_id.get(rid)
        if not resource:
            errors.append(f"download_links.csv contains unknown resource id: {rid}")
            continue
        if row.get("public_url_status") != "released":
            errors.append(f"{rid}: download_links.csv row is not marked released")
        if not is_public_resource_url(row.get("public_url", "")):
            errors.append(f"{rid}: download_links.csv public_url is not an approved public resource URL")
        for field in ["title", "course", "contributor", "resource_type", "release_tier"]:
            if row.get(field, "") != str(resource.get(field, "")):
                errors.append(f"{rid}: download_links.csv field {field!r} does not match manifest")

    for path in [DOWNLOAD_INDEX, PACKAGE_INDEX]:
        if not path.exists():
            errors.append(f"missing generated file: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        for needle in PUBLIC_PAGE_FORBIDDEN_TEXT:
            if needle in text:
                errors.append(f"{path}: forbidden public text {needle!r}")
        for rid, resource in released.items():
            url = str(resource["public_url"])
            if url and path == DOWNLOAD_INDEX and url not in text and markdown_url(url) not in text:
                errors.append(f"{path}: missing released resource URL for {rid}")
        for rid, resource in released_packages.items():
            url = str(resource["public_url"])
            if url and path == PACKAGE_INDEX and url not in text and markdown_url(url) not in text:
                errors.append(f"{path}: missing released package URL for {rid}")

    if not released:
        text = DOWNLOAD_INDEX.read_text(encoding="utf-8") if DOWNLOAD_INDEX.exists() else ""
        if "## Resource Catalog" not in text or "| Resource | Course | Contributor | Type | Tier | GitHub | OneDrive |" not in text:
            errors.append("resources/index.md must show the route-based resource catalog")
        package_text = PACKAGE_INDEX.read_text(encoding="utf-8") if PACKAGE_INDEX.exists() else ""
        if "No active packages yet" not in package_text:
            errors.append("ZIPS_INDEX.md must show the empty package state")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Resource pages OK: {len(released)} released resources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
