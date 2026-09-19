# Phase 2 Cumulative Lab — Neural Delivery Risk

This is the first required container lab. Phase 1 remains browser-only. Phase 2 introduces Docker deliberately because the learner is now studying persistent evidence, service boundaries, real PyTorch training, checkpoint promotion, and inference through an application API.

## Requirements and first start

- Docker Desktop or Docker Engine with Compose v2;
- at least 8 GB system memory;
- approximately 3 GB free disk space for images, build cache, database, and CPU PyTorch dependencies;
- internet access for the first image build.

The first start is slower because Docker downloads base images and the CPU-only PyTorch wheel. Later starts reuse the local cache.

## Start

```bash
make phase2-start
```

Open <http://localhost:8090>. The API is also inspectable at <http://localhost:8091/health>.

The walkthrough follows this loop: orient, import, predict, build, observe, break, diagnose, recover, use, verify, and save.

## Diagnose startup

```bash
make phase2-status
docker compose --profile phase2 logs phase2-api
docker compose --profile phase2 logs phase2-db
```

The web page reports each service boundary separately. A database failure cannot be mistaken for a model-training failure.

## Verify

```bash
make phase2-test
```

This runs the verification inside the same API image used by the lab; no host Python installation is required. The automated gate requires recall of at least 0.25, accuracy more than 0.03 above the majority baseline, a validation-selected checkpoint before the final epoch, finite parameter gradients, and exactly one sealed-test evaluation. It also confirms that the deliberately explosive learning rate fails closed.

## Reset and clean

To deliberately erase Phase 2 database records and checkpoints, then restart from the seeded state:

```bash
make phase2-reset
```

To remove the Phase 2 containers and volumes without restarting:

```bash
make phase2-clean
```

Both commands remove only the explicitly named `learn-ai-phase2-data` and `learn-ai-phase2-artifacts` volumes. They do not change lesson progress, Phase 1 browser storage, or the Foundations API volume. Normal stopping with `Ctrl+C` preserves the Phase 2 volumes.

## Design reference

Read [SPEC.md](SPEC.md) for the phase contract, service boundaries, accessibility requirements, numeric acceptance gate, reasoning gate, and explicit non-goals.
