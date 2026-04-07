# Non-record Submission Template (Parameter Golf)

This folder is a template for preparing an official-style **non-record** OpenAI Parameter Golf submission package.

## What goes here

Required files for submission packaging:

1. `README.md` (this file, updated with run details)
2. `submission.json` (metadata + measured outcomes)
3. `train_gpt.py` (runnable script, baseline-compatible workflow)
4. `train.log` / `train_run_*.log` (real logs from training runs)
5. Any additional small dependency files needed to run this folder standalone

## Rules this template is designed to respect

- Target metric stays **`val_bpb` on FineWeb validation**.
- Total counted artifact must stay under **16,000,000 bytes**.
- Record-track runs must be reproducible in **10 minutes on 8xH100**.
- Evaluation must be self-contained, with **no external network/download calls**.

## train_gpt.py note

`train_gpt.py` in this template is inherited from the repository baseline as a compatibility starting point. Replace or edit it only as needed for your method, while keeping workflow compatibility with official Parameter Golf evaluation.

## How to use this template

1. Copy this folder to a new dated run folder under `records/`.
2. Run training and save logs in that new folder.
3. Fill in `submission.json` with real measured values only.
4. Update this README with:
   - architecture/method summary
   - exact command(s)
   - hardware details
   - measured `val_bpb`
   - artifact byte accounting

Do **not** leave placeholder values in a real submission.
