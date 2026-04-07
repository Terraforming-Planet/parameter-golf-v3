# Auxiliary Evaluation (Custom Diagnostics Only)

This folder is for **custom datasets and diagnostic experiments** that are intentionally separate from the official Parameter Golf submission path.

## Scope

- Allowed: ablations, sanity checks, custom corpus diagnostics, profiling notes.
- Not allowed here: official submission artifacts or claims replacing FineWeb `val_bpb`.

Official submission materials belong under `records/`.


## Custom HF dataset workflow

Use `data/download_hf_dataset_and_tokenize.py` to convert custom Hugging Face datasets into `fineweb_train_*.bin` / `fineweb_val_*.bin` shards, then point `DATA_PATH` at that output directory for auxiliary training runs.
