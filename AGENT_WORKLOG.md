# Agent Worklog — intellectualresistance.com

  Shared, append-only log so each agent knows what the other changed.
  NOT published: the deploy excludes `*.md` from the S3 sync, so this file lives only
  in the repo, never on the live site. Newest entries on top.
  Format: `## YYYY-MM-DD · <agent>` then terse bullets (what & why · commit if any).

  ---

  ## 2026-06-29 · Replit Agent
    - Integrated three owner-approved, verified scientific improvements into index.html
      (+ the llms.txt / llms-full.txt mirrors). All additive; reused existing component
      classes only, so the CSP style-hash is unchanged and verify.sh passes clean
      (no-JS / no-inline-style / no-external-subresource invariants intact).
      · §1 Verification Principle — added a CANDIDATE lock-detector: raw belief-movement
        M = Σ|P(H|Ei) − P(H)| is the wrong metric (BFi = 1 ⇒ a rational agent also stays
        put); the right quantity is deviation from the Bayes-correct posterior. Placed
        clearly below the proven theorem, labeled candidate.
      · §4 Owl Semaphore — fixed "two independent involutions" → "independent, commuting"
        (the one-word omission that left the V₄ derivation under-specified); added a
        "why commuting is load-bearing" note ((a∘b)² = a²b² = e vs. the dihedral group
        non-commuting involutions generate) and "C₄ excluded: no element of order 4" to
        the equation key. Algebra-only; the design-hypothesis status of the four-state
        partition is untouched.
      · §5 Star-Centric Transport — added the epistemic packet P = ⟨D, C, L⟩ (payload /
        carrier-color metadata / signed lineage log) and a convergence paragraph linking
        it to §1's odds form and §2's carrier color; flagged "center = latent invariant,
        not political centrism." Stays PROPOSAL.
    - Source corroboration: three owner-supplied review files (2026-06-29) independently
      confirmed the commuting fix and the lock-detector/OEP reframe. Their prose framework
      names were treated as untrusted (some hallucinated) — only the verified math landed.
    - Published via the GitHub Git Data API on top of origin/main (no local git push; the
      Replit workspace stays repo-local). This is the commit below.
    - Follow-up (same day, after code review): tightened §4 for precision — the
      "exactly four / V₄" claim now requires a, b to be distinct, non-identity
      involutions, and the non-commuting case names the dihedral group D_n
      (n = ord(ab) ≥ 3, or infinite dihedral) instead of "arbitrarily many."
      Synced to llms-full.txt; verify.sh still green.

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
  