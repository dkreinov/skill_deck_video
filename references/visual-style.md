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

- one named visual genre for the whole deck;
- background value (e.g. near-black editorial dark, or warm paper light) —
  hex codes beat adjectives;
- one or two neutrals + ONE accent color, and the accent's MEANING — the
  accent marks the single thing that matters on each slide, nothing else;
- typography mood (e.g. large light serif for quotes, small mono for data);
- rendering style (e.g. "flat matte, vector-like, no gloss, no 3D");
- the standing bans (see the fluff list below), stated explicitly so the
  generator prompt inherits them;
- the closing line "Keep this style identical across all slides."

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
  large flat color planes in the deck's own palette — are the SAFE option:
  no garbled text, no uncanny anatomy, strong at a glance. Safe is not the
  same as good. A deck built only from hairlines, ticks and rules is
  correct and forgettable; use them for the connective slides, not for all
  of them.
- **Typography-as-image** (a full-bleed quote or a single huge number with
  enormous margins) is often the strongest slide in the deck; use one or
  two. These ARE rendered text, so keep them short and have the Fact Gate
  read every word and digit.
- Metaphor is allowed only when the mapping is stated in the paragraph; an
  unstated metaphor is decoration.

## NotebookLM: style is set ONCE, in the generation prompt

Slides render as finished images; there is no post-hoc theming. "Any design
direction you don't put in the prompt is design direction you don't get."
Google officially supports full aesthetic direction in the customization
prompt — their own examples include a chalkboard design with colored chalk
text and brand styling pulled from an uploaded brandbook. The Global visual
direction block therefore IS the style paragraph of the Phase 2 generation
prompt (the SKILL.md template pastes it verbatim). Write it to be obeyed:

- Name ONE coherent visual genre ("minimal editorial", "blackboard",
  "modern newspaper", "constructivist poster") — never two; mixed visual
  languages fragment the deck.
- Prefer exact values over adjectives: hex codes for background / neutral /
  accent, a named font family or type mood, quantified emphasis when it
  matters ("headline 10x body size").
- ONE accent color with a stated meaning, and explicit bans — the model
  obeys prohibitions ("no gradients, no shadows, no frames or border
  decoration, no clip-art").
- End with: "Keep this style identical across all slides."
- Add: "Reference only concepts explicitly present in the sources."
- Brand deck? Upload the brandbook / style guide as a notebook source and
  point the prompt at it.

The division of labor that keeps a deck coherent (confirmed by comparing a
good and a poor real run side by side):

- **Deck-level prompt** — ALL palette, typography, mood, and bans live here.
- **Per-slide Visual** — a short, positive, concrete SCENE: what to draw
  and what it encodes (25-60 words). Reuse the style block's vocabulary
  ("the accent"); never assign new colors per slide and never stack
  negatives per slide — per-slide art direction is how a deck ends up
  looking like thirteen different decks.
- **Data field** — thin. On-slide text density tracks what you put in Data,
  not the "keep text minimal" instruction; long evidence bullets come back
  as wall-to-wall text. Move detail to narration.
- **DATA CHART replacements** — locally rendered charts draw from the same
  style block (background, neutral, accent), or the deck alternates between
  two visual systems.

## Revise: per-slide fixes for concrete defects

Revise (pencil icon on the deck) opens a per-slide instruction box;
instructions batch under "Pending changes" and apply with one "Generate
revised deck". Use it for CONCRETE defects found in review:

- a wrong or invented number, name, or order — state the correct value
  verbatim in the instruction, because revisions do NOT consult the
  notebook sources;
- an image that missed its Visual spec or drew a banned element;
- garbled or unwanted words inside artwork; brand lookalikes;
- a specific visual delta ("remove the border decoration on this slide",
  "make only the third box the accent color").

Mechanism facts to plan around: every revision pass regenerates the WHOLE
deck — batch all slide instructions into as few passes as possible, and
re-check untouched slides after each pass (they can shift). Revise cannot
add or remove slides. If the same style fault appears on every slide, the
generation prompt was wrong: fix the prompt and regenerate the deck once
rather than fighting it slide by slide. Last resort for a single stubborn
slide: capture it, edit the image outside NotebookLM, and substitute it in
the rebuilt PPTX — the same path the DATA CHART replacements use.

## Visual register (asked at Phase 0)

The Phase 0 intake asks how visually ambitious the deck should be. The
register moves three things only: the share of slides carrying a picture,
how ambitious those pictures are, and the style vocabulary. It NEVER moves
the Fact Gate, the DATA CHART rules, the anti-cliche bans, or the
no-generator-rendered-numbers rule.

| Register | Pictures | Typography-only | Character |
|---|---|---|---|
| paper | 0-15% of slides | up to 1/3 | working paper: type, charts, hairline diagrams; the deck the numbers would write for themselves |
| editorial (default) | >= 1/3 | up to 1/3 | magazine: a real picture per act, strong type, charts where numbers matter |
| evocative | >= 1/2 | up to 1/4 | documentary film: pictures carry the feeling of the subject, scale contrasts, one showpiece slide |

Record the chosen register in `run_manifest.json` (`intake.answers`) and
name it in the deck's Global visual direction block, because it changes what
the generation prompt should ask for.

### What "wonder" is allowed to mean

Evocative does not mean science fiction, and it is not a licence to reopen
the banned-fluff list. The rule:

**Wonder comes from the real at scale, never from the imagined.**

The awe in a serious subject lives in physical fact — the size of the
infrastructure, the smallness of the feature, the length of the timescale,
the density of the thing nobody pictures. So: a cooling hall receding into
the dark; a transformer yard at dusk; a wafer stepper's optics; a queue of
identical racks; a coastline of turbines; the night side of a continent lit
by load. Never: a glowing brain, a humanoid robot, a hologram, a neon
"digital future" cityscape. Those are imagined wonder, and they read as
slop precisely because they are.

Three levers make a real image feel large: **scale contrast** (a person-sized
object against a landscape-sized one), **light** (a single source in a dark
field, dawn, sodium, screen glow), and **depth** (something receding past
where the eye can resolve it). Name at least one of them in the Visual
paragraph.

The register also sets how much of the deck is showpiece: at evocative,
pick ONE slide — usually the cold open or the verdict — and give it the
deck's most ambitious image.

## The variety floor: earn the images

The banned-fluff list says what not to draw. It is not a licence to draw
nothing. An abstract subject (a trend, a risk, a definition) is exactly the
case where a reader needs something to look at, and "no imagery at all" is
the failure mode this guide must prevent as firmly as the glowing brain.

Minimum for any deck of ~10+ slides, at the DEFAULT editorial register
(paper and evocative shift the first two numbers per the register table):

- **At least a third of the slides carry a real picture** — a scene, an
  object, a place, a process rendered as something you could photograph or
  draw, not a hairline abstraction. Charts, tick-marks, rules, arrows and
  pure typography do NOT count toward this third.
- **At most one third pure typography** (large-type quote or verdict
  slides). Two or three in a 13-slide deck is plenty.
- **No three consecutive slides without a picture** (all registers,
  including paper).

"Evidence, not decoration" governs WHAT an image shows, not whether an
image exists. An image is evidence when it makes the claim legible: the
concrete instance behind an abstraction (the actual bottleneck: a
substation, a transformer yard, a cooling hall), the physical object a
number describes, the scene a scenario would look like. It is decoration
when any deck could use it.

Finding a picture for an abstract claim — the drill:

1. Name the most concrete noun in the claim. "Compute is constrained" →
   transformers, substations, cooling. "Automation of research" → a bench,
   a terminal, a queue of experiments.
2. Put that noun in a real place, at a stated scale, with the deck's
   palette and lighting: "a row of grid transformers behind chain-link at
   dusk, seen from a low angle, near-black sky, the deck's amber only in
   the sodium lamps."
3. Say what the picture encodes ("the queue is the wait, not the machine").
4. Add the risky-subject constraints (generic/unbranded, no readable text,
   no faces) — the same specificity that avoids stock clichés is what makes
   the image striking.

If a scene genuinely cannot be found for a claim, that slide is a
typography or diagram slide — but the deck as a whole must still clear the
floor above.

## Deck-level rhythm

- Vary the species: never three consecutive slides of the same category. A
  strong deck alternates diagram / chart / typography / illustration, and
  clears the variety floor above — count the categories before generating.
- The cold open and the takeaway slide get the boldest treatment (full-bleed
  typography or the deck's single most striking composition).
- Report-video decks: the measurement-dashboard beat is DATA CHART
  territory; the evidence-for and evidence-against beats work well as
  mirrored compositions (same layout, accent swapped side).

## Writing the Visual paragraph — formula

`**CATEGORY.** [style-block tag] + [composition: what, where, how sized] +
[what each element encodes] + [a negative constraint only if the subject is
risky]` — 25–60 words, positive scene description. Style, palette, and the
standing bans live in the deck-level prompt, not here.

Good (from the shipped example): "**DIAGRAM.** A clean horizontal timeline
spanning May to August, with circular markers sized proportionally to
engagement. One markedly larger circle sits at the 19 May position; a
second, slightly smaller, at 23 June. Axis labelled by month only. Flat
vector, dark background, warm accent for the two largest markers."

Bad: "A glowing brain with circuit patterns representing AI progress,
cinematic 8k" — decoration not evidence, banned cliché, portability-test
failure, style filler, nothing encoded.

## Sources

Slide-design research: Alley's assertion-evidence studies (Penn State),
Duarte's glance test, Reynolds' signal-to-noise, Tufte's data-ink ratio.
NotebookLM specifics: Google's Slide Deck help
(support.google.com/notebooklm/answer/16757456) and "8 ways to make the
most of Slide Decks" (blog.google), which document aesthetic direction in
the customization prompt and brandbook-as-source; community prompt
libraries (github.com/serenakeyitan/awesome-notebookLM-prompts,
sabrina.dev, excellentprompts.substack.com) for hex-over-adjectives,
named-genre recipes, and the identical-across-slides directive; Revise
mechanics per Google help and 2026 practitioner guides. Division-of-labor
rules confirmed by a side-by-side comparison of two real runs of this
skill (one coherent, one fragmented).
