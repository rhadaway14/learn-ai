# Lesson 04 — Probability and Statistics for ML

## Why this matters

Models quantify patterns under uncertainty rather than deterministic truth.

## Learning outcomes

- Explain and apply random variables and distributions.
- Explain and apply expectation, variance, and sampling.
- Explain and apply conditional probability and Bayes rule.
- Explain and apply confidence intervals and calibration.

## Mental model

Keep asking what each value represents, where state lives, what is trusted, and how success is measured. Write down inputs, outputs, assumptions, and failure modes before using a framework that hides them.

## Core concepts

1. **Random variables and distributions** — identify its inputs, outputs, assumptions, and role.
2. **Expectation, variance, and sampling** — identify its inputs, outputs, assumptions, and role.
3. **Conditional probability and bayes rule** — identify its inputs, outputs, assumptions, and role.
4. **Confidence intervals and calibration** — identify its inputs, outputs, assumptions, and role.

## Guided lab

From the repository root:

~~~bash
python lessons/04_probability_and_statistics_for_ml/lab.py
~~~

The lab prints structured JSON so results can be inspected, diffed, and tested. Read the code, predict its output, run it, and explain differences from your prediction.

## Primary experiment

Change sample size from 20 to 10000 and compare bootstrap interval width.

Record your hypothesis, independent variable, controlled variables, observation, and explanation in PROGRESS.md.

## Important failure mode

Small or biased samples can produce precise-looking but misleading estimates.

Reproduce the failure safely and identify what telemetry or test would expose it.

## Exercise

Simulate a rare-event diagnostic test and calculate how prevalence changes the posterior.

Use [EXERCISES.md](EXERCISES.md) as the worksheet. Check [SOLUTIONS.md](SOLUTIONS.md) only after completing an attempt.

## Knowledge checkpoint

1. Why is correlation not causation?
2. What does a 95 percent confidence interval mean?
3. Why does the base rate matter?

## Connection to modern AI

Generation, classification confidence, evaluation, and sampling all depend on probability.

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
