# Lesson 09 Reference Notes — Train and Evaluate a Neural Network

Review these notes only after completing your own attempt.

## 1. Prediction contract

A defensible example predicts one shipment's three-class delay outcome six hours before scheduled delivery. Features must exist at that moment. Actual delivery time, post-delivery corrections, and outcomes from later workflow stages are leakage.

The operational contract matters because it defines what evidence is eligible, what errors cost, and what population the evaluation claims to represent.

## 2. Split strategies

1. Use a customer group split so no customer appears in more than one partition.
2. Use a time split with the final period held out.
3. Use a patient group split so images from one patient remain together.
4. Use a geographic or domain holdout, ideally with time-aware evidence as well.
5. A random split may be reasonable after confirming independence and duplicate absence.

Each build should assert zero prohibited overlap in the relevant customer, patient, event, source, time, or content-duplicate identifiers.

## 3. Batch and epoch calculations

| Training examples | Batch size | Epochs | Batches per epoch | Total updates |
|---:|---:|---:|---:|---:|
| 1,000 | 50 | 5 | 20 | 100 |
| 1,025 | 50 | 5 | 21 | 105 |
| 12,000 | 128 | 20 | 94 | 1,880 |
| 750 | 1 | 3 | 750 | 2,250 |
| 750 | 750 | 3 | 1 | 3 |

Moving from 25 to 250 generally makes gradient estimates smoother and creates one tenth as many updates per epoch. It also uses more activation memory but may use parallel hardware more efficiently.

## 4. Correct aggregation

The incorrect equal batch average is:

> (0.40 + 0.50 + 0.90) ÷ 3 = 0.60

The example-weighted loss is:

> ((50 × 0.40) + (50 × 0.50) + (10 × 0.90)) ÷ 110 = 0.491

The small final batch should not receive the same weight as a batch containing five times as many examples. Accumulate total loss contribution and total example count, then divide once.

## 5. Curve diagnosis

1. Both decline: transferable learning is occurring; continue within the budget and monitor later separation.
2. Validation turns upward: likely overfitting; preserve the best checkpoint and inspect regularization or data coverage.
3. Both flat and high: check data, labels, gradients, loss compatibility, learning rate, features, and capacity.
4. Both oscillate: reduce learning rate and inspect scaling, anomalies, batch size, and gradient magnitude.
5. Immediate near-zero training loss: investigate leakage, duplicate targets, broken loss aggregation, trivial labels, or an excessively small dataset.
6. Validation consistently better: training-only regularization may explain it, but also inspect split difficulty, leakage, metric-mode differences, and aggregation.

Curves support hypotheses; they do not identify causes alone.

## 6. Early stopping

With minimum improvement 0.002, epoch 5 at 0.330 is the last clear qualifying best before the smaller changes. Epoch 7 at 0.329 does not beat 0.330 by more than 0.002. The exact equality policy must be documented; under a strict “more than” rule, patience expires at epoch 8 after epochs 6–8 fail to qualify. Restore epoch 5, not epoch 8.

Different systems may define the comparison as greater-than-or-equal. That choice can change the trace and belongs in the contract. The test set cannot drive stopping because stopping is model selection.

## 7. Confusion matrix

- total = 1,000;
- correct = 640 + 150 + 30 = 820;
- accuracy = 820 ÷ 1,000 = 82.0%;
- actual severe late = 12 + 28 + 30 = 70;
- severe-late recall = 30 ÷ 70 = 42.9%;
- predicted severe late = 15 + 25 + 30 = 70;
- severe-late precision = 30 ÷ 70 = 42.9%;
- missed actual severe late = 12 + 28 = 40;
- false severe-late alarms = 15 + 25 = 40.

The operating point should combine the cost of a missed severe delay, the cost and capacity of intervention, class prevalence, and the value of acting early. Limited capacity often calls for a precision constraint while maximizing recall within that capacity.

## 8. Seed evidence

Sorted results are 73%, 79%, 82%, 84%, and 86%.

- mean = 80.8%;
- median = 82%;
- minimum = 73%;
- maximum = 86%;
- range = 13 percentage points.

Reporting only 86% selects the luckiest run and exaggerates expected behavior. The 73% run could reflect an unfavorable initialization, unlucky batch order, optimization instability, or a fragile model-data combination.

Repeating one seed tests repeatability. Different predetermined seeds test sensitivity to random choices. Reproduction also requires data and split identity, configuration, preprocessing, code and dependencies, device details, model and optimizer state, and evaluation procedure.

## 9. Release-gate review

- **Workflow A: invalid final evidence.** The test set guided selection and became validation evidence. Freeze a process and evaluate against new untouched evidence.
- **Workflow B: structurally valid.** Selection, final testing, subgroup review, and repeated-run evidence have separate roles. Release still depends on predetermined business thresholds.
- **Workflow C: weak selection.** Newest does not mean best. Restore the best qualifying validation checkpoint and package its exact identity.

## 10. Capstone acceptance criteria

A strong protocol:

- defines the prediction moment before choosing features;
- prevents entity, time, duplicate, preprocessing, and decision leakage;
- calculates batches and updates explicitly;
- records training and validation curves with correct aggregation;
- specifies early stopping before observing final test results;
- preserves the best validation checkpoint separately from the latest checkpoint;
- evaluates class, subgroup, time-slice, and representative error behavior;
- reports a predetermined repeated-seed distribution;
- uses the sealed test set only after selection is frozen;
- links the approved release artifact to evidence, limits, monitoring, and rollback.

The artifact is ready for Lesson 10 when another engineer can tell exactly what was optimized, what selected the model, what supplied final evidence, and what would block release.
