"""The adapter's round-trip and its refusals (spec 001 §5).

Run from the repository root: `just test`. The round-trip needs source/,
which is not redistributable, so it skips in CI; the refusal tests use a
synthetic file and always run.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import apparatus  # noqa: E402

SOURCE = apparatus.REPO / "source"

SAMPLE = """## What is Zen?

Zen is plain.

![](media/images/image_rsrcW3.jpg)

**EVERYDAY ZEN**

### SHARPEN YOUR AXE

![](media/images/image_rsrcW4.jpg)

A woodcutter sharpens his axe.
"""


def markup(text: str) -> list[str]:
    """Each line reduced to what the apparatus must preserve.

    Heading text is translated (or renamed from [tool.book.titles]) and the
    label becomes Persian, so only their level survives the comparison. Every
    other line -- images, paragraphs, blanks -- must come back byte for byte,
    since nothing was translated.
    """
    out = []
    for line in text.strip().split("\n"):
        if line.startswith("#"):
            line = line.split(" ", 1)[0]
        elif line in ("**EVERYDAY ZEN**", f"**{apparatus.FA_LABEL}**"):
            line = "LABEL"
        out.append(line)
    return out


def body(restored: str) -> str:
    return restored.split("---\n", 2)[2]


class RoundTrip(unittest.TestCase):
    @unittest.skipUnless(SOURCE.is_dir(), "source/ is not present")
    def test_every_source_file(self):
        names = [p.name for p in sorted(SOURCE.glob("*.md")) if p.name not in apparatus.EXCLUDE]
        self.assertEqual(len(names), 70)
        for name in names:
            with self.subTest(name):
                src = (SOURCE / name).read_text(encoding="utf-8")
                out = apparatus.restore_text(name, src, apparatus.strip_text(name, src))
                self.assertTrue(out.startswith("---\nstatus: reviewed\n---\n\n"))
                self.assertEqual(markup(body(out)), markup(src))
                if name in apparatus.TITLES and src.startswith("# "):
                    self.assertEqual(body(out).lstrip().split("\n")[0], f"# {apparatus.TITLES[name]}")

    def test_sample(self):
        stripped = apparatus.strip_text("1-04.md", SAMPLE)
        self.assertNotIn("media/images", stripped)
        self.assertNotIn("EVERYDAY", stripped)
        self.assertIn("⟦4⟧ Sharpen your axe", stripped)
        out = body(apparatus.restore_text("1-04.md", SAMPLE, stripped))
        self.assertIn("### Sharpen your axe", out)
        self.assertIn(f"**{apparatus.FA_LABEL}**", out)
        self.assertEqual(markup(out), markup(SAMPLE))

    def test_heading_spacing_normalised(self):
        stripped = apparatus.strip_text("1-04.md", SAMPLE).replace("⟦1⟧ ", "⟦1⟧")
        out = body(apparatus.restore_text("1-04.md", SAMPLE, stripped))
        self.assertTrue(out.lstrip().startswith("## What is Zen?"))


class Refusal(unittest.TestCase):
    def setUp(self):
        self.stripped = apparatus.strip_text("1-04.md", SAMPLE)

    def test_deleted_sentinel(self):
        draft = self.stripped.replace("⟦4⟧", "")
        with self.assertRaisesRegex(ValueError, r"dropped sentinel\(s\) \[4\][\s\S]*⟦4⟧"):
            apparatus.restore_text("1-04.md", SAMPLE, draft)

    def test_duplicated_sentinel(self):
        draft = self.stripped.replace("⟦2⟧", "⟦2⟧ ⟦2⟧")
        with self.assertRaisesRegex(ValueError, r"duplicated sentinel\(s\) \[2\]"):
            apparatus.restore_text("1-04.md", SAMPLE, draft)


if __name__ == "__main__":
    unittest.main()
