from __future__ import annotations

import argparse

import torch

from model import DeliveryRiskNet


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--demonstrate-error", action="store_true")
    args = parser.parse_args()
    model = DeliveryRiskNet()
    if args.demonstrate_error:
        try:
            model(torch.ones(4, 4))
        except ValueError as error:
            print(f"EXPECTED ERROR: {error}")
            return 0
        return 1
    features = torch.ones(4, 5)
    logits = model(features)
    loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, torch.tensor([0.0, 1.0, 0.0, 1.0]))
    loss.backward()
    print({"input_shape": tuple(features.shape), "logit_shape": tuple(logits.shape), "dtype": str(features.dtype), "device": str(features.device), "loss": loss.detach().item()})
    for name, parameter in model.named_parameters():
        print({"parameter": name, "shape": tuple(parameter.shape), "gradient_shape": tuple(parameter.grad.shape)})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
