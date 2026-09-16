# Lesson 05 Reference Notes — Regression and Classification

Review these notes after attempting the exercises. They show the reasoning standard, not the only acceptable wording.

## Exercise 1

- Engineer-hours and request volume are regression because their targets are numeric amounts.
- Late/on-time and routing destination are classification because their targets are categories.
- Strong answers define a real prediction moment and action. “Predict risk” without a horizon or action remains underspecified.

## Exercise 2

- Planned source-system count and contracted deadline are valid if recorded accurately at approval.
- Final delay reason and completed-project satisfaction are future information and therefore leakage.
- An engineer assigned after kickoff is unavailable at approval unless the prediction moment changes.
- Prior project count can be valid if computed only from history available at approval.
- An undocumented risk score needs lineage, timing, and construction review. It may contain the target or future information.

## Exercise 3

| Project | Residual | Absolute error | Squared error |
|---|---:|---:|---:|
| A | −10 | 10 | 100 |
| B | +30 | 30 | 900 |
| C | −40 | 40 | 1,600 |
| D | +20 | 20 | 400 |

MAE is $(10+30+40+20)\div4=25$ hours. RMSE is $\sqrt{(100+900+1600+400)\div4}=\sqrt{750}\approx27.39$ hours. RMSE is larger because squaring gives the 40-hour miss extra influence. The model beats the stated 85-hour baseline MAE on this sample, but the evaluation still needs uncertainty, slices, and production-realistic data.

## Exercise 4

- Accuracy: $(18+74)\div100=92\%$.
- Precision: $18\div(18+6)=75\%$.
- Recall: $18\div(18+2)=90\%$.
- Specificity: $74\div(74+6)=92.5\%$.
- F1: $2\times(.75\times.90)\div(.75+.90)\approx81.8\%$.

Precision describes how trustworthy an escalation is. Recall describes how many late projects are caught. Specificity describes how reliably on-time projects avoid escalation.

## Exercise 5

Scenario A, with FP cost 2 and FN cost 15:

- 0.30: $20\times2+1\times15=55$.
- 0.50: $6\times2+2\times15=42$.
- 0.70: $2\times2+7\times15=109$.

Choose 0.50 among these candidates.

Scenario B, with FP cost 8 and FN cost 5:

- 0.30: $20\times8+1\times5=165$.
- 0.50: $6\times8+2\times5=58$.
- 0.70: $2\times8+7\times5=51$.

Choose 0.70 among these candidates. Review capacity, calibration, subgroup effects, uncertain costs, benefits of true decisions, and safety constraints are examples of omitted considerations.

## Exercise 6

Accuracy is $9{,}950\div10{,}000=99.5\%$. Fraud recall is $0\div50=0\%$. The classifier reproduces the majority class and detects no fraud. Report the confusion matrix, recall, precision at useful operating points, precision–recall behavior, and expected cost. A ranking or rule-based current process may also be a meaningful operational baseline.

## Exercise 7

1. Use a chronological split: earlier projects for training and later projects for validation/test.
2. Group by device so records from one device cannot cross partitions; preserve time order where future failure is predicted.
3. A stratified random split may be reasonable if images are independent, while grouping near-duplicates and preserving rare defects.
4. Group by customer and split chronologically so one customer's adjacent snapshots cannot leak across partitions.

## Exercise 8

The plan has at least four problems:

- Project records cross splits: entity leakage. Group entire projects.
- Full-dataset imputation: preprocessing leakage. Fit averages on training data only.
- Final closure reason: target or temporal leakage. Remove it from intake-time features.
- Threshold selected on the test set: test-set leakage. Select on validation data, freeze the design, then evaluate once on test.

The reported test result is optimistic because test information influenced model development.

## Gate A quality bar

A strong artifact:

- defines targets precisely enough that labels can be collected consistently;
- distinguishes model scores from product decisions;
- proves every feature exists at prediction time;
- includes naive baselines before model complexity;
- ties metrics and thresholds to explicit error consequences;
- uses split boundaries that prevent time and entity leakage;
- includes base-rate, calibration, uncertainty, and subgroup checks;
- states evaluation limitations; and
- makes keep, revise, or reject criteria testable.

The artifact is a contract for later implementation. Future lessons may replace the model family, but they should not silently change the target, evaluation population, or success criteria.
