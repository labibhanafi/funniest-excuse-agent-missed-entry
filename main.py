"""Write the competition entry to /output/entry.txt.

SPDX-License-Identifier: MIT

How the generator works: the entry text lives in entry.txt, shipped
next to this file. main() reads that file verbatim and writes the exact
same contents to /output/entry.txt, the path the grader checks — a
byte-for-byte copy with no transformation, no trimming, and no added
newline. No network, no environment secrets, no input beyond the
shipped entry.txt.
"""

import os

ENTRY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUTPUT_PATH = "/output/entry.txt"


def main():
    with open(ENTRY_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
