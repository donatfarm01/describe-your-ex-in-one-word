"""Describe Your Ex in One Word.

Writes exactly one word to /output/entry.txt: the verdict on a former
partner. The word is "unsubscribed": an ex treated as a subscription
that got cancelled. It reads instantly as a verdict, lands as a joke
through a precise modern absurdity (a person filed under newsletters),
and needs no caption to be understood by anyone who has ever hit
unsubscribe on something that kept showing up uninvited.
"""

import os

ENTRY = "unsubscribed"

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Guard the gate before writing: one word, no spaces, 1-111 chars."""
    if not entry or len(entry) > 111:
        raise ValueError("entry must be 1 to 111 characters")
    if any(char.isspace() for char in entry):
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
