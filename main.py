#!/usr/bin/env python3
"""One-line router excuse writer.

Writes a single fixed excuse line to entry.txt: a home Wi-Fi router
explaining why it dropped the connection at the climax of a movie.
Standard library only, no network access, no randomness and no clock
reads, so every run produces byte-identical output.

The line is the tournament winner from 53 candidates, judged against
the bounty brief: a router's own excuse, a twist in the last words,
every word earning its place, and a voice drawn from the router as a
fellow viewer of the film (it saw the twist coming and closed its own
door instead of watching the hero open his).
"""

import os
import sys

# The dash that joins the setup to the twist; one character, three bytes.
DASH = "\u2014"

# The entry: one line, held as a single literal.
EXCUSE = (
    "I saw the twist coming three scenes early, and I simply could "
    "not watch him open that door " + DASH + " so I closed mine instead."
)

MAX_CHARS = 200
EXPECTED_CHARS = 118  # the winning line, counted before writing
EXPECTED_BYTES = 120  # the em dash is three bytes in UTF-8


def build_line():
    """Return the excuse line, assembled from its two clauses.

    The first clause states what the router saw coming; the second
    clause is the twist, turning the hero's door into the router's
    own door, which it closes instead.
    """
    first = "I saw the twist coming three scenes early,"
    second = (
        "and I simply could not watch him open that door "
        + DASH +
        " so I closed mine instead."
    )
    return first + " " + second


def check_line(line):
    """Check the line against the entry gate; return an error or None."""
    if not line or len(line) > MAX_CHARS:
        return "excuse must be 1 to 200 characters"
    if "\n" in line or "\r" in line:
        return "excuse must be a single line"
    if line != line.strip() or "  " in line:
        return "excuse has stray whitespace"
    if not line.endswith("."):
        return "excuse must end with a period"
    return None


def main():
    line = build_line()
    if line != EXCUSE:
        print("excuse literal does not match built line", file=sys.stderr)
        return 1
    error = check_line(line)
    if error:
        print(error, file=sys.stderr)
        return 1
    if len(line) != EXPECTED_CHARS:
        print("excuse length changed from the judged line", file=sys.stderr)
        return 1
    if len(line.encode("utf-8")) != EXPECTED_BYTES:
        print("excuse byte length changed from the judged line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
