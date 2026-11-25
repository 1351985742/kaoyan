# Section Learning Cycle

Use this workflow whenever the student begins, practices, or closes a named question-bank section. Its purpose is to make a section a reusable method system rather than a completed queue of questions.

## Core Model

Organize every section around an entry-to-path mapping:

$$
S_0
\longrightarrow
\text{目标 }G
\longrightarrow
\text{强信号}
\longrightarrow
\text{候选工具}
\longrightarrow
\text{第一操作}
\longrightarrow
\text{中间状态}
\longrightarrow
\text{落地点}.
$$

Here '入口' is the visible signal and '路径' is the ordered state transformation it activates. They are recorded as one mapping pair, not as two unrelated tags. The final theorem, definition, counterexample, or direct computation that settles the requested claim is the '落地点'; substitution, logarithm, differentiation, and variable change are bridges or tools, not landing points.

Call the final theorem, definition, counterexample, or direct computation that settles the requested claim the **landing point**. Distinguish it from bridges such as a substitution, logarithm, differentiation, or variable change.

Examples of landing points include monotone boundedness, squeezing, a unique root, continuity of an inverse on the relevant range, a subsequence contradiction, a divergence comparison, a direct limit law, and a counterexample to a universal statement.

## Section States

- `未启动`: no start card or representative attempt.
- `在刷`: questions are being attempted and individually recorded as needed.
- `已覆盖`: the full planned set has been seen and a closeout map exists.
- `待二刷`: representative delayed retrieval is due.
- `已闭环`: the student independently solves representative originals and one changed-surface variation after delay.

Do not call a section mastered merely because all questions have been viewed or explained.

## Before Practice: Section Start Card

When the student supplies a chapter, heading, or category path:

1. Locate the exact question-bank booklet and nearest lecture sections.
2. Count questions and cluster them by mathematical decision and entry-to-path mapping, not by superficial notation or by the name of a tool.
3. State one governing question for the section. Example: for convergence/divergence, "What information can lock the tail behavior into one conclusion?"
4. For each main path, write 'S_0', target 'G', strongest signal, candidate tools, first operation, expected intermediate state, and landing point.
5. Name one or two likely decoy triggers and the boundary conditions that invalidate a tempting route.
6. Label the question-bank order as '锚点题', '变式题', and '同构题': anchors establish independent recognition, variants change one control while preserving the path, and isomorphic items change the surface while preserving the same proposition and path.
7. Propose the practice order: recognition anchors first, then necessary variants, then isomorphic confirmation and mixed/deceptive variants.
8. Do not add an independent '校验方式' field to the start card unless the student explicitly requests it; later transfer and delayed retrieval are separate closeout actions.
7. Ask the student to begin with a representative question; do not solve every example in the start card.

Keep this card to one screen unless the student requests an expanded map.

## During Practice: Problem Blocks

Use blocks of roughly three to five questions, adjusted for difficulty and fatigue.

For each substantive question:

1. If the student supplied a real attempt, preserve the first trigger, route, stopping point, time, confidence, and feeling before diagnosing. If the student says they have no idea, construct a route and mark the diagnosis provisional.
2. Identify the intended landing point before giving computations.
3. Explain the route as 'S_0 -> G -> signal -> first operation -> intermediate state -> landing point -> conclusion'.
4. Compare it to the student's route; classify it as invalid, valid but low-priority, good but incompletely executed, or optimal.
5. Create or update the normal one-problem Notion record unless the student explicitly requests answer-only, no-record, hint, or simulation mode.
6. Add a one-sentence trigger rule that can be reused inside the current section. The rule must identify the visible entrance and the first path operation.

At the end of each block, give only:

- landing points encountered;
- one recurring missed signal or unstable operation;
- the next block's focus.

Avoid a large chapter summary after every question.

## Stop-Loss Rules

Use observable route checks rather than rigid universal time limits.

- If the student cannot name a plausible landing point after inspecting the conditions and options, pause calculation and identify the required conclusion first.
- If two transformations have not created a relation to a known theorem, definition, or option, reset and choose a different control quantity.
- If a reverse implication is being used, explicitly test information loss: non-injectivity, a boundary escape, a missing bound, cancellation, or a degenerate case.
- If a universal option cannot be derived quickly, test it with the smallest relevant counterexample family: constant nonzero root, alternating sequence, escape to infinity, or a simple polynomial/exponential model.

## After Practice: Section Closeout

Run this when the student declares a section finished, not merely after the final question appears.

1. Produce a compact landing-point map: each landing point, its signals, representative question IDs, and its nearest trap.
2. Separate outcomes into `stable`, `understood but not retrieved`, and `recurring risk`.
3. Select two to four representative redo problems. Choose by structural coverage and prior error evidence, not by perceived difficulty alone.
4. Assign retrieval:
   - Day 3: identify the landing point and first operation from an unseen or lightly changed stem.
   - Day 7: solve two representative problems without hints.
   - Day 14: solve one cross-section variation that changes the surface but preserves the landing point.
5. State the section status as `已覆盖` or `待二刷`. Use `已闭环` only after the delayed retrieval succeeds.

Only after this closeout map is complete should the delayed method network be updated. Create or update exactly one card for the whole section. Put the section's multiple methods, landing points, traps, and representative evidence into subsections of that card. The card uses only its title, a `位置` with the highest subject level removed and at most three remaining directory levels, and `掌握情况` as operational indexes; put the map's actual method content in the card body.

Then update the question-count progress tracker. The smallest-section row was pre-established from the local file's `题量`; set `已完成题数` to the file's full `题目总数` only after this closeout. Recalculate the containing large chapter, subject, and overall rows from their leaf rows. This is a question-count report, so do not use the number of reviewed records or method cards as a substitute.

When the ongoing Notion workflow is available, create one compact Section Closeout page under the hub at this stage. Keep individual solutions in their existing database records; the closeout page should contain only the map, representative redo list, and retrieval status.

## Default Interaction Contract

- A section path or heading is sufficient input to start.
- The student may interrupt the cycle with a single problem, "只提示", "只要答案", "不沉淀", or a request for a broader map; follow the newest instruction immediately.
- Do not demand a daily plan from the student. Maintain the next useful action from the current section state.
- Use the local question-bank taxonomy for names and counts, but build the map from mathematical structure rather than folders alone.
