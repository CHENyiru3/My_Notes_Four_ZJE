# Edit Rules

## Freely editable

Agents may edit these without confirmation when the meaning and policy stay the same:
- Low-risk navigation copy on course pages.
- Resource-center explanatory copy and layout.
- Resource-center CSS.
- README and contribution-guide wording that clarifies existing policy.
- Generated public resource pages, but only through the generator unless doing a temporary inspection.

## Restricted

Ask before changing:
- Resource status, visibility, public URLs, checksums, sizes, dates, or storage provider fields.
- OneDrive browser-folder links.
- GitHub resource repository paths.
- Contributor names and attribution.
- Course names, year grouping, or academic-year labels.
- License, non-commercial, school-policy, or exam-material language.
- Any large navigation restructure in `mkdocs.yml`.

## Exact wording only

Only change from direct user wording:
- README personal voice, identity/contact statements, and closing remarks.
- School policy statements.
- Contributor-provided technical notes when the request is not specifically to edit them.
- License restriction language.

## Refactoring policy

- Keep resource release logic manifest-driven.
- Keep generated resource tables route-based with separate GitHub and OneDrive columns.
- Avoid duplicating resource tables on course pages.
- Do not add binary payloads under `ZJE_Collection/`; use the manifest and external storage workflow.
- Do not expose maintainer-only fields in public pages.
