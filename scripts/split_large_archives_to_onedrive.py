#!/usr/bin/env python3
"""Separate large archive resources into the OneDrive LARGE_ARCHIVES tier."""

from __future__ import annotations

import argparse
import csv
import shutil
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import MANIFEST_PATH, REPORT_DIR, read_manifest, write_manifest

LARGE_PREFIX = "LARGE_ARCHIVES/"
DEFAULT_THRESHOLD = 100 * 1024 * 1024
LARGE_SUFFIXES = {".one"}
REPORT_CSV = REPORT_DIR / "large_archive_split.csv"
REPORT_MD = REPORT_DIR / "large_archive_split.md"
MIGRATION_LOG = ONEDRIVE_ROOT / "MANIFESTS" / "migration_log.md"


@dataclass(frozen=True)
class SplitPlan:
    rid: str
    title: str
    course: str
    contributor: str
    current_tier: str
    target_tier: str
    current_path: str
    target_path: str
    size_bytes: int
    reason: str
    action: str


def inside_onedrive(path: Path) -> Path:
    root = ONEDRIVE_ROOT.resolve(strict=False)
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Refusing to write outside ZJE_resource: {path}") from exc
    return resolved


def payload_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return [item for item in path.rglob("*") if item.is_file()]
    return []


def logical_size(path: Path) -> int:
    return sum(item.stat().st_size for item in payload_files(path))


def contains_large_suffix(path: Path) -> str:
    suffixes = sorted({item.suffix.lower() for item in payload_files(path)})
    for suffix in suffixes:
        if suffix in LARGE_SUFFIXES:
            return suffix
    return ""


def target_path_for(current_path: str, target_tier: str) -> str:
    if target_tier != "large_archive":
        return current_path.removeprefix(LARGE_PREFIX)
    if current_path.startswith(LARGE_PREFIX):
        return current_path
    return f"{LARGE_PREFIX}{current_path}"


def classify(resource: dict[str, object], threshold: int) -> tuple[str, int, str]:
    status = str(resource.get("public_url_status", ""))
    resource_type = str(resource.get("resource_type", ""))
    if status == "retired" or resource_type == "retired_mirror":
        return "retired", int(resource.get("size_bytes") or 0), "retired"

    path = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
    manifest_size = int(resource.get("size_bytes") or 0)
    size = manifest_size or logical_size(path)
    large_suffix = contains_large_suffix(path)
    if large_suffix:
        return "large_archive", size, f"contains {large_suffix}"
    if size >= threshold:
        return "large_archive", size, f"size >= {threshold} bytes"
    return "core", size, "below large threshold"


def build_plan(resources: list[dict[str, object]], threshold: int) -> list[SplitPlan]:
    plans: list[SplitPlan] = []
    for resource in resources:
        target_tier, size, reason = classify(resource, threshold)
        current_tier = str(resource.get("release_tier", ""))
        current_path = str(resource.get("local_onedrive_path", ""))
        target_path = target_path_for(current_path, target_tier)
        if target_tier == "retired":
            target_path = current_path

        action_parts: list[str] = []
        if current_tier != target_tier:
            action_parts.append("update tier")
        if current_path != target_path:
            action_parts.append("move payload")
        action = ", ".join(action_parts) if action_parts else "none"
        plans.append(
            SplitPlan(
                rid=str(resource["id"]),
                title=str(resource["title"]),
                course=str(resource["course"]),
                contributor=str(resource["contributor"]),
                current_tier=current_tier,
                target_tier=target_tier,
                current_path=current_path,
                target_path=target_path,
                size_bytes=size,
                reason=reason,
                action=action,
            )
        )
    return plans


def write_report(plans: list[SplitPlan], executed: bool) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "title",
        "course",
        "contributor",
        "current_tier",
        "target_tier",
        "current_path",
        "target_path",
        "size_bytes",
        "reason",
        "action",
    ]
    with REPORT_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for plan in plans:
            writer.writerow(
                {
                    "id": plan.rid,
                    "title": plan.title,
                    "course": plan.course,
                    "contributor": plan.contributor,
                    "current_tier": plan.current_tier,
                    "target_tier": plan.target_tier,
                    "current_path": plan.current_path,
                    "target_path": plan.target_path,
                    "size_bytes": plan.size_bytes,
                    "reason": plan.reason,
                    "action": plan.action,
                }
            )

    counts: dict[str, int] = {}
    for plan in plans:
        counts[plan.target_tier] = counts.get(plan.target_tier, 0) + 1
    move_count = sum(1 for plan in plans if "move payload" in plan.action)
    lines = [
        "# Large Archive Split",
        "",
        f"Mode: {'executed' if executed else 'dry run'}",
        "",
        "| Target Tier | Count |",
        "|---|---:|",
    ]
    for tier in ["core", "large_archive", "retired"]:
        lines.append(f"| {tier} | {counts.get(tier, 0)} |")
    lines.extend(
        [
            "",
            f"Payload moves: {move_count}",
            "",
            "| ID | Course | Contributor | Target Tier | Size | Reason | Action |",
            "|---|---|---|---|---:|---|---|",
        ]
    )
    for plan in plans:
        if plan.action == "none":
            continue
        lines.append(
            f"| `{plan.rid}` | {plan.course} | {plan.contributor} | {plan.target_tier} | {plan.size_bytes} | {plan.reason} | {plan.action} |"
        )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate_plan(plans: list[SplitPlan]) -> list[str]:
    errors: list[str] = []
    target_paths: dict[str, str] = {}
    for plan in plans:
        if plan.target_path in target_paths and target_paths[plan.target_path] != plan.rid:
            errors.append(f"{plan.rid}: target path duplicates {target_paths[plan.target_path]}: {plan.target_path}")
        target_paths[plan.target_path] = plan.rid
        if plan.target_tier == "large_archive" and not plan.target_path.startswith(LARGE_PREFIX):
            errors.append(f"{plan.rid}: large archive target is not under {LARGE_PREFIX}")
        if plan.target_tier == "core" and plan.target_path.startswith(LARGE_PREFIX):
            errors.append(f"{plan.rid}: core target remains under {LARGE_PREFIX}")
    return errors


def execute_plan(resources: list[dict[str, object]], plans: list[SplitPlan]) -> None:
    by_id = {str(resource["id"]): resource for resource in resources}
    for plan in plans:
        resource = by_id[plan.rid]
        src = inside_onedrive(ONEDRIVE_ROOT / plan.current_path)
        dest = inside_onedrive(ONEDRIVE_ROOT / plan.target_path)
        if plan.current_path != plan.target_path:
            if src.exists():
                if dest.exists():
                    raise FileExistsError(f"{plan.rid}: destination already exists: {dest}")
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dest))
            elif not dest.exists():
                raise FileNotFoundError(f"{plan.rid}: missing payload at {src}")
        resource["release_tier"] = plan.target_tier
        resource["local_onedrive_path"] = plan.target_path

    write_manifest(resources, MANIFEST_PATH)
    MIGRATION_LOG.parent.mkdir(parents=True, exist_ok=True)
    with MIGRATION_LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {date.today().isoformat()} large archive split\n\n")
        for plan in plans:
            if plan.action == "none":
                continue
            fh.write(
                f"- `{plan.rid}` -> `{plan.target_tier}` at `{plan.target_path}` ({plan.reason}).\n"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Move payloads and update the manifest.")
    parser.add_argument("--threshold-bytes", type=int, default=DEFAULT_THRESHOLD, help="Logical size threshold for large archives.")
    args = parser.parse_args()

    resources = read_manifest()
    plans = build_plan(resources, args.threshold_bytes)
    errors = validate_plan(plans)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    write_report(plans, args.execute)
    if args.execute:
        execute_plan(resources, plans)
        write_report(plans, True)
        print(f"Executed large archive split; wrote {REPORT_MD} and {REPORT_CSV}")
    else:
        print(f"Dry run large archive split; wrote {REPORT_MD} and {REPORT_CSV}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
