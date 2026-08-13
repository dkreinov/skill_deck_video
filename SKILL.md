---
name: deck-video
description: Turn a topic — with or without ready sources — into a fact-checked slide deck (via Gemini Notebook / NotebookLM) and a narrated MP4 with music. Use when the user asks for a presentation, explainer deck, narrated presentation video, or a narrated research/report video investigating a question or hypothesis. Covers one-round intake, topic-only multi-pass Deep Research (landscape + adversarial passes), claim-level evidence verification (source registry + evidence matrix), NotebookLM slide generation (manual gate or Chrome-automated), fact verification of ALL text and visuals, deterministic data charts, watermark cleanup, TTS narration, and music mixing.
---

# deck-video — sourced deck + narrated video pipeline

This skill turns a topic — with or without sources you already trust — into a
fact-checked slide deck built in **Gemini Notebook (formerly NotebookLM)** and
a narrated MP4 with music.

Produces, from a topic — with or without ready sources:
- On a topic-only research run (no ready sources, Phase 1R), before the deck:
  `run_manifest.json` — run manifest and artifact ledger; `research_brief.md`
  — intake answers, defaults, and research plan; `source_registry.md` — every
  source found, with locators; `evidence_matrix.md` — claim-level evidence
  linking claims to sources; `research_checkpoint.md` — written automatically
  in place of an editorial pause — plus the preserved per-pass research
  reports.
- On every run: `notebooklm_source.md` — the full factual narrative (single
  source of truth); `slide_division.md` — per-slide Data + Visual spec; the
  NotebookLM-generated deck (PPTX + PDF), fact-gated and watermark-free;
  `<name>_narrated.mp4` — narrated video; `<name>_final.mp4` — with music bed.

Scripts live in `scripts/` next to this file. Preflight (once per machine):
`pip install pymupdf opencv-python numpy edge-tts imageio-ffmpeg`
(ffmpeg itself ships with imageio-ffmpeg — no separate install). Auto mode
additionally needs the claude-in-chrome extension connected and the user logged
into NotebookLM in that Chrome; music generation needs a logged-in Suno account
(optional — see Phase 5 fallback).

## Reference map

- `references/research-modes.md` — intake fields, defaults, style-vs-evidence
  rules. Read at Phase 0.
- `references/notebooklm-research.md` — notebook lifecycle, multi-pass Deep
  Research, preservation, synthesis surfaces, source isolation, UI adapter.
  Read on any notebook operation.
- `references/research-quality.md` — registry/matrix schemas, evidence rules,
  DATA CHART requirements, audit checklist. Read when curating evidence.
- `references/visual-style.md` — slide visual language: global style block,
  category playbook, anti-AI-fluff rules. Read when authoring slide_division.md
  and when reviewing rendered slides.
- `references/singularity-forward-test.md` — acceptance test plan. Read when
  asked to run the forward test.
- `scripts/init_research_run.py` — creates the run dir + manifest +
  placeholders.
- `scripts/validate_evidence.py` — validates registry/matrix; `--selftest`.

## Non-negotiable: the Fact Gate

Everything shown or spoken must trace to the source documents. Enforce at three points:

1. **While writing** `notebooklm_source.md`: every claim comes from a fetched source
   (docs site, user-provided files). No remembered "facts". Numbers, stage names,
   orderings, file formats — verbatim from sources. On a research run, every
   central claim must also have an `evidence_matrix.md` row with a non-`-`
   Locator before it may enter `notebooklm_source.md`.
2. **Slide review** (after any generation): render every slide to PNG
   (`render_review.py`) and check EACH slide against `notebooklm_source.md`:
   - every number on the slide exists in the source doc (**no-unsourced-numbers rule**
     — generators love inventing "85% faster / 10X" stopwatches; kill on sight)
   - names, stage orders, file names, platform names exactly right
   - **text rendered inside images** — AI image renderers garble words
     ("Laisnry Budget") and produce invalid data (non-hex "0xAT"); zoom and read it all
   - slides claiming two things are "equal/identical" must show identical values
   - imagery must not depict recognizable third-party brands (a "generic car" often
     renders as a Tesla)
   - phrasing that inverts meaning ("if degradation fails")
   - numbers on a DATA CHART slide are verified against the chart's
     **data file**, not merely the narrative paragraph
   Produce a verdict table (slide | claim | source line | pass/fix). Fix via
   NotebookLM Revise, re-export, re-review changed slides. Iterate until all pass.
   Prefer a fresh-eyes subagent for this pass — the author of slide_division.md is
   blind to their own hand-waves.
3. **Narration script**: same rule — the spoken text may simplify but never add
   facts/numbers absent from the source doc.

## Phase 0 — Intake & run setup (one batched round, before any work)

Ask ONE batched round (AskUserQuestion) covering these seven fields:
- Central question or hypothesis
- Research/editorial approach
- Epistemic posture
- Audience and desired takeaway
- Delivery format and length
- Scope and time boundary
- Research permissions and extras

For the full sub-questions and modes behind each field, see
`references/research-modes.md`. "your call" is accepted as an answer for
every field; defaults then come from that file's `## Recommended defaults`
section — do not restate the default values here.

Then run setup:
- Run `python scripts/init_research_run.py <run-dir> --topic "<topic>"`. The
  run directory is created in the **user's working directory** (the project
  the video is for) — **never inside the skill repo**. This creates
  `run_manifest.json` plus the four placeholder files. Record the intake
  answers and defaults used in the manifest (`intake.answers`,
  `intake.defaults_used`); every artifact path produced later is recorded in
  the manifest's `artifacts`.
- Create a NEW notebook per project named
  `YYYY-MM-DD — <topic-slug> — deck-video` (the init script prints it), and
  verify it holds no sources from another project; record its URL in the
  manifest. Reuse a notebook only when the user explicitly continues that
  project — see `## Notebook lifecycle` in `references/notebooklm-research.md`.

For high-stakes decks (execs, external audiences, decision meetings): if a
grill-me-style interrogation skill is available in the session, offer to run it
instead of the mini-brief — but never depend on it; this phase is
self-contained.

## Automatic continuation and escalation

After Phase 0, proceed automatically through research, synthesis, deck,
narration, music, and QA. There is NO editorial checkpoint by default: write
`research_checkpoint.md` (sections defined in `references/research-quality.md`)
instead of asking.

Ask the user again ONLY when:
- login, browser control, file access, or payment authorization is required
- the user's chosen approach is technically or legally unavailable
- two materially different interpretations would produce different videos and the intake does not resolve them
- central evidence is unavailable or contradictory enough that any conclusion would be misleading
- a source or action requires new authority beyond the initial permission

UI drift alone is never a reason to abandon the run — use the documented
fallback, record it in the manifest's `blockers`, and continue.

## Phase 1 — Research & author the two docs

The Fact Gate is only as strong as this phase — every later verification checks
slides *against the source doc*, so what isn't captured here can't be verified
later. Research procedure:

1. **Start from what the user gave** (docs URLs, files, MCP doc tools). If they
   gave only a topic, ask where the trusted sources live — do NOT substitute
   web search for authoritative topics (internal systems, products, APIs),
   regardless of opt-in. If the user has only a topic and granted public-web
   Deep Research permission in the Phase 0 intake, go to **Phase 1R** below
   instead of stalling here. If they hand over an already-researched write-up,
   treat it as the raw source: still run step 3 (verbatim extraction) and
   step 4 (coverage check) on it, then continue from "Then author" below.
2. **Drill, don't skim.** Index/landing pages give marketing-level text; the
   flows, stage names, file formats, and platform names live in sub-pages.
   From each landing page, list its sub-page links and fetch the ones matching
   the deck's spine (getting-started / flow / architecture / high-level design).
   Two levels deep is the norm, one fetch is never enough.
3. **Extract verbatim, not paraphrased**: exact stage names and their order,
   tool/command names, file names and formats, platform/version names, and any
   number you might want on a slide (with its source location). Distinguish
   "the doc says X" from "I inferred X" — inferences don't go in the source doc.
4. **Coverage check before writing**: for each planned slide topic, can you
   point at a fetched source for it? Gaps → fetch more or drop the topic.
   If the sources genuinely don't cover something the user asked for, say so
   and ask — don't fill with plausible content.

### Phase 1R — Topic-only: multi-pass research in Gemini Notebook

Trigger: the user has only a topic and granted public-web Deep Research permission in the Phase 0 intake.

1. Write `research_brief.md` from the intake BEFORE any research pass — required headings are frozen in `references/research-quality.md` (`## research_brief.md`). Never send a bare topic (e.g. "singularity") to Deep Research.
2. Run the multi-pass protocol per `## Multi-pass Deep Research protocol` in `references/notebooklm-research.md`: Pass A (landscape) and Pass B (adversarial) always; Pass C (weak signals / editorial lens) when the chosen approach calls for it; Pass D (gap closure) only after the evidence matrix exists. Record each pass (query, timestamps, fallback) in `run_manifest.json` `research_passes`.
3. Before closing ANY Deep Research result view: capture the report text, citation mapping, and the complete result inventory; default to **Import all results**; record omissions — per `## Preserve results before closing` in `references/notebooklm-research.md`. Save each pass's full report locally, one file per pass, its path recorded in the manifest's `artifacts`.
4. Curate into `source_registry.md` and `evidence_matrix.md` per `references/research-quality.md` (schemas live there). Hard rule, verbatim: "No central claim may enter `notebooklm_source.md` without an evidence-matrix entry."
5. Run `python scripts/validate_evidence.py <run-dir>` after curation — ERRORs block progress; WARNs are fixed or explained in `research_checkpoint.md`. Run it AGAIN after `notebooklm_source.md` and any chart data files exist (the uncited-number and chart checks need them).
6. Only after the independent evidence review below: THE AGENT writes the synthesis: Deep Research reports are discovery leads, source summaries are orientation, Chat with selected sources is for evidence extraction, Studio Reports are an optional second opinion — per `## Synthesis surfaces` in `references/notebooklm-research.md`. NotebookLM never silently chooses the thesis.
7. Write `research_checkpoint.md` (headings frozen in `references/research-quality.md`) and continue automatically on a go verdict — no user checkpoint (see "Automatic continuation and escalation" above).

Mechanism: **manual gate** (default) — the user runs the research in the notebook and hands results back; **auto mode** — drive the UI per the recipe and adapter in `references/notebooklm-research.md`. Nothing else about the UI belongs here.

Provenance: `notebooklm_source.md` carries a note that its content is web-researched via Gemini Notebook (formerly NotebookLM) Deep Research as of the run's as-of date, NOT verified against authoritative docs; the same disclosure is repeated in Phase 6.

Notebook reuse: this research happens in the SAME notebook later used for slide generation.

### Independent evidence review

Before the synthesis is written (topic-only research runs): dispatch a
fresh-eyes subagent — fresh context, no authoring history — that receives
ONLY `research_brief.md`, `source_registry.md`, `evidence_matrix.md`, and the
preserved source excerpts.

Its job is adversarial: try to refute the central claims — verify each
Locator against its source; hunt for omitted contradicting evidence;
challenge Class and Confidence labels.

Every finding must be resolved in the matrix (fix, qualify, or omit the
claim) before synthesis; record the review and its resolutions in
`research_checkpoint.md`.

Rationale: the Independent column and the validator are bookkeeping by the
same author; this is the only step where different eyes check the evidence
itself.

Then author:
- `notebooklm_source.md`: full narrative (why it matters, actors, flows, how
  parts connect, takeaway) — on a research run, built ONLY from claims with
  evidence-matrix rows; central claims carry their compact source IDs (e.g.
  [S03]).
- `slide_division.md`: N slides (let content decide N; 10–15 typical). Per
  slide:
  - **Data**: exactly what appears on the slide
  - **Visual**: one paragraph, usable directly as an image prompt, written
    per `references/visual-style.md` (declare a Global visual direction block
    first; assertion-evidence, one accent, no AI-fluff cliches, no
    generator-rendered numbers). Visual categories are **DIAGRAM**
    (flow/architecture), **DATA CHART** (quantitative), or illustration.
  - Each slide lists the compact source IDs backing its claims.
  - The deck ends with a bibliography slide mapping source IDs to
    titles/URLs.
- End slide_division.md with the NotebookLM run notes and the outline-paste prompt
  (see Phase 2 template).

### Report-video mode

Applies when the Phase 0 delivery format is a narrated report video. The slide
outline follows this twelve-beat structure, in order:

1. Cold open: the central question.
2. Definition: what would count as the phenomenon?
3. Measurement dashboard.
4. Strongest evidence supporting the hypothesis.
5. Strongest evidence against it.
6. Non-obvious indicators or the selected special lens.
7. Bottlenecks and alternative explanations.
8. Scenarios and forecast ranges.
9. Calibrated answer as of the stated date.
10. What would change the conclusion.
11. What to monitor next.
12. Methodology and sources.

Narration carries the reasoning; slides show evidence, diagrams, timelines,
and charts — never paragraphs of report text.

### DATA CHART slides

Quantitative charts are generated deterministically from a local CSV/JSON data
file in the run dir — never by asking an image generator to draw numbers. The
data file carries `source_ids` metadata; all seven required fields per chart
are listed in `## DATA CHART requirements` in `references/research-quality.md`;
`scripts/validate_evidence.py` machine-checks only the `source_ids` presence —
the rest is Fact Gate work.

## Phase 2 — Generate the deck in NotebookLM

The single biggest control lever: **paste the outline verbatim into the prompt box**
(NotebookLM follows a pasted outline near-1:1; referencing an uploaded source is weaker).

Settings: Studio → Slide Deck → Format **Presenter Slides**, Length **Default**.
Prompt template:

```
Audience: <who>. Create exactly <N> slides. Use this outline EXACTLY — same order,
same titles, one slide each:
1. <title> ... N. <title>
For each slide use the matching "Data" and "Visual" descriptions from the
Slide Division source. Keep text minimal: key message + max 3 bullets per slide.
House style for EVERY slide: <paste the Global visual direction block from
slide_division.md verbatim, including its standing ban line>.
```

### Source isolation (hard gate)

On a research run the notebook also contains raw Deep Research reports,
imported web sources, and saved notes — not just the two authored docs. For
slide generation, select ONLY `notebooklm_source.md` and `slide_division.md`
as sources and EXCLUDE everything else. Explicitly verify the source checkboxes
before generating — this is a hard gate, do not proceed assuming selection is
already correct. See `## Source-selection isolation` in
`references/notebooklm-research.md`.

Two execution modes:

**Manual gate (default):** give the user the upload list (both .md files), the
settings, and the prompt. They generate, optionally Revise, and export PPTX + PDF.

**Auto mode (Chrome):** with claude-in-chrome tools (`tabs_context_mcp` first,
then navigate/computer/find/file_upload):
1. notebooklm.google.com → Create new notebook
2. Upload both .md files as sources (file_upload; if .md rejected, rename .txt)
3. Studio panel → Slide Deck → open customization → set Format/Length → paste prompt
4. Generate (60s–10min; poll with wait+screenshot)
5. Three-dot menu on the artifact → "Download PDF Document (.pdf)" and
   "Download PowerPoint (.pptx)"
6. Verify the file actually landed in `~/Downloads` (downloads fail silently;
   re-try via UI once, then stop and hand to user)
Two known failure modes: source upload has no `<input type=file>` until the
native picker opens (use the Copied-text path instead), and
automation-initiated export downloads are blocked by Chrome (the download
click is the user's). Details and current workarounds live in
`## UI adapter (verified 2026-08-12)` in `references/notebooklm-research.md`.
Site UIs churn — if any step 404s or elements moved, fall back to the manual gate
rather than fighting it.

**Audit-first order (auto mode): review → revise → capture. Fully automatic.**
Do NOT download after generation. Open the artifact's expanded viewer (⤢ icon),
walk every slide via the right-hand thumbnails (click thumb → screenshot → zoom
where text is small), and run the full Fact Gate on the screenshots — no files
needed. Then click **Revise**, select each failing slide, enter its instruction
(form_input on the "Revision instructions" textbox), let them batch under
"Pending changes", and **Generate revised deck**. Re-audit the changed slides.
Batch all slide instructions into as few Revise passes as possible — each
pass regenerates the WHOLE deck, so re-check untouched slides too; revisions
do not consult the sources, so state corrected facts verbatim in the
instruction. A style fault repeating on every slide means the generation
prompt was wrong: fix the prompt and regenerate once, per
`references/visual-style.md`.

**Native-resolution capture (replaces the download entirely):** the slide PNGs
live on auth-gated lh3.googleusercontent URLs (session-cookie-only; curl gets a
login page, canvas export is CORS-tainted). But they render in-page at native
1376×768 — so extract them via the screenshot pipeline:
1. In the expanded viewer, scroll the thumbnail rail fully (forces lazy-load),
   then collect srcs in DOM order via javascript_tool:
   `[...document.querySelectorAll('img[src*="lh3.googleusercontent.com/notebooklm"]')].map(i=>i.src)`
2. **Measure the buffer scale first — this is the whole trick.** The `zoom`
   region is in SCREENSHOT-BUFFER pixels, NOT CSS pixels, and the buffer is the
   viewport downscaled to a **1568px-wide cap**. Take one plain `screenshot`,
   read its width `SW`, read `innerWidth` via javascript_tool, and compute
   `S = SW / innerWidth`. On a maximized 1920×855 window S = 0.8167 and the
   buffer is only ~698 rows tall — **less than a slide's 768**, which is why the
   naive region [0,0,1376,768] fails with "Region exceeds viewport boundaries".
   Do not trust `resize_window` to fix this: Chrome silently ignores resizes
   while a window is maximized, and `innerWidth` stays pinned.
3. Inject a fixed overlay `<img>` at top-left with a **magenta** full-page
   backdrop (`#ff00ff`, z-index max) so backdrop bleed is detectable later.
   Size the overlay in CSS px so it lands at native size in the buffer:
   `W_css = 1376 / S`, `H_css = 768 / S` (≈1685×940 at S=0.8167). Set its src
   per slide (`await img.decode()` +250ms).
4. Because `H_css` exceeds the viewport, capture each slide in **two vertical
   passes** and stitch:
   - pass A: overlay `top: 0px`      → `zoom` region [0, 0, 1376, 690]
   - pass B: overlay `top: -96px`    → `zoom` region [0, 0, 1376, 690]
   96 CSS px ≈ 78 buffer px of shift, so pass B covers slide rows ~78..768.
   Use `save_to_disk: true`; save as `slide_NN_A.png` / `slide_NN_B.png`.
   Batch the four actions (js, zoom, js, zoom) per slide with `browser_batch` —
   larger batches time out. Remove the overlay afterwards.
5. Stitch with `python scripts/stitch_slides.py captures_dir slides_dir`. It
   resizes each capture back to the true region size, recovers the vertical
   offset by cross-correlating the overlap (do NOT trust the arithmetic — zoom
   resamples its output), and writes exact 1376×768 PNGs. It also replaces any
   edge row/column still showing the magenta backdrop; expect `edge_rows=1`,
   which is sub-pixel rounding, not a bug. Sanity check: reported offset should
   be identical across all slides and overlap error < ~4/255.
6. Inpaint the watermark with
   `python scripts/clean_watermark_png.py slides_dir slides_clean`, then build
   the PPTX with `python scripts/build_pptx.py out.pptx slides_clean/` — it
   assembles a valid deck for any number of images from the bundled
   `deck_template.zip` (no donor file or third-party libs needed).

If the Chrome window is minimized, `innerWidth/innerHeight` read 0 and
`visibilityState` is `hidden`; screenshots fail with a clip-deserialization or
host-permission error. JavaScript still runs, so this is easy to misdiagnose —
check those two values before assuming the page is broken, and ask the user to
restore the window.
Then CONTINUE WITHOUT PAUSING into Phase 4 (narration) and Phase 5 (music) —
the deliverable of auto mode is the narrated+music MP4 plus the rebuilt PPTX,
not a deck the user still has to process. The NotebookLM Download buttons
remain available to the user for an "official" export, but nothing depends on
them.

Export reality (as of 2026-08): slides come back as one full-bleed PNG per slide —
no editable text boxes. All fixes go through NotebookLM Revise + re-export, or
pixel edits.

## Phase 3 — Clean

- `python scripts/clean_watermark.py in.pptx out_clean.pptx` — inpaints the
  bottom-right "Gemini Notebook" stamp on every slide image locally (never upload
  internal decks to third-party watermark sites). Then run render_review.py on
  the output and zoom the bottom-right corner of photo-heavy slides to check for
  inpaint smudges.

## Phase 4 — Narrate

- Write `narration_script.md`: one `## Slide N — <title>` block per slide.
  Spoken register: full sentences, transitions between slides, spell out technical
  tokens ("network dot json"), ~2–3 sentences (~20–30s) per slide. Fact Gate applies.
- Voice: edge-tts neural voices; default `en-US-AndrewMultilingualNeural` at rate -4%.
  Offer samples: `python scripts/build_narration.py --samples narration_script.md`
  writes one test line in Andrew/Ava/Brian for the user to audition. Only script
  text leaves the machine.
- Build: `python scripts/build_narration.py script.md slides_dir out.mp4
  [--voice V] [--lead 0.6] [--tail 1.0]` — per-slide TTS, measured durations size
  each slide's screen time (sync correct by construction), 1080p, concat.
- On report-video runs (see **Report-video mode** in Phase 1), the narration
  carries the reasoning of the report — definitions, evidence for and against,
  calibration — while slides stay visual. The Fact Gate applies unchanged: the
  spoken text may simplify but never add facts or numbers absent from the
  source doc.

## Phase 5 — Music

- Source, in preference order: (a) a track the user provides or names;
  (b) generate with Suno via Chrome (requires the user's logged-in Suno
  account); (c) if neither is available, deliver the narrated-only MP4 as the
  final output and tell the user music can be mixed in later with mix_music.py —
  never source music from random royalty-free sites without asking.
  Suno flow:
  suno.com/create → Simple mode → **check the model selector before generating**
  (top-right of the compose panel). It defaults to whatever was last used and is
  often an older tier; open it and pick the newest the account has — v5.5 Pro
  needs a subscription, so confirm rather than assume, and check the badges on
  existing library tracks to see which tiers the account can actually produce.
  Then toggle **Instrumental** → prompt like
  "Calm minimal ambient electronic underscore for a technology presentation. Warm
  analog synth pads, soft slow pulsing arpeggio, no drums, no vocals, instrumental
  only, 85 BPM" → Create (produces 2 variants, ~1–2 min).
  Download fallback (menus fail silently): read the row's `/song/<uuid>` link and
  fetch `https://cdn1.suno.ai/<uuid>.mp3` directly.
- Pick between variants objectively: `python scripts/mix_music.py --analyze a.mp3 b.mp3`
  → lower loudness-stddev (steadier) and longer duration win for a background bed.
- Mix: `python scripts/mix_music.py video.mp4 music.mp3 out.mp4 --bed-db -25`
  — auto-gains music to the target bed level, lowpass 10k, fade in/out, video
  stream copied untouched. Produce TWO versions by default: `--bed-db -25`
  (present; survives laptop speakers) and `--bed-db -35` (subtle) — users
  reliably ask for the other one.
- Verify: the script prints speech-region levels (peaks should sit at least
  10 dB above the bed). To also verify the bed level itself, pass
  `--gap-ss <t>` with a timestamp of a known music-only moment — e.g. a slide
  boundary: end of slide 1 = lead + slide-1 narration duration + a bit of tail
  (build_narration prints per-slide durations).

## Phase 6 — QA & deliver

- Extract 2–3 frames from the final MP4 and eyeball; confirm audio levels printed.
- Deliverables table: final.mp4 (+ soft-music variant), narrated.mp4 (no music,
  fallback), clean.pptx, narration_script.md, the two source docs. On research
  runs, also list: `run_manifest.json`, `research_brief.md`,
  `source_registry.md`, `evidence_matrix.md`, `research_checkpoint.md`, the
  preserved per-pass research reports, and any chart data files.
- Final QA on research runs: run `python scripts/validate_evidence.py <run-dir>`
  one last time (must be error-free) and walk the manual items of
  `## Audit checklist` in `references/research-quality.md`.
- The deck's bibliography slide must be present, and the web-researched
  provenance disclosure is repeated to the user in the deliverables
  conversation.
- Remind: re-exports from NotebookLM re-add the watermark → rerun Phase 3.
