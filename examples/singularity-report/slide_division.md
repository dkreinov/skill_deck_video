# Slide division — "Are we approaching the technological singularity?"

13 slides. Narrated report video, ~15 minutes, technically curious general audience.
As-of date 2026-08-12, forecast horizon 2035. **Visual register: evocative.**

Supersedes `slide_division_paper.md`, `slide_division_editorial.md` and
`slide_division_evocative.md` (the 2026-08-13 register comparison). Slide titles, order,
Data fields, per-slide source IDs and the four DATA CHART slides are unchanged from that
comparison; only the Global visual direction block and the Visual paragraphs are rewritten,
against the updated `references/visual-style.md`.

**Global visual direction:** Speculative documentary — the visual language of a serious
documentary about a contested future, where the camera is shown both the promised future and
the actual machinery, and the distance between them is the story. Background is a flat
near-black `#07090C` on every slide, edge to edge. Type and primary marks are pale `#DCE3EA`;
secondary marks, rules, axes and captions are cool grey `#79838F`. There is exactly ONE
accent, sodium amber `#E8A33D`, and it carries a fixed meaning for the whole deck: **the
amber element is the single measured thing that decides the slide's claim.** Inside a
photograph, amber appears only as real light — a lamp, a screen, a sodium fitting — never as
an overlay. Never accent two things on one slide and never introduce another colour.
Typography: a large light grotesque sans for assertions, small monospace for labels, figures,
axis text and captions.

Most slides carry a picture, and every picture comes from this subject's own world. Pictures
are of exactly two kinds, and the deck's argument lives in the difference between them:

- **REAL** — ordinary machinery photographed straight and unglamorously: machine-room
  aisles, substation yards, instrument racks, paper on a desk. One light source, deep
  shadow, no styling.
- **IMAGINED** — the singularity as popular culture pictures it: colossal luminous
  structures, chrome, ascending light, scale beyond architecture. This is permitted **only
  as the exhibit under discussion**, never as background decoration.

Where both appear on one slide they are divided by a hard edge and left to speak for
themselves; the composition carries the contrast, not a caption. No text is rendered inside
artwork at all.

Bans. Banned everywhere as decoration, and admissible **only where the
imagined future is itself the exhibit**: humanoid robots, glowing brains,
holograms, neon "digital future" cityscapes. Banned outright on every slide, with no
exception: gradients used as decoration, lens flares, bokeh sparkle, isometric 3D clip-art,
decorative frames or borders, blueprint or HUD overlays, digital rain, padlocks, light
bulbs, gears, rockets, puzzle pieces, robot–human handshakes, stock-photo people, faces or
hands, company logos or recognisable brands, and any word or number rendered inside
artwork. Reference only concepts explicitly present in the
sources. Keep this style identical across all slides.

Visual categories: **PICTURE** (a photograph or render from the subject's world),
**DIAGRAM** (flow/structure), **DATA CHART** (quantitative — rendered deterministically from
`charts/*.csv`; the existing renders in `charts/out_evocative/` are reused unchanged and
already draw their background, neutral and accent from this same style block),
**TYPOGRAPHY** (the slide is the words).

Deck rhythm: picture → diagram → picture → chart → picture → chart → chart → picture →
picture → chart → picture → picture → typography. No three consecutive slides share a
category, and only slide 13 is text-only. **Slide 1 is the showpiece.** The imagined/real
contrast is stated three times, escalating: the cold open is the dream (slide 1), slide 5
splits the frame between dream and thing, slide 9 puts the dream under the FRAMING ONLY
banner, and slide 12 answers slide 1 with the thing itself.

Slides 4, 6, 7 and 10 are DATA CHART slides; their generated images are **replaced** after
capture with the unchanged renders in `charts/out_evocative/`.

---

## Slide 1 — Are we approaching the technological singularity?
**Sources:** S14, S13
**Data:**
- Title: Are we approaching the technological singularity?
- Subtitle: A calibrated status as of 12 August 2026
- One line: "The honest answer depends entirely on which of five questions you are asking."
**Visual:** **PICTURE — showpiece.** Full-bleed IMAGINED. The singularity as popular culture
pictures it: a colossal luminous structure climbing out of a dark plain, far taller than any
real building, seen from ground level so it exceeds the frame. This is the picture already in the
audience's head; the deck exists to test it.

## Slide 2 — Five different questions wearing one word
**Sources:** S14, S13
**Data:**
- Key message: "Singularity", "AGI" and "superintelligence" are not synonyms.
- Five separated items: 1. Rapid capability improvement · 2. AI automating AI R&D ·
  3. Recursive self-improvement · 4. Economic growth discontinuity ·
  5. Social/institutional discontinuity
- Bottom line: AGI and superintelligence name a *level*. The singularity names a *rate*.
**Visual:** **DIAGRAM.** One word at the left splitting into five thin horizontal rules that
fan rightward across the dark field to five numbered rows. The third rule, recursive
self-improvement, is amber and slightly heavier — it is the one the singularity claim
actually depends on. Hairlines only, no boxes.

## Slide 3 — What we can actually measure
**Sources:** S56, S23, S64, S01, S15, S43
**Data:**
- Key message: Six instruments carry real signal in 2026.
- Task horizon (METR) · Benchmark-to-practice gap · AI share of engineering work ·
  Algorithmic efficiency · Macro productivity · Physical power delivery
- Caption: None of these six measures the loop itself — that measurement comes later.
**Visual:** **PICTURE — REAL.** A rack holding exactly six analogue measuring instruments in
a dark equipment room, a single raking light across their faces, and beside them a seventh
bay standing empty and unlit. Six instruments, no more. The empty bay is the loop measurement
we do not have. Unbranded, dial faces unreadable.

## Slide 4 — The capability clock is speeding up
**Sources:** S56
**Data:** (from `charts/task_horizon_doubling.csv`)
- 50%-success task-horizon doubling time: 196.5 days (2019–2025 baseline) · 130.8 days
  (post-2023 cohort) · 88.6 days (post-2024 cohort)
- Caveat on slide: METR Time Horizon 1.1, 228 tasks; cohort splits are post-hoc.
- Caveat on slide: this is the rate of *capability* progress, not the rate of AI R&D.
**Visual:** **DATA CHART.** Three horizontal bars, longest at the top, shortening downward;
the shortest bar amber because the shrinking interval is the claim. Value axis starts at
zero, bars direct-labelled, no legend.

## Slide 5 — The loop is partly closed
**Sources:** S64, S66, S67, S74, S75, S92
**Data:**
- Key message: AI now writes a large share of the software that builds AI.
- Anthropic: >80% of merged code authored by Claude (May 2026); Google: 75% of new code
  AI-generated (2026) — both self-reported
- Kernel optimisation loop: 2.8x geometric-mean speedup on vLLM operators
- Flag: interested sources; the metric does not separate boilerplate from core
  training-loop code
**Visual:** **PICTURE — split frame, the deck's central contrast.** A hard vertical edge down
the middle. Left, the imagined: a gleaming machine assembling a copy of itself in blank
white light. Right, the real: an ordinary machine-room aisle at night, one service lamp, a
wall screen of unreadable queued rows. The seam is the argument.

## Slide 6 — Ask for reliability and the horizon collapses
**Sources:** S89
**Data:** (from `charts/reliability_gap.csv`)
- Public frontier models: ~12 h at 50% success, ~1.5 h at 80% success
- Internal frontier configurations: 16–20 h at 50%, 3–4 h at 80% (floors)
- Caption: unattended R&D needs the 80% bar, not the 50% bar.
- Source note: METR Frontier Risk Report (Feb–Mar 2026), published 2026-05-19.
**Visual:** **DATA CHART.** Two pairs of vertical bars, one pair per configuration. The
50%-success bars are neutral grey; both 80%-success bars are amber, because the strict bar
is the one that governs unattended work. Zero-based axis, direct-labelled, no legend.

## Slide 7 — The benchmark and the maintainer disagree
**Sources:** S23, S03, S04
**Data:** (from `charts/benchmark_vs_reality.csv`)
- Automated grader on SWE-bench Verified: 79.4%
- Human maintainer merge rate on 296 AI-generated PRs that passed that grader: 39.7%
- SWE-bench Pro, held-out commercial repositories: 23.0%
- On-slide warning: three different graders, three different denominators — not a decline
  over time.
**Visual:** **DATA CHART.** Three horizontal bars, each carrying its own denominator as a
small caption. Only the human-maintainer bar is amber — it is the measurement that
contradicts the benchmark. Zero-based axis, direct-labelled, no legend.

## Slide 8 — Autonomous science, and one correction
**Sources:** S08, S76, S96
**Data:**
- ~42% of an autonomous research system's proposed experiments failed outright on code errors
- Median of five citations per generated paper; hallucinated numerical results
- Correction: as of mid-2026 **no paper written solely by an AI has been published in a major
  peer-reviewed journal**
- The March 2026 *Nature* paper is human-authored and describes the system; the one
  AI-generated paper that cleared an ICLR workshop bar was withdrawn before publication
**Visual:** **PICTURE — REAL.** A printed paper under one desk lamp in a dark room, pages
fanned across the pool of light, the top sheet turned face-down and pushed to the edge where
the light gives out. The face-down sheet is the paper that was withdrawn. Unbranded, no
readable text, no hands.

## Slide 9 — Weak signals, and a framing device
**Sources:** S89, S90, S97, S98, S99, S13, S45
**Data:**
- Worth watching, measurable: workflow steps run without a human · automated experiment
  throughput · evaluation-build speed · interval between model generations
- Watch, do not count: insurance pricing of AI capability risk · frontier-lab hiring
  composition — commercial sources with an interest in the narrative
- Header on the lower half, verbatim: **FRAMING ONLY — NOT EVIDENCE**
- Good (1965) assumes frictionless scaling · Vinge (1993) requires a vertical asymptote ·
  Seed-AI/"FOOM" assumes a software-only takeoff
**Visual:** **PICTURE — stacked halves, divided by one full-width amber rule.** Above the
rule, a dim ordinary control room with four lit monitors. Below the rule, a glossy imagined
takeoff — chrome forms and light ascending into white. The rule is the only amber element;
it separates evidence from framing.

## Slide 10 — The forecasters do not agree
**Sources:** S46, S51, S54
**Data:** (from `charts/forecast_disagreement.csv`)
- Superforecasters: 1% probability of transformative AI by 2030, 21% by 2050
- AI domain experts: 9% by 2030, 46% by 2050
- On-slide note: this measures belief, not capability. Elicited 2023.
**Visual:** **DATA CHART.** Two cohorts, two bars each. The by-2030 pair is amber because
the nine-fold gap between one per cent and nine per cent is the message; the by-2050 pair
stays neutral grey. Zero-based axis, direct-labelled, no legend.

## Slide 11 — What is actually blocking it
**Sources:** S13, S83, S84, S85, S45, S43, S15, S49, S79, S78
**Data:**
- Model collapse and contamination: real bounds, but conditional and confounded — ACL 2026
  removed the temporal-decay signal by rewording tasks
- Parallelisation: capped by serial experiment depth and coordination cost
- Power and economics: interconnection takes 36–60 months; US TFP growth at 0.53% — though
  J-curve revisions imply that is not a hard ceiling
**Visual:** **PICTURE — REAL.** A substation yard at dusk behind chain-link, shot from a low
angle so the transformers tower over the fence and recede into haze, a single sodium fitting
the only warm light, a small access gate at the near end for scale. The queue of transformers
is the wait for power. Unbranded, no readable text.

## Slide 12 — The calibrated answer, 12 August 2026
**Sources:** S89, S56, S64, S23, S08, S45
**Data:**
- Observed: capability rate has risen · AI writes much of the labs' code · AI optimises its
  own low-level software
- Not observed: a compounding rise in the rate of AI R&D itself · the cross-lab measurement
  reports not yet 2x · reliable long-horizon autonomy
- Verdict: not measurably inside a singularity; measurably inside a period of unusually fast
  capability growth in which AI does much of AI engineering
- Confidence: moderate — the decisive metric is self-reported by the labs being evaluated
**Visual:** **PICTURE — REAL, answering slide 1.** The same low camera angle and the same
dark plain as the cold open, but the structure on the horizon is an ordinary low windowless
building with cooling plumes rising in still air. Upper frame stays empty for the verdict
type. The two words "not yet" are the only amber.

## Slide 13 — What would change this, and where it came from
**Sources:** S89, S92, S76, S78, S79, S56 — plus full bibliography
**Data:**
- Would change the answer: 80%-bar horizons exceeding a working day · a cross-lab audit
  reporting sustained ≥2x R&D acceleration · externally audited core-code authorship above
  ~20% · AI-authored papers repeatedly clearing full peer review · TFP breaking trend after
  revision
- Method: 3 Deep Research passes · 264 sources imported, none discarded · claim-level
  evidence matrix with locators · 10 claims dropped for unusable locators · charts rendered
  from data files
- Provenance line, verbatim: Web-researched via Gemini Notebook Deep Research on 2026-08-12.
  Not verified against authoritative internal documentation.
- Key sources: [S89] METR Frontier Risk Report · [S56] METR Time Horizon 1.1 · [S23] METR
  SWE-bench PR study · [S64] Anthropic, When AI builds itself · [S01] Epoch AI, Algorithmic
  progress · [S86] Gundlach et al. reanalysis · [S08] NUS AI Scientist evaluation · [S76]
  Pebblous correction · [S45] Epoch AI, Parallelization constraints · [S49] Acemoglu, Simple
  macroeconomics of AI · [S84] Contamination systematic review · [S85] ACL 2026 Test of Time ·
  [S46] Forecasting Research Institute
**Visual:** **TYPOGRAPHY.** End titles on the dark field. A left column of five short trigger
lines, each preceded by a small amber tick; a right column listing each source identifier
with its title in monospace at lower contrast. The provenance line runs full width along the
bottom. No imagery.

---

## NotebookLM run notes

- Sources selected for generation: **only** `notebooklm_source.md` and this file. Every
  other source in the notebook must be **unticked**. Verify before generating — hard gate.
- Studio → Slide Deck → Format **Presenter Slides**, Length **Default**.
- The Global visual direction block above is pasted verbatim into the generation prompt.
- Audit every slide, including any text the generator renders inside artwork — zoom and
  read it. Batch all fixes into as few Revise passes as possible.
- Replace slides 4, 6, 7 and 10 with the unchanged renders in `charts/out_evocative/`.
- Re-exports from NotebookLM re-add the watermark → rerun the watermark cleanup.

## Outline paste prompt

```
Audience: a technically curious general audience watching a narrated research report.
Create exactly 13 slides. Use this outline EXACTLY — same order, same titles, one slide each:
1. Are we approaching the technological singularity?
2. Five different questions wearing one word
3. What we can actually measure
4. The capability clock is speeding up
5. The loop is partly closed
6. Ask for reliability and the horizon collapses
7. The benchmark and the maintainer disagree
8. Autonomous science, and one correction
9. Weak signals, and a framing device
10. The forecasters do not agree
11. What is actually blocking it
12. The calibrated answer, 12 August 2026
13. What would change this, and where it came from
For each slide use the matching "Data" and "Visual" descriptions from the Slide Division
source. Keep text minimal: key message plus a maximum of 3 bullets per slide. Do not invent
any number, percentage, date or source name that does not appear in the sources. Slide 9
must carry the words FRAMING ONLY - NOT EVIDENCE exactly. Slide 13 must list each source ID
with its title.

House style for EVERY slide: Speculative documentary - the visual language of a serious
documentary about a contested future, where the camera is shown both the promised future and
the actual machinery, and the distance between them is the story. Background is a flat
near-black #07090C on every slide, edge to edge. Type and primary marks are pale #DCE3EA;
secondary marks, rules, axes and captions are cool grey #79838F. There is exactly ONE accent,
sodium amber #E8A33D, and it carries a fixed meaning for the whole deck: the amber element is
the single measured thing that decides the slide's claim. Inside a photograph, amber appears
only as real light - a lamp, a screen, a sodium fitting - never as an overlay. Never accent
two things on one slide and never introduce another colour. Typography: a large light
grotesque sans for assertions, small monospace for labels, figures, axis text and captions.

Most slides carry a picture, and every picture comes from this subject's own world. Pictures
are of exactly two kinds, and the deck's argument lives in the difference between them. REAL:
ordinary machinery photographed straight and unglamorously - machine-room aisles, substation
yards, instrument racks, paper on a desk; one light source, deep shadow, no styling. IMAGINED:
the singularity as popular culture pictures it - colossal luminous structures, chrome,
ascending light, scale beyond architecture; this is permitted only as the exhibit under
discussion, never as background decoration. Where both appear on one slide they are divided
by a hard edge and left to speak for themselves; the composition carries the contrast, not a
caption. No text is rendered inside artwork at all.

Bans. Banned everywhere as decoration, and admissible only where the imagined future is
itself the exhibit: humanoid robots, glowing brains, holograms,
neon digital-future cityscapes. Banned outright on every slide with no exception: gradients
used as decoration, lens flares, bokeh sparkle, isometric 3D clip-art, decorative frames or
borders, blueprint or HUD overlays, digital rain, padlocks, light bulbs, gears, rockets,
puzzle pieces, robot-human handshakes, stock-photo people, faces or hands, company logos or
recognisable brands, and any word or number rendered inside artwork or inside
photographs. Reference only concepts explicitly present in the sources. Keep this style
identical across all slides.
```
