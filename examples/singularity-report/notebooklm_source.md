# Are we approaching the technological singularity? A calibrated status as of 12 August 2026

**Provenance disclosure.** Everything in this document was researched on the public web via
Gemini Notebook (formerly NotebookLM) Deep Research on 2026-08-12, across three passes
(landscape, adversarial, weak signals), and has **not** been verified against authoritative
internal or proprietary documentation. Every central claim carries a compact source ID that
resolves in `source_registry.md`, and every claim has a row in `evidence_matrix.md` with an
exact locator. Claims whose locators did not survive checking were removed — they are listed
in the "Omitted claims" table of the evidence matrix.

---

## 1. Why this question is usually asked badly

"Are we approaching the singularity?" is not one question. It is at least five, and they have
different answers, different evidence, and different measuring instruments. Public discussion
routinely fuses them, and once fused the question becomes unanswerable [S14, S13].

The five must be kept apart [S14, S13]:

1. **Rapid general capability improvement** — models get better across many tasks, quickly.
2. **AI automation of AI research and engineering** — AI systems doing a material share of the
   work that produces the next AI system.
3. **Recursive self-improvement** — a closed loop where each generation shortens the time or
   cost of producing a more capable successor, with the loop gain sustained rather than damped.
4. **Economic growth discontinuity** — a break in the trend of output or productivity.
5. **Social or institutional discontinuity** — a break in our ability to observe, predict or
   govern the technology.

Two further distinctions matter. **AGI** names a capability level — roughly, matching competent
human performance across most economically valuable cognitive work. **Superintelligence** names
a higher level. The **singularity** is not a level at all: it is a claim about a *rate*, the
claim that the rate of improvement itself climbs without bound [S14]. A system can be
extraordinarily capable and the rate can still be constant. An exponential is not a singularity.

That distinction decides what evidence counts. To test the singularity claim you must measure
whether the *rate* of progress is rising — not whether capability is high.

## 2. What we can actually measure

Six instruments carry real signal as of August 2026.

- **Task horizon.** METR measures the length of task, calibrated in human-expert time, that an
  agent completes autonomously at a stated success probability, fitted with an
  item-response-theory logistic across a task suite [S56, S55].
- **Benchmark-to-practice gap.** The difference between what an automated grader scores and
  what a human repository maintainer accepts [S23].
- **AI share of engineering work.** The proportion of code, pull requests and experiments at
  frontier labs produced by AI — self-reported [S64, S66, S67].
- **Algorithmic efficiency.** The training compute needed to reach a fixed capability, over
  time [S01, S86, S87].
- **Macro statistics.** Total factor productivity and firm-level productivity [S15, S49, S80].
- **Physical delivery.** Time-to-power, interconnection queues, grid capacity [S43, S44, S81].

There is also a measurement of the *loop itself*, and it is the single most decision-relevant
number in this report — see section 5.

## 3. The evidence that something real is accelerating

**Task horizons are doubling faster.** On METR's Time Horizon 1.1 suite (228 tasks, released
2026-01-29), the 50%-success task horizon doubled roughly every **196.5 days** across the
2019–2025 baseline, every **130.8 days** for the post-2023 model cohort, and every **88.6 days**
for the post-2024 cohort [S56]. By early 2026, Claude Opus 4.6 reached a 50%-success horizon of
**719 minutes**, about twelve hours [S56]. That is a change in the rate, which is exactly the
kind of quantity the singularity claim is about.

**Capability indices show the same shape.** An item-response-theory index fitted across more
than three dozen benchmarks shows latent-capability growth rising from 8.3 to 15.5 index points
per year after April 2024 [S90].

**AI now writes much of the software the labs run on.** Anthropic reports that more than 80% of
the code merged into its main codebase is authored by Claude as of May 2026, up from low single
digits before February 2025, with the typical engineer merging roughly eight times as many lines
per day as in the 2021–2024 baseline [S64]. Google states 75% of new code across its codebases
is AI-generated in 2026, up from about 50% in 2025 and 25% in 2024; OpenAI's president puts AI
authorship of internal code at about 80% [S66, S67].

**AI optimises the machinery underneath itself.** An LLM-driven Triton kernel optimisation loop,
running candidates on real hardware and backtracking on regressions, produced a geometric-mean
**2.8x speedup** across vLLM attention and mixture-of-experts operators [S74]. A specialised
reinforcement-learning kernel model achieved a 1.2x-or-better speedup on **31.6%** of
KernelBench tasks in one shot, rising to **47.8%** with multi-turn iterative search [S75].

Taken together: the capability side of the loop is fast, and part of the loop is genuinely
closed. AI is helping build AI.

## 4. The evidence that cuts the other way

**Reliability collapses when you raise the bar.** The twelve-hour figure is a *50%* success
horizon. METR's cross-lab pilot found that at an 80% success bar, public frontier models sit at
about **1.5 hours**; internal configurations reach 16–20 hours at 50% but only 3–4 hours at 80%
[S89]. Unattended research needs the 80% bar, not the 50% one. METR's evaluation of GPT-5 put
its autonomous horizon at about **2 hours 17 minutes**, far below METR's own >40-hour threshold
of concern for AI-development acceleration [S26].

**Benchmarks overstate real engineering.** On SWE-bench Verified, proprietary models average
**79.4%** by automated grader. When human maintainers reviewed 296 AI-generated pull requests
that had already passed that grader, they rejected roughly half; merge rates ran about **24
percentage points** below the automated scores [S23]. On SWE-bench Pro — held-out splits,
commercial repositories, contamination controls — state-of-the-art success falls from over 70%
to about **23%** [S03, S04].

**Autonomous science is not yet science.** An independent evaluation of an end-to-end autonomous
research system found about **42%** of its proposed experiments failed outright on code errors,
literature review done by keyword rather than semantic synthesis, a median of five citations per
paper, and hallucinated numerical results [S08].

**And the headline claim about AI-authored science is false as usually told.** As of mid-2026 no
paper written exclusively by an AI has been published in a major peer-reviewed journal. The
March 2026 *Nature* paper is a human-authored manuscript describing the AI Scientist system, not
a paper written by it; the one AI-generated paper that cleared an ICLR workshop bar — average
score 6.33 at a workshop with a 32.6% acceptance rate — was withdrawn before publication by
prior agreement [S76, S96]. This report's own first research pass repeated the vendor framing;
the correction came from the adversarial pass.

**The code-share numbers are softer than they look.** They are measured by the interested party,
"new code" is undefined, and the metric does not separate boilerplate from the core training
loop. The architecturally decisive code may still be human-authored [S92].

**Efficiency estimates disagree by an order of magnitude.** Annual algorithmic-efficiency gain is
put at roughly 2x per year when one-time architectural transitions are excluded, ~3x by Epoch's
eight-month halving figure, ~4x in an informal executive estimate, and ~6x by another 2025
analysis [S86, S01, S87]. A reanalysis argues small-scale ablations account for less than 10x of
a claimed 22,000x gain between 2012 and 2023, implying progress is step-like rather than smoothly
exponential [S86]. These four numbers are not the same metric measured the same way — which is
itself the finding.

**Most of the gain has been bought, not invented.** Between **60% and 95%** of historical
language-model performance improvement is attributable to compute and data scaling rather than to
novel algorithms [S01].

## 5. The measurement that matters most

If AI R&D were self-accelerating, the rate of R&D itself would be compounding. METR's cross-lab
pilot asked exactly that. Its finding, as of the February–March 2026 window: although
task-completion duration has been doubling roughly every four months since 2024, **developer
audits report that overall research-and-development velocity has not yet reached a 2x compounding
acceleration** [S89].

That is the loop-gain measurement. The labs themselves, reporting to an external evaluator, say
the loop has not yet closed at the level the singularity claim requires.

## 6. Non-obvious indicators, and one honest framing device

Beyond the headline benchmarks, several leading indicators have been proposed: the fraction of
research workflow steps executed without a human in the loop; automated experiment throughput per
researcher; the speed at which new evaluations can be built; the wall-clock interval between model
generations; compute-to-capability elasticity; and energy per unit of capability [S89, S90].

Two proposed indicators — insurance-market pricing of AI capability risk and frontier-lab hiring
composition — currently rest on recruiting-vendor and insurance-marketing sources with a
commercial interest in the narrative. They belong on a watch list, not in an evidence base [S97,
S98, S99].

**Framing only, not evidence.** The classic intelligence-explosion models are useful for
intuition and misleading as predictions. I. J. Good's 1965 formulation assumes intelligence
scales frictionlessly and ignores the compute cost of each increment. Vernor Vinge's 1993 essay
requires a mathematical asymptote — progress going vertical at a finite date — whereas measured
progress follows smooth log-linear curves gated by roughly two-year gigawatt-cluster build times.
Later Seed-AI and "FOOM" scenarios assume a software-only takeoff that current hardware limits
contradict [S13, S45]. These are stories that sharpen the question. They are not observations,
and nothing in this report rests on them.

## 7. Bottlenecks and alternative explanations

**Model collapse is real, and conditional.** The mathematical result is that a self-training loop
degenerates when the share of externally grounded data vanishes [S13]. But that is not how
frontier training works: accumulating synthetic data alongside real data bounds the test error,
retaining as little as 10% real seed data is sufficient to stabilise training, external verifiers
screen bad samples, and reinforcement learning with verifiable rewards grounds optimisation in
deterministic environments [S83]. The bound is real; it just does not bind where people usually
invoke it. What *is* true is that improvement under an external verifier stays bounded by that
verifier's grounding capacity — it does not license open-ended expansion [S13].

**Contamination is real, and its headline evidence is confounded.** A systematic review of 55
studies found GPT-3.5 and GPT-4 exposure to about 4.7 million samples across 263 benchmarks, with
contamination inflating GSM8K accuracy by up to 22.9% and MMLU by up to 19.0% [S84]. But the
strongest single argument for contamination — worse performance on post-cutoff questions —
partly dissolves: an ACL 2026 study removed the temporal-decay pattern entirely by paraphrasing
and restructuring LiveCodeBench tasks, showing the decay tracks formatting and lexical drift as
well as leakage [S85]. Contamination inflates scores; the decay signal does not prove by how much.

**Parallelisation has a ceiling.** Even with fully automated R&D, an economic model shows progress
is capped by the serial depth of experiments, combinatorial limits, and the coordination cost of
many highly correlated model instances. It yields three trajectories: conventional explosion,
slower explosion, or prevented explosion [S45].

**Power is the binding physical constraint.** Utilities report time-to-power running 1.5 to 2
years longer than data-centre developers assume, and interconnection for new substations and
high-voltage lines in major US regions routinely takes 36 to 60 months [S43, S81]. US data-centre
electricity use was 176 TWh in 2023, 4.4% of US electricity, and is projected at 325–580 TWh by
2028; global consumption is projected to roughly double from 485 TWh in 2025 to about 950 TWh by
2030 [S39, S81].

**The economy has not moved — but that is weaker evidence than it looks.** Rolling 20-year average
US total factor productivity growth fell to 0.53% in late 2025, and a peer-reviewed model bounds
AI's aggregate TFP contribution at no more than 0.66% over a decade [S15, S49]. Against that:
the productivity J-curve implies unmeasured intangible investment depresses measured output early
— one retrospective adjustment raised measured 2017 TFP by 15.9% — and the underlying data are
heavily revised, with the BLS cutting its March 2025 employment level by 898,000 jobs in January
2026 [S79, S78]. Firm-level evidence is small but positive: a 2026 Richmond Fed CFO survey
attributed about 0.6% labour-productivity growth to AI in 2025 [S80]. Flat macro statistics in
2026 are consistent with both "nothing is happening" and "something is happening and the accounts
have not caught up".

## 8. What the forecasters say, and how little that settles

Expert median forecasts for human-level machine intelligence have moved closer: 2050 in a 2011
elicitation, 2061 in 2016, 2059 in 2022, and 2047 in the 2023 survey conducted after GPT-4
[S51, S54]. The compression is not monotonic — the 2016 median is later than 2011's.

More striking is the disagreement between cohorts asked the same question in the same year:
superforecasters put transformative AI at **1% by 2030 and 21% by 2050**, while AI-domain experts
put it at **9% and 46%** [S46]. A nine-fold gap by 2030 among careful people is not noise; it is
the honest state of the question. And all of these measure *belief*, not capability.

## 9. The calibrated answer, as of 12 August 2026

**Already observed.** Capability is improving fast and the doubling interval for measured task
horizons has shortened [S56]. AI writes a large and rising share of the software at frontier labs
[S64, S66, S67]. AI measurably optimises the low-level code its own training and inference run on
[S74, S75]. Parts of the loop are genuinely closed.

**Not observed.** A compounding rise in the rate of AI R&D itself. The one cross-lab measurement
that targets this reports that R&D velocity has not yet reached a 2x compounding acceleration
[S89]. Reliable long-horizon autonomy is not there either: horizons collapse at the 80% bar
[S89], benchmark scores do not survive contact with maintainers [S23], and autonomous research
systems still fail roughly two experiments in five [S08].

**Still inference.** Whether the loop closes further within the horizon; whether physical and
economic bottlenecks bind or merely delay; whether flat productivity statistics are a real ceiling
or a measurement lag [S45, S79, S78].

**Which definition the evidence bears on.** The evidence bears strongly on sense 1 (rapid
capability improvement — yes, and the rate has risen) and moderately on sense 2 (AI automating AI
engineering — substantially, with the caveat that the metric is self-reported and boilerplate-
heavy [S92]). It does **not** currently support sense 3 (recursive self-improvement with sustained
loop gain), sense 4 (economic discontinuity) or sense 5 (institutional discontinuity).

**The answer.** On the evidence available on 12 August 2026: we are *not* measurably inside a
technological singularity, and the specific loop the classical argument depends on has not been
observed to close. We are, measurably, inside a period of unusually fast capability growth in
which AI performs a large share of AI engineering. Those are different claims, and only the second
is established. Confidence in that split: moderate — high on the individual measurements, lower on
the synthesis, because the decisive metric (compounding R&D velocity) is self-reported by the labs
being evaluated and "velocity" is not a standardised quantity [S89].

## 10. What would change this answer

Five observations would materially move it:

1. METR-style task horizons at the **80%** bar exceeding a full working day — the 50% figure is
   not the one that matters [S89].
2. The cross-lab audit reporting that R&D velocity **has** reached sustained 2x-or-better
   compounding acceleration [S89].
3. An externally audited measurement — not a self-report — of the share of *core* model and
   training-loop code authored by AI, above roughly 20% [S92].
4. Papers authored solely by AI systems clearing full peer review at major venues, repeatedly and
   without prior arrangement [S76].
5. Total factor productivity breaking its post-1970s trend in a way that survives revision, or the
   intangible-investment adjustment closing the gap [S78, S79].

Equally, the answer would harden in the other direction if 80%-bar horizons flatten, if the METR
suite saturates without a successor that preserves the trend measurement [S56, S94], or if the
time-to-power gap widens rather than closes [S43].

## 11. What to monitor

The 80%-success task horizon; the cross-lab R&D-velocity audit; independently audited core-code
authorship; peer-review outcomes for AI-authored work; interconnection queue times; and revised
productivity statistics. Watch, but do not yet count: insurance pricing of AI capability risk and
frontier-lab hiring composition [S97, S98, S99].

## 12. Methodology

Three Deep Research passes were run in one fresh Gemini Notebook on 2026-08-12: a landscape pass,
an adversarial pass aimed at the thesis emerging from the first, and a weak-signals pass. All 264
results were imported so that nothing was discarded; every pass report, its citation mapping and
its result inventory were preserved locally. Sources were then curated into a registry with
provenance lineage, and claims into an evidence matrix with exact locators. Ten candidate claims
were dropped for unusable locators — including three whose citation markers in the first pass
pointed at sources that could not support them. Quantitative charts were rendered
deterministically from local data files, never drawn by an image generator. Contradictions between
passes were preserved rather than averaged.

Content is web-researched as of 2026-08-12 and is not verified against authoritative internal
documentation.
