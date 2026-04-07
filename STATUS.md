# STATUS.md — Parameter Golf v3 State

Date: 2026-04-07

## Current repository status

### Completed

- Repository baseline training path is active at `train_gpt.py` and synchronized into `records/non_record_submission_template/train_gpt.py`.
- Compatibility-oriented training-path settings for current RunPod/PyTorch environments are in place:
  - no `enable_gqa` argument in `scaled_dot_product_attention`
  - no `torch.compile` wrapping for `zeropower_via_newtonschulz5`
  - no `torch.compile` wrapping for `base_model`
- A verified baseline record exists at `records/track_non_record_16mb/2026-04-07_VerifiedBaseline/` with measured `val_bpb`, `val_loss`, training time, and artifact byte totals from a completed run.

### Current verification state

- Verified baseline run: complete.
- Baseline values are stored in the verified baseline folder (`README.md` + `submission.json`).
- Next work is limited to controlled, single-change FineWeb `val_bpb` experiments.

## Benchmark scope (frozen)

- **Official benchmark path only:** `openai_parameter_golf_fineweb_val_bpb`.
- **Custom datasets are frozen and excluded from benchmark planning and tuning.**
- No project-structure redesign; only small, high-signal iterations on the official path.

## Controlled experiment variants (next)

1. **Variant A (architecture-only):** `NUM_KV_HEADS=8` (MQA/GQA simplification removed while keeping all other settings fixed).
2. **Variant B (training-only):** `WARMDOWN_ITERS=1800` (longer decay tail, all architecture/export settings unchanged).
3. **Variant C (compression/export-only):** `ZLIB_LEVEL=6` (export-level-only change, train/eval graph unchanged).
