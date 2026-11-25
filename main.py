"""Write the winning one-line office joke to /output/entry.txt.

Deterministic: the same single line on every run. No network, no clock,
no randomness, no input files. No trailing newline, so the file is
exactly the joke: 77 bytes.
"""

import os

LINE = "I raised an IT ticket about the printer, and the printer raised one about me."

# The gate allows 1-199 chars on one line; refuse to write anything else
# rather than ship an entry the scorer would mark invalid.
assert "\n" not in LINE and 1 <= len(LINE) <= 199, "entry must be one line of 1-199 chars"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
