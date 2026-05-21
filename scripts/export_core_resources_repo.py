#!/usr/bin/env python3
"""Export core ZJE resources into a separate GitHub-ready repository."""

from __future__ import annotations

import argparse
import csv
import shutil
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import MANIFEST_PATH, read_manifest, write_manifest

DEFAULT_TARGET = Path("/Users/eric_yiru/Desktop/Github/Awesome-ZJE")
RESOURCE_REPO_URL = "https://github.com/CHENyiru3/awesome_ZJE_resource"
RAW_BASE_URL = "https://raw.githubusercontent.com/CHENyiru3/awesome_ZJE_resource/main"
GITHUB_PAYLOAD_SUFFIXES = {".md", ".pdf"}
MAX_GIT_FILE_BYTES = 100 * 1024 * 1024
DEFAULT_COPY_TIMEOUT_SECONDS = 30


def repo_relative_payload_path(resource: dict[str, Any]) -> Path:
    return Path("resources") / str(resource["local_onedrive_path"])


def payload_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return [item for item in path.rglob("*") if item.is_file()]
    return []


def payload_label(payload_path: Path, file_path: Path) -> str:
    if payload_path.is_file():
        return file_path.name
    return file_path.relative_to(payload_path).as_posix()


def should_export_resource(resource: dict[str, Any]) -> bool:
    return (
        str(resource.get("public_url_status")) != "retired"
        and str(resource.get("release_tier", "core")) == "core"
    )


def file_is_allowed(path: Path) -> bool:
    if path.suffix.lower() not in GITHUB_PAYLOAD_SUFFIXES:
        return False
    stat = path.stat()
    if stat.st_size == 0:
        return False
    if stat.st_size >= MAX_GIT_FILE_BYTES:
        return False
    return True


def resource_export_issue(resource: dict[str, Any]) -> str | None:
    if not should_export_resource(resource):
        return "not a core public resource"
    payload_path = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
    files = payload_files(payload_path)
    if not files:
        return "payload missing or empty"
    for file_path in files:
        suffix = file_path.suffix.lower()
        if suffix not in GITHUB_PAYLOAD_SUFFIXES:
            return f"contains non-PDF/non-Markdown payload: {payload_label(payload_path, file_path)}"
        if file_path.stat().st_size == 0:
            return f"contains empty payload: {payload_label(payload_path, file_path)}"
        if file_path.stat().st_size >= MAX_GIT_FILE_BYTES:
            return f"contains file >= {MAX_GIT_FILE_BYTES} bytes: {payload_label(payload_path, file_path)}"
    return None


def github_exportable_resources(resources: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[tuple[str, str]]]:
    exported: list[dict[str, Any]] = []
    skipped: list[tuple[str, str]] = []
    for resource in resources:
        if not should_export_resource(resource):
            continue
        issue = resource_export_issue(resource)
        if issue:
            skipped.append((str(resource["id"]), issue))
        else:
            exported.append(resource)
    return exported, skipped


def existing_destination_matches(src: Path, dest: Path) -> bool:
    if not dest.exists() or not dest.is_file():
        return False
    if dest.stat().st_size != src.stat().st_size:
        return False
    return dest.stat().st_size > 0


def copy_one_file(src: Path, dest: Path, timeout_seconds: int) -> str:
    if not file_is_allowed(src):
        return "skipped"
    if existing_destination_matches(src, dest):
        return "existing"
    dest.parent.mkdir(parents=True, exist_ok=True)

    try:
        subprocess.run(["cp", "-p", str(src), str(dest)], check=True, timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        if dest.exists():
            dest.unlink()
        return "timeout"
    except subprocess.CalledProcessError:
        if dest.exists():
            dest.unlink()
        return "skipped"
    return "copied"


def copy_payload(src: Path, dest: Path, timeout_seconds: int, skipped_paths: list[str]) -> tuple[int, int, int]:
    copied = 0
    skipped = 0
    existing = 0
    if src.is_file():
        result = copy_one_file(src, dest, timeout_seconds)
        if result == "copied":
            copied += 1
        elif result == "existing":
            existing += 1
        else:
            skipped_paths.append(src.as_posix())
            skipped += 1
        return copied, skipped, existing

    for file_path in payload_files(src):
        rel = file_path.relative_to(src)
        target = dest / rel
        result = copy_one_file(file_path, target, timeout_seconds)
        if result == "copied":
            copied += 1
        elif result == "existing":
            existing += 1
        else:
            skipped_paths.append(file_path.as_posix())
            skipped += 1
    return copied, skipped, existing


def resource_raw_url(resource: dict[str, Any]) -> str:
    rel = repo_relative_payload_path(resource).as_posix()
    if str(resource.get("resource_type")) in {"course_package", "folder_bundle"}:
        return f"{RESOURCE_REPO_URL}/tree/main/{rel}"
    return f"{RAW_BASE_URL}/{rel}"


def exported_manifest(resources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    exported: list[dict[str, Any]] = []
    for resource in resources:
        if not should_export_resource(resource):
            continue
        row = dict(resource)
        row["storage_provider"] = "github"
        row["resource_repo"] = RESOURCE_REPO_URL
        row["resource_repo_path"] = repo_relative_payload_path(resource).as_posix()
        row["public_url"] = resource_raw_url(resource)
        row["public_url_status"] = "released"
        row["visibility"] = "public_after_review"
        row["public_link_released_at"] = date.today().isoformat()
        exported.append(row)
    return exported


def write_csv(path: Path, resources: list[dict[str, Any]]) -> None:
    fieldnames = [
        "id",
        "title",
        "course",
        "contributor",
        "resource_type",
        "release_tier",
        "size_bytes",
        "resource_repo_path",
        "public_url",
    ]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for resource in resources:
            writer.writerow({key: resource.get(key, "") for key in fieldnames})


def write_readme(target: Path, resources: list[dict[str, Any]], copied: int, skipped: int) -> None:
    counts = Counter(str(resource.get("resource_type")) for resource in resources)
    lines = [
        "# awesome_ZJE_resource",
        "",
        "Online resource database for ZJEr, working with the ZJE study website.",
        "",
        "This repository is intended to store GitHub-suitable PDF and Markdown resource payloads separately from the MkDocs website source. Non-PDF/non-Markdown payloads, large archives, OneNote `.one` files, Office documents, XMind bundles, ZIP files, and other large package formats stay in the school OneDrive release flow.",
        "",
        "## Export Summary",
        "",
        f"- Export date: {date.today().isoformat()}",
        f"- Core resources exported: {len(resources)}",
        f"- Files copied: {copied}",
        f"- Files skipped by policy: {skipped}",
        "",
        "## Resource Counts",
        "",
        "| Type | Count |",
        "|---|---:|",
    ]
    for resource_type in sorted(counts):
        lines.append(f"| {resource_type} | {counts[resource_type]} |")
    lines.extend(
        [
            "",
            "## Files",
            "",
            "- `resources/`: exported core payloads.",
            "- `metadata/resource_manifest.yml`: manifest for exported core resources.",
            "- `metadata/download_links.csv`: GitHub raw/tree links for website integration.",
            "- `metadata/skipped_files.txt`: resources skipped because they contain non-PDF/non-Markdown payloads, oversized files, or unavailable OneDrive placeholders.",
            "",
            "Only `.pdf` and `.md` payloads below 100 MiB are eligible for normal Git storage. Other resource formats are intentionally OneDrive-only.",
            "",
        ]
    )
    target.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def write_gitignore(target: Path) -> None:
    target.joinpath(".gitignore").write_text(
        "\n".join(
            [
                ".DS_Store",
                "__pycache__/",
                "*.tmp",
                "*.partial",
                "*.docx",
                "*.pptx",
                "*.xlsx",
                "*.one",
                "*.xmind",
                "*.zip",
                "",
            ]
        ),
        encoding="utf-8",
    )


def init_git(target: Path) -> None:
    if not target.joinpath(".git").exists():
        subprocess.run(["git", "init"], cwd=target, check=True)
    subprocess.run(["git", "branch", "-M", "main"], cwd=target, check=True)
    existing_remotes = subprocess.run(
        ["git", "remote"],
        cwd=target,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    if "origin" not in existing_remotes:
        subprocess.run(["git", "remote", "add", "origin", f"{RESOURCE_REPO_URL}.git"], cwd=target, check=True)


def remove_exported_payload(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def update_source_manifest(resources: list[dict[str, Any]], exported_ids: set[str]) -> None:
    released_at = date.today().isoformat()
    for resource in resources:
        if str(resource["id"]) not in exported_ids:
            continue
        resource["storage_provider"] = "github"
        resource["resource_repo"] = RESOURCE_REPO_URL
        resource["resource_repo_path"] = repo_relative_payload_path(resource).as_posix()
        resource["public_url"] = resource_raw_url(resource)
        resource["public_url_status"] = "released"
        resource["visibility"] = "public_after_review"
        resource["public_link_released_at"] = released_at
    write_manifest(resources, MANIFEST_PATH)


def clean_target(target: Path) -> None:
    for child_name in ["resources", "metadata"]:
        child = target / child_name
        if child.exists():
            shutil.rmtree(child)


def export(target: Path, *, execute: bool, force: bool, update_manifest: bool, copy_timeout: int, clean: bool) -> int:
    resources = read_manifest()
    core_resources, skipped_resources = github_exportable_resources(resources)
    target = target.expanduser()
    if target.exists() and any(target.iterdir()) and not force and not target.joinpath(".git").exists():
        print(f"target exists and is not empty; use --force after reviewing: {target}", file=sys.stderr)
        return 1
    if not execute:
        print(f"Would export {len(core_resources)} core resources to {target}")
        print(f"Would skip {len(skipped_resources)} core resources that are not GitHub-suitable")
        print(f"Would exclude {sum(1 for resource in resources if str(resource.get('release_tier')) == 'large_archive')} large archive resources")
        if clean:
            print("Would clean target resources/ and metadata/ before export")
        if update_manifest:
            print("Would update website manifest core resources to GitHub release URLs")
        return 0

    target.mkdir(parents=True, exist_ok=True)
    if clean:
        clean_target(target)
    target.joinpath("metadata").mkdir(parents=True, exist_ok=True)
    target.joinpath("resources").mkdir(parents=True, exist_ok=True)

    copied = 0
    skipped = 0
    existing = 0
    skipped_paths: list[str] = []
    copied_resources: list[dict[str, Any]] = []
    missing: list[str] = []
    for resource in core_resources:
        src = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
        dest = target / repo_relative_payload_path(resource)
        if not src.exists():
            missing.append(str(resource["id"]))
            continue
        copied_now, skipped_now, existing_now = copy_payload(src, dest, copy_timeout, skipped_paths)
        copied += copied_now
        skipped += skipped_now
        existing += existing_now
        if skipped_now:
            remove_exported_payload(dest)
            skipped_resources.append((str(resource["id"]), "one or more payload files could not be copied"))
        else:
            copied_resources.append(resource)

    if missing:
        print(f"Missing core payloads: {', '.join(missing)}", file=sys.stderr)
        return 1

    exported = exported_manifest(copied_resources)
    write_manifest(exported, target / "metadata" / "resource_manifest.yml")
    write_csv(target / "metadata" / "download_links.csv", exported)
    skipped_lines = [f"{rid}: {reason}" for rid, reason in skipped_resources]
    skipped_lines.extend(skipped_paths)
    target.joinpath("metadata", "skipped_files.txt").write_text(
        "\n".join(skipped_lines) + ("\n" if skipped_lines else ""),
        encoding="utf-8",
    )
    write_readme(target, exported, copied, skipped)
    write_gitignore(target)
    init_git(target)
    if update_manifest:
        update_source_manifest(resources, {str(resource["id"]) for resource in copied_resources})

    print(f"Exported {len(exported)} core resources to {target}")
    print(f"Copied files: {copied}; existing files: {existing}; skipped files: {skipped}")
    if update_manifest:
        print("Updated website manifest core resources to GitHub release URLs")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET, help="Target Awesome-ZJE repository path.")
    parser.add_argument("--execute", action="store_true", help="Copy resources and initialize the local repo.")
    parser.add_argument("--force", action="store_true", help="Allow exporting into an existing non-empty target directory.")
    parser.add_argument("--clean-target", action="store_true", help="Remove target resources/ and metadata/ before exporting.")
    parser.add_argument("--update-source-manifest", action="store_true", help="Mark core resources in the website manifest as released from Awesome-ZJE.")
    parser.add_argument("--copy-timeout", type=int, default=DEFAULT_COPY_TIMEOUT_SECONDS, help="Seconds before skipping a slow OneDrive-backed file copy.")
    args = parser.parse_args()
    return export(
        args.target,
        execute=args.execute,
        force=args.force,
        update_manifest=args.update_source_manifest,
        copy_timeout=args.copy_timeout,
        clean=args.clean_target,
    )


if __name__ == "__main__":
    sys.exit(main())
