#!/usr/bin/env python3
"""Self-test the local resource release workflow without creating share links."""

from __future__ import annotations

import csv
import sys
import tempfile
from pathlib import Path
from typing import Any

from check_public_link_release_queue import collect_queue_updates, valid_release_date
from create_onedrive_share_links import (
    normalize_server_root,
    preflight_release_rows,
    select_resources,
)
from discover_onedrive_release_context import context_from_namespace
from materialize_folder_bundles_to_onedrive import ONEDRIVE_ROOT
from resource_manifest import read_manifest

FIXED_RELEASE_DATE = "2026-05-20"
DAV_NAMESPACE = "https://zjuintl-my.sharepoint.com/personal/yiru_22_intl_zju_edu_cn/Documents"
BASE_CMD = ["m365"]


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def payload_path(resource: dict[str, Any]) -> Path:
    return ONEDRIVE_ROOT / str(resource["local_onedrive_path"])


def release_test_copy(resource: dict[str, Any]) -> dict[str, Any]:
    copied = dict(resource)
    copied["public_url"] = ""
    copied["public_url_status"] = "pending"
    copied["public_link_released_at"] = ""
    copied["visibility"] = "pending_review"
    return copied


def find_payload_pair(resources: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
    file_resource: dict[str, Any] | None = None
    folder_resource: dict[str, Any] | None = None
    for resource in resources:
        if str(resource.get("public_url_status", "")) == "retired":
            continue
        path = payload_path(resource)
        if path.is_file() and file_resource is None:
            file_resource = release_test_copy(resource)
        if path.is_dir() and folder_resource is None:
            folder_resource = release_test_copy(resource)
        if file_resource and folder_resource:
            return file_resource, folder_resource
    raise AssertionError("expected at least one file payload and one folder payload in OneDrive")


def write_queue(path: Path, rows: list[dict[str, str]]) -> None:
    fieldnames = ["id", "public_url_to_fill", "public_link_released_at_to_fill"]
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def sharepoint_url(rid: str) -> str:
    return f"https://zjuintl-my.sharepoint.com/:u:/g/self-test-{rid}"


def test_queue_validation(file_resource: dict[str, Any], folder_resource: dict[str, Any]) -> None:
    synthetic_resources = [file_resource, folder_resource]
    with tempfile.TemporaryDirectory(prefix="zje-release-queue-") as tmp:
        tmp_path = Path(tmp)

        valid_queue = tmp_path / "valid.csv"
        write_queue(
            valid_queue,
            [
                {
                    "id": str(file_resource["id"]),
                    "public_url_to_fill": sharepoint_url(str(file_resource["id"])),
                    "public_link_released_at_to_fill": FIXED_RELEASE_DATE,
                }
            ],
        )
        updates, errors = collect_queue_updates(valid_queue, synthetic_resources)
        assert_true(not errors, f"valid queue unexpectedly failed: {errors}")
        assert_true(len(updates) == 1, f"expected 1 valid queue update, got {len(updates)}")
        assert_true(updates[0].rid == str(file_resource["id"]), "valid queue update used wrong resource id")
        assert_true(updates[0].released_at == FIXED_RELEASE_DATE, "valid queue update used wrong release date")

        bad_url_queue = tmp_path / "bad-url.csv"
        write_queue(
            bad_url_queue,
            [
                {
                    "id": str(file_resource["id"]),
                    "public_url_to_fill": "https://example.com/not-onedrive",
                    "public_link_released_at_to_fill": FIXED_RELEASE_DATE,
                }
            ],
        )
        _, errors = collect_queue_updates(bad_url_queue, synthetic_resources)
        assert_true(any("public URL must be a public OneDrive/SharePoint URL" in error for error in errors), "bad URL was not rejected")

        bad_date_queue = tmp_path / "bad-date.csv"
        write_queue(
            bad_date_queue,
            [
                {
                    "id": str(file_resource["id"]),
                    "public_url_to_fill": sharepoint_url(str(file_resource["id"])),
                    "public_link_released_at_to_fill": "2026-13-40",
                }
            ],
        )
        _, errors = collect_queue_updates(bad_date_queue, synthetic_resources)
        assert_true(any("release date must use YYYY-MM-DD" in error for error in errors), "bad release date was not rejected")

        duplicate_url = "https://zjuintl-my.sharepoint.com/:u:/g/self-test-duplicate"
        duplicate_queue = tmp_path / "duplicate-url.csv"
        write_queue(
            duplicate_queue,
            [
                {
                    "id": str(file_resource["id"]),
                    "public_url_to_fill": duplicate_url,
                    "public_link_released_at_to_fill": FIXED_RELEASE_DATE,
                },
                {
                    "id": str(folder_resource["id"]),
                    "public_url_to_fill": duplicate_url,
                    "public_link_released_at_to_fill": FIXED_RELEASE_DATE,
                },
            ],
        )
        _, errors = collect_queue_updates(duplicate_queue, synthetic_resources)
        assert_true(any("public URL duplicates queue row" in error for error in errors), "duplicate public URL was not rejected")


def release_context() -> tuple[str, Any]:
    context = context_from_namespace(DAV_NAMESPACE, ONEDRIVE_ROOT, Path("/tmp/ClientPolicy.ini"))
    return context.web_url, normalize_server_root(context.server_relative_root)


def command_option(cmd: list[str], option: str) -> str:
    assert_true(option in cmd, f"command is missing {option}: {' '.join(cmd)}")
    index = cmd.index(option)
    assert_true(index + 1 < len(cmd), f"command option {option} is missing a value")
    return cmd[index + 1]


def test_cli_preflight(file_resource: dict[str, Any], folder_resource: dict[str, Any]) -> int:
    web_url, server_root = release_context()
    rows, commands, errors = preflight_release_rows(
        BASE_CMD,
        [file_resource, folder_resource],
        web_url,
        server_root,
        "anonymous",
        "",
        False,
        False,
    )
    assert_true(not errors, f"synthetic CLI preflight unexpectedly failed: {errors}")
    assert_true(len(rows) == 2, f"expected two synthetic preflight rows, got {len(rows)}")

    command_by_id = {row["id"]: command for row, command in zip(rows, commands)}
    file_command = command_by_id[str(file_resource["id"])]
    folder_command = command_by_id[str(folder_resource["id"])]
    assert_true(file_command[1:4] == ["spo", "file", "sharinglink"], f"file command used wrong m365 route: {file_command}")
    assert_true(folder_command[1:4] == ["spo", "folder", "sharinglink"], f"folder command used wrong m365 route: {folder_command}")
    assert_true(command_option(file_command, "--fileUrl").endswith(str(file_resource["local_onedrive_path"])), "file command used wrong server-relative URL")
    assert_true(command_option(folder_command, "--folderUrl").endswith(str(folder_resource["local_onedrive_path"])), "folder command used wrong server-relative URL")

    rows, _, errors = preflight_release_rows(
        BASE_CMD,
        [file_resource],
        "http://zjuintl-my.sharepoint.com/personal/yiru_22_intl_zju_edu_cn",
        server_root,
        "anonymous",
        "",
        False,
        False,
    )
    assert_true(not rows or errors, "invalid web URL should not pass silently")
    assert_true(any("--web-url must use https" in error for error in errors), "invalid web URL was not rejected")

    live_resources = read_manifest()
    selected, missing = select_resources(live_resources, [], include_released=False)
    assert_true(not missing, f"unexpected missing ids from full selection: {missing}")
    if not selected:
        return 0
    rows, _, errors = preflight_release_rows(
        BASE_CMD,
        selected,
        web_url,
        server_root,
        "anonymous",
        "",
        False,
        False,
    )
    assert_true(not errors, f"live pending-resource preflight failed: {errors}")
    return len(rows)


def main() -> int:
    resources = read_manifest()
    file_resource, folder_resource = find_payload_pair(resources)
    assert_true(valid_release_date(FIXED_RELEASE_DATE), "fixed test date is invalid")

    test_queue_validation(file_resource, folder_resource)
    live_preflight_count = test_cli_preflight(file_resource, folder_resource)

    print("Resource release self-test OK")
    print(f"queue fixture file resource: {file_resource['id']}")
    print(f"queue fixture folder resource: {folder_resource['id']}")
    print(f"live pending preflight resources: {live_preflight_count}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as exc:
        print(f"Resource release self-test failed: {exc}", file=sys.stderr)
        sys.exit(1)
