# Lesson 06 — Neural Network Anatomy

## Start here

Open the [interactive lesson](index.html). It teaches the complete lesson in a browser with no programming required.

Lesson 5 established supervised-learning targets, baselines, metrics, and evaluation boundaries. Lesson 6 introduces the structure of a neural-network candidate while preserving that evaluation contract. The learner should understand every forward-pass operation and tensor shape before Lesson 7 explains how gradients move backward through the network.

By the end of this lesson, you should be able to:

- explain what a neuron computes without biological mythology;
- distinguish weights, biases, pre-activations, and activations;
- explain how a dense layer runs many neurons in parallel;
- trace input, weight, bias, and output tensor shapes;
- count the learned parameters in a dense network;
- compare ReLU, sigmoid, tanh, and linear activations;
- explain why stacked linear-only layers collapse into one linear map;
- distinguish width, depth, parameter count, and model capacity;
- choose an output head for regression, binary classification, or multiclass classification;
- distinguish a forward pass during training from inference; and
- produce a neural architecture and tensor-shape contract for the capstone.

## Prerequisites

This lesson assumes only concepts already introduced:

- a feature vector describes one example;
- a matrix can represent a batch of vectors;
- a dot product combines values into one weighted score;
- parameters are learned, while hyperparameters are chosen;
- a model makes a prediction during a forward pass; and
- training uses loss and gradients to update parameters.

If `(32, 10)` does not yet read naturally as “32 examples, each with 10 features,” revisit Lesson 2's shape-tracing section before continuing.

## 1. Why neural networks exist

A linear model applies one learned transformation directly to the original features. This works when the target changes along a sufficiently simple boundary or trend.

Real relationships often involve interactions:

- a short deadline may be risky only for large migrations;
- high transaction volume may be safe until memory pressure and index load are also high;
- a visual edge becomes meaningful only when combined with nearby edges; or
- a word's meaning depends on surrounding words.

A neural network inserts hidden layers between input and output. Hidden layers learn intermediate representations that make the final task easier.

The word “hidden” simply means that the layer's desired values are not directly supplied as labels. They are internal values learned because they help reduce the final loss.

## 2. One artificial neuron is a small numerical function

A neuron performs four steps:

1. multiply each input by a learned weight;
2. add those weighted inputs;
3. add a learned bias; and
4. apply an activation function.

The weighted sum plus bias is often called the **pre-activation** and written as $z$. The value after the activation is written as $a$.

### Fully worked example

Suppose a neuron receives:

- project complexity $x_1=2$ with weight $w_1=0.8$;
- urgency $x_2=3$ with weight $w_2=-0.4$; and
- bias $b=0.5$.

Calculate in words first:

1. Complexity contribution: $2\times0.8=1.6$.
2. Urgency contribution: $3\times-0.4=-1.2$.
3. Add contributions and bias: $1.6-1.2+0.5=0.9$.

So the pre-activation is:

$$
z=0.9
$$

If the activation is ReLU, positive values pass through unchanged, so the neuron outputs 0.9.

The compact form is:

$$
z=\sum_{i=1}^{n}w_i x_i+b
$$

$$
a=f(z)
$$

Here:

- $n$ is the number of inputs;
- $x_i$ is input i;
- $w_i$ is its learned weight;
- $b$ is the learned bias;
- $z$ is the pre-activation;
- $f$ is an activation function; and
- $a$ is the activated output.

### What weights and bias do

- A positive weight makes a larger input push the pre-activation upward.
- A negative weight makes a larger input push it downward.
- A weight near zero makes that input contribute little for this neuron.
- The bias shifts the neuron's response even when all inputs are zero.

These meanings are local to the learned model. A large weight is not automatically causal, fair, stable, or globally important.

## 3. A dense layer runs many neurons in parallel

A dense, linear, or fully connected layer contains several neurons. Every output neuron sees every incoming feature, but owns a different weight vector and bias.

If one example has 10 incoming features and the layer has 64 neurons:

- each neuron needs 10 weights;
- 64 neurons need $10\times64=640$ weights;
- each neuron has one bias, so there are 64 biases; and
- the layer has $640+64=704$ learned parameters.

The 64 neuron outputs become a new 64-value representation for that example.

## 4. Dense-layer shape tracing

This lesson uses row-oriented examples:

$$
XW+b
$$

For:

- input $X$ shaped `(batch, inputs)`;
- weights $W$ shaped `(inputs, outputs)`; and
- bias $b$ shaped `(outputs)`;

the layer produces:

$$
(batch, inputs)\times(inputs, outputs)+(outputs)\rightarrow(batch, outputs)
$$

The inner `inputs` dimensions must match. The batch axis survives. The layer replaces the incoming feature width with its number of neurons.

### Why the bias can be added

The output before bias is shaped `(batch, outputs)`, while bias is `(outputs)`. Broadcasting reuses the same bias vector for every example in the batch. Each neuron adds its own bias to every row.

### Framework convention warning

Some frameworks store weights as `(outputs, inputs)` and internally apply the transpose. That is not a different model. It is a storage and multiplication convention. When debugging, write the framework's documented shape rather than relying on memory.

## 5. Activation functions change how signals pass onward

### ReLU

ReLU returns zero for negative inputs and keeps positive inputs:

$$
\operatorname{ReLU}(z)=\max(0,z)
$$

Examples:

- ReLU(−2) = 0;
- ReLU(0) = 0; and
- ReLU(3) = 3.

ReLU is computationally simple and common in hidden layers. A unit can become **dead** if it remains on the negative side for the relevant data and receives no useful gradient to move back.

At exactly zero, ReLU has a sharp corner and its mathematical derivative is undefined. Training libraries choose a practical convention for that single point, commonly a local slope of zero.

### Sigmoid

Sigmoid compresses any real value into the interval from 0 to 1:

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$

At $z=0$, sigmoid equals 0.5. Large positive inputs approach 1, and large negative inputs approach 0. Sigmoid is commonly used to turn a binary output logit into a bounded score.

At extreme inputs the curve becomes flat. This is **saturation**. Small changes to z produce very small output changes, so backward learning signals can shrink.

### Tanh

Tanh compresses values into the interval from −1 to 1:

$$
\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
$$

It is centered around zero but also saturates at extremes.

### Linear activation

A linear activation returns z unchanged:

$$
f(z)=z
$$

This is appropriate for many unbounded regression outputs. It is not sufficient between every hidden layer because it does not add nonlinearity.

## 6. Why nonlinear activations are essential

Consider two layers without a nonlinear activation.

The first layer computes:

$$
h=w_1x+b_1
$$

The second computes:

$$
y=w_2h+b_2
$$

Substitute the first into the second:

$$
y=w_2(w_1x+b_1)+b_2
$$

Rearrange:

$$
y=(w_2w_1)x+(w_2b_1+b_2)
$$

The terms in parentheses form one new weight and one new bias. Two linear layers have collapsed into one linear layer. The same argument extends to any number of linear-only layers.

A nonlinear activation between layers prevents this collapse. It lets the network bend or fold the representation so later layers can separate patterns that one flat boundary cannot.

### XOR as a small example

XOR outputs 1 when exactly one of two binary inputs is 1:

| x₁ | x₂ | XOR |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The positive corners are diagonal, so one straight boundary cannot separate them from both negative corners.

Two hidden ReLU features can represent disagreement:

$$
h_1=\operatorname{ReLU}(x_1-x_2)
$$

$$
h_2=\operatorname{ReLU}(x_2-x_1)
$$

For binary inputs, $h_1+h_2$ is 1 when the inputs differ and 0 when they match.

This example proves the structural role of nonlinearity. It does not imply that real networks are manually programmed with XOR features; training learns useful transformations from data.

## 7. Width, depth, parameters, and capacity are related but different

### Width

Width is the number of neurons in a layer. A wider layer can represent more features in parallel.

### Depth

Depth is the number of successive learned transformations. A deeper network can build hierarchical compositions: simple patterns first, then combinations of those patterns.

### Parameter count

Parameter count is the total number of learned weights and biases. For a dense layer:

$$
\text{parameters}=\text{inputs}\times\text{outputs}+\text{outputs}
$$

### Capacity

Capacity describes the range and complexity of functions the model can represent. Parameter count contributes to capacity, but architecture, activation, regularization, optimization, and data also matter. Two models with similar parameter counts can behave differently.

Too little effective capacity can underfit: training and validation performance both remain poor. Too much relative to the evidence can overfit: training improves while validation deteriorates.

The goal is not the largest network. The goal is the least-complex candidate that provides defensible held-out improvement over the Lesson 5 baseline.

## 8. Full shape trace: 10 → 64 → 16 → 3

Trace a batch of 32 examples, each with 10 features:

| Stage | Input shape | Weight shape | Bias shape | Output shape | Parameters |
|---|---|---|---|---|---:|
| Dense 1 + ReLU | `(32, 10)` | `(10, 64)` | `(64)` | `(32, 64)` | 704 |
| Dense 2 + ReLU | `(32, 64)` | `(64, 16)` | `(16)` | `(32, 16)` | 1,040 |
| Output | `(32, 16)` | `(16, 3)` | `(3)` | `(32, 3)` | 51 |

Total learned parameters:

$$
704+1{,}040+51=1{,}795
$$

Changing the batch from 32 to 64 doubles the number of activation values processed together but does not change the 1,795 learned parameters.

## 9. The output head must match the task

### Regression

Use one output per numeric target. Many regression tasks use a linear output so predictions are not artificially bounded. Domain constraints may justify a different transformation.

### Binary classification

Use one output logit and sigmoid to produce a score between 0 and 1. Lesson 5's threshold then converts that score into an action.

### Multiclass classification

Use one logit per mutually exclusive class. Softmax exponentiates and normalizes the scores so the outputs are positive and sum to 1:

$$
\operatorname{softmax}(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
$$

The symbols mean: $z_i$ is one class logit, and the denominator sums exponentiated logits across all classes. Softmax creates relative class probabilities under the model; it does not guarantee calibration.

For multilabel classification, classes are not mutually exclusive, so each label commonly receives its own sigmoid output instead of one shared softmax.

## 10. Forward pass during training and inference

The forward computation uses the same current parameters in both modes:

1. receive input batch;
2. compute dense transformation;
3. apply hidden activation;
4. repeat through the network; and
5. produce task outputs.

During **training**, the system continues: compare output with labels, calculate loss, compute gradients, and update parameters.

During **inference**, the system uses the output to estimate or act. It does not normally update model parameters from that request.

Training frameworks may change the behavior of components such as dropout or batch normalization between training and inference. Those mechanisms arrive in later lessons.

## 11. Important failure modes and diagnostics

| Failure | What it looks like | Diagnostic |
|---|---|---|
| Shape mismatch | Matrix multiplication cannot connect adjacent layers | Write every tensor axis and weight convention |
| Missing nonlinearity | Deep network behaves like one linear map | Inspect operations between dense layers |
| Dead ReLU | A unit outputs zero for nearly every example | Inspect activation and gradient distributions |
| Sigmoid/tanh saturation | Values cluster near extremes and gradients shrink | Inspect pre-activations and local slopes |
| Under-capacity | Training and validation metrics both remain poor | Compare with baseline and training fit |
| Over-capacity or shortcuts | Training improves while validation or slices fail | Compare held-out curves and subgroup behavior |
| Wrong output head | Output range or normalization conflicts with target | Trace target, loss, output shape, and activation together |

## 12. Connection to modern AI

Large language models are neural networks. Transformer blocks contain learned projections and feed-forward neural layers. The same fundamentals still apply:

- tensors have named axes;
- weights and biases define learned transformations;
- activations introduce nonlinearity;
- hidden widths affect parameter and activation memory;
- residual pathways preserve and combine representations;
- forward passes produce logits; and
- training calculates loss and gradients after the forward pass.

The scale is enormous, but the underlying bookkeeping is not a different species.

## Interactive learning sequence

In [index.html](index.html):

1. Confirm the meaning of batch and feature axes.
2. Change neuron inputs, weights, bias, and activation.
3. Build a dense layer and trace its shapes and parameter count.
4. Move one pre-activation across ReLU, sigmoid, tanh, and linear curves.
5. Compare a linear-only network with hidden ReLU features on XOR.
6. Change hidden widths and batch size in the architecture builder.
7. Complete all eight knowledge checks.

## Capstone increment: neural architecture and tensor-shape contract

Complete [EXERCISES.md](EXERCISES.md) for one Gate A prediction target. Define:

- the preserved task, baseline, and release metric;
- input features and `(batch, features)` shape;
- each dense layer's input, weights, bias, and output shapes;
- hidden activations and why nonlinearity is necessary;
- output head and why it matches the target;
- layer and total parameter counts;
- largest activation tensor for a proposed batch;
- an under-capacity and over-capacity signal; and
- evidence required to justify this candidate over the simpler baseline.

Lessons 7–10 will add backpropagation, an implementation framework, training, validation, and regularization behind this contract.

## Definition of done

- [ ] Complete the browser lesson and all interactions.
- [ ] Calculate a neuron's pre-activation and output by hand.
- [ ] Trace the complete `(32, 10) → (32, 64) → (32, 16) → (32, 3)` network.
- [ ] Explain why parameter count does not depend on batch size.
- [ ] Compare ReLU, sigmoid, tanh, and linear activation behavior.
- [ ] Prove in words why linear-only depth collapses.
- [ ] Choose the correct output head for three task types.
- [ ] Complete all eight knowledge checks.
- [ ] Produce the capstone architecture and tensor-shape contract.
- [ ] Mark Lesson 6 complete on the course dashboard.

## Instructor and maintainer note

The repository retains `lab.py` and reusable course-lab code for automated verification and optional instructor demonstrations. They are not part of the learner path. Students do not need to read or edit Python in Lesson 6.
