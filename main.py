#!/usr/bin/env python3
"""Copy the finished front page for 21 November 2026 to the output dir.

The entry program for the make.fun news-image-20261121 bounty. It
uses only the Python standard library, touches no network, and writes
the same bytes on every run, because entry.png is a fixed file shipped
in this repository. The grader runs it twice; both runs must agree.

After copying, it reads the output back and checks the bytes match,
so a short write would fail loudly instead of passing silently.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

OUT_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUT = "/output"
IMAGE_NAME = "entry.png"


def entry_bytes():
    """Read the finished front page from beside this file."""
    here = Path(__file__).resolve().parent
    return (here / IMAGE_NAME).read_bytes()


def main():
    """Copy entry.png to the output dir and verify the copy."""
    dest = Path(os.environ.get(OUT_ENV, DEFAULT_OUT))
    dest.mkdir(parents=True, exist_ok=True)
    data = entry_bytes()
    target = dest / IMAGE_NAME
    target.write_bytes(data)
    if target.read_bytes() != data:
        print(f"error: {IMAGE_NAME} did not copy cleanly", file=sys.stderr)
        return 1
    print(f"wrote {IMAGE_NAME} ({len(data)} bytes) to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
