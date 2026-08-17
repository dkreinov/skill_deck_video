# Fact Gate review — "Karpathy Frontier Signals"

Deck generated in Gemini Notebook (NotebookLM) from `notebooklm_source.md` +
`slide_division.md`, Presenter Slides format, 16 slides.

Every slide was rendered and read at full size. Each on-slide number was checked
digit-for-digit against `notebooklm_source.md`, which in turn quotes
`raw_tweets.md` verbatim.

## Round 1 verdict

| # | Slide | Claims checked | Verdict |
|---|---|---|---|
| 1 | Title | 28 posts; 12 May – 12 Aug 2026 | PASS |
| 2 | The window at a glance | 149,750 likes; 8,140,553 views; 28 posts | PASS |
| 3 | "I've joined Anthropic" | 149,750; 27,909,958; "3x the likes" | **FAIL — misquote** |
| 4 | Stuck on step 1 | 1,992; 218,965; "8XH100"; "step 1" | PASS |
| 5 | Fable 5: benchmarks vs. feel | 25,645; 3,044,871; "trigger happy"; "don't do this in prod!" | PASS |
| 6 | Jevons paradox for software | wandb example; 10X test suites | PASS |
| 7 | The third redesign of LLM UI/UX | 23,317; 8,140,553; paradigm order 1→2→3 | PASS |
| 8 | "I work from Slack now" | 1,657; 476,414; "everyone is a manager" | PASS |
| 9 | The opposite regime | 1,725; 105,899; voltage/current polarity | PASS |
| 10 | The long ramble session | 49,332; 4,054,610 | **FAIL — design + clipping** |
| 11 | Laggy self-awareness | 998; 84,675; /compact | PASS |
| 12 | Off the clock | 4,159; 22,226; 672 | PASS |
| 13 | A rumor, twice denied | 01:43 & 01:51 UTC; both replies | PASS |
| 14 | Retiring the pelican | 1M tokens (~$10); Opus 5; 5,500 lines; ~2 hours; three.js | PASS |
| 15 | It cannot watch its own work | reads as a limitation, not a success | PASS |
| 16 | Where it points | 915; 74,171 | PASS |

### Defects found

**D1 — Slide 3, misquote (Fact Gate violation).**
The verbatim quotation rendered "I remain deeply **psionate** about education".
The word is "passionate". Misquoting a named person is the exact failure the
Fact Gate exists to catch.
→ Revision round 1. **FIXED** — now reads "deeply passionate".

**D2 — Slide 10, background.** The slide rendered on a white/light background
while all 15 others are near-black. Breaks the deck's visual system.
→ Revision round 1. **FIXED** — now near-black with the orange accent.

**D3 — Slide 10, quote clipped.** The pull quote overflowed the right edge,
cut mid-word at "In these cases I lik". Text loss on a direct quotation.
→ Revision round 1: not fixed. Revision round 2 with explicit font-size and
   text-block-width constraints.

### Checks that specifically passed

These were on the pre-registered watch list in `slide_division.md` because
generators commonly break them:

- **No invented statistics.** No rounded "150K", no fabricated percentages, no
  invented speedups anywhere in 16 slides.
- **The four fragile numbers on slide 14** — 1M token budget, ~$10, 5,500 lines,
  ~2 hours — all correct and correctly paired.
- **Model names exact**: Opus 5, Claude Fable 5, Mythos, Claude 4.5.
- **Paradigm order not scrambled**: website → downloaded app → persistent
  asynchronous entity.
- **Voltage contrast not inverted** (slide 9): transmission = high voltage / low
  current / great distances; inference silicon = low voltage / high current /
  tiny distances.
- **Slide 15 reads as a limitation.** The broken feedback ring makes the missing
  audit loop the subject of the image; it does not read as a success story.
- **No third-party brand marks**, including on slide 8, which is about Slack.
- **No copyrighted characters or creatures** on slide 14 — generic low-poly
  terrain only.
- **No text rendered inside illustrations** except the step numerals on slide 4
  and deliberately illegible glyph texture on slides 11 and 12, both intended.

## Known limitation

Engagement figures are a snapshot taken 12 August 2026. They rise continuously.
Anyone re-checking these slides against live X will find higher numbers; that is
drift, not error. `raw_tweets.md` records the capture-time values.
