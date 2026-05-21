# Style Preferences

## Voice

- Public student-facing pages should be direct, friendly, and practical.
- Use simple labels over migration jargon.
- Keep maintainer-only workflow details out of public pages.
- Chinese README/contribution prose can remain informal and personal; preserve that voice unless explicitly asked to rewrite it.

## Resource UI

- Prefer clear route labels: `GitHub`, `OneDrive`, `Browse in OneDrive`, `Download from GitHub`, `Open GitHub folder`.
- Avoid ambiguous labels such as `Channel`, `GitHub Direct`, or `OneDrive Browser` on public pages when both routes can be available.
- Do not make the resource center decorative. It should feel like a functional catalog.
- Keep cards compact and tables scannable.

## Navigation

- Homepage quick links should point users to the resource center for downloads.
- Course pages should link to course anchors in the resource center, not duplicate full resource information.
- Keep year/course navigation aligned with `mkdocs.yml`.

## CSS

- Keep resource CSS scoped with `resource-*` classes.
- Avoid global MkDocs overrides unless necessary.
- Use responsive grids for cards and compact table text.
- Preserve readability on mobile; tables may remain horizontally scrollable through MkDocs Material defaults.
