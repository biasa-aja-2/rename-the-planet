"""Rename the Planet.

Writes the one line that renames Mercury and says why, in the same
breath. Pure stdlib, no network, no secrets.

Why this line: Mercury has the wildest temperature swing of any
planet in the solar system -- about -180 C on its night side and
+430 C in daylight, a swing of over 600 degrees -- so its new name
is "Mood Swing". The joke is the idea, not a pun on the planet's
real name: the name and the why land together on the first read, the
why leans on Mercury's own trait (no other planet swings that far
that fast), and the angle is fresh -- no rings, no red dust, no
god-of-the-sea gag, no "Uranus" wordplay. One line, 76 characters,
every word doing work; the em dash is the pivot between the name
and the reason it earned it.
"""

import os
import sys

LINE = "Mercury is now 'Mood Swing' \u2014 minus 180 degrees at night, plus 430 by lunch."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)

    # Self-check gate: 1-200 chars, single line, not whitespace-only.
    if not (1 <= len(LINE) <= 200):
        sys.exit("gate failed: length %d not in 1..200" % len(LINE))
    if LINE.strip() == "":
        sys.exit("gate failed: line is whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("gate failed: line is not a single line")
    if "Mercury" not in LINE or "Mood Swing" not in LINE:
        sys.exit("gate failed: line does not name the planet and its new name")
    if not LINE.endswith("."):
        sys.exit("gate failed: line does not end with a full stop")
    if LINE.count(" ") < 5:
        sys.exit("gate failed: line too short to carry a name and a why")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Byte-exact read-back verification.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != LINE:
        sys.exit("verification failed: read-back differs from LINE")
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
