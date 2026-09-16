# Lesson 05 — Regression and Classification

## Start here

Open the [interactive lesson](index.html). The complete learner path runs in a browser and requires no programming.

Lessons 1–4 established how models learn, how AI data is represented, how optimization reduces loss, and how probability describes uncertainty. Lesson 5 turns those pieces into a complete supervised-learning decision: define a target, choose regression or classification, establish a baseline, evaluate on held-out data, and connect model errors to real consequences.

By the end of this lesson, you should be able to:

- distinguish features, labels, predictions, scores, and decisions;
- decide whether a business question requires regression or classification;
- interpret residuals, MAE, RMSE, and R² for regression;
- read every cell of a binary confusion matrix;
- calculate and interpret accuracy, precision, recall, specificity, and F1;
- explain how a classification threshold changes operational behavior;
- choose metrics and a threshold from error costs rather than habit;
- explain ROC and precision–recall curves without overstating AUC;
- design train, validation, and test splits that resemble production;
- identify obvious target, temporal, entity, preprocessing, and test-set leakage; and
- finish Foundation Gate A for the cumulative capstone.

## 1. Supervised learning starts with known answers

In supervised learning, each historical example contains:

1. information the model may use; and
2. the correct outcome it should learn to estimate.

For an AI delivery advisor, one example might represent a completed project. Its inputs could include document count, number of source systems, required integrations, team capacity, and planned duration. Its known outcomes could include actual engineer-hours and whether the project finished late.

| Term | Meaning | Delivery-advisor example |
|---|---|---|
| Example or observation | One case used for learning or evaluation | One delivery project |
| Feature | An input available when prediction occurs | Planned integration count |
| Label or target | The known outcome to estimate | Actual hours or late/on time |
| Prediction | The model's estimate for a new example | 620 hours or 72% late risk |
| Parameter | A value learned from training examples | A weight on integration count |
| Hyperparameter | A training or design setting chosen outside learning | Maximum tree depth |

### The prediction-time rule

A feature is valid only if it is legitimately available at the moment the real prediction will be made.

If the advisor predicts lateness during project intake, the planned number of integrations is available. The actual completion date and final delay-reason code are not. Including those future fields creates **target leakage**: the model receives information that reveals or closely follows the answer.

Leakage often produces spectacular validation results and disappointing production behavior. The validation is not measuring the real task.

## 2. Task framing comes before algorithm selection

“Use machine learning to predict project risk” is not a complete problem statement. A supervised-learning task should specify:

- **unit of prediction:** one project, customer, transaction, document, or request;
- **target:** the exact numeric value or category;
- **time horizon:** when the outcome is measured;
- **prediction moment:** when the model must produce its estimate;
- **action:** what changes because of the prediction;
- **error costs:** what false alarms and missed cases cause; and
- **target population:** which future cases the system is intended to serve.

### Regression predicts a numeric amount

Regression targets vary along a numeric scale:

- engineer-hours;
- response latency;
- monthly revenue;
- delivery duration;
- temperature; or
- remaining useful life.

### Classification predicts a category

Classification targets are categories:

- late or on time;
- fraud or legitimate;
- approve, review, or reject;
- billing, security, or product-support route; or
- document type.

Binary classification has two classes. Multiclass classification chooses among more than two mutually exclusive classes. Multilabel classification allows several labels to apply at once.

The same domain can contain both task types. “How many hours will this project require?” is regression. “Will this project miss its date?” is classification.

## 3. Regression predicts a location on a numeric scale

Linear regression is one method for solving a regression task. Decision trees, ensembles, neural networks, and other model families can also predict numeric targets.

### Residuals

A residual is the signed difference between the actual value and the prediction.

In words:

> residual = actual value − predicted value

For an actual effort of 640 hours and a prediction of 590 hours:

$$
640 - 590 = +50\text{ hours}
$$

A positive residual means the prediction was too low. A negative residual means it was too high. Looking at residual patterns can reveal missing nonlinear structure, different variance across the range, subgroup failures, or systematic underprediction.

### Mean Absolute Error

MAE asks: how far away are predictions on average, ignoring direction?

For absolute errors of 10, 20, and 30 hours:

$$
\operatorname{MAE}=\frac{10+20+30}{3}=20\text{ hours}
$$

Compactly:

$$
\operatorname{MAE}=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

Here, $n$ is the number of examples, $y_i$ is the actual target, and $\hat{y}_i$ is the prediction. MAE is easy to communicate because it remains in target units.

### Root Mean Squared Error

RMSE asks: what is the typical error when large misses should receive extra weight?

For errors of 10, 20, and 30 hours:

1. Square them: 100, 400, and 900.
2. Average them: $(100+400+900)\div3=466.67$.
3. Take the square root: approximately 21.6 hours.

$$
\operatorname{RMSE}=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

RMSE is more sensitive to large misses than MAE. That is useful when a few severe underestimates create disproportionate harm, but it also makes the metric sensitive to outliers.

### R-squared

R² asks: how does this model compare with always predicting the target mean?

$$
R^2=1-\frac{\text{model squared error}}{\text{mean-baseline squared error}}
$$

- $R^2=1$ means perfect predictions on that dataset.
- $R^2=0$ means the model matches the mean baseline.
- $R^2<0$ means the model is worse than that baseline.

R² is not “percent correct,” and a high R² does not prove causation, unbiased data, or acceptable error for the business.

### Baselines and generalization

A naive baseline is a deliberately simple reference. For regression, predict the training-set mean for every case. A useful model should outperform that baseline on unseen data.

A flexible model can memorize training examples and show nearly zero training error while performing badly between or beyond them. That is **overfitting**. Generalization is the ability to perform well on new cases drawn from the intended population.

## 4. Classification produces evidence for categories

A binary classifier commonly produces a score for the positive class. The positive class is simply the event the system is trying to detect—late project, fraud, defect, or escalation. It is not necessarily desirable.

The score may be used to rank cases. It should only be called a probability when the model and its calibration justify that interpretation.

### Logistic regression

Logistic regression combines features into a weighted score and passes it through a sigmoid function. The sigmoid compresses any real-number score into a value between 0 and 1.

For weighted score $z$:

$$
p=\frac{1}{1+e^{-z}}
$$

- $z$ is the weighted evidence from the features;
- $e$ is the natural exponential constant; and
- $p$ is the bounded output for the positive class.

When $z=0$, $e^0=1$, so $p=1\div(1+1)=0.5$. Large positive scores approach 1, and large negative scores approach 0.

Logistic regression learns feature weights. The model score still needs an operating rule.

### Threshold and decision boundary

A threshold converts a score into a class decision. With a 0.70 threshold:

- score 0.82 becomes positive;
- score 0.64 becomes negative.

The **decision boundary** is the location in feature space where the decision changes. With one feature it can be a point; with two features, a line or curve; with many features, a high-dimensional surface.

Changing the threshold moves the operating boundary without retraining the model. That distinction matters: the model ranking can stay fixed while product behavior changes.

## 5. The confusion matrix names every binary result

| | Actually positive | Actually negative |
|---|---:|---:|
| Predicted positive | True positive (TP) | False positive (FP) |
| Predicted negative | False negative (FN) | True negative (TN) |

For late-project prediction:

- **TP:** escalated and actually late;
- **FP:** escalated but actually on time;
- **FN:** not escalated but actually late; and
- **TN:** not escalated and actually on time.

The words “true” and “false” describe whether the prediction matched reality. “Positive” and “negative” describe the selected class.

## 6. Classification metrics answer different questions

### Accuracy

Accuracy asks: what fraction of all decisions were correct?

$$
\text{accuracy}=\frac{TP+TN}{TP+FP+FN+TN}
$$

Accuracy can be appropriate when classes are reasonably balanced and the errors have similar costs. It can conceal complete failure on a rare class.

If 10 of 1,000 projects are late, predicting “on time” for every project produces 990 correct decisions and 99% accuracy—but catches no late projects.

### Precision

Precision asks: when the model predicted positive, how often was it correct?

$$
\text{precision}=\frac{TP}{TP+FP}
$$

Prioritize precision when false positives are especially costly or review capacity is limited.

### Recall or sensitivity

Recall asks: of all actual positives, how many did the model catch?

$$
\text{recall}=\frac{TP}{TP+FN}
$$

Prioritize recall when missing a positive case is especially harmful. Sensitivity is another name for recall or true-positive rate.

### Specificity

Specificity asks: of all actual negatives, how many did the model correctly leave negative?

$$
\text{specificity}=\frac{TN}{TN+FP}
$$

Specificity is the true-negative rate. The false-positive rate is $1-\text{specificity}$.

### F1 score

F1 is the harmonic mean of precision and recall:

$$
F1=2\times\frac{\text{precision}\times\text{recall}}{\text{precision}+\text{recall}}
$$

The harmonic mean becomes low when either precision or recall is low. F1 is useful as a compact balance, especially for imbalanced classes, but it ignores true negatives and does not encode the actual cost of each error.

## 7. Threshold selection is a product and risk decision

Lowering a binary threshold predicts more cases as positive. This usually increases recall and false positives. Raising it usually increases precision or specificity while creating more false negatives.

There is no universally correct value of 0.5. Choose an operating point using:

- false-positive and false-negative consequences;
- available human-review or intervention capacity;
- class base rates;
- calibration and subgroup behavior;
- legal, safety, and policy constraints; and
- metrics on validation data not used to train model parameters.

### Expected error cost

Suppose a false escalation costs 3 units and a missed late project costs 12 units. For 4 false positives and 2 false negatives:

$$
(4\times3)+(2\times12)=36\text{ cost units}
$$

This calculation makes assumptions explicit. Real costs may differ by case, include benefits for correct actions, or be uncertain. Treat the cost matrix as a reviewable decision model, not objective truth.

## 8. ROC and precision–recall curves sweep thresholds

A single confusion matrix describes one threshold. Threshold curves show behavior across many operating points.

### ROC curve

The receiver operating characteristic curve plots:

- vertical axis: true-positive rate, which is recall; and
- horizontal axis: false-positive rate, which is $FP\div(FP+TN)$.

ROC AUC summarizes how well the model ranks positives above negatives across thresholds. It does not select the production threshold, prove calibration, encode error costs, or guarantee good performance in the operating region you care about.

### Precision–recall curve

A precision–recall curve plots precision against recall across thresholds. It focuses on positive-class performance and is often more informative when positives are rare, because a large number of true negatives does not dominate the visual.

Compare curves on held-out data, then select an operating point from business consequences and constraints.

## 9. Train, validation, and test sets have different jobs

| Partition | Purpose | What may use its labels? |
|---|---|---|
| Training | Learn model parameters | Training process |
| Validation | Choose model design, hyperparameters, and threshold | Development decisions |
| Test | Estimate final generalization after choices are frozen | Final evaluation only |

Repeatedly choosing changes based on test results turns the test set into another validation set. Its reported performance becomes optimistic.

### Match the split to production

- **Random split:** reasonable only when examples are independent and exchangeable.
- **Chronological split:** train on the past and evaluate on the future when deployment predicts future events.
- **Group split:** keep all records from one customer, patient, device, or project in one partition.
- **Stratified split:** preserve rare-class representation where compatible with time and group constraints.

Real designs may require several constraints at once. Production similarity matters more than a convenient percentage.

## 10. Leakage makes validation fiction

Common forms include:

- **target leakage:** a feature directly or indirectly reveals the label;
- **temporal leakage:** future information is used to predict the past;
- **entity leakage:** related records from the same entity appear across partitions;
- **preprocessing leakage:** scaling, feature selection, imputation, or encoding is fit using validation or test data; and
- **test-set leakage:** model or threshold choices repeatedly adapt to final test results.

Leakage checks should ask:

1. When is every field created?
2. Could the field exist at the exact prediction moment?
3. Could related entities or near-duplicates cross partitions?
4. Which data fit every preprocessing step?
5. How many times have test results influenced development?

## 11. A defensible model evaluation is more than one score

Report:

- the target population and evaluation sample;
- base rates and class counts;
- the baseline and candidate model;
- split strategy and dates or entity boundaries;
- confusion matrix at the proposed threshold;
- precision, recall, specificity, F1, and operational cost as relevant;
- regression error in target units for numeric targets;
- calibration and uncertainty;
- slice metrics for important subgroups and operating conditions;
- leakage checks;
- normal and costly failure examples; and
- a keep, revise, or reject decision.

Metrics are evidence for a decision. They are not the decision by themselves.

## 12. Connections to modern AI systems

Classical supervised learning remains the right tool for many tasks:

| System need | Likely task |
|---|---|
| Forecast infrastructure demand | Regression |
| Detect fraud or abuse | Classification |
| Predict delivery duration | Regression |
| Route tickets or documents | Multiclass classification |
| Rank cases for human review | Classification score or ranking |
| Predict whether an LLM answer needs escalation | Classification |

LLM systems also use these ideas. Moderation, routing, quality prediction, reranking, intent detection, and automated evaluation often use classifiers. The same rules about base rates, calibration, leakage, thresholds, and held-out data still apply.

## Common failure modes

- Choosing an algorithm before defining the target and action.
- Using a field that appears only after the prediction moment.
- Reporting training performance as evidence of generalization.
- Skipping a naive baseline.
- Reporting accuracy without class counts or a confusion matrix.
- Assuming a 0.5 threshold is neutral or correct.
- Selecting a threshold on the final test set.
- Treating ROC AUC as calibration or production utility.
- Ignoring subgroup failures behind an acceptable aggregate.
- Treating a predictive relationship as causal.

## Interactive learning sequence

In [index.html](index.html):

1. Identify the prediction-time-safe feature.
2. Frame four tasks as regression or classification.
3. Compare a mean baseline, a useful linear trend, and an overfit curve.
4. Read regression metrics on unseen examples.
5. Move the classification threshold and watch the confusion matrix change.
6. Change false-positive and false-negative costs and observe the preferred threshold move.
7. Diagnose four safe or leaking evaluation designs.
8. Complete all eight knowledge checks.

## Gate A capstone: baseline decision model and evaluation worksheet

Complete [EXERCISES.md](EXERCISES.md) for the AI delivery advisor. The result must include:

- one regression target and one classification target;
- prediction unit, moment, horizon, and action;
- valid features and rejected leakage fields;
- a naive baseline for each task;
- chosen metrics and error costs;
- a production-realistic split strategy;
- a provisional classification threshold;
- sample, base-rate, uncertainty, calibration, and subgroup checks; and
- a keep, revise, or reject rule.

This completes Foundation Gate A: you can frame learning and evaluation, establish a baseline, select meaningful metrics, and detect obvious leakage. Later lessons will implement stronger models behind this preserved evaluation contract.

## Definition of done

- [ ] Complete the interactive browser lesson.
- [ ] Explain regression and classification from their target types.
- [ ] Interpret residuals, MAE, RMSE, and R².
- [ ] Reconstruct precision and recall from a confusion matrix.
- [ ] Use the threshold-and-cost lab to compare operating points.
- [ ] Explain why accuracy can fail on imbalanced data.
- [ ] Identify all four leakage examples correctly.
- [ ] Complete the eight knowledge checks.
- [ ] Produce the Gate A capstone artifact.
- [ ] Mark Lesson 5 complete on the course dashboard.

## Instructor and maintainer note

The repository retains `lab.py` and reusable course-lab code for automated verification and optional instructor demonstrations. They are not part of the learner path. A student can complete Lesson 5 without reading or editing Python.
