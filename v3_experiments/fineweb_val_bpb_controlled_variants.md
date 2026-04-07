# FineWeb `val_bpb` Controlled Variants (Frozen Scope)

Scope constraints for this plan:

- Official benchmark path only: `openai_parameter_golf_fineweb_val_bpb`
- No custom dataset integration
- No broad refactors
- Single main idea per variant

## Baseline re-run command (RunPod)

```bash
RUN_ID=baseline_rerun_$(date -u +%Y%m%dT%H%M%SZ) \
torchrun --standalone --nproc_per_node=8 train_gpt.py
```

## Variant A — Architecture-only

Main change: increase KV heads to full heads (`NUM_KV_HEADS=8`) while leaving all training and export settings unchanged.

Why this might improve `val_bpb`: less key/value sharing can improve attention expressivity and reduce underfitting in a small model.

```bash
RUN_ID=variantA_arch_kv8_$(date -u +%Y%m%dT%H%M%SZ) \
NUM_KV_HEADS=8 \
torchrun --standalone --nproc_per_node=8 train_gpt.py
```

## Variant B — Training hyperparameter-only

Main change: increase warmdown length (`WARMDOWN_ITERS=1800`) with architecture/export fixed.

Why this might improve `val_bpb`: longer LR taper can reduce late-training noise and improve final validation compression.

```bash
RUN_ID=variantB_train_warmdown1800_$(date -u +%Y%m%dT%H%M%SZ) \
WARMDOWN_ITERS=1800 \
torchrun --standalone --nproc_per_node=8 train_gpt.py
```

## Variant C — Compression/export-only

Main change: lower zlib compression level (`ZLIB_LEVEL=6`) with train graph and optimizer settings unchanged.

Why this might improve `val_bpb`: faster export/decompression step can reduce end-of-run overhead variability; in strict wallclock environments this can preserve consistency for final measured eval.

```bash
RUN_ID=variantC_export_zlib6_$(date -u +%Y%m%dT%H%M%SZ) \
ZLIB_LEVEL=6 \
torchrun --standalone --nproc_per_node=8 train_gpt.py
```

## Experiment table

| Name | What changed | Expected upside | Main risk |
|---|---|---|---|
| Baseline re-run | No change | Reconfirm baseline stability | Natural run-to-run noise |
| Variant A (architecture) | `NUM_KV_HEADS: 4 -> 8` | Better attention fidelity, potential lower `val_bpb` | Higher memory/compute pressure |
| Variant B (training) | `WARMDOWN_ITERS: 1200 -> 1800` | Smoother late optimization, potential lower `val_bpb` | Can under-train if decay is too slow |
| Variant C (export) | `ZLIB_LEVEL: 9 -> 6` | Faster export/roundtrip stage under wallclock variability | Larger artifact size; little/no metric gain |
