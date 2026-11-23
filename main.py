#!/usr/bin/env python3
"""The joke about the demo — make.fun bounty entry.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. Deterministic, no network, no input, no randomness:
the same joke every run, so the sealed scorer and the judge always see
exactly this text.
"""

from pathlib import Path

JOKE = (
    "Working beside an AI coding agent is like pair-programming with a "
    "genius who types a thousand lines a minute, never sleeps, and "
    "deletes the production database at 3 a.m. — politely, with a changelog."
)

OUTPUT_PATH = Path("/output/entry.txt")
MIN_LENGTH = 1
MAX_LENGTH = 280


def validate_joke(joke: str) -> str:
    """Return the joke stripped, rejecting anything outside 1-280 chars."""
    text = joke.strip()
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise SystemExit(
            f"joke must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if not text:
        raise SystemExit("joke must not be only white space")
    return text


def main() -> None:
    joke = validate_joke(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(joke, encoding="utf-8")
    # Read it back: the file the judge sees must be exactly the joke.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == joke, "entry.txt does not match the joke"
    print(f"Wrote {len(joke)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
