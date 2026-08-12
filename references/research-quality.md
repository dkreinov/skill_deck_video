# Research quality: registry, evidence matrix, and gates

This reference defines the evidence-quality control system for `deck-video`
research runs: the source registry, the evidence matrix, the evidence rules,
the placeholder structures for `research_brief.md` and
`research_checkpoint.md`, the deterministic-chart contract, the audit
checklist, and the go/no-go rules. Follow it exactly when curating research
into `notebooklm_source.md`.

## source_registry.md

`source_registry.md` records every imported or materially considered source.
Every such source gets a row. Reproduce this table header and separator row
verbatim:

```
| ID | Title | Org/Author | URL | Pub date | Accessed | Type | Primary | Independent | Pass | Status | Topics | Caveats | Lineage | Score |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Column definitions:

- **ID** — stable source identifier, format `S` followed by 2 or more digits
  (e.g. `S01`, `S23`). Never renumber or reassign an ID once given.
- **Title** — the source's title.
- **Org/Author** — the publishing organization or author.
- **URL** — the source URL.
- **Pub date** — the source's publication date.
- **Accessed** — the date the source was accessed by this run.
- **Type** — one of: paper, dataset, benchmark, system card, official
  statement/report, journalism, commentary, fiction, forum, etc.
- **Primary** — `primary` or `secondary`.
- **Independent** — `independent` or `interested`. A source counts as
  `interested` when it is a vendor, funder, or other stakeholder in the claim
  it bears on.
- **Pass** — which research pass found the source (e.g. Pass A, Pass B, Pass
  C, Pass D).
- **Status** — `imported`, `downloaded`, `omitted`, or `inaccessible`.
- **Topics** — topics the source covers.
- **Caveats** — known caveats about the source.
- **Lineage** — `-` if the source has no parent, or a comma-separated list of
  parent source IDs. A summary or recap of `S03` must list `S03` in its
  Lineage column. This prevents counting a summary and its underlying source
  as two independent pieces of evidence.
- **Score** — `-` or a 0-10 integer.

### Triage scoring (0-10)

Score is optional per source but, when used, is broken down as:

- directness to the claim: 0-3;
- authority / methodological quality: 0-3;
- independence: 0-2;
- freshness for the question: 0-2.

The score is for triage only. It is never a mechanical truth score — a high
score does not make a claim true, and a low score does not make it false.

## evidence_matrix.md

`evidence_matrix.md` records every central claim. Reproduce this table
header and separator row verbatim:

```
| Claim ID | Claim | Class | Supports | Contradicts | Locator | Metric | Confidence | Caveats | Disposition |
|---|---|---|---|---|---|---|---|---|---|
```

Column definitions:

- **Claim ID** — format `C` followed by 2 or more digits (e.g. `C01`, `C14`).
- **Claim** — the atomic claim text.
- **Class** — one of: `observed` (an observed result), `interpretation` (a
  source's interpretation), `forecast`, or `inference` (a presenter
  inference).
- **Supports** — `-` or comma-separated source IDs.
- **Contradicts** — `-` or comma-separated source IDs.
- **Locator** — the exact quotation, table, figure, page, section, or
  timestamp that grounds the claim. Required — must not be `-` — whenever
  Disposition is `include` or `qualify`.
- **Metric** — the metric definition and version, for quantitative claims.
- **Confidence** — `strong`, `moderate`, `weak`, or `speculative`.
- **Caveats** — known caveats.
- **Disposition** — `include`, `qualify`, `omit`, or `investigate`.

**Hard rule:** no central claim may enter `notebooklm_source.md` without a
corresponding evidence-matrix entry.

## Evidence rules

- Prefer primary evidence and independent replication.
- For consequential synthesized claims, seek at least two independent
  sources when possible.
- A vendor's own benchmark is evidence of what the vendor reported — it is
  not independent proof of the underlying general claim.
- Preserve disagreements and ranges rather than averaging them into false
  certainty.
- Never compare metrics across incompatible benchmark versions, datasets,
  evaluators, or experimental settings.
- Timestamp all current-state claims and forecasts.

## research_brief.md

Write `research_brief.md` before running any Deep Research pass. Never send
a vague topic (e.g. bare "singularity") to research. The file must contain
these section headings, exactly:

- `## Central question`
- `## Definitions`
- `## Hypotheses` (initial hypothesis and alternative hypotheses)
- `## Evidence that would support`
- `## Evidence that would weaken or falsify`
- `## Research axes`
- `## Source-quality policy`
- `## Scope and dates` (as-of date, forecast horizon, and boundaries)
- `## Editorial approach and audience`
- `## Excluded topics`
- `## Expected output structure`

## research_checkpoint.md

Write `research_checkpoint.md` after synthesis, instead of asking the user
for an editorial checkpoint. The file must contain these section headings,
exactly:

- `## Emerging answer`
- `## Strongest supporting evidence`
- `## Strongest counter-evidence`
- `## Unresolved gaps`
- `## Omitted claims` (claims omitted for insufficient support)
- `## Go/no-go` (whether the evidence supports continuing)

## DATA CHART requirements

Generate every quantitative chart deterministically from a local CSV/JSON
data file. Never ask an image generator to draw a quantitative chart.

Each chart must record all seven of the following fields:

1. source ID(s);
2. metric name and definition;
3. units and denominator;
4. dataset/benchmark version;
5. date range;
6. transformation or normalization performed;
7. render command — the code or command used to render the chart.

Chart data files must carry `source_ids` metadata: a CSV header comment
(`# source_ids: ...`) or a JSON key. `scripts/validate_evidence.py`
machine-checks only the `source_ids` presence; the other six fields are
enforced by this checklist during the Fact Gate. The Fact Gate must compare
every displayed number with the data file, not merely with the narrative
paragraph.

## Audit checklist

Run these checks against a finished evidence set:

- **Stale sources** — Accessed date far older than the as-of date.
- **Source concentration** — most included claims resting on one source.
- **Circular citations** — a claim "supported" by both a source and its own
  summary/derivative via Lineage.
- **Unsupported forecasts** — forecast-class claims presented with strong
  confidence.
- **Contradictory claims** included without caveats.
- **Chart-number mismatches** — numbers on a rendered chart not matching the
  data file.

`scripts/validate_evidence.py` automatically flags: stale sources, source
concentration, circular citations, unsupported forecasts, unhandled
contradictions, missing chart `source_ids`, and uncited numbers. The
remaining checks in this list are a manual pass.

## Go / no-go

- **Proceed** when central claims have evidence-matrix entries with
  locators, and `research_checkpoint.md` shows the evidence supports
  continuing.
- **Stop and escalate to the user** when central evidence is unavailable, or
  so contradictory that any conclusion would mislead.
