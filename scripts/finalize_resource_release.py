#!/usr/bin/env python3
"""Finalize resource pages and validation after public links are released."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from resource_manifest import ROOT


def run_step(label: str, cmd: list[str], *, allow_failure: bool = False) -> int:
    print(f"\n==> {label}", flush=True)
    completed = subprocess.run(cmd, cwd=ROOT)
    if completed.returncode and not allow_failure:
        print(f"{label} failed with exit code {completed.returncode}", file=sys.stderr)
        return completed.returncode
    if completed.returncode and allow_failure:
        print(f"{label} reported incomplete state with exit code {completed.returncode}", flush=True)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="site", help="MkDocs build output directory.")
    parser.add_argument("--skip-build", action="store_true", help="Skip mkdocs build and public site output scan.")
    parser.add_argument(
        "--sync-onedrive-manifest",
        action="store_true",
        help="Copy the repo manifest and CSV into OneDrive MANIFESTS after regeneration.",
    )
    parser.add_argument(
        "--allow-incomplete",
        action="store_true",
        help="Allow the completion audit to report remaining unreleased links.",
    )
    args = parser.parse_args()

    steps: list[tuple[str, list[str]]] = [
        ("Generate public resource pages", ["python3", "scripts/generate_resource_pages.py"]),
        ("Generate public-link release queue", ["python3", "scripts/generate_public_link_release_queue.py"]),
        ("Generate migration status", ["python3", "scripts/generate_migration_status.py"]),
        ("Validate resource manifest", ["python3", "scripts/check_resource_manifest.py"]),
        ("Validate generated resource pages", ["python3", "scripts/check_resource_pages.py"]),
        ("Validate public-link release queue", ["python3", "scripts/check_public_link_release_queue.py"]),
        ("Validate local Markdown links", ["python3", "scripts/check_links.py"]),
        ("Validate OneDrive payloads", ["python3", "scripts/check_onedrive_payloads.py"]),
    ]
    for label, cmd in steps:
        code = run_step(label, cmd)
        if code:
            return code

    if args.sync_onedrive_manifest:
        code = run_step("Sync manifest into OneDrive", ["python3", "scripts/sync_resource_manifest_to_onedrive.py"])
        if code:
            return code

    if not args.skip_build:
        site_dir = Path(args.site_dir)
        code = run_step("Build MkDocs site", ["python3", "-m", "mkdocs", "build", "--site-dir", str(site_dir)])
        if code:
            return code
        code = run_step(
            "Validate public site output",
            ["python3", "scripts/check_public_site_output.py", "--site-dir", str(site_dir)],
        )
        if code:
            return code

    code = run_step(
        "Generate completion audit",
        ["python3", "scripts/generate_migration_completion_audit.py"],
        allow_failure=args.allow_incomplete,
    )
    if code:
        return code

    print("\nResource release finalization checks completed.", flush=True)
    if args.allow_incomplete:
        print("Completion audit was allowed to remain incomplete; inspect resource_migration_reports/completion_audit.md.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
