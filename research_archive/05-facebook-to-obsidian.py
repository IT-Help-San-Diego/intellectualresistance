#!/usr/bin/env python3
"""
Facebook Archive to Obsidian Converter

Converts a Facebook post archive into Obsidian markdown notes.

Supported input:
1. Preferred: JSON list of post objects, such as 04-facebook-archive.json.
2. Fallback: CSV crawl export with post text columns.

This script skips posts in DELETE_LIST and creates:
- one markdown note per kept post
- 00-TIMELINE.md
- 00-IMPORT-REPORT.md

Project: Intellectual Resistance
Author: Carey Balboa + Perplexity Computer
Date: 2026-05-15
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any


DELETE_LIST = {7, 14, 19, 46, 56, 80, 86, 99, 104, 106}


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("|", "\n")
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def yaml_string(value: Any) -> str:
    text = clean_text(value)
    return json.dumps(text, ensure_ascii=False)


def safe_filename(value: Any) -> str:
    text = clean_text(value) or "unknown"
    text = re.sub(r"[^\w.\-]+", "-", text, flags=re.UNICODE).strip("-")
    return text[:120] or "unknown"


def normalize_tags(tags: list[str]) -> str:
    return "[" + ", ".join(tags) + "]"


def load_json_posts(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        for key in ("posts", "data", "items"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
    if not isinstance(data, list):
        raise ValueError(f"{path} does not contain a JSON list of posts")
    posts: list[dict[str, Any]] = []
    for index, item in enumerate(data, 1):
        if isinstance(item, dict):
            post = dict(item)
        else:
            post = {"body": clean_text(item)}
        post.setdefault("post_id", index)
        posts.append(post)
    return posts


def load_csv_posts(path: Path) -> list[dict[str, Any]]:
    posts: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8-sig", newline="", errors="replace") as handle:
        reader = csv.DictReader(handle)
        for index, row in enumerate(reader, 1):
            candidates = [
                row.get("text"),
                row.get("text general"),
                row.get("text2"),
                row.get("Column 3"),
                row.get("Opmerking"),
                row.get("body"),
            ]
            body = next((clean_text(value) for value in candidates if clean_text(value)), "")
            if not body:
                continue
            if body.lower() in {"share a thought...", "see more", "filters\nmanage posts"}:
                continue
            posts.append(
                {
                    "post_id": index,
                    "date": clean_text(row.get("date")) or "unknown",
                    "author": "Carey James Balboa",
                    "audience": "Public",
                    "body": body,
                    "reactions": clean_text(row.get("Likes")) or 0,
                    "comments": [],
                    "source_row": index,
                    "source_file": path.name,
                }
            )
    return posts


def auto_tags(body: str) -> list[str]:
    tags = ["facebook", "epistemic-clean"]
    body_lower = body.lower()
    if "verify" in body_lower:
        tags.append("verification-principle")
    if "fact" in body_lower and "opinion" in body_lower:
        tags.append("epistemic-boundary")
    if "left" in body_lower and "right" in body_lower:
        tags.append("anti-tribalism")
    if "pattern" in body_lower or "metacogn" in body_lower:
        tags.append("metacognition")
    if "ai" in body_lower:
        tags.append("ai-accountability")
    if "dns" in body_lower:
        tags.append("dns-tool")
    return sorted(set(tags), key=tags.index)


def first_line(body: str, limit: int = 180) -> str:
    line = clean_text(body).split("\n", 1)[0]
    return line[:limit] + ("…" if len(line) > limit else "")


def convert_posts(posts: list[dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    created = 0
    skipped = 0
    kept_posts: list[dict[str, Any]] = []

    for ordinal, post in enumerate(posts, 1):
        post_id_raw = post.get("post_id", ordinal)
        try:
            post_id_int = int(post_id_raw)
        except (TypeError, ValueError):
            post_id_int = ordinal

        if post_id_int in DELETE_LIST:
            skipped += 1
            continue

        date = clean_text(post.get("date")) or "unknown"
        body = clean_text(post.get("body") or post.get("text") or "(No body captured)")
        url = clean_text(post.get("url"))
        reactions = post.get("reactions", 0) or 0
        comments = post.get("comments") or []
        if not isinstance(comments, list):
            comments = []

        tags = auto_tags(body)
        filename = output_dir / f"{safe_filename(date)}-post-{safe_filename(post_id_raw)}.md"

        with filename.open("w", encoding="utf-8") as handle:
            handle.write("---\n")
            handle.write(f"date: {yaml_string(date)}\n")
            handle.write("source: facebook\n")
            handle.write(f"post_id: {yaml_string(post_id_raw)}\n")
            if url:
                handle.write(f"url: {yaml_string(url)}\n")
            handle.write(f"reactions: {yaml_string(reactions)}\n")
            handle.write(f"tags: {normalize_tags(tags)}\n")
            handle.write("---\n\n")
            handle.write(f"# Post {post_id_raw} — {date}\n\n")
            if url:
                handle.write(f"[View on Facebook]({url})\n\n")
            handle.write(f"## Content\n\n{body}\n\n")
            if reactions:
                handle.write(f"**Reactions:** {reactions}\n\n")
            if comments:
                handle.write(f"## Comments ({len(comments)})\n\n")
                for comment in comments:
                    if isinstance(comment, dict):
                        author = clean_text(comment.get("author")) or "Unknown"
                        text = clean_text(comment.get("text"))
                    else:
                        author = "Unknown"
                        text = clean_text(comment)
                    if text:
                        handle.write(f"**{author}:** {text}\n\n---\n\n")
            handle.write("## Analysis\n\n_[Add your analysis]_\n\n")
            handle.write("## Related Notes\n\n")
            handle.write("- [[00-TIMELINE|Facebook Archive Timeline]]\n")
            handle.write("- [[Intellectual Resistance Development]]\n")

        created += 1
        kept_posts.append(post)

    create_timeline(posts, kept_posts, output_dir)
    create_report(posts, created, skipped, output_dir)

    print(f"Created {created} Obsidian notes")
    print(f"Skipped {skipped} posts from delete list")
    print(f"Output: {output_dir}")


def create_timeline(all_posts: list[dict[str, Any]], kept_posts: list[dict[str, Any]], output_dir: Path) -> None:
    timeline = output_dir / "00-TIMELINE.md"
    with timeline.open("w", encoding="utf-8") as handle:
        handle.write("---\n")
        handle.write("type: index\n")
        handle.write("tags: [facebook, timeline, master-index, intellectual-resistance]\n")
        handle.write("---\n\n")
        handle.write("# Facebook Archive Timeline\n\n")
        handle.write(f"**Total input records:** {len(all_posts)}\n")
        handle.write(f"**Kept records:** {len(kept_posts)}\n")
        handle.write(f"**Delete-list IDs:** {len(DELETE_LIST)}\n\n---\n\n")

        sorted_posts = sorted(
            all_posts,
            key=lambda item: clean_text(item.get("date")),
            reverse=True,
        )
        for ordinal, post in enumerate(sorted_posts, 1):
            post_id = post.get("post_id", ordinal)
            try:
                post_id_int = int(post_id)
            except (TypeError, ValueError):
                post_id_int = ordinal
            date = clean_text(post.get("date")) or "unknown"
            body = clean_text(post.get("body") or post.get("text"))
            if post_id_int in DELETE_LIST:
                handle.write(f"- ~~**{date}** — Post {post_id} — DELETE-LIST~~\n")
            else:
                handle.write(f"- **{date}** — [[{safe_filename(date)}-post-{safe_filename(post_id)}|Post {post_id}]]\n")
                handle.write(f"  - _{first_line(body)}_\n")


def create_report(all_posts: list[dict[str, Any]], created: int, skipped: int, output_dir: Path) -> None:
    report = output_dir / "00-IMPORT-REPORT.md"
    with report.open("w", encoding="utf-8") as handle:
        handle.write("# Facebook Import Report\n\n")
        handle.write(f"- Input records detected: {len(all_posts)}\n")
        handle.write(f"- Notes created: {created}\n")
        handle.write(f"- Delete-list records skipped: {skipped}\n")
        handle.write(f"- Delete-list IDs: {', '.join(str(x) for x in sorted(DELETE_LIST))}\n\n")
        if len(all_posts) < 129:
            handle.write("## Data completeness warning\n\n")
            handle.write(
                "This run did not contain 129 input records. Use the official Facebook JSON export "
                "or the complete 129-post JSON as the source of truth before treating this archive as complete.\n"
            )


def main() -> None:
    base = Path.cwd()
    candidates = [
        base / "04-facebook-archive.json",
        base / "carey_facebook_archive.json",
        base / "Crawl_2026_05_15_10_35-5.csv",
        base / "fb_comments___708450639-4.csv",
    ]
    existing = [path for path in candidates if path.exists()]
    if not existing:
        raise SystemExit("No supported input found. Add 04-facebook-archive.json or a supported CSV export.")

    source = existing[0]
    if source.suffix.lower() == ".json":
        posts = load_json_posts(source)
    else:
        posts = load_csv_posts(source)

    convert_posts(posts, base / "facebook-archive")


if __name__ == "__main__":
    main()
