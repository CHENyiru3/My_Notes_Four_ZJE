#!/usr/bin/env python3
"""Deprecated compatibility wrapper.

Resource package pages are generated from the manifest. This wrapper is kept
so older automation does not recreate ZIP-centric indexes.
"""

from __future__ import annotations

from generate_resource_pages import main


if __name__ == "__main__":
    main()
