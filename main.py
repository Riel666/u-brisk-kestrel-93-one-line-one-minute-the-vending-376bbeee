"""One pickup line, 200 characters at most, that a vending machine would use on a passing human.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "Hey, I am stocked, lit, and exactly your type: I take coins, give change, and never leave you on read."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
