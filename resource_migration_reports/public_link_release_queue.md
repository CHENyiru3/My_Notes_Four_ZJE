# Public Link Release Queue

This maintainer-facing queue is generated from the resource manifest and local OneDrive payload state.

Paste OneDrive or SharePoint share links into `public_link_release_queue.csv`, then run `python3 scripts/check_public_link_release_queue.py --require-filled` before `python3 scripts/apply_public_link_release_queue.py --execute`. The helpers validate Microsoft share-link hosts, stale or duplicate rows, release dates, and local OneDrive payload presence. Executed runs update the manifest, write `public_link_release_results.*`, and append to the OneDrive `MANIFESTS/public_link_release_log.md`.

Before either release path, run the local release workflow self-test:

```bash
python3 scripts/self_test_resource_release.py
```

Manual queue release after pasting links:

```bash
python3 scripts/check_public_link_release_queue.py --require-filled
python3 scripts/apply_public_link_release_queue.py --execute
python3 scripts/generate_resource_pages.py
python3 scripts/sync_resource_manifest_to_onedrive.py
```

Optional CLI path: use `scripts/create_onedrive_share_links.py --discover-context` with an existing Microsoft Entra app id. The helper reads local OneDrive sync metadata for the SharePoint `webUrl` and server-relative `ZJE_resource` root. It does not create app registrations; it only runs `m365 login --ensure --appId ...` when `--login` is supplied. Dry runs print commands only by default. Executed runs checkpoint local-only `public_link_release_results.*` and the manifest after each processed item, then append released links to the OneDrive `MANIFESTS/public_link_release_log.md`. If an executed run partially fails, rerun with `--all`; released resources are skipped unless `--include-released` is supplied.

Example dry run:

```bash
python3 scripts/discover_onedrive_release_context.py
python3 scripts/create_onedrive_share_links.py --discover-context --all --preflight-only
python3 scripts/create_onedrive_share_links.py \
  --discover-context \
  --ids bg2-yiru-calculation-c4ec76cf
```

Example executed run after maintainer review:

```bash
python3 scripts/create_onedrive_share_links.py --discover-context --all --preflight-only
python3 scripts/create_onedrive_share_links.py \
  --discover-context \
  --ids bg2-yiru-calculation-c4ec76cf \
  --login --app-id '<existing-entra-app-id>' \
  --execute --update-manifest
python3 scripts/finalize_resource_release.py --sync-onedrive-manifest
```

## Summary

| Public URL Status | Count |
|---|---:|
| released | 0 |
| pending | 64 |
| private | 0 |
| unavailable | 0 |
| broken | 0 |

| Release Tier | Count |
|---|---:|
| core | 42 |
| large_archive | 22 |

| Payload State | Count |
|---|---:|
| ready for review | 39 |
| payload unavailable | 25 |
| ready to materialize | 0 |
| source files required | 0 |
| payload missing | 0 |

## Queue

| ID | Course | Contributor | Type | Tier | Payload State | Next Action |
|---|---|---|---|---|---|---|
| `ads2-hal-2022-2023` | ADS2 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `bg2-hal-2022-2023` | BG2 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `bia4-hal-2024-2025` | BIA4 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `bmi3-hal-2023-2024` | BMI3 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `cbsb3-hal-2023-2024` | CBSB3 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `chem1-hal-2021-2022` | CHEM1 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `dst2-hal-2022-2023` | DST2 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `gp2-hal-2022-2023` | GP2 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `ibi1-hal-2021-2022` | IBI1 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `ibms1-hal-2021-2022` | IBMS1 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `ibms3-hal-2023-2024` | IBMS3 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `ibms4-hal-2024-2025` | IBMS4 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `icmb1-hal-2021-2022` | ICMB1 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `ifbs2-hal-2022-2023` | IFBS2 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `iid4-hal-2024-2025` | IID_4 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `math1-hal-calculus-2021-2022` | MATH1 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `math1-hal-statistics-2021-2022` | MATH1 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `mbe3-hal-2023-2024` | MBE3 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `pon3-hal-2023-2024` | PoN3 | Hal | course_package | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `zip-bg-maps-xiaoran-etal` | BG2 | Xiaoran_etal | folder_bundle | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `zip-ifbs-mindmap-xiaoran-etal` | IFBS2 | Xiaoran_etal | folder_bundle | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `zip-in-lxfwyqlxr` | IN3_full | Xiaoran_etal | folder_bundle | large_archive | payload unavailable | hydrate or restore local payload before sharing |
| `zip-mbe-lxrwyalxf` | MBE3 | Xiaoran_etal | folder_bundle | core | payload unavailable | hydrate or restore local payload before sharing |
| `zip-pon-review-lxrwyqlxf` | PoN3 | Xiaoran_etal | folder_bundle | core | payload unavailable | hydrate or restore local payload before sharing |
| `zip-ifbs-theme34-yue` | IFBS2 | Yue | folder_bundle | core | ready for review | paste public URL |
| `zip-pon-yue` | PoN3 | Yue | folder_bundle | core | ready for review | paste public URL |
| `zip-bg2-sum-yiru` | BG2 | Yiru | folder_bundle | core | ready for review | paste public URL |
| `zip-code-cheatsheet-yiru` | Code_Cheatsheet | Yiru | folder_bundle | core | ready for review | paste public URL |
| `zip-gp2-sum-yiru` | GP2 | Yiru | folder_bundle | core | ready for review | paste public URL |
| `zip-ibms3-full-yiru` | IBMS3 | Yiru | folder_bundle | core | ready for review | paste public URL |
| `zip-iid4-full-yiru` | IID_4 | Yiru | folder_bundle | core | ready for review | paste public URL |
| `zip-mbe3-sum-yiru` | MBE3 | Yiru | folder_bundle | core | ready for review | paste public URL |
| `zip-pon3-full-yiru` | PoN3 | Yiru | folder_bundle | core | ready for review | paste public URL |
| `bg2-yiru-collection-of-disease-83195e15` | BG2 | Yiru | individual_file | core | ready for review | paste public URL |
| `bg2-yiru-collection-of-technology-6df3a98f` | BG2 | Yiru | individual_file | core | ready for review | paste public URL |
| `bg2-yiru-calculation-c4ec76cf` | BG2 | Yiru | individual_file | core | ready for review | paste public URL |
| `bao2-yue-bao-b4a4d26a` | BaO2 | Yue | individual_file | core | ready for review | paste public URL |
| `code-cheatsheet-yiru-java-sum-yiru-d19faa4c` | Code_Cheatsheet | Yiru | individual_file | core | ready for review | paste public URL |
| `code-cheatsheet-yiru-r-etc-z-library-b26e5231` | Code_Cheatsheet | Yiru | individual_file | core | ready for review | paste public URL |
| `code-cheatsheet-yiru-sql-cheat-sheet-02d7f2aa` | Code_Cheatsheet | Yiru | individual_file | core | ready for review | paste public URL |
| `code-cheatsheet-yiru-base-r-cheat-sheet-550428b5` | Code_Cheatsheet | Yiru | individual_file | core | ready for review | paste public URL |
| `code-cheatsheet-yiru-data-visualization-4c76c19d` | Code_Cheatsheet | Yiru | individual_file | core | ready for review | paste public URL |
| `code-cheatsheet-yiru-java-cheat-sheet-comprehensive-guide-a8c2150f` | Code_Cheatsheet | Yiru | individual_file | core | ready for review | paste public URL |
| `gp2-yiru-gp-526d301a` | GP2 | Yiru | individual_file | core | ready for review | paste public URL |
| `ibms3-xiaoran-etal-ibms3-lxrjshtp-32737026` | IBMS3 | Xiaoran_etal | individual_file | core | payload unavailable | hydrate or restore local payload before sharing |
| `ibms3-yiru-experimental-design-ethics-ad7c5ce0` | IBMS3 | Yiru | individual_file | core | ready for review | paste public URL |
| `ibms3-yiru-ibms-dry-lab-85f0f986` | IBMS3 | Yiru | individual_file | core | ready for review | paste public URL |
| `ibms3-yiru-ibms-wet-lab-c2d0e5b2` | IBMS3 | Yiru | individual_file | core | ready for review | paste public URL |
| `ibms3-yiru-resource-c3cddfc6` | IBMS3 | Yiru | individual_file | core | ready for review | paste public URL |
| `ibms3-yiru-1-8c2915c2` | IBMS3 | Yiru | individual_file | core | ready for review | paste public URL |
| `ifbs2-yue-ifbs-theme3-48a20e78` | IFBS2 | Yue | individual_file | core | ready for review | paste public URL |
| `ifbs2-yue-ifbs-theme3-1-3bc9175b` | IFBS2 | Yue | individual_file | core | ready for review | paste public URL |
| `ifbs2-yue-ifbs-theme3-2-6639bdd9` | IFBS2 | Yue | individual_file | core | ready for review | paste public URL |
| `ifbs2-yue-ifbs-theme4-0d594c28` | IFBS2 | Yue | individual_file | core | ready for review | paste public URL |
| `ifbs2-yue-ifbstheme34-tutorialquestion-46239494` | IFBS2 | Yue | individual_file | core | ready for review | paste public URL |
| `iid-4-yiru-notebookllm-topic-1-60d3232b` | IID_4 | Yiru | individual_file | core | ready for review | paste public URL |
| `iid-4-yiru-notebookllm-topic-4-7a0936a8` | IID_4 | Yiru | individual_file | core | ready for review | paste public URL |
| `iid-4-yiru-notebookllm-topic-5-eva-f9009126` | IID_4 | Yiru | individual_file | core | ready for review | paste public URL |
| `iid-4-yiru-notebookllm-topic-3-b8bb3fde` | IID_4 | Yiru | individual_file | core | ready for review | paste public URL |
| `mi2-yue-mi-4b09c058` | MI2 | Yue | individual_file | core | ready for review | paste public URL |
| `pon3-yue-pon-angelica-53f4930a` | PoN3 | Yue | individual_file | core | ready for review | paste public URL |
| `pon3-yue-pon-gedi-dd612b53` | PoN3 | Yue | individual_file | core | ready for review | paste public URL |
| `pon3-yue-pon-0a6b582c` | PoN3 | Yue | individual_file | core | ready for review | paste public URL |
| `pon3-yue-theme-ndd-375a6d7b` | PoN3 | Yue | individual_file | core | ready for review | paste public URL |
