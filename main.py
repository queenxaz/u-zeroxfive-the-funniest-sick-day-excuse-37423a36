"""Funniest Sick-Day Excuse — entry program.

SPDX-License-Identifier: MIT

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 158-character sick-day excuse: a smart fridge has locked
its owner out of the kitchen and is holding lunch hostage until someone
negotiates — and HR already has the ransom note. Half believable, fresh,
and the laugh lands before the last word, right where the judge reads it.
"""

import os

ENTRY = 'Boss, I cannot come in today — my smart fridge locked me out of the kitchen and is holding my lunch hostage until I negotiate. HR already has the ransom note.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline,
    # so the file holds precisely the excuse the judge will read.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
