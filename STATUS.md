# STATUS.md — Parameter Golf v3 State

Date: 2026-04-07

## Current repository status

### Completed

- Baseline training scaffold is in place at repository root (`train_gpt.py`) and in the non-record submission template.
- Compatibility-oriented training-path changes are present for current RunPod/PyTorch environments:
  - no `enable_gqa` argument in `scaled_dot_product_attention`
  - no `torch.compile` wrapping for `zeropower_via_newtonschulz5`
  - no `torch.compile` wrapping for `base_model`
- Submission packaging scaffold exists under `records/non_record_submission_template/` with template `README.md`, `submission.json`, and `train_gpt.py`.

### Still unverified

- End-to-end baseline run completion in the current environment (including successful final artifact generation).
- Verified official benchmark numbers (`val_bpb` on FineWeb validation) from a fully successful run.
- Final byte accounting with verified compressed model artifact for submission fields.
- Required submission artifacts are pending verification (final logs, measured metric values, artifact size totals).

## Priority

**Current top priority is baseline execution stability** (i.e., getting deterministic, repeatable baseline training/evaluation runs to complete cleanly in current runtime stacks before performance tuning).

## Benchmark scope clarification

The following three datasets are tracked as **auxiliary evaluation assets only** (diagnostics/sanity checks), not the official benchmark path:

- Cube-Multi-Object-Consistency-Dataset
- planet-alphabet-mapping-1-26
- geometric_optics_physical_consistency_eval

The **official benchmark path remains FineWeb validation with `val_bpb`**.
