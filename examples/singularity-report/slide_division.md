# Slide division — "Are we approaching the technological singularity?"

13 slides. Narrated report video, ~15 minutes, technically curious general audience.
As-of date 2026-08-12, forecast horizon 2035.

**Global visual direction:** Minimal editorial dark — the visual language of a serious
printed science review, not a technology marketing deck. Background is a flat near-black
`#0B0E14` on every slide, edge to edge. Primary marks and headline type are pale grey
`#D7DEE8`; secondary marks, axes and captions are muted slate `#6E7A8A`. There is exactly
ONE accent, amber `#E8A33D`, and it carries a fixed meaning for the whole deck: **the amber
element is the single measured thing that decides the slide's claim.** Never use amber for
decoration, never accent two things on one slide, and never introduce any other colour.
Typography: a large light grotesque sans for assertions, small monospace for labels, figures
and axis text. Rendering: flat matte and vector-like, generous empty space, thin hairline
rules. Bans, standing for every slide: no gradients, no glows, no shadows, no lens flares,
no bokeh, no 3D or isometric clip-art, no frames or border decoration, no blueprint or HUD
overlays, no grid-paper texture, no glowing brains, no circuit-board heads, no humanoid
robots, no handshakes, no padlocks, no light bulbs, no gears, no rockets, no puzzle pieces,
no stock-photo people, no faces or hands, no company logos or recognisable brands, and no
words or numbers rendered inside artwork except where a slide explicitly asks for them.
Reference only concepts explicitly present in the sources. Keep this style identical across
all slides.

Visual categories: **DIAGRAM** (flow/structure), **DATA CHART** (quantitative — rendered
deterministically from `charts/*.csv` by `charts/render_charts.py`, which takes its
background, neutral and accent from this same style block), **TYPOGRAPHY** (the slide is
the words), or illustration.

Deck rhythm: typography → diagram → illustration → chart → diagram → chart → chart →
illustration → diagram → chart → diagram → typography → typography. Slides 5 and 8 are
mirrored compositions (same layout, accent on opposite sides) because they carry the
evidence-for and evidence-against beats. Slides 1 and 12 get the boldest treatment.

Slides 4, 6, 7 and 10 are DATA CHART slides; their generated images are **replaced** after
capture with the local renders in `charts/out/`, so every number on screen comes from a data
file with recorded `source_ids`.

---

## Slide 1 — Are we approaching the technological singularity?
**Sources:** S14, S13
**Data:**
- Title: Are we approaching the technological singularity?
- Subtitle: A calibrated status as of 12 August 2026
- One line: "The honest answer depends entirely on which of five questions you are asking."
**Visual:** **TYPOGRAPHY.** Full-bleed dark field, no imagery at all. The question set very
large in pale grey across the upper two-thirds with enormous margins; the subtitle and the
single line small beneath it. The word "five" is the only amber element on the slide,
marking the count the rest of the deck unpacks.

## Slide 2 — Five different questions wearing one word
**Sources:** S14, S13
**Data:**
- Key message: "Singularity", "AGI" and "superintelligence" are not synonyms.
- Five separated items: 1. Rapid capability improvement · 2. AI automating AI R&D ·
  3. Recursive self-improvement · 4. Economic growth discontinuity ·
  5. Social/institutional discontinuity
- Bottom line: AGI and superintelligence name a *level*. The singularity names a *rate*.
**Visual:** **DIAGRAM.** One pale grey word at the left splitting into five thin horizontal
lines that fan rightward to five stacked rows, top to bottom. The third line, recursive
self-improvement, is amber and slightly thicker — it is the one the singularity claim
actually depends on. No boxes, no icons, hairline rules only.

## Slide 3 — What we can actually measure
**Sources:** S56, S23, S64, S01, S15, S43
**Data:**
- Key message: Six instruments carry real signal in 2026.
- Task horizon (METR) · Benchmark-to-practice gap · AI share of engineering work ·
  Algorithmic efficiency · Macro productivity · Physical power delivery
- Caption: None of these six measures the loop itself — that measurement comes later.
**Visual:** Illustration, abstract geometric. Six identical pale grey tick marks evenly
spaced along a single horizontal hairline, each with its label set beneath in small
monospace. A seventh position at the far right is empty, marked only by an amber outline
with nothing inside it — the loop measurement we do not have here.

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
**Visual:** **DIAGRAM.** Text block on the left, figure on the right. A ring of four
pale grey nodes read clockwise — model, writes code, trains, next model. Three arcs are
solid; the arc returning to "model" is a dashed gap in amber, marking the part of the loop
that is not closed.

## Slide 6 — Ask for reliability and the horizon collapses
**Sources:** S89
**Data:** (from `charts/reliability_gap.csv`)
- Public frontier models: ~12 h at 50% success, ~1.5 h at 80% success
- Internal frontier configurations: 16–20 h at 50%, 3–4 h at 80% (floors)
- Caption: unattended R&D needs the 80% bar, not the 50% bar.
- Source note: METR Frontier Risk Report (Feb–Mar 2026), published 2026-05-19.
**Visual:** **DATA CHART.** Two pairs of vertical bars, one pair per configuration. The
50%-success bars are neutral grey; both 80%-success bars are amber, because the strict bar
is the one that governs unattended work. Zero-based axis, bars direct-labelled, no legend.

## Slide 7 — The benchmark and the maintainer disagree
**Sources:** S23, S03, S04
**Data:** (from `charts/benchmark_vs_reality.csv`)
- Automated grader on SWE-bench Verified: 79.4%
- Human maintainer merge rate on 296 AI-generated PRs that passed that grader: 39.7%
- SWE-bench Pro, held-out commercial repositories: 23.0%
- On-slide warning: three different graders, three different denominators — not a decline
  over time.
**Visual:** **DATA CHART.** Three horizontal bars, each carrying its own denominator as a
small caption. Only the human-maintainer bar is amber — it is the measurement that contradicts
the benchmark. Zero-based axis, direct-labelled, no legend.

## Slide 8 — Autonomous science, and one correction
**Sources:** S08, S76, S96
**Data:**
- ~42% of an autonomous research system's proposed experiments failed outright on code errors
- Median of five citations per generated paper; hallucinated numerical results
- Correction: as of mid-2026 **no paper written solely by an AI has been published in a major
  peer-reviewed journal**
- The March 2026 *Nature* paper is human-authored and describes the system; the one
  AI-generated paper that cleared an ICLR workshop bar was withdrawn before publication
**Visual:** Illustration, mirroring slide 5 with the figure on the left and the text on the
right. A tall stack of thin pale grey horizontal lines standing for a manuscript, seen
straight on; a single amber rule struck through one line near the top marks the claim that
was corrected. No readable words in the artwork.

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
**Visual:** **DIAGRAM.** The slide divided by one full-width amber hairline. Above it, four
short pale grey vertical bars of even height standing for measurable indicators. Below it,
three faint outlined rectangles at lower contrast standing for the three historical models.
The rule is the only amber element; it separates evidence from framing.

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
**Visual:** **DIAGRAM.** One long pale grey horizontal arrow running left to right across
the slide, crossed by five vertical bars of differing heights. Two bars are drawn as faint
outlines because those constraints are contested; the power bar is solid amber and the
tallest, the one constraint nobody disputes. Labels beneath in small monospace.

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
**Visual:** **TYPOGRAPHY.** The deck's boldest slide. Two columns of short pale grey lines
under the words "observed" and "not observed", separated by one hairline rule. The verdict
sits beneath in large light type, with the two words "not yet" in amber — the whole report
turns on them. No imagery.

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
**Visual:** **TYPOGRAPHY.** Purely typographic on the dark field. A left column of five short
trigger lines, each preceded by a small amber tick; a right column of source identifiers set
small in monospace at lower contrast. The provenance line runs full width along the bottom.
No imagery.

---

## NotebookLM run notes

- Sources selected for generation: **only** `notebooklm_source.md` and `slide_division.md`.
  All research sources, Deep Research reports and saved notes must be **deselected**.
  Verify the checkboxes before generating — hard gate.
- Studio → Slide Deck → Format **Presenter Slides**, Length **Default**.
- The Global visual direction block above is pasted verbatim into the generation prompt —
  that is the only place deck style can be set.
- After generation: audit every slide against `notebooklm_source.md` (no-unsourced-numbers
  rule), batch all fixes into as few Revise passes as possible, re-check untouched slides,
  then capture at native resolution.
- Replace slides 4, 6, 7 and 10 with `charts/out/*.png` before building the PPTX and video.
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
must carry the words FRAMING ONLY - NOT EVIDENCE exactly. Slide 13 must list the source IDs
given.

House style for EVERY slide: Minimal editorial dark — the visual language of a serious
printed science review, not a technology marketing deck. Background is a flat near-black
#0B0E14 on every slide, edge to edge. Primary marks and headline type are pale grey #D7DEE8;
secondary marks, axes and captions are muted slate #6E7A8A. There is exactly ONE accent,
amber #E8A33D, and it carries a fixed meaning for the whole deck: the amber element is the
single measured thing that decides the slide's claim. Never use amber for decoration, never
accent two things on one slide, and never introduce any other colour. Typography: a large
light grotesque sans for assertions, small monospace for labels, figures and axis text.
Rendering: flat matte and vector-like, generous empty space, thin hairline rules. Bans,
standing for every slide: no gradients, no glows, no shadows, no lens flares, no bokeh, no 3D
or isometric clip-art, no frames or border decoration, no blueprint or HUD overlays, no
grid-paper texture, no glowing brains, no circuit-board heads, no humanoid robots, no
handshakes, no padlocks, no light bulbs, no gears, no rockets, no puzzle pieces, no
stock-photo people, no faces or hands, no company logos or recognisable brands, and no words
or numbers rendered inside artwork except where a slide explicitly asks for them. Reference
only concepts explicitly present in the sources. Keep this style identical across all slides.
```
