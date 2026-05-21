---
name: ZJE-page-maintainer
description: Maintain the Yiru_study_in_zje / ZJE Collection MkDocs website safely and consistently. Use this skill whenever the user asks to update, review, polish, reorganize, or extend the ZJE study-materials site, especially for course pages, resource download routing, OneDrive/GitHub release logic, the resource manifest, generated package indexes, contribution instructions, or public layout clarity.
---

# ZJE Page Maintainer

## What this skill does

This skill maintains the ZJE Collection website in `Yiru_study_in_zje`, a MkDocs Material site for ZJE study notes, course pages, contributor pages, and downloadable resource routes. The main goal is to keep the public site clear for students while preserving the internal resource-release workflow.

Use this skill conservatively. The public site should show simple user-facing logic, while private migration details stay inside the manifest, scripts, and maintainer reports.

## Repo map

Read these references before editing:
- `references/repo-map.md`
- `references/edit-rules.md`
- `references/content-contracts.md`
- `references/style-preferences.md`

Primary repo locations:
- Site config: `mkdocs.yml`
- Public docs root: `ZJE_Collection/`
- Homepage: `ZJE_Collection/index.md`
- Course pages: `ZJE_Collection/<course>/index.md`
- Contributor/course subpages: `ZJE_Collection/<course>/<contributor>/index.md`
- Resource center: `ZJE_Collection/resources/index.md`
- Resource manifest: `ZJE_Collection/resources/resource_manifest.yml`
- Public route CSV: `ZJE_Collection/resources/download_links.csv`
- Package index: `ZJE_Collection/ZIPS_INDEX.md`
- Folder bundle detail pages: `ZJE_Collection/zip_contents/*.md`
- Resource styling: `ZJE_Collection/stylesheets/resource-center.css`
- Resource generator: `scripts/generate_resource_pages.py`
- Resource checks: `scripts/check_resource_manifest.py`, `scripts/check_resource_pages.py`, `scripts/check_public_site_output.py`

## Default workflow

1. Inspect the relevant public page, manifest records, and generator before editing.
2. Decide whether the target is hand-authored content, generated content, or maintainer-only reporting.
3. Prefer manifest-driven generation over one-off edits to generated pages.
4. Keep public resource logic simple: one resource row, explicit GitHub route, explicit OneDrive route.
5. Do not expose private paths, Google Drive source links, local OneDrive paths, or account-specific filesystem paths.
6. Ask before changing resource release status, public URLs, contributor attribution, license/policy language, or exam-material policy.
7. Regenerate public resource pages after manifest or generator changes.
8. Run the resource validators before finishing.

## Edit permissions

### Freely editable

- Low-risk public wording that improves navigation clarity.
- Course-page link text pointing users to the resource center.
- Resource center layout/copy when it preserves the manifest source of truth.
- CSS for the resource center when it stays compatible with MkDocs Material.
- README and contribution wording that clarifies existing policy without changing policy.

### Restricted

Ask before changing:
- Contributor names, authorship, academic year labels, or course ownership.
- Resource `public_url_status`, `public_url`, `visibility`, checksums, sizes, or release dates.
- OneDrive/SharePoint shared-folder URLs.
- GitHub resource repository URLs or repository path conventions.
- Exam-material policy and non-commercial license language.
- Bulk course-note content, especially technical study notes.

### Exact wording only

Only change from direct user wording:
- Personal contact information and identity-style README statements.
- School policy claims.
- Contributor-provided notes and descriptions when the request is not purely formatting.
- License restriction language.

## Formatting contracts

### Resource routing

- Treat `ZJE_Collection/resources/resource_manifest.yml` as the source of truth for resources.
- Treat `scripts/generate_resource_pages.py` as the source of truth for public resource layout.
- Generated public pages include:
  - `ZJE_Collection/resources/index.md`
  - `ZJE_Collection/ZIPS_INDEX.md`
  - `ZJE_Collection/zip_contents/index.md`
  - the `Access:` header on folder bundle detail pages
  - `ZJE_Collection/resources/download_links.csv`
- Public resource tables must show route availability directly:
  - `GitHub` column for safe mirrors.
  - `OneDrive` column for the shared folder or direct OneDrive link.
- Do not collapse those two routes back into an exclusive `Channel` field.
- For active resources without GitHub mirrors, show that GitHub is unavailable and still expose the OneDrive route.
- For released GitHub resources, still show the OneDrive folder route because the payload is also organized there.

### Public/private boundary

- Public docs must not expose `local_onedrive_path`, `original_source_url`, Google Drive URLs, local absolute paths, or `resource_manifest.yml`.
- `mkdocs.yml` must continue excluding `resources/resource_manifest.yml`.
- Maintainer reports may contain operational summaries, but public pages should use student-facing language.

### Course pages

- Course pages are primarily for browsing Markdown notes and contributor folders.
- Downloadable resources should point to `../resources/index.md#course-<anchor>` or the correct relative equivalent.
- Do not duplicate full resource tables on course pages unless the generator is extended intentionally.

## Approval-required changes

Ask before:
- Reclassifying a resource as public, private, released, retired, or broken.
- Replacing any OneDrive or GitHub route.
- Moving resources between core and large-archive tiers.
- Changing contributor attribution.
- Changing non-commercial, school-policy, or exam-material policy text.
- Adding binary resource payloads to `ZJE_Collection/`.
- Major navigation changes in `mkdocs.yml`.

## Verification checklist

Before finishing:
- Run `python3 scripts/generate_resource_pages.py` after resource manifest or generator edits.
- Run `python3 scripts/check_resource_manifest.py`.
- Run `python3 scripts/check_resource_pages.py`.
- Run `env PYTHONPYCACHEPREFIX=/private/tmp/zje_pycache python3 -m py_compile scripts/generate_resource_pages.py scripts/check_resource_pages.py scripts/resource_manifest.py` after Python edits.
- Run `mkdocs build --strict` when MkDocs is installed.
- If a site build exists, run `python3 scripts/check_public_site_output.py --site-dir site`.
- Search public docs for stale route language such as `Download links are being migrated`, `Downloadable files have moved`, `GitHub Direct Downloads`, `OneDrive Browser`, or `Full Resource Catalog`.
- Confirm generated pages and course pages agree about GitHub mirrors plus OneDrive folder access.
