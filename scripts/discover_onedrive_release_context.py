#!/usr/bin/env python3
"""Discover local OneDrive/SharePoint release parameters from sync metadata.

The Microsoft 365 CLI share-link helper needs two values:

- ``--web-url``: the OneDrive/SharePoint web URL.
- ``--server-relative-root``: the server-relative path corresponding to the
  local ``ZJE_resource`` root.

This helper reads local OneDrive sync policy metadata only. It does not read or
print auth tokens, create links, log in, or create Microsoft Entra apps.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote, urlparse, urlunparse

from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import REPORT_DIR

DEFAULT_CLIENT_POLICY = (
    Path.home()
    / "Library"
    / "Application Support"
    / "OneDrive"
    / "settings"
    / "Business1"
    / "ClientPolicy.ini"
)
LOCAL_REPORT_MD = REPORT_DIR / "onedrive_release_context.local.md"
LOCAL_REPORT_JSON = REPORT_DIR / "onedrive_release_context.local.json"


@dataclass(frozen=True)
class OneDriveReleaseContext:
    web_url: str
    server_relative_root: str
    dav_url_namespace: str
    local_onedrive_root: str
    client_policy_path: str


def read_sectionless_ini(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("[") or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def context_from_namespace(
    dav_url_namespace: str,
    local_onedrive_root: Path,
    client_policy_path: Path,
) -> OneDriveReleaseContext:
    parsed = urlparse(dav_url_namespace)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError(f"Unsupported DavUrlNamespace: {dav_url_namespace!r}")

    library_path = unquote(parsed.path).rstrip("/")
    if not library_path:
        raise ValueError(f"DavUrlNamespace has no path: {dav_url_namespace!r}")
    if "/" not in library_path.strip("/"):
        raise ValueError(
            "DavUrlNamespace path does not include a web path plus document library: "
            f"{dav_url_namespace!r}"
        )

    web_path = library_path.rsplit("/", 1)[0]
    web_url = urlunparse((parsed.scheme, parsed.netloc, web_path, "", "", ""))
    server_relative_root = f"{library_path}/{local_onedrive_root.name}"
    return OneDriveReleaseContext(
        web_url=web_url,
        server_relative_root=server_relative_root,
        dav_url_namespace=dav_url_namespace,
        local_onedrive_root=str(local_onedrive_root),
        client_policy_path=str(client_policy_path),
    )


def discover_context(
    client_policy_path: Path = DEFAULT_CLIENT_POLICY,
    local_onedrive_root: Path = ONEDRIVE_ROOT,
) -> OneDriveReleaseContext:
    if not client_policy_path.exists():
        raise FileNotFoundError(f"missing OneDrive client policy: {client_policy_path}")
    values = read_sectionless_ini(client_policy_path)
    namespace = values.get("DavUrlNamespace", "")
    if not namespace:
        raise ValueError(f"{client_policy_path} does not contain DavUrlNamespace")
    return context_from_namespace(namespace, local_onedrive_root, client_policy_path)


def write_local_reports(context: OneDriveReleaseContext) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    LOCAL_REPORT_JSON.write_text(
        json.dumps(asdict(context), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# Local OneDrive Release Context",
        "",
        "This file is local-only and ignored by Git because it contains account-specific SharePoint paths.",
        "",
        "```bash",
        "python3 scripts/create_onedrive_share_links.py \\",
        f"  --web-url {json.dumps(context.web_url)} \\",
        f"  --server-relative-root {json.dumps(context.server_relative_root)} \\",
        "  --ids <resource-id>",
        "```",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| web_url | `{context.web_url}` |",
        f"| server_relative_root | `{context.server_relative_root}` |",
        f"| local_onedrive_root | `{context.local_onedrive_root}` |",
        f"| client_policy_path | `{context.client_policy_path}` |",
    ]
    LOCAL_REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client-policy", type=Path, default=DEFAULT_CLIENT_POLICY, help="OneDrive Business ClientPolicy.ini path.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of shell-ready arguments.")
    parser.add_argument("--write-local", action="store_true", help="Write ignored local context reports under resource_migration_reports/.")
    args = parser.parse_args()

    try:
        context = discover_context(args.client_policy, ONEDRIVE_ROOT)
    except Exception as exc:
        print(f"Could not discover OneDrive release context: {exc}", file=sys.stderr)
        return 1

    if args.write_local:
        write_local_reports(context)
    if args.json:
        print(json.dumps(asdict(context), indent=2, ensure_ascii=False))
    else:
        print("--web-url", context.web_url)
        print("--server-relative-root", context.server_relative_root)
        print("Use with: python3 scripts/create_onedrive_share_links.py --discover-context --ids <resource-id>")
        if args.write_local:
            print(f"Wrote {LOCAL_REPORT_MD} and {LOCAL_REPORT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
