# RUN.md — Clean Baseline Training (OpenAI Parameter Golf)

This document prepares a **clean, runnable baseline** while staying compatible with the official `openai/parameter-golf` workflow.

## 1) Setup

```bash
cd /workspace/parameter-golf-v3
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 2) Required environment variables

`train_gpt.py` has defaults, but for reproducibility set these explicitly:

```bash
export DATA_PATH=./data/datasets/fineweb10B_sp1024
export TOKENIZER_PATH=./data/tokenizers/fineweb_1024_bpe.model
export VOCAB_SIZE=1024
export RUN_ID=baseline_sp1024
```

Optional common controls:

```bash
export SEED=1337
export ITERATIONS=20000
export MAX_WALLCLOCK_SECONDS=600
export VAL_LOSS_EVERY=1000
```

## 3) Download the FineWeb dataset + tokenizer artifacts

Use the repository's official cached dataset script:

```bash
python3 data/cached_challenge_fineweb.py --variant sp1024
```

If you need a smaller smoke dataset while validating setup:

```bash
python3 data/cached_challenge_fineweb.py --variant sp1024 --train-shards 1
```

## 4) Run baseline training on 1 GPU

```bash
RUN_ID=baseline_sp1024 \
DATA_PATH=./data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=./data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
torchrun --standalone --nproc_per_node=1 train_gpt.py
```

## 5) Expected final outputs

The baseline script prints all of the following at the end of a run:

- `final_int8_zlib_roundtrip ... val_bpb:...`
- `final_int8_zlib_roundtrip_exact ... val_bpb:...`
- `final_val_bpb:...`
- `final_artifact_size_bytes:...`

The compressed model artifact is written to:

- `final_model.int8.ptz`

## 6) Save/export the trained model artifact

The training script already writes `final_model.int8.ptz` in the repository root. To save it to a run folder:

```bash
mkdir -p artifacts/${RUN_ID}
cp -f final_model.int8.ptz artifacts/${RUN_ID}/final_model.int8.ptz
```

## 7) Evaluation phase: avoid external downloads

To ensure evaluation does not require external network downloads:

1. Run dataset download once before training (step 3).
2. Keep local files present:
   - `${DATA_PATH}/fineweb_train_*.bin`
   - `${DATA_PATH}/fineweb_val_*.bin`
   - `${TOKENIZER_PATH}`
3. During evaluation, run with offline flags:

```bash
export HF_HUB_OFFLINE=1
export HF_DATASETS_OFFLINE=1
```

`train_gpt.py` reads local shard files and local tokenizer path directly; it does not fetch remote assets during evaluation when these files already exist.
