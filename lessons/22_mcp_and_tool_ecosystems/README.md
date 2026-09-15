# Lesson 22 — MCP and Tool Ecosystems

## Why this matters

MCP standardizes how AI clients discover tools, resources, and prompts exposed by servers.

## Learning outcomes

- Explain and apply clients, servers, and transports.
- Explain and apply tools versus resources.
- Explain and apply JSON-RPC-shaped messages.
- Explain and apply authorization and trust boundaries.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Clients, servers, and transports** — identify its inputs, outputs, assumptions, and role.
2. **Tools versus resources** — identify its inputs, outputs, assumptions, and role.
3. **Json-rpc-shaped messages** — identify its inputs, outputs, assumptions, and role.
4. **Authorization and trust boundaries** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/22_mcp_and_tool_ecosystems/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Trace a call from discovery through validation, execution, and result handling.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Protocol compatibility does not imply a server or returned content is trustworthy.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Design a server exposing one read-only resource and one bounded tool.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What does MCP standardize?
2. How do tools differ from resources?
3. Where should authorization occur?

## Connection to modern AI

MCP makes integrations portable across compatible AI applications.

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
