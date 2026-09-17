# Lesson 08 Reference Notes — PyTorch and Autograd

Review these notes only after completing your own attempt. Strong answers may use different wording, but they should preserve the same state boundaries and reasoning.

## 1. Tensor metadata and memory

The shape is `(128, 768)`. It contains:

> 128 × 768 = 98,304 values

Value storage is:

- float32: 98,304 × 4 = 393,216 bytes = 384 KiB;
- float16: 98,304 × 2 = 196,608 bytes = 192 KiB.

Total training memory is larger because value storage excludes gradients, optimizer history, saved forward activations, temporary workspaces, parameters, allocator overhead, and possibly higher-precision copies.

Token IDs and class labels are normally integer tensors. Learned weights, hidden activations, and probabilities are normally floating-point tensors.

## 2. Dtype and device contract

1. **Valid.** Integer IDs select embedding rows; the selected embeddings are floating point.
2. **Invalid for a connected operation.** Inputs and weights must be available to the same execution device.
3. **Potentially invalid or unsafe.** Mixed precision needs an explicit policy that controls conversion and numerically sensitive operations.
4. **Usually inefficient.** The predictions may be correct, but graph context consumes unnecessary memory and work.
5. **Invalid for ordinary autograd.** Discrete integer values do not support infinitesimal continuous changes.

Useful checks assert the expected rank and dimensions, allowed dtype, common device for connected tensors, and gradient tracking only for intended floating-point leaves.

## 3. Autograd graph inventory

The forward values are:

- `xw = 2 × 3 = 6`;
- `xw + b = 6 + 1 = 7`;
- `y = 7² = 49`.

If only `w` and `b` are tracked, those two leaves receive gradients:

- gradient for `w` = 28;
- gradient for `b` = 14.

With recording disabled, the forward calculation still produces 49. It does not retain the backward graph or produce leaf gradients. Backward calculates and stores gradients; it does not apply an update. The optimizer owns the separate update transition.

## 4. Registered model state

| Layer | Weight shape | Bias shape | Parameters |
|---|---|---|---:|
| 10 → 64 | (10, 64) | (64) | 704 |
| 64 → 16 | (64, 16) | (16) | 1,040 |
| 16 → 3 | (16, 3) | (3) | 51 |
| **Total** | | | **1,795** |

Classifications:

- dense-layer weight: trainable parameter;
- batch-normalization running mean: persistent buffer;
- adaptive optimizer moving average: optimizer state;
- label-to-name mapping: external metadata;
- feature-normalization configuration: external metadata, unless deliberately represented as registered model buffers.

An unregistered trainable tensor may be omitted from parameter discovery, device moves, optimizer construction, state collection, and recursive mode operations. It can participate in a calculation while quietly never being updated or restored.

## 5. Training lifecycle diagnosis

The canonical order is:

1. clear stale gradient buffers;
2. perform the forward pass;
3. compute the scalar loss;
4. run backward;
5. update parameters.

Diagnoses:

1. **Step before backward:** no current gradient exists; the step may do nothing or use stale state.
2. **No clearing:** gradients accumulate across independent batches; update magnitude and meaning become wrong.
3. **Loss before prediction:** the required forward result does not exist or comes from the wrong batch.
4. **Extra forward after backward:** the update still refers to the earlier graph, while displayed predictions may describe different state.
5. **Update during validation:** evaluation mutates the model and contaminates both metrics and training history.

## 6. Mode and gradient-context matrix

| Activity | Module mode | Record gradients? | Why? |
|---|---|:---:|---|
| Training | Training | Yes | Build gradients and use training-time layer behavior |
| Validation | Evaluation | No | Stable evaluation behavior without update graphs |
| Production inference | Evaluation | No | Stable, memory-efficient prediction |
| Input-sensitivity explanation | Evaluation | Yes for the chosen input | Stable model behavior while differentiating output with respect to input |

Module mode controls behaviors such as dropout and batch normalization. Gradient context controls graph recording. Either can be changed without automatically changing the other.

## 7. Checkpoint planning

**Inference deployment** needs model parameters and persistent buffers, matching architecture/configuration, preprocessing, label interpretation, compatible runtime versions, and release evaluation evidence.

**Training continuation** additionally needs optimizer and scheduler state, training progress, random/scaler state where relevant, and the training configuration and data identity.

**Experiment reproduction** also needs exact code and dependency identity, data and split identity, seeds, full configuration, recorded metrics, and evaluation artifacts. A checkpoint restores state; it does not by itself prove where that state came from or recreate the complete experiment.

## 8. Failure investigation

| Incident | Likely state category | Detection signal | Corrective action |
|---|---|---|---|
| One layer never learns | Registration or gradient state | Parameter absent from inventory or gradient missing | Register it and verify optimizer discovery plus gradient presence |
| Tensors are on different devices | Tensor execution metadata | Device assertion or runtime mismatch | Move connected state under one explicit device policy |
| Validation changes between identical passes | Module mode | Repeated-pass stability test fails | Switch to evaluation mode and prevent unintended updates |
| Resumed training behaves differently | Optimizer/progress/random state | First resumed steps diverge from controlled continuation | Save and restore complete training state |
| Restored predictions are nonsensical | External metadata or architecture | Golden-input comparison fails | Restore matching preprocessing, labels, architecture, and versions |

## 9. Capstone acceptance criteria

A strong execution and state contract:

- gives every important tensor an explicit meaning, shape, dtype, device, and gradient policy;
- distinguishes parameters, buffers, optimizer history, and external metadata;
- identifies recorded forward operations and expected leaf-gradient shapes;
- treats clear, forward, loss, backward, and step as ordered state transitions;
- separates module mode from gradient context;
- defines different checkpoint contents for inference, continuation, and reproduction;
- includes automated checks for incompatible shapes, dtypes, devices, missing or non-finite gradients, wrong modes, and checkpoint mismatches.

The contract is ready for Lesson 9 when another engineer can implement the model without guessing what state the framework should own or when that state changes.
