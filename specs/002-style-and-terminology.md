# 002 — Style & Terminology

The decisions that keep 70 files sounding like one translator.

---

## 0. How to use this spec

Entries are **proposed** until the pilot (spec 003) has put them through real text; then they become **settled**. Settle a decision the second time you hesitate over the same sentence, not before. When a settled decision conflicts with text already in `fa/`, the spec wins and the text is fixed in a `revise(NN):` commit.

Where a sibling project has already settled a term (ذن، کوآن), use it. A reader of the whole series should not meet two Persian words for one idea. The reference is Ikkyu's `STYLE.md` §2 (the only sibling with an argued glossary); where it is silent, the majority form across the sibling `fa/` trees (Ikkyu, Record of Linji, Lin-chi) wins, and the Notes column cites the count.

The pilot's rule for the rest: **where the model's own form is defensible, settle on it** — every file after the pilot then needs no hand edit. Override the model only for series consistency or a real error, and expect to fix those forms by hand in every file (§7 lists them).

---

## 1. Register

The source is conversational English written for a newcomer: short sentences, second person, the author's own stories. The translation should read the same way to a Persian newcomer.

| Text | Register | Status |
|------|-------------------|--------|
| Answers | Plain written Persian (نوشتاری ساده و روان) — not ornate کتابی, not محاوره | **settled** — the Advanced model's default |
| Sidebars (first-person stories) | Same written register; the anecdote's tone comes from word choice, not colloquial verb endings | **settled** — 1-04 |
| Dialogue inside stories and koans | Written register; short and blunt, as in the source. A teacher speaks to a student or a layman with **تو** (بودا to the farmer, بودی‌دارما to هویی-ک’و), as the model renders it | **settled** — 1-03, 1-04 |
| Quoted verse and sutra lines | Measured, short lines; keep the source's line breaks | **settled** — 1-03, 1-05 |

- Address to the reader: **شما** throughout, sidebars included. **Settled** — the sidebars are the author's first-person stories, not addressed to the reader, so there is nothing to soften; تو lives only inside dialogue.
- Avoid heavy Arabic-derived religious vocabulary where a plain Persian word carries the meaning; this book's point is that Zen is not exotic.

---

## 2. Book and part titles

| Source | Proposed Persian | Status |
|--------|------------------|--------|
| Book title | `<<<TBD>>>` — candidates: «ذن بی‌حاشیه برای تازه‌کارها»، «ذن، ساده و بی‌تعارف» | open |
| Subtitle | `<<<TBD>>>` | open |
| Part One: Origins and History | بخش یکم: خاستگاه و تاریخ | **settled** |
| Part Two: Core Concepts | بخش دوم: مفاهیم بنیادین | proposed |
| Part Three: Core Teachings | بخش سوم: آموزه‌های بنیادین | proposed |
| Part Four: Core Practices | بخش چهارم: تمرین‌های بنیادین | proposed |
| EVERYDAY ZEN (sidebar label) | ذن در زندگی روزمره | **settled** — emitted by `apparatus.py` |
| What You'll Learn | آنچه خواهید آموخت | **settled** — the model's form in `part-1`; it runs into the paragraph, not a heading |
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
| Buddhism / Buddhist | بودیسم / بودایی | Siblings 184 : 43 over آیین بودا; the model's form | **settled** |
| dharma | دارما | Lower-case "the teaching" sense vs. capital "Dharma": same word. Ikkyu §2.7 | **settled** |
| sangha | سانگا | Siblings 15 : 1 over سنگه | proposed |
| zazen | زازن | "just sitting" → «فقط نشستن» (proposed). 1-07 | **settled** |
| meditation | مراقبه | 111× in the source, the book's commonest term. Siblings 211; the model's form | **settled** |
| sitting Zen / sitting meditation | نشستن ذن / مراقبهٔ نشسته | | proposed |
| enlightenment | روشنگری | Siblings 257 : 38 over روشن‌شدگی, and the model's form. Replaces the earlier روشن‌شدگی. Avoid اشراق (Suhrawardi connotation); the model slipped once, in 1-03 | **settled** |
| awakening | بیداری | Kept distinct from enlightenment, as the siblings do (82) | proposed |
| sudden / gradual enlightenment | روشنگری ناگهانی / تدریجی | | proposed |
| nirvana | نیروانا | Ikkyu §2.7 | **settled** |
| karma | کارما | | proposed |
| reincarnation / rebirth | تولد دوباره | Avoid تناسخ unless the source means transmigration specifically | proposed |
| emptiness | تهی‌بودگی | | proposed |
| impermanence | ناپایداری | | proposed |
| suffering | رنج | 1-01, 1-02 | **settled** |
| desire / attachment | خواهش / دلبستگی | attachment settled (1-02, 1-05); desire proposed | **settled** |
| ego | خود / منِ نفسانی | Pick one at pilot | proposed |
| dualistic thinking | ذهن دوگانه‌انگار | | proposed |
| beginner's mind | ذهن نوآموز | | proposed |
| "don't know" mind | ذهنِ «نمی‌دانم» | Kwan Um key term; always with guillemets | proposed |
| Great Doubt / Great Faith / Great Courage | شک بزرگ / ایمان بزرگ / شجاعت بزرگ | | proposed |
| three poisons (greed, anger, ignorance) | سه زهر (آز، خشم، نادانی) | | proposed |
| five precepts | پنج اصل اخلاقی | The model's form (1-14), replacing پنج پیمان; the vow wording inside is «عهد می‌بندم که…» | **settled** |
| Four Great Vows | چهار عهد بزرگ | 1-13; vow → عهد | **settled** |
| bodhisattva | بودی‌ساتوا | Siblings' `fa/` 152, with ZWNJ (Ikkyu's table writes it without; its text does not). The model writes بودیساتوا | **settled** |
| Buddha-nature | طبیعت بودایی | Siblings split (طبیعت بودا 17، سرشت بودا 14، طبیعت بودایی 14); the model's form in 1-03 | **settled** |
| sutra | سوترا | Ikkyu §2.7. Diamond / Heart / Platform Sutra → سوترای الماس / سوترای قلب / سوترای سکو (settled, 1-05, 1-06; the model's forms, replacing سوترای دل) | **settled** |
| Mahayana / Theravada / Vajrayana | مهایانه / تراوادا / وجرایانه | Siblings write مهایانه (73) and never ماهایانه. **The model writes ماهایانا / واجریانا — fix by hand** | **settled** |
| Chan (Chinese Zen) | چان | Siblings. The model wrote «چَن» in 1-01 | **settled** |
| Taoism / Tao | تائوئیسم / تائو | Siblings 9 : 2 over دائوئیسم; the model's form | **settled** |
| Confucianism | کنفوسیوس‌گرایی | The model's form; siblings 6 | **settled** |
| mantra | مانترا | | proposed |
| retreat | دورهٔ خلوت (ریتریت) | Latin in parentheses on first use | proposed |
| prostration(s) | سجده | | proposed |
| Zen master / teacher | استاد ذن / آموزگار ذن | Zen master settled (1-02); the model also uses استاد for teacher | **settled** |
| patriarch | پاتریارک | first / second / sixth patriarch → نخستین / دومین / ششمین پاتریارک. Siblings 272; replaces the earlier «نیای ششم». The model adds a gloss in parentheses (پیشوای ارشد / معنوی) and sometimes uses پیشوا alone; the gloss is tolerated, پیشوا alone is fixed | **settled** |
| student | شاگرد | The model's usual form; دانش‌آموز only for a schoolchild (1-11's classroom game) | **settled** |
| Blue Cliff Record | «سوابق صخره آبی» | Ikkyu's form, and the model's (1-06) | **settled** |
| transmission | انتقال (دارما) | dharma transmission → انتقال دارما; mind-to-mind → ذهن‌به‌ذهن | **settled** |

---

## 4. Proper names

| English | Proposed Persian | Status |
|---------|------------------|--------|
| Bodhidharma | بودی‌دارما | **settled** — siblings 72 : 29. **The model writes بودیدهارما — fix by hand** (all 20 occurrences are in the pilot) |
| Hui-neng | هویی-ننگ | **settled** — Ikkyu §2.8 — the kasre goes, the hyphen stays |
| Hui-k’o | هویی-ک’و | **settled** — Ikkyu §2.2. The model wrote three forms in one file |
| Shen-hsiu | شن-شیو | **settled** — model writes شِن‌شیو |
| Lin-chi | لین-چی | **settled** — Ikkyu's form; Record of Linji's لینجی is Pinyin. Model writes لین‌چی |
| Huai-jang | هوآی-جانگ | **settled** — Lin-chi's form; model writes هوآی‌جانگ |
| Ma-tzu | ما-تسو | **settled** — siblings' Ma-tsu; model writes ما-تزو |
| Te-shan / Hsueh-tou / Yuan-wu | ته-شان / شوئه-تو / یوان-وو | **settled** — Ikkyu §2.8 |
| Providence Zen Center | مرکز ذن پراویدنس | **settled** — the model's form |
| Mahakasyapa | ماهاکاشیاپا | **settled** — Record of Linji, and the model's form |
| Emperor Wu (of Liang) | امپراتور وو (از دودمان لیانگ) | **settled** — siblings, and the model's form |
| Vulture Peak | قلهٔ کرکس | **settled** — Record of Linji, and the model's form |
| Shaolin Monastery | صومعهٔ شائولین | **settled** — the model's form |
| Seung Sahn | سونگ سان | **settled** — the model's form |
| Kwan Um School of Zen | مکتب ذن کوان اوم | **settled** (1-13, 1-14). «کوان» here is why koan must stay «کوآن»: the model writes «کوان» for koan (1-02) |
| Rinzai / Soto | رینزای / سوتو | **settled** — siblings, 1-05, 1-07 |
| Dogen | دوگن | proposed — siblings |
| D. T. Suzuki | دی. تی. سوزوکی | proposed — سوزوکی in Record of Linji |

- The source is Wade-Giles (Hui-k’o, Lin-chi, Ma-tzu, Chao-chou). Transliterate by Ikkyu `STYLE.md` §2.1–§2.3: never from Pinyin, the hyphen stays, the `’` is carried inside the Persian word, no kasre. A name already in Ikkyu §2.8 (Te-shan, Chao-chou, Wu-men, Huang-po …) takes that form. Ma-tzu is Ma-tsu: ما-تسو, as the siblings write it.
- Latin form in parentheses on first occurrence: **tolerated, not required.** The model adds it on its own often (1-05 on every name, 1-04 even on «ذن (Zen)» twice) and not at all elsewhere (1-03). Enforcing it by hand in 60 files buys little; like Ikkyu §2.6, this is accepted variation.
- Book titles in Resources and References stay in English; see spec 007.

---

## 5. Typography & orthography

Enforced by `bargardan_tools.normalize`:

- Persian `ی` (U+06CC) and `ک` (U+06A9) only.
- ZWNJ: `می‌شود`، `کتاب‌ها`، `بی‌دلبستگی`.
- Quotes `«…»`, nested `«… «…» …»`.
- Not enforced, tolerated: the ezafe after ه is written three ways by the model (لحظهٔ، تاریخچه‌ی، قله کرکس). No checker handles it and it changes no meaning.
- Digits: **settled — Persian in prose** (`1,200 monks` → ۱۲۰۰ راهب, `83 problems` → ۸۳ مشکل). The Advanced model persianises every prose numeral unprompted (Ikkyu `STYLE.md` §5.1; confirmed in 1-04). Latin digits in a draft are a sign the Classic model was served — re-run the file. `latin_digits = false` stays: it means *do not rewrite digits in either direction*. The ISBN on the copyright page is spec 007's call.

---

## 6. Acceptance Criteria

- [x] Register decisions in §1 settled after the pilot.
- [ ] Book title and subtitle settled.
- [x] Every term used in the pilot files is **settled** in §3/§4.
- [x] `[tool.book.titles]` in `pyproject.toml` filled from §2 (wording stays proposed; edit both together).
- [x] Digits policy settled and reflected in `[tool.normalize]`.

---

## 7. Hand fixes after every run

The model's forms that §3/§4 override. Check each new `fa/` file for them before commit:

| Model writes | Fix to |
|--------------|--------|
| ماهایانا / واجریانا | مهایانه / وجرایانه |
| بودیدهارما | بودی‌دارما |
| بودیساتوا | بودی‌ساتوا |
| مدیتیشن | مراقبه |
| روشن‌شدگی، اشراق (often in parentheses after روشنگری or بیداری) | روشنگری; drop the parenthesis |
| طبیعت بودا، سرشت بودا | طبیعت بودایی |
| دانش‌آموز for a Zen student | شاگرد |
| «کوان» (koan) | «کوآن» |
| هوی‌نِنگ، هوی-کو، شِن‌شیو، لین‌چی، هوآی‌جانگ، ته‌شان — any Wade-Giles name with ZWNJ or kasre | hyphen, no kasre (§4) |
| ما-تزو | ما-تسو |
| اشراق | روشنگری |
| پیشوا for patriarch, without پاتریارک | پاتریارک |
| U+200B zero-width space (1-03 had two) | delete |
| two ASCII spaces where the source had an em-dash aside (1-01, 1-11) | parentheses |
