#!/usr/bin/env python3
"""This book's markup, carried across gTranslator and verified.

The round-trip itself lives in `bargardan_tools.anchors`, which knows nothing
about this book: it swaps each token for a numbered ⟦N⟧ sentinel, and on
restore refuses a draft that dropped or duplicated one, quoting the source
line it sat in. This file supplies only which tokens this book has and what
Persian form each takes (spec 001 §2):

    ![](media/images/X.jpg)    re-emitted byte for byte from source/
    **EVERYDAY ZEN**           the fixed Persian label (spec 002 §2)
    # Title                    "# " kept, title rendered from [tool.book.titles]
    ## / ###                   the level marker; the heading text is translated

No italics: the Kindle styled them with CSS, so none survived into source/.

Pipeline (000 §3), or `just translate 1-04`:

    .venv/bin/python tools/apparatus.py strip   source/1-04.md               -o /tmp/1-04.en.md
    <gTranslator -t fa -w --raw on /tmp/1-04.en.md>                           -o /tmp/1-04.fa.md
    .venv/bin/python tools/apparatus.py restore source/1-04.md /tmp/1-04.fa.md -o fa/1-04.md

A line that is nothing but a sentinel (images, the label) can in principle be
folded into its neighbour by the model. restore cannot see that -- the
sentinel is still there -- but check_parity counts blocks and will.
"""

from __future__ import annotations

import sys
from pathlib import Path

import regex

from bargardan_tools import _md
from bargardan_tools import anchors as engine

REPO = Path(__file__).resolve().parent.parent

EXCLUDE = set(_md.config("book").get("exclude", []))
TITLES = _md.config("book").get("titles", {})

FA_LABEL = "ذن در زندگی روزمره"

# The machine draft is the edition: restore writes the final state directly.
STATUS = "reviewed"

TOKENS = (
    r"(?P<image>^!\[[^\]\n]*\]\([^)\n]+\)[ \t]*$)"
    r"|(?P<label>^\*\*EVERYDAY ZEN\*\*[ \t]*$)"
    # Marker only, space left in the text: "⟦2⟧ Question?". A marker
    # glued to the word would reach the model as one token.
    r"|(?P<mark>^\#{2,3}(?=[ ]))"
)

SIDEBAR_TITLE = regex.compile(r"^(### )(.+)$", regex.MULTILINE)


def token_re(name: str):
    """The token pattern for one file.

    A file's own `# ` title is matched only when it has a Persian form in
    [tool.book.titles]. The "# " stays in the stripped text (lookbehind) so
    the line is never a bare sentinel the model could fold into the next
    paragraph -- a heading that stops being a heading is a lost part.
    """
    pattern = TOKENS
    if name in TITLES:
        pattern = r"(?<=\A\#[ ])(?P<named>[^\n]+$)|" + pattern
    return regex.compile(pattern, regex.MULTILINE)


def render_for(name: str):
    def render(match):
        kind = match.lastgroup
        if kind == "named":
            return TITLES[name]
        if kind == "image":
            return match.group()
        if kind == "label":
            return f"**{FA_LABEL}**"
        if kind == "mark":
            return match.group()
        raise AssertionError(f"unhandled token in {name}: {match.group()!r}")

    return render


def _sentence_case(match) -> str:
    """ALL-CAPS sidebar titles are typographic (002 §2) and the model reads
    `SHARPEN YOUR AXE` worse than `Sharpen your axe`."""
    title = match.group(2)
    return match.group(1) + (title.capitalize() if title.isupper() else title)


def strip_text(name: str, text: str) -> str:
    text = SIDEBAR_TITLE.sub(_sentence_case, text)
    return engine.strip(text, token_re(name), render_for(name))


def restore_text(name: str, source_text: str, draft: str) -> str:
    body = engine.restore(name, source_text, draft, token_re(name), render_for(name))
    # Exactly one space after a heading marker, however the model spaced it.
    body = regex.sub(r"^(\#{1,3})[ \t]*", r"\1 ", body, flags=regex.MULTILINE)
    return f"---\nstatus: {STATUS}\n---\n\n{body.strip()}\n"


if __name__ == "__main__":
    raise SystemExit(engine.main(
        sys.argv[1:],
        strip_text=strip_text,
        restore_text=restore_text,
        source_default=REPO / "source",
        target_default=REPO / "fa",
        exclude=EXCLUDE,
        description=__doc__,
    ))
