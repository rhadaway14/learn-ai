# Engineering Lab A — Python and PyTorch Readiness

This required bridge comes after Lesson 10. It converts the Phase 2 model-training specification into a tested implementation without assuming that you already know Python.

**Time:** 6–10 hours for the supported path; 60–90 minutes for the diagnostic route.

## What you will prove

By the end, you can:

- create and activate an isolated Python environment;
- run a program and use a traceback to locate a failure;
- read values, lists, dictionaries, functions, loops, and command-line options;
- inspect tensor shape, dtype, device, and gradient state;
- distinguish model parameters, optimizer state, and checkpoint metadata;
- run tests and interpret pass, fail, and skipped results;
- train a small neural model with separate training, validation, and test evidence;
- reproduce the selected checkpoint and write the `P2-I06` evidence record.

No cloud account, paid API, Docker service, or GPU is required.

## Choose your route

### Experienced Python route

Complete setup, then run the diagnostic:

```bash
python labs/engineering_lab_a/diagnostic.py
pytest -q labs/engineering_lab_a/test_model.py
```

If both pass and you can explain every diagnostic output, continue to the implementation gate.

### Supported route

Complete Stages 1–6 in order. Each stage has an expected result and recovery step.

## Setup

Python 3.11–3.13 is supported.

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,engineering-lab-a]"
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,engineering-lab-a]"
```

Verify:

```bash
python --version
python -c "import torch; print(torch.__version__); print(torch.ones(2, 3).shape)"
```

Expected: a supported Python version, a PyTorch version, and `torch.Size([2, 3])`.

Recovery: if `import torch` fails, confirm the environment is active and rerun the install command. Do not install packages globally to work around an inactive environment.

## Stage 1 — Run a program and read an error

Run:

```bash
python labs/engineering_lab_a/diagnostic.py --demonstrate-error
```

The program catches an intentional shape error and explains the traceback boundary. Record:

1. the file and operation that failed;
2. the expected and received shapes;
3. the smallest correction consistent with the shape contract.

## Stage 2 — Map Python syntax to the model contract

Open `model.py` read-only and locate:

| Python construct | Lab responsibility |
|---|---|
| number/string | configuration and metadata |
| list/tuple | layer widths and tensor shape |
| dictionary | evidence and checkpoint manifest |
| function | one testable transformation |
| loop | repeated training epochs and batches |
| class | registered model state and forward behavior |

You are not expected to memorize syntax. Explain what each block owns and what it returns.

## Stage 3 — Inspect tensor and autograd state

Run:

```bash
python labs/engineering_lab_a/diagnostic.py
```

Before running it, predict the input, logits, and gradient shapes. Confirm the output reports:

- input `(4, 5)`;
- logits `(4,)`;
- floating-point dtype;
- CPU unless you deliberately configured another device;
- gradients shaped like their parameters after `backward()`.

## Stage 4 — Run the known-good training system

```bash
python labs/engineering_lab_a/run_lab.py --epochs 80 --learning-rate 0.03 --seed 17
```

The command writes `artifacts/engineering-lab-a/evidence.json` and the best validation checkpoint. The final test is evaluated once, after checkpoint selection.

Expected evidence:

- finite training and validation losses;
- a selected epoch between 1 and 80;
- checkpoint metadata containing feature order, seed, architecture, and selection rule;
- test metrics calculated from the reloaded selected checkpoint.

## Stage 5 — Run a controlled failure and recover

Predict what will happen, then run:

```bash
python labs/engineering_lab_a/run_lab.py --epochs 20 --learning-rate 1000000 --seed 17 --expect-failure
```

The run must stop on nonfinite or explosive loss and report the failure without promoting a checkpoint. Recover by restoring `--learning-rate 0.03` and the same seed. Changing both rate and seed would make the comparison ambiguous.

## Stage 6 — Verify and accept P2-I06

```bash
pytest -q labs/engineering_lab_a/test_model.py
```

Create `P2-I06-tested-reference-implementation.md` from [the evidence template](EVIDENCE_TEMPLATE.md). Accept the increment only when:

- the known-good run and all lab tests pass;
- shapes and output semantics match P2-I01;
- every trainable parameter receives a finite gradient, satisfying P2-I02;
- lifecycle and checkpoint contents satisfy P2-I03;
- validation selects the checkpoint and test remains sealed until selection, satisfying P2-I04;
- the failure experiment and recovery satisfy P2-I05;
- another learner can reproduce the evidence from the documented commands.

## What comes next

Passing this lab establishes the programming boundary for later coding labs. It does not mean every future implementation detail is assumed; later lessons must still teach new APIs and algorithms before asking you to use them.
