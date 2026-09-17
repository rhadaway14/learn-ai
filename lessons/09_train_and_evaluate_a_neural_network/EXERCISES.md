# Lesson 09 Exercises — Train and Evaluate a Neural Network

Complete these exercises after the browser lesson. They require experiment design and interpretation, not programming.

## 1. Prediction contract

For the delivery-risk classifier, write a precise contract containing:

- one unit of prediction;
- the prediction moment;
- the three-class target;
- the prediction horizon;
- five features available at the prediction moment;
- three fields that would leak future information;
- the operational action triggered by a severe-late prediction;
- the costs of a false positive and false negative.

Explain why a model cannot be evaluated honestly until these items are fixed.

## 2. Split-strategy decisions

Choose random, group, time, geographic/domain, or a combination for each scenario. Explain the deployment claim being tested.

1. The same customer creates hundreds of shipments, and production will serve new customers.
2. The system trains on two years of data and will be deployed next month.
3. Medical images include several images from each patient.
4. A speech model trained in the United States will launch in Scotland.
5. Independent manufactured parts are photographed once under stable conditions.

For each, identify one overlap test that should fail the build if leakage is found.

## 3. Batch and epoch calculations

For each experiment, calculate batches per epoch and total optimizer updates. Round batches per epoch up when needed.

| Training examples | Batch size | Epochs | Batches per epoch | Total updates |
|---:|---:|---:|---:|---:|
| 1,000 | 50 | 5 | | |
| 1,025 | 50 | 5 | | |
| 12,000 | 128 | 20 | | |
| 750 | 1 | 3 | | |
| 750 | 750 | 3 | | |

Then explain one statistical and one systems consequence of moving from batch size 25 to batch size 250.

## 4. Correct aggregation

An epoch contains three batches:

| Batch | Examples | Average loss |
|---:|---:|---:|
| 1 | 50 | 0.40 |
| 2 | 50 | 0.50 |
| 3 | 10 | 0.90 |

1. Calculate the incorrect equal average of the three batch averages.
2. Calculate the correct example-weighted epoch loss.
3. Explain why the two results differ.
4. State what values an evaluator should accumulate to calculate the correct result.

## 5. Curve diagnosis

Diagnose each trace and propose the first two checks or responses.

1. Training and validation loss both decline steadily.
2. Training loss declines; validation loss declines and then rises.
3. Both losses remain high and almost flat.
4. Both losses oscillate sharply.
5. Training loss is extremely low from the first epoch, while validation is poor.
6. Validation is much better than training throughout.

Avoid treating the curve as proof. Name alternative causes that should be ruled out.

## 6. Early-stopping trace

Use these validation losses:

| Epoch | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Loss | .52 | .43 | .38 | .34 | .33 | .331 | .329 | .330 | .335 | .341 |

Apply patience 3 and minimum improvement 0.002.

1. Track the saved best and patience counter at every epoch.
2. Identify the best qualifying checkpoint.
3. Identify the stop epoch.
4. State which checkpoint should be restored.
5. Explain why the test set must not supply this trace.

## 7. Confusion-matrix analysis

Rows are actual classes and columns are predictions.

| Actual \ Predicted | On time | Slightly late | Severely late |
|---|---:|---:|---:|
| On time | 640 | 45 | 15 |
| Slightly late | 55 | 150 | 25 |
| Severely late | 12 | 28 | 30 |

Calculate:

1. total examples;
2. accuracy;
3. severe-late recall;
4. severe-late precision;
5. the number of actual severe-late shipments missed;
6. the number of false severe-late alarms.

Then recommend whether an operations team with limited intervention capacity should optimize severe-late recall, precision, or a constrained combination. State the business information needed to choose.

## 8. Seed evidence

Five predetermined seeds produce test accuracies:

> 84%, 79%, 86%, 73%, 82%

1. Calculate the mean, median, minimum, maximum, and range.
2. Explain what would be misleading about publishing only 86%.
3. Describe three possible reasons for the 73% run.
4. Distinguish repeating seed 47 from testing five different seeds.
5. List the state required to reproduce one run.

## 9. Release-gate review

Evaluate each proposed workflow.

### Workflow A

The team tunes 20 configurations against the test set, selects the best result, and reports that same test score.

### Workflow B

The team selects a best validation checkpoint, freezes the pipeline, evaluates once on a sealed test set, audits subgroups, and records results from five predetermined seeds.

### Workflow C

The team deploys the final epoch because it is the newest, even though an earlier checkpoint had lower validation loss.

For each workflow, state whether release evidence is valid, what boundary was preserved or broken, and the corrective action.

## 10. Capstone — training, evaluation, and release protocol

Create the following artifact for the capstone model.

### Prediction and leakage contract

Define the prediction unit, moment, target, horizon, eligible features, excluded future information, and operational decision.

### Split manifest

| Partition | Purpose | Selection rule | Groups or time range | Frozen identity |
|---|---|---|---|---|
| Training | | | | |
| Validation | | | | |
| Test | | | | |

### Training configuration

Record batch size, epoch budget, learning rate, shuffle policy, seed list, optimizer identity, checkpoint frequency, and telemetry.

### Selection rule

Record the primary validation metric, patience, minimum improvement, tie-breaker, best-checkpoint rule, and threshold-selection rule.

### Evaluation plan

List the final test procedure, confusion matrix, class metrics, subgroup slices, time slices, error samples, repeated-seed summary, and uncertainty estimate.

### Release evidence card

State purpose, prohibited uses, artifact version, acceptance thresholds, evidence, limitations, approver, monitoring signals, and rollback conditions.

## Reflection

Explain at two levels:

- **Plain language:** why is a low training loss not enough?
- **Technical:** how do data boundaries, optimization state, validation selection, repeated runs, and final testing combine into defensible evidence?
