"""One Line of Earned Pride — make.fun entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for a boy in a classroom, a small person
doing something hard, the pride landing on the very last word.
"""

from pathlib import Path

ENTRY = (
    "On his third try, Sam read the whole paragraph aloud without stopping, "
    "and the classroom held its breath until the last word."
)


def main() -> None:
    # The gate allows 1-240 characters; refuse loudly rather than write
    # an entry the scorer would reject.
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise ValueError(f"entry is {len(ENTRY)} characters, outside 1-240")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)} characters to {entry_path}")


if __name__ == "__main__":
    main()
