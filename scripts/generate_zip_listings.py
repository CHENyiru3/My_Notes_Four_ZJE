#!/usr/bin/env python3
"""Compatibility wrapper for manifest-driven resource page generation.

ZIP listing pages are now generated from
`ZJE_Collection/resources/resource_manifest.yml`. Do not stage ZIP files inside
the repository to generate listings.
"""

from __future__ import annotations

from generate_resource_pages import main


if __name__ == "__main__":
    main()
