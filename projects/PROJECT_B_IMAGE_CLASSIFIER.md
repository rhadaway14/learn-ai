# Project B — Image Classifier

## Mission

Build and evaluate a PyTorch image-classification pipeline on a small public dataset.

## Required work

1. Inspect labels, class balance, corrupt samples, and licensing.
2. Implement Dataset and DataLoader pipelines.
3. Train a small CNN before using transfer learning.
4. Track train and validation loss, accuracy, per-class recall, and runtime.
5. Add augmentation, regularization, checkpointing, and early stopping separately.
6. Compare at least three seeds.
7. Analyze the most confident mistakes.

## Deliverables

- training and inference entry points;
- saved configuration separate from weights;
- sample predictions with confidence;
- error-analysis gallery;
- model card and reproducibility manifest.

## Acceptance

- CPU execution is documented even if GPU is preferred;
- train and inference preprocessing match;
- best checkpoint is selected on validation data;
- final metrics use an untouched test set.
