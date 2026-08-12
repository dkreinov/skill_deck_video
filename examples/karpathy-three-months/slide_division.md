# Slide Division — Karpathy on X, May–August 2026

16 slides. Audience: AI/ML practitioners. Framing: greatest hits — individual
posts, quoted, with context. Every figure below traces to `notebooklm_source.md`.

**Global visual direction:** dark editorial palette, near-black background,
one warm accent. Generous whitespace. Quotes are the hero element — set large,
in a serif face, with the date and engagement figures small and secondary.
No stock-photo people, no robot imagery, no brain-with-circuits clichés.
No recognizable third-party logos or brand marks anywhere. No depictions of
copyrighted fictional characters.

---

## Slide 1 — Title

**Data:**
- Title: Three Months of Karpathy
- Subtitle: What @karpathy posted on X, 12 May – 12 August 2026
- Footer: 28 posts · sourced directly from X

**Visual:** Abstract dark field of thin horizontal lines of varying length and
opacity, suggesting a stack of text posts compressed to pure rhythm — a timeline
seen edge-on. One line glows in the warm accent, sitting slightly proud of the
rest. No text inside the illustration.

---

## Slide 2 — The window at a glance

**Data:**
- 28 posts between 12 May and 12 August 2026
- Both top-level posts and replies
- Most-liked: 149,750 likes — the Anthropic announcement, 19 May
- Most-viewed: 8,140,553 views — the LLM UI/UX post, 23 June
- Engagement figures captured 12 August 2026 and will drift

**Visual:** **DIAGRAM.** A clean horizontal timeline spanning May to August, with
circular markers sized proportionally to engagement. One markedly larger circle
sits at the 19 May position; a second, slightly smaller, at 23 June. Axis labelled
by month only. Flat vector, dark background, warm accent for the two largest
markers, muted grey for the rest.

---

## Slide 3 — "I've joined Anthropic"

**Data:**
- 19 May 2026 · 149,750 likes · 27,909,958 views
- Quote: "Personal update: I've joined Anthropic. I think the next few years at the frontier of LLMs will be especially formative. I am very excited to join the team here and get back to R&D. I remain deeply passionate about education and plan to resume my work on it in time."
- Roughly 3× the likes of anything else in the window
- Education deferred, not abandoned

**Visual:** Full-bleed quote slide. The words set very large in a light serif,
centred, with enormous margins. Beneath, in small mono type, the date and the two
engagement figures. No illustration at all — the scale of the numbers is the image.

---

## Slide 4 — Stuck on step 1

**Data:**
- 18 May 2026 · 1,992 likes · 218,965 views — the day before the announcement
- Quote: "I was recording my nanochat video when I realized that 'first boot up an 8XH100 from your favorite provider!' would instantly get everyone stuck on step 1 of the video"
- The friction that makes frontier-scale teaching hard

**Visual:** A numbered vertical list of tutorial steps rendered as simple
rounded bars, steps 2 through 6 in dim grey and slightly blurred, step 1 in sharp
warm accent with a small barrier or stop-bar drawn across it. Conveys "everyone
halts at the first instruction" with no text inside the graphic.

---

## Slide 5 — Fable 5: benchmarks vs. feel

**Data:**
- 9 June 2026 · 25,645 likes · 3,044,871 views
- "the same underlying model as Mythos but with added safeguards"
- SOTA "on everything by a margin" — but the point is the qualitative jump
- "a major-version-bump-deserving step change forward (imo of the same order as Claude 4.5 was in November)"
- Strongest on "long problem-solving sessions on very difficult problems"
- Candid caveats: "still has quirks"; safeguards "a little too trigger happy for launch"
- "it's never felt this tempting to stop looking at the code at all (but don't do this in prod!)"

**Visual:** Two vertical panels side by side. Left: a conventional bar chart of
benchmark scores, drawn small, neat and grey — deliberately unremarkable. Right:
a single continuous ascending curve in the warm accent, thick and smooth,
occupying far more visual weight. The composition argues that the felt step change
outweighs the benchmark table. No numbers or labels inside either panel.

---

## Slide 6 — Jevons paradox for software

**Data:**
- Same post, 9 June 2026
- Quote: "I feel a lot of things changing as working software increasingly comes out on a tap. The Jevon's paradox kicks in and I feel my own demand for software growing substantially."
- What becomes worth building: explainers, visualizers, dashboards, bespoke single-use apps, 10X test suites, auto-optimized code
- His example: "a full wandb that is hyper-specific just for your project"
- Cheaper to produce ⇒ more produced, not less

**Visual:** **DIAGRAM.** A tap or spigot at upper left in simple line art, from
which falls not water but a widening cascade of small rectangles — software
artifacts — that multiply as they descend and fill the lower two-thirds of the
frame. Density increases downward. Warm accent for the cascade, thin white line
art for the tap. No text inside.

---

## Slide 7 — The third redesign of LLM UI/UX

**Data:**
- 23 June 2026 · 23,317 likes · 8,140,553 views — his most-viewed post of the window
- Paradigm 1: the LLM is a website you go to
- Paradigm 2: an app you download to your computer
- Paradigm 3: "a self-contained, persistent, asynchronous entity with org-wide tools and context, working alongside teams of humans"
- Getting there is engineering, not modelling: "tools, integrations, compute environments, memory, security"

**Visual:** **DIAGRAM.** Three panels left to right. Panel 1: a browser window
outline with a small figure travelling toward it. Panel 2: a laptop outline with
the same shape sitting inside it. Panel 3: a rounded node embedded among several
human figures arranged in a ring, with short connector lines radiating out to
small tool icons. Progression reads as "out there → on my machine → among us".
Consistent line weight, warm accent reserved for panel 3.

---

## Slide 8 — "I work from Slack now"

**Data:**
- 24 June 2026 · 1,657 likes · 476,414 views
- Pushing back on dismissals: "The basic idea is easy and v0 is a hackathon project. The product here is a lot closer to *it actually works*, for enterprise grade deployments"
- "it's writing majority of code, it's deeply integrated, multiplayer, and it starts to feel like everyone is a manager"
- Not "LLM Q&A with RAG over Slack" — "a different way of working entirely"
- Closing line: "I work from Slack now."

**Visual:** A generic chat-thread layout — plain rounded message bubbles in a
single column, no logos, no avatars, no legible text (bubbles filled with abstract
line-fill). Most bubbles are the accent colour, a minority are white, expressing
that the agent produces the majority of the output. A thin bracket at the right
margin gathers the accent bubbles together.

---

## Slide 9 — The opposite regime

**Data:**
- 30 June 2026 · 1,725 likes · 105,899 views
- The metric: tokens/watt "at interactive tokens/sec/user" — efficiency under a latency constraint
- Engineering wizardry cited: "*very* low voltage domains, cluster scale memory"
- The contrast he found memorable: inference silicon is "very low voltage high current (at tiny distances)"; power transmission is "very high voltage & low current (at great distances)"

**Visual:** **DIAGRAM.** A split composition. Left half: two pylons with a long
catenary line strung between them across a wide gap, drawn thin and sparse —
labelled by form as high-voltage, long-distance. Right half: an extreme close-up
of a dense grid of tiny parallel traces separated by microscopic gaps, drawn thick
and crowded. A vertical rule divides them. The visual rhyme is that the two are
mirror images in scale and density. No text inside the graphic.

---

## Slide 10 — The long ramble session

**Data:**
- 21 July 2026 · 49,332 likes · 4,054,610 views — his most-liked technique post of the window
- The move: "lean back, switch to /voice and just ramble for like 10 minutes, total mess, anything goes, full stream of consciousness"
- Why: "Sometimes the LLM needs more bits to understand what you're trying to achieve, but you're too lazy to type them"
- What comes back: "their echo of your own tangle of thoughts comes out quite a bit cleaner than what you started with"
- Payoff: "you improve the mind meld and have to correct things less from that point on"

**Visual:** Left side, a dense tangle of overlapping scribbled loops in dim grey,
chaotic and knotted. It passes through a narrow vertical aperture at centre and
emerges on the right as a small number of clean, evenly spaced parallel lines in
the warm accent. Reads unmistakably as mess in, order out. No text inside.

---

## Slide 11 — Laggy self-awareness

**Data:**
- 21 July 2026 · 998 likes · 84,675 views
- Quote: "their self-awareness gradually builds up and falls out from pretraining on tokens of us talking about them, but it's laggy and a bit incomplete"
- The mechanism: it comes from pretraining on text humans wrote *about* the models
- Therefore necessarily lagging — the corpus describes previous generations
- Concrete sign of progress: it is starting to "get" what he means when he says he is about to /compact its context

**Visual:** A figure formed entirely from small text-like tick marks stands facing
a mirror. The reflection is built from the same marks but is visibly sparser,
slightly smaller and offset to one side — an incomplete, delayed copy. Rendered as
flat vector line art in two tones, accent for the figure, grey for the reflection.
No legible characters anywhere in the illustration.

---

## Slide 12 — Off the clock

**Data:**
- 15 July · 4,159 likes — "It's not just em dashes, it's that many other legitimate & useful language constructs are suddenly and somewhat arbitrarily super awkw and cringe"
- 12 June · 22,226 likes — "In awe of SpaceX and its story - past, present and the future."
- 12 June · 672 likes — on what he works on: "the brains that glide our von neumann probes around, make contact, establish galactic harmony, all that :)"

**Visual:** A loose three-card arrangement on the dark field, each card a plain
rounded rectangle at a slight rotation, overlapping a little, like notes tossed on
a desk. Cards carry only abstract typographic texture, not real words. One
punctuation mark — a single em dash — floats oversized behind the group in a very
dark tone, barely visible. Light, informal, clearly an interlude.

---

## Slide 13 — A rumor, twice denied

**Data:**
- 26 July 2026 — a rumor circulated that he had resigned
- 01:43 UTC · 2,626 likes · 693,890 views: "weird misinformation to find circling on twitter, no."
- 01:51 UTC · 3,026 likes · 270,405 views: "I thought the way to announce such a thing was not to change your bio but to post the 10 paragraph essay that i just shared with the team?"
- Eight minutes apart
- Both are replies — neither appears on the profile's default Posts tab

**Visual:** Two stacked quote cards, the upper one small and terse, the lower one
wider. To their left runs a thin vertical time rule with two tick marks very close
together, the eight-minute gap rendered almost as a single point. Behind both, a
faint radiating ripple pattern in near-black suggests the rumor spreading. Warm
accent on the tick marks only.

---

## Slide 14 — Retiring the pelican

**Data:**
- 2 August 2026 · 27,882 likes · 4,631,178 views
- "We're starting to leave the territory where you'd test an LLM by e.g. 'create an svg of pelican on a bicycle'."
- The replacement test, exactly: input the first paragraph of the Lord of the Rings; a 1M token budget (~$10); ask for a three.js render; model Opus 5
- Result: ran ~2 hours, wrote 5,500 lines of code that procedurally rendered the story
- His verdict: "It's kind of janky but fun."
- Why it is hard: the model must "place and orchestrate various polygon assets in (x,y,z) coordinates and write code that animates it all"
- The economics: from "no one would ever do this" to "sure, why not, it's ~free"
- Published playable at karpathy.ai/lotr-movie/ ; audio from Eleven Labs

**Visual:** **DIAGRAM.** A left-to-right specification strip rendered as four
connected blocks: a small paragraph glyph → a budget meter → a gear/process block
with a clock arc around it → a wireframe landscape of low-polygon hills and a
winding path. The final block is the largest and carries the warm accent; the
first three are grey line art. Strictly generic fantasy terrain — rolling hills, a
path, a few conifers. No characters, no figures, no creatures, no insignia, no
text of any kind inside the illustration.

---

## Slide 15 — It cannot watch its own work

**Data:**
- Same post, 2 August 2026 — the negative result, and the most important part for practitioners
- Quote: "the domain of worlds/games exposes a weakness in LLMs: they can't easily audit their work because they aren't able to efficiently and natively perceive videos or play games within them"
- What Opus 5 had to do instead: "very slowly and painstakingly take screenshots at different points"
- Consequence: "it messed up a few times and created a bunch of jank"
- His framing: "raw capability (multimodal, gameplay) that I think is still quite lacking"
- Generation has outrun verification; the missing capability is perceptual, not generative

**Visual:** **DIAGRAM.** A closed feedback loop drawn as a ring with two arcs:
the "generate" arc is thick, continuous and in the warm accent; the "perceive"
arc returning is drawn as a broken dashed line that fades out entirely before it
closes the circle. At the break, three small static rectangles float in sequence —
the sampled screenshots standing in for continuous vision. The gap in the ring is
the whole point and should be immediately legible.

---

## Slide 16 — Where it points

**Data:**
- 10 August 2026 · 915 likes · 74,171 views — the last post of the window
- Quote: "It's going to feel so weird that historically you couldn't just talk to your computer like you'd talk to any other person"
- Takeaways: Jevons applies to software — cheap generation grows total demand
- The interface arc: website → local app → persistent asynchronous teammate; "everyone is a manager"
- Raise input bandwidth — ramble by voice; the model's paraphrase is a free alignment check
- Verification is the frontier, not generation
- Follow the replies — his most substantive posts often never reach the default tab

**Visual:** Return of the opening motif: the same field of thin horizontal lines
from slide 1, but now most lines are lit in the warm accent rather than one, and
they resolve toward the right edge into a single continuous line that runs off the
frame. Closes the loop with the title slide and reads as "this continues".

---

# NotebookLM run notes

**Sources to upload:** `notebooklm_source.md` and `slide_division.md`.
If .md upload is rejected, paste each as a **Copied text** source instead — one
source per document.

**Settings:** Studio → Slide Deck → Format **Presenter Slides**, Length **Default**.

**Prompt to paste verbatim into the prompt box:**

```
Audience: AI/ML practitioners. Create exactly 16 slides. Use this outline EXACTLY — same order,
same titles, one slide each:
1. Title
2. The window at a glance
3. "I've joined Anthropic"
4. Stuck on step 1
5. Fable 5: benchmarks vs. feel
6. Jevons paradox for software
7. The third redesign of LLM UI/UX
8. "I work from Slack now"
9. The opposite regime
10. The long ramble session
11. Laggy self-awareness
12. Off the clock
13. A rumor, twice denied
14. Retiring the pelican
15. It cannot watch its own work
16. Where it points
For each slide use the matching "Data" and "Visual" descriptions from the
Slide Division source. Keep text minimal: key message + max 3 bullets per slide.
Quotes are the hero element — set them large and let them dominate the slide.
Do not invent any statistic, engagement figure, date or model name that does not
appear in the sources. Do not render any text inside illustrations.
```

**Fact-gate watch list for the review pass:**
- Engagement figures are exact and must match `notebooklm_source.md` digit for
  digit. The generator will be tempted to round 149,750 to "150K" or invent
  percentages — reject any figure not in the source.
- **5,500 lines**, **~2 hours**, **1M token budget**, **~$10** — these four are the
  most likely to be garbled or swapped. Check each.
- Model names must be exact: **Opus 5**, **Claude Fable 5**, **Mythos**,
  **Claude 4.5**. Do not let "Fable 5" become "Fable 5.0" or "Claude 5".
- The paradigm order is website → downloaded app → persistent asynchronous entity.
  Any reordering inverts the argument.
- The voltage contrast must not flip: inference silicon is *low* voltage / *high*
  current at tiny distances; transmission lines are *high* voltage / *low* current
  at great distances.
- Slide 15 must read as a *limitation*. If it renders as a success story, it has
  inverted the meaning.
- No Tolkien characters, creatures or insignia on slide 14 — generic terrain only.
- No real brand logos anywhere, including on slide 8.
