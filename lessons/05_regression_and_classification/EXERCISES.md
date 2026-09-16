# Lesson 05 Exercises — Regression and Classification

Complete these exercises after the [interactive lesson](index.html). No programming is required.

## Exercise 1 — Frame the prediction

For each request, identify the unit of prediction, target, task type, prediction moment, horizon, and action.

| Request | Unit | Exact target | Regression or classification? | Prediction moment | Horizon | Resulting action |
|---|---|---|---|---|---|---|
| Estimate migration engineer-hours | | | | | | |
| Predict whether a project will miss its committed date | | | | | | |
| Route a new support request | | | | | | |
| Forecast next week's API request volume | | | | | | |

Rewrite any request that is too vague to evaluate.

## Exercise 2 — Feature or leakage?

The delivery advisor predicts lateness when a project is approved. Classify each field and explain the timing.

| Field | Valid feature, invalid, or needs investigation? | Reason |
|---|---|---|
| Planned source-system count | | |
| Contracted deadline | | |
| Final delay-reason code | | |
| Engineer assigned two weeks after kickoff | | |
| Customer's completed-project satisfaction score | | |
| Prior project count known at approval | | |
| A field named `risk_score` from an undocumented system | | |

For every “needs investigation” answer, write the question you would ask the data owner.

## Exercise 3 — Regression evaluation

An effort model produces these held-out predictions:

| Project | Actual hours | Predicted hours | Residual | Absolute error | Squared error |
|---|---:|---:|---:|---:|---:|
| A | 100 | 110 | | | |
| B | 200 | 170 | | | |
| C | 300 | 340 | | | |
| D | 400 | 380 | | | |

1. Complete the table using `residual = actual − predicted`.
2. Calculate MAE.
3. Calculate RMSE.
4. Explain why RMSE is larger than MAE here.
5. The mean baseline has MAE 85 hours. Has the model beaten it on this sample?
6. Which individual error should receive operational review first, and why?

## Exercise 4 — Confusion matrix and metrics

At its proposed threshold, a late-project classifier produces:

- 18 true positives;
- 6 false positives;
- 2 false negatives; and
- 74 true negatives.

Calculate:

| Metric | Your calculation | Result |
|---|---|---:|
| Accuracy | | |
| Precision | | |
| Recall | | |
| Specificity | | |
| F1 | | |

Then explain each metric in one sentence without using its formula.

## Exercise 5 — Choose an operating point

Three validation thresholds produce:

| Threshold | TP | FP | FN | TN |
|---:|---:|---:|---:|---:|
| 0.30 | 19 | 20 | 1 | 60 |
| 0.50 | 18 | 6 | 2 | 74 |
| 0.70 | 13 | 2 | 7 | 78 |

Scenario A assigns a cost of 2 units to a false positive and 15 units to a false negative. Scenario B assigns 8 units to a false positive and 5 units to a false negative.

1. Calculate total error cost for every threshold in both scenarios.
2. Select a threshold for each scenario.
3. Explain why the preferred threshold changes even though the model scores do not.
4. Name two real considerations missing from this simple cost calculation.

## Exercise 6 — Accuracy trap

A fraud dataset contains 9,950 legitimate transactions and 50 fraudulent transactions. A classifier predicts every transaction as legitimate.

1. Calculate accuracy.
2. Calculate recall for fraud.
3. Explain why the model is not a useful detector.
4. Name a baseline that is more informative than accuracy alone.
5. Choose at least two metrics you would report and explain why.

## Exercise 7 — Design the split

For each situation, choose a split strategy and explain it.

1. Predict next quarter's delivery risk from five years of projects.
2. Predict device failure when every device sends thousands of records.
3. Classify independent product images with a rare defect class.
4. Predict customer churn when the same customer has monthly snapshots.

For each design, state what must remain grouped and what data should be later than the training period.

## Exercise 8 — Leakage review

Find every problem in this evaluation plan:

> The team randomly splits individual weekly project records. Records from the same project can appear in every split. Missing values are filled using averages calculated from the full dataset. The feature set includes the final closure reason. The team tries twelve thresholds and selects the one with the highest test F1. It reports the same test result as final performance.

For each problem, provide:

- the leakage type;
- why the reported result becomes optimistic; and
- a corrected design.

## Gate A capstone worksheet — Baseline decision model

### A. Decision contract

| Field | Regression task | Classification task |
|---|---|---|
| Unit of prediction | | |
| Target | | |
| Target units or classes | | |
| Prediction moment | | |
| Outcome horizon | | |
| Action supported | | |
| Primary user | | |

### B. Evidence contract

| Item | Your answer |
|---|---|
| Candidate prediction-time features | |
| Two rejected leaking fields | |
| Label source and known quality risks | |
| Target population | |
| Available evaluation sample | |
| Important base rate | |
| Important subgroup or slice | |

### C. Baseline and evaluation contract

| Item | Regression task | Classification task |
|---|---|---|
| Naive baseline | | |
| Primary metric | | |
| Supporting metrics | | |
| Costly failure example | | |
| Acceptable minimum improvement over baseline | | |
| Uncertainty to report | | |

### D. Split and operating contract

| Item | Your answer |
|---|---|
| Train period or groups | |
| Validation period or groups | |
| Test period or groups | |
| Duplicate/entity isolation rule | |
| Provisional classification threshold | |
| False-positive consequence and cost | |
| False-negative consequence and cost | |
| Review-capacity constraint | |
| Calibration check | |
| Evidence that would change the threshold | |

### E. Release decision

Define explicit rules for:

- **keep:** what evidence would justify using the model;
- **revise:** what failure would send it back for feature, data, or threshold work; and
- **reject:** what result would show that the model adds no defensible value over the baseline.

Finish with a short model-evaluation narrative that states the decision being supported, the population represented, performance against baseline, important uncertainty, costly failure behavior, and the next action.
