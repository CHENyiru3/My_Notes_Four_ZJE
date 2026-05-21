#!/usr/bin/env python3
"""Generate a maintainer report for OneDrive folder-bundle payloads.

This report is intentionally local-maintainer oriented: it checks the local
OneDrive sync tree and classifies missing bundle folders by whether they can be
reconstructed from currently available Git Markdown plus already-migrated
OneDrive single files.
"""

from __future__ import annotations

from collections import Counter

from materialize_folder_bundles_to_onedrive import (
    ONEDRIVE_ROOT,
    resolve_bundle_members,
)
from resource_manifest import REPORT_DIR, payload_integrity_issues, read_manifest


def status_for(resource: dict[str, object], resources: list[dict[str, object]]) -> tuple[str, int, int]:
    path = ONEDRIVE_ROOT / str(resource["local_onedrive_path"])
    if path.exists():
        file_count = sum(1 for item in path.rglob("*") if item.is_file()) if path.is_dir() else 1
        if payload_integrity_issues(path):
            return "unavailable", file_count, 0
        return "present", file_count, 0
    members, missing = resolve_bundle_members(resource, resources)
    if missing:
        return "source files required", len(members), len(missing)
    if members:
        return "ready to materialize", len(members), 0
    return "no listed files", 0, 0


def main() -> None:
    resources = read_manifest()
    bundles = [resource for resource in resources if resource["resource_type"] == "folder_bundle"]
    rows: list[tuple[dict[str, object], str, int, int]] = []
    for resource in bundles:
        state, available_count, missing_count = status_for(resource, resources)
        rows.append((resource, state, available_count, missing_count))

    counts = Counter(row[1] for row in rows)
    lines = [
        "# Folder Bundle Payload Status",
        "",
        "This maintainer-facing report is generated from the local OneDrive sync tree and the manifest. It does not expose absolute local paths.",
        "",
        "Run `python3 scripts/generate_folder_bundle_status.py` after changing the manifest or OneDrive folder bundle payloads.",
        "",
        "## Summary",
        "",
        "| State | Count |",
        "|---|---:|",
    ]
    for state in ["present", "unavailable", "ready to materialize", "source files required", "no listed files"]:
        lines.append(f"| {state} | {counts.get(state, 0)} |")

    lines.extend(
        [
            "",
            "## Folder Bundles",
            "",
            "| ID | Course | Contributor | Payload State | Available Listed Files | Missing Listed Files |",
            "|---|---|---|---|---:|---:|",
        ]
    )
    for resource, state, available_count, missing_count in sorted(rows, key=lambda item: str(item[0]["id"])):
        lines.append(
            f"| `{resource['id']}` | {resource['course']} | {resource['contributor']} | {state} | {available_count} | {missing_count} |"
        )

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORT_DIR / "folder_bundle_status.md"
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Generated {output_path}")


if __name__ == "__main__":
    main()
