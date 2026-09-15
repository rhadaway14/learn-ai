# Lesson 30 — Distributed AI

## Why this matters

Large models and datasets require work and state partitioned across devices.

## Learning outcomes

- Explain and apply data parallelism.
- Explain and apply tensor and pipeline parallelism.
- Explain and apply FSDP and ZeRO concepts.
- Explain and apply collectives, synchronization, and failure.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Data parallelism** — identify its inputs, outputs, assumptions, and role.
2. **Tensor and pipeline parallelism** — identify its inputs, outputs, assumptions, and role.
3. **Fsdp and zero concepts** — identify its inputs, outputs, assumptions, and role.
4. **Collectives, synchronization, and failure** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/30_distributed_ai/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Average simulated gradients from uneven worker batches and identify the weighting bug.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Naively averaging worker means is wrong when workers process different sample counts.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Compare data, tensor, and pipeline parallelism for a model that fits nowhere on one GPU.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What does all-reduce do?
2. Why shard optimizer state?
3. What is a pipeline bubble?

## Connection to modern AI

Frontier training and high-throughput serving are distributed-systems problems.

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
