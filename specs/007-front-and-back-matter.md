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

- [x] `introduction.md`
- [x] `front-matter.md` — dedication + Persian colophon
- [x] `resources.md`
- [x] `references.md`
- [x] `acknowledgments.md`
- [x] `about-the-author.md`

**Findings (2026-09-30).**

- **introduction** came back Advanced. Hand fixes from 002 §7: خلوت‌نشینی → دورهٔ خلوت‌گزینی, آیین بوداییِ ذن → بودیسمِ ذن, a (مدیتیشن) gloss, شفافیت → روشنی, «ذنِ روزمره» → the sidebar label. The book title is now settled (002 §2). Its four `#part….xhtml` links are left for spec 008 §3a.
- **acknowledgments, about-the-author** came back Classic on every run, identical text each time (سونگ ساهن، دانش‌آموز، «مدرسه ذن»، retreats as «دوره‌های کوتاه»). Both are one paragraph; rewritten by hand.
- **resources**: the model translated the titles; they were put back in English, author lines verbatim. No Persian edition of any of the seven could be verified (searched 2026-09-30), so none is noted.
- **references**: not sent to the model. `strip` + `restore` on the English text gives the Persian heading and the ornament. `check_linebreaks` has no off switch, so the entries are one sentence per line, which renders the same.
- **front-matter**: written by hand, not translated. The 15 legal blocks are replaced by a 6-block colophon (title, source edition and ISBN, the Kwan Um credit restated as attribution only, translator, machine-translation note, CC BY-SA 4.0 like the Lin-chi sibling). `parity: offset -8`, explained in the file. The cover/title/ornament images stay for spec 008 §3 to decide.

---

## 3. Acceptance Criteria

- [x] All 6 files `status: reviewed`.
- [x] `just check` clean, with any parity offsets declared and explained inline.
- [x] No English legal text from the source remains in `fa/`.
