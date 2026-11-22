#!/usr/bin/env python3
"""Ship the finished front page for 21 November 2026.

This is the entry program for make.fun's news-image-20261121 bounty.
It needs nothing but the Python standard library: it takes the
entry.png that lives next to it in this repository and puts an exact
copy at $MAKEFUN_OUTPUT_DIR/entry.png (or /output when the variable
is unset, which is where the grader looks). No network, no randomness,
no third-party code, so the grader's two runs write identical bytes.

The copy is checked with a SHA-256 digest before and after the copy,
so a truncated or garbled write fails loudly instead of slipping
through silently.

Try it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
OUTPUT_VARIABLE = "MAKEFUN_OUTPUT_DIR"
FALLBACK_DIRECTORY = "/output"


def digest_of(path):
    """Return the SHA-256 hex digest of a file's bytes."""
    hasher = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def run():
    """Copy entry.png into the output directory and verify it."""
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    wanted = digest_of(source)
    out_dir = Path(os.environ.get(OUTPUT_VARIABLE, FALLBACK_DIRECTORY))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / SOURCE_NAME
    shutil.copyfile(source, target)
    got = digest_of(target)
    if got != wanted:
        print(f"error: {SOURCE_NAME} copy mismatch: {got} != {wanted}",
              file=sys.stderr)
        return 1
    size = target.stat().st_size
    print(f"wrote {SOURCE_NAME} ({size} bytes, sha256 {got}) to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
