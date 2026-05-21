#!/usr/bin/env python3
"""Generate maintainer queue files for OneDrive public-link release."""

from __future__ import annotations

import csv
from collections import Counter

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT, resolve_bundle_members
from resource_manifest import REPORT_DIR, payload_integrity_issues, read_manifest


def payload_state(resource: dict[str, object], resources: list[dict[str, object]]) -> str:
    if resource["public_url_status"] == "retired":
        return "retired"
    path = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
    issues = payload_integrity_issues(path)
    if not issues:
        return "ready for review"
    if not any(issue_path == path and issue == "missing" for issue_path, issue in issues):
        return "payload unavailable"
    if resource["resource_type"] == "folder_bundle":
        members, missing = resolve_bundle_members(resource, resources)
        if missing:
            return "source files required"
        if members:
            return "ready to materialize"
    return "payload missing"


def main() -> None:
    resources = read_manifest()
    rows: list[dict[str, str]] = []
    for resource in resources:
        if resource["public_url_status"] == "retired":
            continue
        state = payload_state(resource, resources)
        action = "paste public URL"
        if state == "ready to materialize":
            action = "materialize folder bundle before sharing"
        elif state == "source files required":
            action = "supply source files before sharing"
        elif state == "payload missing":
            action = "restore payload before sharing"
        elif state == "payload unavailable":
            action = "hydrate or restore local payload before sharing"
        elif resource["public_url_status"] == "released":
            action = "released"
        rows.append(
            {
                "id": str(resource["id"]),
                "title": str(resource["title"]),
                "course": str(resource["course"]),
                "contributor": str(resource["contributor"]),
                "resource_type": str(resource["resource_type"]),
                "release_tier": str(resource.get("release_tier", "core")),
                "public_url_status": str(resource["public_url_status"]),
                "visibility": str(resource["visibility"]),
                "payload_state": state,
                "local_onedrive_path": str(resource["local_onedrive_path"]),
                "public_url_to_fill": "",
                "public_link_released_at_to_fill": "",
                "next_action": action,
            }
        )

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = REPORT_DIR / "public_link_release_queue.csv"
    fieldnames = [
        "id",
        "title",
        "course",
        "contributor",
        "resource_type",
        "release_tier",
        "public_url_status",
        "visibility",
        "payload_state",
        "local_onedrive_path",
        "public_url_to_fill",
        "public_link_released_at_to_fill",
        "next_action",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    status_counts = Counter(row["public_url_status"] for row in rows)
    tier_counts = Counter(row["release_tier"] for row in rows)
    payload_counts = Counter(row["payload_state"] for row in rows)
    lines = [
        "# Public Link Release Queue",
        "",
        "This maintainer-facing queue is generated from the resource manifest and local OneDrive payload state.",
        "",
        "Paste OneDrive or SharePoint share links into `public_link_release_queue.csv`, then run `python3 scripts/check_public_link_release_queue.py --require-filled` before `python3 scripts/apply_public_link_release_queue.py --execute`. The helpers validate Microsoft share-link hosts, stale or duplicate rows, release dates, and local OneDrive payload presence. Executed runs update the manifest, write `public_link_release_results.*`, and append to the OneDrive `MANIFESTS/public_link_release_log.md`.",
        "",
        "Before either release path, run the local release workflow self-test:",
        "",
        "```bash",
        "python3 scripts/self_test_resource_release.py",
        "```",
        "",
        "Manual queue release after pasting links:",
        "",
        "```bash",
        "python3 scripts/check_public_link_release_queue.py --require-filled",
        "python3 scripts/apply_public_link_release_queue.py --execute",
        "python3 scripts/generate_resource_pages.py",
        "python3 scripts/sync_resource_manifest_to_onedrive.py",
        "```",
        "",
        "Optional CLI path: use `scripts/create_onedrive_share_links.py --discover-context` with an existing Microsoft Entra app id. The helper reads local OneDrive sync metadata for the SharePoint `webUrl` and server-relative `ZJE_resource` root. It does not create app registrations; it only runs `m365 login --ensure --appId ...` when `--login` is supplied. Dry runs print commands only by default. Executed runs checkpoint local-only `public_link_release_results.*` and the manifest after each processed item, then append released links to the OneDrive `MANIFESTS/public_link_release_log.md`. If an executed run partially fails, rerun with `--all`; released resources are skipped unless `--include-released` is supplied.",
        "",
        "Example dry run:",
        "",
        "```bash",
        "python3 scripts/discover_onedrive_release_context.py",
        "python3 scripts/create_onedrive_share_links.py --discover-context --all --preflight-only",
        "python3 scripts/create_onedrive_share_links.py \\",
        "  --discover-context \\",
        "  --ids bg2-yiru-calculation-c4ec76cf",
        "```",
        "",
        "Example executed run after maintainer review:",
        "",
        "```bash",
        "python3 scripts/create_onedrive_share_links.py --discover-context --all --preflight-only",
        "python3 scripts/create_onedrive_share_links.py \\",
        "  --discover-context \\",
        "  --ids bg2-yiru-calculation-c4ec76cf \\",
        "  --login --app-id '<existing-entra-app-id>' \\",
        "  --execute --update-manifest",
        "python3 scripts/finalize_resource_release.py --sync-onedrive-manifest",
        "```",
        "",
        "## Summary",
        "",
        "| Public URL Status | Count |",
        "|---|---:|",
    ]
    for status in ["released", "pending", "private", "unavailable", "broken"]:
        lines.append(f"| {status} | {status_counts.get(status, 0)} |")
    lines.extend(["", "| Release Tier | Count |", "|---|---:|"])
    for tier in ["core", "large_archive"]:
        lines.append(f"| {tier} | {tier_counts.get(tier, 0)} |")
    lines.extend(["", "| Payload State | Count |", "|---|---:|"])
    for state in ["ready for review", "payload unavailable", "ready to materialize", "source files required", "payload missing"]:
        lines.append(f"| {state} | {payload_counts.get(state, 0)} |")

    lines.extend(
        [
            "",
            "## Queue",
            "",
            "| ID | Course | Contributor | Type | Tier | Payload State | Next Action |",
            "|---|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        lines.append(
            f"| `{row['id']}` | {row['course']} | {row['contributor']} | {row['resource_type']} | {row['release_tier']} | {row['payload_state']} | {row['next_action']} |"
        )

    md_path = REPORT_DIR / "public_link_release_queue.md"
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {md_path} and {csv_path}")


if __name__ == "__main__":
    main()
