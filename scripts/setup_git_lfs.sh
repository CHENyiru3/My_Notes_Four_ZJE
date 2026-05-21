#!/usr/bin/env bash
set -euo pipefail

cat <<'MSG'
Git LFS ZIP migration is retired for this repository.

Resource binaries are no longer stored in Git or Git LFS. Publish resources as
OneDrive single files or OneDrive folder bundles, then update
ZJE_Collection/resources/resource_manifest.yml.
MSG
