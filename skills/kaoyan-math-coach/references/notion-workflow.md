# Notion Workflow

Use this reference only when recording or reviewing the student's established Notion learning system.

Keep the question-bank organization and the error-review organization separate. The question bank is indexed by local position and entry-to-path mapping; the review database stores path-repair evidence and the student's actual route.

## Connection

DSH has no built-in Notion connector and no MCP server for it. Use the Notion REST API through `scripts/notion_api.ps1`.

- Integration secret: `%USERPROFILE%\.dsh\notion-token.txt`, a single line. Keep it out of the git repository (this workspace has a GitHub remote).
- The internal integration must be connected to the hub page and to each of the four databases, or that object answers 404.
- The sandbox blocks outbound network under `workspace-write`; Notion calls only succeed where network is available. A blocked call fails as a closed connection, not as an HTTP status.
- A local HTTP proxy on `127.0.0.1:7897` is detected and used automatically. Override with `-Proxy`, disable with `-NoProxy`.
- Use `Notion-Version: 2025-09-03`. Query rows through `POST /v1/data_sources/<data_source_id>/query`; the bare database ID only serves schema lookup.
- Send request bodies as UTF-8 bytes. PowerShell 5.1 otherwise mangles Chinese property values.
- A `GET` request must carry no body at all.
- Verified 2026-10-22 on workspace `ziraw's Notion`: read of all four targets, page create, and move-to-trash all succeed.

## Existing Destination

- Hub page: `题目复盘与方法沉淀`
- Hub page ID: `3a3af6c3-0605-810b-b68f-c4f2ab370b69`
- Hub URL: `https://app.notion.com/p/3a3af6c30605810bb68fc4f2ab370b69`
- Database: `考研数学题目复盘数据库`
- Database URL: `https://app.notion.com/p/9beb138ae9be46cc8ff97da9a98f2898`
- Data source ID: `collection://787ee68f-f3f0-475a-915f-e50a2f1afe4e`

## Question-Count Progress

- Database: `考研数学题数进度`
- Database URL: `https://app.notion.com/p/023d75029feb415b84aba873165d9c1a`
- Data source ID: `collection://b8934194-260b-480b-97b8-c5c559ded67e`
- Overview page: `考研数学进度总览`
- Overview page URL: `https://app.notion.com/p/3b0af6c3060581689ab6c56958775b7d`

This tracker is pre-populated from the local Obsidian question-bank files: one `最小节` row per file with a `题量` line, summary rows for each `大节` and `学科`, and overall rows. The current baseline counts the sections the student has explicitly completed in the study sequence. A closeout updates the leaf row to its full question count and then recalculates the containing large chapter, subject, three-subject total, and all-question-bank total. Use the question count in the source file, never the number of Notion records or method cards.

Baseline reconciled on 2026-10-22: 567 `最小节` rows, of which 53 are `已完成` for 617 questions (高等数学 51 sections / 586 questions, 线性代数 2 sections / 31 questions). The current section `已知极限（存在）确定参数` holds 51 questions and stays `进行中` with `0` completed until closeout. Subject and overall rows now read 高等数学 586/3343, 线性代数 31/952, 三科题库 617/4612, 全部题库 617/4619.

A leaf row's `题目总数` matched the local `题量` line in every file checked, so treat the leaves as the source of truth and recompute the three summary layers from them rather than trusting a summary row that was not refreshed. Row titles are inconsistent about spacing around `/`: leaf titles use `01 高等数学/01 极限/...` while summary titles use `01 高等数学 / 01 极限`. Normalize with `-replace '\s*/\s*','/'` before matching prefixes. An empty `已完成题数` on an unfinished leaf means zero, not a missing value.

## Delayed Method Network

- Database: `考研数学题型与方法网络`
- Database URL: `https://app.notion.com/p/36e6f738c0a3457d805b8b5bfd69dca5`
- Data source ID: `collection://81cdf605-a8c1-4e65-8d3f-90ae83ccc793`

This database is a section-closeout artifact, not a live tagging system. Do not create method cards while solving individual questions. After a section is finished, synthesize the landing-point map first, then create or update exactly one node for that whole section. Put multiple methods and landing points inside the node body as headings and subsections.

Operational properties are limited to:

- `方法节点`: title
- `位置`: text, omit the highest subject level and keep at most the next three directory levels
- `掌握情况`: select; 已建立 / 待补充 / 需验证

Write all substantive content in the page body: section signals, method branches, control relations, landing points, boundaries, variants, representative question evidence, and the next trigger rule.

Fetch the database before creating or updating records because the schema may evolve.

## Current Properties

Verified against the live data source on 2026-10-22. The schema has grown past the original short list: treat this section as the authority and re-fetch before writing if a property is rejected.

- `题目标题`: title
- `日期`: date
- `知识模块`: select; 高等数学 / 线性代数 / 概率论与数理统计
- `细分知识点`: multi_select; extend options only when a new recurring topic requires it, never rename existing ones
- `题型`: select; 选择题 / 填空题 / 解答题
- `错误类型`: multi_select; 入口选择错误 / 结构信号漏看 / 知识点不熟 / 计算失误 / 做题策略问题 / 时间管理风险 / 审题陷阱
- `题型分类`: multi_select; currently only 计算能力专题. Use it for cross-chapter training themes, not for the chapter position.
- `掌握状态`: select; 待复盘 / 已纠偏 / 待二刷 / 已掌握 / 待复核
- `考场风险`: select; 低 / 中 / 高
- `二刷日期`: date
- `二刷结果`: select; 未二刷 / 独立做出 / 提示后做出 / 再次做错
- `首次耗时（分钟）`: number
- `首次信心`: select; 确定 / 犹豫 / 蒙猜
- `复发次数`: number
- `一句话沉淀`: rich_text
- `题库路径`: rich_text; full local question-bank path
- `章节目录`: rich_text; chapter directory segment
- `专题目录`: rich_text; topic directory segment
- `题型目录`: rich_text; question-type file segment
- `小节目录`: rich_text; smallest section name
- `方法节点`: relation, single_property, target `collection://81cdf605-a8c1-4e65-8d3f-90ae83ccc793`. Link only when that section's method node already exists at closeout; never create a method node to satisfy this field.

The five directory/position fields replace guessing from prose. Fill only the segments the local source actually provides, and leave the rest empty rather than inventing a level.

## Progress Tracker Properties

- `进度节点`: title
- `题库位置`: rich_text
- `题目总数`: number
- `已完成题数`: number
- `完成状态`: select; 未开始 / 进行中 / 已完成
- `统计层级`: select; 最小节 / 大节 / 学科 / 总体

Do not invent unavailable property values. Leave them empty until the student provides evidence.

## Record Content Order

Create one page per problem with this order:

1. `原始题目`: exact statement and options; preserve the image when upload is supported.
2. `题库定位`: local category path, question ID, source, and matched lecture section when found.
3. `标准结论`: intended answer and any formal caveat.
4. 我的真实过程：retain the student's actual wording, route, hesitation, time, confidence, and feeling. Do not replace it with the polished solution.
5. 状态—路径切片：S_0, target G, strong signals, candidate tools, first operation, intermediate state, and landing point.
6. 诊断校准：one primary failure layer, route verdict, and any secondary cause.
7. 出题专家视角：strong signals, decoy trigger, target skill, and option construction.
8. 考场解法：preferred route with Notion-compatible LaTeX.
9. 方法抽象与推广：problem signal, method choice, reusable template, variant boundary, and when to switch methods.
10. 做题专家纠偏：route comparison, earliest warning sign, stop-loss, and backup.
11. 暴露的问题：evidence-based diagnosis by layer.
12. 修复动作：the exact first action and route replacement for the next encounter.
13. 知识小网：core proposition, two to four variants, nearest prerequisite/sibling/application/trap nodes, and typed relationships.
14. 下次触发规则：visible cue, first action, fallback.
15. 迁移与二刷：transfer prompt, due date, and later result.
16. 一句话沉淀.

## Writing Rules

- Always format mathematical formulas with Notion's native equation syntax:
  - **Block-level formulas**: Use Notion equation blocks `{"object": "block", "type": "equation", "equation": {"expression": "..."}}`.
  - **Inline formulas**: Use Notion equation rich_text items `{"type": "equation", "equation": {"expression": "..."}}` within text, callout, or list blocks.
  - Never output raw LaTeX delimiters (`$...$`, `\(...\)`, `\[...\]`) or ascii math as plain text content in Notion.
  - Ensure all math variables ($x$, $a$, $f(x)$), limits, and expressions are explicitly converted to Notion equation objects.
- Verify rendered equations and blocks by fetching the page after creation or update.
- Keep the original problem before any explanation.
- Keep the student's original reasoning separate from the corrected version.
- A problem enters this review database not only when the final answer is wrong, but also when it was guessed, slow, explanation-dependent, low-efficiency, or exposed a repeated path break.
- Assign exactly one primary failure layer. Use 计算失误 for arithmetic, sign, omitted derivative, algebraic, or notation execution errors; record earlier path-selection failures as primary when they caused the later calculation error.
- Set `掌握状态` to `已纠偏` after the first complete review unless independent delayed evidence already exists.
- Set `二刷结果` to `未二刷` only when a retry is genuinely pending; do not invent a schedule.
- Increment `复发次数` only when a later problem demonstrates the same diagnosed pattern.

## Safe Update Sequence

1. Fetch the destination data source and, for edits, the existing page.
2. Create a new record or make the smallest targeted update.
3. Verify the page content, formulas, and properties by fetching it again.
4. Preserve unrelated user changes and existing child pages/databases.
