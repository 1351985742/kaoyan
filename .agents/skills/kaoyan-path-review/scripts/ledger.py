#!/usr/bin/env python3
"""Persist path-review evidence and history; never infer mathematical mastery."""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile


DIMENSIONS = ("题型识别与方法选择", "整体流程", "中间处理", "完整执行")
STATUSES = ("进行中", "本轮已复习")
MODES = ("思路回顾", "片段手算", "完整作答")
INDEPENDENCE = ("独立", "提示后", "看过解答", "未说明")
SYNC = ("未使用", "待同步", "已核验")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def heading_paths(path):
    """Return literal ATX heading ancestry, excluding fenced code blocks."""
    stack = []
    found = []
    fence_char, fence_len = None, 0
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence_char is not None:
            if fence and fence[1][0] == fence_char and len(fence[1]) >= fence_len and not fence[2].strip():
                fence_char = None
            continue
        if fence:
            fence_char, fence_len = fence[1][0], len(fence[1])
            continue
        match = re.match(r"^ {0,3}(#{1,6})[ \t]+(.+?)\s*$", line)
        if not match:
            continue
        level = len(match[1])
        title = re.sub(r"[ \t]+#+[ \t]*$", "", match[2]).strip()
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        found.append({"line": line_number, "heading_path": [item[1] for item in stack]})
    return found


def load_ledger(root):
    path = root / "ledger.json"
    if not path.exists():
        return None
    value = read_json(path)
    require(isinstance(value, dict) and value.get("schema_version") == 1, "不支持的台账格式；未覆盖原文件")
    require(isinstance(value.get("paths"), dict), "台账 paths 格式错误")
    return value


def atomic_write(path, contents):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".review-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(contents)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render(ledger):
    paths = list(ledger["paths"].values())
    counts = {key: 0 for key in ("未开始", *STATUSES)}
    for entry in paths:
        counts[entry["history"][-1]["status"] if entry["history"] else "未开始"] += 1
    lines = [
        "# 路径复习台账", "",
        f"范围：{ledger['scope_note']}", "",
        f"已登记 {len(paths)} 条原目录条目；" + "；".join(f"{key} {value}" for key, value in counts.items()) + "。", "",
        "原目录条目可能是同一上位路径的不同分支，以上是条目状态，不是独立路径数。本轮已复习与能力已验证分开记录；以下仅统计已登记范围，不代表整个题库。", "",
        "已确认的层级和待办见 `路径层级校准.md`（如已建立）。", "",
        "本文件由 ledger.json 生成。", "",
        "| ID | 原文件与路径 | 本轮状态 | 未完成事项 |", "| --- | --- | --- | --- |",
    ]
    for entry in paths:
        latest = entry["history"][-1] if entry["history"] else None
        location = entry["source_file"] + " / " + " / ".join(entry["heading_path"])
        lines.append("| " + " | ".join(map(cell, (
            entry["path_id"], location, latest["status"] if latest else "未开始",
            "；".join(latest["followups"]) if latest else "尚未复习",
        ))) + " |")
    for entry in paths:
        lines += ["", f"## {entry['path_id']}｜{entry['heading_path'][-1]}", "", f"原文件：{entry['source_file']}"]
        for event in entry["history"]:
            lines += ["", f"### {event['date']}｜{event['session_id']}｜{event['status']}", ""]
            for dimension in DIMENSIONS:
                lines.append(f"- {dimension}：{event['assessment'][dimension]}")
            lines += ["", "实际题目活动：", ""]
            for question in event["questions"]:
                lines.append(f"- {question['question_id']}｜{question['mode']}｜{question['independence']}：{question['evidence']}")
                if question.get("review_mark"):
                    lines.append(f"  - 本轮路径标记：{question['review_mark']}；依据：{question.get('mark_reason', '见上述过程')}")
                if question.get("calculation_mark"):
                    lines.append(f"  - 关键处理标记：{question['calculation_mark']}；依据：{question.get('calculation_reason', '见上述过程')}；实际计算：{question.get('calculation_executed', '未说明')}")
            if not event["questions"]:
                lines.append("- 尚无题目作答证据。")
            if event.get("fragment_decisions"):
                lines += ["", "出题前中间处理判定（计划，不是作答证据）：", ""]
                for decision in event["fragment_decisions"]:
                    lines.append(f"- {decision['question_id']}｜{decision['decision']}｜片段：{decision['fragment']}；理由：{decision['rationale']}；依据：{decision['evidence_basis']}；后续：{decision['followup']}")
            if event["fragments"]:
                lines += ["", "中间片段证据：", "", "```json", json.dumps(event["fragments"], ensure_ascii=False, indent=2), "```"]
            lines += ["", "当前待办：", ""]
            lines += [f"- {item}" for item in event["followups"]] or ["- 无已记录待办；不据此认定掌握。"]
            lines += ["", f"下一动作：{event['next_action']}", "", f"Notion 同步：{event['notion_sync']}"]
            if event["problem_records"]:
                lines += ["", "原复盘或待同步稿：", "", *[f"- {item}" for item in event["problem_records"]]]
    return "\n".join(lines) + "\n"


def save(root, ledger):
    atomic_write(root / "ledger.json", json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
    require(read_json(root / "ledger.json") == ledger, "主数据回读核验失败")
    try:
        markdown = render(ledger)
        atomic_write(root / "台账.md", markdown)
        require((root / "台账.md").read_text(encoding="utf-8") == markdown, "总览回读核验失败")
    except (OSError, ValueError) as error:
        raise ValueError(f"主数据已保存，但 Markdown 总览未成功更新；请用相同输入重试：{error}") from error


def register(root, payload):
    require(isinstance(payload, dict), "注册输入必须为对象")
    bank = Path(payload["bank_root"]).expanduser().resolve()
    require(bank.is_dir(), "题库根目录不存在")
    require(nonempty(payload.get("scope_note")), "缺少实际复习范围 scope_note")
    require(isinstance(payload.get("paths"), list) and payload["paths"], "没有待注册路径")
    ledger = load_ledger(root) or {"schema_version": 1, "bank_root": str(bank), "scope_note": payload["scope_note"], "paths": {}}
    require(ledger["bank_root"] == str(bank), "不能更换既有台账的题库根目录")
    require(ledger["scope_note"] == payload["scope_note"], "复习范围描述与原台账不同；请先核实范围，不自动覆盖")
    registered = []
    for item in payload["paths"]:
        require(isinstance(item, dict) and nonempty(item.get("source_file")), "缺少原题库文件")
        relative = Path(item["source_file"])
        require(not relative.is_absolute() and ".." not in relative.parts, "source_file 必须为题库内相对路径")
        source = (bank / relative).resolve()
        require(source.is_relative_to(bank) and source.is_file(), "原题库文件不存在或不在题库范围")
        headings = item.get("heading_path")
        require(isinstance(headings, list) and headings and all(nonempty(x) for x in headings), "缺少完整原始标题序列")
        matches = [x for x in heading_paths(source) if x["heading_path"] == headings]
        require(len(matches) == 1, f"原路径定位不存在或不唯一：{relative} / {headings}")
        normalized = source.relative_to(bank).as_posix()
        identity = json.dumps([normalized, headings], ensure_ascii=False, separators=(",", ":"))
        path_id = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
        existing = ledger["paths"].get(path_id)
        require(existing is None or (existing["source_file"] == normalized and existing["heading_path"] == headings), "路径 ID 冲突")
        if existing is None:
            ledger["paths"][path_id] = {"path_id": path_id, "source_file": normalized, "heading_path": headings, "history": []}
        registered.append({"path_id": path_id, "source_file": normalized, "heading_path": headings})
    save(root, ledger)
    return {"saved_and_verified": True, "registered": registered, "total_registered": len(ledger["paths"])}


def validate_event(event):
    require(isinstance(event, dict), "日志必须为对象")
    for key in ("path_id", "session_id", "date", "next_action"):
        require(nonempty(event.get(key)), f"缺少 {key}")
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", event["date"]) is not None, "日期需为 YYYY-MM-DD")
    date.fromisoformat(event["date"])
    require(event.get("status") in STATUSES, "无效本轮流程状态")
    require(event.get("notion_sync") in SYNC, "需明确实际 Notion 同步状态")
    if "fragment_decisions" in event:
        require(isinstance(event["fragment_decisions"], list), "fragment_decisions 必须为列表")
        for decision in event["fragment_decisions"]:
            require(isinstance(decision, dict) and all(nonempty(decision.get(key)) for key in ("question_id", "decision", "fragment", "rationale", "evidence_basis", "followup")), "中间处理判定缺少必要字段")
            require(decision["decision"] in ("思路回顾", "写关键过程", "完整作答"), "无效中间处理决定")
    assessment = event.get("assessment")
    require(isinstance(assessment, dict) and all(nonempty(assessment.get(key)) for key in DIMENSIONS), "需分别记录四维证据；未知写未验证")
    for key in ("questions", "fragments", "followups", "problem_records"):
        require(isinstance(event.get(key), list), f"{key} 必须为列表")
    for key in ("followups", "problem_records"):
        require(all(nonempty(item) for item in event[key]), f"{key} 含空白条目")
    if event["status"] == "本轮已复习":
        require(bool(event["questions"]), "无题目活动证据，不能标本轮已复习")
    for question in event["questions"]:
        require(isinstance(question, dict), "题目活动必须为对象")
        require(nonempty(question.get("question_id")) and nonempty(question.get("evidence")), "题目活动缺少题号或实际证据")
        require(question.get("mode") in MODES, "无效作答方式")
        require(question.get("independence") in INDEPENDENCE, "独立性未知需记未说明")
    seen = set()
    for fragment in event["fragments"]:
        require(isinstance(fragment, dict), "片段必须为对象")
        for key in ("fragment_id", "question_id", "input_context", "conditions", "result", "evidence"):
            require(nonempty(fragment.get(key)), f"片段缺少 {key}")
        require(fragment.get("task_kind") in ("识别与选择", "执行"), "需区分片段选择与执行验证")
        require(fragment["fragment_id"] not in seen, "同次日志片段 ID 重复")
        seen.add(fragment["fragment_id"])


def record(root, event):
    validate_event(event)
    ledger = load_ledger(root)
    require(ledger is not None, "请先注册原路径")
    require(event["path_id"] in ledger["paths"], "未登记的路径 ID")
    history = ledger["paths"][event["path_id"]]["history"]
    same = [x for x in history if x["session_id"] == event["session_id"]]
    require(not same or same[0] == event, "同日志 ID 已有不同内容；请用新日志 ID 追加，旧历史未覆盖")
    if not same:
        history.append(event)
    save(root, ledger)
    return {"saved_and_verified": True, "path_id": event["path_id"], "idempotent_retry": bool(same), "history_count": len(history), "status": history[-1]["status"], "ledger": str(root / "ledger.json"), "overview": str(root / "台账.md")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    headings = commands.add_parser("headings", help="列出源文件标题，不自动分类路径")
    headings.add_argument("--file", required=True, type=Path)
    for name in ("register", "record", "show"):
        command = commands.add_parser(name)
        command.add_argument("--root", required=True, type=Path)
        if name == "show":
            command.add_argument("--path-id")
        else:
            command.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.command == "headings":
            result = heading_paths(args.file)
        elif args.command == "register":
            result = register(args.root.expanduser().resolve(), read_json(args.input))
        elif args.command == "record":
            result = record(args.root.expanduser().resolve(), read_json(args.input))
        else:
            result = load_ledger(args.root.expanduser().resolve())
            if args.path_id:
                require(result is not None and args.path_id in result["paths"], "未登记的路径 ID")
                result = result["paths"][args.path_id]
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"台账操作失败：{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
