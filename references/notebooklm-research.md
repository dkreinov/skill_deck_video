# Gemini Notebook (formerly NotebookLM) — research operations

This is the deck-video skill's operating reference for research inside Gemini
Notebook. It covers notebook lifecycle, the multi-pass Deep Research protocol,
the UI recipe for running research, how to preserve results before Google
discards them, which synthesis surface to use for which job, and the
source-selection discipline that keeps provenance clean.

Button labels and DOM selectors documented here are versioned adapters and are
expected to churn. UI drift alone is never a reason to abandon a run: use the
documented fallback, record it in `run_manifest.json`, and continue.

## Notebook lifecycle

For every new video project:

1. Open Gemini Notebook (formerly NotebookLM).
2. Create a completely NEW notebook.
3. Name it using:

   ```text
   YYYY-MM-DD — <topic-slug> — deck-video
   ```

4. Verify the notebook contains no sources from another project.
5. Record the notebook URL/identifier in `run_manifest.json`.

Reuse an existing notebook ONLY when the user explicitly says this continues
that project.

Rationale: a fresh notebook prevents cross-project source contamination,
stale instructions carried over from an earlier run, and accidental reuse of
earlier generated notes as if they were new evidence.

## Multi-pass Deep Research protocol

Run all passes inside the same fresh notebook. Always run the first two
passes (A and B). Add Pass C when the approach or subject benefits from it.
Add Pass D only after the evidence matrix exists.

### Pass A — Landscape and baseline

Map definitions, observable measurements, schools of thought, existing
forecasts, and important sources. Do not seek or record a conclusion yet —
this pass is purely for coverage.

### Pass B — Adversarial and falsification

Search explicitly for:

- the strongest evidence against the emerging thesis;
- failed predictions;
- benchmark limitations;
- contrary measurements;
- replication failures;
- physical, economic, regulatory, and organizational bottlenecks;
- conflicts of interest and source dependence.

### Pass C — Non-obvious indicators / selected editorial lens

Search for weak signals and second-order effects not usually included in
mainstream summaries. A sci-fi or fringe frame may be investigated as a
selected editorial lens, but keep any such claims in a separate evidence
class from mainstream/measured evidence — never blend them silently.

### Pass D — Gap closure

Run only after the evidence matrix has been constructed. Issue focused
queries only for unresolved, high-impact gaps identified by that matrix.
Never run another generic search under the label of Pass D.

## Starting Deep Research (UI recipe)

For each pass:

1. Open the Sources panel.
2. Add a source.
3. Select Web.
4. Select Deep Research.
5. Paste the complete pass-specific query.
6. Start the search and poll in the background.
7. Continue only when the result view shows the report and source list.

Use Fast Research only as a fallback: when Deep Research is unavailable, or
when a targeted gap needs a small number of additional sources rather than a
full pass. Record the fallback and the reason it was used.

## Preserve results before closing

Google's current behavior: Deep Research displays the generated report plus
relevant CITED and UNCITED sources, and any results not imported are
DISCARDED when the Deep Research result view closes.

Therefore, before closing the result view:

1. Open the full result view.
2. Capture the report text and its citation mapping.
3. Capture the complete result inventory: title, URL, description,
   cited/uncited status, and import status.
4. Default to **Import all results** before closing the result view.
5. Deselect only obvious duplicates, inaccessible items, malformed results,
   or clearly irrelevant sources — and only once the inventory has already
   been preserved outside the deselection step.
6. If account source limits force a partial import, prioritize, in order:
   1. the Deep Research report;
   2. primary sources cited by the report;
   3. independent counter-sources;
   4. data and benchmark sources;
   5. the best secondary syntheses.
7. Record every omitted result and the reason it was omitted.

Motto: import broadly first, curate second. Do not risk losing an undisclosed
result merely to keep the notebook visually tidy.

### What to preserve locally

Always preserve locally:

- the full Deep Research report from every pass;
- the citation markers and citation-to-source mapping;
- the complete source inventory;
- the final curated source registry;
- exact quotations, tables, and figures used by the final narrative.

Do NOT bulk-download every webpage or file returned by research. Instead:

- download or snapshot only the sources supporting a central claim;
- download primary PDFs, papers, datasets, benchmark documentation, system
  cards, and official reports actually used in the video;
- retain URL and metadata only for unused candidate sources;
- never bypass paywalls or access controls;
- mark sources that could not be preserved locally.

## Synthesis surfaces

Gemini Notebook offers several synthesis surfaces. Assign each one a precise
role — do not treat any of them as interchangeable with the agent's own
authored synthesis.

- **Deep Research reports** — discovery and leads only. Never authoritative
  evidence.
- **Auto-generated source summaries** — orientation only, used to decide
  whether a source deserves closer inspection. Never cited when the original
  source is available.
- **Chat with explicitly selected sources** — targeted evidence work: extract
  atomic claims with citations; locate exact quotes, tables, and figures and
  their caveats; compare sources; find disagreement and missing evidence; ask
  what evidence contradicts a proposed claim; distinguish observation,
  interpretation, forecast, and speculation. Save valuable chat responses to
  notes to keep their inline citations, but a saved response is still
  generated material and must still be checked against its cited source.
- **Studio Reports** (Briefing Document / custom Report) — an optional second
  synthesis, useful for a coverage check, an alternative organization of the
  evidence, a candidate outline, or a comparison against the agent's own
  synthesis. Never used as `notebooklm_source.md` without claim-level
  verification.

THE AGENT writes the final synthesis. `notebooklm_source.md` comes from the
verified evidence matrix; NotebookLM helps retrieve and compare evidence but
never silently chooses the thesis.

## Source-selection isolation

The notebook accumulates raw Deep Research reports, imported sources, saved
notes, and the authored control docs (`research_brief.md`,
`notebooklm_source.md`, `slide_division.md`) side by side. Without selection
discipline, generated artifacts can end up citing other generated artifacts,
creating circular provenance.

Apply these selection rules:

| Operation | Sources selected | Sources excluded |
|---|---|---|
| Evidence extraction | Original curated sources | Deep Research reports, saved summaries, authored control docs |
| Contradiction analysis | Relevant original sources from opposing positions | Authored narrative and slide outline |
| Coverage check | Curated original sources + evidence matrix | Slide-generation artifacts |
| Slide generation | Only `notebooklm_source.md` and `slide_division.md` | Raw research reports, web sources, notes, earlier deck artifacts |

Before slide generation, explicitly verify the source checkboxes match the
"Slide generation" row above. This is a HARD GATE — do not proceed on the
assumption that the right sources are already selected.

## UI adapter (verified 2026-08-12)

- Deep Research runs in the background for minutes and produces a cited Deep
  Research Report importable together with the sources it found.
- Some found sources may be paywalled or otherwise unusable — that is
  normal; keep the usable ones.
- Fast Research is the quicker "Discover sources"-style fallback for when
  Deep Research is unavailable.
- Source upload has no `<input type=file>` in the DOM until the native file
  picker opens, so automation cannot drive it directly. Use the Copied-text
  path instead: find the textarea, set the full document text into it, and
  click Insert. Paste each doc as its own source.
- Automation-initiated export downloads are blocked by Chrome: the click
  fires the export request but the download is blocked, leaving blank
  `about:blank` tabs with no file landing in `~/Downloads`. The download
  click belongs to the USER — leave the artifact menu open and hand the
  click to them.
- If elements have moved or a step 404s, fall back to the manual gate rather
  than fighting the UI.
