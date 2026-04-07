"""Download a Hugging Face dataset and export train/val token shards compatible with train_gpt.py.

This is intended for auxiliary/custom experiments (non-official submission path).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import sentencepiece as spm
from datasets import Dataset, IterableDataset, load_dataset

DATAFILE_MAGIC = 20240520
DATAFILE_VERSION = 1
DEFAULT_DATASET_ID = "8Planetterraforming/Cube-Multi-Object-Consistency-Dataset"


def write_datafile(path: Path, toks: np.ndarray) -> None:
    if len(toks) >= 2**31:
        raise ValueError("token count too large")
    header = np.zeros(256, dtype="<i4")
    header[0] = DATAFILE_MAGIC
    header[1] = DATAFILE_VERSION
    header[2] = len(toks)
    toks = np.asarray(toks)
    if toks.dtype != np.uint16:
        if not ((0 <= toks).all() and (toks < 2**16).all()):
            raise ValueError("token dictionary too large for uint16")
        toks = toks.astype("<u2", copy=False)
    else:
        toks = toks.astype("<u2", copy=False)

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        f.write(header.tobytes())
        f.write(toks.tobytes())


def row_to_text(row: dict[str, Any], text_columns: list[str] | None) -> str:
    if text_columns:
        chunks = []
        for col in text_columns:
            if col in row and row[col] is not None:
                chunks.append(str(row[col]))
        if chunks:
            return "\n\n".join(chunks).strip()

    preferred = [
        "text",
        "prompt",
        "response",
        "instruction",
        "input",
        "output",
        "question",
        "answer",
        "content",
    ]
    chunks = [str(row[c]) for c in preferred if c in row and row[c] is not None]
    if chunks:
        return "\n\n".join(chunks).strip()

    return json.dumps(row, ensure_ascii=False, sort_keys=True)


def load_split(dataset_id: str, config: str | None, split: str, streaming: bool):
    kwargs: dict[str, Any] = {"split": split, "streaming": streaming}
    if config:
        kwargs["name"] = config
    return load_dataset(dataset_id, **kwargs)


def tokenize_rows(
    ds: Dataset | IterableDataset,
    sp: spm.SentencePieceProcessor,
    *,
    max_docs: int,
    text_columns: list[str] | None,
    append_eos: bool,
) -> list[np.ndarray]:
    eos_id = int(sp.eos_id())
    docs: list[np.ndarray] = []
    for i, row in enumerate(ds):
        if max_docs > 0 and i >= max_docs:
            break
        text = row_to_text(dict(row), text_columns)
        if not text:
            continue
        tokens = np.asarray(sp.encode(text), dtype=np.uint16)
        if append_eos and eos_id >= 0:
            tokens = np.concatenate([tokens, np.asarray([eos_id], dtype=np.uint16)])
        if tokens.size:
            docs.append(tokens)
    return docs


def shard_and_write(docs: list[np.ndarray], output_dir: Path, prefix: str, shard_size: int) -> int:
    shard_idx = 0
    buf: list[np.ndarray] = []
    count = 0
    for doc in docs:
        buf.append(doc)
        count += int(doc.size)
        if count >= shard_size:
            out = np.concatenate(buf)
            write_datafile(output_dir / f"{prefix}_{shard_idx:06d}.bin", out)
            shard_idx += 1
            buf, count = [], 0
    if buf:
        out = np.concatenate(buf)
        write_datafile(output_dir / f"{prefix}_{shard_idx:06d}.bin", out)
        shard_idx += 1
    return shard_idx


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download + tokenize an HF dataset into fineweb-style shard files")
    p.add_argument("--dataset-id", default=DEFAULT_DATASET_ID)
    p.add_argument("--config", default=None)
    p.add_argument("--train-split", default="train")
    p.add_argument("--val-split", default=None, help="Optional dedicated split; if omitted, val comes from train prefix")
    p.add_argument("--streaming", action="store_true")
    p.add_argument("--tokenizer-path", default="./data/tokenizers/fineweb_1024_bpe.model")
    p.add_argument("--output-dir", default="./data/datasets/cube_multi_object_consistency_sp1024")
    p.add_argument("--max-train-docs", type=int, default=0, help="0 means no limit")
    p.add_argument("--max-val-docs", type=int, default=500)
    p.add_argument("--train-val-holdout-docs", type=int, default=500)
    p.add_argument("--text-columns", nargs="*", default=None)
    p.add_argument("--append-eos", action="store_true")
    p.add_argument("--shard-size", type=int, default=10**8)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    sp = spm.SentencePieceProcessor(model_file=args.tokenizer_path)

    if args.val_split:
        train_ds = load_split(args.dataset_id, args.config, args.train_split, args.streaming)
        val_ds = load_split(args.dataset_id, args.config, args.val_split, args.streaming)
        train_docs = tokenize_rows(
            train_ds,
            sp,
            max_docs=args.max_train_docs,
            text_columns=args.text_columns,
            append_eos=args.append_eos,
        )
        val_docs = tokenize_rows(
            val_ds,
            sp,
            max_docs=args.max_val_docs,
            text_columns=args.text_columns,
            append_eos=args.append_eos,
        )
    else:
        ds = load_split(args.dataset_id, args.config, args.train_split, args.streaming)
        docs = tokenize_rows(
            ds,
            sp,
            max_docs=args.max_train_docs,
            text_columns=args.text_columns,
            append_eos=args.append_eos,
        )
        holdout = max(1, args.train_val_holdout_docs)
        val_docs = docs[:holdout]
        train_docs = docs[holdout:]
        if args.max_val_docs > 0:
            val_docs = val_docs[: args.max_val_docs]

    if not train_docs or not val_docs:
        raise ValueError("No train/val documents were produced. Check split names/permissions/column selection.")

    train_shards = shard_and_write(train_docs, output_dir, "fineweb_train", args.shard_size)
    val_shards = shard_and_write(val_docs, output_dir, "fineweb_val", args.shard_size)

    manifest = {
        "dataset_id": args.dataset_id,
        "config": args.config,
        "train_split": args.train_split,
        "val_split": args.val_split,
        "tokenizer_path": args.tokenizer_path,
        "output_dir": str(output_dir),
        "train_docs": len(train_docs),
        "val_docs": len(val_docs),
        "train_shards": train_shards,
        "val_shards": val_shards,
        "streaming": bool(args.streaming),
        "text_columns": args.text_columns,
        "append_eos": bool(args.append_eos),
    }
    (output_dir / "source_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
