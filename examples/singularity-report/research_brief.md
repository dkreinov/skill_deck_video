# Research brief — Are we approaching the technological singularity?

Run: `singularity_report` · As-of date: **2026-08-12** · Forecast horizon: **through 2035**
Deliverable: narrated report video, ~15 minutes, technically curious general audience.

## Central question

Is there measurable evidence that artificial-intelligence development is becoming
self-accelerating, and does any such evidence bear on the claim that a
"technological singularity" is approaching?

The report maps the evidence without choosing a side in advance (epistemic
posture selected at intake: *map the evidence, pick no side*). It must end in a
calibrated status as of 2026-08-12 — not a cinematic yes or no.

## Definitions

The report must keep the following five phenomena strictly separate and must
never treat "singularity", "AGI", and "superintelligence" as synonyms.

1. **Rapid general capability improvement** — AI systems get better across many
   tasks quickly. Measurable via benchmark scores, task-horizon length,
   reliability at long autonomous tasks. This is the weakest claim and the one
   with the most data.
2. **AI automation of AI research and engineering (AI-in-the-loop R&D)** — AI
   systems performing a material share of the work that produces the next AI
   system: writing code, running experiments, designing evaluations, tuning
   hardware. Measurable via the share of R&D workflows executed by AI, PR/commit
   share, experiment throughput.
3. **Recursive self-improvement (RSI)** — a closed loop where each generation of
   AI materially shortens the time or cost to produce a more capable successor,
   with the loop gain sustained rather than damped. This is the technical core of
   the classical singularity argument. Measurable in principle via the trend in
   time-and-cost per capability doubling.
4. **Economic growth discontinuity** — a break in aggregate output, productivity,
   or growth-rate trend attributable to AI. Measurable via TFP, GDP, labour
   productivity, sectoral output.
5. **Social or institutional discontinuity** — a break in the ability of human
   institutions to observe, predict, or govern the technology. Largely not
   directly measurable; treated as inference and scenario, never as observation.

Also defined for precision: **AGI** (a system matching competent human
performance across most economically valuable cognitive work), **superintelligence**
(a system substantially exceeding the best human performance across essentially
all cognitive domains), and **takeoff speed** (the wall-clock time between those
two states). Note explicitly that the classical "singularity" is a claim about
*rate*, not about *level*.

## Hypotheses

**Initial hypothesis (H1):** Some feedback loops between AI capability and AI
production are already measurable, but their existence is not equivalent to a
singularity; the loop may be real and still be damped, bottlenecked, or slow.

**Alternative hypotheses:**

- **H2 — Ordinary fast technology:** progress is rapid but follows the same
  S-curve/diffusion pattern as prior general-purpose technologies; no
  discontinuity in rate.
- **H3 — Measurement artefact:** apparent acceleration is largely benchmark
  saturation, contamination, selective reporting, and metric choice, and shrinks
  under independent evaluation.
- **H4 — Bottleneck-dominated:** the capability loop is real but rate-limited by
  compute, energy, capital, data, hardware supply chains, or organisational
  absorption, so the observable rate stays bounded.
- **H5 — Approaching discontinuity:** at least one measurable quantity (task
  horizon, AI share of AI R&D, cost per capability unit) is on a
  super-exponential path that, extrapolated, breaks trend inside the horizon.

## Evidence that would support

- Sustained shortening of the interval between capability generations, measured
  in wall-clock time at constant or falling cost.
- A rising, independently measured share of frontier AI R&D work performed by AI
  systems, with a demonstrated causal link to shortened cycle time.
- Task horizon (length of task an AI completes autonomously at a fixed success
  rate) growing faster than exponential over multiple years, under an unchanged
  methodology.
- Algorithmic efficiency gains that themselves accelerate — i.e. the rate of
  cost-per-capability decline increasing rather than holding constant.
- Productivity or TFP statistics breaking their post-1970s trend in ways
  attributable to AI diffusion.
- Automated experiment throughput or AI-authored scientific results rising
  steeply with independent verification of quality.

## Evidence that would weaken or falsify

- Benchmark gains driven by contamination, saturation, or evaluator choice, and
  shrinking under held-out or independent evaluation.
- Weak transfer from benchmark scores to reliable long-horizon autonomy; error
  rates compounding over multi-step tasks.
- Compute, energy, capital, fab capacity, or data limits that bound the loop
  regardless of algorithmic progress.
- Deployment and diffusion friction: measured enterprise adoption failing to
  convert into measured output.
- The historical record of confidently wrong AI timeline forecasts, and of
  general-purpose technologies whose measured productivity effects arrived
  decades late.
- Constant-rate rather than increasing-rate improvement: an exponential is not a
  singularity.

## Research axes

1. AI task horizon, autonomy, and long-run reliability.
2. AI contribution to AI research: model research, coding, evaluation design,
   chip design, and scientific discovery.
3. Algorithmic efficiency, training cost, and inference cost trends.
4. Compute, energy, data, hardware, and infrastructure constraints.
5. Direct evidence of recursive feedback and of change in the *rate* of progress.
6. Deployment, economic diffusion, productivity, and institutional adaptation.
7. Forecasts, prediction markets, expert disagreement, and the accuracy record of
   past AI predictions.
8. Non-obvious indicators: AI-authored research share, automated experiment
   throughput, evaluation-development speed, lab cycle-time compression, share of
   AI R&D workflow performed by AI, and compute-to-capability elasticity.

Axes are research hypotheses, not findings. An axis survives into the deck only
if it is measurable and sourced.

## Source-quality policy

- Prefer primary sources: papers, datasets, benchmark repositories, system
  cards, official technical reports, statistical-agency data.
- A lab's own benchmark is evidence of *what the lab reported*, not independent
  proof of the general claim. Label such sources `interested`.
- Seek at least two independent sources for any consequential synthesized claim.
- Never compare metrics across incompatible benchmark versions, datasets,
  evaluators, or settings.
- Preserve disagreements and ranges; do not average them into false certainty.
- Timestamp every current-state claim and every forecast.
- Every central claim needs an `evidence_matrix.md` row with a non-empty
  Locator before it may enter `notebooklm_source.md`.

## Scope and dates

- **As-of date:** 2026-08-12. All current-state claims are stated as of this date.
- **Forecast horizon:** through 2035.
- **In scope:** measurable indicators of AI self-acceleration; the five
  operational definitions above; the strongest skeptical counter-case; weak
  signals; scenario ranges through 2035.
- **Out of scope by default:** non-public networks or dark-web sources; anything
  requiring paywall circumvention; internal or proprietary company data.

## Editorial approach and audience

- **Audience:** technically curious general audience — comfortable with a chart
  and a rate-versus-level distinction, not specialists.
- **Approach (selected at intake):** rigorous scientific evidence review as the
  backbone; pop-science narration layered on top; a dedicated non-obvious
  weak-signals section; science-fiction framing used *only* to introduce mental
  models, explicitly labelled as fiction wherever it appears.
- **Desired takeaway:** the viewer should leave able to say which specific claim
  the evidence supports, which it does not, and what observable event would
  change the answer.
- **Style never lowers the evidence bar.** Simplification happens after the Fact
  Gate, and simplified language must still carry the uncertainty.

## Excluded topics

- Consciousness, sentience, machine subjective experience.
- AI existential-risk advocacy or policy prescription (mentioned only where it
  is itself the measured object, e.g. as a forecast dataset).
- Company-by-company competitive commentary and stock/market predictions.
- Science-fiction plot summary as a substitute for evidence.
- Dark-web or non-public sources.

## Expected output structure

Twelve-beat report-video structure:

1. Cold open: the central question.
2. Definition: what would actually count as the phenomenon (the five senses).
3. Measurement dashboard: what we can actually measure.
4. Strongest evidence for self-acceleration.
5. Strongest evidence against.
6. Non-obvious indicators (weak signals) + the science-fiction frame, labelled.
7. Bottlenecks and alternative explanations.
8. Scenarios and forecast ranges through 2035.
9. Calibrated answer as of 2026-08-12.
10. What would change the conclusion.
11. What to monitor next.
12. Methodology, provenance disclosure, and sources.
