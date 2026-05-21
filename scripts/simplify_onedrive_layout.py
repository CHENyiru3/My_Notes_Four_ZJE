#!/usr/bin/env python3
"""Rewrite manifest paths and recopy binaries into the simplified OneDrive layout."""

from __future__ import annotations

from migrate_local_binaries_to_onedrive import main as copy_binaries
from resource_manifest import MANIFEST_PATH, read_manifest, write_manifest


def simple_path(resource: dict) -> str:
    rtype = resource["resource_type"]
    title = resource["title"]
    if rtype == "course_package":
        slug = resource["id"].replace("-", "_")
        return f"COURSES/{resource['year_group']}/{resource['course']}/{resource['contributor']}/{slug}"
    if rtype == "folder_bundle":
        return f"COURSES/{resource['year_group']}/{resource['course']}/{resource['contributor']}/{title.removesuffix('.zip')}"
    if rtype == "retired_mirror":
        return f"ARCHIVE/removed_from_website/zip_contents/Yue/{title}"
    return f"COURSES/{resource['year_group']}/{resource['course']}/{resource['contributor']}/{title}"


def main() -> None:
    resources = read_manifest(MANIFEST_PATH)
    for resource in resources:
        resource["local_onedrive_path"] = simple_path(resource)
    write_manifest(resources, MANIFEST_PATH)
    copy_binaries()
    print("Simplified manifest paths and copied local binaries into the new OneDrive layout.")


if __name__ == "__main__":
    main()
