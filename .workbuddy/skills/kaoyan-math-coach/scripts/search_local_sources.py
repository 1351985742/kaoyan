#!/usr/bin/env python3
"""Rank relevant Markdown files in the student's local lecture and question bank."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


LECTURE_ROOT = Path("/Users/devilrecal/Downloads/教材/讲义")
BANK_ROOT = Path("/Users/devilrecal/Downloads/教材/Obsidian题库")


@dataclass
class Match:
    score: int
    path: Path
    snippets: list[tuple[int, str]]


def compact(value: str) -> str:
    """Normalize spacing and common Markdown/LaTeX wrappers for fuzzy phrase matches."""
    return re.sub(r"[\s`$\\{}_^*（）()【】\[\]]+", "", value.casefold())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("terms", nargs="+", help="Chinese or mathematical search terms")
    parser.add_argument("--scope", choices=("all", "lecture", "bank"), default="all")
    parser.add_argument(
        "--chapter",
        help="Optional chapter or category hint; boosts matching paths/content without filtering",
    )
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--snippets", type=int, default=3)
    return parser.parse_args()


def iter_markdown(scope: str):
    if scope in ("all", "lecture") and LECTURE_ROOT.exists():
        for path in LECTURE_ROOT.rglob("*.md"):
            if path.name == "book.md" or "assets" in path.parts:
                continue
            yield "lecture", LECTURE_ROOT, path
    if scope in ("all", "bank") and BANK_ROOT.exists():
        for path in BANK_ROOT.rglob("*.md"):
            if ".obsidian" in path.parts or "_meta" in path.parts:
                continue
            yield "bank", BANK_ROOT, path


def rank_file(
    kind: str,
    root: Path,
    path: Path,
    terms: list[str],
    chapter: str | None,
    snippet_limit: int,
) -> Match | None:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None

    relative = str(path.relative_to(root))
    relative_folded = relative.casefold()
    text_folded = text.casefold()
    relative_compact = compact(relative)
    text_compact = compact(text)
    folded_terms = [term.casefold() for term in terms]
    compact_terms = [compact(term) for term in terms]

    found = [
        raw in relative_folded
        or raw in text_folded
        or (normalized and (normalized in relative_compact or normalized in text_compact))
        for raw, normalized in zip(folded_terms, compact_terms)
    ]
    if not any(found):
        return None

    score = 0
    for term, normalized, is_found in zip(folded_terms, compact_terms, found):
        if not is_found:
            continue
        if term in relative_folded or (normalized and normalized in relative_compact):
            score += 30
        count = max(text_folded.count(term), text_compact.count(normalized) if normalized else 0)
        score += min(count, 20)
    if all(found):
        score += 25
    if kind == "bank" and "题目" in text[:200]:
        score += 2
    if chapter:
        chapter_folded = chapter.casefold()
        chapter_compact = compact(chapter)
        if chapter_folded in relative_folded or (
            chapter_compact and chapter_compact in relative_compact
        ):
            score += 60
        elif chapter_folded in text_folded or (
            chapter_compact and chapter_compact in text_compact
        ):
            score += 12

    snippets: list[tuple[int, str]] = []
    for number, line in enumerate(text.splitlines(), start=1):
        line_folded = line.casefold()
        line_compact = compact(line)
        hits = sum(
            raw in line_folded or (normalized and normalized in line_compact)
            for raw, normalized in zip(folded_terms, compact_terms)
        )
        if not hits:
            continue
        if line.lstrip().startswith("#"):
            score += 4 * hits
        cleaned = " ".join(line.strip().split())
        if cleaned and len(snippets) < snippet_limit:
            snippets.append((number, cleaned[:260]))

    return Match(score=score, path=path, snippets=snippets)


def main() -> int:
    args = parse_args()
    matches = []
    for kind, root, path in iter_markdown(args.scope):
        match = rank_file(kind, root, path, args.terms, args.chapter, args.snippets)
        if match:
            matches.append(match)

    matches.sort(key=lambda item: (-item.score, str(item.path)))
    for match in matches[: max(args.limit, 0)]:
        print(f"[{match.score}] {match.path}")
        for line_number, snippet in match.snippets:
            print(f"  L{line_number}: {snippet}")

    if not matches:
        print("No matching Markdown sources found.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
