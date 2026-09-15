# Repository Instructions

## Purpose

This repository is a cumulative, hands-on AI engineering curriculum. Preserve the progression from primitives to frameworks.

## Lesson standard

Every implemented lesson should contain:

- `README.md` with motivation, theory, vocabulary, walkthrough, experiments, checkpoint questions, and modern-AI connection;
- runnable reference code;
- learner exercises or an experiment workbook;
- separate reference solutions or reference notes;
- deterministic automated tests where practical;
- no required paid service unless a local or free alternative is documented.

## Engineering rules

- Support Python 3.11–3.13 unless a documented ML dependency prevents it.
- Pin compatible dependency ranges in `pyproject.toml`.
- Seed randomized educational examples.
- Write plots to an `outputs/` directory; do not require a desktop display.
- Never commit API keys, model credentials, datasets with restricted licenses, virtual environments, or generated model weights.
- Prefer direct NumPy/PyTorch implementations before high-level orchestration frameworks.
- Explain tensor shapes at each important boundary.
- Keep tests fast; mark expensive or GPU-specific tests explicitly.

## Before committing

Run:

```bash
python -m pytest
```

Run every new or changed lesson entry point. Update `ROADMAP.md` and `PROGRESS.md` when a lesson becomes fully implemented.
