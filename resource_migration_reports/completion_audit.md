# Resource Migration Completion Audit

This report maps the current repository, generated site, and local OneDrive sync state to `RESOURCE_MIGRATION_SPEC.md`.

Overall status: incomplete

| Phase | Requirement | Status | Evidence | Remaining work |
|---|---|---|---|---|
| Phase 0 | Manifest exists and every resource has an id. | pass | 67 resources loaded from ZJE_Collection/resources/resource_manifest.yml |  |
| Phase 1 | OneDrive manifest copy exists and matches the repo manifest. | pass | OneDrive copy exists: True |  |
| Phase 2 | No downloadable binaries remain in the Git website source. | pass | working-tree binaries: 0; tracked binaries: 0 |  |
| Phase 3 | All non-retired manifest payloads exist under the OneDrive resource root. | pass | present: 39; missing: 0; unavailable: 25 |  |
| Phase 3 | All non-retired manifest payloads are locally hydrated and non-empty. | fail | unavailable: 25 | ads2-hal-2022-2023; bg2-hal-2022-2023; bia4-hal-2024-2025; bmi3-hal-2023-2024; cbsb3-hal-2023-2024; chem1-hal-2021-2022; dst2-hal-2022-2023; gp2-hal-2022-2023; ibi1-hal-2021-2022; ibms1-hal-2021-2022 |
| Phase 3 | Folder bundles are materialized and no source bundle work remains. | fail | present: 9; unavailable: 5; ready to materialize: 0; source files required: 0; no listed files: 0 |  |
| Phase 3 | No generated ZIP archives remain under the OneDrive resource root. | pass | ZIP files under ZJE_resource: 0 |  |
| Phase 3 | Large archive resources are separated under LARGE_ARCHIVES while core resources remain in the main course skeleton. | pass | tier layout issues: 0 |  |
| Phase 4 | All public release statuses and URLs are internally consistent. | pass | released: 0; pending: 64; retired: 3 |  |
| Phase 4 | All non-retired resources have maintainer-approved public resource links. | fail | released: 0; pending: 64; retired: 3 | Release pending large archives with manual OneDrive links or `scripts/create_onedrive_share_links.py` using an existing Entra app id. |
| Phase 5 | Public download CSV contains exactly the released resources and only approved public resource URLs. | pass | 0 rows in ZJE_Collection/resources/download_links.csv |  |
| Phase 5 | Public docs do not expose internal migration/storage text. | pass | public-doc policy hits: 0 |  |
| Phase 5 | MkDocs excludes the private resource manifest from public output. | pass | resources/resource_manifest.yml is excluded |  |
| Phase 6 | Deployment no longer packages or publishes generated ZIP downloads. | pass | gh-pages workflow does not create or publish generated ZIP downloads |  |
| Phase 6 | Built public site does not expose the manifest, local paths, or legacy source URLs. | pass | site output scan passed |  |
| Phase 7 | Contributor instructions describe the post-migration resource intake flow without exposing internals. | pass | contributor instructions describe the OneDrive maintainer resource flow |  |
