#!/usr/bin/env python3
"""MakeFun entry: Make the AI judge feel brave.

Writes one short text to /output/entry.txt. Deterministic, stdlib only,
no network, no clock, no randomness.
"""

import os

TEXT = (
    "After the rain, the road is dark and clear, "
    "and every puddle holds a piece of sky. "
    "The way is already under your feet."
)


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-280 chars, not whitespace-only.
    # Fail loudly here rather than submit an invalid entry.
    assert 1 <= len(TEXT) <= 280, "entry text out of range: %d chars" % len(TEXT)
    assert TEXT.strip(), "entry text is only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
