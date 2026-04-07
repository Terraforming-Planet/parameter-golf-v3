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
- A verified baseline run record now exists at `records/track_non_record_16mb/2026-04-07_VerifiedBaseline/`, including measured baseline `val_bpb`, training time, and artifact byte accounting from the completed baseline run.

### Current verification state

- Baseline verification is complete for the repository baseline path.
- Verified baseline metrics and size totals are captured in the dedicated verified baseline record folder.
- Further tuning runs remain optional and should be added as separate dated records.

## Priority

**Current top priority is incremental improvement over the verified baseline** while preserving reproducibility and submission consistency.

## Benchmark scope clarification

The following three datasets are tracked as **auxiliary evaluation assets only** (diagnostics/sanity checks), not the official benchmark path:

- Cube-Multi-Object-Consistency-Dataset
- planet-alphabet-mapping-1-26
- geometric_optics_physical_consistency_eval

The **official benchmark path remains FineWeb validation with `val_bpb`**.
