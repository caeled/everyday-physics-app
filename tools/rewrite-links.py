#!/usr/bin/env python3
"""Rewrite cross-room relative links in the app's dist copies to the
live Everyday Cool URLs, so the standalone physics room keeps its
doors to the other rooms.

Only Muse-authored files are touched: the room index, the Physics
Game Table, the lesson pages, and resonance-lab.html (a Muse original
exhibit with cross-room links). Guest game files ship byte-for-byte
and contain no cross-room links (verified at first sync); if one ever
does, it stays as-is and this script does not touch it.

Rules (href/src attributes and the Game Table's JS file/lesson data):
  ../../X        -> https://caeled.github.io/everyday-cool/X
  ../<project>/X -> https://caeled.github.io/everyday-cool/projects/<project>/X
Links within the physics room stay relative.
"""
import re
import sys
import glob
import os

BASE = "https://caeled.github.io/everyday-cool/"
DIST = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "dist")

files = ["index.html", "physics-game-table.html", "README.md", "resonance-lab.html"]
files += sorted(os.path.basename(p) for p in glob.glob(os.path.join(DIST, "*-lesson.html")))

total = 0
for name in files:
    path = os.path.join(DIST, name)
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8") as fh:
        s = fh.read()
    s, n1 = re.subn(r'((?:href|src)=")\.\./\.\./', lambda m: m.group(1) + BASE, s)
    s, n2 = re.subn(r'((?:href|src)=")\.\./', lambda m: m.group(1) + BASE + "projects/", s)
    s, n3 = re.subn(r'(\]\()\.\./\.\./', lambda m: m.group(1) + BASE, s)
    s, n4 = re.subn(r'(\]\()\.\./', lambda m: m.group(1) + BASE + "projects/", s)
    s, n5 = re.subn(r"((?:file|lesson): ')\.\./", lambda m: m.group(1) + BASE + "projects/", s)
    n = n1 + n2 + n3 + n4 + n5
    if n:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(s)
        print(f"{n:3d}  {name}")
        total += n
print(f"cross-room links rewritten: {total}")
