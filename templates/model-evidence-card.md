# Model-Training Specification and Evidence Card

Use this card for the cumulative Lessons 6–10 artifact. It is a specification until Engineering Lab A establishes implementation readiness.

## Intended use

- Prediction target, unit, horizon, and user:
- Supported decision:
- Prohibited or unsupported use:
- Deployment population and expected shifts:

## Data contract

- Eligible prediction-time features:
- Label definition and availability time:
- Train/validation/test boundary:
- Duplicate, entity, and time leakage controls:
- Preprocessing fit scope:

## Architecture and shapes

| Stage | Input shape | Operation | Output shape | Learned state |
|---|---|---|---|---|
| Input | | | | |
| Hidden | | | | |
| Output | | | | |

## Training protocol

- Loss and why it matches the task:
- Optimizer controls, batch size, epoch budget, and seeds:
- Gradient clear/forward/loss/backward/step lifecycle:
- Training/evaluation mode behavior:
- Early-stopping and best-checkpoint rule:

## Evaluation evidence

- Baseline and primary metrics:
- Train/validation/test results:
- Confusion matrix or residual analysis:
- Subgroup, time-slice, calibration, and repeated-seed results:
- Uncertainty and known limitations:

## Generalization controls

- Capacity evidence:
- L1/L2, dropout, augmentation, or early-stopping experiments:
- Selected control set and validation rationale:
- Shift, monitoring, retraining, and rollback triggers:

## Reproduction contract

- Required state, versions, configuration, and checkpoint contents:
- Browser evidence procedure before Engineering Lab A:
- Automated commands and expected results after Engineering Lab A:

## Release decision

- Decision and approver:
- Acceptance thresholds:
- Failed or deferred criteria:
- Next revision trigger:
