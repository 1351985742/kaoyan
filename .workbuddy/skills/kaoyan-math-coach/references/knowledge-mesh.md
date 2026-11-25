# Knowledge Mesh Protocol

Use this reference after solving and diagnosing a normal review problem. Build a small navigable network, not a chapter summary.

## Trace Back One Layer

Identify four levels without expanding beyond the nearest useful neighborhood:

1. **Problem surface**: the notation, story, or option arrangement seen in this problem.
2. **Core proposition**: the single theorem, equivalence, invariant, or decision rule that closes the problem.
3. **Variant controls**: assumptions or targets an item writer can change while testing the same proposition.
4. **Adjacent nodes**: the closest prerequisite, sibling property, downstream application, or common trap.

The core proposition must be more precise than a chapter label. Prefer `周期函数的变限积分周期判据` over `定积分`, and `秩与齐次方程基础解系维数` over `线性方程组`.

## Use Typed Edges

Label why a neighboring node is connected:

- `前置`: needed to derive or recognize the core proposition.
- `同核变式`: same proposition with a changed condition, target, representation, or direction.
- `下游`: an application that uses the proposition as a step.
- `易混`: a nearby statement whose conditions or conclusion are often confused.
- `跨章`: a genuine connection to another chapter, used only when it frequently appears in questions.

Do not connect two topics merely because they appear in the same chapter.

## Generate Item-Writer Variants

Turn the following knobs and keep the mathematical core fixed:

1. **Change the target**: value, parity, periodicity, monotonicity, boundedness, convergence, rank, probability, or parameter range.
2. **Change the condition**: add/remove symmetry, mean-zero, independence, invertibility, differentiability, or boundary assumptions.
3. **Change the representation**: explicit formula, variable-limit integral, recurrence, matrix equation, distribution function, or geometric language.
4. **Reverse the logic**: sufficient condition, necessary condition, equivalence, counterexample, or number-of-correct-statements.
5. **Add a decoy**: include a familiar local trigger that is valid but lower priority than the core structure.

Prefer variants already present in the local question bank. Mention their category or question ID when useful. Create a new variation only when the bank lacks the needed branch.

## Control Depth

- **Standard review**: four through eight nodes, two or three variants, and two or three adjacent nodes. Keep the mesh to roughly six through twelve short lines.
- **Expanded mesh**: six through twelve nodes only when the student explicitly asks to expand, connect a chapter, or review a recurring pattern.
- **Answer-only turn**: omit the mesh entirely.

Do not use source quantity as a reason to enlarge the mesh. Select the highest-yield connections for this student's current error.

## Output Shape

Default to a compact indented map:

```text
本题表面
└─ 核心考点：精确命题
   ├─ 前置：节点 → 为什么需要
   ├─ 同核变式：节点 → 命题人改了哪个旋钮
   ├─ 下游：节点 → 如何调用核心命题
   └─ 易混：节点 → 条件或结论差在哪里
```

Add a separate `还能怎么出` list with two to four high-value variants. Do not repeat the full solution inside the mesh.

Use Mermaid only when the user explicitly asks to draw the network or when more than five typed edges would be materially clearer as a graph. Even then, keep node labels short and do not restate the full derivation inside nodes.

## Quality Checks

- Can the student state the core proposition without the original notation?
- Does every edge have a mathematical reason?
- Are the variants genuinely different item forms rather than cosmetic number changes?
- Is at least one adjacent node a likely confusion or prerequisite?
- Does the mesh remain readable in under one minute?
- Are local-source matches distinguished from inferred connections?
