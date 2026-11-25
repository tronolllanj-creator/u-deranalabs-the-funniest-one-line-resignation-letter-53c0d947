"""
make.fun entry: The Funniest One-Line Resignation Letter.

Writes a one-line resignation letter (spoken by a stuck, ancient queued job)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default 'out' if unset). The letter is fixed text;
this script only validates the byte/char budget and writes it deterministically.
"""

import os

MESSAGE = "I have been queued since 2019. The backlog is now a geological layer. I resign.\n"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    path = os.path.join(output_dir, "entry.txt")

    content = MESSAGE

    # Gate: entry.txt is 1-140 chars, UTF-8, not only whitespace (judge reads it pairwise).
    if not (1 <= len(content) <= 140 and content.strip()):
        raise ValueError("entry.txt content is outside the allowed 1-140 char budget or is only whitespace")

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)

    print(path)
    print(len(content))


if __name__ == "__main__":
    main()
