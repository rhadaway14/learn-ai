# Lesson 10 Reference Notes — Regularization and Generalization

Review these notes only after completing your own attempt.

## 1. Evidence diagnosis

1. Both results are weak and close: investigate underfitting, optimization, labels, features, and excessive regularization.
2. Strong training and weak validation: investigate overfitting, data coverage, duplicates, and regularization.
3. The apparent success is compromised by leakage. Rebuild the split before tuning.
4. The ordinary validation gap is small, but geographic shift is severe. Redesign evidence and training coverage for the deployment region.
5. Later training increases the generalization gap. Preserve the epoch-14 checkpoint and compare targeted controls.
6. Large seed sensitivity indicates brittle optimization or fit. Inspect failed runs and report the distribution.

## 2. Capacity and evidence

- Low capacity with ample clean evidence risks underfitting.
- High capacity with little evidence risks high variance.
- High capacity with broad clean evidence may generalize well and must be judged empirically.
- High capacity with little noisy evidence can memorize label noise.
- Moderate capacity trained on shifted data may generalize poorly regardless of its size.

Capacity matters relative to evidence, signal, noise, optimization, and the deployment claim.

## 3. Learning curves

- **Model A:** high-bias pattern. Both errors remain high and converge. More identical data offers limited improvement; test features, optimization, capacity, and target design.
- **Model B:** high-variance pattern. Training remains strong while validation improves substantially with data. More representative evidence and a targeted constraint may help.
- **Model C:** healthy convergence. Both errors become low and close. Continue shift, subgroup, calibration, and operational validation.

## 4. Objective calculations

For weights 2, −1, and 0.5:

- L1 = 2 + 1 + 0.5 = 3.5;
- L2 = 4 + 1 + 0.25 = 5.25.

With λ = 0.10:

- L1 objective = 0.30 + 0.10 × 3.5 = 0.65;
- L2 objective = 0.30 + 0.10 × 5.25 = 0.825.

With λ = 1.0:

- L1 objective = 3.80;
- L2 objective = 5.55.

The objectives contain different penalties and are not direct task-performance metrics. Candidate quality must be compared with prediction loss and decision metrics on representative validation evidence.

## 5. Parameter groups

Dense weights, embeddings, normalization scales, biases, frozen weights, and new output heads are parameters, but a deliberate policy may treat each differently. Running means are persistent buffers. Optimizer averages are optimizer state. Penalty strengths and inclusion rules are external configuration.

Frozen weights receive no optimizer update. A newly initialized head may need a different learning rate or decay. Bias and normalization parameters are commonly excluded from weight decay, depending on architecture and evidence.

## 6. Dropout

| Drop probability | Keep probability | Survivor scale | Expected active of 200 |
|---:|---:|---:|---:|
| 0 | 1.00 | 1.00 | 200 |
| 0.25 | 0.75 | 1.33 | 150 |
| 0.50 | 0.50 | 2.00 | 100 |
| 0.75 | 0.25 | 4.00 | 50 |

Evaluation disables dropout and uses the full network. Variable ordinary inference suggests the model remains in training mode or another nondeterministic component exists. A jump to 0.75 can remove too much useful signal. Moderate dropout may slow training while improving validation because it constrains co-adaptation.

## 7. Augmentation

1. Cat-photo flip is often safe for species classification.
2. Traffic-arrow flip is unsafe for direction classification.
3. Realistic typos may be safe when intent is preserved.
4. Deleting negation is unsafe when it changes sentiment.
5. In-tolerance sensor noise may be safe.
6. Negative distance is physically invalid.
7. A crop preserving the complete object may be safe.
8. Future values in a feature window create leakage.

Compare the baseline and augmentation under identical splits and seeds, inspect generated examples, and evaluate clean, subgroup, and transformation-robustness results.

## 8. Normalization

1. (600 − 300) ÷ 150 = 2.
2. Complete-data statistics leak validation and test distribution information.
3. Batch normalization learns scale and shift and stores running statistics.
4. Layer normalization computes statistics within an example across selected features rather than relying on batch running statistics.
5. Input standardization changes feature scale; L2 adds parameter pressure to the training objective.
6. Training-mode batch normalization can use or update batch statistics, making inference batch-dependent or unstable.

## 9. Ablation acceptance

A strong plan changes one primary mechanism at a time, uses predetermined seeds, reports variability and operational cost, and defines a meaningful improvement threshold before final testing. The selected combination is compared with its individual components so unnecessary controls can be removed.

## 10. Capstone acceptance criteria

A strong Phase 2 artifact:

- makes a bounded generalization claim;
- distinguishes absolute performance from the train-validation gap;
- compares capacity under controlled conditions;
- uses learning curves to test data-shortage and capacity hypotheses;
- calculates and documents penalty policy;
- verifies dropout and normalization mode behavior;
- reviews augmentation for plausibility and label preservation;
- performs ablations across repeated seeds;
- selects controls with validation evidence only;
- links the approved checkpoint to preprocessing, results, limitations, monitoring, retraining, and rollback.

The phase is complete when another engineer can reproduce the experiment, explain why each constraint exists, and identify what evidence would invalidate the release claim.
