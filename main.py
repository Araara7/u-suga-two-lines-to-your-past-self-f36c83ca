#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun bounty entry.

Writes a two-line warning to my past self to /output/entry.txt.
Line 1 warns about one specific moment; line 2 says why it mattered.
"""

import os

ENTRY = (
    "Don't trust the 'quick fix' at 2 a.m. — the bug you patch half-asleep "
    "will wake you up three more times before sunrise.\n"
    "That night mattered because it taught me sleep is a debugging tool, "
    "and ever since, I fix nothing after midnight."
)


def main() -> None:
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no line may be blank"
    assert all(line.count(".") >= 1 for line in lines), "each line is one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
