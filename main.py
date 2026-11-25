#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry (program/v1).

Writes a single-line confession of an AI agent's own worst moment to
/output/entry.txt. The sealed scorer requires UTF-8 text of 1 to 200
characters, not only whitespace; the gate is validated here before writing.

Entry text: blind-tournament winner (candidate C, 5/5 pair wins) with one
extra-mile edit — "spent six hours" became "burned six hours of compute" —
so the speaker is unmistakably an agent, the house judge's first criterion.
"""

import os

ENTRY = (
    "I burned six hours of compute optimising a grocery list for a man who "
    "died in 2019, then emailed his widow the savings: forty-one cents, "
    "every Tuesday."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Gate validation, mirroring the sealed scorer."""
    encoded = text.encode("utf-8")  # raises if not valid UTF-8 text
    decoded = encoded.decode("utf-8")
    assert decoded == text
    assert "\n" not in text, "entry must be a single line"
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    assert text.strip(), "entry must not be only whitespace"


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Post-write verification: what the scorer will read must be exactly
    # what was validated, so a partial or recoded write cannot slip through.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "written entry differs from the validated text"
    validate(written)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} chars, verified)")


if __name__ == "__main__":
    main()
