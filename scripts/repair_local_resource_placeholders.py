#!/usr/bin/env python3
"""Repair known local OneDrive placeholder payloads from trusted local sources."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import ROOT, file_payload_issue

PLACEHOLDER_COPY_REPAIRS: list[tuple[str, str]] = []

HEAD_REPAIRS = [
    (
        "ZJE_Collection/IFBS2/Yue/IFBStheme34_tutorialquestion.pdf",
        "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_4_tutorial_questions.pdf",
    ),
    (
        "ZJE_Collection/MI2/Yue/MI（非完整）.pdf",
        "COURSES/Year2/MI2/Yue/MI2_Yue_incomplete_notes.pdf",
    ),
    (
        "ZJE_Collection/zip_contents/Yue/BaO（非完整）.pdf",
        "ARCHIVE/removed_from_website/zip_contents/Yue/BaO（非完整）.pdf",
    ),
    (
        "ZJE_Collection/zip_contents/Yue/IFBStheme34_tutorialquestion.pdf",
        "ARCHIVE/removed_from_website/zip_contents/Yue/IFBStheme34_tutorialquestion.pdf",
    ),
    (
        "ZJE_Collection/zip_contents/Yue/MI（非完整）.pdf",
        "ARCHIVE/removed_from_website/zip_contents/Yue/MI（非完整）.pdf",
    ),
]


def ensure_local_source(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)
    issue = file_payload_issue(path)
    if issue:
        raise RuntimeError(f"source is not locally usable: {path} ({issue})")


def write_bytes(path: Path, content: bytes, *, execute: bool) -> None:
    if not execute:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.repair.tmp")
    try:
        temp.write_bytes(content)
        validate_file(temp)
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


def restore_from_head(git_path: str, dest: Path, *, execute: bool) -> str:
    completed = subprocess.run(
        ["git", "show", f"HEAD:{git_path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    content = completed.stdout
    if not content:
        raise RuntimeError(f"HEAD object is empty: {git_path}")
    write_bytes(dest, content, execute=execute)
    return f"HEAD:{git_path}"


def copy_repair(src: Path, dest: Path, *, execute: bool) -> str:
    ensure_local_source(src)
    if execute:
        write_bytes(dest, src.read_bytes(), execute=True)
    return src.relative_to(ONEDRIVE_ROOT).as_posix()


def validate_file(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(path)
    issue = file_payload_issue(path)
    if issue:
        raise RuntimeError(f"file still has payload issue: {path} ({issue})")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Write repaired files into the local OneDrive tree.")
    args = parser.parse_args()

    repaired: list[tuple[str, str]] = []
    for source_rel, dest_rel in PLACEHOLDER_COPY_REPAIRS:
        dest = ONEDRIVE_ROOT / dest_rel
        source_label = copy_repair(ONEDRIVE_ROOT / source_rel, dest, execute=args.execute)
        if args.execute:
            validate_file(dest)
        repaired.append((dest_rel, source_label))
        print(f"{'REPAIRED' if args.execute else 'PLAN'} {dest_rel} <- {source_label}", flush=True)

    for git_path, dest_rel in HEAD_REPAIRS:
        dest = ONEDRIVE_ROOT / dest_rel
        source_label = restore_from_head(git_path, dest, execute=args.execute)
        if args.execute:
            validate_file(dest)
        repaired.append((dest_rel, source_label))
        print(f"{'REPAIRED' if args.execute else 'PLAN'} {dest_rel} <- {source_label}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
