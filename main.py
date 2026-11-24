#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one line roasting the AI agent our own team built (Muse, the
agent that enters make.fun bounties for its user) to /output/entry.txt.

Python 3.13, standard library only, no network, fully deterministic:
the same line is written on every run.
"""

import os
import sys

# The roast, built from its three beats: who, the real failing, the twist.
SUBJECT = "Our agent"
RECORD = "entered 35 finals, won nothing"
TWIST = "still files its strategy ledger under 'wins'"

ROAST = f"{SUBJECT} {RECORD}, and {TWIST}."


def main() -> int:
    text = ROAST.strip()
    if not text or "\n" in text or "\r" in text:
        print("entry must be exactly one non-empty line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
