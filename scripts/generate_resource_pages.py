#!/usr/bin/env python3
"""Generate public resource pages from the resource manifest."""

from __future__ import annotations

import csv
import html
import urllib.parse
from collections import defaultdict
from typing import Any

from resource_manifest import (
    DOCS_DIR,
    GITHUB_RESOURCE_HOSTS,
    REPORT_DIR,
    RESOURCE_DIR,
    is_public_onedrive_url,
    read_manifest,
)

ONEDRIVE_BROWSER_LINKS = {
    "all": {
        "label": "All Resources",
        "description": "Browse the full shared OneDrive library.",
        "url": "https://zjuintl-my.sharepoint.com/:f:/g/personal/yiru_22_intl_zju_edu_cn/IgDoBTOVj1tKQIgVTYuh7EiiARbvwTZYgynoP30JCfSy3Rk?e=AlKMq4",
    },
    "Year1": {
        "label": "Year 1",
        "description": "Open Year 1 folders, inspect files, and download selected items or the whole folder.",
        "url": "https://zjuintl-my.sharepoint.com/:f:/g/personal/yiru_22_intl_zju_edu_cn/IgC2JwUazghaTrQCEYoQ-44kARnLAL1v94ybyAMVFl25ZHg?e=aSnCYW",
    },
    "Year2": {
        "label": "Year 2",
        "description": "Open Year 2 folders, inspect files, and download selected items or the whole folder.",
        "url": "https://zjuintl-my.sharepoint.com/:f:/g/personal/yiru_22_intl_zju_edu_cn/IgAQsSutUsB9SKby83Q5DBL8ARaH6G0SwoRC1PcAGeImmn4?e=c7kbO5",
    },
    "Year3": {
        "label": "Year 3",
        "description": "Open Year 3 folders, inspect files, and download selected items or the whole folder.",
        "url": "https://zjuintl-my.sharepoint.com/:f:/g/personal/yiru_22_intl_zju_edu_cn/IgBFjNEq0SJTRoSULgSHjztQARzlUUuGBtdTGMKUllexUtA?e=GY314i",
    },
    "Year4": {
        "label": "Year 4",
        "description": "Open Year 4 folders, inspect files, and download selected items or the whole folder.",
        "url": "https://zjuintl-my.sharepoint.com/:f:/g/personal/yiru_22_intl_zju_edu_cn/IgCSCCfBxURMSq5JFol9LPT0AUOWaYbFo67D2u_X_O8z508?e=vYnq5P",
    },
}

YEAR_ORDER = ["Year1", "Year2", "Year3", "Year4", "Resources", "all"]
YEAR_LABELS = {
    "Year1": "Year 1",
    "Year2": "Year 2",
    "Year3": "Year 3",
    "Year4": "Year 4",
    "Resources": "Shared Resources",
    "all": "Other Resources",
}

LEGACY_DETAIL_PAGE_ALIASES = {
    "ADS2_exam_skill_bundle.md": ("ADS2 Yiru Exam Skill Bundle", "ADS2_Yiru_exam_skill_bundle.md"),
    "BG2_sum_Yiru.md": ("BG2 Yiru Summary", "BG2_Yiru_summary.md"),
    "Code_Cheatsheet_Yiru.md": ("Code Cheatsheet Yiru Collection", "Code_Cheatsheet_Yiru_collection.md"),
    "GP2_sum_Yiru.md": ("GP2 Yiru Summary", "GP2_Yiru_summary.md"),
    "IBMS3_full_Yiru.md": ("IBMS3 Yiru Full Notes", "IBMS3_Yiru_full_notes.md"),
    "IFBS（theme34).md": ("IFBS2 Yue Theme 3-4 Notes", "IFBS2_Yue_theme3_theme4.md"),
    "IID_4_full_Yiru.md": ("IID4 Yiru Full Notes", "IID4_Yiru_full_notes.md"),
    "MBE3_sum_Yiru.md": ("MBE3 Yiru Summary", "MBE3_Yiru_summary.md"),
    "PoN3_full_Yiru.md": ("PoN3 Yiru Full Notes", "PoN3_Yiru_full_notes.md"),
    "pon.md": ("PoN3 Yue Notes", "PoN3_Yue_notes.md"),
}


def anchor(course: str) -> str:
    return "course-" + course.lower().replace("_", "-")


def md_text(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", "<br>").strip()


def markdown_url(url: str) -> str:
    """Percent-encode URL paths so Markdown links survive spaces and Unicode."""
    if not url:
        return ""
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme in {"http", "https"}:
        path = urllib.parse.quote(urllib.parse.unquote(parsed.path), safe="/:@")
        query = urllib.parse.quote(urllib.parse.unquote(parsed.query), safe="=&%")
        fragment = urllib.parse.quote(urllib.parse.unquote(parsed.fragment), safe="")
        return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, query, fragment))
    return urllib.parse.quote(url, safe="/._-:#?=&%")


def markdown_path(path: str) -> str:
    return urllib.parse.quote(path, safe="/._-")


def type_label(value: str) -> str:
    return value.replace("_", " ").title()


def tier_label(value: str) -> str:
    if value == "large_archive":
        return "Large Archive"
    return value.replace("_", " ").title()


def year_key(resource: dict[str, Any]) -> str:
    value = str(resource.get("year_group") or "").strip()
    if value in YEAR_LABELS:
        return value
    return "all"


def onedrive_key(resource: dict[str, Any]) -> str:
    key = year_key(resource)
    if key in ONEDRIVE_BROWSER_LINKS:
        return key
    return "all"


def onedrive_link(resource: dict[str, Any]) -> dict[str, str]:
    return ONEDRIVE_BROWSER_LINKS[onedrive_key(resource)]


def github_label(resource: dict[str, Any]) -> str:
    if resource["resource_type"] in {"course_package", "folder_bundle"}:
        return "Open GitHub folder"
    return "Download from GitHub"


def onedrive_label(resource: dict[str, Any]) -> str:
    link = onedrive_link(resource)
    if onedrive_key(resource) == "all":
        return "Browse all resources"
    return f"Browse {link['label']} folder"


def released_public_url(resource: dict[str, Any]) -> str:
    if resource["public_url_status"] != "released":
        return ""
    return str(resource.get("public_url") or "").strip()


def public_url_channel(url: str) -> str:
    if not url:
        return ""
    if is_public_onedrive_url(url):
        return "onedrive"
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme == "https" and parsed.netloc.lower() in GITHUB_RESOURCE_HOSTS:
        return "github"
    return "direct"


def github_url(resource: dict[str, Any]) -> str:
    url = released_public_url(resource)
    if public_url_channel(url) == "github":
        return url
    return ""


def onedrive_direct_url(resource: dict[str, Any]) -> str:
    url = released_public_url(resource)
    if public_url_channel(url) == "onedrive":
        return url
    return ""


def github_cell(resource: dict[str, Any]) -> str:
    url = github_url(resource)
    if not url:
        return '<span class="resource-muted">Not mirrored</span>'
    return f"[{github_label(resource)}]({markdown_url(url)})"


def onedrive_cell(resource: dict[str, Any]) -> str:
    direct_url = onedrive_direct_url(resource)
    if direct_url:
        return f"[Open OneDrive link]({markdown_url(direct_url)})"
    link = onedrive_link(resource)
    return f"[{onedrive_label(resource)}]({markdown_url(link['url'])})"


def access_summary(resource: dict[str, Any]) -> str:
    parts: list[str] = []
    url = github_url(resource)
    if url:
        parts.append(f"GitHub: [{github_label(resource)}]({markdown_url(url)})")
    parts.append(f"OneDrive: {onedrive_cell(resource)}")
    return " | ".join(parts)


def active_resources(resources: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [resource for resource in resources if resource["public_url_status"] != "retired"]


def sort_key(resource: dict[str, Any]) -> tuple[int, str, str, str]:
    key = year_key(resource)
    year_index = YEAR_ORDER.index(key) if key in YEAR_ORDER else len(YEAR_ORDER)
    return (
        year_index,
        str(resource.get("course", "")),
        str(resource.get("resource_type", "")),
        str(resource.get("title", "")),
    )


def grouped_by_year(resources: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for resource in sorted(resources, key=sort_key):
        grouped[year_key(resource)].append(resource)
    return grouped


def ordered_year_keys(grouped: dict[str, list[dict[str, Any]]]) -> list[str]:
    keys = list(grouped)
    return sorted(keys, key=lambda key: YEAR_ORDER.index(key) if key in YEAR_ORDER else len(YEAR_ORDER))


def table_for_resources(resources: list[dict[str, Any]], *, include_status: bool = False) -> list[str]:
    if include_status:
        lines = [
            "| Resource | Course | Contributor | Type | Tier | GitHub | OneDrive |",
            "|---|---|---|---|---|---|---|",
        ]
    else:
        lines = [
            "| Resource | Course | Contributor | Type | GitHub | OneDrive |",
            "|---|---|---|---|---|---|",
        ]

    for resource in sorted(resources, key=sort_key):
        if include_status:
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_text(resource["title"]),
                        md_text(resource["course"]),
                        md_text(resource["contributor"]),
                        type_label(str(resource["resource_type"])),
                        tier_label(str(resource.get("release_tier", "core"))),
                        github_cell(resource),
                        onedrive_cell(resource),
                    ]
                )
                + " |"
            )
        else:
            lines.append(
                "| "
                + " | ".join(
                    [
                        md_text(resource["title"]),
                        md_text(resource["course"]),
                        md_text(resource["contributor"]),
                        type_label(str(resource["resource_type"])),
                        github_cell(resource),
                        onedrive_cell(resource),
                    ]
                )
                + " |"
            )
    return lines


def write_download_csv(resources: list[dict[str, Any]]) -> None:
    path = RESOURCE_DIR / "download_links.csv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "id",
                "title",
                "course",
                "contributor",
                "resource_type",
                "release_tier",
                "public_url_status",
                "public_url",
                "github_url",
                "onedrive_url",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        for resource in resources:
            if resource["public_url_status"] != "released":
                continue
            row = {key: resource.get(key, "") for key in writer.fieldnames}
            row["github_url"] = github_url(resource)
            row["onedrive_url"] = onedrive_direct_url(resource) or onedrive_link(resource)["url"]
            writer.writerow(row)


def folder_card_html(key: str, resources: list[dict[str, Any]]) -> str:
    link = ONEDRIVE_BROWSER_LINKS[key]
    if key == "all":
        count = len(active_resources(resources))
    else:
        count = sum(1 for resource in active_resources(resources) if year_key(resource) == key)
    return "\n".join(
        [
            '<article class="resource-folder-card">',
            f'<h3>{html.escape(link["label"])}</h3>',
            f'<p>{html.escape(link["description"])}</p>',
            f'<div class="resource-folder-count">{count} listed resources</div>',
            f'<a class="resource-button resource-button--onedrive" href="{html.escape(markdown_url(link["url"]))}" target="_blank" rel="noopener">Browse in OneDrive</a>',
            "</article>",
        ]
    )


def write_index(resources: list[dict[str, Any]]) -> None:
    active = active_resources(resources)
    github_mirrors = [resource for resource in active if github_url(resource)]
    large_archives = [resource for resource in active if str(resource.get("release_tier")) == "large_archive"]
    courses = sorted({resource["course"] for resource in active})

    lines = [
        "# Resource Center",
        "",
        '<section class="resource-hero">',
        "<div>",
        "<p class=\"resource-kicker\">ZJE study materials</p>",
        "<h2>Use GitHub for direct mirrors, or OneDrive for the complete shared folders.</h2>",
        "<p>Each resource row lists the available routes. GitHub is fastest for mirrored PDFs and Markdown bundles. OneDrive is the complete browser for large archives, Office files, OneNote, XMind, and course folders.</p>",
        "</div>",
        "</section>",
        "",
        '<section class="resource-kpi-grid">',
        f'<div class="resource-kpi"><strong>{len(active)}</strong><span>resources listed</span></div>',
        f'<div class="resource-kpi"><strong>{len(github_mirrors)}</strong><span>GitHub mirrors</span></div>',
        f'<div class="resource-kpi"><strong>{len(large_archives)}</strong><span>OneDrive-first archives</span></div>',
        f'<div class="resource-kpi"><strong>{len(courses)}</strong><span>course collections</span></div>',
        "</section>",
        "",
        "## How Downloads Work",
        "",
        '<section class="resource-route-grid">',
        '<article class="resource-route-card"><h3>GitHub</h3><p>Use the GitHub column when a resource has a direct mirror. It opens a raw file or a browsable folder in the resource repository.</p></article>',
        '<article class="resource-route-card"><h3>OneDrive</h3><p>Use the OneDrive column when you want the complete course folder, mixed file formats, or large archives.</p></article>',
        '<article class="resource-route-card"><h3>Course Pages</h3><p>Course pages remain for reading Markdown notes. Resource tables below are the source of truth for downloadable files and folder bundles.</p></article>',
        "</section>",
        "",
        "## OneDrive Folders",
        "",
        '<section class="resource-folder-grid">',
    ]
    for key in ["all", "Year1", "Year2", "Year3", "Year4"]:
        lines.append(folder_card_html(key, resources))
    lines.extend(
        [
            "</section>",
            "",
            "## Resource Catalog",
            "",
            "Every non-retired resource appears once below. If a GitHub mirror exists, it is shown next to the matching OneDrive folder route.",
            "",
        ]
    )

    grouped_active = grouped_by_year(active)
    for key in ordered_year_keys(grouped_active):
        lines.extend([f"### {YEAR_LABELS.get(key, key)}", ""])
        by_course: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for resource in grouped_active[key]:
            by_course[resource["course"]].append(resource)
        for course in sorted(by_course):
            lines.extend([f'<h4 id="{anchor(course)}">{course}</h4>', ""])
            lines.extend(table_for_resources(by_course[course], include_status=True))
            lines.append("")

    (RESOURCE_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def write_status(resources: list[dict[str, Any]]) -> None:
    lines = [
        "# Resource Status",
        "",
        "This maintainer-facing summary omits private local paths. The authoritative storage paths are in `resource_manifest.yml`.",
        "",
        "For current migration gates, see `migration_status.md`. For local OneDrive folder bundle payload readiness, see `folder_bundle_status.md`. For share-link work, see `public_link_release_queue.md`.",
        "",
        "| ID | Course | Contributor | Tier | Status | Access Channel | Visibility | Source Pages |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for resource in sorted(resources, key=lambda item: item["id"]):
        sources = "<br>".join(resource.get("website_sources", []))
        channel_parts = []
        if github_url(resource):
            channel_parts.append("GitHub direct")
        channel_parts.append("OneDrive browser")
        channel = " + ".join(channel_parts)
        lines.append(
            f"| `{resource['id']}` | {md_text(resource['course'])} | {md_text(resource['contributor'])} | {tier_label(str(resource.get('release_tier', 'core')))} | {resource['public_url_status']} | {channel} | {resource['visibility']} | {sources} |"
        )
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    (REPORT_DIR / "resource_status.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_packages_index(resources: list[dict[str, Any]]) -> None:
    package_resources = [
        resource
        for resource in active_resources(resources)
        if resource["resource_type"] in {"course_package", "folder_bundle"}
    ]
    lines = [
        "# Resource Package Index",
        "",
        "Course packages and folder bundles are listed here with both routes. GitHub appears when a safe mirror exists; OneDrive is the complete folder browser.",
        "",
        "| Resource | Course | Contributor | Type | Tier | GitHub | OneDrive |",
        "|---|---|---|---|---|---|---|",
    ]
    if not package_resources:
        lines.append("| No active packages yet |  |  |  |  |  |  |")
    for resource in sorted(package_resources, key=sort_key):
        lines.append(
            f"| {md_text(resource['title'])} | {md_text(resource['course'])} | {md_text(resource['contributor'])} | {type_label(resource['resource_type'])} | {tier_label(str(resource.get('release_tier', 'core')))} | {github_cell(resource)} | {onedrive_cell(resource)} |"
        )
    (DOCS_DIR / "ZIPS_INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_folder_contents_overview(resources: list[dict[str, Any]]) -> None:
    folder_resources = [
        resource
        for resource in active_resources(resources)
        if resource["resource_type"] == "folder_bundle"
    ]
    lines = [
        "# Folder Bundle Contents Overview",
        "",
        "This folder contains lightweight contents pages for folder bundles. Use GitHub for mirrored bundles and OneDrive for the complete shared folder browser.",
        "",
        "| Resource | Course | Contributor | Tier | Detail Page | GitHub | OneDrive |",
        "|---|---|---|---|---|---|---|",
    ]
    for resource in sorted(folder_resources, key=sort_key):
        detail_pages = [
            source
            for source in resource.get("website_sources", [])
            if source.startswith("ZJE_Collection/zip_contents/")
        ]
        if detail_pages:
            rel = detail_pages[0].replace("ZJE_Collection/zip_contents/", "")
            detail = f"[contents]({markdown_path(rel)})"
        else:
            detail = ""
        lines.append(
            f"| {md_text(resource['title'])} | {md_text(resource['course'])} | {md_text(resource['contributor'])} | {tier_label(str(resource.get('release_tier', 'core')))} | {detail} | {github_cell(resource)} | {onedrive_cell(resource)} |"
        )
    (DOCS_DIR / "zip_contents" / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_folder_detail_headers(resources: list[dict[str, Any]]) -> None:
    for resource in resources:
        if resource["resource_type"] != "folder_bundle":
            continue
        detail_pages = [
            source
            for source in resource.get("website_sources", [])
            if source.startswith("ZJE_Collection/zip_contents/")
        ]
        if not detail_pages:
            continue
        path = DOCS_DIR.parent / detail_pages[0]
        if not path.exists():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        output: list[str] = []
        replaced_status = False
        for idx, line in enumerate(lines):
            if idx == 0 and line.startswith("# "):
                output.append(f"# Contents of {resource['title']}")
                continue
            if not replaced_status and (line.startswith("Download:") or line.startswith("Access:")):
                output.append(f"Access: {access_summary(resource)}")
                replaced_status = True
                continue
            output.append(line)
        path.write_text("\n".join(output) + "\n", encoding="utf-8")


def write_legacy_detail_aliases() -> None:
    alias_dir = DOCS_DIR / "zip_contents"
    alias_dir.mkdir(parents=True, exist_ok=True)
    for legacy_name, (title, target_name) in LEGACY_DETAIL_PAGE_ALIASES.items():
        target_route = "../" + target_name.removesuffix(".md") + "/"
        lines = [
            f'<meta http-equiv="refresh" content="0; url={target_route}">',
            "",
            f"# Moved: {title}",
            "",
            f"This folder contents page moved to [{title}]({markdown_path(target_name)}).",
            "",
            "<script>",
            f'window.location.replace("{target_route}" + window.location.search + window.location.hash);',
            "</script>",
        ]
        (alias_dir / legacy_name).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    RESOURCE_DIR.mkdir(parents=True, exist_ok=True)
    resources = read_manifest()
    write_download_csv(resources)
    write_index(resources)
    write_status(resources)
    write_packages_index(resources)
    write_folder_contents_overview(resources)
    write_folder_detail_headers(resources)
    write_legacy_detail_aliases()
    print(f"Generated resource pages for {len(resources)} resources")


if __name__ == "__main__":
    main()
