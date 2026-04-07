# OpenAI Parameter Golf Submission Workspace

This repository is maintained as a submission-focused workspace for the OpenAI Parameter Golf challenge.

## Primary objective

Train and package a model for the official FineWeb evaluation path (`openai_parameter_golf_fineweb_val_bpb`) while respecting submission byte constraints.

## Current best verified result

- `run_id`: `arch_v1_refined`
- `final_val_bpb`: **1.86808647**
- `final_val_loss`: **3.15418576**
- `final_artifact_size_bytes`: **4,971,557**
- `total_submission_size_int8_zlib`: **5,019,795**
- `code_size_bytes`: **48,238**

Primary candidate folder:

- `records/best_run/`

## Clean repository layout

- `train_gpt.py` — current root training script used for active iteration.
- `records/best_run/` — single clearly identified best verified run (primary submission candidate).
- `records/non_record_submission_template/` — official-style template preserved for compatibility.
- `archive/` — historical and exploratory material moved out of the main submission path.
- `data/` — dataset/tokenizer preparation and metadata helpers.

## Official submission path

Use `records/best_run/` for the currently verified candidate.

For future runs, start from `records/non_record_submission_template/`, run training, then write measured outputs into a new run folder under `records/` and update best-run designation only after verification.

## Official vs archived material

- **Official-facing path:** root `train_gpt.py`, `records/best_run/`, and `records/non_record_submission_template/`.
- **Archived path:** `archive/` contains prior experiments, diagnostics, and historical runs retained for reference.

No claims beyond measured values in checked-in artifacts are made in this repository.
