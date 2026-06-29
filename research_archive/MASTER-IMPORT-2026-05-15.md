---
date: 2026-05-15
type: master-archive
project: intellectual-resistance
tags: [carrier-color, verification-principle, owl-semaphore, facebook-archive, complete-session]
status: recovered-129-post-json-ready
---

# Master Import — Intellectual Resistance

This file is the Obsidian entry point for the May 15, 2026 Intellectual Resistance archive package. It preserves the session materials and points to the recovered 129-post Facebook JSON archive.

## Package contents

- [[01-CONVERSATION-TRANSCRIPT-3]] — Session transcript and framework development notes.
- [[02-DELETE-LIST-2]] — Ten Facebook posts flagged for deletion before public cleanup.
- [[03-README]] — Package overview and quick start.
- [[06-INSTALLATION]] — Updated installation and Facebook export instructions.
- [[DATA-COMPLETENESS-REPORT]] — Current data completeness status.
- `05-facebook-to-obsidian.py` — Python converter for Facebook JSON or fallback CSV input.
- `04-facebook-archive.json` — Recovered 129-post Facebook archive extracted from the attached Markdown conversation export.
- `source-files/` — Raw attached CSV and Markdown source exports.
- `facebook-archive/` — Generated Obsidian output from the recovered JSON.

## Important data status

The 129-post JSON has been recovered into `04-facebook-archive.json`. Some posts retain scrape-quality caveats in `capture_notes`; see [[DATA-COMPLETENESS-REPORT]] for the remaining gaps.

To regenerate the Obsidian notes, rerun:

```bash
python3 05-facebook-to-obsidian.py
```

## Core frameworks

### The Verification Principle

Independent audit before deployment, proportional to harm. Confidence intervals, not certainty theater.

### Carrier Color Theory

Carrier color is the set of identity signals that can block rational processing before evidence is evaluated. The operational solution is to strip tribal cues and transmit the clean factual signal.

### The Owl Semaphore

The Owl Semaphore, σh, is a metacognitive pause signal. When detected, pause belief processing, verify the claim independently, check for carrier color, and resume only after audit.

## Domain decision

`intellectualresistance.com` remains the approved domain framing when positioned operationally:

> We resist the deployment of high-stakes systems without independent audit. Not resisting AI. Not resisting innovation. Resisting the accountability gap that lets critical systems operate on the honor system.

## Next action

Import the generated `facebook-archive/` folder into Obsidian, then optionally run a fresh official Facebook JSON export later to fill the few posts flagged in `capture_notes`.
