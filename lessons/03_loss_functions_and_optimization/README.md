# Lesson 03 — Loss Functions and Optimization

## Start here

Launch Lesson 3 from the course dashboard or open [index.html](index.html). The complete learner-facing lesson runs in a browser with no programming environment, terminal, account, or internet connection.

This lesson answers four questions:

1. How does training turn many mistakes into one measurable objective?
2. Why do different loss functions produce different behavior?
3. How does a gradient indicate a direction for improvement?
4. Why do learning rate and batch size change whether training succeeds?

## Prerequisites

You should be able to:

- distinguish a prediction from its correct target;
- explain that model parameters change during training;
- understand a scalar as one number;
- read simple vectors and shapes from Lesson 2;
- add, subtract, multiply, square, and average ordinary numbers.

No calculus or programming background is assumed. Gradients are introduced through slope and controlled experiments before symbolic notation.

## Learning outcomes

After completing the lesson, you should be able to:

- distinguish error, loss, objective, and evaluation metric;
- calculate MAE and MSE for a small set of predictions;
- explain why MSE reacts strongly to outliers;
- explain how cross-entropy treats probability assigned to the correct class;
- interpret gradient sign and magnitude;
- explain analytical gradients and finite-difference checks;
- perform one gradient-descent update by hand;
- diagnose learning rates that are too small, useful, oscillating, or divergent;
- compare full-batch, stochastic, and mini-batch gradient descent;
- define an optimization and evaluation contract for the capstone.

## 1. Training needs a measurable objective

A model can make thousands of predictions, each with its own error. Training requires one scalar that summarizes how undesirable the current behavior is. That scalar is the **loss**.

Think of loss as a scoreboard. “Improve” is not measurable. “Reduce this score calculated by this exact rule” is measurable.

The metaphor has an important limit: a scoreboard represents only the behavior included in its rules. A decreasing loss does not automatically prove that a model is fair, safe, robust, well calibrated, or useful to the business.

### Vocabulary

| Term | Meaning | Delivery-time example |
|---|---|---|
| Prediction | Value produced by the model | 42 minutes |
| Target or label | Correct value supplied by the data | 50 minutes |
| Error | Difference between prediction and target | 8 minutes |
| Loss | Penalty produced by a defined rule | 8 with absolute error; 64 with squared error |
| Objective | Quantity training is instructed to optimize | Average loss, possibly plus penalties |
| Evaluation metric | Evidence used to judge the trained system | MAE, worst-case delay, cost, latency, fairness |

### Loss is not automatically the business metric

Training losses are often selected partly because they provide useful gradients. Release decisions need metrics connected to the actual task.

For example, a fraud classifier may train with cross-entropy while the production decision also considers fraud dollars prevented, false declines, recall on high-value fraud, latency, and calibration across important groups.

The loss teaches the model. The evaluation suite decides whether the result should ship.

## 2. Regression losses: MAE and MSE

Regression predicts a number, such as delivery time, energy consumption, price, or demand.

Suppose actual values are `[3, 5, 7, 9]` and predictions are `[2, 6, 8, 9]`. The absolute errors are `[1, 1, 1, 0]`.

### Mean Absolute Error

Question answered:

> On average, how large are the mistakes, ignoring direction?

With actual numbers:

> MAE = (1 + 1 + 1 + 0) ÷ 4 = 0.75

Symbolically:

$$
MAE=\frac{1}{N}\sum_{i=1}^{N}|\hat{y}_i-y_i|
$$

`N` is the number of examples, `y` is the target, `ŷ` is the prediction, and the vertical bars mean absolute value. MAE applies a steady penalty: doubling an error doubles its contribution.

### Mean Squared Error

Question answered:

> What is the average squared size of the mistakes?

With the same data:

> MSE = (1² + 1² + 1² + 0²) ÷ 4 = 0.75

Symbolically:

$$
MSE=\frac{1}{N}\sum_{i=1}^{N}(\hat{y}_i-y_i)^2
$$

MSE makes large errors disproportionately influential. If the final prediction changes from 9 to 21, its error is 12: it contributes 12 to MAE but 144 to MSE before averaging.

### Metaphor: two late-fee policies

- MAE charges one dollar for every minute late.
- MSE charges the square of minutes late.

MSE therefore treats one disastrous miss as potentially more important than several modest misses. The correct policy depends on real consequences and data quality.

| Prefer considering MAE when… | Prefer considering MSE when… |
|---|---|
| error magnitude has roughly linear cost | large misses are disproportionately costly |
| target data contains legitimate extreme values | smooth gradients are especially useful |
| interpretability in original units matters | the conditional mean is the desired estimate |

Neither loss is universally superior. Investigate outliers rather than choosing MAE solely to hide them or MSE solely to punish them.

## 3. Classification loss: cross-entropy

A classifier often produces a probability distribution over categories. Cross-entropy asks how much probability the model assigned to the correct category.

For one correct category:

$$
loss=-\ln(p_{correct})
$$

Read it in words: take the probability assigned to the correct answer, apply the natural logarithm, then negate the result.

You do not need logarithm fluency to understand the behavior:

| Probability assigned to correct class | Cross-entropy loss | Interpretation |
|---:|---:|---|
| 0.99 | 0.010 | Confident and correct; tiny penalty |
| 0.80 | 0.223 | Correct class favored; small penalty |
| 0.50 | 0.693 | Uncertain between alternatives |
| 0.10 | 2.303 | Correct class given little probability |
| 0.01 | 4.605 | Confidently wrong; severe penalty |

Cross-entropy is relevant to image classification, fraud probability, document routing, and next-token prediction in language models. A cross-entropy value is not a percentage and is not directly meaningful without a consistent dataset and setup.

## 4. Loss surfaces and gradients

If a model has one parameter, draw parameter value horizontally and loss vertically. The result is a loss curve. With two parameters it becomes a surface. Real networks have enormous high-dimensional loss landscapes that cannot be drawn directly.

### Metaphor: hiking downhill in fog

You cannot see the entire mountain, but you can feel the slope beneath your feet. The local slope indicates which direction rises and how steeply. To descend, step in the opposite direction.

The metaphor stops being literal because a model may have billions of independent parameter directions. It also encounters saddle points, plateaus, noisy estimates, and complex curvature.

### Gradient sign and magnitude

- A **positive gradient** means increasing the parameter locally increases loss.
- A **negative gradient** means increasing the parameter locally decreases loss.
- A gradient near zero means the surface is locally flat.

A zero gradient does not guarantee the global best solution. It may indicate a local minimum, local maximum, saddle point, or flat plateau.

Magnitude describes local sensitivity. A magnitude of 10 means a small parameter change is associated with a larger local loss change than a magnitude of 0.1. Gradient magnitude is not a safe step size by itself; the learning rate controls the update.

## 5. Analytical gradients and finite differences

An **analytical gradient** comes from differentiation rules applied to the exact operations that produced loss.

A **finite-difference estimate** probes loss slightly to the left and right:

$$
\frac{dL}{dw}\approx\frac{L(w+h)-L(w-h)}{2h}
$$

`L` is the loss function, `w` is the parameter, and `h` is a small probe distance. The numerator is the change in loss; `2h` is the distance between probe points.

This is like estimating a road's grade from two nearby elevation measurements.

Finite differences are valuable for checking an implementation. They are not the normal way to train a large model because every checked parameter requires extra loss calculations. Backpropagation computes analytical gradients much more efficiently.

The probe distance has a tradeoff: too large averages across too much of the curve; too small can expose floating-point cancellation. Agreement across sensible probe sizes is evidence, not absolute proof, that a gradient is correct.

### Must every loss be differentiable everywhere?

Gradient methods need a usable slope at the current point, but a loss does not need to be perfectly smooth everywhere. MAE has a sharp corner when error is zero. Libraries commonly use a defined **subgradient** at that corner. Neural networks also use piecewise operations such as ReLU.

The practical requirement is that the system can produce useful update directions for the operations it encounters. Smooth losses often make optimization easier, but one non-differentiable point does not automatically make a loss unusable.

## 6. Gradient descent

Gradient descent repeats this update:

$$
w_{new}=w_{old}-\eta\frac{dL}{dw}
$$

`w` is a model parameter, `L` is loss, `dL/dw` is the gradient, and `η` is the learning rate.

### Complete numeric example

Use the toy objective `loss = (weight − 4)²`. At weight −1, loss is 25 and the gradient is −10.

With learning rate 0.15:

> new weight = −1 − (0.15 × −10) = 0.5

The new loss is `(0.5 − 4)² = 12.25`. One update reduced loss from 25 to 12.25.

## 7. Learning rate controls update size

The gradient proposes a direction and sensitivity. The learning rate decides how far to move.

### Metaphor: adjusting a shower

Tiny handle adjustments are safe but may take too long. An enormous adjustment overshoots the desired temperature, causing increasingly frantic corrections. Useful changes approach the target without destructive oscillation.

| Learning rate | Expected behavior in the lesson's toy objective |
|---:|---|
| 0.001 | Stable but painfully slow |
| 0.15 | Smooth, useful convergence |
| 0.7 | Crosses the minimum repeatedly, but oscillations shrink |
| 1.1 | Overshoots with increasing error; divergence |

### Diagnose from trajectories

- **Stalled:** loss barely changes and gradients remain meaningful. The learning rate may be too small.
- **Oscillating but converging:** the parameter crosses the valley while loss trends down.
- **Diverging:** parameter magnitude and loss grow, often rapidly or non-finitely.
- **Sudden spikes:** the rate may be too aggressive, a batch may be unusual, or numeric instability may be present.

Useful telemetry includes training loss, validation loss, gradient norms, parameter and update norms, non-finite batches, and learning rate over time.

## 8. Full-batch, stochastic, and mini-batch descent

The full training dataset may contain millions of examples. Training must decide how many examples contribute to each gradient estimate.

A **step** is one parameter update. An **epoch** is one pass through all training examples. With 12 examples:

- batch size 12 produces 1 step per epoch;
- batch size 4 produces 3 steps per epoch;
- batch size 1 produces 12 steps per epoch.

### Customer-feedback metaphor

- Reading every survey before acting resembles **full-batch** descent.
- Reacting after one survey resembles **stochastic** descent.
- Reviewing groups of surveys resembles **mini-batch** descent.

The analogy explains stability versus responsiveness. It does not capture mathematical averaging or the importance of accelerator memory and throughput.

| Strategy | Examples per update | Strength | Tradeoff |
|---|---:|---|---|
| Full batch | Entire dataset | Stable, deterministic gradient | Expensive and infrequent updates |
| Stochastic | 1 | Frequent updates; noisy exploration | Erratic path and weak hardware efficiency |
| Mini-batch | A manageable subset | Practical balance | Adds batch-size and sampling decisions |

Mini-batch training is standard for neural networks because matrix hardware processes batches efficiently and moderate gradient noise can be useful. Batch size interacts with learning rate; it is not merely a memory setting.

## 9. Common failures and diagnostic responses

### Loss improves but the real outcome does not

The objective measures the wrong behavior. Define business-facing validation metrics and inspect representative errors.

### Outliers dominate MSE

A few examples account for most loss or gradient magnitude. Verify data, understand the outliers, compare MAE or robust losses, and report tail behavior.

### Learning rate is too small

Loss is stable but progress per unit time is negligible. Inspect gradient and update magnitudes, then test a controlled range of larger rates.

### Learning rate is too large

Loss oscillates or grows; parameters may become infinite or not-a-number. Stop, restore a safe checkpoint, lower the rate, and inspect scaling and problematic batches.

### Training loss falls while validation loss rises

The model fits training examples without improving unseen behavior. Preserve the split, investigate overfitting and leakage, and never tune on the test set.

## 10. Connections to modern AI

These primitives survive at every scale:

- language-model pretraining minimizes next-token cross-entropy;
- instruction tuning optimizes objectives over desired responses;
- image models use classification, contrastive, or diffusion-related losses;
- embedding models use objectives that arrange related and unrelated examples;
- optimizers such as SGD and Adam turn gradients into parameter updates;
- distributed training combines gradient estimates across accelerators.

Frameworks automate gradient calculation and parameter updates. They do not choose the right objective, data, validation design, or release metric for you.

## 11. Interactive practice sequence

Complete these in [index.html](index.html):

1. Distinguish prediction, error, loss, objective, and metric.
2. Move one outlier and compare MAE with MSE.
3. Change correct-class probability and inspect cross-entropy.
4. Move across a loss curve and interpret gradient sign.
5. Compare analytical and finite-difference gradients.
6. Work through one complete gradient-descent update.
7. Compare learning rates 0.001, 0.15, 0.7, and 1.1.
8. Group examples into full, mini, and stochastic batches.
9. Complete all knowledge checks.

## 12. Capstone increment

Create an **optimization and evaluation contract** for the future AI delivery advisor. Record:

- one prediction the system could learn to produce;
- its target or expected answer;
- one candidate training loss and the behavior it rewards;
- evaluation metrics tied to real usefulness;
- the cost of an important false positive and false negative;
- one normal example and one costly failure example;
- telemetry indicating convergence, stalled progress, and divergence;
- why falling training loss alone would not authorize release.

This becomes part of the baseline decision model and evaluation worksheet completed across Lessons 3–5.

## Knowledge checkpoint

1. How do error, loss, objective, and evaluation metric differ?
2. Why does MSE react more strongly to one large error than MAE?
3. When might MAE be more appropriate than MSE?
4. What behavior does cross-entropy reward?
5. Why is cross-entropy not a confidence percentage?
6. What do gradient sign and magnitude describe?
7. Why does gradient descent subtract the gradient?
8. What can a finite-difference check reveal?
9. How do you recognize a learning rate that is too small or too large?
10. Why are mini-batches common in neural-network training?
11. Why can lower training loss still produce a worse product?

## Speak about it confidently

Plain-language version:

> Training needs a numeric definition of error. The gradient measures how that loss changes near the current parameters, and the optimizer uses that information to make repeated updates. The loss function, learning rate, and batch strategy each shape what the model learns and whether training is stable.

Technical version:

> A differentiable scalar objective maps model outputs and targets to loss. Analytical gradients provide local sensitivity for each parameter, while finite differences offer an implementation check. Gradient descent applies learning-rate-scaled updates opposite the gradient. MAE, MSE, and cross-entropy encode different error priorities, and mini-batch sampling trades gradient variance against memory and throughput.

## Definition of done

- [ ] Complete every browser interaction.
- [ ] Calculate one MAE and MSE example by hand.
- [ ] Explain cross-entropy behavior without relying on the formula.
- [ ] Interpret gradient sign and magnitude on the loss landscape.
- [ ] Explain a finite-difference gradient check.
- [ ] Diagnose all four learning-rate trajectories.
- [ ] Compare full-batch, stochastic, and mini-batch descent.
- [ ] Answer all knowledge checks correctly.
- [ ] Produce the capstone optimization and evaluation contract.
- [ ] Mark Lesson 3 complete in the course dashboard.

## Instructor note

The browser lesson is the primary learner path. Python files remain deterministic maintainer references and are not required reading or execution for learners at this stage.
