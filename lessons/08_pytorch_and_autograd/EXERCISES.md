# Lesson 08 Exercises — PyTorch and Autograd

Complete these exercises after using the browser lesson. They require reasoning about framework state, not writing Python.

## 1. Tensor metadata and memory

A system receives a batch of 128 records. Each record has 768 floating-point features.

1. Write the tensor shape.
2. Calculate the number of stored values.
3. Calculate value storage for float32, where each value uses 4 bytes.
4. Calculate value storage for float16, where each value uses 2 bytes.
5. Explain why neither answer predicts the total memory used during training.

Then classify each item as normally integer or floating point:

- token IDs;
- learned weights;
- class labels;
- hidden activations;
- predicted probabilities.

## 2. Dtype and device contract

For each scenario, identify whether it is valid, invalid, or merely inefficient. Explain why.

1. Integer token IDs are used to select rows from a floating-point embedding table.
2. A floating-point weight tensor is on an accelerator while its input is on the CPU.
3. A float32 input is combined with a float16 weight without an explicit precision policy.
4. Inference runs on the CPU with gradient recording enabled even though no gradients are needed.
5. Integer class IDs are marked as requiring a continuous gradient.

Write one validation check for shape, dtype, device, and gradient status.

## 3. Autograd graph inventory

Use this calculation:

> y = (xw + b)², where x = 2, w = 3, and b = 1

1. List the forward intermediate values.
2. If only `w` and `b` are tracked, identify the leaves that receive gradients.
3. State the gradients for `w` and `b`.
4. Explain what still happens—and what does not happen—when gradient recording is disabled.
5. Explain why backward does not update either parameter.

## 4. Registered model state

Inventory the Lesson 6 network with widths 10 → 64 → 16 → 3.

1. List every weight and bias shape.
2. Calculate the parameter count for each layer and the total.
3. Classify these as a trainable parameter, persistent buffer, optimizer state, or external metadata:
   - a dense-layer weight;
   - a batch-normalization running mean;
   - an adaptive optimizer's moving average;
   - the label-to-name mapping;
   - the feature-normalization configuration.
4. Explain what could go wrong if a trainable tensor exists but is not registered with the module.

## 5. Training lifecycle diagnosis

Put these stages in the correct order:

- compute the scalar loss;
- clear stale gradient buffers;
- update parameters;
- perform the forward pass;
- run backward.

Then diagnose each failure:

1. The optimizer step occurs before backward.
2. Gradients are never cleared between independent batches.
3. The loss is calculated before the prediction.
4. The forward pass is repeated after backward but before the step.
5. Parameters are updated during validation.

For each, name the incorrect state transition and the likely symptom.

## 6. Mode and gradient-context matrix

Complete the decision table.

| Activity | Module mode | Record gradients? | Why? |
|---|---|:---:|---|
| Training | | | |
| Validation | | | |
| Production inference | | | |
| Input-sensitivity explanation requiring input gradients | | | |

Explain why evaluation mode and disabled gradient recording are related in common workflows but are not the same control.

## 7. Checkpoint planning

Choose the minimum defensible checkpoint contents for each goal:

1. Deploy a fixed model for inference.
2. Resume an interrupted adaptive-optimizer training run.
3. Reproduce a published experiment six months later.

Consider model state, architecture/configuration, preprocessing, label mapping, optimizer state, scheduler state, training progress, random state, code version, dependency versions, data identity, split identity, metrics, and evaluation artifacts.

For every omitted item, be prepared to say why it is unnecessary for that goal.

## 8. Failure investigation

For each incident, identify the most likely state category, one detection signal, and one corrective action.

| Incident | State category | Detection signal | Corrective action |
|---|---|---|---|
| One layer never learns, but the rest do | | | |
| Runtime reports that tensors are on different devices | | | |
| Validation results change between identical passes | | | |
| Resumed training immediately behaves differently | | | |
| A restored model accepts inputs but predictions are nonsensical | | | |

## 9. Capstone — PyTorch execution and state contract

Create a framework-neutral contract for the capstone model. It must include:

### Tensor inventory

| Tensor | Meaning | Shape | Dtype | Device | Requires gradient? |
|---|---|---|---|---|:---:|
| | | | | | |

### Module-state inventory

List trainable parameters, persistent buffers, optimizer state, and external metadata separately.

### Autograd contract

- Which forward operations must be recorded?
- Which leaves must receive gradients?
- Which values must never receive gradients?
- What evidence proves that gradients exist and have the expected shapes?

### Lifecycle contract

Describe the required state before and after clear, forward, loss, backward, and step.

### Execution-mode matrix

Define training, validation, ordinary inference, and gradient-based explanation behavior.

### Checkpoint matrix

List the contents needed for inference, training continuation, and experiment reproduction.

### Validation gates

Include checks for shape, dtype, device, missing or non-finite gradients, mode, and checkpoint compatibility.

## Reflection

Explain PyTorch at two levels:

- **Plain language:** what problem does a training framework solve?
- **Technical:** how do tensors, autograd, modules, optimizers, modes, and checkpoints divide responsibility?
