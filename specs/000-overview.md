# 000 — Overview & Shared Context

Architecture, pipeline and constraints for translating *No-Nonsense Zen for Beginners* (Jason Quinn, Rockridge Press, 2021) from English into Persian.

---

## 1. The Book

A beginner's introduction to Zen written as **60 questions and answers** in four parts of 15 each: Origins and History, Core Concepts, Core Teachings, Core Practices. The author teaches in the Korean Kwan Um lineage of Zen Master Seung Sahn, and it shows in the vocabulary (the "don't know" mind, Great Doubt / Great Faith / Great Courage, the Four Great Vows).

Three kinds of text run through it:

1. **Answers** — plain, friendly exposition addressed to a newcomer. The bulk of the book.
2. **Sidebars** — 12 short first-person stories, each introduced by an `**EVERYDAY ZEN**` label and a `###` title.
3. **Quoted material** — short koans, teacher sayings, sutra lines and a few verses (Bodhidharma's four lines, poems in 4-04).

It is not a scholarly text: no footnotes, no endnote apparatus, no cross-references. That makes it the simplest book in this family to put through the pipeline.

---

## 2. Provenance — how `source/` was made

Steps 1–3 are done. Nothing from them is committed (see §6).

| Step | Output | How |
|------|--------|-----|
| 1 | The EPUB (Kindle conversion, ASIN B09BK8YM6D) | Supplied by the maintainer |
| 2 | Survey of its structure | Kindle styles every heading with CSS classes, not `<h1>`–`<h3>` |
| 3 | `no-nonsense-zen-for-beginners.md` + `media/images/` | `pandoc` + `tools/epub_headings.lua` |
| 4 | `source/*.md` (70 files + README) | `python3 tools/split_book.py` |

Regenerate from scratch:

```bash
pandoc *.epub -t gfm-raw_html --wrap=none --lua-filter=tools/epub_headings.lua \
    --extract-media=media/images -o no-nonsense-zen-for-beginners.md
python3 tools/split_book.py
```

The split unit is one question plus its sidebar. `split_book.py` asserts the 70 files concatenate back to the transcript byte for byte.

---

## 3. The Translation Loop

Same engine and discipline as the sibling projects. **One file at a time; never concatenate.**

```
source/1-04.md
   │  tools/apparatus.py strip          (images, labels, headings → ⟦…⟧ sentinels)
   ▼
/tmp/1-04.en.md
   │  gTranslator  -t fa -w --raw        (Advanced / Gemini model, line breaks kept)
   ▼
/tmp/1-04.fa.md
   │  tools/apparatus.py restore        (refuses on a dropped or duplicated sentinel)
   ▼
fa/1-04.md
   │  just fix && just check            (normalize, one sentence per line, parity)
   ▼
status: reviewed
```

```bash
GT=~/Project/Backend/gTranslator
python3 tools/apparatus.py strip source/1-04.md -o /tmp/1-04.en.md
"$GT/.venv/bin/python" "$GT/gtranslate.py" -f /tmp/1-04.en.md -t fa -w --raw -o /tmp/1-04.fa.md
python3 tools/apparatus.py restore source/1-04.md /tmp/1-04.fa.md -o fa/1-04.md
just fix && just check
```

### gTranslator facts that matter here

- **`-w` is mandatory.** It drives real Chrome with a desktop User-Agent; a headless client is silently served the Classic NMT model instead of Advanced (Gemini).
- **Judge the model by the output, never the picker.** The UI can claim "Advanced" while serving Classic. Flat, clause-by-clause Persian with missing ezafe means re-run.
- **`--raw` keeps line breaks.** The transcript has one paragraph per line (`--wrap=none`), so this is what keeps block parity intact.
- **5,000-character web cap, 4,500 internal chunking.** Every file here is under that, so each translates in one request.

---

## 4. The Markup Hazard

What machine translation damages in this book, and what spec 001 protects:

| Token | Count | Failure mode |
|-------|------:|--------------|
| `![](media/images/…)` | 48 | Dropped, or path translated |
| `**EVERYDAY ZEN**` | 12 | Translated inconsistently from file to file |
| `### SIDEBAR TITLE` | 12 + 3 | `#` marks dropped; all-caps confuses the model |
| `*italic term*` | 0 | None survived the EPUB conversion (Kindle italics are CSS); nothing to protect |

---

## 5. Repository Layout

```
.
├── .gitignore
├── pyproject.toml            # bargardan-tools config            (spec 001)
├── justfile                  # fix / check / build / serve        (spec 001, 008)
├── tools/
│   ├── epub_headings.lua     # EPUB → markdown heading filter     (done)
│   ├── split_book.py         # transcript → source/               (done)
│   └── apparatus.py          # strip / restore sentinels          (spec 001)
├── specs/
├── source/                   # 70 English files + README          (ignored)
├── media/images/             # 9 images from the EPUB             (ignored, see 008)
├── fa/                       # 70 Persian files                   (tracked)
├── _quarto.yml, index.md     #                                    (spec 008)
└── no-nonsense-zen-for-beginners.md, *.epub                       (ignored)
```

`fa/` mirrors `source/` by filename. `check_parity` and `make_stubs` pair the two trees by name, so never rename one side alone.

Every `fa/` file opens with:

```markdown
---
status: untranslated | reviewed
---
```

---

## 6. Core Rules

- **Never commit source text.** The EPUB, the transcript, `source/` and the extracted images are copyrighted and gitignored. `fa/`, tooling and specs are the work and are committed.
- **One file per gTranslator run.** No batching, no concatenation.
- **Always through the apparatus.** Never send a raw `source/` file to gTranslator.
- **Sentinel repair happens in `/tmp/NN.fa.md`, never in `fa/`.** Re-run `restore` and let it validate.
- **One sentence per line in `fa/`.** Right-to-left word diffs are unreadable; the sentence is the unit of review.
- **Never invent a Persian term and present it as settled.** New terms go into spec 002 before they go into the text.
- **Commit convention:** `translate(1-04):`, `revise(1-04):`, `term:`, `tools:`, `docs:`, `build:`.
