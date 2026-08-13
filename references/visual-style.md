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

The Phase 0 intake asks how visually ambitious the deck should be:

- **paper** — sober working-paper look: type, charts, diagrams; pictures rare.
- **editorial** (default) — real pictures from the subject's world alongside
  the charts and type.
- **evocative** — imagery carries the subject's atmosphere on most slides,
  with ONE showpiece slide (usually the cold open or the verdict).

The register changes only how much the deck shows — never what counts as
true. Fact Gate, DATA CHART rules and the cliché bans are identical in all
three. Record the choice in `run_manifest.json` and name it in the Global
visual direction block, because it changes what the generation prompt asks
for.

## The subject dictates the imagery

Visuals come from the topic's own world. A deck about the singularity may
look futuristic; a deck about a deployment pipeline looks like
infrastructure; a history deck looks like its period. The imagery should
feel like the subject — not like "a presentation".

Each image earns its slide by being part of the explanation: it depicts the
thing a claim is about, or it makes the argument visible. The sharpest case
is a skeptical deck: a claim about hype can SHOW the hype — the glossy
imagined AI future on one half, the mundane real thing (a data-center
aisle, a benchmark table) on the other, and the contrast IS the argument.
Used that way, even the banned clichés are legitimate: the fluff list bans
them **as decoration**, not **as the exhibit under discussion** — when the
slide is about the imagined future, depicting the imagined future (clearly
framed as the imagined view) is explanation, and often the most interesting
slide in the deck.

Keep something to look at on most slides. Pure typography is for a few
verdict or quote moments — never several text-only slides in a row, in any
register. When writing a picture for an abstract claim: name the most
concrete noun in the claim, put it in a real place at a stated scale in the
deck's palette, and say what it encodes.

## Deck-level rhythm

- Vary the species: never three consecutive slides of the same category. A
  strong deck alternates diagram / chart / typography / illustration —
  count the categories before generating.
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
