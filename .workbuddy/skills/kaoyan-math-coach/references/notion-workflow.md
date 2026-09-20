# Notion Workflow

Use this reference only when recording or reviewing the student's established Notion learning system.

Keep the question-bank organization and the error-review organization separate. The question bank is indexed by local position and entry-to-path mapping; the review database stores path-repair evidence and the student's actual route.

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

This tracker is pre-populated from the local Obsidian question-bank files: one `最小节` row per file with a `题量` line, summary rows for each `大节` and `学科`, and overall rows. The current baseline counts the sections the student has explicitly completed in the study sequence. A closeout updates the leaf row to its full question count and then recalculates the containing large chapter, subject, three-subject total, and all-question-bank total. Use the question count in the source file, never the number of Notion records or method cards. The current baseline is 572 completed questions from the 49 smallest sections preceding `已知极限（存在）确定参数`; that current section has 51 questions and remains `进行中`, with `0` completed until closeout.

## Delayed Method Network

- Database: `考研数学题型与方法网络`
- Database URL: `https://app.notion.com/p/36e6f738c0a3457d805b8b5bfd69dca5`
- Data source ID: `collection://81cdf605-a8c1-4e65-8d3f-90ae83ccc793`

This database is a section-closeout artifact, not a live tagging system. Do not create method cards while solving individual questions. After a section is finished, synthesize the landing-point map first, then create or update exactly one node for that whole section. Put multiple methods and landing points inside the node body as headings and subsections.

Operational properties are limited to:

- `方法节点`: title
- `位置`: text, omit the highest subject level and keep at most the next three directory levels
- `掌握情况`: the current mastery state

Write all substantive content in the page body: section signals, method branches, control relations, landing points, boundaries, variants, representative question evidence, and the next trigger rule.

Fetch the database before creating or updating records because the schema may evolve.

## Current Properties

- `题目标题`: title
- `日期`: date
- `知识模块`: 高等数学 / 线性代数 / 概率论与数理统计
- `细分知识点`: multi-select; extend options only when a new recurring topic requires it
- `题型`: 选择题 / 填空题 / 解答题
- `错误类型`: 入口选择错误 / 结构信号漏看 / 知识点不熟 / 计算失误 / 做题策略问题 / 时间管理风险
- `掌握状态`: 待复盘 / 已纠偏 / 待二刷 / 已掌握
- `考场风险`: 低 / 中 / 高
- `二刷日期`: date
- `一句话沉淀`: text
- `首次耗时（分钟）`: number
- `首次信心`: 确定 / 犹豫 / 蒙猜
- `二刷结果`: 未二刷 / 独立做出 / 提示后做出 / 再次做错
- `复发次数`: number

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
