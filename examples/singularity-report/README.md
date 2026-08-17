# Example: the singularity report (web-researched run)

A complete **topic-only** run of this skill: the only human input was the
clean-session prompt from `references/singularity-forward-test.md` —

> Create a narrated report video investigating whether we are approaching the
> technological singularity. Use auto mode.

— followed by one batched intake round. Everything else (research, evidence,
narrative, deck, narration, music, QA) ran automatically. Run date
2026-08-12; as-of date of the report itself is the same day.

The deck was regenerated on 2026-08-13 at the **evocative** visual register
(`references/visual-style.md`): the research, narrative, narration and the
four DATA CHART slides are unchanged; only the Global visual direction and
the per-slide Visual paragraphs were rewritten. The deck's image system has
two kinds — REAL (ordinary machinery, photographed plainly, the single amber
accent appearing only as actual light) and IMAGINED (the singularity as
popular culture pictures it) — and the argument lives in the distance
between them, framed by headlines and narration rather than labels.

This is the counterpart to [`../karpathy-three-months/`](../karpathy-three-months/),
which is a **source-grounded** run. Here nothing was supplied but a question.

## What is in this folder

| File | What it is |
|---|---|
| `run_manifest.json` | The run ledger: intake answers, notebook identity, the three research passes, source counts, artifact paths, blockers |
| `research_brief.md` | Written **before** any research: central question, definitions, hypotheses, falsifiers, axes, scope |
| `research/pass_[ABC]_report.md` | The full Deep Research report from each pass, preserved verbatim with its citation markers |
| `research/pass_[ABC]_inventory.md` | Per-pass result inventory and the import decision (all 264 results imported, none omitted) |
| `source_registry.md` | 99 sources: type, primary/secondary, independent/interested, pass, status, and a `Lineage` column that stops a study and its recap being counted twice |
| `evidence_matrix.md` | 35 central claims, each with class, supporting/contradicting sources, an exact locator, confidence, caveats and disposition — plus 10 claims explicitly omitted, with reasons |
| `research_checkpoint.md` | Written instead of pausing to ask the user: emerging answer, strongest evidence for and against, gaps, go/no-go |
| `notebooklm_source.md` | The agent-authored narrative — every central claim carries its `[Snn]` source IDs |
| `slide_division.md` | Per-slide Data + Visual spec, the source IDs behind each slide, and the exact prompt pasted into Gemini Notebook |
| `narration_script.md` | The spoken script, one block per slide |
| `charts/*.csv` + `render_charts.py` | The four DATA CHART slides: data files carrying `source_ids`, metric definitions, units, dataset versions and the render command |
| `singularity_clean.pptx` | The deck, watermark-removed and rebuilt locally |
| `singularity_final.mp4` | The narrated video with a music bed (~15 min) |

Intermediates that are not shipped: raw captures, per-segment TTS/video files,
the music source, and the QA frames.

## How it scored

Graded by a fresh reviewer against the 16-item checklist in
`references/singularity-forward-test.md`: **14 PASS, 2 PARTIAL, 0 FAIL.**

The two partials are disclosure gaps, kept visible on purpose:

1. **Intake round count** — the manifest records batched answers and the
   defaults used, but the conversation itself is not part of the run
   directory, so "exactly one round" cannot be verified from artifacts alone.
2. **Complete source inventory** — all 264 results were imported, and every
   cited source is enumerated; roughly 69 *uncited* results across the three
   passes were imported but not transcribed individually. Each pass inventory
   says so in writing.

Worth reading for what the pipeline is meant to catch: `evidence_matrix.md`
preserves contradictions instead of averaging them away, the omitted-claims
table shows what was dropped for thin support, and `research_checkpoint.md`
records a citation error the run caught against itself and the claim it
removed as a result.

Note: `research_checkpoint.md` states that `scripts/validate_evidence.py`
runs error- and warning-free on this run. That was aspirational when written —
the validator was miscounting citation IDs such as `[S64]` as uncited
numbers. The validator was fixed afterwards; the statement is now true, and
`python scripts/validate_evidence.py examples/singularity-report` exits 0
with no findings.

## Caveat on provenance

This run is **web-researched**, not verified against authoritative
documentation. The narrative, the deck and the video all carry that
disclosure. Treat it as a demonstration of the evidence pipeline, not as a
reference on its subject.
