# intellectualresistance.com

The umbrella site for the **Intellectual Resistance** — a body of work on logic,
reason, and thinking done right. Single-page, zero-JS, hardened static site in
the IT Help San Diego scientific design family.

## Frameworks (each labeled by epistemic status)

| # | Framework | Status |
|---|-----------|--------|
| 1 | The Verification Principle | **Proven** (Bayes theorem) |
| 2 | Carrier Color | Model / framework |
| 3 | Societal Control Levers | **Candidate** variables (no causality demonstrated) |
| 4 | The Owl Semaphore | Algebra **proven** (V₄); utility = open study |
| 5 | Star-Centric Transport | Proposal |

Applied / shipped: **DNS Tool** (dnstool.it-help.tech) and **Organic Computer**
(organiccomputer.me).

## Stack

Plain static HTML/CSS, no framework, **no JavaScript** (`script-src 'none'`).
Private S3 + CloudFront (OAC) + ACM (us-east-1) + Route 53, account 433198535569.
Push to `main` deploys via GitHub Actions.

## Quality gates

Lighthouse 100/100/100/100 · Mozilla Observatory A+ · strict CSP with a hashed
`style-src` (no `unsafe-inline`) · WCAG AA · email-locked domain · no cookies,
no trackers, no third-party requests.

See `AGENTS.md` for the full contributor contract — especially the **epistemic
discipline** section (never inflate a framework's status; the Owl Semaphore is a
V₄ group of stance-operations, NOT a four-valued logic).

© 2026 IT Help San Diego Inc. All rights reserved.
