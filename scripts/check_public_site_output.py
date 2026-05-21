#!/usr/bin/env python3
"""Validate that built MkDocs output does not expose migration internals."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

FORBIDDEN_RELATIVE_FILES = [
    Path("resources/resource_manifest.yml"),
]
FORBIDDEN_TEXT = [
    "original_source_url",
    "local_onedrive_path",
    "drive.google.com",
    "docs.google.com",
    "OneDrive-InternationalCampus",
    "/Users/eric_yiru",
    "OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource",
    "ZJE_Collection/resources/resource_manifest.yml",
]
TEXT_SUFFIXES = {
    ".css",
    ".csv",
    ".html",
    ".js",
    ".json",
    ".md",
    ".txt",
    ".xml",
    ".yml",
}


def text_files(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"), help="Built MkDocs output directory.")
    args = parser.parse_args()

    site_dir = args.site_dir
    errors: list[str] = []
    if not site_dir.exists():
        errors.append(f"missing site directory: {site_dir}")
    else:
        for relative in FORBIDDEN_RELATIVE_FILES:
            path = site_dir / relative
            if path.exists():
                errors.append(f"forbidden published file: {path}")

        for path in text_files(site_dir):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for needle in FORBIDDEN_TEXT:
                if needle in text:
                    errors.append(f"forbidden public text {needle!r} in {path}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Public site output OK: {site_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
