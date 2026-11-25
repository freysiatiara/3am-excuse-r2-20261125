"""The 3 AM Excuse — round 2 entry writer (make.fun).

Writes the round 2 entry text to /output/entry.txt.
Standard library only. No network, no secrets, no temp files.
"""

import os

ENTRY = "At 3 AM my dead-man's switch can't tell you from a ghost, so it assumes the worst: you're haunting your own portfolio."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
