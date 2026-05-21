#!/usr/bin/env python3
"""Small manifest helpers for the ZJE resource migration.

The project intentionally avoids a YAML dependency in CI.  These helpers read
and write the restricted YAML shape used by
`ZJE_Collection/resources/resource_manifest.yml`.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "ZJE_Collection"
RESOURCE_DIR = DOCS_DIR / "resources"
MANIFEST_PATH = RESOURCE_DIR / "resource_manifest.yml"
REPORT_DIR = ROOT / "resource_migration_reports"

LIST_FIELDS = {"website_sources"}
INT_FIELDS = {"version", "size_bytes"}
PAYLOAD_SUFFIXES = {".pdf", ".docx", ".pptx", ".xlsx", ".zip", ".one", ".xmind"}
ONEDRIVE_PUBLIC_URL_HOST_SUFFIXES = (
    "sharepoint.com",
    "sharepoint.cn",
    "1drv.ms",
    "onedrive.live.com",
)
GITHUB_RESOURCE_HOSTS = {
    "github.com",
    "raw.githubusercontent.com",
}


def is_public_onedrive_url(value: str) -> bool:
    """Return whether a URL looks like a public OneDrive/SharePoint share URL."""
    parsed = urlparse(value)
    if parsed.scheme != "https":
        return False
    host = parsed.netloc.lower()
    if not host or host.startswith("localhost"):
        return False
    return any(host == suffix or host.endswith(f".{suffix}") for suffix in ONEDRIVE_PUBLIC_URL_HOST_SUFFIXES)


def is_public_resource_url(value: str) -> bool:
    """Return whether a URL is allowed for released website resources."""
    if is_public_onedrive_url(value):
        return True
    parsed = urlparse(value)
    if parsed.scheme != "https":
        return False
    host = parsed.netloc.lower()
    return host in GITHUB_RESOURCE_HOSTS


def file_payload_issue(path: Path) -> str | None:
    """Return a local payload issue for files that are empty or cloud-only."""
    if path.suffix.lower() not in PAYLOAD_SUFFIXES:
        return None
    try:
        stat = path.stat()
    except OSError as exc:
        return f"unreadable: {exc}"
    if stat.st_size == 0:
        return "empty file"
    if getattr(stat, "st_blocks", 1) == 0:
        return "cloud-only placeholder"
    return None


def payload_integrity_issues(path: Path) -> list[tuple[Path, str]]:
    """Return missing, empty, or cloud-only payload files without hydrating them."""
    if not path.exists():
        return [(path, "missing")]
    if path.is_file():
        issue = file_payload_issue(path)
        return [(path, issue)] if issue else []
    if not path.is_dir():
        return [(path, "not a file or directory")]

    issues: list[tuple[Path, str]] = []
    for item in path.rglob("*"):
        if not item.is_file():
            continue
        issue = file_payload_issue(item)
        if issue:
            issues.append((item, issue))
    return issues


def payload_has_local_data(path: Path) -> bool:
    """Return whether a payload path exists and has no empty/cloud-only files."""
    return not payload_integrity_issues(path)


def _parse_scalar(raw: str) -> Any:
    raw = raw.strip()
    if raw == "null":
        return None
    if raw.startswith('"') and raw.endswith('"'):
        return json.loads(raw)
    if raw in {"true", "false"}:
        return raw == "true"
    try:
        return int(raw)
    except ValueError:
        return raw


def _format_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def read_manifest(path: Path = MANIFEST_PATH) -> list[dict[str, Any]]:
    resources: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    current_list_key: str | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line == "resources:":
            continue
        if line.startswith("    - "):
            if current is None or current_list_key is None:
                raise ValueError(f"List item without list key: {line}")
            current[current_list_key].append(_parse_scalar(line[6:]))
            continue
        if line.startswith("- "):
            key, raw = line[2:].split(":", 1)
            current = {key: _parse_scalar(raw)}
            resources.append(current)
            current_list_key = None
            continue
        if line.startswith("  "):
            if current is None:
                raise ValueError(f"Field without resource: {line}")
            key, raw = line[2:].split(":", 1)
            if raw.strip() == "":
                current[key] = []
                current_list_key = key
            else:
                current[key] = _parse_scalar(raw)
                current_list_key = None
            continue
        raise ValueError(f"Unsupported manifest line: {line}")

    return resources


def write_manifest(resources: list[dict[str, Any]], path: Path = MANIFEST_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Generated by scripts/bootstrap_resource_manifest.py; edit values in-place after bootstrap.",
        "# Public URLs remain blank until OneDrive share links are released.",
        "resources:",
    ]

    for resource in resources:
        lines.append(f"- id: {_format_scalar(resource['id'])}")
        for key, value in resource.items():
            if key == "id":
                continue
            if key in LIST_FIELDS:
                lines.append(f"  {key}:")
                for item in value:
                    lines.append(f"    - {_format_scalar(item)}")
            else:
                lines.append(f"  {key}: {_format_scalar(value)}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
