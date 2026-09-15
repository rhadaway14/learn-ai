# Lesson 01 — Machine Learning and Linear Regression

## Why this lesson matters

Machine learning looks mysterious when the first example is a neural network with millions of parameters. Linear regression removes that mystery. It is small enough to understand completely, yet it contains the same core training cycle used by much larger models:

1. make predictions from inputs;
2. compare predictions with correct answers;
3. calculate how each parameter contributed to the error;
4. adjust the parameters;
5. repeat and evaluate on unseen data.

Later, a transformer will have far more parameters and produce token probabilities rather than one number. The basic learning process is still prediction, loss, gradients, and parameter updates.

## Learning outcomes

After this lesson, you should be able to:

- distinguish AI, machine learning, and deep learning;
- explain supervised learning and regression;
- distinguish training from inference;
- identify features, labels, predictions, parameters, and hyperparameters;
- explain loss and gradient descent;
- explain why test data must be separated from training data;
- train and evaluate linear regression using NumPy;
- recognize slow learning, divergence, noise, underfitting, and overfitting.

## 1. Where machine learning fits

**Artificial intelligence** is the broad field of building systems that perform tasks associated with intelligent behavior. It includes rules, search, planning, optimization, machine learning, and other approaches.

**Machine learning** learns patterns from data instead of requiring a developer to explicitly program every rule. **Deep learning** is machine learning based on multilayer neural networks. An LLM is therefore a deep-learning model inside machine learning inside the broader field of AI. AI and LLM are not synonyms.

## 2. Traditional programming versus machine learning

Traditional programming supplies the rules:

```text
rules + data → program → answer
```

```python
def shipping_cost(weight: float) -> float:
    return 8 if weight < 5 else 12
```

During supervised machine-learning training, we supply examples with correct answers:

```text
examples + correct answers → training → learned model
```

We then use that model on new inputs:

```text
new input + trained model → inference → prediction
```

Machine learning does not eliminate programming. Engineers still define the data pipeline, model form, objective, evaluation, deployment, and safety boundaries.

## 3. Supervised learning and regression

Each example in **supervised learning** contains an input and a correct target:

- a **feature**, `x`;
- a **label**, `y`.

| Feature | Label |
|---|---|
| Square footage | House price |
| Advertising spend | Sales revenue |
| Temperature | Energy consumption |

This is a **regression** problem because its output is a continuous number. Predicting a category such as `fraud` or `not fraud` would be **classification**.

## 4. A model is a parameterized function

Our model is a straight line:

$$
\hat{y}=wx+b
$$

The hat in $\hat{y}$, pronounced “y-hat,” means predicted value.

| Symbol | Meaning |
|---|---|
| $x$ | Input feature |
| $y$ | Correct label |
| $\hat{y}$ | Prediction |
| $w$ | Weight or slope |
| $b$ | Bias or intercept |

The weight says how much the prediction changes when `x` rises by one. The bias is the prediction when `x` is zero.

For $\hat{y}=3.5x+2$ and `x = 4`:

$$
\hat{y}=3.5(4)+2=16
$$

`w` and `b` are **parameters** learned during training. By contrast, **hyperparameters** are choices made by the engineer.

| Type | Selected by | Examples |
|---|---|---|
| Parameter | Training | `w`, `b` |
| Hyperparameter | Engineer | learning rate, epochs, sample count |

A model with billions of parameters does not have billions of manually configured settings. Optimization learns their values.

## 5. The dataset and noise

The lab generates data from a hidden relationship:

$$
y=3.5x+2+\epsilon
$$

$\epsilon$ is random **noise**, representing measurement error or factors not captured by `x`.

```python
x = rng.uniform(0, 10, samples)
noise = rng.normal(0, 1.5, samples)
y = 3.5 * x + 2 + noise
```

The model sees only `x` and `y`; it is never told `3.5` or `2`. Because of noise, no line can pass through every point. A useful model captures the underlying trend rather than every random deviation.

## 6. Training, validation, and test data

The program shuffles the examples into:

- 160 **training examples** used to learn `w` and `b`;
- 40 **test examples** hidden until final evaluation.

A model can perform well on examples it has seen without learning a general pattern. Performance on unseen data measures **generalization**.

Larger projects normally use three splits:

| Split | Purpose |
|---|---|
| Training | Learn parameters |
| Validation | Choose hyperparameters and models |
| Test | Estimate final unseen performance |

Allowing test information to influence training is **data leakage**. It produces an unrealistically optimistic evaluation.

## 7. The forward pass

Training starts with `w = 0` and `b = 0`. The model calculates predictions for every input:

```python
predictions = w * x + b
```

This is the **forward pass**. Initially every prediction is zero. Wrong predictions are expected—they provide an error the algorithm can measure and learn from.

## 8. Error and mean squared error

For one example, the residual error is:

$$
e=\hat{y}-y
$$

```python
errors = predictions - y
```

A **loss function** combines the errors into one objective. This lab uses mean squared error:

$$
MSE=\frac{1}{N}\sum_{i=1}^{N}(\hat{y}_i-y_i)^2
$$

MSE subtracts each label from its prediction, squares each result, and takes the mean. Squaring prevents positive and negative errors from cancelling and penalizes large mistakes more heavily. That latter property also makes MSE sensitive to outliers.

Loss guides optimization; it is not automatically the best business metric. Production evaluation may also require absolute error, percentiles, fairness, latency, reliability, or cost.

## 9. Gradients: what should change?

A **gradient** measures how loss changes when a parameter changes. It tells us:

- the direction in which loss increases;
- how sensitive loss is to that parameter.

For this model and MSE:

$$
\frac{\partial L}{\partial w}=\frac{2}{N}\sum(\hat{y}_i-y_i)x_i
$$

$$
\frac{\partial L}{\partial b}=\frac{2}{N}\sum(\hat{y}_i-y_i)
$$

The code is the direct translation:

```python
dw = 2 * np.mean(errors * x)
db = 2 * np.mean(errors)
```

You do not need to memorize the derivation yet. Understand that the sign gives direction, the magnitude gives local sensitivity, and moving oppositely should lower loss.

## 10. Gradient descent

Gradient descent subtracts a scaled gradient:

$$
w_{new}=w_{old}-\eta\frac{\partial L}{\partial w}
$$

$$
b_{new}=b_{old}-\eta\frac{\partial L}{\partial b}
$$

$\eta$, eta, is the **learning rate**:

```python
w -= learning_rate * dw
b -= learning_rate * db
```

Think of parameters as coordinates on a loss surface. The gradient points uphill, so subtracting it moves downhill.

- Too small: stable but very slow learning.
- Appropriate: smooth convergence.
- Too large: overshooting, oscillation, or divergence.

Linear regression with MSE has a convex, bowl-shaped loss surface. Unlike many deep-network objectives, it has one global minimum rather than many competing local minima.

## 11. The complete training loop

An **epoch** is one complete pass through the training data. This lab uses every example for each update, called batch gradient descent.

```python
for epoch in range(epochs):
    predictions = w * x + b       # forward pass
    errors = predictions - y      # residuals
    loss = np.mean(errors**2)      # objective
    dw = 2 * np.mean(errors * x)   # weight gradient
    db = 2 * np.mean(errors)       # bias gradient
    w -= learning_rate * dw        # update parameters
    b -= learning_rate * db
```

The reusable mental model is:

```text
predict → measure loss → calculate gradients → update parameters → repeat
```

PyTorch will later calculate gradients automatically, but it does not change the meaning of this loop.

## 12. One update by hand

Suppose `x = 2`, `y = 10`, and both parameters start at zero.

$$
\hat{y}=0(2)+0=0
$$

$$
e=0-10=-10, \qquad L=(-10)^2=100
$$

For this single example:

$$
dw=2ex=2(-10)(2)=-40
$$

$$
db=2e=-20
$$

With learning rate `0.01`:

$$
w_{new}=0-0.01(-40)=0.4
$$

$$
b_{new}=0-0.01(-20)=0.2
$$

The next prediction becomes `1.0`. It is still wrong, but it moved from `0` toward `10`. Repeated updates across many examples find parameters that fit the dataset as a whole.

## 13. Evaluation and inference

After training, the model predicts labels for the test set:

```python
test_predictions = w * x_test + b
test_loss = np.mean((test_predictions - y_test) ** 2)
```

No parameters are updated. This is **inference**: using learned parameters to make predictions.

The saved figure shows the learned line over unseen test points and the training loss by epoch. A healthy loss curve drops sharply and then flattens. Parameters should approach `w = 3.5` and `b = 2`, but finite noisy data prevents an exact result.

## 14. Run the lab

Treat `train.py` as laboratory equipment. **Do not edit its source code for this lesson.** Change an experiment by passing command-line options, so every run is visible, reproducible, and easy to compare.

From the repository root, run the baseline:

```bash
python lessons/01_linear_regression/train.py
```

Ask the program to list every available control:

```bash
python lessons/01_linear_regression/train.py --help
```

The options fall into three categories:

| Category | Options | What they control |
|---|---|---|
| Training hyperparameters | `--learning-rate`, `--epochs` | How the model learns |
| Dataset configuration | `--samples`, `--noise`, `--data-seed`, `--true-weight`, `--true-bias`, `--relationship`, `--outlier` | What evidence the model receives |
| Evaluation configuration | `--train-size`, `--split-seed` | Which examples are used for learning and testing |

These command-line values are experiment controls. `w` and `b` inside the model are still the learned parameters. That distinction prevents the overloaded phrase “change the parameters” from becoming confusing.

Every run prints its complete configuration, learned model, and test loss. Use `--output-name` to keep plots from different runs:

```bash
python lessons/01_linear_regression/train.py \
  --learning-rate 0.001 \
  --epochs 500 \
  --output-name slow-learning.png
```

PowerShell accepts the command on one line, or uses a backtick for line continuation:

```powershell
python lessons/01_linear_regression/train.py `
  --learning-rate 0.001 `
  --epochs 500 `
  --output-name slow-learning.png
```

Plots are written under:

```text
lessons/01_linear_regression/outputs/
```

Locate every concept in the program:

| Code | Concept |
|---|---|
| `x` | Feature |
| `y` | Label |
| `w`, `b` | Parameters |
| `learning_rate`, `epochs` | Hyperparameters |
| `w * x + b` | Model and forward pass |
| `errors` | Residuals |
| `np.mean(errors**2)` | Loss |
| `dw`, `db` | Gradients |
| `w -= ...`, `b -= ...` | Optimization |
| Repeated loop | Training |
| Held-out examples | Test set |
| Final predictions | Inference |

## 15. Experiments: learn by breaking it

For each experiment:

1. run the baseline first;
2. predict what will change;
3. run the provided command without modifying Python;
4. compare final `w`, `b`, training-loss shape, test loss, and fitted line;
5. explain the causal relationship rather than merely reporting that numbers changed.

### Experiment A — Learning rate

```powershell
python lessons/01_linear_regression/train.py --learning-rate 0.00001 --output-name lr-tiny.png
python lessons/01_linear_regression/train.py --learning-rate 0.001 --output-name lr-small.png
python lessons/01_linear_regression/train.py --learning-rate 0.01 --output-name lr-baseline.png
python lessons/01_linear_regression/train.py --learning-rate 0.1 --output-name lr-large.png
python lessons/01_linear_regression/train.py --learning-rate 1.0 --output-name lr-extreme.png
```

Look for slow convergence, smooth convergence, overshooting, and exploding values. If the extreme run prints `inf` or `nan`, that is an observed result rather than a broken lab.

### Experiment B — Number of epochs

```powershell
python lessons/01_linear_regression/train.py --epochs 1 --output-name epochs-1.png
python lessons/01_linear_regression/train.py --epochs 10 --output-name epochs-10.png
python lessons/01_linear_regression/train.py --epochs 100 --output-name epochs-100.png
python lessons/01_linear_regression/train.py --epochs 2000 --output-name epochs-2000.png
```

This isolates training duration. Identify where the model is undertrained and where additional epochs provide almost no improvement.

### Experiment C — Noise

```powershell
python lessons/01_linear_regression/train.py --noise 0 --output-name noise-0.png
python lessons/01_linear_regression/train.py --noise 4 --output-name noise-4.png
python lessons/01_linear_regression/train.py --noise 8 --output-name noise-8.png
```

Noise changes the problem, not the optimizer. Ask why longer training cannot eliminate uncertainty that the feature does not explain.

### Experiment D — Dataset size

```powershell
python lessons/01_linear_regression/train.py --samples 10 --train-size 8 --output-name samples-10.png
python lessons/01_linear_regression/train.py --samples 50 --train-size 40 --output-name samples-50.png
python lessons/01_linear_regression/train.py --samples 200 --train-size 160 --output-name samples-200.png
python lessons/01_linear_regression/train.py --samples 2000 --train-size 1600 --output-name samples-2000.png
```

Run the 10-sample case again with `--data-seed 10`, then `--data-seed 20`. Compare that variability with the 2,000-sample runs.

### Experiment E — Training/test split

```powershell
python lessons/01_linear_regression/train.py --train-size 10 --split-seed 7 --output-name train-10.png
python lessons/01_linear_regression/train.py --train-size 100 --split-seed 7 --output-name train-100.png
python lessons/01_linear_regression/train.py --train-size 190 --split-seed 7 --output-name train-190.png
```

More training data leaves less test data. Explain why both an undersized training set and an undersized evaluation set can create uncertainty.

### Experiment F — Outlier sensitivity

```powershell
python lessons/01_linear_regression/train.py --outlier 0 --output-name outlier-none.png
python lessons/01_linear_regression/train.py --outlier 100 --output-name outlier-100.png
```

MSE squares errors, so one extreme label can exert substantial influence. Observe which learned parameter and which part of the line changes most.

### Experiment G — Recover a different hidden relationship

```powershell
python lessons/01_linear_regression/train.py --true-weight 7 --true-bias -4 --noise 0 --output-name different-line.png
```

The training code has not been told the answer through `w` and `b`; it receives examples generated from this relationship and must learn it.

### Experiment H — Wrong model form

```powershell
python lessons/01_linear_regression/train.py --relationship quadratic --output-name quadratic-data.png
```

The dataset is now curved while the model remains a straight line. More epochs optimize the available line; they cannot give the model capacity it does not possess.

Record each experiment:

```markdown
### Experiment

Hypothesis:
Change made:
Expected result:
Actual result:
Explanation:
```

## 16. Common failure modes

### Loss becomes `inf` or `nan`

The learning rate is probably causing increasingly extreme updates.

### Loss barely changes

The learning rate may be too small, the epoch count too low, or feature scales poorly conditioned.

### Training looks good but unseen performance is poor

The model may have overfit, train and test data may differ, or leakage may have corrupted evaluation.

### Parameters do not exactly equal `3.5` and `2`

That is expected with finite noisy data. The objective is a generalizable estimate, not exact recovery of the generator constants.

### A straight line fits curved data poorly

This is underfitting from insufficient model capacity. Additional epochs optimize the wrong model form more thoroughly; they do not make it nonlinear.

### Low loss is treated as proof of usefulness

Loss measures one objective on one dataset. Usefulness also depends on representative data, decision-aligned metrics, edge cases, and operational behavior.

## 17. Connection to LLMs

| Linear regression | Language model |
|---|---|
| Numeric feature | Token sequence |
| Two parameters | Billions of weights and biases |
| Numeric prediction | Next-token probability distribution |
| Mean squared error | Usually cross-entropy loss |
| Manual gradients | Backpropagation and autodiff |
| Gradient descent | Optimizers such as AdamW |
| Predict a number | Generate a token |

An LLM is not a giant linear-regression model, but both are parameterized functions trained by minimizing loss over examples.

## 18. Knowledge checkpoint

Answer without copying the lesson:

1. What does ML learn that traditional code usually specifies directly?
2. Why is this supervised learning and regression?
3. What do `w` and `b` control?
4. How do parameters differ from hyperparameters?
5. Why square residuals, and what drawback does that create?
6. What two pieces of information does a gradient provide?
7. Why do updates subtract the gradient?
8. What happens when the learning rate is too small or too large?
9. Why must final evaluation use unseen data?
10. What is data leakage?
11. Why does noise prevent exact recovery of hidden parameters?
12. Why can no amount of training make this line perfectly model a curve?
13. Which parts of this loop also appear in neural-network training?

## 19. Speak about it confidently

**Plain-language explanation:**

> Machine learning uses examples to estimate a useful relationship. Here, the model adjusts the slope and intercept of a line until its predictions resemble known answers, then we test it on examples it never saw during training.

**Technical explanation:**

> Linear regression is a parameterized function, $\hat{y}=wx+b$. We minimize mean squared error with batch gradient descent by computing analytical gradients for the weight and bias and iteratively updating both parameters. A held-out test set estimates generalization to unseen samples.

## Definition of done

- [ ] Explain AI, ML, deep learning, supervised learning, and regression.
- [ ] Identify every part of the training loop in `train.py`.
- [ ] Run the lab and inspect both plots.
- [ ] Perform at least four experiments and record observations.
- [ ] Explain parameters versus hyperparameters.
- [ ] Explain training versus inference.
- [ ] Explain loss, gradients, and gradient descent without relying only on an analogy.
- [ ] Explain why test data must remain unseen during training.
- [ ] Answer the knowledge checkpoint in your own words.
- [ ] Pass the repository test suite.

## What comes next

Lesson 02 introduces vectors, matrices, tensors, dot products, matrix multiplication, and shapes. Those tools let one model process many features, many examples, and eventually batches of token representations.
