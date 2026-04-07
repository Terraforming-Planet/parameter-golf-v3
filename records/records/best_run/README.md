Best Run – Parameter Golf Submission

Result

final_val_bpb: 1.86808647

Run ID

arch_v1_refined

Description

This is the best verified training run for this repository, optimized under the Parameter Golf constraints.

Model

- Quantized: int8 + zlib
- Final artifact size: ~5MB (within 16MB limit)

Training setup

- Dataset: FineWeb (sp1024)
- Tokenizer: SentencePiece (1024 vocab)
- Context length: 1024
- Iterations: 300
- Warmup steps: 60

Command used

RUN_ID=arch_v1_refined \
DATA_PATH=./data/datasets/fineweb10B_sp1024 \
TOKENIZER_PATH=./data/tokenizers/fineweb_1024_bpe.model \
VOCAB_SIZE=1024 \
NUM_LAYERS=8 \
MODEL_DIM=384 \
NUM_HEADS=8 \
NUM_KV_HEADS=2 \
MLP_MULT=2 \
WARMUP_STEPS=60 \
ITERATIONS=300 \
VAL_LOSS_EVERY=50 \
TRAIN_LOG_EVERY=25 \
torchrun --standalone --nproc_per_node=1 train_gpt.py

Files

- final_model.int8.ptz – final compressed model
- train.log – full training log
- train_gpt.py – training script
- submission.json – submission config
