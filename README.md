# deck-video — a Claude Code skill for fact-checked decks & narrated videos

Turn a topic + trusted sources into a **fact-checked slide deck** (generated via
Google NotebookLM / Gemini Notebook) and a **narrated MP4 with a music bed** —
with an adversarial fact gate standing between the generator and the deliverable.

Built with and for [Claude Code](https://claude.com/claude-code). The whole
pipeline is driven by the agent; the deterministic steps are plain-Python
scripts bundled here.

## What it produces

| Artifact | Description |
|---|---|
| `notebooklm_source.md` | Full factual narrative, every claim traced to a fetched source |
| `slide_division.md` | Per-slide spec: Data (what's on the slide) + Visual (image/diagram prompt) |
| Deck (PPTX) | NotebookLM-generated slides, fact-gated, watermark-free, rebuilt locally |
| `*_narrated.mp4` | Neural-TTS narration, per-slide timing measured (sync by construction) |
| `*_final.mp4` | Narrated video with an auto-gained music bed |

See a complete real run in [`examples/karpathy-three-months/`](examples/karpathy-three-months/) —
a deck + video built from Andrej Karpathy's public posts (summer 2026), including
the pipeline's intermediate documents and the fact-gate verdict table.

## Why this exists

AI slide generators produce beautiful slides that confidently lie: invented
"85% faster / 10X" metrics, garbled words rendered inside images, "identical"
panels showing different values, mislabeled diagrams. This skill treats those
as first-class defects:

- **Fact Gate** — every number, name, stage order, and even *text rendered inside
  generated images* is verified against the source documents. No-unsourced-numbers
  is a hard rule; anti-hallucination constraints are baked into the generation
  prompt itself.
- **Audit-first, download-last** — slides are reviewed and revised *in* NotebookLM
  (via browser automation screenshots) before anything is exported.
- **Everything local** — watermark removal, PPTX assembly, TTS, and audio mixing
  run on your machine. Confidential source material never touches third-party
  converter sites.

## Install

Copy this repo into your Claude Code skills directory:

```
~/.claude/skills/deck-video/        # SKILL.md + scripts/
```

One-time Python prerequisites (ffmpeg ships inside imageio-ffmpeg):

```
pip install pymupdf opencv-python numpy edge-tts imageio-ffmpeg
```

Then, in any Claude Code session:

```
/deck-video <topic>, sources: <urls or files>, auto mode, ~N slides
```

Optional, for **auto mode** (agent drives NotebookLM end-to-end):
- [Claude in Chrome](https://claude.ai/chrome) extension connected
- Logged into NotebookLM in that Chrome profile
- A Suno account if you want generated background music (a no-music fallback exists)

## The pipeline

```
Phase 0  Brief            one question round: audience, delivery mode, scope
Phase 1  Research         drill sources two levels deep, extract verbatim, coverage check
         Author           notebooklm_source.md + slide_division.md
Phase 2  Generate         NotebookLM Slide Deck; outline pasted verbatim into the prompt
         Audit → Revise   per-slide fact gate on screenshots; batch revisions; re-audit
         Capture          slide images extracted at native resolution (no export needed)
Phase 3  Clean            watermark inpainted locally (OpenCV)
         Rebuild          build_pptx.py assembles a real PPTX from the images
Phase 4  Narrate          spoken-register script → edge-tts; measured durations set timing
Phase 5  Music            analyze candidate tracks, auto-gain to a bed level, mix
Phase 6  QA               frames + audio levels verified; deliverables listed
```

### Scripts (usable standalone, no skill required)

| Script | Purpose |
|---|---|
| `scripts/render_review.py` | Deck (pptx/pdf) → per-slide PNGs for review |
| `scripts/clean_watermark.py` | Inpaint the NotebookLM watermark locally |
| `scripts/build_pptx.py` | N slide images → valid PPTX (no dependencies, bundled template) |
| `scripts/build_narration.py` | Narration markdown + slide PNGs → narrated 1080p MP4 |
| `scripts/mix_music.py` | Mix/duck a music bed under narration; `--analyze` picks the steadier track |

## Notes & limitations

- NotebookLM's slide decks render as one image per slide — text is not editable
  post-export. All content fixes go through NotebookLM's Revise, which this
  skill automates.
- The browser-automation recipes match NotebookLM's UI as of mid-2026; UI drift
  is expected and the skill documents a manual fallback for every automated step.
- Watermark removal is intended for your own generated content. NotebookLM's
  official watermark-free export is a Google AI Ultra feature.
- Music generated with Suno is subject to Suno's terms for your account tier.

## Example

[`examples/karpathy-three-months/`](examples/karpathy-three-months/) contains a
full run on public material: source narrative, slide division, narration script,
the fact-gate review table, the final PPTX, and the narrated video with music.
