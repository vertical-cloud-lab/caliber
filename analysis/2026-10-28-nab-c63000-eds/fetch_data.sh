#!/usr/bin/env bash
# Fetch the staged NAB (C63000) SEM/EDS drop into a directory outside the checkout and
# check every file against the sha256 list in the drop's MANIFEST.md.
# Usage: GH_READ_PAT_STAGING=... ./fetch_data.sh [dest=/tmp/nab-staging]
set -euo pipefail
dest="${1:-/tmp/nab-staging}"
ref=3c25afa
base="for/vertical-cloud-lab/caliber/2026-10-28-nab-c63000-sem-eds"
mkdir -p "$dest/files/eds" "$dest/files/sem"
get() { GH_TOKEN=$GH_READ_PAT_STAGING gh api "repos/sgbaird/agent-staging/contents/$base/$(python3 -c 'import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1]))' "$1")?ref=$ref" -H "Accept: application/vnd.github.raw"; }
get MANIFEST.md > "$dest/MANIFEST.md"
sed -n '/^```$/,/^```$/p' "$dest/MANIFEST.md" | grep -E '^[0-9a-f]{64}  ' > "$dest/hashes.txt"
while IFS= read -r line; do get "${line:66}" > "$dest/files/${line:66}"; done < "$dest/hashes.txt"
cd "$dest/files" && sha256sum -c ../hashes.txt
