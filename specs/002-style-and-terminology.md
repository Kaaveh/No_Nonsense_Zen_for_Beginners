# 002 — Style & Terminology

The decisions that keep 70 files sounding like one translator.

---

## 0. How to use this spec

Entries are **proposed** until the pilot (spec 003) has put them through real text; then they become **settled**. Settle a decision the second time you hesitate over the same sentence, not before. When a settled decision conflicts with text already in `fa/`, the spec wins and the text is fixed in a `revise(NN):` commit.

Where a sibling project has already settled a term (ذن، کوآن), use it. A reader of the whole series should not meet two Persian words for one idea.

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
| Buddha | بودا | | proposed |
| Buddhism | بودیسم / آیین بودا | Pick one at pilot | proposed |
| dharma | دارما | Lower-case "the teaching" sense vs. capital "Dharma": same word | proposed |
| sangha | سانگا | | proposed |
| zazen | زازن | "just sitting" → «فقط نشستن» | proposed |
| sitting Zen / sitting meditation | نشستن ذن / مراقبهٔ نشسته | | proposed |
| enlightenment | روشن‌شدگی | Avoid اشراق (Suhrawardi connotation) | proposed |
| sudden / gradual enlightenment | روشن‌شدگی ناگهانی / تدریجی | | proposed |
| nirvana | نیروانا | | proposed |
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
| bodhisattva | بودی‌ساتوا | | proposed |
| sutra | سوترا | Heart Sutra → سوترای دل; Diamond Sutra → سوترای الماس | proposed |
| Mahayana / Theravada / Vajrayana | ماهایانه / تراوادا / وجرایانه | | proposed |
| mantra | مانترا | | proposed |
| retreat | دورهٔ خلوت (ریتریت) | Latin in parentheses on first use | proposed |
| prostration(s) | سجده | | proposed |
| Zen master / teacher | استاد ذن / آموزگار ذن | | proposed |
| transmission | انتقال (دارما) | | proposed |

---

## 4. Proper names

| English | Proposed Persian | Status |
|---------|------------------|--------|
| Bodhidharma | بودی‌دارما | proposed |
| Hui-neng / the Sixth Patriarch | هویی‌نِنگ / نیای ششم | proposed |
| Seung Sahn | سونگ سان | proposed |
| Kwan Um School of Zen | مکتب ذن کوان اوم | proposed |
| Rinzai / Soto | رینزای / سوتو | proposed |
| Dogen | دوگن | proposed |
| D. T. Suzuki | دی. تی. سوزوکی | proposed |

- Latin form in parentheses **on first occurrence per file**: `بودی‌دارما (Bodhidharma)`. Readers meet these names again elsewhere; give them the handle to search.
- Book titles in Resources and References stay in English; see spec 007.

---

## 5. Typography & orthography

Enforced by `bargardan_tools.normalize`:

- Persian `ی` (U+06CC) and `ک` (U+06A9) only.
- ZWNJ: `می‌شود`، `کتاب‌ها`، `بی‌دلبستگی`.
- Quotes `«…»`, nested `«… «…» …»`.
- Digits: `<<<TBD>>>` — Persian digits in prose (`latin_digits = true`) is the likely choice for a non-scholarly book; the only Latin numbers are years and ISBNs.

---

## 6. Acceptance Criteria

- [ ] Register decisions in §1 settled after the pilot.
- [ ] Book title and subtitle settled.
- [ ] Every term used in the pilot files is **settled** in §3/§4.
- [ ] `[tool.book.titles]` in `pyproject.toml` filled from §2.
- [ ] Digits policy settled and reflected in `[tool.normalize]`.
