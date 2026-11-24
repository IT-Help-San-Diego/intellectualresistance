# Change log

This file records changes to intellectualresistance.com that are not corrections: nothing a reader was
told was wrong. Corrections are not recorded here. They are made where a reader sees them: as an entry in
the family corrections index, https://www.it-help.tech/corrections/, which the home page links from its
footer, and as three notes dated 28 and 29 July 2026 on the home page, each beside the passage it
concerns.

This file is for whoever maintains the site. It is not served: the deploy leaves every `.md` file out of
the bucket.

This file begins with the entry below. Earlier changes are in this repository's history. Newest first.
Each heading gives the day in UTC, and the day in Los Angeles where the two differ.

## 23 November 2026: the METACOGNITIVE film on the Dose 01 page, and the DOI that resolves to the latest version

The Dose 01 page gains a closed disclosure under the METACOGNITIVE still, "Watch the three moves applied to
it (18 seconds, no sound)". Opening it shows the release's own 1298 px still as the poster of a plain video
element. Nothing is fetched until the reader presses play; the film then plays inline with the browser's own
controls, WebM first and MP4 second, both served from this site (`assets/films/`) and byte for byte the files
of Tetrasemaphore release 1.3.0. No script and no third party are involved; the page's policy already allowed
media from this site. The caption says what the film shows and that the pale blue outline the film draws is
not part of the semaphore. The still stays as it was. The rules for the disclosure were added to the style
block both pages share, so the style hash changed in both pages and in `infra/cloudfront/security-headers.json`.

The home page's reference list, its structured data, `llms.txt` and `llms-full.txt` cited The Tetrasemaphore
as version 1.0.0 with that version's DOI, 10.5281/zenodo.23575816. They now cite 10.5281/zenodo.23575814, the
DOI that always resolves to the latest version, and name no version number. On the Dose 01 page the footer
link and the sentence on the four stances do the same; the sentence that says what the garment's glyphs were
checked against keeps 1.0.0, because that is the version they were checked against.

Why: Tetrasemaphore releases now follow one another (1.1.0, 1.2.0 and 1.3.0 since 1.0.0), and a citation
pinned to one version goes stale with each; the concept DOI does not. No claim changed: the 1.0.0 citation
was true when written. Recorded here and not in the corrections index.

## 17 November 2026: one sentence repunctuated

On the home page, the sentence about a line with no resistor at its end had a spaced hyphen after "more
signal". It now reads: "And a line with no resistor at its end doesn't carry more signal. It rings: the
wave reflects, returns over what is still arriving, and the receiver cannot tell the message from its own
echo." Organic Computer carries the same sentence and changed with it.

Why: the site's own words carry no long dash, and no spaced hyphen standing in for one. The substitute
is a full stop, a colon, a comma or parentheses.

No claim changed, so this is recorded here and not as a new entry in the corrections index. The index's
entry for this page, C-20261115-02, quotes the sentence; the change to its quotation is recorded in that
entry, with the earlier punctuation.

The head note of this file now gives the dates of the three notes on the home page, 28 and 29 July 2026,
where it said "from July 2026", which read as a continuing practice.

## 17 November 2026: narrow screens

In Chromium, the home page and the Dose 01 page no longer scroll sideways at phone widths, and the home
page no longer does at tablet widths. The numbers in this entry are Chromium's, except in the last
paragraph, which says what was measured in Safari and what was not.

Before this change the home page's document was 596 px wide in every window narrower than that (measured
at 320, 375, 390, 430 and 595 px) and 1033 px wide in a window 861 to 1032 px wide. The Dose 01 page's
document was 566 px wide in a window 320, 375, 390 or 430 px wide. After the change, each document is
exactly as wide as its window at each of 68 widths from 320 to 1920 px.

Everything that changed is in the one style block the two pages share:

- The levers table needs 571 px as three columns. At 640 px and below, each row takes two lines: the
  lever beside its failure mode, then where you see it. The cells and their order are the same.
- The name and the domain tag in the header need 411 px side by side. In less, the tag takes a second
  line.
- The header's link row needs 1075 px beside the name at full spacing: below 1077 px its spacing
  tightens, and below 1016 px it wraps to a second line inside the bar. From 1077 px up the header is as
  it was.
- The Carrier Color statement is one line of 34 characters that cannot break. In a window narrower than
  430 px it follows the width so that it stays whole. At 375 px wide it is set at 14.1 px, where it was
  16.8 px and ran past the window's edge.
- At 480 px and below, the equation boxes have less padding at their sides.
- An image stops at the width of its column, and a callout may break a word longer than its line.

No word, link or image changed: each page's bytes after the style block are identical. Full-page
screenshots at 1080, 1280, 1440 and 1920 px wide are byte-for-byte the same before and after. The style
block's hash changed with the block and is pinned again in each page's own policy and in the response
header policy. This is recorded here and not in the corrections index because nothing a reader was told
changed.

The numbers above are from Chromium 141 and Chrome 157 on macOS. Mobile Safari was measured separately,
before the merge, in the iOS Simulator (iOS 27.0), by comparing a frame of the page at rest with a frame
after a push to the left. Before this change the home page moved 222 px sideways in a window 375 points
wide and 195 px in one 402 points wide, and the Dose 01 page moved 191 px at 375. With this change the
home page did not move at 375 or at 402, and the Dose 01 page did not move at 375. Not measured: a real
iPhone, any tablet width in Safari, Safari on a Mac, and a phone turned on its side.
