#!/usr/bin/env python3
"""Hydrate cloud-only OneDrive payload files by reading them locally."""

from __future__ import annotations

import argparse
import signal
import sys
from pathlib import Path

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import file_payload_issue, read_manifest

CHUNK_SIZE = 1024 * 1024


class HydrationTimeout(RuntimeError):
    pass


def timeout_handler(signum: int, frame: object) -> None:
    raise HydrationTimeout("timed out while hydrating")


def payload_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return [item for item in path.rglob("*") if item.is_file()]
    return []


def hydrate_file(path: Path, *, execute: bool, timeout_seconds: int) -> str:
    issue = file_payload_issue(path)
    if issue != "cloud-only placeholder":
        return "ok" if issue is None else issue
    if not execute:
        return "would hydrate"

    old_handler = signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout_seconds)
    try:
        with path.open("rb") as fh:
            while fh.read(CHUNK_SIZE):
                pass
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)

    issue_after = file_payload_issue(path)
    return "hydrated" if issue_after is None else f"still {issue_after}"


def selected_resources(tier: str, resource_ids: list[str]) -> list[dict[str, object]]:
    resources = read_manifest()
    wanted = set(resource_ids)
    selected: list[dict[str, object]] = []
    for resource in resources:
        if str(resource.get("public_url_status")) == "retired":
            continue
        if wanted and str(resource["id"]) not in wanted:
            continue
        if not wanted and tier != "all" and str(resource.get("release_tier", "core")) != tier:
            continue
        selected.append(resource)
    missing = sorted(wanted - {str(resource["id"]) for resource in selected})
    if missing:
        raise ValueError(f"unknown or filtered resource ids: {', '.join(missing)}")
    return selected


def normalize_suffixes(values: list[str]) -> set[str]:
    suffixes: set[str] = set()
    for value in values:
        suffix = value.lower()
        if not suffix.startswith("."):
            suffix = f".{suffix}"
        suffixes.add(suffix)
    return suffixes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("resource_ids", nargs="*", help="Specific resource ids to hydrate.")
    parser.add_argument("--tier", choices=["core", "large_archive", "all"], default="core")
    parser.add_argument("--suffix", action="append", default=[], help="Only hydrate files with this suffix. Repeat for multiple suffixes.")
    parser.add_argument("--execute", action="store_true", help="Read cloud-only files to hydrate local data.")
    parser.add_argument("--timeout", type=int, default=120, help="Maximum seconds to spend on one file.")
    args = parser.parse_args()

    resources = selected_resources(args.tier, args.resource_ids)
    suffixes = normalize_suffixes(args.suffix)
    counts = {"ok": 0, "planned": 0, "hydrated": 0, "failed": 0}
    for resource in resources:
        payload_path = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
        for file_path in payload_files(payload_path):
            if suffixes and file_path.suffix.lower() not in suffixes:
                continue
            issue = file_payload_issue(file_path)
            if issue is None:
                counts["ok"] += 1
                continue
            rel = file_path.relative_to(ONEDRIVE_ROOT).as_posix()
            try:
                result = hydrate_file(file_path, execute=args.execute, timeout_seconds=args.timeout)
            except Exception as exc:
                counts["failed"] += 1
                print(f"FAILED {rel}: {exc}", flush=True)
                continue
            if result == "would hydrate":
                counts["planned"] += 1
                print(f"PLAN hydrate {rel}", flush=True)
            elif result == "hydrated":
                counts["hydrated"] += 1
                print(f"HYDRATED {rel}", flush=True)
            elif result == "ok":
                counts["ok"] += 1
            else:
                counts["failed"] += 1
                print(f"FAILED {rel}: {result}", flush=True)

    print(
        "Hydration summary: "
        f"ok={counts['ok']} planned={counts['planned']} hydrated={counts['hydrated']} failed={counts['failed']}"
    )
    return 1 if counts["failed"] else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
