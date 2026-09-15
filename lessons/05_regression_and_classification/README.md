# Lesson 05 — Regression and Classification

## Why this matters

Supervised learning maps labeled examples to numeric or categorical predictions.

## Learning outcomes

- Explain and apply linear and logistic regression.
- Explain and apply decision boundaries.
- Explain and apply precision, recall, F1, and ROC concepts.
- Explain and apply splits, leakage, and baselines.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Linear and logistic regression** — identify its inputs, outputs, assumptions, and role.
2. **Decision boundaries** — identify its inputs, outputs, assumptions, and role.
3. **Precision, recall, f1, and roc concepts** — identify its inputs, outputs, assumptions, and role.
4. **Splits, leakage, and baselines** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/05_regression_and_classification/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Move the classification threshold from 0.2 to 0.8 and chart precision and recall.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Accuracy hides failure on imbalanced data and leakage makes validation fiction.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Create an imbalanced dataset and choose a threshold for a stated business cost matrix.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why is a probability threshold a product decision?
2. What distinguishes a feature from a label?
3. When is accuracy unsafe?

## Connection to modern AI

Routing, moderation, fraud, and ranking frequently remain classical classification problems.

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
