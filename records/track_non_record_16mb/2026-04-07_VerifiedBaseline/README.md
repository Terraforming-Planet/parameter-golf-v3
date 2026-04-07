# Verified Baseline (non-record, 16MB track)

This folder is the frozen reference baseline for official OpenAI Parameter Golf FineWeb `val_bpb`.

## Run identity

- Task: `openai_parameter_golf_fineweb_val_bpb`
- Track: `non_record_16mb`
- Baseline command:

```bash
torchrun --standalone --nproc_per_node=8 train_gpt.py
```

## Verified measured baseline values

- `val_bpb`: **1.22436570**
- `val_loss`: **2.07269931**
- `training_time_seconds`: **600.038**
- `code_bytes`: **47642**
- `compressed_model_bytes`: **15815847**
- `total_bytes`: **15863489**

Values are also recorded in `submission.json` for machine-readable comparisons.
