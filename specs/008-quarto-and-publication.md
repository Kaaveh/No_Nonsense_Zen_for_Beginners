# 008 — Quarto & Publication

Build `fa/` into an RTL web book, a LuaLaTeX PDF and an EPUB, reusing the sibling projects' setup rather than rebuilding it.

---

## 1. Reuse, don't redesign

*The Zen Teachings of Master Lin-chi* and *Lao-tzu's Taoteching* already solved Persian Quarto publishing. Copy from them:

- `_quarto.yml` / `_quarto-mobile.yml` structure and `_language.yml` (Persian UI strings).
- `tex/preamble.tex` — **LuaLaTeX, not XeLaTeX**: under XeLaTeX, Babel `bidi=default` reverses Latin runs inside Persian text.
- `fonts/` — Vazirmatn (or whatever the siblings settled on).
- The `build` / `serve` recipes in the `justfile`.

---

## 2. `_quarto.yml` outline

```yaml
project:
  type: book
  output-dir: _book

book:
  title: "…"                # spec 002 §2
  subtitle: "…"
  author: "جیسون کویین"
  repo-url: https://github.com/Kaaveh/No_Nonsense_Zen_for_Beginners
  repo-branch: main
  downloads: [pdf, epub]
  search: true
  chapters:
    - index.md
    - fa/front-matter.md
    - fa/introduction.md
    - part: fa/part-1.md
      chapters: [fa/1-01.md, …, fa/1-15.md]
    - part: fa/part-2.md
      chapters: [fa/2-01.md, …, fa/2-15.md]
    - part: fa/part-3.md
      chapters: [fa/3-01.md, …, fa/3-15.md]
    - part: fa/part-4.md
      chapters: [fa/4-01.md, …, fa/4-15.md]
    - fa/resources.md
    - fa/references.md
    - fa/acknowledgments.md
    - fa/about-the-author.md

lang: fa
dir: rtl
```

---

## 3. Images

`media/images/` is gitignored because every image came from the EPUB (cover, title page, author photo, decorative ornaments). Decide before the first public build:

- **Ornaments** (dividers before sidebars and part pages) → replace with a CSS/LaTeX rule, or draw a replacement. They carry no content.
- **Cover** → a new Persian cover, not the publisher's.
- **Author photo** → drop, or use only with permission.

Whatever survives must be committed, or the CI build has nothing to render.

**Applied (2026-09-30).** Nothing survives. All nine images are the publisher's, so none is committed and `fa/` keeps its `![](media/images/…)` lines for block parity. `tex/ornaments.lua` drops them at render time in every format, so the build never reads `media/images/`.

| Image | What it is | In the build |
|-------|-----------|--------------|
| VZ, W1 | Cover, title page | dropped: Quarto's own title page stands in |
| W0, W6 | Bonsai at part ends, seated Buddha after the 4-13 meditation how-to | dropped: decoration |
| W2, W4 | Thin rules under headings | dropped |
| W3, W5 | Buddha icon opening each sidebar, bonsai closing it | a horizontal rule, so each story still has edges |
| W7 | Author photo | dropped: no permission |

A Persian cover is not made. Add one when the book is to be released.

---

## 3a. Internal links

The EPUB's cross-references survive as `[text](#partNNNN.xhtml)` — dead targets outside the EPUB. One in `1-06` (to Part Four), four in `introduction.md`. The two in the source's `front-matter.md` went with the legal page (spec 007). Retarget each to the Quarto section id, or unlink it, before `quarto render`.

**Done.** All five now point at the part file (`[بخش اول](part-1.md)`). Quarto rewrites that per format: `part-1.html` on the web and an internal link in the PDF and EPUB.

## 4. Publication decision

The repository is private. Publishing a translation of an in-copyright 2021 book needs the rights holder's permission. **Do not make the repo or the built book public until that is settled.** Record the outcome here.

**Outcome (2026-09-30): published.** The maintainer released v1.0.0 and made the repository public. v1.0.0 was cut by hand with `gh release create`. From the next version on, `.github/workflows/release.yml` (the Ikkyu book's, minus its site deploy) renders and releases on every `v*` tag: bump `book-version` in `_quarto.yml`, tag, push the tag.

---

## 5. Acceptance Criteria

- [x] `_quarto.yml` lists all 70 files in book order.
- [x] `index.md` with Persian overview, version and licence.
- [x] `quarto render` produces HTML, PDF and EPUB locally without warnings.
- [x] Image policy in §3 applied; no unlicensed image committed.
- [x] Publication rights recorded in §4 before any public release. (Published by the maintainer's decision, 2026-09-30.)
- [x] No `#part….xhtml` link left in `fa/` (§3a).
