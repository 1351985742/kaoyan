# Local Source Library

Use these student-owned local materials as the primary taxonomy and practice source.

## Roots

Verified on this Windows workspace on 2026-10-22:

- Lecture notes: `D:\personal\kaoyan\讲义`
- Obsidian question bank: `D:\personal\kaoyan\Obsidian题库`
- Lecture index: `D:\personal\kaoyan\讲义\INDEX.md`
- Question-bank category tree: `D:\personal\kaoyan\Obsidian题库\_meta\categories.json`
- Question-bank manifest: `D:\personal\kaoyan\Obsidian题库\_meta\manifest.json`

The search script resolves both roots itself: `KYS_LECTURE_ROOT` / `KYS_BANK_ROOT` when set, otherwise it walks up from the script location looking for `讲义` and `Obsidian题库`. Only override the paths here if the library actually moves.

The question bank is organized by category directories. Each Markdown booklet contains question text, options, question ID, source, category, and a collapsed answer block. Treat the category path as the student's working exam taxonomy.

The lecture library contains duplicated `book.md` files and split `chapters/*.md` files. Search and read chapter files first to avoid duplicate hits and oversized reads.

### Filename normalization

Local directory and file names keep LaTeX wrappers (`$f(x)$`) and full-width backslash escapes (`＼＼mathbf`), while Notion progress titles dropped the same characters. Match a Notion title to a local file by replacing `\` and `＼` with `/`, removing `$`, and collapsing spaces around `/`. Without that normalization most titles look missing even though the file exists.

Numbering drifts too: the local tree currently uses `02 一元微分/01 导数与微分概念`, `02 导数与微分计算`, `03 微分中值定理`, `04 导数应用`, while the pre-populated Notion rows still say `01 导数概念`, `02 导数计算`, `03 导数应用`, `04 微分中值定理` with a deeper `极最拐` level. Do not assume a Notion path resolves to a local file; verify before citing a source.

## Search Tool

Run:

```powershell
python D:\personal\kaoyan\.agents\skills\kaoyan-math-coach\scripts\search_local_sources.py TERM [TERM ...] --scope all --limit 12 [--chapter "章节或分类提示"]
```

Python is `C:\Python314\python.exe`. The console renders Chinese output as mojibake under some code pages; judge the result from the matched paths and pass criteria rather than the terminal glyphs.

Use `--scope bank` for question-bank retrieval and `--scope lecture` for theorem explanations. Terms are AND-preferred but partial matches remain visible when evidence is sparse. `--chapter` boosts files whose paths or contents match the supplied chapter/category; it is deliberately not a hard filter because lecture chapters and question-bank categories may use different names.

## Three Entry Routes

Choose the route from the information actually supplied. A question number is never required.

### Chapter or category supplied

1. Solve or structurally inspect the problem before searching.
2. Infer one to three candidate core propositions.
3. Search two to four normalized concept terms with `--chapter` in `lecture` scope.
4. Search the core term and one variation term with the same chapter hint in `bank` scope.
5. Check the named chapter first, then its nearest prerequisite or sibling category when the mathematics crosses a boundary.

### Problem supplied without chapter

1. Infer candidate propositions from the task, conditions, structural signals, options, and the student's route.
2. Search those concepts in `lecture` and `bank` scope.
3. Use a distinctive phrase afterward when identifying the exact original question would add source, ID, or category metadata.
4. If the exact question is not found, continue with the closest well-supported concept node.

### Question ID or distinctive wording supplied

1. Directly locate the question and capture its ID, source, and category.
2. Independently verify the mathematical classification.
3. Search the core concept in the lecture notes and combine it with one adjacent property in the bank to find variants.

## Classification and Confidence

- **已定位原题**: the question ID or sufficiently distinctive wording matches the complete problem.
- **高置信考点**: mathematical analysis, lecture material, and question-bank taxonomy support the same core proposition, although the original question was not found.
- **候选考点**: more than one classification remains plausible or only partial source evidence is available.
- If the supplied chapter and the inferred proposition disagree, do not force the problem into the chapter. State whether it is a cross-chapter application, a neighboring prerequisite, or an uncertain classification.
- Build the knowledge mesh from the verified core proposition, not from the filename of the first search hit.

## Retrieval Discipline

- Do not modify the source library unless the user explicitly asks.
- Do not assume an image question is the original bank item until exact or near-exact wording is found; this does not prevent concept-level retrieval.
- If the same question appears in multiple category files, use that duplication as evidence of a cross-category connection, but avoid double-counting it as two separate variants.
- Prefer true exam questions and the student's marked重点 entries when choosing a transfer problem.
- Validate formulas and conclusions independently. Source membership is evidence of taxonomy, not proof of correctness.
- If a root is unavailable, report that briefly and continue from the accessible source.
