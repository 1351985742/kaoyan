# Interaction and Review Protocol

Use this reference for hinting, simulation, transfer design, and periodic review.

## Hint Mode

Give only the next necessary hint.

1. **Target hint**: Ask what property or quantity the question actually requests.
2. **Signal hint**: Point to one overlooked condition or option feature.
3. **Action hint**: Suggest an operation without carrying it out.
4. **Key-step hint**: Show the decisive transformation, leaving completion to the student.
5. **Full solution**: Give only after the student requests it or remains blocked after appropriate hints.

After each hint, wait for the student's next attempt. Do not bundle several levels into one message.

## Simulation Mode

- Do not reveal correctness before the student commits to an answer.
- Ask for the selected result, one-line reason, elapsed time, and confidence.
- Evaluate both mathematical correctness and decision quality.
- Penalize an unjustified guess differently from a correct, efficient route.
- After the attempt, switch to the normal diagnosis workflow.

## Review Mode

Use the student's original language as evidence. The review should answer:

1. Was the initial trigger mathematically relevant?
2. Was it the highest-priority trigger for this task?
3. At what earliest point should the student have noticed route cost or contradiction?
4. What exact action should replace the old automatic response?
5. How will independent transfer be tested?

## Design Transfer Questions

Change one structural feature at a time:

- Keep the method but change notation or surface form to test recognition.
- Remove one key condition to test whether the student understands necessity.
- Change the question type or options to test strategy adaptation.
- Add a decoy trigger to test method ranking.

Do not make the transfer problem much harder merely to appear rigorous.

## Mastery States

- `待复盘`: no complete diagnosis yet.
- `已纠偏`: explanation is understood and a trigger rule exists.
- `待二刷`: a delayed attempt is scheduled or due.
- `已掌握`: the student independently solves the original structure and one small variation.

Use `二刷结果` values consistently:

- `未二刷`
- `独立做出`
- `提示后做出`
- `再次做错`

If the same pattern recurs, increment `复发次数` and consider a focused drill set.

## Periodic Review Output

Every five problems, produce:

- Top repeated diagnosis with evidence from problem records.
- Most frequently missed signal.
- Most expensive automatic method.
- One improvement that has already appeared.
- One focused drill for the next block of five problems.

Weekly, classify training time into:

- Concept repair
- Signal recognition
- Method ranking
- Execution accuracy
- Timed decision practice

Do not infer trends from one isolated problem. Label tentative patterns as tentative.
