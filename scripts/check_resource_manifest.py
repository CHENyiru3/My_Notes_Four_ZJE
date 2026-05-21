#!/usr/bin/env python3
"""Validate the ZJE resource manifest and repo resource policy."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from resource_manifest import DOCS_DIR, MANIFEST_PATH, ROOT, is_public_resource_url, read_manifest

STATUS_VALUES = {"pending", "released", "broken", "private", "unavailable", "retired"}
VISIBILITY_VALUES = {"pending_review", "public_after_review", "private_internal", "retired"}
RESOURCE_TYPES = {"course_package", "folder_bundle", "individual_file", "retired_mirror"}
RELEASE_TIERS = {"core", "large_archive", "retired"}
REQUIRED = {
    "id",
    "title",
    "course",
    "year_group",
    "contributor",
    "resource_type",
    "release_tier",
    "storage_provider",
    "local_onedrive_path",
    "public_url",
    "public_url_status",
    "website_sources",
    "visibility",
    "version",
}
BINARY_SUFFIXES = {".pdf", ".docx", ".pptx", ".xlsx", ".zip"}
MKDOCS_PATH = ROOT / "mkdocs.yml"
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PUBLIC_DOC_FORBIDDEN_TEXT = [
    "/Users/eric_yiru/",
    "OneDrive-InternationalCampus",
    "OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource",
    "ZJE_Collection/resources/resource_manifest.yml",
    "original_source_url",
    "local_onedrive_path",
    "drive.google.com",
    "docs.google.com",
]


def main() -> int:
    errors: list[str] = []
    if not MANIFEST_PATH.exists():
        errors.append(f"missing manifest: {MANIFEST_PATH}")
        resources = []
    else:
        resources = read_manifest(MANIFEST_PATH)

    seen: set[str] = set()
    for idx, resource in enumerate(resources, start=1):
        missing = REQUIRED - resource.keys()
        if missing:
            errors.append(f"resource #{idx} missing fields: {sorted(missing)}")
        rid = str(resource.get("id", ""))
        if not rid:
            errors.append(f"resource #{idx} has empty id")
        if rid in seen:
            errors.append(f"duplicate id: {rid}")
        seen.add(rid)

        status = resource.get("public_url_status")
        if status not in STATUS_VALUES:
            errors.append(f"{rid}: invalid public_url_status {status!r}")
        visibility = resource.get("visibility")
        if visibility not in VISIBILITY_VALUES:
            errors.append(f"{rid}: invalid visibility {visibility!r}")
        resource_type = resource.get("resource_type")
        if resource_type not in RESOURCE_TYPES:
            errors.append(f"{rid}: invalid resource_type {resource_type!r}")
        release_tier = resource.get("release_tier")
        if release_tier not in RELEASE_TIERS:
            errors.append(f"{rid}: invalid release_tier {release_tier!r}")
        public_url = str(resource.get("public_url", ""))
        released_at = str(resource.get("public_link_released_at", ""))
        if status == "released":
            if not public_url:
                errors.append(f"{rid}: released resource has empty public_url")
            elif not is_public_resource_url(public_url):
                errors.append(f"{rid}: released public_url must be an approved public resource URL")
            if not released_at:
                errors.append(f"{rid}: released resource has empty public_link_released_at")
            elif not ISO_DATE_RE.match(released_at):
                errors.append(f"{rid}: public_link_released_at must use YYYY-MM-DD")
        if status == "pending" and public_url:
            errors.append(f"{rid}: pending resource must not have public_url")
        if public_url.startswith("/Users/") or public_url.startswith("file://"):
            errors.append(f"{rid}: public_url must not be a local path")
        local_path = str(resource.get("local_onedrive_path", ""))
        if local_path.startswith("/") or "OneDrive-InternationalCampus" in local_path:
            errors.append(f"{rid}: local_onedrive_path must be relative to ZJE_resource")
        if local_path.lower().endswith(".zip"):
            errors.append(f"{rid}: ZIP archives are retired; use a OneDrive folder bundle path")
        if release_tier == "large_archive" and not local_path.startswith("LARGE_ARCHIVES/"):
            errors.append(f"{rid}: large_archive resources must live under LARGE_ARCHIVES/")
        if release_tier == "core" and local_path.startswith("LARGE_ARCHIVES/"):
            errors.append(f"{rid}: core resources must not live under LARGE_ARCHIVES/")
        if resource_type == "retired_mirror" and release_tier != "retired":
            errors.append(f"{rid}: retired_mirror resources must use release_tier 'retired'")
        storage_provider = str(resource.get("storage_provider", ""))
        if storage_provider == "github":
            if not str(resource.get("resource_repo_path", "")):
                errors.append(f"{rid}: github resources must include resource_repo_path")
            if status == "released" and "github.com/CHENyiru3/awesome_ZJE_resource" not in public_url and "raw.githubusercontent.com/CHENyiru3/awesome_ZJE_resource" not in public_url:
                errors.append(f"{rid}: github resource URL must point to CHENyiru3/awesome_ZJE_resource")

    binaries = sorted(path for path in DOCS_DIR.rglob("*") if path.suffix.lower() in BINARY_SUFFIXES)
    if binaries:
        errors.append("binary resources still present in ZJE_Collection:")
        errors.extend(f"  {path.relative_to(DOCS_DIR.parent)}" for path in binaries)

    text_hits = []
    for path in DOCS_DIR.rglob("*"):
        if path == MANIFEST_PATH:
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".csv", ".yml"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            matched = [needle for needle in PUBLIC_DOC_FORBIDDEN_TEXT if needle in text]
            if matched:
                text_hits.append(
                    f"{path.relative_to(DOCS_DIR.parent).as_posix()} ({', '.join(matched)})"
                )
    if text_hits:
        errors.append("public docs contain internal migration/storage text:")
        errors.extend(f"  {hit}" for hit in text_hits)

    if MKDOCS_PATH.exists():
        mkdocs_text = MKDOCS_PATH.read_text(encoding="utf-8")
        if "exclude_docs:" not in mkdocs_text or "resources/resource_manifest.yml" not in mkdocs_text:
            errors.append("mkdocs.yml must exclude resources/resource_manifest.yml from the public site")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Manifest OK: {len(resources)} resources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
