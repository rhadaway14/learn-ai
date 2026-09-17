# Lesson 10 — Regularization and Generalization

## Start here

Training rewards a model for fitting available examples. Production rewards it for behaving usefully on cases it has not seen.

Those goals overlap, but they are not identical.

A high-capacity model can learn the durable relationship, accidental noise, duplicates, labeling quirks, or identifiers that happen to correlate with the target. A low-capacity model can miss the durable relationship entirely. Regularization helps control this fit, but it cannot repair bad data, leakage, an irrelevant validation population, or a target that does not match the real decision.

Use the [interactive lesson](index.html) first. It requires no account, terminal, Python knowledge, paid service, or GPU.

## What this lesson assumes

This lesson builds on:

- training and inference from Lesson 1;
- loss and optimization from Lesson 3;
- sampling, uncertainty, and distribution shift from Lesson 4;
- regression, classification, splits, and leakage from Lesson 5;
- network capacity and activation behavior from Lesson 6;
- training/evaluation modes and checkpoints from Lesson 8;
- training curves, early stopping, error analysis, and seed evidence from Lesson 9.

## Code boundary

The learner path remains browser-based. You will design controlled experiments and interpret their evidence without editing source code. The deterministic program in this directory remains a maintainer reference and regression fixture.

## Running example

We continue with the delivery-risk classifier:

> 10 operational features → 64 hidden values → 16 hidden values → 3 delay classes

The goal is not merely high accuracy on historical shipments. The goal is stable, useful behavior on relevant future shipments, including important customers, routes, seasons, and severe-delay cases.

## 1. Generalization is observed behavior

**Generalization** means that a model performs usefully on relevant unseen examples drawn from the population or shifts named in its contract.

It is not a property that can be read from:

- parameter count;
- training loss alone;
- whether dropout was enabled;
- whether an L2 penalty was used;
- one random seed;
- one convenient test set.

Generalization is supported by evidence: representative held-out evaluation, repeated runs, subgroup and shift tests, honest boundaries, and eventually monitored production outcomes.

## 2. Underfitting and overfitting

### Underfitting

The model fails to capture enough useful structure.

Typical evidence:

- training performance is weak;
- validation performance is also weak;
- the gap between them may be small;
- more training may not help after optimization has stabilized.

Possible causes:

- insufficient capacity;
- poor or missing features;
- an unsuitable architecture;
- incorrect labels or target;
- optimization failure;
- excessive regularization;
- a prediction horizon with too little available signal.

### Overfitting

The model fits training-specific details that do not transfer.

Typical evidence:

- training performance becomes very strong;
- validation performance is materially weaker;
- the gap may widen with more training;
- results may vary substantially across seeds or small data changes.

Possible causes:

- high capacity relative to evidence;
- too little representative data;
- noisy labels;
- duplicate or correlated examples;
- excessive training duration;
- selection against validation noise;
- weak constraints.

### A small gap is not enough

Training and validation can both be poor and close together. That is not successful generalization; it is consistent failure.

Likewise, both can be excellent because leakage lets the same information cross boundaries. Always interpret the gap together with absolute performance and boundary integrity.

## 3. Bias and variance are diagnostic tendencies

**Bias** is systematic error from assumptions that are too restrictive for the relationship. High bias often appears as underfitting.

**Variance** is sensitivity to the particular training sample. High variance often appears as a large train-validation gap or unstable results across samples and seeds.

**Irreducible noise** is variation that the available information cannot predict reliably.

The phrase *bias–variance tradeoff* does not mean every problem has one simple knob. Real systems also face:

- dataset shift;
- label noise;
- optimization error;
- measurement error;
- subgroup imbalance;
- changing decisions and feedback loops.

Use bias and variance as hypotheses supported by learning curves and repeated experiments, not as labels applied from one metric.

## 4. Capacity must be interpreted relative to evidence

Capacity describes the variety of functions a model can represent.

Capacity can increase through:

- more layers;
- wider layers;
- more parameters;
- higher-degree polynomial features;
- richer input features;
- longer training under some conditions;
- less restrictive parameter sharing.

A high-capacity model is not automatically overfit. Large models can generalize well when trained with enough diverse evidence, appropriate optimization, and effective constraints.

A small model is not automatically safe. It can still exploit leakage or fit a narrow shortcut.

The useful question is:

> Is the effective capacity appropriate for the signal, evidence, noise, and deployment claim?

## 5. Learning curves separate several hypotheses

A learning-curve experiment trains comparable models on increasing amounts of training data and records training and validation performance.

### High-bias pattern

Training and validation results converge in a weak-performance region.

Likely responses:

- improve features;
- verify optimization;
- increase appropriate capacity;
- reconsider the target or prediction horizon;
- reduce excessive regularization.

More examples from the same distribution may provide limited benefit if the model cannot represent or access the signal.

### High-variance pattern

Training performance is much stronger than validation performance. Validation improves and the gap may narrow as evidence grows.

Likely responses:

- gather more representative data;
- reduce unnecessary capacity;
- add a controlled regularizer;
- improve augmentation where invariances are valid;
- strengthen group or shift coverage.

### Healthy convergence

Training and validation enter a strong-performance region with a modest gap.

The next questions are about important subgroups, shifts, calibration, latency, and production behavior—not whether one can force the training score even higher.

### Keep the experiment comparable

When sample count changes, preserve:

- validation population;
- architecture and optimization policy;
- metric definitions;
- epoch or compute budget rationale;
- seed protocol;
- preprocessing rules.

Otherwise the curve mixes data quantity with other changes.

## 6. The regularized objective

### The question

How can optimization balance fitting the examples against a preference for selected parameter patterns?

### The operation in words

Take the ordinary data loss. Add a penalty multiplied by a configurable strength.

If data loss is 0.30, the penalty is 0.20, and the strength is 0.10:

> total objective = 0.30 + (0.10 × 0.20) = 0.32

The optimizer follows the total objective. Evaluation should still report the prediction loss and task metrics clearly rather than hiding them inside the penalty total.

### Compact notation

> objective = data loss + λ × penalty

Where:

- **objective** is the quantity optimized;
- **data loss** measures prediction error on the batch;
- **penalty** measures the selected parameter property;
- **λ**, pronounced “lambda,” controls penalty strength.

When λ is zero, that penalty contributes nothing. When λ is too large, the preference can overpower useful fit and cause underfitting.

## 7. L2 regularization

### The question

How can we discourage very large selected weights smoothly?

### The operation in words

Square each selected weight and add the squares.

For weights 2, −1, and 0.5:

> L2 penalty = 2² + (−1)² + 0.5² = 4 + 1 + 0.25 = 5.25

Large magnitudes contribute disproportionately because they are squared.

### Compact notation

> L2 penalty = sum of wᵢ²

Where **wᵢ** means the weight at position *i*.

Typical effect:

- weights shrink smoothly;
- responsibility is distributed rather than concentrated in extreme values;
- weights usually approach but do not become exactly zero.

### L2 penalty and weight decay

The terms are often used loosely as synonyms. In simple gradient descent, adding an L2 penalty produces an update resembling weight decay. With adaptive optimizers, a decoupled weight-decay update can behave differently from adding L2 directly to the loss.

Record the actual optimizer and parameter-group policy instead of relying only on the label “L2.”

## 8. L1 regularization

### The question

How can we encourage sparse selected weights?

### The operation in words

Take the absolute value of each selected weight and add them.

For weights 2, −1, and 0.5:

> L1 penalty = |2| + |−1| + |0.5| = 2 + 1 + 0.5 = 3.5

### Compact notation

> L1 penalty = sum of |wᵢ|

L1 applies pressure that can move small weights exactly to zero, creating sparsity.

Sparsity may help compression or interpretation, but zero weights do not automatically make a neural network understandable or fair.

## 9. Which parameters should receive penalties?

Do not assume every numeric value should receive the same penalty.

Policies often treat these separately:

- layer weights;
- bias terms;
- normalization scale and shift parameters;
- embeddings;
- adapter parameters;
- pretrained versus newly initialized components.

Penalizing biases or normalization parameters can be undesirable. Fine-tuning may use different strengths for different parameter groups. The policy belongs in the experiment record and checkpoint metadata.

## 10. Dropout changes the training network temporarily

During training, dropout randomly sets some activations to zero.

If drop probability is 0.25, keep probability is:

> 1 − 0.25 = 0.75

With inverted dropout, surviving activations are scaled by:

> 1 ÷ keep probability = 1 ÷ 0.75 = 1.33

This keeps the expected activation magnitude comparable between training and evaluation.

### What dropout encourages

Because the available activation pathways change, units cannot depend as strongly on one exact collaboration. Training samples many temporary subnetworks that share parameters.

### Evaluation behavior

Dropout is disabled during validation and inference. The full network produces deterministic output for fixed input, parameters, and other deterministic operations.

Forgetting evaluation mode creates unstable predictions. Applying random dropout during ordinary evaluation also changes the model being measured.

### More is not always better

High drop probability can remove too much signal and cause underfitting. Useful rates depend on architecture, data, location, and other controls.

## 11. Data augmentation encodes invariance

An augmentation creates a plausible training view while preserving the intended target.

It tells the model:

> This change should not change the answer.

### Vision examples

Potentially valid:

- slight brightness or contrast changes;
- modest crops that preserve the object;
- small translations;
- rotations when orientation does not define the label.

Potentially invalid:

- mirroring a direction-dependent traffic sign;
- rotating an orientation-sensitive medical image implausibly;
- cropping away the evidence needed for the label.

### Text examples

Potentially valid:

- carefully reviewed paraphrases;
- realistic keyboard noise;
- substituting non-semantic identifiers.

Potentially invalid:

- deleting negation;
- replacing an entity that determines the label;
- random word reordering that destroys meaning.

### Tabular and time-series examples

Potentially valid:

- measurement noise within known sensor tolerance;
- masking fields that are genuinely missing in production;
- transformations derived from domain symmetries.

Potentially invalid:

- impossible negative quantities;
- changing target-bearing history without updating the target;
- crossing physical or operational constraints.

Apply random augmentation to training data. Validation and test should ordinarily measure the defined population in a stable way, with separate robustness tests when needed.

## 12. Early stopping is implicit regularization

Training duration affects effective fit. Stopping at the best validation checkpoint prevents later epochs from fitting more training-specific detail.

Early stopping is called *implicit* regularization because it constrains the learned solution through the optimization path rather than adding a direct weight penalty.

It remains a model-selection procedure and therefore uses validation evidence—not test evidence.

Early stopping can coexist with L2, dropout, or augmentation. That does not mean stacking every control is optimal.

## 13. Capacity control is regularization too

Choosing a smaller architecture, sharing parameters, freezing pretrained layers, or limiting adapter rank can reduce effective capacity.

This may:

- improve generalization;
- reduce compute and memory;
- simplify deployment;
- or cause underfitting if useful structure cannot be represented.

The simplest model that meets the evidence and operational requirements is often preferable, but “simplest” includes the whole system—not parameter count alone.

## 14. Normalization is not one thing

### Input standardization

Input standardization usually transforms a feature into standard-deviation units:

> standardized value = (value − training mean) ÷ training standard deviation

For a distance of 600 miles, training mean 300, and training standard deviation 300:

> (600 − 300) ÷ 300 = 1

The value is one training standard deviation above the training mean.

Fit the mean and standard deviation on training data only. Store and reuse them for validation, test, and production.

Input scaling improves numerical conditioning. It is not itself proof of generalization.

### Batch normalization

Batch normalization transforms internal activations and maintains:

- learned scale and shift parameters;
- training-time batch statistics;
- persistent running statistics used during evaluation.

It can have a regularizing side effect because batch statistics are noisy, but its primary mechanism is not the same as L1, L2, or dropout.

### Layer normalization

Layer normalization computes statistics within each example across selected features. It is common in transformers and does not use running batch statistics in the same way as batch normalization.

Do not use the word *normalization* without naming which mechanism, axes, state, and mode behavior you mean.

## 15. Data quality can dominate regularization

No regularizer repairs:

- labels that encode the wrong outcome;
- missing causal or predictive information;
- future information leaked into features;
- duplicate groups across splits;
- severe deployment shift;
- a metric unrelated to the decision;
- systematic underrepresentation of important populations.

Before tuning regularization, verify the experiment from Lesson 9.

## 16. Design controlled regularization experiments

Start with a credible baseline. Then change one primary intervention at a time.

For each candidate record:

- architecture and parameter count;
- training-data identity;
- preprocessing state;
- augmentation policy;
- optimizer and learning-rate schedule;
- L1, L2, or weight-decay policy;
- dropout locations and rates;
- epoch budget and early-stopping rule;
- predetermined seeds;
- train, validation, and final test metrics;
- subgroup and shift metrics;
- compute, latency, and memory.

An **ablation** removes or changes one component to measure its contribution under an otherwise controlled protocol.

Useful comparisons include:

- baseline versus L2 only;
- baseline versus dropout only;
- baseline versus valid augmentation only;
- each candidate across the same seeds;
- selected combination versus each component alone.

## 17. Select the smallest defensible control set

More controls create more hyperparameters, interactions, and operational state.

A defensible selection:

1. fixes the evaluation contract;
2. establishes a baseline;
3. diagnoses likely bias, variance, data shortage, or boundary failure;
4. tests a targeted response;
5. repeats across predetermined seeds;
6. checks task, subgroup, calibration, and operational metrics;
7. chooses with validation evidence;
8. evaluates once on sealed final evidence;
9. documents the exact selected state.

Do not select the most complicated configuration merely because its validation metric wins by an amount smaller than evaluation noise.

## 18. Common failures

| Failure | Evidence | Response |
|---|---|---|
| Excessive regularization | Training and validation both worsen | Reduce strength or remove the unnecessary control |
| Inadequate regularization | Strong training fit, weak validation fit | Verify boundary, then test targeted controls or more data |
| Invalid augmentation | Performance degrades on unchanged semantics | Repair domain invariance and label-preservation rules |
| Dropout active at inference | Repeated predictions vary | Use evaluation mode and test stability |
| Preprocessing leakage | Validation/test statistics influenced training | Refit on training only and invalidate prior results |
| Penalty applied to every parameter | Important scales or biases collapse | Define explicit parameter groups |
| Learning curve mixes configurations | Apparent trend has multiple causes | Keep model and protocol comparable |
| Regularization tuned on test | Optimistic final estimate | Retire consumed test evidence |
| Wrong deployment population | Good held-out score, poor production transfer | Redesign splits and shift tests |

## 19. Connection to modern AI

The same mechanisms appear in foundation-model systems:

- pretraining scale supplies vast and diverse evidence;
- weight decay and dropout remain common training controls;
- data deduplication prevents memorization and benchmark contamination;
- fine-tuning can overfit a small instruction dataset;
- LoRA rank limits trainable adaptation capacity;
- freezing layers constrains which representations can change;
- early stopping protects small fine-tuning datasets;
- text and multimodal augmentation require semantic invariance;
- benchmark reuse can overfit research decisions to the benchmark;
- retrieval and prompt changes can overfit an application evaluation set even when model weights never change.

Regularization is therefore broader than a term in a neural-network loss. It is any deliberate constraint on how a system adapts to finite evidence.

## Interactive learning sequence

The browser lesson provides practice in this order:

1. distinguish underfitting, useful fit, and overfitting;
2. vary capacity, evidence, noise, and constraint together;
3. diagnose learning-curve patterns;
4. compare L1 and L2 weight behavior;
5. observe dropout across training and evaluation passes;
6. judge domain-specific augmentation policies;
7. separate input scaling, internal normalization, and regularization;
8. choose an evidence-based response plan;
9. complete knowledge checks;
10. produce the Phase 2 capstone milestone.

## Capstone increment: generalization stress-test and control plan

Complete the reproducible model-training specification and model evidence card promised for Lessons 6–10.

### Generalization claim

State the deployment population, time horizon, important groups, and expected shifts.

### Capacity evidence

Compare at least three defensible capacity levels under the same protocol.

### Learning curves

Record training and validation metrics across increasing sample counts and repeated seeds.

### Regularization ablations

Compare the baseline against relevant individual controls:

- L1 or L2/weight decay;
- dropout;
- valid augmentation;
- early stopping;
- capacity reduction or freezing.

### State contract

Record preprocessing statistics, normalization state, parameter groups, dropout locations, augmentation policy, seeds, and selected checkpoint.

### Evidence card

Include:

- train, validation, and sealed test results;
- class, subgroup, shift, and calibration results;
- repeated-seed variability;
- chosen controls and rejected alternatives;
- known limitations;
- monitoring, retraining, and rollback triggers.

## Phase 2 milestone

After this lesson, the learner should be able to explain and specify:

- a neural-network architecture;
- forward and backward state;
- framework runtime state;
- a reproducible training and evaluation protocol;
- a controlled generalization strategy;
- a model evidence card that supports a release decision.

The next phase begins language-model mechanics with tokenization.

## Definition of done

- [ ] Complete every browser interaction.
- [ ] Explain why a small generalization gap can still be bad.
- [ ] Diagnose high-bias, high-variance, and healthy learning curves.
- [ ] Calculate L1 and L2 penalties for small weight sets.
- [ ] Explain the role of λ in the objective.
- [ ] Explain dropout scaling and mode behavior.
- [ ] Judge whether an augmentation preserves the target.
- [ ] Distinguish input, batch, and layer normalization from regularization.
- [ ] Design controlled ablations across repeated seeds.
- [ ] Produce the capstone generalization stress-test and evidence card.
- [ ] Mark Lesson 10 complete in the browser.

## Instructor and maintainer note

The learner-facing material intentionally contains no programming requirement. `lab.py` remains a maintainer reference and automated regression fixture. Preserve the browser-first path until a later lesson explicitly introduces the programming workflow.
