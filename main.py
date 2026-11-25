#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
The joke turns on a real office detail (the reply-all chain) and lands
its laugh in the last few words. Standard library only.
"""

import os

JOKE = (
    "The reply-all chain started with 'Happy birthday, Sarah' and ended "
    "with Legal replying-all to ask everyone to stop replying-all."
)


def main() -> None:
    text = JOKE.strip()
    if not (1 <= len(text) <= 199):
        raise ValueError("entry must be 1-199 characters, got %d" % len(text))
    if "\n" in text:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
