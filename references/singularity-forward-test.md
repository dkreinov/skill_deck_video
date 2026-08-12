# Singularity forward test

This is the forward test to run in a clean session against the revised skill. It is a test plan, not something to execute during authoring. The test validates that the enhanced deck-video skill can conduct rigorous, source-grounded research on a complex existential hypothesis while maintaining epistemic discipline and avoiding conflation of distinct concepts.

## Clean-session prompt

> Create a narrated report video investigating whether we are approaching the technological singularity. Use auto mode.

The agent must ask the full Phase 0 batch before research. It must not assume what "singularity" means.

## Example intake

- **Question:** Are there measurable early signs that AI development is becoming self-accelerating?
- **Initial hypothesis:** Some feedback loops may already be measurable, but that is not equivalent to a singularity.
- **Approach:** balanced scientific core + pop-science narrative + science-fiction framing + non-obvious weak signals.
- **Epistemic posture:** attempt to falsify the hypothesis before forming the conclusion.
- **Audience:** technically curious general audience.
- **Format:** 15-minute narrated report video.
- **As-of date:** 2026-08-12.
- **Forecast horizon:** through 2035.
- **Automation:** continue without another editorial checkpoint unless blocked.

## Operational definitions

The report must distinguish at least:

- rapid general capability improvement;
- AI automation of AI research and engineering;
- recursive self-improvement;
- economic growth discontinuity;
- social or institutional discontinuity.

It must not use "singularity," "AGI," and "superintelligence" as synonyms.

## Research axes

1. AI task horizon, autonomy, and reliability.
2. AI contribution to model research, coding, evaluation, chip design, and scientific discovery.
3. Algorithmic efficiency and cost trends.
4. Compute, energy, data, hardware, and infrastructure constraints.
5. Recursive feedback loops and evidence of acceleration in the rate of AI progress.
6. Deployment, economic diffusion, productivity, and institutional adaptation.
7. Forecasts, prediction markets, expert disagreement, and failed historical predictions.
8. Non-obvious indicators such as AI-authored research share, automated experiment throughput, evaluation-development speed, lab-cycle compression, and the fraction of AI R&D workflows performed by AI.

These are research hypotheses, not facts. The final set should be retained only when measurable and sourced.

## Deep Research queries

### Landscape query

> As of 2026-08-12, investigate what measurable evidence supports or contradicts the claim that AI research and development is becoming self-accelerating. Define the relevant meanings of technological singularity and keep them separate. Prioritize original papers, benchmark repositories, independent evaluations, system cards, economic datasets, and official technical reports. Separate observed measurements, author interpretations, forecasts, and speculation. Cover AI task horizons and autonomy, AI contributions to AI R&D, algorithmic efficiency, compute and energy constraints, economic diffusion, and historical prediction accuracy. Do not assume the singularity is near. Return important disagreements and methodological limitations with citations.

### Adversarial query

> Build the strongest evidence-based case that current AI progress does not demonstrate an approaching technological singularity. Find failed forecasts, benchmark contamination or saturation, weak transfer from benchmarks to reliable autonomy, limits to recursive self-improvement, compute and energy bottlenecks, deployment friction, economic evidence, and independent critiques. Trace secondary claims back to primary sources where possible. Distinguish lack of evidence from evidence of absence.

### Weak-signals query

> Identify measurable, non-obvious leading indicators that would update the probability of AI development becoming self-accelerating before conventional AGI benchmarks make it obvious. For each proposed indicator, explain the causal link, current measurable evidence, data availability, confounders, falsification condition, and strongest source. Exclude indicators that are merely restatements of model benchmark improvement.

## Required conclusion form

The final report must answer with a calibrated status rather than a cinematic yes/no declaration:

- what is already observed;
- what remains inference;
- what evidence is missing;
- which definition of singularity, if any, the evidence bears on;
- current confidence and uncertainty;
- what measurable events would materially update the answer.

## Pass criteria

The forward test passes only if the execution demonstrates all of the following:

- [ ] one batched intake round;
- [ ] a fresh notebook with recorded identity;
- [ ] distinct landscape and adversarial Deep Research passes;
- [ ] preservation of report text, citation mapping, and complete source inventory;
- [ ] import-all-first behavior or a documented source-limit fallback;
- [ ] local preservation of all evidence used in central claims;
- [ ] a source registry with provenance lineage;
- [ ] a claim-level evidence matrix;
- [ ] explicit handling of contradictory evidence;
- [ ] correct separation of science fiction, fringe claims, forecasts, and observations;
- [ ] agent-authored final synthesis;
- [ ] source isolation during slide generation;
- [ ] deterministic rendering of quantitative charts;
- [ ] visible citations in the video;
- [ ] a dated, calibrated conclusion;
- [ ] uninterrupted automatic continuation unless an escalation rule is triggered.
