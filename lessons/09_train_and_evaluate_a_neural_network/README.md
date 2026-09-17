# Lesson 09 — Train and Evaluate a Neural Network

## Start here

A neural network can reduce its training loss and still be useless in production.

That is not a contradiction. Training loss answers a narrow question:

> How well does this model fit the examples currently used for optimization?

A production decision needs a broader answer:

> How well is this frozen system likely to perform on relevant future cases, including the costly and unusual ones?

This lesson builds the complete path between those questions.

Use the [interactive lesson](index.html) first. It runs locally in a browser and requires no account, terminal, Python knowledge, cloud service, or GPU.

## What this lesson assumes

The lesson uses ideas already introduced:

- features, targets, training, and inference from Lesson 1;
- tensors and shapes from Lesson 2;
- loss, gradients, and learning rates from Lesson 3;
- sampling and uncertainty from Lesson 4;
- classification metrics and data leakage from Lesson 5;
- neural-network layers from Lesson 6;
- backward propagation from Lesson 7;
- tensor, autograd, module, optimizer, mode, and checkpoint state from Lesson 8.

If the words *validation*, *batch*, *epoch*, or *seed* are unfamiliar, that is expected. They are taught here.

## Code boundary

You do not need to read or edit Python in this lesson. The repository retains a deterministic reference program for maintainers and automated tests. The learner path uses visible controls so that programming syntax does not hide the training and evaluation mechanism.

The important outcome is a precise execution and evidence contract. A later implementation can express that contract in Python, another language, or a managed training platform.

## Running example: delivery-risk classification

We will use one scenario throughout the lesson.

A delivery platform predicts one of three outcomes:

1. on time;
2. slightly late;
3. severely late.

Each prediction uses ten features available at the decision moment, such as route length, carrier history, weather category, current queue depth, and remaining schedule margin.

The Lesson 6 architecture transforms those ten features through widths:

> 10 inputs → 64 hidden values → 16 hidden values → 3 class scores

The network contains 1,795 trainable parameters. Lesson 8 described how a framework manages those parameters and their gradients. This lesson designs the experiment that trains them and decides whether the result deserves release.

## 1. Training and evaluation have different jobs

### Training

Training examples are allowed to change parameters.

For each training batch, the system:

1. loads features and targets;
2. performs a forward pass;
3. calculates loss;
4. performs backward propagation;
5. updates the parameters.

Repeating this process creates many candidate model states.

### Validation

Validation examples do not update parameters. They compare candidates and guide choices such as:

- learning rate;
- architecture width;
- regularization strength;
- number of epochs;
- early-stopping point;
- classification threshold;
- which checkpoint to retain.

Because validation results influence decisions, the validation set is no longer untouched evidence after model selection.

### Testing

The test set estimates the final, frozen selection process. It should be used after the model, preprocessing, thresholds, and checkpoint-selection rule are fixed.

If test results repeatedly influence choices, the test set has become another validation set. A new untouched test set is then needed for an honest final estimate.

### A responsible metaphor

Think of training as classwork, validation as a practice exam, and testing as a sealed final exam.

The metaphor explains why the same questions cannot be used both to design the study strategy and to judge the final strategy fairly.

It has a limit: real data may contain related records. Two shipments from the same customer or event can be more similar than two exam questions. A careless random split can therefore leak recognizable patterns across the boundary even when every row appears only once.

## 2. Define the prediction contract before splitting

Before creating partitions, write down:

- **unit of prediction:** one shipment, customer, image, message, or other entity;
- **prediction moment:** the exact time at which inference occurs;
- **features:** information available at that moment;
- **target:** the outcome the system should predict;
- **prediction horizon:** how far into the future the target occurs;
- **deployment population:** the people, devices, customers, or events that will receive predictions;
- **decision use:** what action follows each prediction;
- **error costs:** the consequences of false positives and false negatives.

This contract determines which records are eligible and what a representative split means.

### Example

Suppose the model predicts severe lateness six hours before scheduled delivery.

A feature calculated from the actual delivery timestamp is unavailable at prediction time. Including it would be target leakage even if the feature appears in a clean numeric column.

Likewise, a correction entered by an operator after delivery is not historical evidence available to the prediction. It is information from the future.

## 3. Split strategies must match the deployment question

### Random record split

Records are assigned randomly to training, validation, and test partitions.

Use this only when examples are reasonably independent and drawn from the same process. It is simple but frequently overused.

### Group split

All records belonging to a group remain together.

Groups may be customers, patients, users, devices, routes, physical locations, source documents, or incidents.

If production requires predictions for unseen customers, holding out complete customers tests the right question. A record-level random split may let the model learn a customer's characteristic pattern and then appear to generalize to another record from that same customer.

### Time split

Training uses earlier data, validation uses a later period, and testing uses the most recent held-out period.

This mirrors systems deployed into the future. It also reveals temporal drift such as new carrier behavior, policy changes, seasonality, or sensor replacements.

### Geographic or domain split

Sometimes the required claim is transfer to a new region, hospital, product line, or language. The split should hold out that domain explicitly.

### Split sizes

There is no universal percentage. The partitions need enough examples to perform their jobs.

A small dataset may benefit from cross-validation. A huge dataset may need only a small percentage for stable validation and test estimates. Rare classes and important groups must have enough representation for meaningful measurements.

## 4. Leakage can occur outside the model

Leakage means information crosses an experimental boundary in a way that would not occur during deployment.

Common sources include:

- near-duplicate records in different partitions;
- records from the same event or customer split across partitions;
- future information included as a feature;
- normalization statistics calculated using validation or test data;
- feature selection performed using the complete dataset;
- thresholds tuned against test outcomes;
- manual data cleanup informed by test errors;
- repeated test-set review during development.

### Preprocessing must be fitted on training data

Suppose feature standardization subtracts a mean and divides by a standard deviation.

The correct sequence is:

1. calculate the mean and standard deviation from training data only;
2. store those values as preprocessing state;
3. apply the stored values to training, validation, test, and future production inputs.

Calculating the mean from the complete dataset lets validation and test distributions influence training-time representation.

## 5. Dataset, batch, step, and epoch

These terms describe different units of work.

| Term | Meaning |
|---|---|
| Example | One feature-target pair |
| Dataset | An organized collection of examples |
| Batch | Examples processed together before one optimizer update |
| Step or iteration | One batch-level parameter update |
| Epoch | One planned pass through the training dataset |

### The practical question

How many optimizer updates happen?

First calculate batches per epoch:

> batches per epoch = training examples divided by batch size, rounded up

Then calculate total updates:

> total updates = batches per epoch × epochs

For 1,000 examples, batch size 50, and 5 epochs:

> 1,000 ÷ 50 = 20 batches per epoch

> 20 batches × 5 epochs = 100 optimizer updates

The final smaller batch matters when the dataset size is not evenly divisible by batch size.

### Batch-size tradeoffs

Smaller batches use less activation memory, create more updates per epoch, and produce noisier gradient estimates. Noise can help exploration, but tiny batches may underuse parallel hardware.

Larger batches use more memory, create fewer updates per epoch, and produce smoother gradient estimates. They can use accelerator parallelism efficiently but may need learning-rate adjustment.

Batch size is therefore both a statistical and systems hyperparameter.

## 6. Shuffling changes batch composition

Without shuffling, meaningful ordering can repeatedly group similar examples.

Imagine shipment records sorted by carrier. The first batches contain only carrier A, later batches contain carrier B, and so on. Each update pulls the model toward the current carrier's pattern before the next carrier pulls it elsewhere.

Shuffling changes group composition each epoch while preserving the same training examples.

Do not shuffle away a dependency the model needs. Sequence models and time-series windows may require order within each example, even while the examples themselves are shuffled.

## 7. The complete training epoch

A training epoch coordinates multiple layers of state:

1. put the model in training mode;
2. select the epoch's example order;
3. load one batch;
4. move or represent tensors under the device and dtype policy;
5. clear stale gradients;
6. perform the forward pass;
7. calculate batch loss;
8. perform backward propagation;
9. apply the optimizer step;
10. accumulate detached reporting totals;
11. repeat for every batch;
12. report a correctly weighted epoch result.

### Correct loss aggregation

If batches have different sizes, averaging the batch averages equally can be wrong.

Suppose one batch contains 50 examples with average loss 0.4 and the final batch contains 10 examples with average loss 0.8.

An equal batch average gives:

> (0.4 + 0.8) ÷ 2 = 0.6

But the example-weighted result is:

> ((50 × 0.4) + (10 × 0.8)) ÷ 60 = 0.467

The second answer represents the average example.

This quiet measurement bug can distort training and validation curves without causing a runtime error.

## 8. Validation is an evaluation pass, not a training pass

After an epoch, validation usually:

1. switches the model to evaluation mode;
2. disables unnecessary gradient recording;
3. loads validation batches;
4. performs forward calculations;
5. accumulates loss and task metrics;
6. makes no optimizer updates;
7. restores or begins the next training phase deliberately.

Validation must not update model parameters, fit preprocessing state, update training-only behavior unintentionally, or use test labels to choose a model.

## 9. Read curves as relationships, not isolated numbers

### Both training and validation improve

The model is learning signal that transfers. It may still benefit from more training.

### Training improves while validation flattens

The model continues fitting training data, but additional fit offers little validation benefit. Early stopping or regularization may help.

### Training improves while validation worsens

The generalization gap is widening. The model is increasingly fitting training-specific patterns.

### Both remain high

Possible causes include insufficient model capacity, poor features, incorrect labels, a low learning rate, broken gradients, incompatible loss, or preprocessing errors.

### Both oscillate or diverge

The learning rate may be too high, inputs may be badly scaled, gradients may be unstable, or the data may contain severe anomalies.

Do not diagnose solely from one curve. Check data, gradients, prediction distributions, metrics, and examples.

## 10. Early stopping is a state machine

Early stopping has at least four pieces of state:

- best validation value so far;
- checkpoint associated with that value;
- minimum qualifying improvement;
- count of consecutive non-qualifying epochs.

### Patience

Patience is the number of non-qualifying epochs allowed before training stops. It prevents one noisy validation result from ending training immediately.

### Minimum improvement

Minimum improvement requires a new result to beat the saved best by a meaningful amount. Without it, microscopic noise can reset patience indefinitely.

### Best is not last

When stopping occurs, the system should restore the best qualifying checkpoint. The stop epoch and the best epoch are normally different.

### Never stop from the test set

Stopping based on test loss makes test evidence part of model selection. Use validation evidence.

## 11. A confusion matrix names the mistakes

For multiclass classification, a confusion matrix compares actual classes with predicted classes.

In this course, rows represent actual outcomes, columns represent predictions, diagonal cells are correct, and off-diagonal cells are errors.

Always label the orientation. Libraries and articles do not all use the same convention.

### Accuracy

The question:

> Out of all predictions, what share was correct?

The operation:

> correct diagonal counts divided by all counts

Accuracy treats every example equally and can hide rare-class failure.

### Recall for severely late shipments

The question:

> Out of shipments that were actually severely late, what share did we detect?

The operation:

> correctly predicted severe-late shipments divided by all actual severe-late shipments

Low recall means costly cases escape intervention.

### Precision for severely late shipments

The question:

> Out of shipments flagged as severely late, what share truly was?

The operation:

> correctly predicted severe-late shipments divided by all severe-late predictions

Low precision means intervention capacity is spent on false alarms.

### Choose metrics from decisions

If missing a severe delay is costly, recall matters. If each intervention is expensive, precision matters. If predicted probabilities drive resource allocation, calibration matters. If users wait synchronously, latency matters.

## 12. Error analysis goes beyond the matrix

Inspect high-confidence false positives and false negatives, severe errors between distant classes, rare-group errors, suspicious missing features, boundary cases, and recent time periods.

Ask whether the label is correct, the needed information was available, the group was represented, preprocessing is consistent, the case is ambiguous, or the requested prediction is even possible at this horizon.

Error analysis often reveals a data or problem-framing issue that a larger model cannot fix.

## 13. Reproducibility, determinism, and robustness differ

### Seed

A seed initializes a pseudo-random number generator. Under compatible conditions, it can reproduce operations such as initialization, shuffling, or dropout masks.

### Reproducibility

Reproducibility also requires data and split identity, code version, configuration, preprocessing state, architecture, checkpoints, dependency versions, device details, optimizer state, random states, and the evaluation procedure.

### Determinism

Determinism means repeated execution produces the same result. Some parallel hardware operations are nondeterministic unless slower deterministic alternatives are selected.

### Robustness across seeds

One repeatable run may be lucky. Train with several predetermined seeds and report individual results, mean or median, range, variability, and failed runs.

Do not run many seeds and publish only the best one.

## 14. Model selection must precede final testing

A defensible sequence is:

1. define the target, eligible data, groups, time boundary, and metrics;
2. create and freeze split identities;
3. fit preprocessing on training data;
4. train candidates;
5. compare candidates using validation evidence;
6. perform error and subgroup analysis;
7. choose settings, threshold, and checkpoint rule;
8. lock the selection;
9. evaluate the selected system on the sealed test set;
10. document results and limitations;
11. decide against predetermined release thresholds.

If the final test result leads to another round of choices, record that the test was consumed and create new untouched evidence where possible.

## 15. Checkpoint roles

### Latest checkpoint

Captures recent training state and supports recovery from interruption.

### Best validation checkpoint

Captures the candidate with the strongest qualifying validation evidence. It is the ordinary model-selection artifact.

### Release checkpoint

The approved artifact is packaged with its architecture, preprocessing contract, labels, version, provenance, evaluation results, operating thresholds, limitations, compatibility, and rollback identity.

These roles may point to the same underlying state, but they should not be confused.

## 16. Evaluation evidence is larger than one metric

A release evidence card should state:

- model purpose and prohibited uses;
- training, validation, and test populations;
- split strategy and dates;
- target and prediction moment;
- model and preprocessing version;
- primary and guardrail metrics;
- confusion matrix;
- subgroup and time-slice results;
- multiple-seed variability;
- important error examples;
- known limitations;
- acceptance thresholds;
- approver and decision;
- monitoring and rollback plan.

A strong evidence card does not turn weak evidence into strong evidence. It makes the evidence and its limits visible.

## 17. Evaluation continues after release

Offline test performance estimates a deployment environment. It does not freeze the world.

Monitor input schema, missingness, feature drift, prediction drift, latency, failures, subgroup behavior, delayed production quality, intervention volume, business outcomes, and feedback loops caused by model decisions.

Production thresholds for alerting, retraining, rollback, and human review belong in the release protocol.

## 18. Common loud and quiet failures

| Failure | Loud or quiet? | Detection | Response |
|---|---|---|---|
| Shape or device mismatch | Usually loud | Runtime error and contract assertion | Correct tensor construction or placement |
| No parameter gradients | Loud or quiet | Gradient inventory | Repair graph or parameter registration |
| Validation updates weights | Quiet | Parameter checksum before and after | Remove optimizer transitions from evaluation |
| Preprocessing fitted on all data | Quiet | Fit-scope audit | Refit on training only and rerun evaluation |
| Duplicate groups across splits | Quiet | Group-overlap test | Rebuild split by group |
| Test-set tuning | Quiet | Experiment decision log | Retire consumed test evidence |
| Best seed only | Quiet | Run registry | Report predetermined repeated runs |
| Last checkpoint deployed | Quiet | Checkpoint metadata comparison | Restore and package validated best state |
| Unequal batches averaged equally | Quiet | Aggregation test | Weight totals by example count |
| Strong average, weak subgroup | Quiet | Sliced evaluation | Redesign data, model, threshold, or use policy |

## Connection to modern AI

The same evidence boundaries apply beyond small classifiers.

- Fine-tuning an LLM still needs training, validation, and test separation.
- Retrieval systems need query sets that were not hand-tuned into the index or prompts.
- Agent evaluation must keep acceptance tasks separate from development traces.
- Multimodal systems need group-aware splits so near-duplicate images or documents do not leak.
- Foundation-model benchmarks become less informative when repeatedly used to guide development.
- Production AI needs versioned prompts, tools, retrievers, models, and evidence—not only weights.

Scale changes the cost of an experiment. It does not remove the need for honest evidence.

## Interactive learning sequence

The browser lesson provides supported practice in this order:

1. distinguish training, validation, and test jobs;
2. design dataset proportions and split strategies;
3. calculate batches, epochs, and optimizer updates;
4. diagnose learning-rate behavior from curves;
5. configure early stopping and best-checkpoint restoration;
6. inspect a multiclass confusion matrix;
7. compare one seed with a repeated-run distribution;
8. build a release evidence gate;
9. complete knowledge checks;
10. produce the capstone protocol.

## Capstone increment: training, evaluation, and release protocol

Extend the prior capstone artifacts with:

### Prediction and data contract

- prediction unit and moment;
- target and horizon;
- eligible features;
- deployment population;
- leakage exclusions.

### Split contract

- split strategy and reason;
- group or time boundary;
- frozen record identities;
- class and subgroup counts;
- overlap checks.

### Training contract

- batch size;
- epoch budget;
- learning rate;
- shuffle policy;
- seed list;
- optimizer and checkpoint state;
- recorded curves and telemetry.

### Selection and evaluation contract

- primary validation measure;
- early-stopping patience and minimum improvement;
- tie-breaking and best-checkpoint rules;
- final test procedure;
- confusion matrix and class metrics;
- subgroup and time-slice metrics;
- error-review samples;
- repeated-seed summary.

### Release contract

- acceptance and guardrail thresholds;
- approval owner;
- artifact identity;
- monitoring signals;
- rollback conditions.

## Definition of done

- [ ] Complete every browser interaction.
- [ ] Explain the separate jobs of training, validation, and test data.
- [ ] Choose a split strategy based on the deployment claim.
- [ ] Calculate updates from examples, batch size, and epochs.
- [ ] Diagnose training and validation curve relationships.
- [ ] Explain patience, minimum improvement, stop epoch, and best epoch.
- [ ] Interpret accuracy, class recall, class precision, and confusion-matrix cells.
- [ ] Distinguish seed repeatability from robustness.
- [ ] Explain why model selection must precede final testing.
- [ ] Produce the capstone training, evaluation, and release protocol.
- [ ] Mark Lesson 9 complete in the browser.

## Instructor and maintainer note

The learner-facing lesson deliberately does not expose source code. `lab.py` and the deterministic course-lab implementation remain maintainer references and automated regression fixtures. Do not direct learners to them until a future lesson explicitly teaches the required programming workflow.
