# Phase 2 Pilot Specification — Neural Delivery Risk

## Decision

Phase 1 remains a zero-install browser experience. Phase 2 is the first required container lab because persistent runs, real PyTorch training, checkpoint promotion, and application/API boundaries are part of the learning objective.

The pilot extends the Northstar delivery-risk application. It does not create a separate demonstration. The Phase 1 majority baseline and prediction contract are evaluated against the same sealed test population as the Phase 2 neural model.

## Learner outcome

The learner starts three services, opens one browser URL, trains and diagnoses a neural model, promotes a validation-selected checkpoint, compares it with the baseline, scores a new project, and downloads a reviewable Phase 2 artifact.

## Phase contract

### Inputs

- a Phase 1 artifact with schema version `1.0`;
- the five-feature Northstar prediction contract;
- the Phase 2 lesson increments P2-I01 through P2-I05;
- a seeded dataset with a stable sealed test partition.

The teaching dataset includes seeded Gaussian noise (`σ = 0.6`) in the latent risk process. Runs remain reproducible, but labels are not a perfectly recoverable function of the visible features. This preserves the course's irreducible-error, threshold, and generalization lessons.

### Outputs

- a selected PyTorch checkpoint;
- training and validation history;
- one sealed-test evaluation;
- baseline and neural-model metrics;
- a controlled failure and recovery record;
- a versioned `phase2-neural-risk-attempt-NN.json` artifact.

### Downstream consumer

Phase 3 adds project-description tokenization and embeddings to the same intake and evidence model.

## Service boundary

| Service | Responsibility |
|---|---|
| `phase2-web` | Guided walkthrough, accessible visual evidence, comparison, prediction, artifact download |
| `phase2-api` | Dataset contract, PyTorch training, inference, acceptance checks, artifact construction |
| `phase2-db` | Imported Phase 1 evidence, run metadata, metrics, and artifact JSON |

Training is synchronous because the seeded CPU workload is deliberately small. A queue is not introduced until the course teaches asynchronous production workloads.

## Required learner loop

1. Orient to the current Phase 1 baseline.
2. Inspect the tensor-shape contract and predict expected model behavior.
3. Build by selecting a bounded training configuration.
4. Observe curves, metrics, gradients, and checkpoint selection.
5. Break training with an explosive learning rate.
6. Diagnose the failure signal.
7. Recover from the same seed with one changed control.
8. Verify automated and reasoning gates.
9. Use the promoted model on a new project.
10. Save the evidence artifact.

## Numeric acceptance gate

The known-good run passes only when all conditions hold:

- sealed-test recall is at least `0.25`;
- sealed-test accuracy is greater than majority-class accuracy plus `0.03`;
- the selected checkpoint epoch is earlier than the configured final epoch;
- every trainable parameter receives a finite gradient;
- the sealed test is evaluated exactly once;
- an identical seed and configuration reproduce the selected epoch and metrics.

## Reasoning gate

Automated success is necessary but insufficient. The artifact must also include the learner's prediction, observed evidence, failure diagnosis, recovery explanation, promotion rationale, and one limitation that the reported metrics do not establish.

Each reasoning response must contain at least 18 distinct words across two substantive sentences, name the Northstar case, express a causal or conditional relationship, and use concepts specific to that prompt. Repeated characters, generic filler, and keyword-only text fail closed.

The inference endpoint returns an uncalibrated model risk `score`. The UI must not label this value as a probability unless a later lesson adds and verifies calibration.

## Accessibility contract

- all controls and steps are keyboard operable;
- focus is visible;
- state is never communicated only through color;
- charts have a persistent table equivalent;
- status and step changes use restrained live regions;
- animation respects `prefers-reduced-motion`;
- the interface remains usable at 320 CSS pixels;
- training results remain visible after animation completes.

## Recovery contract

`make phase2-reset` restores seeded database and artifact state without requiring a new clone. Container runs keep checkpoints and evidence in explicitly named Phase 2 volumes; direct host experiments use the ignored `artifacts/` directory. `make phase2-clean` deliberately removes only the Phase 2 containers, volumes, and generated artifacts.

## Out of scope for the pilot

- Redis, object storage, Grafana, and a separate job worker;
- a browser IDE or arbitrary host-file mutation;
- GPU requirements;
- hosted APIs or paid services;
- multi-user authentication.
