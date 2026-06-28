# Agent Worklog — intellectualresistance.com

  Shared, append-only log so each agent knows what the other changed.
  NOT published: the deploy excludes `*.md` from the S3 sync, so this file lives only
  in the repo, never on the live site. Newest entries on top.
  Format: `## YYYY-MM-DD · <agent>` then terse bullets (what & why · commit if any).

  ---

  ## 2026-06-28 · Replit Agent
  - Stood up Replit as a PRIVATE dev/backend workspace only (local dev server on :5000).
    Nothing from the Replit workspace is pushed to origin — the canonical repo is left
    pristine, by owner's instruction. `.replit` / `replit.md` stay local-only.
  - Verified GitHub push access (account `careyjames`, admin/push) and that the
    S3 + CloudFront auto-deploy is healthy: last 5 Actions runs green; all 5 AWS
    secrets present (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, IR_S3_BUCKET,
    IR_CF_DIST_ID, IR_CF_HEADERS_POLICY_ID).
  - Created this worklog + an AGENTS.md pointer to establish the cross-agent channel.

  ## 2026-06-27 · Hermes desktop
  - infra: documented `/assets/*` CORP cross-origin policy — fixes iMessage/Slack/FB
    link previews silently blocked by CORP same-origin on the OG image. (commit 3935d21)
  