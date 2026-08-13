# Visual style guide — authoring the Visual field of slide_division.md

Every **Visual** paragraph in `slide_division.md` is a literal image prompt:
Gemini Notebook's generator renders it, and the Fact Gate later reviews the
result against it. This guide makes those visuals interesting AND correct,
and keeps generic AI imagery out of the deck. It applies to every run, both
source-grounded and topic-only.

Grounding: assertion-evidence slide research (Alley, Penn State — slides
built as a claim + visual evidence measurably beat bullet slides for
comprehension), the glance test (Duarte — a slide must land in ~3 seconds),
signal-to-noise (Reynolds), and the data-ink ratio (Tufte).

## The three laws

1. **Assertion-evidence.** The slide's Data field states a claim; the Visual
   is EVIDENCE for that claim — never decoration. Before writing a Visual,
   ask: what would make this claim *visible*?
2. **One idea, three seconds.** One idea per slide, readable at a glance
   from the back of the room. If the Visual needs study, split the slide.
3. **Signal over noise.** Every visual element must either encode something
   from the Data field or set tone deliberately (declared in the style
   block). If deleting an element loses nothing, delete it.

## The global style block (declare once, repeat everywhere)

At the top of `slide_division.md`, before slide 1, write a
`**Global visual direction:**` block that fixes, for the whole deck:

- background value (e.g. near-black editorial dark, or warm paper light);
- one or two neutrals + ONE accent color, and the accent's MEANING — the
  accent marks the single thing that matters on each slide, nothing else;
- typography mood (e.g. large light serif for quotes, small mono for data);
- rendering style (e.g. "flat matte, vector-like, no gloss, no 3D");
- the standing bans (see the fluff list below), stated explicitly so the
  generator prompt inherits them.

Then every Visual paragraph reuses the same vocabulary ("dark field", "the
warm accent") instead of re-inventing colors per slide. Consistency across
slides is the single highest-leverage trick: it makes sixteen generated
images read as one designed deck. The shipped example
(`examples/karpathy-three-months/slide_division.md`) demonstrates this
pattern end to end.

Rule: at most ONE accented element per slide. The accent is a semantic
highlight, not a theme color.

## Banned: the AI-fluff list

Never put these in a Visual prompt, and kill them on sight during slide
review. They are the statistical average of the training data — technically
competent, instantly forgettable, and they mark the deck as machine-made:

- glowing brains; circuit-board heads; humanoid robots (unless the topic IS
  a specific robot — then describe that robot concretely); robot–human
  handshakes;
- generic isometric 3D clip-art scenes; purple-teal or orange-teal gradient
  "tech" backgrounds; lens flares; bokeh sparkles; soft fog glow;
- floating holograms and HUDs; digital rain; padlock-and-shield for
  "security"; light bulb for "idea"; gears for "process"; rocket for
  "growth"; puzzle pieces for "integration"; chessboard for "strategy";
- stock-photo humans: smiling teams pointing at screens, suited handshakes;
- prompt filler like "cinematic, ultra-detailed, epic, 8k" — these words
  summon the crowd's default image.

The portability test: if the visual would fit an unrelated deck unchanged,
it is fluff. A good visual only makes sense for THIS slide's claim.

## Correctness rules (what keeps the Fact Gate quiet)

- **No generator-rendered words or numbers.** Image models garble text and
  invent digits. Words belong in the Data field (slide text); numbers belong
  on a DATA CHART. If an in-image label is unavoidable (a timeline axis),
  keep it to at most 3 short labels and expect the Fact Gate to zoom and
  read every one.
- **Sizes and positions may encode data only when the numbers are sourced.**
  Then say them: "circle at 19 May roughly twice the diameter of the 23 June
  circle" — never "sized by importance".
- **Say "generic, unbranded"** for any product, car, phone, or device;
  generators default to real brands, and the Fact Gate rejects them.
- **Avoid people, faces, and hands** unless the story requires them; when
  required, keep them distant, silhouetted, or cropped — close anatomy is
  artifact-prone.
- **State what each element encodes** inside the Visual paragraph ("steps
  2–6 dim and blurred, step 1 sharp in the accent with a stop-bar = everyone
  says start here, skip the rest"). That sentence is what the reviewer
  checks the rendered image against.

## Category playbook

### DIAGRAM (flow / architecture / timeline)

- At most 7 elements, one flow direction (left→right or top→bottom).
- Spell out the geometry: "three rounded boxes left to right, single arrows
  between them" — never "a diagram of the architecture".
- Stage names come verbatim from the source doc; put them in slide text
  where possible. In-image labels are allowed but each one is Fact-Gate
  verified after rendering.
- Prefer position, size, and connection as the encodings; icons rarely earn
  their place.

### DATA CHART (quantitative)

- Rendered deterministically from a local data file — never by the image
  generator (see `## DATA CHART requirements` in
  `references/research-quality.md` for the provenance fields).
- One message per chart, and the Data field states it as a sentence.
- Direct-label the series on the plot; avoid legends where possible. No 3D,
  no dual axes, no pies beyond 4 slices (prefer sorted bars). Bar-chart
  value axes start at zero. Time series → line; comparisons → sorted bars.
- Grey everything, accent the one series or point that carries the message;
  the render code takes ALL its colors from the style block (deck
  background, one neutral, the accent) — never matplotlib/plotly defaults,
  or the chart reads as pasted-on instead of part of the deck.

### Illustration

- Concrete beats abstract: an object or scene from the actual story
  outperforms a metaphor ("a stack of text posts compressed to thin
  horizontal lines, seen edge-on" beats "a concept of communication").
- Abstract-geometric compositions — line fields, grids, edge-on timelines,
  large flat color planes in the deck's own palette — are the safest way to
  be visually interesting: no garbled text, no uncanny anatomy, strong at a
  glance.
- **Typography-as-image** (a full-bleed quote or a single huge number with
  enormous margins) is often the strongest slide in the deck; use one or
  two. These ARE rendered text, so keep them short and have the Fact Gate
  read every word and digit.
- Metaphor is allowed only when the mapping is stated in the paragraph; an
  unstated metaphor is decoration.

## Driving NotebookLM to pretty slides (house-style countermeasures)

NotebookLM composes the whole slide — layout, type, and artwork — from your
text. Left unsteered it has a house style, and the house style is the main
reason decks come out "not pretty". Observed tells and their countermeasures
(verified on a real 13-slide run, 2026-08-13):

- **Monochrome wash.** With no accent declared, everything renders pale
  blue-on-navy at one value — no hierarchy, nothing pops. Countermeasure:
  the style block NAMES one accent family ("warm amber", "electric coral")
  and says everything else stays monochrome; each slide's Visual names the
  ONE element that gets it.
- **Schematic garnish.** Style words like "technical", "scientific",
  "blueprint", "schematic", "HUD" summon frame borders around the slide,
  corner crosses, tick clusters, measurement marks, dashed boxes, particle
  speckles, and smudged micro-text debris at the edges. Countermeasure:
  never use those style words; use "minimal editorial", "flat matte",
  "generous whitespace"; AND append the explicit ban (next bullet).
- **The standing ban line** — include it verbatim in the style block and in
  the deck-generation prompt: "No frame or border around the slide, no
  corner crosses, no tick marks, no measurement marks, no scattered
  speckles or particle dust, no dashed outline boxes, no stray small text
  or numbers at the edges, no gradients inside shapes — flat solid fills."
- **Rainbow text and rainbow boxes.** Multi-item lists come back with each
  item's border a different color and words colorized mid-sentence.
  Countermeasure: "all body text in a single soft-white; all boxes share
  one neutral outline; color marks meaning only" — and never write a Visual
  that asks for "a different colour per item".
- **Wall-to-wall layouts.** Dense Data fields produce zero-whitespace
  slides. Countermeasure: demand "at least one third of the slide empty"
  and name a single hero element per slide; move detail to narration.
- **DATA CHART palette drift.** Locally rendered charts default to
  matplotlib grey/blue/orange and look pasted-on. Countermeasure: the chart
  render code takes its colors FROM the style block — deck background, one
  neutral for context series, the accent only on the message; soft-white
  labels; no default palettes.

Carry the style INTO generation: the Phase 2 outline-paste prompt includes
the Global visual direction block verbatim (see the SKILL.md Phase 2
template). Slides styled per-slide without a deck-level style paragraph will
not cohere, no matter how good each Visual is.

## The Revise aesthetics pass

Revise is not only for fact fixes — run TWO passes over the generated deck:

1. **Content pass (Fact Gate):** numbers, names, orders, garbled text,
   brands — fix, regenerate, re-audit. This pass comes first; there is no
   point beautifying a slide whose content will change.
2. **Aesthetics pass:** walk every slide against this guide and batch
   visual-only Revise instructions. Write them as concrete deltas, 1-3 per
   slide, naming what to remove / recolor / resize — never "make it
   prettier":
   - "Remove the frame, corner crosses, tick marks and speckles; clean
     solid background."
   - "Make all five boxes the same slate-grey outline; recolor only box 3
     to the warm amber accent."
   - "Set all body text in one soft-white; remove the multicolored words."
   - "Enlarge the headline; add empty margin around the diagram."
   Batch them under Pending changes, regenerate once, then re-run the
   CONTENT check on every revised slide (Revise can alter text while
   restyling). Two aesthetics rounds is the norm; stop when the deck passes
   the glance test, not when it is perfect.

## Deck-level rhythm

- Vary the species: never three consecutive slides of the same category. A
  strong deck alternates diagram / chart / typography / illustration.
- The cold open and the takeaway slide get the boldest treatment (full-bleed
  typography or the deck's single most striking composition).
- Report-video decks: the measurement-dashboard beat is DATA CHART
  territory; the evidence-for and evidence-against beats work well as
  mirrored compositions (same layout, accent swapped side).

## Writing the Visual paragraph — formula

`**CATEGORY.** [style-block tag] + [composition: what, where, how sized] +
[what each element encodes] + [negative constraints if the subject is
risky]` — 40–90 words.

Good (from the shipped example): "**DIAGRAM.** A clean horizontal timeline
spanning May to August, with circular markers sized proportionally to
engagement. One markedly larger circle sits at the 19 May position; a
second, slightly smaller, at 23 June. Axis labelled by month only. Flat
vector, dark background, warm accent for the two largest markers."

Bad: "A glowing brain with circuit patterns representing AI progress,
cinematic 8k" — decoration not evidence, banned cliché, portability-test
failure, style filler, nothing encoded.
