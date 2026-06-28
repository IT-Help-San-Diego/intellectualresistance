# AGENTS.md

Canonical, durable source of truth for all AI agents and human contributors on
the **intellectualresistance.com** repository. Read this fully before any edit.

/ The umbrella over the research body of work — the Verification Principle,
/ Carrier Color, candidate societal control levers, the Owl Semaphore, and
/ Star-Centric Transport — plus the shipped projects (DNS Tool, Organic Computer).
/ Same scientific design family as it-help.tech / dnstool.it-help.tech /
/ organiccomputer.me.

## Cross-agent worklog (read this, then append after every change)

  Two agents touch this repo: **Hermes desktop** (local, on the owner's Mac) and the
  **Replit Agent** (a private dev/backend workspace). To avoid a conflicting source of
  truth, both record their work in `AGENT_WORKLOG.md` (repo root). Before you start,
  READ it to see what the other did; after any change, APPEND a dated, signed entry.
  It is `*.md`, so the deploy excludes it from the published site — it lives only in
  the repo, never on the live domain.

  ## What this site is

A single-page, dead-serious umbrella that ties the frameworks together. Each
framework gets its own explainer section WITH ITS MATH, and the projects are
framed as the principle shipped. The voice is calm scientific authority.

## Stack (deliberately minimal)

- **Plain static HTML/CSS. No build step. No framework. No JS at all.**
  `script-src 'none'` is enforced by the CSP — do not add scripts. JSON-LD
  (`<script type="application/ld+json">`) is INERT DATA and is permitted; nothing
  executable. If a feature seems to need JS, redesign without it or ask the owner.
- One self-contained `index.html` (inline `<style>`), self-hosted assets in
  `assets/`. No external subresources, fonts, CDNs, trackers, or cookies.

## EPISTEMIC DISCIPLINE — the heart of this site (non-negotiable)

This site exists to model honest reasoning, so its OWN claims must be labeled by
status. Never inflate a status. The status pills are load-bearing:

- **Verification Principle** = PROVEN (one-line Bayes theorem). OK to call proven.
- **Carrier Color** = a MODEL/framework. Predictions not formally tested here.
- **Societal Control Levers** = CANDIDATE variables. Causality NOT demonstrated.
  Always say "candidate," never "the levers" or "identified."
- **Owl Semaphore** = the ALGEBRA (Klein four-group V₄) is PROVEN; whether the
  four states are the right partition is an UNVALIDATED design hypothesis (IRR
  pilot pending). TWO claims, TWO statuses — never conflate.
- **Star-Centric Transport** = a PROPOSAL with a worked formalism; no benchmarks.

### Owl Semaphore framing — a specific trap to never fall into

The owl is a **group of stance-operations, NOT a many-valued logic.** Do NOT
describe it as "four-valued logic," do NOT say it "extends Boolean algebra," and
do NOT call it a derivative or rediscovery of Belnap–Dunn. It shares ONLY the
abstract V₄ group skeleton with four-valued logics — a structural rhyme that any
two-independent-binary-distinction system produces (there are only two groups of
order 4). Belnap may be cited ONLY to mark this boundary, never as kinship. The
canonical source of truth is the owl-semaphore repo's own AGENTS.md.
Also never reproduce the false claim "V₄ is the automorphism group of DM₄"
(it is ℤ₂).

## Acceptance gates (required)

- **Lighthouse:** target 100/100/100/100 on the homepage.
- **Mozilla Observatory:** target A+ (≈130 is the honest max for a zero-JS,
  zero-cookie static site; do NOT add JS/cookies to chase a higher number).
- **CSP:** `default-src 'none'`, `script-src 'none'`, tight per-type allowlists,
  `style-src` pinned to a SHA-256 hash (no `'unsafe-inline'`). Source of truth:
  `infra/cloudfront/security-headers.json` — and the `<meta>` CSP in index.html
  must carry the SAME hash. Recompute the hash on EVERY change to the `<style>`
  block (build step: `scripts/` if added, else by hand) and update BOTH places.
- **No trackers, cookies, third-party requests, or framework bloat.**
- **Accessibility:** WCAG AA contrast, underlined prose links, readable type.

## Sourcing & claims discipline

Every factual/mathematical claim must be backed by a high-authority source or be
explicitly marked as a candidate/hypothesis/proposal. No hyperbole, no invented
statistics, no "first/only" without a systematic review. Mirror the dnstool
Verification Principle.

## Email lockdown (this is NOT an email domain)

DNS is hardened so the domain cannot send/spoof mail: `MX "0 ."`, `TXT
"v=spf1 -all"`, `_dmarc TXT "v=DMARC1; p=reject; ..."`, wildcard no-key DKIM.
These records already exist in Route 53. Do not add mail records without owner
direction.

## Deploy pipeline

Automatic on push to `main` via `.github/workflows/deploy.yml`:
1. (No build.) Guards: no executable `<script>`; no external subresources.
2. Push CloudFront response-headers policy from
   `infra/cloudfront/security-headers.json` (idempotent).
3. S3 sync: immutable assets long-cache; `*.html`/`*.txt`/`*.xml`/security.txt
   short-cache with correct content-types; `--delete`.
4. CloudFront invalidation `/*` and wait.

Hosting: private S3 bucket (OAC-only) behind CloudFront, ACM cert in
**us-east-1**, Route 53 zone `intellectualresistance.com` (account 433198535569).

GitHub secrets required: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`,
`IR_S3_BUCKET`, `IR_CF_DIST_ID`, `IR_CF_HEADERS_POLICY_ID`.

## Canonical files

- Page: `index.html` (inline visual system)
- 404: `404.html`
- Security headers / CSP: `infra/cloudfront/security-headers.json`
- Deploy: `.github/workflows/deploy.yml`
- Crawl/LLM: `robots.txt`, `llms.txt`, `llms-full.txt`, `sitemap.xml`
- Security: `.well-known/security.txt`
- Brand mark: `favicon.svg`; OG card: `assets/og-card.svg`

## House rules

- Keep the repo clean: no dead CSS, no duplicate selectors, no `.DS_Store`.
- Reuse the CSS custom properties in `:root`; don't introduce palette colors ad hoc.
- Brand/architecture: "Intellectual Resistance" is the UMBRELLA; DNS Tool and
  Organic Computer are projects UNDER it. Keep the reciprocal cross-links intact
  (Organic Computer links up here; this site links down to both).
