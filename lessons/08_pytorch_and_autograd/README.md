# Lesson 08 — PyTorch and Autograd

## Start here

Open the [interactive lesson](index.html). This lesson teaches the PyTorch execution model without requiring Python.

Lessons 6 and 7 defined a network's forward and backward behavior manually. PyTorch represents the same tensors and operations, records the differentiation graph, discovers registered parameters, stores gradient state, coordinates optimizers, switches mode-aware layers, and serializes model state.

The framework removes repetitive mechanics. It does not decide whether tensor shapes are meaningful, a loss matches the task, validation is trustworthy, a threshold is useful, or a checkpoint contains enough evidence for production.

By the end, you should be able to:

- describe a tensor using values, shape, dtype, device, and gradient status;
- estimate tensor value memory and explain why training uses more;
- distinguish floating-point data, integer indices, and label encodings;
- explain device and dtype compatibility;
- explain how autograd constructs and traverses a dynamic graph;
- distinguish leaves, non-leaves, tracked values, and disabled gradient contexts;
- explain what module registration enables;
- distinguish parameters, persistent buffers, optimizer state, and external metadata;
- trace the clear → forward → loss → backward → step lifecycle;
- distinguish training/evaluation mode from gradient recording;
- specify checkpoint contents for inference, training continuation, and experiment reproduction; and
- produce a PyTorch execution and state contract for Lesson 9.

## Code-readiness boundary

This lesson deliberately contains no Python implementation. The course promise is that engineers with no Python background can understand the examples and capstone requirements.

Lesson 9 must provide an explicit bridge before asking students to modify a training program:

- values and variables;
- lists, mappings, functions, loops, and indentation;
- importing a package;
- creating and activating an isolated environment;
- installing dependencies;
- running a program and reading an error;
- changing documented configuration; and
- running tests and interpreting pass/fail output.

Experienced Python engineers can pass that diagnostic quickly. The concepts in this lesson remain required because framework state causes failures that syntax knowledge alone does not prevent.

## 1. PyTorch manages several kinds of state

### Tensor state

Numerical values plus shape, dtype, device, storage, and gradient metadata.

### Graph state

Relationships between tracked operations and saved context needed for backward rules.

### Module state

Registered parameters, persistent buffers, nested modules, and current training/evaluation mode.

### Optimizer state

References to selected parameters and optional history such as momentum or moving averages.

### Artifact state

Serialized weights, buffers, update history, progress, configuration, and provenance needed for a restoration goal.

Understanding which subsystem owns a value is the fastest route through many PyTorch bugs.

## 2. A tensor is more than an array of numbers

A tensor includes:

| Property | Question answered |
|---|---|
| Values | What numerical data is stored? |
| Shape | How are values organized into axes? |
| Dtype | How is each value represented numerically? |
| Device | Where do storage and computation live? |
| Gradient status | Should autograd record dependent operations? |
| Layout/stride | How do logical indices map to storage? |

Lesson 2 established that shape has semantic meaning. `(32, 64)` should be read as named axes—perhaps 32 examples and 64 hidden features—not merely two numbers.

## 3. Estimate tensor value memory

For a dense tensor:

$$
\text{value bytes}=\text{number of elements}\times\text{bytes per element}
$$

A `(32, 64)` tensor has:

$$
32\times64=2{,}048\text{ elements}
$$

With float32 at 4 bytes per element:

$$
2{,}048\times4=8{,}192\text{ bytes}=8\text{ KiB}
$$

With float16 or bfloat16 at 2 bytes per element, its raw value storage is 4 KiB.

This does not estimate full training memory. Training may also retain:

- parameter gradients;
- optimizer history, sometimes several values per parameter;
- saved activations and operation context;
- temporary workspaces;
- memory allocator reservations; and
- distributed communication buffers.

The largest activation can dominate memory even when it contains no learned parameters.

## 4. Dtype controls range, precision, memory, and valid operations

### float32

A common default for model training and numerical work. It balances range, precision, memory, and broad hardware support.

### float16

Uses half the raw storage of float32 and can accelerate supported hardware. Its narrower numerical range can overflow or underflow, so mixed-precision training may use scaling and higher-precision master state.

### bfloat16

Also uses 2 bytes but preserves a range closer to float32 while keeping fewer precision bits. It is widely useful on supported accelerators.

### float64

Uses 8 bytes and offers higher precision. It costs more memory and often lower accelerator throughput; it is valuable for selected numerical or verification workloads rather than automatically “better AI.”

### Integer dtypes

Integers represent discrete values such as token IDs, indices, counts, and class labels. Ordinary autograd cannot assign continuous derivatives to integer leaves because infinitesimal integer changes are not defined.

A model can still use integer indices to select floating-point embeddings. Gradients update embedding weights, not the discrete token IDs.

## 5. Device is part of compatibility

A device identifies where tensor storage and operations occur, such as CPU or an accelerator.

Connected operations normally require participating tensors and model parameters to be on compatible devices. A CPU input cannot silently multiply an accelerator weight without a transfer. Explicit movement makes cost and ownership visible.

Device movement matters because:

- transfers consume time and bandwidth;
- repeated transfers inside a hot loop can erase accelerator benefits;
- inputs, parameters, labels, and optimizer state must be coordinated; and
- checkpoints are often restored to a device chosen at load time rather than the device where they were saved.

“Use the GPU” is incomplete. Ask whether the operation is supported, data movement is controlled, memory fits, throughput improves, and results meet numerical requirements.

## 6. Autograd records differentiable operations dynamically

PyTorch uses a dynamic computational graph. The graph is created as tracked operations execute during the forward pass.

If a floating-point leaf requests gradients and later operations depend on it:

1. each result records graph history;
2. operations store context needed by their backward rules;
3. a scalar loss becomes the backward starting point; and
4. reverse-mode differentiation computes gradients for tracked leaves.

Control flow can create different graphs for different forward passes. The graph describes what actually executed, not a permanently fixed symbolic program.

## 7. Leaves and non-leaves

### Leaf tensor

A tensor introduced directly rather than produced by a tracked operation. Trainable model parameters are leaves. Their gradient buffers are the values optimizers normally read.

### Non-leaf tensor

A result produced by a tracked operation. It keeps graph history so gradients can continue toward its ancestors. Intermediate gradients need not be retained permanently unless explicitly requested.

For the Lesson 7 graph:

$$
y=(xw+b)^2
$$

x, w, and b can be leaves. Multiply, add, and square produce non-leaf results. If w and b request gradients but x does not, backward still uses x's forward value to compute the weight gradient, but it does not need to store a final gradient buffer for x.

## 8. Gradient tracking and disabled recording

The idea commonly exposed as `requires_grad` says that a floating-point leaf needs derivative information from dependent operations.

The idea commonly exposed as a no-gradient or inference context says not to build a backward graph for operations inside that context.

These controls answer different levels of question:

- Does this leaf need gradients?
- Should operations in this region be recorded at all?

Disabling recording is useful for inference and validation because it reduces graph bookkeeping and saved forward context. The forward numerical result still exists.

After a normal backward call, graph resources may be released because they are no longer needed. Reusing the exact graph for another backward pass requires deliberate retention and additional memory. Most training iterations build a new graph from a new forward pass.

## 9. Backward computes gradients; it does not update parameters

Calling backward on a scalar loss conceptually:

1. seeds loss gradient with 1;
2. follows reverse graph dependencies;
3. applies operation-specific vector–Jacobian products;
4. adds branch contributions; and
5. accumulates results into requested leaf gradient buffers.

It does not choose an optimizer, learning rate, or update rule.

If a selected output is not scalar, backward needs an explicit upstream gradient with matching shape. Neural training avoids that complication at the outer boundary by reducing per-example losses to one scalar batch loss.

## 10. A module is a registered component tree

A module combines forward behavior with discoverable nested state.

Registration enables the framework to:

- enumerate trainable parameters;
- enumerate persistent buffers;
- move nested state to another device or dtype;
- switch mode-aware children recursively;
- create a keyed state dictionary; and
- supply intended parameters to an optimizer.

An arbitrary tensor stored outside registration can participate in computation but be missed by optimizer discovery, device movement, or checkpoint state.

### Parameter

A persistent tensor intended to be optimized. A weight or bias is typically a parameter and normally requests gradients.

### Persistent buffer

Model state saved with the module but not updated by gradient descent. Examples include certain running statistics or fixed masks.

### Ordinary attribute or external state

Configuration or application data that the module system does not automatically treat as a tensor parameter or persistent buffer. It requires separate serialization and lifecycle decisions.

## 11. Optimizers apply update rules and may retain history

The simplest update from Lesson 3 is:

$$
w_{new}=w_{old}-\eta\frac{\partial L}{\partial w}
$$

An optimizer owns the update policy. More advanced optimizers can retain state such as:

- momentum estimates;
- moving averages of gradients;
- moving averages of squared gradients;
- per-parameter step counts; and
- scheduling state managed alongside the optimizer.

Therefore:

- model state is not optimizer state;
- backward must run before an optimizer can use current gradients;
- stepping does not necessarily clear gradients; and
- resuming training from weights alone can change the future trajectory.

## 12. The canonical batch lifecycle

For independent batches:

1. **Clear gradients.** Remove stale buffer contents.
2. **Forward.** Produce predictions with current module parameters.
3. **Loss.** Compare predictions with labels and reduce to a scalar objective.
4. **Backward.** Populate parameter gradient buffers through autograd.
5. **Step.** Let the optimizer update parameters and its own state.

The order follows state dependencies:

- loss needs predictions;
- backward needs loss and graph history;
- step needs gradients; and
- the next independent batch needs clean buffers.

Clearing after the step can also be correct if done consistently before the next backward call. The invariant matters more than stylistic placement: stale gradients must not enter an independent update.

## 13. Training and evaluation modes

A module tree has a training/evaluation mode flag. Mode-aware layers consult it.

### Dropout

During training, dropout randomly zeroes a fraction of activations and rescales survivors so the expected signal remains aligned. During evaluation, dropout is disabled.

The same input can therefore produce different training-mode outputs but stable evaluation-mode outputs.

### Batch normalization

During training, batch normalization commonly uses current batch statistics and updates running estimates. During evaluation, it commonly uses saved running statistics.

Forgetting evaluation mode can make validation noisy or contaminate running state. Forgetting to restore training mode afterward can silently alter later training behavior.

## 14. Mode and gradient context are independent

Evaluation mode does not automatically disable autograd. A validation pass can be:

- in evaluation mode, so dropout/batch-normalization behave appropriately; and
- in a disabled-gradient context, so no training graph is saved.

Conversely, one may need gradients while a model is in evaluation mode for explanation, optimization, or adversarial analysis.

Think in two axes:

| Question | Control |
|---|---|
| How should mode-aware layers behave? | Training versus evaluation mode |
| Should operations build a backward graph? | Gradient-recording context |

## 15. State dictionaries are keyed registered tensor state

A model state dictionary maps hierarchical names to registered parameters and persistent buffers.

Conceptually:

| Key | Tensor shape |
|---|---|
| `dense1.weight` | `(64, 10)` or framework storage convention |
| `dense1.bias` | `(64)` |
| `dense2.weight` | `(16, 64)` |
| `head.weight` | `(3, 16)` |

The keys and shapes must match the reconstructed architecture. Strict loading helps catch missing or unexpected state rather than silently deploying a partial model.

A state dictionary does not automatically include:

- the module class definition;
- feature names and order;
- preprocessing;
- class-label mapping;
- package versions;
- training data or splits;
- business thresholds; or
- evaluation evidence.

Those belong in the surrounding artifact contract.

## 16. Checkpoint contents depend on restoration goal

### Inference deployment

Usually requires:

- model state;
- reconstructable architecture/configuration;
- preprocessing and feature contract;
- output interpretation and thresholds;
- software/runtime versions; and
- validation and release metadata.

### Resume training

Also requires:

- optimizer state;
- scheduler state when present;
- training step or epoch;
- best-metric and early-stopping state;
- mixed-precision scaler state when used; and
- random-state information when trajectory continuity matters.

### Reproduce an experiment

Also requires identity for:

- code;
- dependency environment;
- data and exact split;
- configuration and seeds;
- hardware-relevant settings; and
- raw metrics and artifacts.

Restoring is not reproducing. A model can load successfully without recreating how it was obtained.

## 17. Checkpoint safety and provenance

Serialized artifacts are part of the software supply chain. Only load artifacts from trusted sources, validate integrity and provenance, prefer formats and loading modes designed to restrict executable behavior, and preserve version/approval metadata.

A checksum proves bytes did not change after the checksum was established. It does not prove the original artifact was safe, authorized, or high quality.

## 18. Loud and quiet failures

| Failure | Usually loud or quiet? | Detection |
|---|---|---|
| Device mismatch | Loud | Preflight device assertions |
| Unsupported dtype combination | Often loud | Dtype contract and operation test |
| Wrong tensor shape | Loud or misleading | Named-axis assertions |
| Parameter not registered | Quiet | Compare expected and discovered parameter names/counts |
| Missing gradient | Quiet | Assert required leaf gradients exist and are finite |
| Stale gradient buffer | Quiet | Check clear/backward/step lifecycle |
| Validation left in training mode | Quiet | Mode assertions and deterministic fixture |
| Inference builds graphs | Quiet memory/performance cost | Gradient-context and memory checks |
| Partial checkpoint load | Loud if strict, quiet if ignored | Enforce and review missing/unexpected keys |
| Missing preprocessing metadata | Quiet semantic corruption | End-to-end golden examples |

The dangerous failures are often the ones that produce plausible numbers.

## 19. Connection to modern AI

PyTorch-compatible model state and operations appear throughout open-model research and production tooling. Transformers still use:

- tensors with batch, token, head, and feature axes;
- registered projection and feed-forward parameters;
- reverse-mode autograd for training;
- optimizer state far larger than a single gradient buffer;
- training and inference execution differences;
- mixed precision and device placement; and
- versioned sharded checkpoints.

The vocabulary scales directly from the small Lesson 6 network.

## Interactive learning sequence

In [index.html](index.html):

1. Confirm the training lifecycle order.
2. Change tensor shape, dtype, device, and gradient tracking; inspect memory and validity.
3. Choose tracked leaves or disable graph recording in the autograd explorer.
4. Inspect registered module state for the Lesson 6 architecture.
5. Advance the training-loop state machine one stage at a time.
6. Compare repeated dropout outputs in training and evaluation modes.
7. Plan checkpoint contents for inference, training continuation, and reproduction.
8. Complete all eight knowledge checks.

## Capstone increment: PyTorch execution and state contract

Extend the Lesson 6–7 model specification with:

- tensor shape, dtype, device, and gradient status;
- registered parameter and persistent-buffer inventory;
- expected parameter names and count;
- tracked leaves and expected gradient shapes;
- canonical lifecycle and buffer-clearing rule;
- optimizer state expectations;
- training, validation, and inference mode/context matrix;
- checkpoint contents by restoration goal;
- strict restoration checks; and
- golden examples proving preprocessing and output interpretation.

Lesson 9 will implement and test this contract after teaching the minimum code and environment skills.

## Definition of done

- [ ] Complete every browser interaction.
- [ ] Explain tensor shape, dtype, device, and gradient status.
- [ ] Estimate raw tensor value memory.
- [ ] Trace which leaves receive gradients in the autograd explorer.
- [ ] Explain module parameter and buffer registration.
- [ ] Complete the training-loop state machine in order.
- [ ] Explain mode versus gradient context.
- [ ] Plan three checkpoint restoration goals.
- [ ] Complete all eight knowledge checks.
- [ ] Produce the capstone execution and state contract.
- [ ] Mark Lesson 8 complete on the course dashboard.

## Instructor and maintainer note

The repository retains `lab.py` and reusable course-lab code for automated verification and optional instructor demonstrations. They are not part of the learner path. Students do not need to read or edit Python in Lesson 8.
