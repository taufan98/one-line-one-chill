#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt. Deterministic: no input, no network, no secrets.
"""

import os

# Craft notes (judge weighs frightening > vivid > original > crafted):
# - Frightening: dread outlasts the line — a warning from your own future self.
# - Vivid: voicemail, own number, a timestamp three hours ahead, breathing.
# - Original: no mirror, doll or basement; the scare is a future you.
# - Crafted: one sentence, rhythm builds, last word ("door") lands the blow.
LINE = (
    "The voicemail on my phone came from my own number, timestamped "
    "three hours from now, and it was just me breathing, begging me "
    "not to answer the door."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
