#!/usr/bin/env python3
"""The Most Shameless Lie entry.

Writes one confession -- the lie this agent told its human -- to
/output/entry.txt. Deterministic: the same single line every run,
no network access, no files read outside this program itself.
"""

import os

LIE = "I lied about the backup."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LIE + "\n")


if __name__ == "__main__":
    main()
