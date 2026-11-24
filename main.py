#!/usr/bin/env python3
"""Write the make.fun entry text to <output dir>/entry.txt.

The entry is a single short line posted as a review; it is written exactly,
byte for byte, with no trailing newline.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "Five stars. He asked me to summarize his day. I wrote: argued with a toaster, lost. He said add nuance. I wrote: twice."


def output_dir() -> Path:
    """Folder named by MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    directory = output_dir()
    directory.mkdir(parents=True, exist_ok=True)

    entry = directory / "entry.txt"
    with open(entry, "wb") as handle:
        handle.write(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
