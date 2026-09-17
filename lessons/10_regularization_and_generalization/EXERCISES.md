# Lesson 10 Exercises — Regularization and Generalization

Complete these exercises after the browser lesson. They require calculation, diagnosis, and experiment design—not programming.

## 1. Diagnose the evidence

For each scenario, identify the strongest initial hypothesis and two checks needed before changing the model.

1. Training accuracy is 61%; validation accuracy is 59%.
2. Training accuracy is 99%; validation accuracy is 72%.
3. Training and validation accuracy are both 99%, but customer IDs overlap across splits.
4. Training accuracy is 91%; validation accuracy is 89%; a new region scores 63%.
5. Training improves until epoch 40; validation peaks at epoch 14 and then worsens.
6. Results range from 65% to 91% across five seeds.

Use the terms underfitting, overfitting, generalization gap, leakage, shift, and instability precisely.

## 2. Capacity–evidence matrix

Predict the likely risk in each case and recommend a controlled first experiment.

| Capacity | Representative evidence | Label noise | Likely risk | First experiment |
|---|---|---|---|---|
| Low | Large | Low | | |
| High | Small | Low | | |
| High | Large | Low | | |
| High | Small | High | | |
| Moderate | Large but shifted | Low | | |

Explain why capacity alone cannot determine whether a model will overfit.

## 3. Learning-curve diagnosis

Three models are trained with 10%, 25%, 50%, and 100% of the available training data.

### Model A

| Data share | Training error | Validation error |
|---:|---:|---:|
| 10% | .42 | .51 |
| 25% | .40 | .47 |
| 50% | .39 | .45 |
| 100% | .39 | .44 |

### Model B

| Data share | Training error | Validation error |
|---:|---:|---:|
| 10% | .05 | .46 |
| 25% | .07 | .35 |
| 50% | .09 | .27 |
| 100% | .11 | .22 |

### Model C

| Data share | Training error | Validation error |
|---:|---:|---:|
| 10% | .23 | .34 |
| 25% | .20 | .27 |
| 50% | .18 | .22 |
| 100% | .17 | .19 |

For each model:

1. classify the pattern;
2. explain what the gap and absolute values show;
3. predict whether more comparable data is likely to help;
4. propose the next experiment.

## 4. Regularized-objective calculations

The prediction loss is 0.30 and the selected weights are 2, −1, and 0.5.

1. Calculate the L1 penalty.
2. Calculate the L2 penalty.
3. Calculate the total objective for L1 with λ = 0.10.
4. Calculate the total objective for L2 with λ = 0.10.
5. Recalculate both objectives with λ = 1.0.
6. Explain why a larger total objective does not by itself mean worse validation performance.

## 5. Parameter-group policy

Classify each item and decide whether it should receive the same weight penalty by default:

- dense-layer weights;
- dense-layer biases;
- embedding table;
- batch-normalization scale;
- batch-normalization running mean;
- frozen pretrained weights;
- newly initialized output head;
- optimizer moving averages.

Distinguish trainable parameters, persistent buffers, optimizer state, and external configuration.

## 6. Dropout reasoning

For drop probabilities 0, 0.25, 0.50, and 0.75:

1. calculate keep probability;
2. calculate inverted-dropout survivor scale;
3. estimate the expected number of active units in a layer of 200 units;
4. explain what happens during evaluation;
5. predict the underfitting risk as drop probability rises.

Then diagnose:

- identical inputs produce different ordinary inference outputs;
- training loss is much higher after increasing dropout from 0.25 to 0.75;
- validation improves but training slows after adding moderate dropout.

## 7. Augmentation policy

For each transformation, decide safe, unsafe, or dependent on the target contract. Explain the invariant being claimed.

1. Horizontally flip a cat photograph for animal classification.
2. Horizontally flip a traffic arrow for direction classification.
3. Add realistic keyboard errors for support-intent classification.
4. Delete negation from a sentiment sentence.
5. Add sensor noise within certified tolerance.
6. Generate a negative distance value.
7. Crop an image while preserving the complete target object.
8. Shift a time series forward so future values enter the feature window.

State how you would test that an augmentation is helping rather than changing the task.

## 8. Normalization distinctions

Answer each question.

1. A feature value is 600, training mean is 300, and training standard deviation is 150. What is the standardized value?
2. Why must those statistics come from training data?
3. What state does batch normalization learn or store?
4. How does layer normalization differ from batch normalization at a high level?
5. Why is input standardization not the same as L2 regularization?
6. What failure occurs if batch normalization remains in training mode during ordinary inference?

## 9. Ablation plan

Design a controlled comparison for:

- baseline;
- L2 or decoupled weight decay;
- dropout;
- valid augmentation;
- early stopping;
- the selected combination.

Hold the split, metrics, seed list, compute budget, and preprocessing policy constant. State:

- the primary validation metric;
- guardrail metrics;
- parameter values being compared;
- number of seeds;
- acceptance threshold for a meaningful improvement;
- how final test evidence remains sealed.

## 10. Capstone — generalization stress-test and control plan

Complete the Phase 2 model evidence card.

### Generalization claim

Name the deployment population, time horizon, important subgroups, and plausible shifts.

### Capacity study

| Candidate | Capacity description | Parameters | Training result | Validation result | Seed variability |
|---|---|---:|---:|---:|---:|
| Small | | | | | |
| Baseline | | | | | |
| Large | | | | | |

### Learning-curve study

Record comparable training and validation results at four sample sizes.

### Regularization ablations

| Candidate | One primary change | Validation evidence | Operational cost | Decision |
|---|---|---|---|---|
| Baseline | None | | | |
| Penalty | | | | |
| Dropout | | | | |
| Augmentation | | | | |
| Early stopping | | | | |
| Selected combination | | | | |

### State and evidence

Record preprocessing statistics, normalization state, parameter groups, dropout locations, augmentation policy, seeds, selected checkpoint, final-test evidence, subgroup results, calibration, limitations, monitoring, retraining, and rollback triggers.

## Reflection

Explain at two levels:

- **Plain language:** how can a model learn too much and too little at the same time?
- **Technical:** how do capacity, data, noise, penalties, dropout, augmentation, early stopping, and honest evaluation interact?
