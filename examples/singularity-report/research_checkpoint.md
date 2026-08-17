# Research checkpoint

Written 2026-08-12, after synthesis, in place of an editorial pause (the intake authorised
automatic continuation).

## Emerging answer

As of 2026-08-12 the evidence supports a split verdict, not a yes or no. **Sense 1** (rapid
general capability improvement) is established, and the *rate* has measurably risen: METR's
50%-success task-horizon doubling time falls from 196.5 days (2019–2025) to 88.6 days for the
post-2024 cohort [S56]. **Sense 2** (AI automating AI engineering) is substantially true but
measured only by interested parties [S64, S66, S67, S92]. **Sense 3** (recursive self-improvement
with sustained loop gain), **sense 4** (economic discontinuity) and **sense 5** (institutional
discontinuity) are not supported.

The decisive datum is METR's cross-lab pilot: task-completion duration has been doubling roughly
every four months since 2024, yet developer audits report that overall R&D velocity has **not
yet** reached a 2x compounding acceleration [S89]. That is the loop-gain measurement the
classical singularity argument requires, and it currently reads negative.

Verdict for the video: *not measurably inside a singularity; measurably inside a period of
unusually fast capability growth in which AI performs much of AI engineering.* Confidence:
moderate.

## Strongest supporting evidence

1. **Task-horizon doubling compression** — 196.5 → 130.8 → 88.6 days by cohort, METR TH1.1,
   228 tasks [S56]. A change in rate, which is the right kind of quantity.
2. **Opus 4.6 at a 719-minute (~12 h) 50%-success horizon** in early 2026 [S56].
3. **AI authorship of frontier-lab code** — Anthropic >80% of merged code (May 2026, from low
   single digits in early 2025), 8x lines/engineer-day [S64]; Google 75% in 2026 from 25% in
   2024 [S66]; OpenAI ~80% [S67].
4. **AI optimising its own substrate** — 2.8x geometric-mean kernel speedup on vLLM operators
   [S74]; 31.6% → 47.8% of KernelBench tasks improved ≥1.2x with multi-turn search [S75].
5. **Latent-capability index acceleration** — ECI growth 8.3 → 15.5 points/year after April 2024
   [S90].
6. **The skeptical theory is weaker than advertised** — model collapse is conditional on
   vanishing exogenous data and does not describe frontier training [S83]; the headline
   contamination signal (post-cutoff decay) is confounded by benchmark construction [S85].

## Strongest counter-evidence

1. **The loop-gain measurement is negative** — no 2x compounding R&D acceleration reported by
   developer audits [S89].
2. **Reliability collapse** — public models: ~12 h at 50% success but ~1.5 h at 80%; internal:
   16–20 h vs 3–4 h [S89]. GPT-5 at ~2 h 17 min against METR's >40 h threshold of concern [S26].
3. **Benchmarks overstate practice** — 79.4% automated grader vs ~39.7% maintainer merge rate on
   296 PRs; SWE-bench Pro ~23% [S23, S03].
4. **Autonomous research is unreliable** — ~42% experiment failure, keyword-level literature
   review, hallucinated numbers [S08]; and no AI-only paper has been published in a major
   peer-reviewed journal as of mid-2026 [S76, S96].
5. **Progress is mostly bought, not invented** — 60–95% of historical performance gains
   attributable to compute and data scaling [S01]; efficiency-rate estimates span ~2x to ~6x per
   year and one reanalysis calls the canonical curve a reference-dependence artefact [S86].
6. **Physical and economic bounds** — time-to-power 1.5–2 years longer than assumed,
   interconnection 36–60 months [S43, S81]; parallelisation ceiling with an explicit "prevented
   explosion" trajectory [S45]; rolling 20-yr TFP at 0.53% and a modelled ≤0.66%/decade AI
   contribution [S15, S49].

## Independent evidence review

**Deviation recorded.** The skill prescribes a fresh-context subagent for this review. This
session carries a standing instruction not to use the Agent tool unless the user requests it, so
the adversarial review was conducted in-session against the preserved pass reports, registry and
matrix rather than by a separate agent. This is weaker on the "different eyes" dimension and is
disclosed here rather than glossed. Findings and resolutions:

| Finding | Resolution |
|---|---|
| Pass A attributed METR's Opus 4.6 task-horizon numbers to `[cite: 20]`, which resolves to an AI-2027 prediction tracker (S20) — a source that cannot ground a METR measurement. | Claim re-grounded on S56 and S89 (METR's own publications) via Pass B/C. Recorded as C33. |
| Pass A attributed the "Codex collaborators 2% → 8%" figure and the July 2026 Project Glasswing CVE figure to `[cite: 7]`, which resolves to Epoch AI's rolling "Latest" index page (S07). | Both claims **omitted**. No alternative locator found. |
| Pass A attributed "zero capability improvement across 30 EBR-bench playthroughs" to `[cite: 12]` (an Epoch hub page). | Claim **omitted** despite being rhetorically attractive. |
| Pass A repeated the vendor framing that an AI-generated paper was "published in Nature". | **Contradicted** by Pass B: the Nature paper is human-authored and describes the system; the workshop paper was withdrawn. The correction (C13) is now a slide of its own. |
| Task-horizon acceleration was initially treated as evidence of self-acceleration. | **Qualified.** It measures the rate of capability progress, not the rate of R&D. The chart carries this caveat on its face. |
| Lab code-share figures were initially read as measurements. | **Reclassified** as `interpretation` from `interested` sources, with the boilerplate-split counter-reading (S92) given equal on-slide weight. |
| Four algorithmic-efficiency estimates were initially going to be plotted together. | **Qualified**: they are not the same metric measured the same way, and the MIRI 60x figure measures catch-up progress, so it was excluded from any comparison entirely. |
| Several vivid numbers (Copilot 55.8% faster; 14% more issues/hour; 25% degradation on jagged-frontier tasks; global AI code share 6/19/42/55%; 68.3% SWE-bench sample filtering; Brier-score improvements) reached us only through blogs citing unread primaries. | All **omitted**. Listed in the matrix's omitted-claims table. |

## Unresolved gaps

- **The decisive metric is self-reported.** "R&D velocity" [S89] is not a standardised quantity
  and comes from the labs being evaluated. No independent audit exists.
- **No externally audited figure for core-code authorship** — only the boilerplate-inclusive
  self-reports [S64] and a community sanity check [S92].
- **Secondary-sourced physical numbers.** The LBNL and IEA electricity figures and the PJM
  interconnection ranges reach us via aggregator pages (S81), not the originating bodies.
- **The 15.9% intangibles TFP adjustment** [S79] is carried by a university news item, not the
  primary J-curve literature. Used with an explicit hedge.
- **Pass D (gap closure) was not run.** The gaps above are all *source-tracing* gaps —
  retrieving primary PDFs already identified — not discovery gaps that another Deep Research
  sweep would close. Each is disclosed on the relevant slide or in the matrix caveats instead.
  Recorded as a deliberate omission, not an oversight.

## Omitted claims

See the "Omitted claims (insufficient or unusable support)" table in `evidence_matrix.md` —
ten claims dropped, each with its reason. Summary of reasons: three for citation markers
resolving to sources that cannot ground them; five for reaching us only through blogs citing
unread primaries; one rhetorical illustration; one untraceable extreme forecast.

## Go/no-go

**Go.** Every central claim carries an evidence-matrix row with a non-empty locator;
`scripts/validate_evidence.py` runs error- and warning-free; the strongest counter-case is
represented at equal weight to the supporting case; six substantive contradictions are preserved
rather than averaged; and the conclusion is stated as a dated, falsifiable, calibrated status
rather than a verdict. The evidence supports continuing to the deck.
