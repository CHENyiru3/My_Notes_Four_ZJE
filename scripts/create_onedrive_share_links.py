#!/usr/bin/env python3
"""Create OneDrive/SharePoint sharing links for manifest resources.

This helper is intentionally opt-in:

- it never creates a Microsoft Entra app registration;
- executed runs require an existing Microsoft 365 CLI login, or an explicit
  existing app id passed to ``m365 login --ensure``;
- dry runs print the exact commands that would be executed.
"""

from __future__ import annotations

import argparse
import csv
import json
import shlex
import shutil
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse

from discover_onedrive_release_context import discover_context
from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import MANIFEST_PATH, REPORT_DIR, is_public_onedrive_url, payload_integrity_issues, read_manifest, write_manifest

RESULTS_CSV = REPORT_DIR / "public_link_release_results.csv"
RESULTS_MD = REPORT_DIR / "public_link_release_results.md"
ONEDRIVE_RELEASE_LOG = ONEDRIVE_ROOT / "MANIFESTS" / "public_link_release_log.md"
FOLDER_TYPES = {"course_package", "folder_bundle"}


def m365_command(use_npx: bool) -> list[str]:
    if use_npx:
        return ["npx", "-y", "-p", "@pnp/cli-microsoft365", "m365"]
    if shutil.which("m365"):
        return ["m365"]
    return ["npx", "-y", "-p", "@pnp/cli-microsoft365", "m365"]


def shell_join(parts: list[str]) -> str:
    return " ".join(shlex.quote(part) for part in parts)


def normalize_server_root(value: str) -> PurePosixPath:
    if not value.startswith("/"):
        raise ValueError("--server-relative-root must start with /")
    return PurePosixPath(value.rstrip("/"))


def validate_web_url(value: str) -> list[str]:
    parsed = urlparse(value)
    errors: list[str] = []
    if parsed.scheme != "https":
        errors.append("--web-url must use https")
    host = parsed.netloc.lower()
    if not host or not (host.endswith(".sharepoint.com") or host.endswith(".sharepoint.cn")):
        errors.append("--web-url must point to a SharePoint host")
    if not parsed.path.strip("/"):
        errors.append("--web-url must include the OneDrive/SharePoint web path")
    return errors


def server_relative_url(server_root: PurePosixPath, local_onedrive_path: str) -> str:
    rel = PurePosixPath(local_onedrive_path)
    if rel.is_absolute() or ".." in rel.parts:
        raise ValueError(f"unsafe local_onedrive_path: {local_onedrive_path}")
    return str(server_root.joinpath(rel))


def validate_server_relative_root(web_url: str, server_root: PurePosixPath) -> list[str]:
    errors: list[str] = []
    parsed = urlparse(web_url)
    web_path = PurePosixPath(parsed.path.rstrip("/"))
    root_text = str(server_root)
    if not root_text.startswith(str(web_path)):
        errors.append(
            f"--server-relative-root {root_text!r} must be under the --web-url path {str(web_path)!r}"
        )
    if server_root.name != ONEDRIVE_ROOT.name:
        errors.append(
            f"--server-relative-root must end with {ONEDRIVE_ROOT.name!r}, got {server_root.name!r}"
        )
    return errors


def is_folder_resource(resource: dict[str, Any], payload_path: Path) -> bool:
    if str(resource.get("resource_type", "")) in FOLDER_TYPES:
        return True
    if payload_path.exists():
        return payload_path.is_dir()
    return not Path(str(resource.get("local_onedrive_path", ""))).suffix


def select_resources(
    resources: list[dict[str, Any]],
    ids: list[str],
    include_released: bool,
) -> tuple[list[dict[str, Any]], list[str]]:
    wanted = set(ids)
    by_id = {str(resource["id"]): resource for resource in resources}
    missing = sorted(wanted - by_id.keys())
    selected: list[dict[str, Any]] = []

    for resource in resources:
        rid = str(resource["id"])
        if wanted and rid not in wanted:
            continue
        status = str(resource.get("public_url_status", ""))
        if status == "retired":
            continue
        if status == "released" and not include_released:
            continue
        selected.append(resource)

    return selected, missing


def preflight_release_rows(
    base_cmd: list[str],
    resources: list[dict[str, Any]],
    web_url: str,
    server_root: PurePosixPath,
    scope: str,
    expiration: str,
    include_released: bool,
    no_payload_check: bool,
) -> tuple[list[dict[str, str]], list[list[str]], list[str]]:
    rows: list[dict[str, str]] = []
    commands: list[list[str]] = []
    errors: list[str] = []
    errors.extend(validate_web_url(web_url))
    errors.extend(validate_server_relative_root(web_url, server_root))

    for resource in resources:
        rid = str(resource["id"])
        status = str(resource.get("public_url_status", ""))
        if status == "released" and include_released:
            pass
        elif status != "pending":
            errors.append(f"{rid}: public_url_status is {status!r}; expected 'pending'")

        local_rel = str(resource["local_onedrive_path"])
        try:
            item_url = server_relative_url(server_root, local_rel)
        except ValueError as exc:
            errors.append(f"{rid}: {exc}")
            continue
        if not item_url.startswith(f"{str(server_root)}/"):
            errors.append(f"{rid}: server-relative item URL escapes the release root")
            continue

        payload_path = ONEDRIVE_ROOT / local_rel
        item_is_folder = is_folder_resource(resource, payload_path)
        if not no_payload_check:
            if not payload_path.exists():
                errors.append(f"{rid}: missing local OneDrive payload: {local_rel}")
            elif item_is_folder and not payload_path.is_dir():
                errors.append(f"{rid}: expected OneDrive folder payload: {local_rel}")
            elif not item_is_folder and not payload_path.is_file():
                errors.append(f"{rid}: expected OneDrive file payload: {local_rel}")
            else:
                issues = payload_integrity_issues(payload_path)
                if issues:
                    issue_path, issue = issues[0]
                    try:
                        issue_label = issue_path.relative_to(ONEDRIVE_ROOT).as_posix()
                    except ValueError:
                        issue_label = str(issue_path)
                    errors.append(f"{rid}: OneDrive payload is unavailable: {issue_label} ({issue})")

        cmd, item_type, command_item_url = build_share_command(
            base_cmd,
            resource,
            web_url,
            server_root,
            scope,
            expiration,
        )
        row = {
            "id": rid,
            "title": str(resource["title"]),
            "course": str(resource["course"]),
            "contributor": str(resource["contributor"]),
            "item_type": item_type,
            "server_relative_url": command_item_url,
            "public_url_status": "planned",
            "public_url": "",
            "public_link_released_at": "",
            "error": "",
        }
        rows.append(row)
        commands.append(cmd)

    return rows, commands, errors


def build_share_command(
    base_cmd: list[str],
    resource: dict[str, Any],
    web_url: str,
    server_root: PurePosixPath,
    scope: str,
    expiration: str,
) -> tuple[list[str], str, str]:
    local_rel = str(resource["local_onedrive_path"])
    payload_path = ONEDRIVE_ROOT / local_rel
    item_url = server_relative_url(server_root, local_rel)
    if is_folder_resource(resource, payload_path):
        cmd = [
            *base_cmd,
            "spo",
            "folder",
            "sharinglink",
            "add",
            "--webUrl",
            web_url,
            "--folderUrl",
            item_url,
            "--type",
            "view",
            "--scope",
            scope,
            "-o",
            "json",
        ]
        item_type = "folder"
    else:
        cmd = [
            *base_cmd,
            "spo",
            "file",
            "sharinglink",
            "add",
            "--webUrl",
            web_url,
            "--fileUrl",
            item_url,
            "--type",
            "view",
            "--scope",
            scope,
            "-o",
            "json",
        ]
        item_type = "file"
    if expiration:
        cmd.extend(["--expirationDateTime", expiration])
    return cmd, item_type, item_url


def extract_public_url(stdout: str) -> str:
    payload = json.loads(stdout)
    link = payload.get("link", {})
    public_url = link.get("webUrl", "")
    if not public_url:
        raise ValueError("Microsoft 365 CLI response did not contain link.webUrl")
    if not is_public_onedrive_url(str(public_url)):
        raise ValueError(f"sharing link is not a public OneDrive/SharePoint URL: {public_url}")
    return str(public_url)


def run_login(base_cmd: list[str], app_id: str, tenant: str, auth_type: str) -> None:
    cmd = [*base_cmd, "login", "--ensure", "--authType", auth_type, "--appId", app_id]
    if tenant:
        cmd.extend(["--tenant", tenant])
    subprocess.run(cmd, check=True)


def write_results(rows: list[dict[str, str]]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "title",
        "course",
        "contributor",
        "item_type",
        "server_relative_url",
        "public_url_status",
        "public_url",
        "public_link_released_at",
        "error",
    ]
    with RESULTS_CSV.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Public Link Release Results",
        "",
        "Generated by `scripts/create_onedrive_share_links.py`.",
        "",
        "## Summary",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    status_counts = Counter(row["public_url_status"] for row in rows)
    for status in ["released", "error", "planned", "skipped"]:
        lines.append(f"| {status} | {status_counts.get(status, 0)} |")
    lines.extend(
        [
            "",
            "If an executed run is interrupted or partially fails, inspect the rows below, then rerun with `--all`; already released resources are skipped unless `--include-released` is supplied.",
            "",
            "## Rows",
            "",
        ]
    )
    lines.extend(
        [
            "| ID | Course | Contributor | Item | Status | Public URL | Error |",
            "|---|---|---|---|---|---|---|",
        ]
    )
    for row in rows:
        url = row["public_url"] if row["public_url"] else ""
        lines.append(
            f"| `{row['id']}` | {row['course']} | {row['contributor']} | {row['item_type']} | {row['public_url_status']} | {url} | {row['error']} |"
        )
    RESULTS_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def append_onedrive_release_log(rows: list[dict[str, str]], scope: str) -> None:
    released = [row for row in rows if row["public_url_status"] == "released"]
    if not released:
        return
    ONEDRIVE_RELEASE_LOG.parent.mkdir(parents=True, exist_ok=True)
    if not ONEDRIVE_RELEASE_LOG.exists():
        ONEDRIVE_RELEASE_LOG.write_text("# Public Link Release Log\n\n", encoding="utf-8")
    with ONEDRIVE_RELEASE_LOG.open("a", encoding="utf-8") as fh:
        fh.write(f"\n## {date.today().isoformat()} Microsoft 365 CLI release\n\n")
        for row in released:
            fh.write(
                f"- `{row['id']}` ({row['item_type']}, scope: {scope}) -> {row['public_url']}\n"
            )


def write_execution_checkpoint(
    resources: list[dict[str, Any]],
    rows: list[dict[str, str]],
    update_manifest: bool,
) -> None:
    write_results(rows)
    if update_manifest:
        write_manifest(resources, MANIFEST_PATH)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--web-url", default="", help="SharePoint/OneDrive site URL passed to m365 --webUrl.")
    parser.add_argument(
        "--server-relative-root",
        default="",
        help="Decoded server-relative URL that corresponds to the local ZJE_resource root.",
    )
    parser.add_argument("--discover-context", action="store_true", help="Read --web-url and --server-relative-root from local OneDrive sync metadata.")
    parser.add_argument("--ids", nargs="*", default=[], help="Resource ids to process.")
    parser.add_argument("--all", action="store_true", help="Allow executed runs to process every non-retired, non-released resource.")
    parser.add_argument("--include-released", action="store_true", help="Include already released resources.")
    parser.add_argument("--scope", choices=["anonymous", "organization"], default="anonymous", help="Sharing link scope.")
    parser.add_argument("--expiration-date-time", default="", help="Optional ISO 8601 expirationDateTime value.")
    parser.add_argument("--execute", action="store_true", help="Create links. Without this flag, only print commands.")
    parser.add_argument("--update-manifest", action="store_true", help="Write created anonymous links back to the resource manifest.")
    parser.add_argument("--write-dry-run-results", action="store_true", help="Write public_link_release_results.* during dry runs.")
    parser.add_argument("--preflight-only", action="store_true", help="Validate selected resources and context without printing every m365 command.")
    parser.add_argument("--login", action="store_true", help="Run m365 login --ensure before creating links.")
    parser.add_argument("--app-id", default="", help="Existing Microsoft Entra app id for m365 login --ensure.")
    parser.add_argument("--tenant", default="", help="Optional tenant id/name for m365 login --ensure.")
    parser.add_argument("--auth-type", default="deviceCode", help="Authentication type for m365 login --ensure.")
    parser.add_argument("--use-npx", action="store_true", help="Always run m365 through npx @pnp/cli-microsoft365.")
    parser.add_argument("--no-payload-check", action="store_true", help="Do not require the local OneDrive payload path to exist.")
    args = parser.parse_args()

    if args.discover_context:
        try:
            context = discover_context()
        except Exception as exc:
            print(f"Could not discover OneDrive release context: {exc}", file=sys.stderr)
            return 2
        args.web_url = args.web_url or context.web_url
        args.server_relative_root = args.server_relative_root or context.server_relative_root

    if not args.web_url:
        print("--web-url is required unless --discover-context can derive it.", file=sys.stderr)
        return 2
    if not args.server_relative_root:
        print("--server-relative-root is required unless --discover-context can derive it.", file=sys.stderr)
        return 2
    if args.execute and not args.ids and not args.all:
        print("Executed runs require --ids ... or --all.", file=sys.stderr)
        return 2
    if args.login and not args.app_id:
        print("--login requires --app-id for an existing Microsoft Entra application.", file=sys.stderr)
        return 2
    if args.update_manifest and not args.execute:
        print("--update-manifest requires --execute.", file=sys.stderr)
        return 2
    if args.update_manifest and args.scope != "anonymous":
        print("--update-manifest requires --scope anonymous for public website release.", file=sys.stderr)
        return 2

    resources = read_manifest()
    selected, missing_ids = select_resources(resources, args.ids, args.include_released)
    if missing_ids:
        print(f"Unknown resource id(s): {', '.join(missing_ids)}", file=sys.stderr)
        return 1
    if not selected:
        print("No matching resources selected.")
        return 0

    base_cmd = m365_command(args.use_npx)
    server_root = normalize_server_root(args.server_relative_root)
    rows, commands, preflight_errors = preflight_release_rows(
        base_cmd,
        selected,
        args.web_url,
        server_root,
        args.scope,
        args.expiration_date_time,
        args.include_released,
        args.no_payload_check,
    )
    if preflight_errors:
        print("Release preflight failed:", file=sys.stderr)
        print("\n".join(preflight_errors), file=sys.stderr)
        return 1
    print(f"Release preflight OK: {len(rows)} resource(s)")
    if args.preflight_only:
        return 0

    if args.execute and args.login:
        run_login(base_cmd, args.app_id, args.tenant, args.auth_type)

    released_at = date.today().isoformat()
    by_id = {str(resource["id"]): resource for resource in resources}
    processed_any = False

    try:
        for resource, row, cmd in zip(selected, rows, commands):
            rid = str(resource["id"])
            if not args.execute:
                print(f"PLAN {rid}: {shell_join(cmd)}")
                continue

            try:
                completed = subprocess.run(cmd, check=True, capture_output=True, text=True)
                public_url = extract_public_url(completed.stdout)
                row["public_url_status"] = "released"
                row["public_url"] = public_url
                row["public_link_released_at"] = released_at
                print(f"RELEASED {rid}: {public_url}")
                if args.update_manifest:
                    current = by_id[rid]
                    current["public_url"] = public_url
                    current["public_url_status"] = "released"
                    current["visibility"] = "public_after_review"
                    current["public_link_released_at"] = released_at
            except Exception as exc:
                row["public_url_status"] = "error"
                row["error"] = str(exc)
                print(f"ERROR {rid}: {exc}", file=sys.stderr)
            processed_any = True
            write_execution_checkpoint(resources, rows, args.update_manifest)
    except KeyboardInterrupt:
        if args.execute and processed_any:
            write_execution_checkpoint(resources, rows, args.update_manifest)
            print(
                f"Interrupted; checkpointed progress to {RESULTS_MD} and {RESULTS_CSV}",
                file=sys.stderr,
            )
        raise

    if args.execute or args.write_dry_run_results:
        write_results(rows)
    if args.execute:
        append_onedrive_release_log(rows, args.scope)
    if args.update_manifest:
        write_manifest(resources, MANIFEST_PATH)
        print(f"Updated released links in {MANIFEST_PATH}")

    if args.execute or args.write_dry_run_results:
        print(f"Wrote {RESULTS_MD} and {RESULTS_CSV}")
    return 1 if any(row["public_url_status"] == "error" for row in rows) else 0


if __name__ == "__main__":
    sys.exit(main())
