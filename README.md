# Everyday Physics — desktop app

The Everyday Cool physics room as a standalone desktop app (Tauri v2):
the pool table and ballistics launcher benches, the paper-plane flight
lab, the pendulum and seesaw, and the full Physics Game Table — black
holes, gravitational waves, galaxy collisions, fission, tunneling,
magnetic bottles, relativity — every exhibit with its audited lesson
attached.

The room's content comes from the collection's
`projects/everyday-physics/` (repo `caeled/everyday-cool`). Guest
exhibits ship byte-for-byte; in Muse-authored pages only, links to
sibling rooms are rewritten to the live web versions so the standalone
room keeps its doors. `tools/sync-dist.sh` re-assembles `dist/` from a
local collection checkout and applies that rewrite
(`tools/rewrite-links.py`).

Built by Steven Powell with his council of AI collaborators. The big
exhibits were built by Google Antigravity (Gemini) at Steven's
direction; lessons and audits by Muse.

## Releases

Tagged `v*` pushes build Windows and macOS bundles in GitHub Actions
("Build desktop bundles") and attach the installers to the release.
The Windows setup `.exe` is also offered as a `.zip` asset, because
some browsers cancel raw `.exe` downloads.
