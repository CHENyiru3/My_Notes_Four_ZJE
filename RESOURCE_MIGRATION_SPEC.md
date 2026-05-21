# ZJE Resource Migration Specification

Status: Draft implementation plan  
Owner: CHENyiru and contributors  
Repository: `Yiru_study_in_zje`  
Website source branch: `main`  
Generated website branch: `gh-pages`  
Canonical resource storage root:

```text
/Users/eric_yiru/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/ZJE_resource
```

## 1. Decision

The GitHub repository must not store actual downloadable resources such as ZIP archives, PDFs, DOCX files, PPTX files, XLSX files, videos, or copied image assets.

The GitHub repository should store only:

- MkDocs source Markdown.
- lightweight metadata and manifests.
- scripts for checking, generating, and validating resource pages.
- contributor instructions.
- placeholder links before OneDrive share links are released.

All actual downloadable resources are moved to OneDrive under `ZJE_resource`. The website links to public OneDrive share URLs after the owner releases them.

Local filesystem paths under `/Users/eric_yiru/...` are for maintenance only. They must never be used as public website links.

External resources must be downloaded directly into `ZJE_resource`. Do not stage Google Drive downloads, ZIP downloads, extracted packages, or copied binaries in `/tmp`, the Git repository, `site/`, or any other local scratch folder before moving them to OneDrive.

Update: generated ZIP archives are retired. Resources should be released as OneDrive single files or OneDrive folder bundles. Existing `zip_contents/*.md` pages remain only as lightweight contents documentation for those folder bundles.

## 2. Goals

1. Reduce GitHub repository size and avoid storing binary study resources in Git.
2. Make OneDrive the single storage authority for all downloadable resources.
3. Keep the website useful by providing clean download links, clear metadata, and searchable descriptions.
4. Replace scattered hardcoded download links with a structured manifest.
5. Preserve contributor attribution, course/year metadata, and archive history.
6. Make future contributions easy to ingest without changing many files manually.
7. Keep public site pages stable while resource storage changes behind them.

## 3. Non-Goals

1. Do not remove Markdown notes from the website source.
2. Do not expose private local OneDrive paths to website users.
3. Do not rely on GitHub Releases for large course resources.
4. Do not continue generating `site/downloads/*.zip` during deployment.
5. Do not require contributors to understand the internal OneDrive folder layout.
6. Do not migrate copyrighted or school-restricted materials without explicit approval from the maintainer.

## 4. Resource Categories

### 4.1 Course Packages

Large packaged submissions, usually ZIP folders or Drive folders originally referenced from course pages.

Examples:

- `ADS2/Hal/ADS2_2022_2023`
- `MATH1/Hal/Calculus_2021_2022`
- `MATH1/Hal/Statistics_2021_2022`
- `IBMS3/Hal/IBMS3_2023_2024`

### 4.2 Individual Files

Standalone files previously stored inside `ZJE_Collection`, such as PDFs and DOCX files.

Examples:

- `BG2/Yiru/Collection of disease.pdf`
- `IBMS3/Yiru/Experimental Design & Ethics.pdf`
- `IFBS2/Yue/IFBStheme34_tutorialquestion.pdf`
- `PoN3/Yue/theme NDD.pdf`

### 4.3 Folder Bundle Contents Documentation

Markdown pages that describe what a package contains. These stay in Git because they are lightweight documentation.

Examples:

- `ZJE_Collection/ZIPS_INDEX.md`
- `ZJE_Collection/zip_contents/*.md`

### 4.4 External Images

Images embedded in Markdown notes through URLs such as `i.imgur.com` or third-party anatomy sites.

These are not primary downloadable course packages. They should be handled separately:

- keep external URLs for now if stable enough.
- optionally mirror images into OneDrive later if link rot becomes a problem.
- if mirrored, update Markdown image links to public OneDrive image URLs or local lightweight optimized copies only if legally and technically safe.

### 4.5 Current Inventory Baseline

Use this baseline to seed the first manifest.

Known extraction coverage:

- external URLs found in website source: 107.
- local downloadable binary files found in `ZJE_Collection`: 34.
- direct course package link sources: course `index.md` pages plus mirrored `Hal/*.txt` files.
- source branch containing editable files: `main`.
- generated branch containing deployed output: `gh-pages`.

Initial course package entries:

| Course | Contributor / Label | Source Pages | Legacy Provider |
|---|---|---|---|
| ADS2 | Hal 2022-2023 | `ADS2/index.md`, `ADS2/Hal/ADS2_2022_2023_link.txt` | Google Drive |
| BG2 | Hal 2022-2023 | `BG2/index.md`, `BG2/Hal/BG2_2022_2023_link.txt` | Google Drive |
| BIA4 | Hal 2024-2025 | `BIA4/index.md`, `BIA4/Hal/BIA4_2024_2025_link.txt` | Google Drive |
| BMI3 | Hal 2023-2024 | `BMI3/index.md`, `BMI3/Hal/BMI3_2023_2024_link.txt` | Google Drive |
| CBSB3 | Hal 2023-2024 | `CBSB3/index.md`, `CBSB3/Hal/CBSB3_2023_2024_link.txt` | Google Drive |
| CHEM1 | Hal 2021-2022 | `CHEM1/index.md`, `CHEM1/Hal/CHEM_2021_2022_link.txt` | Google Drive |
| DST2 | Hal 2022-2023 | `DST2/index.md`, `DST2/Hal/DST2_2022_2023_link.txt` | Google Drive |
| GP2 | Hal 2022-2023 | `GP2/index.md`, `GP2/Hal/GP2_2022_2023_link.txt` | Google Drive |
| IBI1 | Hal 2021-2022 | `IBI1/index.md`, `IBI1/Hal/IBI1_2021_2022_link.txt` | Google Drive |
| IBMS1 | Hal 2021-2022 | `IBMS1/index.md`, `IBMS1/Hal/IBMS1_2021_2022_link.txt` | Google Drive |
| IBMS3 | Hal 2023-2024 | `IBMS3/index.md`, `IBMS3/Hal/IBMS3_2023_2024_link.txt` | Google Drive |
| IBMS4 | Hal 2024-2025 | `IBMS4/index.md`, `IBMS4/Hal/IBMS4_2024_2025_link.txt` | Google Drive |
| ICMB1 | Hal 2021-2022 | `ICMB1/index.md`, `ICMB1/Hal/ICMB1_2021_2022_link.txt` | Google Drive |
| IFBS2 | Hal 2022-2023 | `IFBS2/index.md`, `IFBS2/Hal/IFBS2_2022_2023_link.txt` | Google Drive |
| IID_4 | Hal 2024-2025 | `IID_4/index.md`, `IID_4/Hal/IID4_2024_2025_link.txt` | Google Drive |
| MATH1 | Calculus 2021-2022 | `MATH1/index.md`, `MATH1/Hal/MATH_2021_2022_link.txt` | Google Drive |
| MATH1 | Statistics 2021-2022 | `MATH1/index.md`, `MATH1/Hal/MATH_2021_2022_link.txt` | Google Drive |
| MBE3 | Hal 2023-2024 | `MBE3/index.md`, `MBE3/Hal/MBE3_2023_2024_link.txt` | Google Drive |
| PoN3 | Hal 2023-2024 | `PoN3/index.md`, `PoN3/Hal/PoN3_2023_2024_link.txt` | Google Drive |
| Folder bundle documentation | Existing package contents pages | `ZIPS_INDEX.md`, `zip_contents/index.md` | OneDrive folder bundle |

Initial local binary groups:

| Course / Area | Contributor | Current Files | Target Category |
|---|---|---:|---|
| BG2 | Yiru | 3 PDFs | `COURSES` |
| BaO2 | Yue | 1 PDF | `COURSES` |
| Code_Cheatsheet | Yiru | 6 PDFs | `COURSES` |
| GP2 | Yiru | 1 PDF | `COURSES` |
| IBMS3 | Xiaoran_etal, Yiru | 1 DOCX, 5 PDFs | `COURSES` |
| IFBS2 | Yue | 5 PDFs | `COURSES` |
| IID_4 | Yiru | 4 PDFs | `COURSES` |
| MI2 | Yue | 1 PDF | `COURSES` |
| PoN3 | Yue | 4 PDFs | `COURSES` |
| zip_contents/Yue mirrors | Yue | 3 PDFs | remove after OneDrive copy is verified |

## 5. Target OneDrive Layout

Create this structure under `ZJE_resource`:

```text
ZJE_resource/
  MANIFESTS/
    resource_manifest.yml
    resource_manifest.csv
    migration_log.md
    public_link_release_log.md
  COURSES/
    Year1/
      CHEM1/
      IBI1/
      IBMS1/
      ICMB1/
      MATH1/
    Year2/
      ADS2/
      BG2/
      BaO2/
      DST2/
      GP2/
      IFBS2/
      MI2/
    Year3/
      BMI3/
      CBSB3/
      IBMS3/
      IN3_full/
      MBE3/
      PoN3/
    Year4/
      BIA4/
      IBMS4/
      IID_4/
    Resources/
      Code_Cheatsheet/
  ZIP_PACKAGES/
    active/
    legacy_google_drive/
    superseded/
  INCOMING/
    unsorted/
    checked/
    rejected/
  ARCHIVE/
    by_date/
    by_contributor/
    removed_from_website/
  IMAGES/
    active/
    pending_review/
  PRIVATE/
```

### 5.1 Folder Naming Convention

Use one course-first pattern for both package folders and individual files:

```text
COURSES/<year_group>/<course>/<contributor>/<resource_or_file>
```

Examples:

```text
COURSES/Year2/ADS2/Hal/ads2_hal_2022_2023/
COURSES/Year2/BG2/Yiru/BG2_Yiru_summary/BG2_Yiru_disease_collection.pdf
COURSES/Year3/IBMS3/Yiru/IBMS3_Yiru_full_notes/IBMS3_Yiru_experimental_design_and_ethics.pdf
COURSES/Shared/Code_Cheatsheet/Yiru/Code_Cheatsheet_Yiru_collection/Code_Cheatsheet_Yiru_Base_R_cheat_sheet.pdf
```

### 5.2 Folder Bundle Convention

Do not create generated ZIP archives for website release. When a resource is a package, publish it as a OneDrive folder bundle under the same course-first pattern:

```text
COURSES/<year_group>/<course>/<contributor>/<resource_slug>/
```

Keep original filenames inside folder bundles unchanged where possible.

## 6. Repository Layout After Migration

The repository should keep:

```text
README.md
mkdocs.yml
RESOURCE_MIGRATION_SPEC.md
scripts/
  generate_resource_pages.py
  apply_public_link_release_queue.py
  check_resource_manifest.py
  check_links.py
  self_test_resource_release.py
resource_migration_reports/
  resource_status.md
  migration_status.md
  folder_bundle_status.md
  public_link_release_queue.md
  public_link_release_queue.csv
ZJE_Collection/
  index.md
  ZIPS_INDEX.md
  resources/
    resource_manifest.yml
    download_links.csv
  <course>/
    index.md
    <contributor>/
      index.md
      notes.md
```

The repository should remove or avoid:

```text
ZJE_Collection/**/*.zip
ZJE_Collection/**/*.pdf
ZJE_Collection/**/*.docx
ZJE_Collection/**/*.pptx
ZJE_Collection/**/*.xlsx
site/downloads/
downloads/
```

If a PDF is intentionally small and necessary for direct web reading, it still needs explicit maintainer approval before staying in Git.

## 7. Manifest Design

The manifest is the source of truth for public downloads.

Recommended source file:

```text
ZJE_Collection/resources/resource_manifest.yml
```

Recommended exported copy in OneDrive:

```text
ZJE_resource/MANIFESTS/resource_manifest.yml
```

### 7.1 Required Fields

```yaml
- id: ads2-hal-2022-2023
  title: ADS2 Hal Materials
  course: ADS2
  year_group: Year2
  academic_year: 2022-2023
  contributor: Hal
  resource_type: course_package
  storage_provider: onedrive
  local_onedrive_path: COURSES/Year2/ADS2/Hal/ads2_hal_2022_2023
  public_url: ""
  public_url_status: pending
  original_source_url: "https://drive.google.com/file/d/1Fl2WtzDZoyEqi3MLvilNCOUIeTbQTl-Y/view?usp=sharing"
  website_sources:
    - ZJE_Collection/ADS2/index.md
    - ZJE_Collection/ADS2/Hal/ADS2_2022_2023_link.txt
  description: "Hal's ADS2 materials for 2022-2023."
  license_note: "Educational sharing; non-commercial use only."
  visibility: pending_review
  version: 1
  checksum_sha256: ""
  size_bytes: null
  migrated_at: ""
  public_link_released_at: ""
  notes: ""
```

### 7.2 Field Rules

- `id` must be stable and lowercase.
- `public_url` stays empty until OneDrive sharing is released.
- `public_url_status` must be one of `pending`, `released`, `broken`, `private`, `unavailable`, `retired`.
- `local_onedrive_path` is relative to `ZJE_resource`, not an absolute local path.
- `original_source_url` stores legacy Google Drive or GitHub URLs for audit history.
- `website_sources` lists every source page that referred to the resource before migration.
- `checksum_sha256` is recommended for ZIP archives and large files.
- `visibility` must be one of `pending_review`, `public_after_review`, `private_internal`, `retired`.
- `visibility` must not be `public_after_review` until the maintainer has checked the material.

## 8. Migration Workflow

### Phase 0: Freeze and Inventory

1. Work only on the `main` branch.
2. Record current external links from `ZJE_Collection/**/*.md` and `ZJE_Collection/**/*.txt`.
3. Record current local binaries from `ZJE_Collection`.
4. Build an initial manifest with:
   - course package links.
   - local PDF/DOCX files.
   - ZIP contents pages.
   - optional external image links.
5. Commit the manifest before moving files.

Acceptance criteria:

- `resource_manifest.yml` exists.
- every known downloadable resource has an `id`.
- every legacy Google Drive link is preserved in `original_source_url`.
- every local binary has a target `local_onedrive_path`.

### Phase 1: Prepare OneDrive Folders

1. Create the target `ZJE_resource` folder tree.
2. Copy `resource_manifest.yml` into `MANIFESTS`.
3. Add `migration_log.md` with date, branch, and operator.
4. Add `public_link_release_log.md` for later share URL release tracking.

Acceptance criteria:

- folder tree exists.
- incoming resources can be placed without ambiguity.
- manifest exists in both Git and OneDrive.

### Phase 2: Move Local Binary Files Out of Git

1. Move each local binary from `ZJE_Collection` into the matching OneDrive folder.
2. Keep the original filename unless it is unsafe for archive tooling.
3. Update manifest entries with file size and checksum.
4. Replace Markdown links to local binaries with generated resource links or placeholder text.
5. Remove duplicate mirror files from `ZJE_Collection/zip_contents/Yue` after confirming OneDrive copies exist.

Acceptance criteria:

- no unapproved `.pdf`, `.docx`, `.pptx`, `.xlsx`, or `.zip` files remain in `ZJE_Collection`.
- Markdown pages do not link to removed local binaries.
- `scripts/check_links.py` passes for local links.

### Phase 3: Download Legacy Google Drive Resources

For each legacy Google Drive resource:

1. Download the file or folder manually or with an approved downloader, using a destination inside `ZJE_resource` from the start.
2. Store it under the matching OneDrive course package folder.
3. Preserve the original archive if available.
4. If unpacking is useful, keep both:
   - original archive in `ZIP_PACKAGES/legacy_google_drive`.
   - organized extracted folder in `COURSES`.
5. Update `resource_manifest.yml` with checksum, size, and migration notes.

Direct-download rule:

- Google Drive file links must download into `COURSES/<year_group>/<course>/<contributor>/<resource_slug>/` or `ZIP_PACKAGES/legacy_google_drive/<resource_id>/`.
- Google Drive folder links must download into a OneDrive folder target, not into a temporary folder that is moved later.
- For command-line downloaders, set the output directory or current working directory to the intended OneDrive destination.
- If a downloader cannot write directly to OneDrive, do not use it for this migration.
- Any extraction step must also extract directly into a OneDrive destination.

Approved command pattern:

```text
scripts/download_external_resources_to_onedrive.py --execute <resource_id>
```

This helper reads `ZJE_Collection/resources/resource_manifest.yml`, derives the destination from `local_onedrive_path`, and refuses to write outside `ZJE_resource`.

Acceptance criteria:

- every legacy course package has a local OneDrive copy or an explicit `private`/`unavailable` status.
- every original Google Drive URL remains recorded for audit.
- no resource is considered released until a OneDrive public URL is added.
- no downloaded external resource appears in `/tmp`, `site/downloads`, or the Git working tree.

### Phase 4: Create Public OneDrive Links

The maintainer releases OneDrive share links manually or with an explicitly configured Microsoft 365 CLI login.

Do not run an unattended setup wizard that creates a new Microsoft Entra application. If the Microsoft 365 CLI is used, authenticate with an existing app registration supplied explicitly by the maintainer:

```text
m365 login --authType deviceCode --appId <existing-entra-app-id> --tenant <tenant-if-needed>
```

The repo-side helper for this flow is:

```text
scripts/create_onedrive_share_links.py
```

It requires the SharePoint/OneDrive `webUrl` and the server-relative URL that maps to the local `ZJE_resource` root, and it supports dry runs before link creation. Before releasing links, run `scripts/self_test_resource_release.py` to exercise the queue validator and the dry-run file/folder command path without logging in or mutating Microsoft 365 state.

For each resource:

1. Confirm the resource is allowed for public non-commercial sharing.
2. Create a OneDrive share link.
3. Paste the share link into `public_url`.
4. Set `public_url_status: released`.
5. Add `public_link_released_at` using ISO date format.
6. Add an entry to `MANIFESTS/public_link_release_log.md`.

Acceptance criteria:

- released resources have public OneDrive URLs.
- unreleased resources show a clear pending status on the website.
- no private local paths appear in generated pages.
- no new Microsoft Entra app registration is created implicitly by the migration scripts.

### Phase 5: Generate Website Resource Pages

Create or update a script:

```text
scripts/generate_resource_pages.py
```

The script should generate:

```text
ZJE_Collection/ZIPS_INDEX.md
ZJE_Collection/resources/index.md
ZJE_Collection/resources/download_links.csv
resource_migration_reports/resource_status.md
course index resource blocks if needed
```

Generated page behavior:

- Public resource pages list non-retired resources in one catalog with separate `GitHub` and `OneDrive` route columns.
- Released GitHub-safe resources show a GitHub mirror and still keep a OneDrive folder route.
- Resources without a GitHub mirror show that GitHub is unavailable and point users to the relevant shared OneDrive browser folder when public browsing is allowed.
- Pending, private, broken, and unavailable resources must not expose direct private URLs or internal storage paths.
- Maintainer reports in `resource_migration_reports/` track pending links, payload readiness, and release queue state.
- If `retired`, hide from course pages but keep in archive/status pages.

Acceptance criteria:

- pages are generated from the manifest.
- no course page has manually duplicated resource tables or per-resource OneDrive links.
- public tables do not collapse GitHub and OneDrive into one exclusive channel.
- `mkdocs build` succeeds.

### Phase 6: Update Deployment

Update `.github/workflows/gh-pages.yml`:

1. Remove the step that creates per-folder ZIP archives in `site/downloads`.
2. Build only the static MkDocs website.
3. Do not upload generated binary downloads to `gh-pages`.

Acceptance criteria:

- `gh-pages` no longer contains `downloads/*.zip`.
- site deployment does not package resource folders.
- website users download from OneDrive, not GitHub.

### Phase 7: Archive and Retention

Use archive folders intentionally:

```text
ARCHIVE/by_date
ARCHIVE/by_contributor
ARCHIVE/removed_from_website
```

Rules:

- keep the first migrated copy of a legacy resource.
- if a new version replaces an old one, move the old version to `superseded`.
- if a resource is removed from the public website, keep it in `removed_from_website` unless deletion is legally or ethically required.
- record all archive moves in `migration_log.md`.

Acceptance criteria:

- no file is deleted without a logged reason.
- the active download list only points to current resources.
- old public links are marked `retired` or `superseded` in the manifest.

## 9. Website UX Rules

Course pages should show resource sections consistently.

Recommended pattern:

```markdown
## Resources

| Resource | Contributor | Year | Status |
|---|---:|---:|---|
| [Hal Materials](<public OneDrive URL>) | Hal | 2022-2023 | Released |
| Yiru Summary Package | Yiru | 2023-2024 | OneDrive link pending release |
```

Rules:

- Do not expose local paths.
- Do not mention internal OneDrive folder names unless helpful for contributors.
- Prefer one clean download table per course.
- Keep descriptions short and factual.
- Preserve contributor attribution.
- Show pending status instead of broken links.

## 10. Contribution Workflow After Migration

For contributors:

1. Contributor sends files or a cloud link to maintainer.
2. Maintainer downloads or places files directly in `ZJE_resource/INCOMING/unsorted`.
3. Maintainer reviews for:
   - course match.
   - file type.
   - privacy or exam restriction risk.
   - contributor name.
   - academic year.
4. Accepted resources move to `INCOMING/checked`.
5. Resources are organized into `COURSES/<year_group>/<course>/<contributor>/`.
6. Manifest entry is added with `public_url_status: pending`.
7. Maintainer releases OneDrive link.
8. Generated website pages are updated.

Do not accept a workflow where incoming resources are first downloaded into the Git repository, `/tmp`, or another local scratch location and then copied into OneDrive. The first durable destination should be `ZJE_resource`.

Rejected resources:

- move to `INCOMING/rejected` if they should be kept temporarily.
- record reason in `migration_log.md`.
- do not publish on the website.

## 11. Validation Checklist

Before each website release:

1. `git status --short` is reviewed.
2. no large binaries remain in Git unless explicitly approved.
3. no absolute local paths appear in Markdown:

   ```text
   /Users/eric_yiru/
   OneDrive-InternationalCampus
   ZJE_resource
   ```

4. no generated page points to `site/downloads`.
5. external downloads have no residue in `/tmp`, `site/downloads`, or the Git working tree.
6. every `released` manifest entry has a non-empty `public_url`.
7. every `pending` manifest entry is absent from public download tables and present in maintainer reports.
8. every `retired` entry is absent from public download tables.
9. `ZJE_Collection/resources/resource_manifest.yml` is excluded from built public output.
10. built public output does not expose `original_source_url`, `local_onedrive_path`, legacy Google Drive URLs, or maintainer local paths.
11. `scripts/check_resource_pages.py` passes.
12. `scripts/check_links.py` passes.
13. `scripts/check_public_site_output.py --site-dir site` passes after `mkdocs build`.
14. `mkdocs build` succeeds.
15. website spot check covers:
    - home page.
    - Resources > Downloads.
    - at least one released file or folder link when a public URL exists.
    - the empty released-download state when no public URLs exist yet.

## 12. Recommended First Implementation Slice

Start with a small but representative migration.

Suggested first slice:

1. `BG2`
   - local PDFs in `BG2/Yiru`.
   - Hal Google Drive link.
2. `GP2`
   - local `GP提纲.pdf`.
   - Hal Google Drive link.
3. `resources/index.md`
   - show released OneDrive downloads only.

Why this slice:

- includes both local binaries and external package links.
- small enough to verify manually.
- exercises the manifest, page generation, and OneDrive release workflow.

Acceptance criteria for first slice:

- BG2 and GP2 binaries are moved to OneDrive.
- their manifest entries are complete except public links if not yet released.
- course pages no longer link to local PDFs.
- `mkdocs build` passes.
- public OneDrive links can be pasted later without changing page prose manually.

## 13. Open Questions

1. Should old Google Drive links stay visible as fallback links after OneDrive links are released?
   - Recommended answer: no, keep them only in `original_source_url` for audit.
2. Should image URLs be mirrored in OneDrive now?
   - Recommended answer: defer; handle after main downloadable resources are migrated.
3. Should small PDFs be allowed to remain in Git for direct browser viewing?
   - Recommended answer: no by default; require explicit approval.
4. Should `Hal/*.txt` link files remain?
   - Recommended answer: replace them with generated metadata pages or remove after manifest migration.
5. Should the manifest be edited manually or generated from OneDrive?
   - Recommended answer: edit manually first, automate later only after the schema stabilizes.

## 14. Done Definition

The resource migration is complete when:

1. actual downloadable resources are stored under `ZJE_resource`, not in GitHub.
2. GitHub contains only source pages, metadata, scripts, and lightweight docs.
3. all public download links on the website point to released OneDrive URLs.
4. pending resources are clearly marked and do not create broken links.
5. deployment no longer creates or publishes `downloads/*.zip`.
6. the manifest is the only place where public resource URLs are maintained.
7. contributors have clear instructions for sending new resources.
8. the maintainer can update resource links by editing one manifest and regenerating pages.
