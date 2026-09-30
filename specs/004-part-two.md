# 004 — Part Two: Core Concepts

**`fa/part-2.md`, `fa/2-01.md` – `fa/2-15.md` · 16 files · ~41,500 characters · 3 sidebars**

---

## 1. Context

The ideas: emptiness, beginner's mind and the "don't know" mind, the three poisons, dualistic thinking, non-attachment, sudden vs. gradual enlightenment, karma, rebirth, heaven and hell, God, and Zen alongside other religions.

This is the part where the terminology table in spec 002 §3 carries the most weight. The "don't know" mind (2-03, 2-04) is the book's signature idea and recurs through Parts Three and Four. Get its Persian form right here and hold it.

---

## 2. Checklist

- [x] `part-2.md` — Part opener
- [x] `2-01.md` — The most important aspect of Zen
- [x] `2-02.md` — Emptiness
- [x] `2-03.md` — Beginner's mind and "don't know" mind
- [x] `2-04.md` — "Don't know" vs. not knowing · *sidebar*
- [x] `2-05.md` — The three poisons
- [x] `2-06.md` — Dualistic thinking
- [x] `2-07.md` — Living without attachment
- [x] `2-08.md` — Sudden and gradual enlightenment · *sidebar*
- [x] `2-09.md` — What kind of Buddhist the Buddha would be today
- [x] `2-10.md` — Karma
- [x] `2-11.md` — Reincarnation
- [x] `2-12.md` — Heaven and hell · *sidebar*
- [x] `2-13.md` — Belief in God
- [x] `2-14.md` — Zen with other religions
- [x] `2-15.md` — How sitting helps the world

**Findings (2026-09-30).** All 16 drafts came back from the Advanced model on the first run: Persian digits, no پدرسالار, no Latin names. What still needed a hand:

- **Merged paragraphs, five files.** 2-03, 2-06 and 2-09 glued two prose paragraphs together. 2-08 and 2-12 glued the sidebar's first image sentinel onto the paragraph before it, as 1-08 did. Split in the draft before `restore`.
- **The signature term drifted most.** "don't know" mind came back five ways, and "enlightened nature" nine ways across Parts One and Two. Attachment came back as وابستگی for all of 2-07 despite being settled. All three are now in spec 002 §7, and Part One's "enlightened nature" was revised to the settled form.
- **U+200B** again, in six files. `normalize` does not strip it; delete it in the draft.
- **One meaning loss.** 2-12's sidebar punchline "My mind was in hell" came back as «ذهنم در آشوب و عذاب بود», which breaks the heaven/hell thread of the answer. Read the sidebars against the source, not only for fluency.

---

## 3. Acceptance Criteria

- [x] All 16 files `status: reviewed`.
- [x] `just check` clean.
- [x] Emptiness, "don't know" mind, dualistic thinking, attachment, karma and rebirth are **settled** in spec 002 and used identically across the part.
