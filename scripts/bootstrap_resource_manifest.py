#!/usr/bin/env python3
"""Create the initial ZJE resource manifest from the current repository state."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

from resource_manifest import DOCS_DIR, MANIFEST_PATH, write_manifest

MIGRATION_DATE = "2026-05-20"
DRIVE_FOLDER_URL = "https://drive.google.com/drive/folders/1_ttbZASdiHPW9xt0GSjVjFHF5MAPk2fv?usp=drive_link"

YEAR_GROUP = {
    "CHEM1": "Year1",
    "IBI1": "Year1",
    "IBMS1": "Year1",
    "ICMB1": "Year1",
    "MATH1": "Year1",
    "ADS2": "Year2",
    "BG2": "Year2",
    "BaO2": "Year2",
    "DST2": "Year2",
    "GP2": "Year2",
    "IFBS2": "Year2",
    "MI2": "Year2",
    "BMI3": "Year3",
    "CBSB3": "Year3",
    "IBMS3": "Year3",
    "IN3_full": "Year3",
    "MBE3": "Year3",
    "PoN3": "Year3",
    "BIA4": "Year4",
    "IBMS4": "Year4",
    "IID_4": "Year4",
    "Code_Cheatsheet": "Resources",
}

COURSE_PACKAGES = [
    ("ads2-hal-2022-2023", "ADS2 Hal Materials", "ADS2", "Hal", "2022-2023", "https://drive.google.com/file/d/1Fl2WtzDZoyEqi3MLvilNCOUIeTbQTl-Y/view?usp=sharing", ["ZJE_Collection/ADS2/index.md", "ZJE_Collection/ADS2/Hal/ADS2_2022_2023_link.txt"]),
    ("bg2-hal-2022-2023", "BG2 Hal Materials", "BG2", "Hal", "2022-2023", "https://drive.google.com/file/d/1M41n2IJuvcm_0eYSWqiJpg2-tatguquG/view?usp=sharing", ["ZJE_Collection/BG2/index.md", "ZJE_Collection/BG2/Hal/BG2_2022_2023_link.txt"]),
    ("bia4-hal-2024-2025", "BIA4 Hal Materials", "BIA4", "Hal", "2024-2025", "https://drive.google.com/file/d/1QkXJCPLbmC3-H4PLHZLA6fEQm3eZzXAL/view?usp=sharing", ["ZJE_Collection/BIA4/index.md", "ZJE_Collection/BIA4/Hal/BIA4_2024_2025_link.txt"]),
    ("bmi3-hal-2023-2024", "BMI3 Hal Materials", "BMI3", "Hal", "2023-2024", "https://drive.google.com/file/d/1QB0Z1TYR2U0DTcqwliKIKlJaJ68Umau2/view?usp=sharing", ["ZJE_Collection/BMI3/index.md", "ZJE_Collection/BMI3/Hal/BMI3_2023_2024_link.txt"]),
    ("cbsb3-hal-2023-2024", "CBSB3 Hal Materials", "CBSB3", "Hal", "2023-2024", "https://drive.google.com/file/d/1aiyIviT2sEW57mjtEKqtddtFxK4n8C4I/view?usp=sharing", ["ZJE_Collection/CBSB3/index.md", "ZJE_Collection/CBSB3/Hal/CBSB3_2023_2024_link.txt"]),
    ("chem1-hal-2021-2022", "CHEM1 Hal Materials", "CHEM1", "Hal", "2021-2022", "https://drive.google.com/file/d/12qrRLagEU9GqZkHguhvcXjDtLmpt5xw9/view?usp=sharing", ["ZJE_Collection/CHEM1/index.md", "ZJE_Collection/CHEM1/Hal/CHEM_2021_2022_link.txt"]),
    ("dst2-hal-2022-2023", "DST2 Hal Materials", "DST2", "Hal", "2022-2023", "https://drive.google.com/file/d/165q4ynH7l4o_Sc8no5C8sqM7MSWMvVye/view?usp=sharing", ["ZJE_Collection/DST2/index.md", "ZJE_Collection/DST2/Hal/DST2_2022_2023_link.txt"]),
    ("gp2-hal-2022-2023", "GP2 Hal Materials", "GP2", "Hal", "2022-2023", "https://drive.google.com/file/d/1P4oNZSKyOg9kB8Ie05srfcW8GpwyFp08/view?usp=sharing", ["ZJE_Collection/GP2/index.md", "ZJE_Collection/GP2/Hal/GP2_2022_2023_link.txt"]),
    ("ibi1-hal-2021-2022", "IBI1 Hal Materials", "IBI1", "Hal", "2021-2022", "https://drive.google.com/file/d/19O7639tb0HM0yrQC_iWNIh360JaLW4al/view?usp=sharing", ["ZJE_Collection/IBI1/index.md", "ZJE_Collection/IBI1/Hal/IBI1_2021_2022_link.txt"]),
    ("ibms1-hal-2021-2022", "IBMS1 Hal Materials", "IBMS1", "Hal", "2021-2022", "https://drive.google.com/file/d/1lDYh5ghRXBE8z3et_ShQg3WCjwoq7egi/view?usp=sharing", ["ZJE_Collection/IBMS1/index.md", "ZJE_Collection/IBMS1/Hal/IBMS1_2021_2022_link.txt"]),
    ("ibms3-hal-2023-2024", "IBMS3 Hal Materials", "IBMS3", "Hal", "2023-2024", "https://drive.google.com/file/d/1_0Snof-NLIY3lqJHfND0-KcFXpHnJM2W/view?usp=sharing", ["ZJE_Collection/IBMS3/index.md", "ZJE_Collection/IBMS3/Hal/IBMS3_2023_2024_link.txt"]),
    ("ibms4-hal-2024-2025", "IBMS4 Hal Materials", "IBMS4", "Hal", "2024-2025", "https://drive.google.com/file/d/1XcHq_gENuok68vWcGgfdZlpxAXnygs9J/view?usp=sharing", ["ZJE_Collection/IBMS4/index.md", "ZJE_Collection/IBMS4/Hal/IBMS4_2024_2025_link.txt"]),
    ("icmb1-hal-2021-2022", "ICMB1 Hal Materials", "ICMB1", "Hal", "2021-2022", "https://drive.google.com/file/d/1-F9q2f747vj1VniamqBVrcKYt_Fn5iH0/view?usp=sharing", ["ZJE_Collection/ICMB1/index.md", "ZJE_Collection/ICMB1/Hal/ICMB1_2021_2022_link.txt"]),
    ("ifbs2-hal-2022-2023", "IFBS2 Hal Materials", "IFBS2", "Hal", "2022-2023", "https://drive.google.com/file/d/1lgH-OKJ_kiLtY1RT4h6Taky-VZNVfUoA/view?usp=sharing", ["ZJE_Collection/IFBS2/index.md", "ZJE_Collection/IFBS2/Hal/IFBS2_2022_2023_link.txt"]),
    ("iid4-hal-2024-2025", "IID_4 Hal Materials", "IID_4", "Hal", "2024-2025", "https://drive.google.com/file/d/1croWrQe1agk-zbvIklNjL-roso30TlZ_/view?usp=sharing", ["ZJE_Collection/IID_4/index.md", "ZJE_Collection/IID_4/Hal/IID4_2024_2025_link.txt"]),
    ("math1-hal-calculus-2021-2022", "MATH1 Calculus Materials", "MATH1", "Hal", "2021-2022", "https://drive.google.com/file/d/1KUHEEFDBXyBm7Oh1rY_DLn2DcPFOQed7/view?usp=sharing", ["ZJE_Collection/MATH1/index.md", "ZJE_Collection/MATH1/Hal/MATH_2021_2022_link.txt"]),
    ("math1-hal-statistics-2021-2022", "MATH1 Statistics Materials", "MATH1", "Hal", "2021-2022", "https://drive.google.com/file/d/1vnRG-aoylkFqrY6-cSYmbtZSIeNBYlim/view?usp=sharing", ["ZJE_Collection/MATH1/index.md", "ZJE_Collection/MATH1/Hal/MATH_2021_2022_link.txt"]),
    ("mbe3-hal-2023-2024", "MBE3 Hal Materials", "MBE3", "Hal", "2023-2024", "https://drive.google.com/file/d/1GC6xVmn8OFAWXFWk_nmLOwHJy7hro2DJ/view?usp=sharing", ["ZJE_Collection/MBE3/index.md", "ZJE_Collection/MBE3/Hal/MBE3_2023_2024_link.txt"]),
    ("pon3-hal-2023-2024", "PoN3 Hal Materials", "PoN3", "Hal", "2023-2024", "https://drive.google.com/file/d/1DXCndsKcLVPyI3PtXEGB4igvw_cncc89/view?usp=sharing", ["ZJE_Collection/PoN3/index.md", "ZJE_Collection/PoN3/Hal/PoN3_2023_2024_link.txt"]),
]

FOLDER_BUNDLES = [
    ("zip-bg-maps-xiaoran-etal", "BG导图合集_lxrwyqlxf", "BG2", "Xiaoran_etal", "ZJE_Collection/zip_contents/BG导图合集_lxrwyqlxf.md"),
    ("zip-ifbs-mindmap-xiaoran-etal", "思维导图IFBS_lxr", "IFBS2", "Xiaoran_etal", "ZJE_Collection/zip_contents/思维导图IFBS_lxr.md"),
    ("zip-in-lxfwyqlxr", "IN_lxfwyqlxr", "IN3_full", "Xiaoran_etal", "ZJE_Collection/zip_contents/IN_lxfwyqlxr.md"),
    ("zip-mbe-lxrwyalxf", "MBE_lxrwyalxf", "MBE3", "Xiaoran_etal", "ZJE_Collection/zip_contents/MBE_lxrwyalxf.md"),
    ("zip-pon-review-lxrwyqlxf", "pon复习资料_lxrwyqlxf", "PoN3", "Xiaoran_etal", "ZJE_Collection/zip_contents/pon复习资料_lxrwyqlxf.md"),
    ("zip-ifbs-theme34-yue", "IFBS（theme34)", "IFBS2", "Yue", "ZJE_Collection/zip_contents/IFBS（theme34).md"),
    ("zip-pon-yue", "pon", "PoN3", "Yue", "ZJE_Collection/zip_contents/pon.md"),
    ("zip-bg2-sum-yiru", "BG2_sum_Yiru", "BG2", "Yiru", "ZJE_Collection/zip_contents/BG2_sum_Yiru.md"),
    ("zip-code-cheatsheet-yiru", "Code_Cheatsheet_Yiru", "Code_Cheatsheet", "Yiru", "ZJE_Collection/zip_contents/Code_Cheatsheet_Yiru.md"),
    ("zip-gp2-sum-yiru", "GP2_sum_Yiru", "GP2", "Yiru", "ZJE_Collection/zip_contents/GP2_sum_Yiru.md"),
    ("zip-ibms3-full-yiru", "IBMS3_full_Yiru", "IBMS3", "Yiru", "ZJE_Collection/zip_contents/IBMS3_full_Yiru.md"),
    ("zip-iid4-full-yiru", "IID_4_full_Yiru", "IID_4", "Yiru", "ZJE_Collection/zip_contents/IID_4_full_Yiru.md"),
    ("zip-mbe3-sum-yiru", "MBE3_sum_Yiru", "MBE3", "Yiru", "ZJE_Collection/zip_contents/MBE3_sum_Yiru.md"),
    ("zip-pon3-full-yiru", "PoN3_full_Yiru", "PoN3", "Yiru", "ZJE_Collection/zip_contents/PoN3_full_Yiru.md"),
]


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "resource"


def checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def package_resource(item: tuple[str, str, str, str, str, str, list[str]]) -> dict:
    rid, title, course, contributor, year, url, sources = item
    local_slug = rid.replace("-", "_")
    return {
        "id": rid,
        "title": title,
        "course": course,
        "year_group": YEAR_GROUP[course],
        "academic_year": year,
        "contributor": contributor,
        "resource_type": "course_package",
        "release_tier": "core",
        "storage_provider": "onedrive",
        "local_onedrive_path": f"COURSES/{YEAR_GROUP[course]}/{course}/{contributor}/{local_slug}",
        "public_url": "",
        "public_url_status": "pending",
        "original_source_url": url,
        "original_repo_path": "",
        "website_sources": sources,
        "description": f"{title}.",
        "license_note": "Educational sharing; non-commercial use only.",
        "visibility": "pending_review",
        "version": 1,
        "checksum_sha256": "",
        "size_bytes": None,
        "migrated_at": "",
        "public_link_released_at": "",
        "notes": "Legacy Google Drive package; awaiting OneDrive copy and share link.",
    }


def folder_bundle_resource(item: tuple[str, str, str, str, str]) -> dict:
    rid, title, course, contributor, detail_page = item
    return {
        "id": rid,
        "title": title,
        "course": course,
        "year_group": YEAR_GROUP[course],
        "academic_year": "",
        "contributor": contributor,
        "resource_type": "folder_bundle",
        "release_tier": "core",
        "storage_provider": "onedrive",
        "local_onedrive_path": f"COURSES/{YEAR_GROUP[course]}/{course}/{contributor}/{title}",
        "public_url": "",
        "public_url_status": "pending",
        "original_source_url": DRIVE_FOLDER_URL,
        "original_repo_path": "",
        "website_sources": ["ZJE_Collection/ZIPS_INDEX.md", detail_page],
        "description": f"Folder bundle documented in {detail_page}.",
        "license_note": "Educational sharing; non-commercial use only.",
        "visibility": "pending_review",
        "version": 1,
        "checksum_sha256": "",
        "size_bytes": None,
        "migrated_at": "",
        "public_link_released_at": "",
        "notes": "Folder bundle awaiting OneDrive share link; no ZIP archive is generated.",
    }


def binary_resource(path: Path) -> dict:
    rel = path.relative_to(DOCS_DIR.parent).as_posix()
    parts = path.relative_to(DOCS_DIR).parts
    is_mirror = parts[:2] == ("zip_contents", "Yue")

    if is_mirror:
        course = "zip_contents"
        contributor = "Yue"
        year = "Archive"
        resource_type = "retired_mirror"
        visibility = "retired"
        status = "retired"
        target = f"ARCHIVE/removed_from_website/zip_contents/Yue/{path.name}"
    else:
        course = parts[0]
        contributor = parts[1] if len(parts) > 1 else "unknown"
        year = YEAR_GROUP.get(course, "Resources")
        resource_type = "individual_file"
        visibility = "pending_review"
        status = "pending"
        target = f"COURSES/{year}/{course}/{contributor}/{path.name}"

    digest = checksum(path)
    short = digest[:8]
    rid = f"{slugify(course)}-{slugify(contributor)}-{slugify(path.stem)}-{short}"

    return {
        "id": rid,
        "title": path.name,
        "course": course,
        "year_group": year,
        "academic_year": "",
        "contributor": contributor,
        "resource_type": resource_type,
        "release_tier": "retired" if resource_type == "retired_mirror" else "core",
        "storage_provider": "onedrive",
        "local_onedrive_path": target,
        "public_url": "",
        "public_url_status": status,
        "original_source_url": "",
        "original_repo_path": rel,
        "website_sources": [rel],
        "description": f"Standalone file formerly stored at {rel}.",
        "license_note": "Educational sharing; non-commercial use only.",
        "visibility": visibility,
        "version": 1,
        "checksum_sha256": digest,
        "size_bytes": path.stat().st_size,
        "migrated_at": "",
        "public_link_released_at": "",
        "notes": "Copied to OneDrive during local-binary migration." if not is_mirror else "Duplicate website mirror; keep archived only.",
    }


def main() -> None:
    binaries = sorted(
        path
        for path in DOCS_DIR.rglob("*")
        if path.suffix.lower() in {".pdf", ".docx", ".pptx", ".xlsx", ".zip"}
    )
    resources = [package_resource(item) for item in COURSE_PACKAGES]
    resources.extend(folder_bundle_resource(item) for item in FOLDER_BUNDLES)
    resources.extend(binary_resource(path) for path in binaries)
    write_manifest(resources, MANIFEST_PATH)
    print(f"Wrote {MANIFEST_PATH.relative_to(DOCS_DIR.parent)} with {len(resources)} resources")


if __name__ == "__main__":
    main()
