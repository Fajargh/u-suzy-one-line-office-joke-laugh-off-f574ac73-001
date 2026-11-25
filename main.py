#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line joke about office life to /output/entry.txt.
Deterministic: the same joke every run.
"""

JOKE = (
    "I finally achieved inbox zero \u2014 by moving everything to a folder "
    "called 'Future Me's Problem' and blocking Future Me."
)


def main() -> None:
    import os

    # Gate: the entry must be a single line of 1-200 characters.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 chars"
    assert "\n" not in JOKE, "joke must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
