# intellectualresistance.com

The umbrella site for the **Intellectual Resistance**: a body of work on logic,
reason, and thinking that shows its work. Zero-JS, hardened static site in
the IT Help San Diego scientific design family.

## Frameworks (each labeled by epistemic status)

| # | Framework | Status |
|---|-----------|--------|
| 1 | The Verification Principle | **Proven** (Bayes theorem) |
| 2 | Carrier Color | Model / framework |
| 3 | Societal Control Levers | **Candidate** variables (no causality demonstrated) |
| 4 | The Tetrasemaphore | Algebra **proven** (V₄, machine-checked in Lean); utility = open study |
| 5 | Star-Centric Transport | Proposal |

Applied / shipped: **DNS Tool** (dnstool.it-help.tech), **Calibration Scope**
(calibrationscope.com) and **Organic Computer** (organiccomputer.me).

## Stack

Plain static HTML/CSS, no framework, **no JavaScript** (`script-src 'none'`).
Private S3 + CloudFront (OAC) + ACM (us-east-1) + Route 53, account 433198535569.
Push to `main` deploys via GitHub Actions.

## Quality gates

Checked by `verify.sh` on every change: a strict CSP with a hashed `style-src`
(no `unsafe-inline`), no executable JavaScript, no inline styles and no
third-party subresources. Targets, not re-measured here: Lighthouse
100/100/100/100, Mozilla Observatory A+, WCAG AA, and an email-locked domain.

**Epistemic discipline:** never inflate a framework's status; the Tetrasemaphore is a
V₄ group of moves, NOT a four-valued logic.

© 2026 IT Help San Diego Inc. All rights reserved.
