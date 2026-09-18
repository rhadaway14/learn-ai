from __future__ import annotations

import argparse
from pathlib import Path

from model import RunConfig, save_checkpoint, train, write_evidence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train and verify the Engineering Lab A delivery-risk model.")
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--learning-rate", type=float, default=0.03)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--expect-failure", action="store_true")
    parser.add_argument("--output", type=Path, default=Path("artifacts/engineering-lab-a"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        model, evidence = train(RunConfig(seed=args.seed, epochs=args.epochs, learning_rate=args.learning_rate))
    except RuntimeError as error:
        print(f"FAILURE SIGNAL: {error}")
        return 0 if args.expect_failure else 1
    if args.expect_failure:
        print("Expected a controlled failure, but training remained stable.")
        return 1
    save_checkpoint(args.output / "best-checkpoint.pt", model, evidence)
    write_evidence(args.output / "evidence.json", evidence)
    print(f"selected_epoch={evidence['selected_epoch']} test_loss={evidence['test_loss']:.4f}")
    print(f"evidence={args.output / 'evidence.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
