# Parameter Golf Submission Repo

This repository is a clean, competition-focused workspace for building an **official OpenAI Parameter Golf** submission.

## Primary objective

Train a language model for the OpenAI Parameter Golf challenge and optimize the official metric:

- **Metric:** `val_bpb` on FineWeb validation
- **Artifact cap:** **16,000,000 bytes** total (code + compressed model artifact)
- **Record track constraint:** train in **10 minutes on 8xH100**
- **Evaluation constraint:** self-contained evaluation, with **no external downloads or network calls during evaluation**

## Repository layout

- `train_gpt.py` — baseline-compatible training script at repo root for local iteration.
- `records/non_record_submission_template/` — template folder structured for official-style submission artifacts.
- `records/track_non_record_16mb/2026-04-07_VerifiedBaseline/` — verified baseline record with measured values.
- `aux_eval/` — auxiliary diagnostics/custom dataset experiments (not part of official submission path).

## Official submission path

Use `records/non_record_submission_template/` as the starting point for preparing new submission-ready folders, then copy it into a dated run folder under `records/` and replace placeholders with measured values.

A verified baseline reference record is already available at:

- `records/track_non_record_16mb/2026-04-07_VerifiedBaseline/`

This provides a consistent measured starting point for future tuning and comparisons.

## Submission status guidance

- Baseline verification has been completed and a verified baseline record is checked in.
- Official submission values (metric, timing, byte counts, hardware/runtime details) in new records must still be filled only from real measured runs.
- Keep template files as scaffolding only; keep measured values in dated run folders.

## Auxiliary path (non-official)

Use `aux_eval/` for custom datasets and diagnostics only. Keep these experiments clearly separated from the official FineWeb/`val_bpb` submission workflow.
