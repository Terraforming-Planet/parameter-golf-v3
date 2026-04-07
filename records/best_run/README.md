# Best Verified Run: `arch_v1_refined`

## Overview

This folder is the primary submission candidate for this repository's OpenAI Parameter Golf workflow.
It contains the best verified run artifact and the files needed to inspect or reuse that run configuration.

## Final result

- `run_id`: `arch_v1_refined`
- `final_val_bpb`: **1.86808647**
- `final_val_loss`: **3.15418576**
- `final_artifact_size_bytes`: **4,971,557**
- `total_submission_size_int8_zlib`: **5,019,795**
- `code_size_bytes`: **48,238**

## Architecture summary

- Decoder-only GPT architecture
- `NUM_LAYERS=8`
- `MODEL_DIM=384`
- `NUM_HEADS=8`
- `NUM_KV_HEADS=2`
- `MLP_MULT=2`

## Tokenizer

- SentencePiece tokenizer
- `TOKENIZER_PATH=./data/tokenizers/fineweb_1024_bpe.model`
- `VOCAB_SIZE=1024`

## Training setup

- Dataset path: `./data/datasets/fineweb10B_sp1024`
- Warmup: `WARMUP_STEPS=60`
- Total iterations: `ITERATIONS=300`
- Validation cadence: `VAL_LOSS_EVERY=50`
- Train logging cadence: `TRAIN_LOG_EVERY=25`
- Launch mode: single-process `torchrun`

## Exact command

```bash
RUN_ID=arch_v1_refined
DATA_PATH=./data/datasets/fineweb10B_sp1024
TOKENIZER_PATH=./data/tokenizers/fineweb_1024_bpe.model
VOCAB_SIZE=1024
NUM_LAYERS=8
MODEL_DIM=384
NUM_HEADS=8
NUM_KV_HEADS=2
MLP_MULT=2
WARMUP_STEPS=60
ITERATIONS=300
VAL_LOSS_EVERY=50
TRAIN_LOG_EVERY=25
torchrun --standalone --nproc_per_node=1 train_gpt.py
```

## Included files

- `README.md` — run summary and reproducibility notes
- `train.log` — captured training/validation log
- `train_gpt.py` — script snapshot used for this run
- `submission.json` — machine-readable measured values for this run
- `final_model.int8.ptz` — compressed model artifact

## Reproducibility note

This is a measured run record, not a claim of guaranteed identical replay across different hardware/software stacks.
Use the command and script snapshot in this folder as the closest reproducible reference.

## Competition constraint note

This run record is intended for OpenAI Parameter Golf submission workflows and keeps reported values grounded in measured run outputs only.
