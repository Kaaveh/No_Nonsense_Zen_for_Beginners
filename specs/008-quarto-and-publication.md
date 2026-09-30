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

---

## 3a. Internal links

The EPUB's cross-references survive as `[text](#partNNNN.xhtml)` — dead targets outside the EPUB. One in `1-06` (to Part Four), four in `introduction.md`. The two in the source's `front-matter.md` went with the legal page (spec 007). Retarget each to the Quarto section id, or unlink it, before `quarto render`.

## 4. Publication decision

The repository is private. Publishing a translation of an in-copyright 2021 book needs the rights holder's permission. **Do not make the repo or the built book public until that is settled.** Record the outcome here.

---

## 5. Acceptance Criteria

- [ ] `_quarto.yml` lists all 70 files in book order.
- [ ] `index.md` with Persian overview, version and licence.
- [ ] `quarto render` produces HTML, PDF and EPUB locally without warnings.
- [ ] Image policy in §3 applied; no unlicensed image committed.
- [ ] Publication rights recorded in §4 before any public release.
- [ ] No `#part….xhtml` link left in `fa/` (§3a).
