# Project A — Classical ML Benchmark

> **Sequence note:** First complete the [browser-first Phase 1 Model Investigation Workbench](phase1/index.html). It assesses the Lessons 1–5 reasoning without requiring programming. This document is the optional implementation extension to begin after Engineering Lab A introduces the coding workflow.

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
