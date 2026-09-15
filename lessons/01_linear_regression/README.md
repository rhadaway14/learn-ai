# Lesson 01 — How Machines Learn

## Start here

This lesson requires no programming experience and shows no programming code.

Open [index.html](index.html) in a web browser. No installation, account, terminal, or internet connection is required. The page contains the complete lesson, interactive model, visualizations, guided experiments, and knowledge checks.

## What you will learn

By the end of the lesson, you should be able to explain:

- how machine learning differs from ordinary rule-based programming;
- features, labels, models, predictions, parameters, and hyperparameters;
- why a straight line can act as a predictive model;
- how weight and bias change that line;
- why a model needs a numerical measure of error;
- what mean squared error measures and why errors are squared;
- what information a gradient provides;
- how learning rate affects gradient descent;
- how training differs from inference;
- why training and test data must remain separate;
- what noise, underfitting, overfitting, and data leakage mean;
- which parts of this small example also appear in neural networks and LLMs.

## The central idea

In traditional programming, people specify a relationship as rules. In machine learning, people provide examples and a learning process estimates a useful relationship.

This lesson uses examples containing one input and one known answer. The model is a movable straight line. Training adjusts the line until its predictions are less wrong across the examples.

Learning therefore has a precise meaning here: finding numerical settings that reduce prediction error. It does not imply that the model understands the problem like a person.

## The model in plain language

The line has two learned settings:

| Setting | What it changes |
|---|---|
| Weight | Tilts the line; controls how much the prediction changes when the input increases |
| Bias | Moves the whole line up or down; controls the prediction when the input is zero |

The model performs this calculation:

> prediction = weight × input + bias

The compact mathematical version is:

$$
\hat{y}=wx+b
$$

Read the symbols as vocabulary:

| Symbol | Read it as | Meaning |
|---|---|---|
| $x$ | x | Input feature given to the model |
| $y$ | y | Correct answer or label |
| $\hat{y}$ | y-hat | Model prediction |
| $w$ | w | Learned weight |
| $b$ | b | Learned bias |

The equation is not an additional concept. It is simply a shorter way to write the plain-language calculation above.

## A worked prediction

Suppose:

- weight is `3.5`;
- input is `4`;
- bias is `2`.

Then:

1. Multiply weight by input: `3.5 × 4 = 14`.
2. Add the bias: `14 + 2 = 16`.
3. The prediction is `16`.

No learning occurred during this calculation. This is a forward pass: the current model was used to make one prediction.

## From one error to one loss

The model needs feedback. For each example, compare its prediction with the correct answer. The difference is a residual error.

If the correct answer is `10` and the prediction is `7`, the prediction is off by `3`.

A dataset contains many residual errors, so training needs one score that summarizes all of them. Mean squared error, or MSE, does this:

1. Find each prediction's difference from its correct answer.
2. Square each difference.
3. Average the squared differences.

In plain language:

> MSE = average of all (prediction − correct answer)²

Squaring serves two purposes:

- errors above and below the correct answer cannot cancel each other;
- large errors receive much more weight than small errors.

The second property is both useful and a limitation. A single extreme outlier can affect MSE substantially. The interactive lab lets you observe that behavior.

Lower loss means better performance on the measured examples. It does not automatically mean the model is useful, fair, safe, or appropriate for a real decision.

## From loss to learning

Knowing that the model is wrong is not enough. Training also needs to know how to adjust weight and bias.

A gradient answers a local “what if?” question:

> If this parameter increases slightly, which direction will the loss move, and how strongly?

The sign gives direction:

| Gradient | Meaning | Training response |
|---|---|---|
| Positive | Increasing the parameter would increase loss | Decrease the parameter |
| Negative | Increasing the parameter would decrease loss | Increase the parameter |
| Near zero | A small change has little local effect | Make little or no adjustment |

The gradient does not reveal the final best answer. It provides a useful next step. The model improves by taking many steps.

## Learning rate

The learning rate controls the size of each adjustment:

- **Too small:** loss may improve, but training takes many steps.
- **Balanced:** loss falls steadily toward a useful result.
- **Too large:** updates overshoot, oscillate, or grow unstable.

This distinction is central:

- weight and bias are **parameters learned by the model**;
- learning rate and training steps are **hyperparameters selected by a person**.

## The complete learning cycle

Training repeatedly performs four operations:

1. **Predict:** use the current weight and bias.
2. **Measure:** calculate loss from known answers.
3. **Evaluate direction:** calculate gradients.
4. **Adjust:** update weight and bias in the direction expected to lower loss.

One pass through the available training examples is an epoch. The interactive lesson calls these training steps to keep the first encounter approachable; later lessons refine the terminology and introduce batches.

## Training versus inference

During **training**, examples with known answers are used to change model parameters.

During **inference**, the learned parameters stay fixed and the model predicts an answer for a new input.

This distinction appears throughout AI:

- training is usually expensive and repeated over a large dataset;
- inference is the operation used when an application asks a trained model for a result.

## Why some data stays hidden

If a learner studies an answer key and then receives exactly the same questions on the exam, the score does not show how well the learner handles new problems. Models have the same issue.

The lab reserves approximately:

- 80% of examples for training;
- 20% as unseen test data.

**Generalization** means performing well on new examples rather than merely the training examples. Allowing test information to influence training is **data leakage**, which makes measured performance unrealistically optimistic.

In larger projects, a validation set is also used to compare designs and select hyperparameters. The final test set remains untouched until the design is settled.

## Noise and model capacity

Real observations vary for reasons a model may not receive as inputs. That unexplained variation is represented as noise.

More training cannot recover information that is absent from the input. Increasing the number of representative examples can improve the estimate, but irreducible uncertainty remains.

Model capacity is a separate limitation. A straight-line model cannot perfectly represent a curved relationship. Training it longer only finds a better straight-line compromise. This is **underfitting**: the model form is too limited for the pattern.

## Guided lab sequence

Use the controls in [index.html](index.html), changing one at a time.

### 1. Establish a baseline

Select **Reset baseline**, then **Train model**. Observe:

- learned weight and bias;
- training and test loss;
- alignment between the line and the points;
- the way loss changes over training.

### 2. Change step size

Move learning rate very low, then very high. Predict the loss curve before training each time.

### 3. Change the amount of evidence

Compare 10 examples with 500. Reset and repeat the experiment. A larger representative sample should produce a more stable estimate.

### 4. Add uncertainty

Increase noise. Notice that the broad trend remains learnable while individual predictions become less certain.

### 5. Add an outlier

Enable the extreme outlier. Observe the learned line and loss. Connect the result to MSE's emphasis on large errors.

### 6. Exceed model capacity

Select curved data. The model still learns the best line it can, but systematic error remains.

For every experiment, record:

| Prompt | Your response |
|---|---|
| What did I change? | |
| What did I predict? | |
| What happened? | |
| Why did it happen? | |
| What stayed constant? | |

## Connection to modern AI

The scale changes dramatically, but the learning structure transfers:

| This lesson | Language model |
|---|---|
| Numeric input | Sequence of tokens |
| Two learned parameters | Billions of learned parameters |
| Numeric prediction | Probabilities for the next token |
| Mean squared error | Usually cross-entropy loss |
| Gradient descent | Gradient-based optimizers |
| Predict on new data | Generate or score new tokens |

An LLM is not merely a larger linear-regression line. It is a much richer function built from many layers. The shared idea is a parameterized model improved by measuring errors and following gradients.

## Knowledge checkpoint

Explain these in your own words:

1. What does machine learning learn that rule-based programming usually specifies?
2. How do a feature, label, prediction, and model differ?
3. What does weight do to the line? What does bias do?
4. Why is loss necessary?
5. Why does MSE square errors, and what limitation follows?
6. What two kinds of information does a gradient provide?
7. Why does training move opposite the gradient?
8. What happens when learning rate is too small or too large?
9. How does training differ from inference?
10. Why must final evaluation use unseen examples?
11. What is data leakage?
12. Why can more training not eliminate noise?
13. Why can a straight line not perfectly represent curved data?

## Speak about it confidently

Plain-language version:

> Machine learning uses examples to estimate a useful relationship. The model makes predictions, measures its errors, and repeatedly adjusts its internal settings in a direction expected to reduce those errors. We then evaluate it on unseen examples to learn whether the pattern generalizes.

Technical version:

> Linear regression models a continuous target as a weighted input plus bias. Training minimizes mean squared error through gradient-based parameter updates. A held-out test set estimates generalization, while controlled experiments expose sensitivity to learning rate, sample size, noise, outliers, and model capacity.

## Definition of done

- [ ] Complete the browser lesson from beginning to end.
- [ ] Run all four guided UI experiments.
- [ ] Answer all three embedded knowledge checks correctly.
- [ ] Explain weight and bias without using an equation.
- [ ] Explain loss, gradient, and learning rate in your own words.
- [ ] Explain why test data must remain unseen during training.
- [ ] Explain why noise and insufficient model capacity are different problems.
- [ ] Answer the written checkpoint questions.

## Instructor note

The learner-facing path is the browser lesson. The repository retains a separate tested numerical reference implementation for maintainers, but learners are not asked to read, edit, or run it.
