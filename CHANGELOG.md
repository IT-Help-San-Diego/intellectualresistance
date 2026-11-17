# Change log

This file records changes to intellectualresistance.com that are not corrections: nothing a reader was
told was wrong. Corrections are not recorded here. They are made where a reader sees them: as an entry in
the family corrections index, https://www.it-help.tech/corrections/, which the home page links from its
footer, and, from July 2026, as three dated notes on the home page, each beside the passage it concerns.

This file is for whoever maintains the site. It is not served: the deploy leaves every `.md` file out of
the bucket.

This file begins with the entry below. Earlier changes are in this repository's history. Newest first.
Each heading gives the day in UTC, and the day in Los Angeles where the two differ.

## 17 November 2026: narrow screens

In Chromium, the home page and the Dose 01 page no longer scroll sideways at phone widths, and the home
page no longer does at tablet widths. Chromium is the one engine these numbers come from: see the last
paragraph.

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

The measurements are from Chromium 141 and Chrome 157 on macOS. Safari was not measured for this change.
Every browser on an iPhone runs Safari's engine, so nothing here says the change is verified on an
iPhone.
