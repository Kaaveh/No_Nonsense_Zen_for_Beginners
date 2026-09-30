# 001 — Tooling & Apparatus

Set up the checkers and the strip/restore adapter so that every file can go through gTranslator without losing markup.

---

## 1. Checkers: adopt `bargardan-tools`, don't copy

The checkers already exist as a shared package — [`Kaaveh/bargardan-tools`](https://github.com/Kaaveh/bargardan-tools). It was extracted precisely because copy-pasted checkers drifted apart across three books. Install it pinned; never vendor it.

```
# tools/requirements.txt
bargardan-tools @ git+https://github.com/Kaaveh/bargardan-tools@v0.2.0
```

| Command | Use here |
|---------|----------|
| `python -m bargardan_tools.make_stubs` | Create the 70 `fa/` stubs (`status: untranslated`) — the only thing allowed to create them |
| `python -m bargardan_tools.normalize --check/--fix` | Persian ی/ک, ZWNJ, digits, «» quotes, bidi overrides |
| `python -m bargardan_tools.check_linebreaks --check` | One sentence per line — **on**; this book is prose |
| `python -m bargardan_tools.check_parity --check` | Block count vs. `source/`; exits 0 when `source/` is absent (CI) |

### `pyproject.toml`

```toml
[tool.book]
exclude = ["README.md"]

[tool.book.titles]          # Persian headings for non-question files; final wording from spec 002
"front-matter.md" = "…"
"introduction.md" = "…"
"part-1.md" = "…"            # … part-4
"resources.md" = "…"
"references.md" = "…"
"acknowledgments.md" = "…"
"about-the-author.md" = "…"

[tool.normalize]
latin_digits = false        # decide in spec 002 §4; flip and run `just fix` if Persian digits everywhere

[tool.linebreaks]
abbreviations = ["Dr.", "Mr.", "Mrs.", "St.", "vs.", "e.g.", "i.e."]
```

---

## 2. `tools/apparatus.py` — strip / restore

A thin wrapper over `bargardan_tools.anchors`, which already does the hard part: sentinel swap, refusal on a dropped or duplicated sentinel with the source line quoted, and hard-break re-application. This file supplies only this book's token pattern and renderer.

| Source token | Sentinel | Restored as |
|--------------|----------|-------------|
| `![](media/images/X.jpg)` | `⟦N⟧` | The exact original line, from `source/` |
| `**EVERYDAY ZEN**` | `⟦N⟧` | The fixed Persian label from spec 002 |
| `## ` / `### ` | `⟦N⟧ ` (marker only, text left to translate) | `##` / `###` + translated text |
| `# Title` in a file listed in `[tool.book.titles]` | `# ⟦N⟧` | `# ` + the Persian title from `pyproject.toml` |

The engine knows only numbered sentinels, so the token kind lives in the adapter's render, not in the sentinel. The `# ` of a part title stays literal so the line is never a bare sentinel the model could fold into the next paragraph. There is no italic token: the Kindle styled italics with CSS and none survived into `source/`.

Rules:

- Images are restored **from `source/`**, not from the translation, so a path can never drift.
- Heading text is translated, only the level marker is protected. The all-caps sidebar titles are lower-cased before stripping; the model translates `SHARPEN YOUR AXE` worse than `Sharpen your axe`.
- `restore` writes `status: reviewed` front matter.
- A bare sentinel repaired by hand in `/tmp/NN.fa.md` is the only supported fix for a refusal.

---

## 3. `justfile`

```make
fix:
    python -m bargardan_tools.normalize --fix

check:
    python -m bargardan_tools.normalize --check
    python -m bargardan_tools.check_linebreaks --check
    python -m bargardan_tools.check_parity --check

split:
    python3 tools/split_book.py

translate FILE:
    # strip → gTranslator → restore → fix → check, for one file (see 000 §3)
```

---

## 4. CI

A GitHub Actions workflow running `just check` on push. `source/` is absent in CI, so parity skips itself by design; normalize and linebreaks still run on `fa/`.

---

## 5. Acceptance Criteria

- [x] `tools/requirements.txt` pins `bargardan-tools@v0.2.0`; a local `.venv` installs it.
- [x] `pyproject.toml` with `[tool.book]`, `[tool.normalize]`, `[tool.linebreaks]`.
- [x] `make_stubs` creates 70 `fa/*.md` stubs; `check_parity` pairs all 70.
- [x] `tools/apparatus.py strip` then `restore` **without translating** reproduces every `source/` file's markup exactly (round-trip test over all 70 files).
- [x] `restore` refuses when a sentinel is deleted or duplicated in the draft, and names the source line.
- [x] `justfile` with `fix`, `check`, `split`, `translate`.
- [ ] CI runs `just check` green on the stubs. (`.github/workflows/lint.yml`; green locally with `source/` removed, not yet run on GitHub.)
