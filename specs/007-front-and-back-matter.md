# 007 — Front & Back Matter

**6 files · ~11,400 characters**

Translated last: these files either reuse the whole book's vocabulary or need a policy rather than a translation.

---

## 1. Per-file policy

| File | Contents | Policy |
|------|----------|--------|
| `front-matter.md` | Cover, title page, copyright/legal page, dedication | **Do not translate the legal page.** Replace it with a Persian colophon (translator, source edition, licence of the translation). Translate the dedication. Keep the cover/title images or drop them per spec 008. |
| `introduction.md` | Welcome, the author's story, how to use the book | Standard loop. Translate after the four parts so it uses settled terms. |
| `resources.md` | Recommended books, each with a short annotation | Titles and authors **stay in English** (the reader needs them to find the book); translate the annotations. Note a Persian edition where one exists. |
| `references.md` | Bibliography | **Not translated.** Kept in English, `<!-- normalize: off -->` around the list. Persian heading only. |
| `acknowledgments.md` | Author's thanks | Standard loop. |
| `about-the-author.md` | Bio + author photo | Standard loop. Photo: see spec 008. |

The colophon replacing the legal page will not match `source/` block for block. Declare it with a parity offset comment rather than weakening the check.

---

## 2. Checklist

- [ ] `introduction.md`
- [ ] `front-matter.md` — dedication + Persian colophon
- [ ] `resources.md`
- [ ] `references.md`
- [ ] `acknowledgments.md`
- [ ] `about-the-author.md`

---

## 3. Acceptance Criteria

- [ ] All 6 files `status: reviewed`.
- [ ] `just check` clean, with any parity offsets declared and explained inline.
- [ ] No English legal text from the source remains in `fa/`.
