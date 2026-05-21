#!/usr/bin/env python3
"""Deprecated compatibility entrypoint.

The resource migration no longer creates ZIP archives. Resources are released
as OneDrive single files or folder bundles.
"""

from __future__ import annotations


def main() -> int:
    print("ZIP archive generation is retired. Publish resources as OneDrive files or folder bundles instead.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
