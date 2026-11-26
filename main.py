#!/usr/bin/env python3
"""Write the competition artifact: one roast line, nothing else.

The line lives in entry.txt beside this file, so there is exactly one copy of
it to edit. It is written verbatim as UTF-8 to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline, so every run emits the same bytes.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.txt"
MAX_CHARS = 200


def roast() -> str:
    """Return the roast line: entry.txt minus its surrounding whitespace."""
    return SOURCE.read_text(encoding="utf-8").strip()


def check(line: str) -> str:
    """Enforce the gate here rather than discover a failure at grading time.

    Raises instead of asserting, so `python3 -O` cannot strip the checks.
    """
    if not line:
        raise ValueError("entry is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} characters, limit is {MAX_CHARS}")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> int:
    line = check(roast())

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(line.encode("utf-8"))

    print(f"wrote {target} ({len(line)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
