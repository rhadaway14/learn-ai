# Project C — Small Language Model

## Mission

Train a small causal transformer on a licensed text corpus and understand every major tensor boundary.

## Required work

1. Establish character and bigram baselines.
2. Build or select a tokenizer and measure compression.
3. Create shifted causal training batches.
4. Implement embeddings, causal attention, multi-head attention, FFN, residuals, and normalization.
5. train with checkpoints and validation loss;
6. compare greedy, temperature, top-k, and top-p decoding;
7. inspect memorization and held-out generalization.

## Deliverables

- architecture diagram with tensor shapes;
- parameter-count calculation;
- training curves and sampled text;
- decoding comparison;
- limitations and data-provenance note.

## Acceptance

- future-token leakage test passes;
- transformer beats the bigram validation baseline;
- generation is reproducible with a fixed seed;
- corpus licensing and limitations are explicit.
