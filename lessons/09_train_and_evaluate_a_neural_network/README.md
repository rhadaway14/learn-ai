# Lesson 09 — Train and Evaluate a Neural Network

## Why this matters

A model matters only when performance survives unseen data and reproducible evaluation.

## Learning outcomes

- Explain and apply dataset and batch loading.
- Explain and apply training and validation loops.
- Explain and apply checkpoints and deterministic seeds.
- Explain and apply confusion matrices and error analysis.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Dataset and batch loading** — identify its inputs, outputs, assumptions, and role.
2. **Training and validation loops** — identify its inputs, outputs, assumptions, and role.
3. **Checkpoints and deterministic seeds** — identify its inputs, outputs, assumptions, and role.
4. **Confusion matrices and error analysis** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/09_train_and_evaluate_a_neural_network/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Train XOR with three seeds and compare convergence.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

A single lucky seed or aggregate metric can conceal brittle behavior.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Add early stopping based only on validation loss and preserve the best checkpoint.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why separate validation and test data?
2. What makes training reproducible?
3. What should a checkpoint contain?

## Connection to modern AI

Fine-tuning and foundation-model evaluation use the same separation of optimization and measurement.

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
