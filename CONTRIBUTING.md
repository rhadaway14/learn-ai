# Contributing

This repository is primarily a personal learning path, but the code should retain production-quality habits.

## Adding a lesson

1. Use the next numbered directory under `lessons/`.
2. Follow the lesson standard in `AGENTS.md`.
3. Add fast, deterministic tests.
4. Add any dependency through `pyproject.toml` with a compatible version range.
5. Update the roadmap and progress checklist.
6. Run the full test suite.

## Commit style

Use a short imperative subject, for example:

```text
Add attention implementation lab
```

Keep generated datasets, outputs, caches, credentials, and model weights out of commits.
