# Lesson 06 — Neural Network Anatomy

## Why this matters

Neural networks compose learned affine transformations with nonlinear functions.

## Learning outcomes

- Explain and apply neurons and dense layers.
- Explain and apply ReLU, sigmoid, and tanh.
- Explain and apply depth, width, and capacity.
- Explain and apply tensor-shape tracing.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Neurons and dense layers** — identify its inputs, outputs, assumptions, and role.
2. **Relu, sigmoid, and tanh** — identify its inputs, outputs, assumptions, and role.
3. **Depth, width, and capacity** — identify its inputs, outputs, assumptions, and role.
4. **Tensor-shape tracing** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/06_neural_network_anatomy/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Replace ReLU with sigmoid and tanh and compare activation distributions.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Without nonlinear activations stacked linear layers collapse into one linear transformation.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Trace a batch of shape 32 by 10 through layers 10 to 64 to 16 to 3 including every weight and bias shape.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. What does a neuron calculate?
2. Why do networks need nonlinearities?
3. What does model capacity mean?

## Connection to modern AI

Transformer projections and feed-forward blocks are learned neural layers.

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
