# Project A — Classical ML Benchmark

## Mission

Build a defensible binary-classification benchmark on a public tabular dataset. The goal is not the highest score; it is a reproducible decision.

## Required work

1. Write the prediction target and business cost of each error.
2. Create train, validation, and untouched test splits.
3. Establish a majority-class and simple-rule baseline.
4. Train logistic regression, a decision tree, and one ensemble.
5. Compare precision, recall, F1, calibration, and the business-cost metric.
6. Inspect errors by at least three meaningful data slices.
7. Record leakage checks and seed/version information.

## Deliverables

- reproducible training script;
- metric table and confusion matrices;
- threshold-selection analysis;
- model card describing intended and prohibited use;
- two-page decision memo.

## Acceptance

- one command reproduces results;
- the test set influences no training or threshold decision;
- conclusions acknowledge uncertainty and slice failures;
- a simple baseline is reported beside every candidate.
