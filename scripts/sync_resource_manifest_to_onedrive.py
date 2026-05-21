#!/usr/bin/env python3
"""Copy the repository resource manifest into OneDrive MANIFESTS.

Run this after repo-side manifest edits are reviewed. The script also exports a
small CSV copy for manual OneDrive/share-link workflows.
"""

from __future__ import annotations

import csv
import shutil
from datetime import date
from pathlib import Path

from resource_manifest import MANIFEST_PATH, read_manifest

ONEDRIVE_ROOT = Path("/Users/eric_yiru/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource")
MANIFESTS_DIR = ONEDRIVE_ROOT / "MANIFESTS"


def inside_onedrive(path: Path) -> Path:
    root = ONEDRIVE_ROOT.resolve(strict=False)
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Refusing to write outside ZJE_resource: {path}") from exc
    return resolved


def main() -> None:
    resources = read_manifest()
    manifests_dir = inside_onedrive(MANIFESTS_DIR)
    manifests_dir.mkdir(parents=True, exist_ok=True)

    manifest_copy = inside_onedrive(manifests_dir / "resource_manifest.yml")
    shutil.copy2(MANIFEST_PATH, manifest_copy)

    csv_path = inside_onedrive(manifests_dir / "resource_manifest.csv")
    fieldnames = [
        "id",
        "title",
        "course",
        "contributor",
        "resource_type",
        "release_tier",
        "storage_provider",
        "public_url_status",
        "local_onedrive_path",
        "resource_repo_path",
        "public_url",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for resource in resources:
            writer.writerow({key: resource.get(key, "") for key in fieldnames})

    log_path = inside_onedrive(manifests_dir / "migration_log.md")
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {date.today().isoformat()} manifest sync\n\n")
        fh.write("- Synced repository `ZJE_Collection/resources/resource_manifest.yml` into OneDrive `MANIFESTS/resource_manifest.yml`.\n")
        fh.write("- Exported OneDrive `MANIFESTS/resource_manifest.csv` for release workflow review.\n")

    release_log = inside_onedrive(manifests_dir / "public_link_release_log.md")
    if not release_log.exists():
        release_log.write_text("# Public Link Release Log\n\n", encoding="utf-8")

    print("Synced resource manifest and CSV into OneDrive MANIFESTS.")


if __name__ == "__main__":
    main()
