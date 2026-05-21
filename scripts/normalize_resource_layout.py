#!/usr/bin/env python3
"""Normalize public resource payload names and remove duplicate loose copies.

The resource website now shows GitHub and OneDrive as two routes to the same
resource record. This script keeps the storage layout aligned with that model:

- contributor folders contain resource units, not duplicate loose copies;
- folder bundles use clear course/contributor names;
- public PDF payloads use stable, descriptive, ASCII filenames where practical;
- individual resource records point into the bundle when the file is already a
  bundle member.

Run without ``--execute`` to print and write a plan. Run with ``--execute`` only
after reviewing the plan, because it renames files inside the local OneDrive
resource tree and updates the website manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from resource_manifest import MANIFEST_PATH, REPORT_DIR, ROOT, read_manifest, write_manifest

ONEDRIVE_ROOT = Path(
    "/Users/eric_yiru/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource"
)
RESOURCE_REPO_URL = "https://github.com/CHENyiru3/awesome_ZJE_resource"
RAW_BASE_URL = "https://raw.githubusercontent.com/CHENyiru3/awesome_ZJE_resource/main"
REPORT_PATH = REPORT_DIR / "resource_layout_normalization.md"


@dataclass(frozen=True)
class ResourceUpdate:
    title: str
    local_onedrive_path: str
    detail_page: str | None = None


@dataclass(frozen=True)
class Move:
    old: str
    new: str
    kind: str


RESOURCE_UPDATES: dict[str, ResourceUpdate] = {
    "ads2-exam-skill-bundle-yiru": ResourceUpdate(
        "ADS2 Yiru Exam Skill Bundle",
        "COURSES/Year2/ADS2/Yiru/ADS2_Yiru_exam_skill_bundle",
        "ZJE_Collection/zip_contents/ADS2_Yiru_exam_skill_bundle.md",
    ),
    "zip-bg2-sum-yiru": ResourceUpdate(
        "BG2 Yiru Summary",
        "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary",
        "ZJE_Collection/zip_contents/BG2_Yiru_summary.md",
    ),
    "zip-code-cheatsheet-yiru": ResourceUpdate(
        "Code Cheatsheet Yiru Collection",
        "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection",
        "ZJE_Collection/zip_contents/Code_Cheatsheet_Yiru_collection.md",
    ),
    "zip-gp2-sum-yiru": ResourceUpdate(
        "GP2 Yiru Summary",
        "COURSES/Year2/GP2/Yiru/GP2_Yiru_summary",
        "ZJE_Collection/zip_contents/GP2_Yiru_summary.md",
    ),
    "zip-ibms3-full-yiru": ResourceUpdate(
        "IBMS3 Yiru Full Notes",
        "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes",
        "ZJE_Collection/zip_contents/IBMS3_Yiru_full_notes.md",
    ),
    "zip-ifbs-theme34-yue": ResourceUpdate(
        "IFBS2 Yue Theme 3-4 Notes",
        "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4",
        "ZJE_Collection/zip_contents/IFBS2_Yue_theme3_theme4.md",
    ),
    "zip-iid4-full-yiru": ResourceUpdate(
        "IID4 Yiru Full Notes",
        "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes",
        "ZJE_Collection/zip_contents/IID4_Yiru_full_notes.md",
    ),
    "zip-mbe3-sum-yiru": ResourceUpdate(
        "MBE3 Yiru Summary",
        "COURSES/Year3/MBE3/Yiru/MBE3_Yiru_summary",
        "ZJE_Collection/zip_contents/MBE3_Yiru_summary.md",
    ),
    "zip-pon-yue": ResourceUpdate(
        "PoN3 Yue Notes",
        "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes",
        "ZJE_Collection/zip_contents/PoN3_Yue_notes.md",
    ),
    "zip-pon3-full-yiru": ResourceUpdate(
        "PoN3 Yiru Full Notes",
        "COURSES/Year3/PoN3/Yiru/PoN3_Yiru_full_notes",
        "ZJE_Collection/zip_contents/PoN3_Yiru_full_notes.md",
    ),
    "bg2-yiru-collection-of-disease-83195e15": ResourceUpdate(
        "BG2 Yiru Disease Collection.pdf",
        "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_disease_collection.pdf",
    ),
    "bg2-yiru-collection-of-technology-6df3a98f": ResourceUpdate(
        "BG2 Yiru Technology Collection.pdf",
        "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_technology_collection.pdf",
    ),
    "bg2-yiru-calculation-c4ec76cf": ResourceUpdate(
        "BG2 Yiru Calculations.pdf",
        "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_calculations.pdf",
    ),
    "bao2-yue-bao-b4a4d26a": ResourceUpdate(
        "BaO2 Yue Incomplete Notes.pdf",
        "COURSES/Year2/BaO2/Yue/BaO2_Yue_incomplete_notes.pdf",
    ),
    "code-cheatsheet-yiru-java-sum-yiru-d19faa4c": ResourceUpdate(
        "Code Cheatsheet Yiru Java Summary.pdf",
        "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_summary.pdf",
    ),
    "code-cheatsheet-yiru-r-etc-z-library-b26e5231": ResourceUpdate(
        "Code Cheatsheet Yiru R Data Science Z-Library.pdf",
        "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_R_data_science_Z-Library.pdf",
    ),
    "code-cheatsheet-yiru-sql-cheat-sheet-02d7f2aa": ResourceUpdate(
        "Code Cheatsheet Yiru SQL Cheat Sheet.pdf",
        "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_SQL_cheat_sheet.pdf",
    ),
    "code-cheatsheet-yiru-base-r-cheat-sheet-550428b5": ResourceUpdate(
        "Code Cheatsheet Yiru Base R Cheat Sheet.pdf",
        "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Base_R_cheat_sheet.pdf",
    ),
    "code-cheatsheet-yiru-data-visualization-4c76c19d": ResourceUpdate(
        "Code Cheatsheet Yiru Data Visualization.pdf",
        "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Data_visualization.pdf",
    ),
    "code-cheatsheet-yiru-java-cheat-sheet-comprehensive-guide-a8c2150f": ResourceUpdate(
        "Code Cheatsheet Yiru Java Comprehensive Guide.pdf",
        "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_cheat_sheet_comprehensive_guide.pdf",
    ),
    "gp2-yiru-gp-526d301a": ResourceUpdate(
        "GP2 Yiru Outline.pdf",
        "COURSES/Year2/GP2/Yiru/GP2_Yiru_summary/GP2_Yiru_outline.pdf",
    ),
    "ibms3-yiru-experimental-design-ethics-ad7c5ce0": ResourceUpdate(
        "IBMS3 Yiru Experimental Design and Ethics.pdf",
        "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_design_and_ethics.pdf",
    ),
    "ibms3-yiru-ibms-dry-lab-85f0f986": ResourceUpdate(
        "IBMS3 Yiru Dry Lab Answer Summary.pdf",
        "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_dry_lab_answer_summary.pdf",
    ),
    "ibms3-yiru-ibms-wet-lab-c2d0e5b2": ResourceUpdate(
        "IBMS3 Yiru Wet Lab Answer Summary.pdf",
        "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_wet_lab_answer_summary.pdf",
    ),
    "ibms3-yiru-resource-c3cddfc6": ResourceUpdate(
        "IBMS3 Yiru Experimental Methods Quick Reference.pdf",
        "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_methods_quick_reference.pdf",
    ),
    "ibms3-yiru-1-8c2915c2": ResourceUpdate(
        "IBMS3 Yiru Pre-Exam Review.pdf",
        "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_pre_exam_review.pdf",
    ),
    "ifbs2-yue-ifbs-theme3-48a20e78": ResourceUpdate(
        "IFBS2 Yue Theme 3 Digestion and Absorption.pdf",
        "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestion_and_absorption.pdf",
    ),
    "ifbs2-yue-ifbs-theme3-1-3bc9175b": ResourceUpdate(
        "IFBS2 Yue Theme 3 Digestive Organs 1.pdf",
        "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_organs_1.pdf",
    ),
    "ifbs2-yue-ifbs-theme3-2-6639bdd9": ResourceUpdate(
        "IFBS2 Yue Theme 3 Digestive System 2.pdf",
        "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_system_2.pdf",
    ),
    "ifbs2-yue-ifbs-theme4-0d594c28": ResourceUpdate(
        "IFBS2 Yue Theme 4 Incomplete.pdf",
        "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme4_incomplete.pdf",
    ),
    "ifbs2-yue-ifbstheme34-tutorialquestion-46239494": ResourceUpdate(
        "IFBS2 Yue Theme 3-4 Tutorial Questions.pdf",
        "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_4_tutorial_questions.pdf",
    ),
    "iid-4-yiru-notebookllm-topic-1-60d3232b": ResourceUpdate(
        "IID4 Yiru NotebookLM Topic 1.pdf",
        "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_1.pdf",
    ),
    "iid-4-yiru-notebookllm-topic-4-7a0936a8": ResourceUpdate(
        "IID4 Yiru NotebookLM Topic 4.pdf",
        "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_4.pdf",
    ),
    "iid-4-yiru-notebookllm-topic-5-eva-f9009126": ResourceUpdate(
        "IID4 Yiru NotebookLM Topic 5 EVA.pdf",
        "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_5_EVA.pdf",
    ),
    "iid-4-yiru-notebookllm-topic-3-b8bb3fde": ResourceUpdate(
        "IID4 Yiru NotebookLM Topic 3.pdf",
        "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_3.pdf",
    ),
    "mi2-yue-mi-4b09c058": ResourceUpdate(
        "MI2 Yue Incomplete Notes.pdf",
        "COURSES/Year2/MI2/Yue/MI2_Yue_incomplete_notes.pdf",
    ),
    "pon3-yue-pon-angelica-53f4930a": ResourceUpdate(
        "PoN3 Yue Angelica Notes.pdf",
        "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_Angelica_notes.pdf",
    ),
    "pon3-yue-pon-gedi-dd612b53": ResourceUpdate(
        "PoN3 Yue Gedi Notes.pdf",
        "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_Gedi_notes.pdf",
    ),
    "pon3-yue-pon-0a6b582c": ResourceUpdate(
        "PoN3 Yue Notes.pdf",
        "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_notes.pdf",
    ),
    "pon3-yue-theme-ndd-375a6d7b": ResourceUpdate(
        "PoN3 Yue Neurodegenerative Disease Theme.pdf",
        "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_neurodegenerative_disease_theme.pdf",
    ),
}


FOLDER_MOVES: list[Move] = [
    Move("COURSES/Year2/ADS2/Yiru/ads2-exam-skill-bundle", "COURSES/Year2/ADS2/Yiru/ADS2_Yiru_exam_skill_bundle", "folder"),
    Move("COURSES/Year2/BG2/Yiru/BG2_sum_Yiru", "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary", "folder"),
    Move("COURSES/Resources/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection", "folder"),
    Move("COURSES/Year2/GP2/Yiru/GP2_sum_Yiru", "COURSES/Year2/GP2/Yiru/GP2_Yiru_summary", "folder"),
    Move("COURSES/Year2/IFBS2/Yue/IFBS（theme34)", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4", "folder"),
    Move("COURSES/Year3/IBMS3/Yiru/IBMS3_full_Yiru", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes", "folder"),
    Move("COURSES/Year3/MBE3/Yiru/MBE3_sum_Yiru", "COURSES/Year3/MBE3/Yiru/MBE3_Yiru_summary", "folder"),
    Move("COURSES/Year3/PoN3/Yiru/PoN3_full_Yiru", "COURSES/Year3/PoN3/Yiru/PoN3_Yiru_full_notes", "folder"),
    Move("COURSES/Year3/PoN3/Yue/pon", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes", "folder"),
    Move("COURSES/Year4/IID_4/Yiru/IID_4_full_Yiru", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes", "folder"),
]


FILE_MOVES: list[Move] = [
    Move("COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/Collection of disease.pdf", "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_disease_collection.pdf", "file"),
    Move("COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/Collection of technology.pdf", "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_technology_collection.pdf", "file"),
    Move("COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/calculation.pdf", "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_calculations.pdf", "file"),
    Move("COURSES/Year2/BaO2/Yue/BaO（非完整）.pdf", "COURSES/Year2/BaO2/Yue/BaO2_Yue_incomplete_notes.pdf", "file"),
    Move("COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/JAVA_Sum_yiru.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_summary.pdf", "file"),
    Move("COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/R数据科学 ( etc.) (Z-Library).pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_R_data_science_Z-Library.pdf", "file"),
    Move("COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/SQL-cheat-sheet.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_SQL_cheat_sheet.pdf", "file"),
    Move("COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/base-r-cheat-sheet.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Base_R_cheat_sheet.pdf", "file"),
    Move("COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/data-visualization.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Data_visualization.pdf", "file"),
    Move("COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/java-cheat-sheet-comprehensive-guide.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_cheat_sheet_comprehensive_guide.pdf", "file"),
    Move("COURSES/Year2/GP2/Yiru/GP2_Yiru_summary/GP提纲.pdf", "COURSES/Year2/GP2/Yiru/GP2_Yiru_summary/GP2_Yiru_outline.pdf", "file"),
    Move("COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS theme3_消化吸收过程.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestion_and_absorption.pdf", "file"),
    Move("COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS theme3_消化器官1.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_organs_1.pdf", "file"),
    Move("COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS theme3_消化系统2.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_system_2.pdf", "file"),
    Move("COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS theme4（非完整）.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme4_incomplete.pdf", "file"),
    Move("COURSES/Year2/IFBS2/Yue/IFBStheme34_tutorialquestion.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_4_tutorial_questions.pdf", "file"),
    Move("COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/Experimental Design & Ethics.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_design_and_ethics.pdf", "file"),
    Move("COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS Dry Lab 答题总结.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_dry_lab_answer_summary.pdf", "file"),
    Move("COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS Wet Lab 答题总结.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_wet_lab_answer_summary.pdf", "file"),
    Move("COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/一实验方法速查.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_methods_quick_reference.pdf", "file"),
    Move("COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/考前整理(1).pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_pre_exam_review.pdf", "file"),
    Move("COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/NotebookLLM_Topic_1.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_1.pdf", "file"),
    Move("COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/NotebookLLM_Topic_4.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_4.pdf", "file"),
    Move("COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/NotebookLLM_Topic_5_EVA.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_5_EVA.pdf", "file"),
    Move("COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/NotebookLLm_Topic_3.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_3.pdf", "file"),
    Move("COURSES/Year2/MI2/Yue/MI（非完整）.pdf", "COURSES/Year2/MI2/Yue/MI2_Yue_incomplete_notes.pdf", "file"),
    Move("COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/pon angelica.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_Angelica_notes.pdf", "file"),
    Move("COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/pon gedi.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_Gedi_notes.pdf", "file"),
    Move("COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/pon笔记.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_notes.pdf", "file"),
    Move("COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/theme NDD.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_neurodegenerative_disease_theme.pdf", "file"),
]


DUPLICATE_LOOSE_FILES: list[tuple[str, str]] = [
    ("COURSES/Year2/BG2/Yiru/Collection of disease.pdf", "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_disease_collection.pdf"),
    ("COURSES/Year2/BG2/Yiru/Collection of technology.pdf", "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_technology_collection.pdf"),
    ("COURSES/Year2/BG2/Yiru/calculation.pdf", "COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_calculations.pdf"),
    ("COURSES/Resources/Code_Cheatsheet/Yiru/JAVA_Sum_yiru.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_summary.pdf"),
    ("COURSES/Resources/Code_Cheatsheet/Yiru/R数据科学 ( etc.) (Z-Library).pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_R_data_science_Z-Library.pdf"),
    ("COURSES/Resources/Code_Cheatsheet/Yiru/SQL-cheat-sheet.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_SQL_cheat_sheet.pdf"),
    ("COURSES/Resources/Code_Cheatsheet/Yiru/base-r-cheat-sheet.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Base_R_cheat_sheet.pdf"),
    ("COURSES/Resources/Code_Cheatsheet/Yiru/data-visualization.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Data_visualization.pdf"),
    ("COURSES/Resources/Code_Cheatsheet/Yiru/java-cheat-sheet-comprehensive-guide.pdf", "COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_cheat_sheet_comprehensive_guide.pdf"),
    ("COURSES/Year2/GP2/Yiru/GP提纲.pdf", "COURSES/Year2/GP2/Yiru/GP2_Yiru_summary/GP2_Yiru_outline.pdf"),
    ("COURSES/Year2/IFBS2/Yue/IFBS theme3_消化吸收过程.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestion_and_absorption.pdf"),
    ("COURSES/Year2/IFBS2/Yue/IFBS theme3_消化器官1.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_organs_1.pdf"),
    ("COURSES/Year2/IFBS2/Yue/IFBS theme3_消化系统2.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_system_2.pdf"),
    ("COURSES/Year2/IFBS2/Yue/IFBS theme4（非完整）.pdf", "COURSES/Year2/IFBS2/Yue/IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme4_incomplete.pdf"),
    ("COURSES/Year3/IBMS3/Yiru/Experimental Design & Ethics.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_design_and_ethics.pdf"),
    ("COURSES/Year3/IBMS3/Yiru/IBMS Dry Lab 答题总结.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_dry_lab_answer_summary.pdf"),
    ("COURSES/Year3/IBMS3/Yiru/IBMS Wet Lab 答题总结.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_wet_lab_answer_summary.pdf"),
    ("COURSES/Year3/IBMS3/Yiru/一实验方法速查.pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_methods_quick_reference.pdf"),
    ("COURSES/Year3/IBMS3/Yiru/考前整理(1).pdf", "COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_pre_exam_review.pdf"),
    ("COURSES/Year4/IID_4/Yiru/NotebookLLM_Topic_1.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_1.pdf"),
    ("COURSES/Year4/IID_4/Yiru/NotebookLLM_Topic_4.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_4.pdf"),
    ("COURSES/Year4/IID_4/Yiru/NotebookLLM_Topic_5_EVA.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_5_EVA.pdf"),
    ("COURSES/Year4/IID_4/Yiru/NotebookLLm_Topic_3.pdf", "COURSES/Year4/IID_4/Yiru/IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_3.pdf"),
    ("COURSES/Year3/PoN3/Yue/pon angelica.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_Angelica_notes.pdf"),
    ("COURSES/Year3/PoN3/Yue/pon gedi.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_Gedi_notes.pdf"),
    ("COURSES/Year3/PoN3/Yue/pon笔记.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_notes.pdf"),
    ("COURSES/Year3/PoN3/Yue/theme NDD.pdf", "COURSES/Year3/PoN3/Yue/PoN3_Yue_notes/PoN3_Yue_neurodegenerative_disease_theme.pdf"),
]


CONTENT_REPLACEMENTS: dict[str, str] = {
    "ADS2_exam_skill_bundle/": "ADS2_Yiru_exam_skill_bundle/",
    "BG2_sum/Collection of disease.pdf": "BG2_Yiru_summary/BG2_Yiru_disease_collection.pdf",
    "BG2_sum/Collection of technology.pdf": "BG2_Yiru_summary/BG2_Yiru_technology_collection.pdf",
    "BG2_sum/calculation.pdf": "BG2_Yiru_summary/BG2_Yiru_calculations.pdf",
    "BG2_sum/index.md": "BG2_Yiru_summary/index.md",
    "Code_Cheatsheet/JAVA_Sum_yiru.pdf": "Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_summary.pdf",
    "Code_Cheatsheet/R数据科学 ( etc.) (Z-Library).pdf": "Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_R_data_science_Z-Library.pdf",
    "Code_Cheatsheet/SQL-cheat-sheet.pdf": "Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_SQL_cheat_sheet.pdf",
    "Code_Cheatsheet/base-r-cheat-sheet.pdf": "Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Base_R_cheat_sheet.pdf",
    "Code_Cheatsheet/data-visualization.pdf": "Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Data_visualization.pdf",
    "Code_Cheatsheet/java-cheat-sheet-comprehensive-guide.pdf": "Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Java_cheat_sheet_comprehensive_guide.pdf",
    "GP2_sum/GP提纲.pdf": "GP2_Yiru_summary/GP2_Yiru_outline.pdf",
    "GP2_sum/index.md": "GP2_Yiru_summary/index.md",
    "IFBS/IFBS theme3_消化吸收过程.pdf": "IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestion_and_absorption.pdf",
    "IFBS/IFBS theme3_消化器官1.pdf": "IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_organs_1.pdf",
    "IFBS/IFBS theme3_消化系统2.pdf": "IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme3_digestive_system_2.pdf",
    "IFBS/IFBS theme4（非完整）.pdf": "IFBS2_Yue_theme3_theme4/IFBS2_Yue_theme4_incomplete.pdf",
    "IBMS3_full/Experimental Design & Ethics.pdf": "IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_design_and_ethics.pdf",
    "IBMS3_full/IBMS Dry Lab 答题总结.pdf": "IBMS3_Yiru_full_notes/IBMS3_Yiru_dry_lab_answer_summary.pdf",
    "IBMS3_full/IBMS Wet Lab 答题总结.pdf": "IBMS3_Yiru_full_notes/IBMS3_Yiru_wet_lab_answer_summary.pdf",
    "IBMS3_full/一实验方法速查.pdf": "IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_methods_quick_reference.pdf",
    "IBMS3_full/考前整理(1).pdf": "IBMS3_Yiru_full_notes/IBMS3_Yiru_pre_exam_review.pdf",
    "IBMS3_full/": "IBMS3_Yiru_full_notes/",
    "IID_4_full/NotebookLLM_Topic_1.pdf": "IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_1.pdf",
    "IID_4_full/NotebookLLM_Topic_4.pdf": "IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_4.pdf",
    "IID_4_full/NotebookLLM_Topic_5_EVA.pdf": "IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_5_EVA.pdf",
    "IID_4_full/NotebookLLm_Topic_3.pdf": "IID4_Yiru_full_notes/IID4_Yiru_NotebookLM_topic_3.pdf",
    "IID_4_full/": "IID4_Yiru_full_notes/",
    "MBE3_sum/": "MBE3_Yiru_summary/",
    "PoN3_full/": "PoN3_Yiru_full_notes/",
    "pon/pon angelica.pdf": "PoN3_Yue_notes/PoN3_Yue_Angelica_notes.pdf",
    "pon/pon gedi.pdf": "PoN3_Yue_notes/PoN3_Yue_Gedi_notes.pdf",
    "pon/pon笔记.pdf": "PoN3_Yue_notes/PoN3_Yue_notes.pdf",
    "pon/theme NDD.pdf": "PoN3_Yue_notes/PoN3_Yue_neurodegenerative_disease_theme.pdf",
}


DETAIL_PAGE_RENAMES: dict[str, str] = {
    "ZJE_Collection/zip_contents/ADS2_exam_skill_bundle.md": "ZJE_Collection/zip_contents/ADS2_Yiru_exam_skill_bundle.md",
    "ZJE_Collection/zip_contents/BG2_sum_Yiru.md": "ZJE_Collection/zip_contents/BG2_Yiru_summary.md",
    "ZJE_Collection/zip_contents/Code_Cheatsheet_Yiru.md": "ZJE_Collection/zip_contents/Code_Cheatsheet_Yiru_collection.md",
    "ZJE_Collection/zip_contents/GP2_sum_Yiru.md": "ZJE_Collection/zip_contents/GP2_Yiru_summary.md",
    "ZJE_Collection/zip_contents/IBMS3_full_Yiru.md": "ZJE_Collection/zip_contents/IBMS3_Yiru_full_notes.md",
    "ZJE_Collection/zip_contents/IFBS（theme34).md": "ZJE_Collection/zip_contents/IFBS2_Yue_theme3_theme4.md",
    "ZJE_Collection/zip_contents/IID_4_full_Yiru.md": "ZJE_Collection/zip_contents/IID4_Yiru_full_notes.md",
    "ZJE_Collection/zip_contents/MBE3_sum_Yiru.md": "ZJE_Collection/zip_contents/MBE3_Yiru_summary.md",
    "ZJE_Collection/zip_contents/PoN3_full_Yiru.md": "ZJE_Collection/zip_contents/PoN3_Yiru_full_notes.md",
    "ZJE_Collection/zip_contents/pon.md": "ZJE_Collection/zip_contents/PoN3_Yue_notes.md",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inside(root: Path, rel: str) -> Path:
    path = root / rel
    resolved_root = root.resolve(strict=False)
    resolved_path = path.resolve(strict=False)
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError as exc:
        raise ValueError(f"Refusing to touch path outside {root}: {path}") from exc
    return path


def github_repo_path(local_onedrive_path: str) -> str:
    return f"resources/{local_onedrive_path}"


def github_public_url(resource_type: str, local_onedrive_path: str) -> str:
    repo_path = github_repo_path(local_onedrive_path)
    if resource_type in {"course_package", "folder_bundle"}:
        return f"{RESOURCE_REPO_URL}/tree/main/{repo_path}"
    return f"{RAW_BASE_URL}/{repo_path}"


def folder_size(path: Path) -> int:
    if path.is_file():
        return path.stat().st_size
    if path.is_dir():
        return sum(item.stat().st_size for item in path.rglob("*") if item.is_file())
    return 0


def move_one(root: Path, move: Move, execute: bool, report: list[str]) -> None:
    old = inside(root, move.old)
    new = inside(root, move.new)
    if old == new:
        return
    if not execute:
        report.append(f"- Move {move.kind}: `{move.old}` -> `{move.new}`")
        return
    if old.exists() and new.exists():
        raise FileExistsError(f"Both source and target exist for {move.kind} move: {old} -> {new}")
    if not old.exists():
        if new.exists():
            report.append(f"- Already moved `{move.old}` -> `{move.new}`")
            return
        raise FileNotFoundError(f"Missing source for {move.kind} move: {old}")

    report.append(f"- Move {move.kind}: `{move.old}` -> `{move.new}`")
    new.parent.mkdir(parents=True, exist_ok=True)
    old.rename(new)


def remove_duplicate(root: Path, loose_rel: str, canonical_rel: str, execute: bool, report: list[str]) -> None:
    loose = inside(root, loose_rel)
    canonical = inside(root, canonical_rel)
    if not execute:
        report.append(f"- Remove verified duplicate loose file: `{loose_rel}`")
        return
    if not loose.exists():
        report.append(f"- Duplicate already absent: `{loose_rel}`")
        return
    if not canonical.exists():
        raise FileNotFoundError(f"Canonical duplicate target missing: {canonical}")
    if not loose.is_file() or not canonical.is_file():
        raise ValueError(f"Duplicate cleanup expects files: {loose} and {canonical}")
    if loose.stat().st_size != canonical.stat().st_size or sha256(loose) != sha256(canonical):
        raise ValueError(f"Refusing to remove non-identical duplicate: {loose_rel}")

    report.append(f"- Remove verified duplicate loose file: `{loose_rel}`")
    loose.unlink()


def cleanup_empty_dirs(root: Path, rels: Iterable[str], execute: bool, report: list[str]) -> None:
    if not execute:
        report.append("- Remove empty folders left by the duplicate cleanup.")
        return
    candidates: set[Path] = set()
    for rel in rels:
        path = inside(root, rel)
        candidates.update(path.parents)
    stop = root.resolve(strict=False)
    for path in sorted(candidates, key=lambda item: len(item.parts), reverse=True):
        if path.resolve(strict=False) == stop:
            continue
        try:
            path.relative_to(root)
        except ValueError:
            continue
        if not path.exists() or any(path.iterdir()):
            continue
        report.append(f"- Remove empty folder: `{path.relative_to(root).as_posix()}`")
        if execute:
            path.rmdir()


def normalize_onedrive(execute: bool, report: list[str]) -> None:
    report.extend(["## OneDrive Operations", ""])
    for move in FOLDER_MOVES:
        move_one(ONEDRIVE_ROOT, move, execute, report)
    for move in FILE_MOVES:
        move_one(ONEDRIVE_ROOT, move, execute, report)
    for loose_rel, canonical_rel in DUPLICATE_LOOSE_FILES:
        remove_duplicate(ONEDRIVE_ROOT, loose_rel, canonical_rel, execute, report)
    cleanup_empty_dirs(
        ONEDRIVE_ROOT,
        [loose for loose, _ in DUPLICATE_LOOSE_FILES] + [move.old for move in FOLDER_MOVES + FILE_MOVES],
        execute,
        report,
    )


def normalize_manifest(execute: bool, report: list[str]) -> None:
    report.extend(["", "## Manifest Updates", ""])
    resources = read_manifest()
    seen: set[str] = set()
    for resource in resources:
        rid = str(resource["id"])
        update = RESOURCE_UPDATES.get(rid)
        if update is None:
            continue
        seen.add(rid)
        old_path = str(resource.get("local_onedrive_path", ""))
        old_title = str(resource.get("title", ""))
        resource["title"] = update.title
        resource["local_onedrive_path"] = update.local_onedrive_path
        if update.detail_page:
            resource["website_sources"] = [
                DETAIL_PAGE_RENAMES.get(str(source), str(source))
                for source in resource.get("website_sources", [])
            ]
            resource["description"] = f"Folder bundle documented in {update.detail_page}."
        if str(resource.get("public_url_status")) == "released" and str(resource.get("storage_provider")) == "github":
            resource["resource_repo"] = RESOURCE_REPO_URL
            resource["resource_repo_path"] = github_repo_path(update.local_onedrive_path)
            resource["public_url"] = github_public_url(str(resource["resource_type"]), update.local_onedrive_path)
        notes = str(resource.get("notes", ""))
        if old_path:
            resource["notes"] = notes.replace(old_path, update.local_onedrive_path)
        payload = ONEDRIVE_ROOT / update.local_onedrive_path
        if payload.exists():
            resource["size_bytes"] = folder_size(payload)
        report.append(f"- `{rid}`: `{old_title}` -> `{update.title}`; `{old_path}` -> `{update.local_onedrive_path}`")

    missing = set(RESOURCE_UPDATES) - seen
    if missing:
        raise KeyError(f"Resource updates refer to unknown manifest ids: {', '.join(sorted(missing))}")
    if execute:
        write_manifest(resources, MANIFEST_PATH)


def rename_detail_pages(execute: bool, report: list[str]) -> None:
    report.extend(["", "## Folder Detail Pages", ""])
    for old_rel, new_rel in DETAIL_PAGE_RENAMES.items():
        old = ROOT / old_rel
        new = ROOT / new_rel
        if old.exists() and new.exists():
            raise FileExistsError(f"Both detail pages exist: {old_rel} and {new_rel}")
        if not old.exists():
            if new.exists():
                report.append(f"- Detail page already moved: `{old_rel}` -> `{new_rel}`")
                continue
            raise FileNotFoundError(f"Missing detail page: {old_rel}")
        report.append(f"- Rename detail page: `{old_rel}` -> `{new_rel}`")
        if execute:
            new.parent.mkdir(parents=True, exist_ok=True)
            old.rename(new)


def normalize_detail_page_contents(execute: bool, report: list[str]) -> None:
    report.extend(["", "## Detail Page Member Names", ""])
    changed = 0
    for path in sorted((ROOT / "ZJE_Collection" / "zip_contents").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        new_text = text
        for old, new in CONTENT_REPLACEMENTS.items():
            new_text = new_text.replace(old, new)
        lines = [
            line
            for line in new_text.splitlines()
            if not (line.startswith("- ") and "/.DS_Store" in line)
        ]
        new_text = "\n".join(lines) + "\n"
        if new_text == text:
            continue
        changed += 1
        report.append(f"- Update member list: `{path.relative_to(ROOT).as_posix()}`")
        if execute:
            path.write_text(new_text, encoding="utf-8")
    if changed == 0:
        report.append("- No member-list changes needed.")


def write_report(execute: bool, report: list[str]) -> None:
    mode = "EXECUTE" if execute else "PLAN"
    header = [
        "# Resource Layout Normalization",
        "",
        f"Mode: `{mode}`",
        "",
        "Naming rule: keep `COURSES/<Year>/<Course>/<Contributor>/`, give each bundle a course/contributor folder name, and keep duplicate member files only inside their bundle.",
        "",
    ]
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(header + report) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Rename OneDrive files and update manifest/detail pages.")
    args = parser.parse_args()

    report: list[str] = []
    normalize_onedrive(args.execute, report)
    normalize_manifest(args.execute, report)
    rename_detail_pages(args.execute, report)
    normalize_detail_page_contents(args.execute, report)
    write_report(args.execute, report)

    action = "Applied" if args.execute else "Planned"
    print(f"{action} resource layout normalization. Report: {REPORT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
