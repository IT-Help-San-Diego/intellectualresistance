## 2026-07-03T04:38:20Z — Hermes desktop

- Replaced the fragile `private-local-only` branch workflow with a normal ignored local artifact directory.
- Imported the private branch vault into `Research Artifacts/` on `main`.
- Initialized `Research Artifacts/` as its own local-only Git repository with no remotes.
- Added parent repo ignore rules for `/Research Artifacts/` and legacy `/private_research_vault/`.
- Verified the parent GitHub repo tracks zero files from either private artifact path.
- Created safety bundles under `~/Downloads/intellectualresistance-local-only-backups/` before branch deletion.
- Deleted the local `private-local-only` branch after verifying the artifact repo commit and parent ignore rules.


## 2026-07-03T04:51:07Z — Hermes desktop

- Diagnosed the GitHub Actions deploy failure at `Upload immutable assets (long cache)`.
- Root cause: the public repo still tracked a broken `.hermes.md -> AGENTS.md` symlink after `AGENTS.md` had been removed from the public branch; `aws s3 sync` skipped the nonexistent symlink target and exited with code 2.
- Removed the obsolete tracked `.hermes.md` symlink and the obsolete `.githooks/pre-push` private-branch guard.
- Added a defensive deploy exclusion for `.githooks/*`.
- Unset local `core.hooksPath` because the private branch guard is no longer part of the workflow.

