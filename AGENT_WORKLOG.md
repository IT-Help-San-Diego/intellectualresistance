## 2026-07-03T04:38:20Z — Hermes desktop

- Replaced the fragile `private-local-only` branch workflow with a normal ignored local artifact directory.
- Imported the private branch vault into `Research Artifacts/` on `main`.
- Initialized `Research Artifacts/` as its own local-only Git repository with no remotes.
- Added parent repo ignore rules for `/Research Artifacts/` and legacy `/private_research_vault/`.
- Verified the parent GitHub repo tracks zero files from either private artifact path.
- Created safety bundles under `~/Downloads/intellectualresistance-local-only-backups/` before branch deletion.
- Deleted the local `private-local-only` branch after verifying the artifact repo commit and parent ignore rules.

