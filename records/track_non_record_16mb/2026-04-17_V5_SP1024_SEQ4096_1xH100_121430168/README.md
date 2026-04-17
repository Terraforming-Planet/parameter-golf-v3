# Non-Record Submission: V5 SP1024 + Seq4096 (1xH100)

This is a non-record submission for OpenAI Parameter Golf.

It documents a V5 run on the official FineWeb sp1024 path using `TRAIN_SEQ_LEN=4096` and a single H100 GPU. This submission does **not** claim record-track status because it was not produced under the official 10-minute / 8xH100 record-setting condition.

## Summary

- Run ID: `v5_sp1024_top10_a`
- Date: `2026-04-17`
- Track: `non-record-16mb`
- GPU: `1xH100`
- Dataset: `fineweb10B_sp1024`
- Tokenizer: `sp1024` (`fineweb_1024_bpe.model`)
- Final exact post-quant roundtrip `val_bpb`: **1.21430168**
- Final exact post-quant roundtrip `val_loss`: **2.05029752**
- Final logged pre-quant `val_bpb`: `1.2089`
- Final logged pre-quant `val_loss`: `2.0411`
- Step stop: `6000`
- Logged train time: `3218242 ms` (`3218.242 s`)
- Total submission size: **15841388 bytes**

## Training configuration

- `world_size=1`
- `grad_accum_steps=8`
- `train_batch_tokens=524288`
- `train_seq_len=4096`
- `warmup_steps=30`
- `seed=1337`

## Model

- Parameters: `17059912`
- `num_layers=9`
- `model_dim=512`
- `num_heads=8`
- `num_kv_heads=4`
- `mlp_mult=2`
- `tie_embeddings=True`

## Serialization

- Raw `final_model.pt`: `67224983` bytes
- Quantized `final_model.int8.ptz`: `15793702` bytes
- `train_gpt.py` code size: `47686` bytes
- Quant payload bytes: `17178912`
- Raw torch bytes before zlib: `17224025`
- Payload compression ratio: `3.91x`

## Memory

- Peak allocated: `10242 MiB`
- Peak reserved: `10556 MiB`

## Included files

- `README.md`
- `submission.json`
- `results.tsv`
- `train_gpt.py`
- `train.log`
- `final_model.int8.ptz`

## Notes

- Pre-quant metrics are only available in the log at 4-decimal precision, so `submission.json` keeps `pre_quant_val_loss` and `pre_quant_val_bpb` as `null` to avoid fake precision.
- The total submission size here is `bytes_model_int8_zlib + bytes_code = 15793702 + 47686 = 15841388`.
