# Lesson 07 — Backpropagation From Scratch

## Start here

Open the [interactive lesson](index.html). It teaches backpropagation visually and numerically without requiring programming.

Lesson 6 explained how a network transforms inputs into outputs during a forward pass. Lesson 7 explains how training computes the gradient of one scalar loss with respect to every learned parameter. Lesson 8 will automate this same procedure with PyTorch, so this lesson makes the automation inspectable rather than magical.

By the end, you should be able to:

- explain derivatives as local sensitivity;
- decompose an expression into a computational graph;
- distinguish forward values, local derivatives, upstream gradients, and parameter gradients;
- apply the chain rule through several operations;
- manually differentiate $y=(xw+b)^2$ with respect to x, w, and b;
- explain why gradients multiply along one path and add across branches;
- explain why reverse-mode differentiation fits scalar-loss training;
- verify that every tensor gradient matches its parameter's shape;
- distinguish within-graph accumulation from accumulation across backward calls;
- explain zeroing, intentional microbatch accumulation, and stop-gradient; and
- verify a leaf gradient with centered finite differences.

## Prerequisites

You should already be able to explain:

- what a forward pass computes;
- what loss measures;
- what gradient sign and magnitude mean;
- how gradient descent uses a parameter gradient;
- what weights, biases, and activation functions do; and
- why tensor axes and shapes must be named.

No calculus course is assumed. Every derivative rule used here is introduced before it is applied.

## 1. A derivative answers a local “what if?” question

Suppose the current weight is 3.0. The derivative of loss with respect to that weight asks:

> If the weight changed by a very small amount near 3.0, approximately how much and in which direction would loss change?

If the gradient is +4:

- increasing the weight slightly increases loss;
- decreasing the weight slightly decreases loss; and
- a small change $\Delta w$ predicts loss change of approximately $4\Delta w$ near the current point.

If the gradient is −4, the local direction reverses. If it is zero, the loss is locally flat with respect to that parameter; this does not prove a global minimum.

Backpropagation computes these sensitivities. Gradient descent later uses them. Backpropagation does not choose a learning rate or update parameters by itself.

## 2. A computational graph decomposes one expression

Consider:

$$
y=(xw+b)^2
$$

Break it into small operations:

$$
m=xw
$$

$$
p=m+b
$$

$$
y=p^2
$$

The graph is directed because later values depend on earlier values. It is acyclic because a standard forward expression does not depend on its own future result.

Each node needs two kinds of information:

- its **forward value**, calculated from its inputs; and
- eventually, its **gradient**, describing how final loss changes with that value.

Frameworks also retain operation-specific context needed for backward rules. Multiplication needs the other input value; sigmoid may retain its output; a matrix operation needs shapes and values.

## 3. Complete forward pass

Let:

$$
x=2,\quad w=3,\quad b=1
$$

Calculate in dependency order:

1. $m=xw=2\times3=6$
2. $p=m+b=6+1=7$
3. $y=p^2=7^2=49$

For this teaching graph, treat y as the scalar loss. A real network would normally calculate prediction first and then apply a loss function comparing prediction with a target.

## 4. Backward pass starts by seeding the scalar loss

The derivative of a value with respect to itself is 1:

$$
\frac{\partial y}{\partial y}=1
$$

This seed says: a one-unit change in y changes y by one unit. The backward pass now moves through graph dependencies in reverse.

Partial-derivative notation uses $\partial$ because the function can depend on several values. The practical question remains the same: change one value slightly while holding the other current inputs fixed.

## 5. Local derivatives describe one operation only

### Square

For:

$$
y=p^2
$$

the local derivative is:

$$
\frac{\partial y}{\partial p}=2p
$$

At p = 7, the local derivative is 14. Multiply by the arriving upstream gradient 1:

$$
\frac{\partial y}{\partial p}=1\times14=14
$$

### Addition

For:

$$
p=m+b
$$

increasing either m or b by a small amount increases p by the same amount:

$$
\frac{\partial p}{\partial m}=1,\qquad\frac{\partial p}{\partial b}=1
$$

Both inputs receive the upstream gradient 14:

$$
\frac{\partial y}{\partial m}=14\times1=14
$$

$$
\frac{\partial y}{\partial b}=14\times1=14
$$

### Multiplication

For:

$$
m=xw
$$

the derivative with respect to one input is the other input:

$$
\frac{\partial m}{\partial x}=w=3
$$

$$
\frac{\partial m}{\partial w}=x=2
$$

Multiply each local derivative by upstream gradient 14:

$$
\frac{\partial y}{\partial x}=14\times3=42
$$

$$
\frac{\partial y}{\partial w}=14\times2=28
$$

The completed leaf gradients are:

| Leaf | Value | Gradient |
|---|---:|---:|
| x | 2 | 42 |
| w | 3 | 28 |
| b | 1 | 14 |

If w and b are learnable parameters, the optimizer uses gradients 28 and 14. If x is input data, its gradient may still be useful for earlier layers, input optimization, or analysis, but ordinary supervised training does not update the dataset value x.

## 6. The chain rule connects local effects

Suppose:

$$
u=2x+1
$$

$$
y=u^2
$$

At x = 3, u = 7.

- One local unit of x changes u by 2, so $du/dx=2$.
- One local unit of u changes y by $2u=14$, so $dy/du=14$.
- Therefore one local unit of x changes y by $14\times2=28$.

Compactly:

$$
\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}
$$

Backpropagation repeatedly evaluates:

$$
\text{downstream gradient}=\text{upstream gradient}\times\text{local derivative}
$$

It is not a separate mathematical law. It is an efficient algorithm for applying the chain rule through a graph while reusing already-computed values and gradients.

## 7. Activation functions gate gradient flow

### ReLU

Away from zero:

$$
\frac{d}{dz}\operatorname{ReLU}(z)=
\begin{cases}
0 & z<0\\
1 & z>0
\end{cases}
$$

A positive ReLU pre-activation passes the upstream gradient unchanged. A negative one blocks it with local derivative zero. At exactly zero the mathematical derivative is undefined; frameworks choose a convention, commonly zero.

### Sigmoid

If $s=\sigma(z)$, sigmoid's derivative is:

$$
\frac{ds}{dz}=s(1-s)
$$

The maximum derivative is 0.25 at s = 0.5. Near outputs 0 or 1, the derivative becomes small and shrinks the arriving gradient.

### Tanh

If $t=\tanh(z)$:

$$
\frac{dt}{dz}=1-t^2
$$

Tanh has its largest slope near zero and small slopes near −1 or 1.

These local rules explain dead ReLU units and saturated sigmoid/tanh layers from Lesson 6 in terms of backward signal flow.

## 8. Gradients add when a value has multiple paths

Let:

$$
y=x^2+3x
$$

x influences y through two paths:

- square path contributes $2x$;
- linear path contributes 3.

The total is:

$$
\frac{dy}{dx}=2x+3
$$

At x = 2, the contributions are 4 and 3, so total gradient is 7.

Keeping only the last contribution would report 3 and silently lose the square path. A node must wait until every later dependency has sent its contribution, then sum them before continuing backward.

This is why backward traversal follows reverse topological order: downstream consumers must be processed before the upstream producer.

## 9. Reverse-mode differentiation fits neural-network training

There are two broad ways to propagate derivatives through a graph:

- **Forward mode** chooses an input direction and carries its effect toward outputs.
- **Reverse mode** chooses an output and carries its sensitivity toward all inputs.

Neural-network training usually has:

- one scalar loss; and
- many learned parameters.

Reverse mode can obtain gradients for every parameter from one backward traversal seeded at that scalar loss. That is the core of backpropagation and modern reverse-mode autograd.

The high-level algorithm is:

1. run the forward pass;
2. store required values and graph relationships;
3. seed scalar loss gradient with 1;
4. traverse nodes in reverse topological order;
5. multiply arriving gradients by local derivatives;
6. sum contributions where paths merge; and
7. store gradients at requested leaves such as parameters.

## 10. Tensor gradients match the tensors they describe

If a dense-layer weight matrix has shape `(10, 64)`, then:

$$
\frac{\partial L}{\partial W}
$$

also has shape `(10, 64)`. Each element describes local loss sensitivity to the corresponding weight element.

Likewise:

- bias b shaped `(64)` has gradient shaped `(64)`;
- input X shaped `(batch, 10)` has gradient shaped `(batch, 10)` if requested; and
- output activation A shaped `(batch, 64)` receives an upstream gradient of that same shape.

Internally, a vector-valued operation has a **Jacobian** containing output-to-input derivatives. Building every full Jacobian would be prohibitively expensive. Reverse mode computes vector–Jacobian products directly: combine the arriving gradient vector with the local derivative operation to produce the next gradient vector.

Students do not need to construct a giant Jacobian to trace ordinary network shapes. The essential invariant is that a value and its gradient share a shape.

## 11. Gradient accumulation has two related meanings

### Within one graph

If a value influences loss through several paths, the mathematically correct gradient is the sum of path contributions. This happens during one backward traversal.

### Across backward calls

Many frameworks store a gradient buffer on each parameter and add each new backward result into it. This stateful behavior supports:

- accumulating several microbatches before an optimizer step;
- combining multiple loss terms; and
- some advanced training procedures.

It also creates a common bug: a new independent batch adds its gradient to stale gradients from the prior update.

## 12. Zeroing and optimizer order

For independent batches, the conceptual sequence is:

1. clear old gradient buffers;
2. run forward pass;
3. calculate scalar loss;
4. run backward pass;
5. apply optimizer update.

An optimizer step normally does not automatically erase gradient buffers. If buffers remain populated, another backward call adds to them.

### Intentional microbatch accumulation

Suppose memory permits only 8 examples at a time, but the desired effective batch is 32. The system can:

1. clear gradients once;
2. run forward/backward on four microbatches of 8;
3. accumulate their gradient contributions;
4. normalize consistently with the loss definition; and
5. apply one optimizer step.

Incorrect scaling changes the effective learning rate. Document whether each microbatch loss is a sum or mean and how the accumulated result is normalized.

## 13. Stop-gradient cuts one backward path

A detach or stop-gradient operation:

- keeps a value in the forward computation; but
- treats that value as constant during backward propagation through that path.

This can be intentional for frozen targets, teacher model outputs, target networks, or carefully constructed objectives. It can also be an accidental silent failure: earlier parameters receive no gradient and cannot learn from that loss.

Stop-gradient is not the same as zeroing parameter buffers. Zeroing clears stored gradients; stop-gradient changes graph connectivity for differentiation.

## 14. Verify gradients with finite differences

Lesson 3 introduced centered finite differences. For parameter w:

$$
\frac{\partial L}{\partial w}\approx\frac{L(w+\epsilon)-L(w-\epsilon)}{2\epsilon}
$$

For $y=(xw+b)^2$ at x = 2, w = 3, b = 1, the analytical gradient with respect to w is 28.

With $\epsilon=0.001$:

$$
\frac{(2(3.001)+1)^2-(2(2.999)+1)^2}{0.002}\approx28
$$

Gradient checking is slow, so it is used on small functions and selected parameters—not as the training algorithm. Agreement helps detect wrong local derivatives, missed branch sums, bad graph order, and shape errors.

## 15. Vanishing and exploding gradients

Backpropagation multiplies many local derivatives along deep paths.

- Repeated factors smaller than 1 can make gradients vanish toward earlier layers.
- Repeated factors larger than 1 can make gradients explode.
- Branches, residual connections, normalization, initialization, activation choice, and gradient clipping all influence this behavior.

A vanishing gradient is not the same as a low loss. It means the learning signal reaching some parameters is extremely small. An exploding gradient can produce unstable updates, non-finite values, or divergence.

Later lessons will connect these signals to actual training telemetry.

## 16. Common failure modes

| Failure | Result | Detection |
|---|---|---|
| Wrong backward order | A node propagates before all contributions arrive | Compare with topological dependency trace |
| Overwritten branch | One path contribution disappears | Construct a two-branch analytical test |
| Forgotten zeroing | Independent batches include stale gradients | Inspect buffer before backward |
| Wrong accumulation scaling | Effective update is too large or small | Compare full-batch and accumulated result |
| Accidental detach | Earlier parameters have no gradients | Trace graph connectivity and missing gradients |
| Saturation or dead ReLU | Gradients shrink to zero through activations | Log pre-activation and gradient distributions |
| Exploding path | Gradients or parameters become extremely large/non-finite | Track gradient norms and finite-value checks |
| Shape mistake | Gradient cannot align with its value | Assert value/gradient shape equality |

## 17. Connection to modern AI

Every trained neural architecture relies on these mechanics:

- transformer attention and feed-forward blocks form a large computational graph;
- residual branches send several gradient paths into shared earlier states;
- automatic differentiation supplies vector–Jacobian products;
- distributed workers aggregate parameter gradients;
- gradient accumulation creates larger effective batches;
- mixed precision requires careful gradient scaling; and
- frozen components use deliberate gradient boundaries.

Frameworks save enormous effort, but they do not eliminate the need to understand gradient state, graph connectivity, scaling, or failure signals.

## Interactive learning sequence

In [index.html](index.html):

1. Confirm gradient-descent direction from a gradient sign.
2. Change x, w, and b in $y=(xw+b)^2$ and reveal each backward step.
3. Move x through a two-operation chain-rule explorer.
4. Pass an upstream gradient through ReLU, sigmoid, tanh, and linear gates.
5. Compare correct branch summation with an overwrite bug.
6. Run backward, zero, and optimizer operations in the gradient-state simulator.
7. Complete all eight knowledge checks.

## Capstone increment: backward-pass and gradient-state contract

Extend the Lesson 6 neural architecture contract with:

- one representative path from input to scalar loss;
- every required forward value;
- the local derivative at each operation;
- upstream × local calculations in reverse order;
- every branch accumulation point;
- parameter-gradient shapes;
- one finite-difference verification;
- gradient zeroing and update order;
- intentional accumulation and normalization rules, if used; and
- deliberate stop-gradient boundaries, if any.

This becomes the expected behavior against which Lesson 8's autograd results are checked.

## Definition of done

- [ ] Complete every browser interaction.
- [ ] Trace $y=(xw+b)^2$ forward and backward by hand.
- [ ] Explain upstream gradient × local derivative.
- [ ] Explain why path contributions add.
- [ ] Explain why reverse mode fits one scalar loss and many parameters.
- [ ] Match parameter and gradient shapes.
- [ ] Demonstrate the stale-gradient failure in the simulator.
- [ ] Verify one gradient with finite differences.
- [ ] Complete all eight knowledge checks.
- [ ] Produce the capstone backward-pass contract.
- [ ] Mark Lesson 7 complete on the course dashboard.

## Instructor and maintainer note

The repository retains `lab.py` and reusable course-lab code for automated verification and optional instructor demonstrations. They are not part of the learner path. Students do not need to read or edit Python in Lesson 7.
