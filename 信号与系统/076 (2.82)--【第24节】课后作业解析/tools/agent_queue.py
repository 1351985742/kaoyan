#!/usr/bin/env python3
"""Small helpers for the office Agent that consumes MinerU chapter outputs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def load_queue(output_dir: Path) -> dict[str, Any]:
    queue_path = output_dir / "agent_inbox" / "queue.json"
    if not queue_path.exists():
        raise SystemExit(f"queue.json not found: {queue_path}")
    return json.loads(queue_path.read_text(encoding="utf-8"))


def save_queue(output_dir: Path, queue: dict[str, Any]) -> None:
    queue_path = output_dir / "agent_inbox" / "queue.json"
    queue_path.write_text(
        json.dumps(queue, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def list_items(output_dir: Path) -> None:
    queue = load_queue(output_dir)
    for item in queue.get("items", []):
        print(
            f"{item['order']:03d}  {item['status']:<10}  "
            f"{item['pages']:<11}  {item['chapter_path']}"
        )


def mark_item(output_dir: Path, order: int, status: str) -> None:
    queue = load_queue(output_dir)
    allowed = {"pending", "processing", "done", "blocked", "skipped"}
    if status not in allowed:
        raise SystemExit(f"status must be one of: {', '.join(sorted(allowed))}")

    for item in queue.get("items", []):
        if item.get("order") == order:
            item["status"] = status
            save_queue(output_dir, queue)
            print(f"marked {order:03d} as {status}")
            return
    raise SystemExit(f"order not found: {order}")


def validate_links(output_dir: Path) -> None:
    queue = load_queue(output_dir)
    missing: list[str] = []

    for item in queue.get("items", []):
        chapter = output_dir / item["chapter_path"]
        if not chapter.exists():
            missing.append(f"missing chapter: {chapter}")
            continue

        text = chapter.read_text(encoding="utf-8", errors="replace")
        for match in IMAGE_LINK_RE.finditer(text):
            target = match.group(1).strip().strip('"').strip("'")
            if target.startswith(("http://", "https://", "data:")):
                continue
            image_path = (chapter.parent / target).resolve()
            if not image_path.exists():
                missing.append(f"{chapter.name}: missing image {target}")

    if missing:
        print("\n".join(missing))
        raise SystemExit(1)

    print("ok: all queued chapter image links resolve")


def main() -> int:
    parser = argparse.ArgumentParser(description="Manage MinerU Agent queue files.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List chapter queue items.")
    list_parser.add_argument("output_dir", type=Path)

    mark_parser = subparsers.add_parser("mark", help="Mark a queue item status.")
    mark_parser.add_argument("output_dir", type=Path)
    mark_parser.add_argument("order", type=int)
    mark_parser.add_argument("status")

    validate_parser = subparsers.add_parser("validate", help="Validate chapter image links.")
    validate_parser.add_argument("output_dir", type=Path)

    args = parser.parse_args()
    output_dir = args.output_dir.expanduser().resolve()

    if args.command == "list":
        list_items(output_dir)
    elif args.command == "mark":
        mark_item(output_dir, args.order, args.status)
    elif args.command == "validate":
        validate_links(output_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
