# Lesson 21 — Agents, Loops, State, and Memory

## Why this matters

An agent is a bounded execution loop where a model selects actions from observations and state.

## Learning outcomes

- Explain and apply observe-decide-act loops.
- Explain and apply state machines.
- Explain and apply short and long-term memory.
- Explain and apply budgets, termination, and approvals.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Observe-decide-act loops** — identify its inputs, outputs, assumptions, and role.
2. **State machines** — identify its inputs, outputs, assumptions, and role.
3. **Short and long-term memory** — identify its inputs, outputs, assumptions, and role.
4. **Budgets, termination, and approvals** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/21_agents_loops_state_and_memory/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Remove the step limit from a cyclic policy and observe the failure.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Unbounded loops amplify cost, latency, side effects, and error accumulation.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Model an agent as explicit states and legal transitions including failed and awaiting-approval states.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What makes an agent different from a chatbot?
2. Why externalize state?
3. When is human approval required?

## Connection to modern AI

Agent frameworks package loops and state but do not remove control design.

## Explain it at two levels

- **Plain language:** explain the purpose without equations or framework names.
- **Technical:** explain the mechanism, shapes or state, assumptions, metric, and failure mode.

## Definition of done

- [ ] Lab executed and output understood
- [ ] Primary experiment recorded
- [ ] Exercise completed before reviewing the solution
- [ ] Failure mode reproduced or analyzed
- [ ] Checkpoint answered in your own words
- [ ] Plain-language and technical explanations written
