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
- `aux_eval/` — auxiliary diagnostics/custom dataset experiments (not part of official submission path).

## Official submission path

Use `records/non_record_submission_template/` as the starting point for preparing a submission-ready folder:

- `README.md`
- `submission.json`
- `train_gpt.py`
- train logs and artifact notes

When you have real results, copy this template into a dated run folder under `records/` and replace placeholders with measured values.


## Submission status guidance

- The submission scaffold exists, but it is still a template until a run is fully verified.
- Official submission values (metric, timing, byte counts, hardware/runtime details) must only be filled in after a verified run.
- Required artifacts are currently pending verification (final logs, final compressed artifact size accounting, and verified FineWeb `val_bpb`).

## Auxiliary path (non-official)

Use `aux_eval/` for custom datasets and diagnostics only. Keep these experiments clearly separated from the official FineWeb/`val_bpb` submission workflow.
