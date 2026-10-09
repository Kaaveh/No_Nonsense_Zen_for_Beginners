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
| Dialogue inside stories and koans | Written register; short and blunt, as in the source. A teacher speaks to a student or a layman with **تو** (بودا to the farmer, بودی‌دارما to هویی‌کو), as the model renders it | **settled** — 1-03, 1-04 |
| Quoted verse and sutra lines | Measured, short lines; keep the source's line breaks | **settled** — 1-03, 1-05 |

- Address to the reader: **شما** throughout, sidebars included. **Settled** — the sidebars are the author's first-person stories, not addressed to the reader, so there is nothing to soften; تو lives only inside dialogue.
- Avoid heavy Arabic-derived religious vocabulary where a plain Persian word carries the meaning; this book's point is that Zen is not exotic.

---

## 2. Book and part titles

| Source | Proposed Persian | Status |
|--------|------------------|--------|
| Book title | ذن بی‌حاشیه برای تازه‌کارها | **settled** — maintainer's choice (spec 007); the model wrote «ذنِ بی‌حاشیه برای مبتدیان» |
| Subtitle: Clear Answers to Burning Questions About Core Zen Teachings | پاسخ‌های روشن به پرسش‌های داغ دربارهٔ آموزه‌های بنیادین ذن | **settled** — maintainer's choice (spec 008); «بنیادین» as in the part titles |
| Part One: Origins and History | بخش یکم: خاستگاه و تاریخ | **settled** |
| Part Two: Core Concepts | بخش دوم: مفاهیم بنیادین | **settled** |
| Part Three: Core Teachings | بخش سوم: آموزه‌های بنیادین | **settled** |
| Part Four: Core Practices | بخش چهارم: تمرین‌های بنیادین | **settled** |
| EVERYDAY ZEN (sidebar label) | ذن در زندگی روزمره | **settled** — emitted by `apparatus.py` |
| What You'll Learn | آنچه خواهید آموخت | **settled** — the model's form in `part-1`; it runs into the paragraph, not a heading |
| Introduction and How to Use This Book | پیش‌گفتار و راهنمای استفاده از کتاب | **settled** |
| Resources / References | منابع برای مطالعهٔ بیشتر / کتاب‌نامه | **settled** |
| Acknowledgments / About the Author | سپاس‌گزاری / دربارهٔ نویسنده | **settled** |
| "Everyday Zen" in running text | «ذن در زندگی روزمره» | **settled** — the label's form (introduction); the model wrote «ذنِ روزمره» (Everyday Zen) |

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
| sangha | سانگا | Siblings 15 : 1 over سنگه; the model's form (3-01) | **settled** |
| zazen | ذاذن | Maintainer's choice, replacing زازن. "just sitting" → «فقط نشستن» (proposed). 1-07 | **settled** |
| meditation | مراقبه | 111× in the source, the book's commonest term. Siblings 211; the model's form | **settled** |
| sitting Zen / sitting meditation | نشستن به مراقبهٔ ذن / مراقبهٔ نشسته | sitting Zen settled (2-15): "we sit Zen" → به مراقبهٔ ذن می‌نشینیم. The model writes «نشستن در ذن (مدیتیشن ذن)». sitting meditation settled (4-01, 4-13); the model writes «مدیتیشن نشسته» | **settled** |
| enlightenment | روشنگری | Siblings 257 : 38 over روشن‌شدگی, and the model's form. Replaces the earlier روشن‌شدگی. Avoid اشراق (Suhrawardi connotation); the model slipped once, in 1-03 | **settled** |
| awakening | بیداری | Kept distinct from enlightenment, as the siblings do (82) | proposed |
| sudden / gradual enlightenment | روشنگری ناگهانی / تدریجی | 2-08 | **settled** |
| nirvana | نیروانا | Ikkyu §2.7 | **settled** |
| karma | کارما | Siblings 170; the model's form (2-10) | **settled** |
| reincarnation / rebirth | تناسخ / تولد دوباره | reincarnation settled: the source defines it as being "born again as another being" (2-11), which is transmigration. Siblings 27 : 14; the model's form. rebirth proposed | **settled** |
| emptiness | تهی‌بودگی | Siblings 45; the model's form (2-01, 2-02) | **settled** |
| impermanence | ناپایداری | The model's form (2-05) | **settled** |
| suffering | رنج | 1-01, 1-02 | **settled** |
| desire / attachment | میل / دلبستگی | attachment settled (1-02, 1-05). desire → میل, the model's form throughout 3-10, replacing the proposed خواهش (siblings: Ikkyu's poems only). aspiration → آرمان (3-10) | **settled** |
| ego | «من» (ایگو) | The source glosses ego as "what we call 'I' or 'me'" (2-10); the model's form. The gloss only on first use in the book (1-12), §4 | **settled** |
| Hui-k’o's dialogue with Bodhidharma (1-03) | «ذهنم آرام نیست. استاد، تمنا دارم…» / «…یافتنی نیست.» | Maintainer's revision toward the Chinese (無門關 41): 心未安 → آرام نیست, keeping the 安 echo through all four lines and keeping 苦 (رنج) out; 乞 → تمنا دارم; 了不可得 → یافتنی نیست, the 不可得 of the Diamond Sutra, not a failed search (نمی‌یابم) | **settled** |
| dualistic thinking | تفکر دوگانه | The source says thinking, not mind; the model's form (2-05, 2-06). Drop the parenthetical glosses it adds (ثنویت‌گرا، دوتایی) | **settled** |
| beginner's mind | ذهن آغازگر | Maintainer's choice, matching «ذهن ذن، ذهن آغازگر» (1-08); replaces the model's ذهن مبتدی and the earlier ذهن نوآموز | **settled** |
| "don't know" mind | ذهنِ «نمی‌دانم» | Kwan Um key term; the guillemets go round «نمی‌دانم» only. "don't know" alone → «نمی‌دانم». The model writes five forms in one part (§7) | **settled** |
| Great Doubt / Great Faith / Great Courage | شک بزرگ / ایمان بزرگ / شجاعت بزرگ | "Great" as in چهار عهد بزرگ. Only in 3-01. The model writes «شکِ عظیم» | **settled** |
| Four Noble Truths / eightfold path | چهار حقیقت شریف / راه هشت‌گانه | Siblings; the model's forms (3-02) | **settled** |
| interdependence | وابستگی متقابل | The model's form (3-08); وابستگی is right here, it is the "depend" sense | **settled** |
| Bodhisattva Way | راه بودی‌ساتوا | 3-08. The model writes «طریقت بودی‌ساتوا»; طریقت is Sufi vocabulary (§1) | **settled** |
| three poisons (greed, hatred, delusion) | سه زهر: طمع، نفرت، توهم (جهل) | The source's own list is greed, hatred, delusion (ignorance); the model's form (2-05) | **settled** |
| five precepts | پنج اصل اخلاقی | The model's form (1-14), replacing پنج پیمان; the vow wording inside is «عهد می‌بندم که…» | **settled** |
| Four Great Vows | چهار عهد بزرگ | 1-13; vow → عهد | **settled** |
| bodhisattva | بودی‌ساتوا | Siblings' `fa/` 152, with ZWNJ (Ikkyu's table writes it without; its text does not). The model writes بودیساتوا | **settled** |
| Buddha-nature | طبیعت بودایی | Siblings split (طبیعت بودا 17، سرشت بودا 14، طبیعت بودایی 14); the model's form in 1-03 | **settled** |
| sutra | سوترا | Ikkyu §2.7. Diamond / Heart / Platform Sutra → سوترای الماس / سوترای قلب / سوترای سکو (settled, 1-05, 1-06; the model's forms, replacing سوترای دل) | **settled** |
| Mahayana / Theravada / Vajrayana | مهایانه / تراوادا / وجرایانه | Siblings write مهایانه (73) and never ماهایانه. **The model writes ماهایانا / واجریانا — fix by hand** | **settled** |
| Chan (Chinese Zen) | چان | Siblings. The model wrote «چَن» in 1-01 | **settled** |
| Taoism / Tao | تائوئیسم / تائو | Siblings 9 : 2 over دائوئیسم; the model's form | **settled** |
| Confucianism | کنفوسیوس‌گرایی | The model's form; siblings 6 | **settled** |
| mantra | مانترا | The model's form (4-01, 4-02) | **settled** |
| chanting / chant | ذکر | ~24× in Part Four. The model's form throughout 4-02 and 4-04; chanting meditation → مراقبه با ذکر. Drop its glosses (ذکرخوانی (چنتینگ)، (chanting)) and «سرودها و اذکار» (4-12) | **settled** |
| shikantaza | شیکانتازا | The model writes it with and without ZWNJ (4-01, 4-02); one word, no ZWNJ | **settled** |
| walking meditation | مراقبهٔ راه رفتن | 4-02, 4-14; the model writes «مدیتیشن پیاده‌روی» | **settled** |
| meditation cushion | بالشتک (بالشتکِ مراقبه) | Parts One–Three's form; the model writes تشکچه in 4-13, 4-14 | **settled** |
| working Zen | ذنِ کار | 4-02 | **settled** |
| backseat driver | رانندهٔ صندلی عقب | The model's form in 4-08; it wrote «راننده‌ی ناخوانده» (صدای مزاحم درونی) in 4-14 | **settled** |
| moktak | موک‌تاک | 4-12; the source glosses it itself | **settled** |
| Gateless Gate | «دروازهٔ بی‌دروازه» | The model's form (4-10); siblings 1 | **settled** |
| Mu (Chao-chou's answer) | «مو» | Siblings 17; the model's form (4-10) | **settled** |
| retreat | دورهٔ خلوت‌گزینی (ریتریت) | The model's form (2-04, 2-08); the gloss only on first use in the book (introduction), §4 | **settled** |
| prostration(s) | سجده | bow → تعظیم. 2-04 | **settled** |
| Zen master / teacher | استاد ذن / آموزگار ذن | Zen master settled (1-02); the model also uses استاد for teacher | **settled** |
| patriarch | پاتریارک | first / second / sixth patriarch → نخستین / دومین / ششمین پاتریارک. Siblings 272; replaces the earlier «نیای ششم». The model adds a gloss in parentheses (پیشوای ارشد / معنوی) and sometimes uses پیشوا alone; the gloss is tolerated, پیشوا alone is fixed | **settled** |
| student | شاگرد | The model's usual form; دانش‌آموز only for a schoolchild (1-11's classroom game) | **settled** |
| Blue Cliff Record | «سوابق صخره آبی» | Ikkyu's form, and the model's (1-06) | **settled** |
| transmission | انتقال (دارما) | dharma transmission → انتقال دارما; mind-to-mind → ذهن‌به‌ذهن | **settled** |
| enlightened nature | ماهیت روشن‌یافته | ~30× in the source. original enlightened nature → ماهیت اصیل و روشن‌یافته. The model wrote nine variants across Parts One and Two (سرشت / طبیعت × روشن‌بینانه / روشن‌ضمیر / روشنگر); Part One revised to match. Not "nature of enlightenment" (1-05: ماهیت روشنگری, correct there) | **settled** |
| Tao Te Ching | «دائو ته چینگ» | Siblings 33 : 7; the model writes «تائو ته چینگ» | **settled** |
| abbot / vice abbot (of a Zen center) | رئیس مرکز / معاون رئیس | 1-05's «رئیس صومعه» for a monastery; the model wrote «راهب اعظم» (about-the-author) | **settled** |
| Kyol Che (retreat) | «کیول چه» | The model's form (about-the-author) | **settled** |
| inka | «اینکا» | The model's form; the source glosses it itself | **settled** |
| sitting group | گروه مراقبهٔ نشسته | The model wrote «گروه نشسته» | **settled** |

---

## 4. Proper names

| English | Proposed Persian | Status |
|---------|------------------|--------|
| Bodhidharma | بودی‌دارما | **settled** — siblings 72 : 29. **The model writes بودیدهارما — fix by hand** (all 20 occurrences are in the pilot) |
| Hui-neng | هویی-ننگ | **settled** — Ikkyu §2.8 — the kasre goes, the hyphen stays |
| Hui-k’o | هویی‌کو | **settled** — maintainer's choice, overriding Ikkyu §2.2's هویی-ک’و: the Wade-Giles ’ only marks aspiration and means nothing in Persian script, and the hyphen becomes a ZWNJ. The Latin gloss keeps Hui-k’o |
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
| Lao Tzu | لائوتزو | **settled** — siblings 147; the model's form (2-10) |
| Dae Kwang | دائه کوانگ | **settled** — the model's form in 2-14; it wrote دِه کوانگ in 2-12 |
| Man Gong | مان گونگ | **settled** — the model's form (2-08) |
| Empty Gate Zen Center | مرکز ذن امپتی گیت | **settled** — the model's form (2-08, 2-12) |
| Kuan Yin | کوان یین | **settled** — Wade-Giles as the source spells it (§4 note; Ikkyu §2.1, Kuang → کوانگ), and the model's form in 3-12. The siblings' گوان‌یین is Record of Linji's Pinyin |
| Wonhyo | وونهیو | **settled** — the model's form (3-12) |
| Jon Kabat-Zinn | جان کابات-زین | **settled** — the model's form (3-08) |
| Pai Chang (Pai-chang) | پای-چانگ | **settled** — siblings 19; the model writes «پای‌چانگ» (4-02) |
| Chao-chou | چائو-چو | **settled** — siblings 10, and the model's form (4-10) |
| Jason Quinn (the author) | جیسون کویین | **settled** — spec 008's form; the model writes جیسون کوین |
| Bon Soeng | بون سونگ | **settled** — the model's form (acknowledgments) |
| Kendra / Myles / Ella | کندرا / مایلز / اِلا | **settled** — dedication |
| Thubten Chodron | توبتن (چودرون) | **settled** — the model's form; the author line itself stays in English (spec 007) |
| Dogen | دوگن | proposed — siblings |
| D. T. Suzuki | دی. تی. سوزوکی | proposed — سوزوکی in Record of Linji |
| *Zen Mind, Beginner's Mind* (Shunryu Suzuki) | «ذهن ذن، ذهن آغازگر» | **settled** — maintainer's choice (1-08) |

- The source is Wade-Giles (Hui-k’o, Lin-chi, Ma-tzu, Chao-chou). Transliterate by Ikkyu `STYLE.md` §2.1–§2.3: never from Pinyin, the hyphen stays, the `’` is carried inside the Persian word, no kasre. A name already in Ikkyu §2.8 (Te-shan, Chao-chou, Wu-men, Huang-po …) takes that form. Ma-tzu is Ma-tsu: ما-تسو, as the siblings write it.
- English form in parentheses: **settled — first occurrence in the book only** (maintainer's rule). A name or term that carries an English gloss gets it on its first mention in book order (introduction onward; the copyright page and dedication do not count), and nowhere after. This covers transliterated glosses too: (ریتریت), (ایگو). A gloss the model puts on a later mention moves to the first one. Two parentheses in a row merge: «کوآن» (koan؛ …).
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
- [x] Book title and subtitle settled.
- [x] Every term used in the pilot files is **settled** in §3/§4.
- [x] `[tool.book.titles]` in `pyproject.toml` filled from §2 (wording stays proposed; edit both together).
- [x] Digits policy settled and reflected in `[tool.normalize]`.

---

## 7. Hand fixes after every run

The model's forms that §3/§4 override. Check each new `fa/` file for them before commit:

| Model writes | Fix to |
|--------------|--------|
| ماهایانا، مهایانا / واجریانا | مهایانه / وجرایانه |
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
| وابستگی for attachment (all of 2-07); keep it only for "depend" | دلبستگی |
| «ذهنِ ندانستن»، ذهن «نمی‌دانم»، «ذهنِ "نمی‌دانم"»، ذهنیت «نمی‌دانم» | ذهنِ «نمی‌دانم» |
| سرشت / طبیعت + روشن‌بینانه، روشن‌ضمیر، روشن‌بین، روشنگر (enlightened nature) | ماهیت روشن‌یافته |
| در آیین بودا | در بودیسم |
| مرکز ذن «پراویدنس» (Providence) | مرکز ذن پراویدنس |
| straight "…" quotes inside a Persian sentence | «…» (nested inside «…» when quoted) |
| ایگو، منیت، «ایگو» (منیت) | «من» (ایگو) on first use in the book (1-12), «من» after |
| «شکِ عظیم»، «ایمانِ عظیم»، «شجاعتِ عظیم» | شک / ایمان / شجاعت بزرگ |
| هنرجو for a Zen student | شاگرد |
| خلوت‌نشینی (ریتریت); مراقبه (ریتریت) for retreat | دورهٔ خلوت‌گزینی (ریتریت) |
| an English gloss after its first occurrence in the book (§4) | drop it |
| a parenthesis the source does not have: روشنگری (نیروانا)، مراقبه (مدیتیشن)، روشن‌ضمیر (بیدار)، «ذن» (Zen)، (Zazen) | drop it |
| [bracketed] alternative readings (3-07, 3-09) | pick the one the source means; drop the brackets |
| رکوع for bow (4-02) | تعظیم; رکوع is Islamic prayer vocabulary (§1) |
| مدیتیشن — back in 13 of 16 Part Four files, often as «مدیتیشن ذن» / «مدیتیشن نشسته» | مراقبه (مراقبهٔ ذن، مراقبهٔ نشسته) |
| ذکرخوانی (چنتینگ)، سرودها for chanting | ذکر |
| تشکچه for cushion | بالشتک |
| شفاف / شفافیت for "clear mind", "clarity" (Part Four throughout) | روشن / روشنی where the source means the Zen sense of clear; شفاف stays for plain transparency |
