#!/usr/bin/env bash
# Assemble dist/ for the Everyday Physics desktop app:
# the collection's everyday-physics project + the app-only interface
# pages, with cross-room links in Muse-authored pages rewritten to
# the live Everyday Cool URLs (guest game files stay byte-for-byte).
set -euo pipefail
APP="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$HOME/workspace/everyday-cool/projects/everyday-physics"
rm -rf "$APP/dist"
mkdir -p "$APP/dist"
cp -r "$SRC"/. "$APP/dist"/
python3 "$APP/tools/rewrite-links.py" "$APP/dist"
cp "$APP/interface/splash.html" "$APP/dist/splash.html"
cp "$APP/interface/about.html" "$APP/dist/about.html"
echo "dist assembled: $(find "$APP/dist" -type f | wc -l) files"
