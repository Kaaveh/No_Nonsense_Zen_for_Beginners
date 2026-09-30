# 002 — Style & Terminology

The decisions that keep 70 files sounding like one translator.

---

## 0. How to use this spec

Entries are **proposed** until the pilot (spec 003) has put them through real text; then they become **settled**. Settle a decision the second time you hesitate over the same sentence, not before. When a settled decision conflicts with text already in `fa/`, the spec wins and the text is fixed in a `revise(NN):` commit.

Where a sibling project has already settled a term (ذن، کوآن), use it. A reader of the whole series should not meet two Persian words for one idea. The reference is Ikkyu's `STYLE.md` §2 (the only sibling with an argued glossary); where it is silent, the majority form across the sibling `fa/` trees (Ikkyu, Record of Linji, Lin-chi) wins, and the Notes column cites the count.

---

## 1. Register

The source is conversational English written for a newcomer: short sentences, second person, the author's own stories. The translation should read the same way to a Persian newcomer.

| Text | Proposed register | Status |
|------|-------------------|--------|
| Answers | Plain written Persian (نوشتاری ساده و روان) — not ornate کتابی, not محاوره | proposed |
| Sidebars (first-person stories) | Same written register; the anecdote's tone comes from word choice, not colloquial verb endings | proposed |
| Dialogue inside stories and koans | Written register; short and blunt, as in the source | proposed |
| Quoted verse and sutra lines | Measured, short lines; keep the source's line breaks | proposed |

- Address to the reader: **شما** throughout. `<<<TBD at pilot>>>` whether to soften to تو in sidebars.
- Avoid heavy Arabic-derived religious vocabulary where a plain Persian word carries the meaning; this book's point is that Zen is not exotic.

---

## 2. Book and part titles

| Source | Proposed Persian | Status |
|--------|------------------|--------|
| Book title | `<<<TBD>>>` — candidates: «ذن بی‌حاشیه برای تازه‌کارها»، «ذن، ساده و بی‌تعارف» | open |
| Subtitle | `<<<TBD>>>` | open |
| Part One: Origins and History | بخش یکم: خاستگاه و تاریخ | proposed |
| Part Two: Core Concepts | بخش دوم: مفاهیم بنیادین | proposed |
| Part Three: Core Teachings | بخش سوم: آموزه‌های بنیادین | proposed |
| Part Four: Core Practices | بخش چهارم: تمرین‌های بنیادین | proposed |
| EVERYDAY ZEN (sidebar label) | ذن در زندگی روزمره | proposed |
| What You'll Learn | آنچه در این بخش می‌آموزید | proposed |
| Introduction and How to Use This Book | پیش‌گفتار و راهنمای استفاده از کتاب | proposed |
| Resources / References | منابع برای مطالعهٔ بیشتر / کتاب‌نامه | proposed |
| Acknowledgments / About the Author | سپاس‌گزاری / دربارهٔ نویسنده | proposed |

Headings keep sentence case in Persian; the source's ALL CAPS is typographic, not meaning.

---

## 3. Terminology

| English | Proposed Persian | Notes | Status |
|---------|------------------|-------|--------|
| Zen | ذن | Sibling projects | **settled** |
| koan | کوآن | Sibling projects | **settled** |
| Buddha | بودا | Ikkyu §2.7 | **settled** |
| Buddhism / Buddhist | بودیسم / بودایی | Siblings 184 : 43 over آیین بودا | proposed |
| dharma | دارما | Lower-case "the teaching" sense vs. capital "Dharma": same word. Ikkyu §2.7 | **settled** |
| sangha | سانگا | Siblings 15 : 1 over سنگه | proposed |
| zazen | زازن | "just sitting" → «فقط نشستن» | proposed |
| meditation | مراقبه | 111× in the source, the book's commonest term. Siblings 211 | proposed |
| sitting Zen / sitting meditation | نشستن ذن / مراقبهٔ نشسته | | proposed |
| enlightenment | روشن‌شدگی | Avoid اشراق (Suhrawardi connotation). Siblings 38 | proposed |
| awakening | بیداری | Kept distinct from enlightenment, as the siblings do (82) | proposed |
| sudden / gradual enlightenment | روشن‌شدگی ناگهانی / تدریجی | | proposed |
| nirvana | نیروانا | Ikkyu §2.7 | **settled** |
| karma | کارما | | proposed |
| reincarnation / rebirth | تولد دوباره | Avoid تناسخ unless the source means transmigration specifically | proposed |
| emptiness | تهی‌بودگی | | proposed |
| impermanence | ناپایداری | | proposed |
| suffering | رنج | | proposed |
| desire / attachment | خواهش / دلبستگی | | proposed |
| ego | خود / منِ نفسانی | Pick one at pilot | proposed |
| dualistic thinking | ذهن دوگانه‌انگار | | proposed |
| beginner's mind | ذهن نوآموز | | proposed |
| "don't know" mind | ذهنِ «نمی‌دانم» | Kwan Um key term; always with guillemets | proposed |
| Great Doubt / Great Faith / Great Courage | شک بزرگ / ایمان بزرگ / شجاعت بزرگ | | proposed |
| three poisons (greed, anger, ignorance) | سه زهر (آز، خشم، نادانی) | | proposed |
| five precepts | پنج پیمان | | proposed |
| Four Great Vows | چهار عهد بزرگ | | proposed |
| bodhisattva | بودی‌ساتوا | Siblings' `fa/` 152, with ZWNJ (Ikkyu's table writes it without; its text does not) | proposed |
| Buddha-nature | طبیعت بودا | Siblings 17 : 14 over سرشت بودا | proposed |
| sutra | سوترا | Ikkyu §2.7. Heart Sutra → سوترای دل; Diamond Sutra → سوترای الماس (proposed) | **settled** |
| Mahayana / Theravada / Vajrayana | مهایانه / تراوادا / وجرایانه | Siblings write مهایانه (73) and never ماهایانه | proposed |
| Chan (Chinese Zen) | چان | Siblings | proposed |
| Taoism / Tao | تائوئیسم / تائو | Siblings 9 : 2 over دائوئیسم | proposed |
| Confucianism | آیین کنفوسیوس | | proposed |
| mantra | مانترا | | proposed |
| retreat | دورهٔ خلوت (ریتریت) | Latin in parentheses on first use | proposed |
| prostration(s) | سجده | | proposed |
| Zen master / teacher | استاد ذن / آموزگار ذن | | proposed |
| patriarch | پاتریارک | first / second / sixth patriarch → نخستین / دومین / ششمین پاتریارک. Siblings 272; replaces the earlier «نیای ششم» | proposed |
| transmission | انتقال (دارما) | mind-to-mind transmission → انتقال ذهن به ذهن | proposed |

---

## 4. Proper names

| English | Proposed Persian | Status |
|---------|------------------|--------|
| Bodhidharma | بودی‌دارما | proposed — Record of Linji 63, Lin-chi 9 |
| Hui-neng | هویی-ننگ | **settled** — Ikkyu §2.8 — the kasre goes, the hyphen stays |
| Hui-k’o | هویی-ک’و | proposed — Ikkyu §2.2 |
| Shen-hsiu | شن-شیو | proposed |
| Lin-chi | لین-چی | proposed — Ikkyu's form; Record of Linji's لینجی is Pinyin |
| Mahakasyapa | ماهاکاشیاپا | proposed — Record of Linji |
| Emperor Wu (of Liang) | امپراتور وو (از لیانگ) | proposed — siblings |
| Vulture Peak | قلهٔ کرکس | proposed — Record of Linji |
| Shaolin Monastery | صومعهٔ شائولین | proposed |
| Seung Sahn | سونگ سان | proposed |
| Kwan Um School of Zen | مکتب ذن کوان اوم | proposed |
| Rinzai / Soto | رینزای / سوتو | proposed — siblings |
| Dogen | دوگن | proposed — siblings |
| D. T. Suzuki | دی. تی. سوزوکی | proposed — سوزوکی in Record of Linji |

- The source is Wade-Giles (Hui-k’o, Lin-chi, Ma-tzu, Chao-chou). Transliterate by Ikkyu `STYLE.md` §2.1–§2.3: never from Pinyin, the hyphen stays, the `’` is carried inside the Persian word, no kasre. A name already in Ikkyu §2.8 (Te-shan, Chao-chou, Wu-men, Huang-po …) takes that form. Ma-tzu is Ma-tsu: ما-تسو, as the siblings write it.
- Latin form in parentheses **on first occurrence per file**: `بودی‌دارما (Bodhidharma)`. Readers meet these names again elsewhere; give them the handle to search.
- Book titles in Resources and References stay in English; see spec 007.

---

## 5. Typography & orthography

Enforced by `bargardan_tools.normalize`:

- Persian `ی` (U+06CC) and `ک` (U+06A9) only.
- ZWNJ: `می‌شود`، `کتاب‌ها`، `بی‌دلبستگی`.
- Quotes `«…»`, nested `«… «…» …»`.
- Digits: **settled — Persian in prose** (`1,200 years` → ۱٬۲۰۰ سال). The Advanced model persianises every prose numeral unprompted and identically on re-runs (measured across ten files, Ikkyu `STYLE.md` §5.1), so this is what the pipeline produces anyway. `latin_digits = false` stays: it means *do not rewrite digits in either direction*. The ISBN on the copyright page is spec 007's call.

---

## 6. Acceptance Criteria

- [ ] Register decisions in §1 settled after the pilot.
- [ ] Book title and subtitle settled.
- [ ] Every term used in the pilot files is **settled** in §3/§4.
- [x] `[tool.book.titles]` in `pyproject.toml` filled from §2 (wording stays proposed; edit both together).
- [x] Digits policy settled and reflected in `[tool.normalize]`.
