#!/usr/bin/env python3
"""Copy local repo binaries into the OneDrive ZJE_resource tree."""

from __future__ import annotations

import csv
import shutil
from datetime import date
from pathlib import Path

from resource_manifest import MANIFEST_PATH, ROOT, read_manifest, write_manifest

ONEDRIVE_ROOT = Path("/Users/eric_yiru/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource")
COPY_TYPES = {"individual_file", "retired_mirror"}

SKELETON_DIRS = [
    "MANIFESTS",
    "COURSES/Year1/CHEM1",
    "COURSES/Year1/IBI1",
    "COURSES/Year1/IBMS1",
    "COURSES/Year1/ICMB1",
    "COURSES/Year1/MATH1",
    "COURSES/Year2/ADS2",
    "COURSES/Year2/BG2",
    "COURSES/Year2/BaO2",
    "COURSES/Year2/DST2",
    "COURSES/Year2/GP2",
    "COURSES/Year2/IFBS2",
    "COURSES/Year2/MI2",
    "COURSES/Year3/BMI3",
    "COURSES/Year3/CBSB3",
    "COURSES/Year3/IBMS3",
    "COURSES/Year3/IN3_full",
    "COURSES/Year3/MBE3",
    "COURSES/Year3/PoN3",
    "COURSES/Year4/BIA4",
    "COURSES/Year4/IBMS4",
    "COURSES/Year4/IID_4",
    "COURSES/Resources/Code_Cheatsheet",
    "INCOMING/unsorted",
    "INCOMING/checked",
    "INCOMING/rejected",
    "ARCHIVE/by_date",
    "ARCHIVE/by_contributor",
    "ARCHIVE/removed_from_website",
    "IMAGES/active",
    "IMAGES/pending_review",
    "PRIVATE",
]


def ensure_skeleton() -> None:
    for rel in SKELETON_DIRS:
        (ONEDRIVE_ROOT / rel).mkdir(parents=True, exist_ok=True)


def main() -> None:
    ensure_skeleton()
    resources = read_manifest()
    copied: list[dict[str, str]] = []

    for resource in resources:
        if resource["resource_type"] not in COPY_TYPES:
            continue
        source = resource.get("original_repo_path")
        if not source:
            continue
        src = ROOT / source
        if not src.exists():
            raise FileNotFoundError(src)
        dest = ONEDRIVE_ROOT / resource["local_onedrive_path"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
        resource["migrated_at"] = date.today().isoformat()
        copied.append(
            {
                "id": resource["id"],
                "source": source,
                "destination": resource["local_onedrive_path"],
                "size_bytes": str(dest.stat().st_size),
            }
        )

    manifests_dir = ONEDRIVE_ROOT / "MANIFESTS"
    manifests_dir.mkdir(parents=True, exist_ok=True)
    write_manifest(resources, MANIFEST_PATH)
    shutil.copy2(MANIFEST_PATH, manifests_dir / "resource_manifest.yml")

    log_path = manifests_dir / "migration_log.md"
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {date.today().isoformat()} local binary copy\n\n")
        for item in copied:
            fh.write(f"- `{item['source']}` -> `{item['destination']}` ({item['size_bytes']} bytes)\n")

    release_log = manifests_dir / "public_link_release_log.md"
    if not release_log.exists():
        release_log.write_text("# Public Link Release Log\n\n", encoding="utf-8")

    csv_path = manifests_dir / "resource_manifest.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        fieldnames = ["id", "title", "course", "contributor", "resource_type", "public_url_status", "local_onedrive_path", "public_url"]
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for resource in resources:
            writer.writerow({key: resource.get(key, "") for key in fieldnames})

    print(f"Copied {len(copied)} local binaries into {ONEDRIVE_ROOT}")


if __name__ == "__main__":
    main()
