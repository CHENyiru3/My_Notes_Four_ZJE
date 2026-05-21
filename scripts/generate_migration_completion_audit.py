#!/usr/bin/env python3
"""Generate a requirement-level audit for RESOURCE_MIGRATION_SPEC.md.

This report is intentionally stricter than the operational status report.  It
answers whether the migration is actually complete, and returns a non-zero exit
code while any spec requirement still needs work.
"""

from __future__ import annotations

import csv
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from check_public_site_output import (
    FORBIDDEN_RELATIVE_FILES,
    FORBIDDEN_TEXT as SITE_FORBIDDEN_TEXT,
    text_files as site_text_files,
)
from generate_migration_status import (
    MANIFEST_COPY,
    mkdocs_excludes_manifest,
    onedrive_zip_count,
    payload_state,
    repo_binary_count,
    text_policy_hits,
)
from resource_manifest import DOCS_DIR, MANIFEST_PATH, REPORT_DIR, ROOT, is_public_resource_url, read_manifest

BINARY_SUFFIXES = {".pdf", ".docx", ".pptx", ".xlsx", ".zip"}
DOWNLOAD_CSV = DOCS_DIR / "resources" / "download_links.csv"
SITE_DIR = ROOT / "site"
GH_PAGES_WORKFLOW = ROOT / ".github" / "workflows" / "gh-pages.yml"
CONTRIBUTING = DOCS_DIR / "CONTRIBUTING.md"


@dataclass
class AuditItem:
    phase: str
    requirement: str
    passed: bool
    evidence: str
    remaining: str = ""


def git_tracked_binaries() -> list[str]:
    completed = subprocess.run(
        ["git", "ls-files", "ZJE_Collection"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(
        path
        for path in completed.stdout.splitlines()
        if Path(path).suffix.lower() in BINARY_SUFFIXES
    )


def download_csv_rows() -> list[dict[str, str]]:
    if not DOWNLOAD_CSV.exists():
        return []
    with DOWNLOAD_CSV.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def built_site_errors() -> list[str]:
    errors: list[str] = []
    if not SITE_DIR.exists():
        return [f"missing built site directory: {SITE_DIR.relative_to(ROOT)}"]
    for relative in FORBIDDEN_RELATIVE_FILES:
        path = SITE_DIR / relative
        if path.exists():
            errors.append(f"forbidden published file: {path.relative_to(ROOT)}")
    for path in site_text_files(SITE_DIR):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for needle in SITE_FORBIDDEN_TEXT:
            if needle in text:
                errors.append(f"forbidden public text {needle!r} in {path.relative_to(ROOT)}")
    return errors


def workflow_retired_zip_publish() -> tuple[bool, str]:
    if not GH_PAGES_WORKFLOW.exists():
        return False, "missing .github/workflows/gh-pages.yml"
    text = GH_PAGES_WORKFLOW.read_text(encoding="utf-8")
    forbidden = [needle for needle in ["pack_yiru_zips.py", "site/downloads", "downloads/*.zip"] if needle in text]
    if forbidden:
        return False, f"workflow still references {', '.join(forbidden)}"
    return True, "gh-pages workflow does not create or publish generated ZIP downloads"


def contributor_instructions_ready() -> tuple[bool, str]:
    if not CONTRIBUTING.exists():
        return False, "missing ZJE_Collection/CONTRIBUTING.md"
    text = CONTRIBUTING.read_text(encoding="utf-8")
    required = ["OneDrive", "resource", "maintainer"]
    missing = [word for word in required if word not in text]
    if missing:
        return False, f"contributor instructions do not mention: {', '.join(missing)}"
    forbidden = [needle for needle in ["ZJE_resource", "resource_manifest.yml"] if needle in text]
    if forbidden:
        return False, f"public contributor instructions expose maintainer internals: {', '.join(forbidden)}"
    return True, "contributor instructions describe the OneDrive maintainer resource flow"


def public_url_errors(resources: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    for resource in resources:
        rid = str(resource["id"])
        status = str(resource["public_url_status"])
        url = str(resource.get("public_url", ""))
        if status == "released":
            if not url:
                errors.append(f"{rid}: released status has empty public_url")
            elif not is_public_resource_url(url):
                errors.append(f"{rid}: released public_url is not an approved public resource URL")
        elif url:
            errors.append(f"{rid}: non-released status {status!r} has public_url populated")
    return errors


def release_tier_layout_errors(resources: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    for resource in resources:
        rid = str(resource["id"])
        tier = str(resource.get("release_tier", ""))
        local_path = str(resource.get("local_onedrive_path", ""))
        if tier == "large_archive" and not local_path.startswith("LARGE_ARCHIVES/"):
            errors.append(f"{rid}: large archive path is not under LARGE_ARCHIVES/")
        if tier == "core" and local_path.startswith("LARGE_ARCHIVES/"):
            errors.append(f"{rid}: core path is under LARGE_ARCHIVES/")
    return errors


def download_table_errors(resources: list[dict[str, object]]) -> list[str]:
    errors: list[str] = []
    released = {
        str(resource["id"]): resource
        for resource in resources
        if str(resource["public_url_status"]) == "released"
    }
    rows = download_csv_rows()
    row_ids = {row.get("id", "") for row in rows}
    if row_ids != set(released):
        missing = sorted(set(released) - row_ids)
        extra = sorted(row_ids - set(released))
        if missing:
            errors.append(f"download_links.csv missing released ids: {', '.join(missing)}")
        if extra:
            errors.append(f"download_links.csv contains non-released ids: {', '.join(extra)}")
    for row in rows:
        rid = row.get("id", "")
        if row.get("public_url_status") != "released":
            errors.append(f"{rid}: public download row is not released")
        if not is_public_resource_url(row.get("public_url", "")):
            errors.append(f"{rid}: public download row URL is not an approved public resource URL")
    return errors


def audit_items() -> list[AuditItem]:
    resources = read_manifest()
    status_counts: dict[str, int] = {}
    for resource in resources:
        status = str(resource["public_url_status"])
        status_counts[status] = status_counts.get(status, 0) + 1

    present_payloads, missing_payloads, unavailable_payloads, bundle_counts = payload_state(resources)
    tracked_binaries = git_tracked_binaries()
    public_doc_hits = text_policy_hits()
    manifest_copy_synced = MANIFEST_COPY.exists() and MANIFEST_COPY.read_bytes() == MANIFEST_PATH.read_bytes()
    public_url_issue_list = public_url_errors(resources)
    release_tier_issue_list = release_tier_layout_errors(resources)
    download_issue_list = download_table_errors(resources)
    site_issue_list = built_site_errors()
    workflow_ok, workflow_evidence = workflow_retired_zip_publish()
    contributor_ok, contributor_evidence = contributor_instructions_ready()

    pending_count = status_counts.get("pending", 0)
    released_count = status_counts.get("released", 0)
    retired_count = status_counts.get("retired", 0)

    items = [
        AuditItem(
            "Phase 0",
            "Manifest exists and every resource has an id.",
            MANIFEST_PATH.exists() and bool(resources) and all(resource.get("id") for resource in resources),
            f"{len(resources)} resources loaded from {MANIFEST_PATH.relative_to(ROOT)}",
        ),
        AuditItem(
            "Phase 1",
            "OneDrive manifest copy exists and matches the repo manifest.",
            manifest_copy_synced,
            f"OneDrive copy exists: {MANIFEST_COPY.exists()}",
            "Run `python3 scripts/sync_resource_manifest_to_onedrive.py` after manifest changes."
            if not manifest_copy_synced
            else "",
        ),
        AuditItem(
            "Phase 2",
            "No downloadable binaries remain in the Git website source.",
            repo_binary_count() == 0 and not tracked_binaries,
            f"working-tree binaries: {repo_binary_count()}; tracked binaries: {len(tracked_binaries)}",
            ", ".join(tracked_binaries[:10]) if tracked_binaries else "",
        ),
        AuditItem(
            "Phase 3",
            "All non-retired manifest payloads exist under the OneDrive resource root.",
            not missing_payloads,
            f"present: {present_payloads}; missing: {len(missing_payloads)}; unavailable: {len(unavailable_payloads)}",
            ", ".join(str(resource["id"]) for resource in missing_payloads[:10]) if missing_payloads else "",
        ),
        AuditItem(
            "Phase 3",
            "All non-retired manifest payloads are locally hydrated and non-empty.",
            not unavailable_payloads,
            f"unavailable: {len(unavailable_payloads)}",
            "; ".join(str(resource["id"]) for resource, _ in unavailable_payloads[:10]) if unavailable_payloads else "",
        ),
        AuditItem(
            "Phase 3",
            "Folder bundles are materialized and no source bundle work remains.",
            bundle_counts.get("ready to materialize", 0) == 0
            and bundle_counts.get("source files required", 0) == 0
            and bundle_counts.get("no listed files", 0) == 0
            and bundle_counts.get("unavailable", 0) == 0,
            "; ".join(f"{key}: {bundle_counts.get(key, 0)}" for key in ["present", "unavailable", "ready to materialize", "source files required", "no listed files"]),
        ),
        AuditItem(
            "Phase 3",
            "No generated ZIP archives remain under the OneDrive resource root.",
            onedrive_zip_count() == 0,
            f"ZIP files under ZJE_resource: {onedrive_zip_count()}",
        ),
        AuditItem(
            "Phase 3",
            "Large archive resources are separated under LARGE_ARCHIVES while core resources remain in the main course skeleton.",
            not release_tier_issue_list,
            f"tier layout issues: {len(release_tier_issue_list)}",
            "; ".join(release_tier_issue_list[:10]) if release_tier_issue_list else "",
        ),
        AuditItem(
            "Phase 4",
            "All public release statuses and URLs are internally consistent.",
            not public_url_issue_list,
            f"released: {released_count}; pending: {pending_count}; retired: {retired_count}",
            "; ".join(public_url_issue_list[:10]) if public_url_issue_list else "",
        ),
        AuditItem(
            "Phase 4",
            "All non-retired resources have maintainer-approved public resource links.",
            pending_count == 0,
            f"released: {released_count}; pending: {pending_count}; retired: {retired_count}",
            "Release pending large archives with manual OneDrive links or `scripts/create_onedrive_share_links.py` using an existing Entra app id."
            if pending_count
            else "",
        ),
        AuditItem(
            "Phase 5",
            "Public download CSV contains exactly the released resources and only approved public resource URLs.",
            not download_issue_list,
            f"{len(download_csv_rows())} rows in {DOWNLOAD_CSV.relative_to(ROOT)}",
            "; ".join(download_issue_list[:10]) if download_issue_list else "",
        ),
        AuditItem(
            "Phase 5",
            "Public docs do not expose internal migration/storage text.",
            not public_doc_hits,
            f"public-doc policy hits: {len(public_doc_hits)}",
            "; ".join(public_doc_hits[:10]) if public_doc_hits else "",
        ),
        AuditItem(
            "Phase 5",
            "MkDocs excludes the private resource manifest from public output.",
            mkdocs_excludes_manifest(),
            "resources/resource_manifest.yml is excluded" if mkdocs_excludes_manifest() else "manifest exclude not found",
            "Add `resources/resource_manifest.yml` to `exclude_docs` in mkdocs.yml."
            if not mkdocs_excludes_manifest()
            else "",
        ),
        AuditItem(
            "Phase 6",
            "Deployment no longer packages or publishes generated ZIP downloads.",
            workflow_ok,
            workflow_evidence,
            workflow_evidence if not workflow_ok else "",
        ),
        AuditItem(
            "Phase 6",
            "Built public site does not expose the manifest, local paths, or legacy source URLs.",
            not site_issue_list,
            "site output scan passed" if not site_issue_list else f"site output errors: {len(site_issue_list)}",
            "; ".join(site_issue_list[:10]) if site_issue_list else "",
        ),
        AuditItem(
            "Phase 7",
            "Contributor instructions describe the post-migration resource intake flow without exposing internals.",
            contributor_ok,
            contributor_evidence,
            contributor_evidence if not contributor_ok else "",
        ),
    ]
    return items


def write_report(items: list[AuditItem]) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORT_DIR / "completion_audit.md"
    complete = all(item.passed for item in items)
    lines = [
        "# Resource Migration Completion Audit",
        "",
        "This report maps the current repository, generated site, and local OneDrive sync state to `RESOURCE_MIGRATION_SPEC.md`.",
        "",
        f"Overall status: {'complete' if complete else 'incomplete'}",
        "",
        "| Phase | Requirement | Status | Evidence | Remaining work |",
        "|---|---|---|---|---|",
    ]
    for item in items:
        status = "pass" if item.passed else "fail"
        remaining = item.remaining.replace("|", "\\|") if item.remaining else ""
        evidence = item.evidence.replace("|", "\\|")
        requirement = item.requirement.replace("|", "\\|")
        lines.append(f"| {item.phase} | {requirement} | {status} | {evidence} | {remaining} |")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    items = audit_items()
    output_path = write_report(items)
    failed = [item for item in items if not item.passed]
    print(f"Generated {output_path}")
    if failed:
        print(f"Migration incomplete: {len(failed)} requirement(s) still failing")
        for item in failed:
            print(f"- {item.phase}: {item.requirement}")
            if item.remaining:
                print(f"  remaining: {item.remaining}")
        return 1
    print("Migration completion audit OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
