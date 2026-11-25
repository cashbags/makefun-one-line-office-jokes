"""Write the winning one-line office joke to /output/entry.txt.

Deterministic: the same single line on every run. No network, no clock,
no randomness, no input files. No trailing newline, so the file is
exactly the joke: 77 bytes.
"""

import os

LINE = "I raised an IT ticket about the printer, and the printer raised one about me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
