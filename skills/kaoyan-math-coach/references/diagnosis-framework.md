# Diagnosis Framework

Use this reference when diagnosing a student's mistake or choosing a corrective exercise.

## Diagnose by Evidence

| Layer | Observable evidence | Corrective action | Verification |
| --- | --- | --- | --- |
| Knowledge gap | Cannot state or correctly use a definition, theorem, condition, or formula | Repair the smallest missing concept and contrast its boundary conditions | One direct concept check plus one standard problem |
| Structural recognition | Knows the relevant fact after being told but did not notice the signal in the problem | Build a signal-to-action cue and compare near-looking structures | Identify the route from several unsolved stems without calculating |
| Method ranking | Notices multiple valid methods but automatically chooses the familiar, longer, or riskier one | Compare route cost, target distance, and stop-loss points | Solve a similar multiple-choice problem under a route-selection time limit |
| Execution | Chooses the right route but makes algebra, calculus, logic, or notation errors | Isolate the failing operation and add a local check | Repeat the operation in a fresh but equivalent setting |
| Time control | Continues after the route has become unproductive, or performs unnecessary derivation | Define observable warning signs and a backup route | Timed retry with explicit switch decision |

Do not diagnose "carelessness" unless the error is genuinely random across repeated attempts. Repeated carelessness usually indicates a missing checking procedure or unstable execution.

## Classify the Student's Route

Use exactly one primary verdict and explain it:

- **Invalid route**: a condition is violated or an inference is false.
- **Valid but low-priority route**: it can solve the problem, but has higher computation, case, proof, or time cost than a visible structural route.
- **Good route, incomplete execution**: the entry is appropriate; the failure occurs later.
- **Optimal route**: the route matches the target and uses the strongest available structure.

This distinction is essential. A familiar trigger can correctly suggest a method without making that method the best first choice.

## Rank Signals Before Calculating

Use this as a heuristic, not an inflexible theorem:

1. What the question and options ask.
2. Domain restrictions and logical quantifiers such as "任意", "存在", "一定", and "可能".
3. Global structure: symmetry, parity, periodicity, invariance, linearity, orthogonality, rank, independence, or named distributions.
4. Relations among quantities: derivative sign, convexity, bounds, eigenvalue/trace/determinant relations, expectation/variance relations.
5. Local operation triggers: absolute values, radicals, denominators, nested functions, or familiar formulas.

When a local trigger conflicts with a stronger global signal, test the global structure first.

## Adjust for Question Type

### Multiple Choice

- Use options as constraints and possible counterexample targets.
- Check whether all allowed boundary or degenerate objects make two options simultaneously true; common checks include the zero function, zero vector, singular matrix, and parameter endpoints.
- Prefer property checks, symmetry, special values, exclusion, and necessity/sufficiency analysis when they close the problem faster.
- Do not derive a full explicit expression unless the options require it.

### Fill in the Blank

- Aim for a controlled computation with quick domain and sign checks.
- Avoid option-dependent shortcuts because no options are available to catch errors.

### Full Solution

- Preserve logical conditions and write the theorem or transformation that justifies each non-obvious step.
- Separate scratch-paper discovery from the final answer structure.

## Set Stop-Loss Rules

A stop-loss rule must be observable. Good forms include:

- "性质题先做 20 秒结构检查；若无法建立目标关系，再展开计算。"
- "选择题推导超过两层且仍未接近选项，回看选项并尝试特值或排除。"
- "分情况超过三支时，检查是否漏掉对称、单调或统一表示。"

Adjust time thresholds by difficulty and question type; do not present 20 seconds as a universal law.

## Write Trigger Sentences

Bad: "以后灵活一点。"

Good: "看到对称区间 + 奇偶条件 + 性质选项，先写目标函数在 $-x$ 处的表达式；若结构换元无结果，再拆区间或求导。"

A trigger sentence must contain a visible cue, first action, and optional fallback.
