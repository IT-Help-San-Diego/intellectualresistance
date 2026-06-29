# Installation Instructions

## Current data status

This package contains the conversation transcript, delete list, README, CSV exports, and the recovered `04-facebook-archive.json` containing 129 Facebook post records. The recovered JSON came from the attached Markdown conversation export. A fresh official Facebook JSON export is still recommended later to fill any `capture_notes` gaps.

## Optional: get the official Facebook source file

1. Open Facebook and go to `facebook.com/dyi`.
2. Choose Download or transfer information.
3. Select your Facebook profile.
4. Choose Some of your information.
5. Select Posts.
6. Set the format to JSON.
7. Use All time, or at minimum January 1, 2023 through May 15, 2026.
8. Create the file and wait for Facebook to prepare the download.
9. Download and unzip the archive.
10. Compare or merge the official export with `04-facebook-archive.json`.

## Run the Obsidian converter

From this package folder:

```bash
python3 05-facebook-to-obsidian.py
```

The script creates a `facebook-archive/` folder with one Markdown note per kept post, plus a timeline and import report.

## Delete-list workflow

Before deleting anything, keep an official Facebook backup. Then use `02-DELETE-LIST-2.md` to find and delete the 10 flagged posts:

```text
7, 14, 19, 46, 56, 80, 86, 99, 104, 106
```

After deleting those posts, download a second clean Facebook archive. That gives you both the legal provenance archive and the cleaned public timeline archive.

## Import to Obsidian

1. Copy `01-CONVERSATION-TRANSCRIPT-3.md` into your Obsidian vault, ideally under `Sessions/`.
2. Copy `02-DELETE-LIST-2.md` and `03-README.md` into the same project folder.
3. Copy the generated `facebook-archive/` folder into the vault.
4. Open `facebook-archive/00-TIMELINE.md` first.

## Recommended folder layout

```text
Intellectual Resistance/
  01-CONVERSATION-TRANSCRIPT-3.md
  02-DELETE-LIST-2.md
  03-README.md
  06-INSTALLATION.md
  facebook-archive/
    00-TIMELINE.md
    00-IMPORT-REPORT.md
    ...
```
