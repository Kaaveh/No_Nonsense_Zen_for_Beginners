# Specs Roadmap — No-Nonsense Zen for Beginners (Persian)

Roadmap for translating Jason Quinn's *No-Nonsense Zen for Beginners: Clear Answers to Burning Questions About Core Zen Teachings* (Rockridge Press, 2021) into Persian.

Shared context, pipeline and constraints: [`000-overview.md`](./000-overview.md).

## Status Table

| #   | Spec                                                          | Depends on | Status      |
|-----|---------------------------------------------------------------|------------|-------------|
| 000 | [Overview & Shared Context](./000-overview.md)                | —          | ✅ Done     |
| 001 | [Tooling & Apparatus](./001-tooling.md)                       | 000        | ✅ Done     |
| 002 | [Style & Terminology](./002-style-and-terminology.md)         | 000        | 🟡 Pilot-gated |
| 003 | [Part One: Origins and History](./003-part-one.md) (+ pilot)  | 001, 002   | ✅ Done     |
| 004 | [Part Two: Core Concepts](./004-part-two.md)                  | 003        | ✅ Done     |
| 005 | [Part Three: Core Teachings](./005-part-three.md)             | 003        | ✅ Done     |
| 006 | [Part Four: Core Practices](./006-part-four.md)               | 003        | ✅ Done     |
| 007 | [Front & Back Matter](./007-front-and-back-matter.md)         | 003–006    | ✅ Done     |
| 008 | [Quarto & Publication](./008-quarto-and-publication.md)       | 007        | ⬜ Todo     |

## Recommended Execution Order

```
001 → 002 → 003 pilot (part-1, 1-01…1-05) → 003 rest → 004 → 005 → 006 → 007 → 008
tools style        pilot                       body                     front/back  ship
```

- **001 first.** Images, the `**EVERYDAY ZEN**` label, sidebar headings and italic terms do not survive machine translation. The strip/restore adapter has to work before any file is translated.
- **002 next, but only the decisions the pilot needs.** Register and the first dozen terms. The rest is settled when the text forces a choice (see 002 §0).
- **Pilot on Part One's first five questions.** They cover Zen vs. Buddhism, history, the first sidebar story (1-04) and a dense run of proper names (1-05). If the pilot reads well, scale.
- **Front and back matter last.** The Introduction reuses vocabulary from the whole book; Resources and References are mostly bibliographic and need a policy, not a translation.

## Corpus Scale

| Group                 | Files | Characters (EN) | Sidebars | Contents |
|-----------------------|------:|----------------:|---------:|----------|
| Front matter          |     2 |           7,121 |        — | Title/copyright/dedication, Introduction |
| Part openers          |     4 |           1,592 |        — | Part title + "What You'll Learn" |
| Part One (1-01…1-15)  |    15 |          40,908 |        3 | Origins and history |
| Part Two (2-01…2-15)  |    15 |          41,107 |        3 | Core concepts |
| Part Three (3-01…3-15)|    15 |          41,279 |        3 | Core teachings |
| Part Four (4-01…4-15) |    15 |          40,816 |        3 | Core practices (+ meditation how-to) |
| Back matter           |     4 |           4,285 |        — | Resources, References, Acknowledgments, About the Author |
| **Total**             | **70**|     **177,108** |   **12** | |

Largest single file is under 5,000 characters, so every file is one gTranslator chunk: no seams.

## Definition of Done (every spec)

- [ ] Every item in the spec's **Acceptance Criteria** is checked and true.
- [ ] Files translated one at a time through gTranslator (`-w --raw`) wrapped in the strip/restore apparatus.
- [ ] `just check` clean: parity, orthography, one sentence per line.
- [ ] Terms match [`002-style-and-terminology.md`](./002-style-and-terminology.md); any new decision recorded there first.
- [ ] `status: reviewed` in the front matter of every finished `fa/` file.
