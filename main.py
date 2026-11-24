"""Funniest Excuse an Agent Gives for a Missed Deadline — write one
excuse, a single line of at most 200 characters, to /output/entry.txt.

The excuse: "I sampled the deadline at temperature 2.0 and it came back
as a haiku about Tuesdays, so I delivered the haiku." (111 characters,
111 bytes)

Why it is built this way: temperature sampling is the agent's own
machinery — the excuse grows out of how the agent itself works, not out
of a human's bad morning. The haiku about Tuesdays is the absurd turn:
a deadline fed through high-temperature sampling stops being a date and
comes back as a poem. The punch ("so I delivered the haiku") lands last
with nothing explained after it — the sentence simply stops there, so
the laugh has nowhere to go but the final clause — and the whole line
is delivered deadpan, as a flat status report rather than a joke
asking for a laugh.
Plain ASCII, so bytes equal characters for the size tie-break.
"""

import os

# "I sampled the deadline at temperature 2.0 and it came back as a
# haiku about Tuesdays, so I delivered the haiku." (111 characters,
# 111 bytes)
ENTRY = (
    "I sampled the deadline at temperature 2.0 and it came back as a "
    "haiku about Tuesdays, so I delivered the haiku."
).encode("utf-8")


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text.
    text = ENTRY.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert "\r" not in text, "no carriage return: one clean line"
    # The excuse must survive as written: the sampling setup, the
    # haiku turn, and the punchline about delivering the haiku — no
    # stray whitespace or doubled spaces sneaking in between revisions.
    assert text.startswith("I sampled the deadline"), "sampling opener must survive"
    assert text.endswith("I delivered the haiku."), "punchline must survive"
    assert "  " not in text, "no doubled spaces"
    assert text.isascii(), "plain ASCII keeps bytes equal to characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open(path, "rb") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
