from __future__ import annotations

import json

from .model import TrainingConfig, train_model


def main() -> int:
    trained = train_model(TrainingConfig())
    evidence = trained.evidence
    summary = {
        "baseline_accuracy": evidence["baseline"]["accuracy"],
        "model_accuracy": evidence["sealed_test"]["accuracy"],
        "model_recall": evidence["sealed_test"]["recall"],
        "selected_epoch": evidence["training"]["selected_epoch"],
        "configured_epochs": evidence["configuration"]["epochs"],
        "acceptance": evidence["acceptance"],
    }
    print(json.dumps(summary, indent=2))
    if not evidence["acceptance"]["passed"]:
        print("VERIFICATION FAILED: the known-good model did not pass every gate")
        return 1

    try:
        train_model(
            TrainingConfig(
                epochs=40,
                learning_rate=1_000_000,
                patience=10,
            )
        )
    except RuntimeError as error:
        print(f"EXPECTED FAILURE OBSERVED: {error}")
        print("PHASE 2 MODEL VERIFICATION PASSED")
        return 0

    print("VERIFICATION FAILED: the explosive run did not fail closed")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
