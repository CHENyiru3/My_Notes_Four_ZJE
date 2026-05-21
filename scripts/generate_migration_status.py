#!/usr/bin/env python3
"""Generate a maintainer-facing migration status report."""

from __future__ import annotations

import filecmp
from collections import Counter

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT, resolve_bundle_members
from resource_manifest import DOCS_DIR, MANIFEST_PATH, REPORT_DIR, ROOT, payload_integrity_issues, read_manifest

MANIFEST_COPY = ONEDRIVE_ROOT / "MANIFESTS" / "resource_manifest.yml"
MKDOCS_PATH = ROOT / "mkdocs.yml"
BINARY_SUFFIXES = {".pdf", ".docx", ".pptx", ".xlsx", ".zip"}
PUBLIC_DOC_FORBIDDEN_TEXT = [
    "/Users/eric_yiru/",
    "OneDrive-InternationalCampus",
    "ZJE_resource",
    "ZJE_Collection/resources/resource_manifest.yml",
    "original_source_url",
    "local_onedrive_path",
    "drive.google.com",
    "docs.google.com",
]


def repo_binary_count() -> int:
    return sum(1 for path in DOCS_DIR.rglob("*") if path.is_file() and path.suffix.lower() in BINARY_SUFFIXES)


def onedrive_zip_count() -> int:
    if not ONEDRIVE_ROOT.exists():
        return 0
    return sum(1 for path in ONEDRIVE_ROOT.rglob("*.zip") if path.is_file())


def text_policy_hits() -> list[str]:
    hits: list[str] = []
    for path in DOCS_DIR.rglob("*"):
        if path == MANIFEST_PATH:
            continue
        if not path.is_file() or path.suffix.lower() not in {".md", ".txt", ".csv", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        matched = [needle for needle in PUBLIC_DOC_FORBIDDEN_TEXT if needle in text]
        if matched:
            hits.append(f"{path.relative_to(DOCS_DIR.parent).as_posix()} ({', '.join(matched)})")
    return hits


def mkdocs_excludes_manifest() -> bool:
    if not MKDOCS_PATH.exists():
        return False
    text = MKDOCS_PATH.read_text(encoding="utf-8")
    return "exclude_docs:" in text and "resources/resource_manifest.yml" in text


def payload_state(resources: list[dict[str, object]]) -> tuple[int, list[dict[str, object]], list[tuple[dict[str, object], list[tuple[object, str]]]], Counter[str]]:
    present = 0
    missing: list[dict[str, object]] = []
    unavailable: list[tuple[dict[str, object], list[tuple[object, str]]]] = []
    bundle_counts: Counter[str] = Counter()
    for resource in resources:
        if resource["public_url_status"] == "retired":
            continue
        path = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
        issues = payload_integrity_issues(path)
        missing_payload_path = any(issue_path == path and issue == "missing" for issue_path, issue in issues)
        if not issues:
            present += 1
            if resource["resource_type"] == "folder_bundle":
                bundle_counts["present"] += 1
            continue
        if not missing_payload_path:
            unavailable.append((resource, issues))
            if resource["resource_type"] == "folder_bundle":
                bundle_counts["unavailable"] += 1
            continue
        missing.append(resource)
        if resource["resource_type"] == "folder_bundle":
            members, missing_members = resolve_bundle_members(resource, resources)
            if missing_members:
                bundle_counts["source files required"] += 1
            elif members:
                bundle_counts["ready to materialize"] += 1
            else:
                bundle_counts["no listed files"] += 1
    return present, missing, unavailable, bundle_counts


def yes_no(value: bool) -> str:
    return "yes" if value else "no"


def main() -> None:
    resources = read_manifest()
    status_counts = Counter(str(resource["public_url_status"]) for resource in resources)
    type_counts = Counter(str(resource["resource_type"]) for resource in resources)
    tier_counts = Counter(str(resource.get("release_tier", "core")) for resource in resources)
    present_payloads, missing_payloads, unavailable_payloads, bundle_counts = payload_state(resources)
    public_docs_hits = text_policy_hits()
    manifest_copy_exists = MANIFEST_COPY.exists()
    manifest_copy_synced = (
        manifest_copy_exists and filecmp.cmp(MANIFEST_PATH, MANIFEST_COPY, shallow=False)
    )
    manifest_excluded = mkdocs_excludes_manifest()
    remaining_actions: list[str] = []
    if not manifest_excluded:
        remaining_actions.append(
            "Exclude `resources/resource_manifest.yml` from MkDocs public output before deploying the site."
        )
    if not manifest_copy_synced:
        remaining_actions.append(
            "Sync the repo manifest into OneDrive with `python3 scripts/sync_resource_manifest_to_onedrive.py` after repo-side changes are accepted."
        )
    ready_count = bundle_counts.get("ready to materialize", 0)
    if ready_count:
        remaining_actions.append(
            f"Materialize the {ready_count} ready folder bundles into OneDrive using `python3 scripts/materialize_folder_bundles_to_onedrive.py --execute` from an environment that can write to the OneDrive sync tree."
        )
    source_required_count = bundle_counts.get("source files required", 0)
    if source_required_count:
        remaining_actions.append(
            f"Supply or directly download the {source_required_count} source-required folder bundles into their manifest paths."
        )
    if unavailable_payloads:
        remaining_actions.append(
            f"Hydrate or restore the {len(unavailable_payloads)} OneDrive payloads that are empty or cloud-only placeholders before release."
        )
    pending_count = status_counts.get("pending", 0)
    if pending_count:
        remaining_actions.append(
            "Run `python3 scripts/self_test_resource_release.py`, review the pending resources, then either paste OneDrive share links into `public_link_release_queue.csv` and run `python3 scripts/apply_public_link_release_queue.py --execute`, or run `python3 scripts/create_onedrive_share_links.py --discover-context --all --preflight-only` followed by an executed `scripts/create_onedrive_share_links.py --discover-context` run with an existing Microsoft Entra app id. Finish with `python3 scripts/finalize_resource_release.py --sync-onedrive-manifest`."
        )

    lines = [
        "# Resource Migration Status",
        "",
        "This maintainer-facing report is generated from the current repository and local OneDrive sync state.",
        "",
        "Run `python3 scripts/generate_migration_status.py` after changing the manifest, generated pages, or OneDrive payloads.",
        "",
        "## Summary",
        "",
        "| Check | State |",
        "|---|---|",
        f"| Repository binaries under `ZJE_Collection` | {repo_binary_count()} |",
        f"| Public docs with internal migration/storage text | {len(public_docs_hits)} |",
        f"| MkDocs excludes repo manifest from public site | {yes_no(manifest_excluded)} |",
        f"| OneDrive manifest copy exists | {yes_no(manifest_copy_exists)} |",
        f"| OneDrive manifest copy matches repo manifest | {yes_no(manifest_copy_synced)} |",
        f"| Non-retired OneDrive payloads present | {present_payloads} |",
        f"| Non-retired OneDrive payloads missing | {len(missing_payloads)} |",
        f"| Non-retired OneDrive payloads unavailable | {len(unavailable_payloads)} |",
        f"| ZIP files under `ZJE_resource` | {onedrive_zip_count()} |",
        "",
        "## Resource Counts",
        "",
        "| Type | Count |",
        "|---|---:|",
    ]
    for resource_type in sorted(type_counts):
        lines.append(f"| {resource_type} | {type_counts[resource_type]} |")

    lines.extend(["", "## Release Tiers", "", "| Tier | Count |", "|---|---:|"])
    for tier in ["core", "large_archive", "retired"]:
        lines.append(f"| {tier} | {tier_counts.get(tier, 0)} |")

    lines.extend(["", "## Public URL Status", "", "| Status | Count |", "|---|---:|"])
    for status in ["released", "pending", "private", "unavailable", "broken", "retired"]:
        lines.append(f"| {status} | {status_counts.get(status, 0)} |")

    lines.extend(["", "## Folder Bundle Payloads", "", "| State | Count |", "|---|---:|"])
    for state in ["present", "unavailable", "ready to materialize", "source files required", "no listed files"]:
        lines.append(f"| {state} | {bundle_counts.get(state, 0)} |")

    if unavailable_payloads:
        lines.extend(["", "## Unavailable Payloads", "", "| ID | Issue Count | First Issue |", "|---|---:|---|"])
        for resource, issues in unavailable_payloads:
            first_path, first_issue = issues[0]
            try:
                first_label = first_path.relative_to(ONEDRIVE_ROOT).as_posix()
            except ValueError:
                first_label = str(first_path)
            lines.append(f"| `{resource['id']}` | {len(issues)} | {first_label} ({first_issue}) |")

    lines.extend(["", "## Remaining External Actions", ""])
    if remaining_actions:
        for index, action in enumerate(remaining_actions, start=1):
            lines.append(f"{index}. {action}")
    else:
        lines.append("No external migration actions remain.")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORT_DIR / "migration_status.md"
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()
