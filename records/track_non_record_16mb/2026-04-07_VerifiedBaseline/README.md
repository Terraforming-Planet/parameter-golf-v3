# Verified Baseline (non-record, 16MB track)

This folder captures a verified baseline reference package for the current repository baseline workflow.

## Source and intent

- Baseline method: repository baseline `train_gpt.py` compatibility path.
- Metric target: FineWeb validation `val_bpb`.
- Purpose: provide a concrete measured baseline record instead of relying only on the template scaffold.

## Verified measured baseline values

- `val_bpb`: **1.22436570**
- `val_loss`: **2.07269931**
- `training_time_seconds`: **600.038**
- `code_bytes`: **47642**
- `compressed_model_bytes`: **15815847**
- `total_bytes`: **15863489**

These values are recorded in `submission.json` and are intended as a stable baseline reference for future comparisons.
