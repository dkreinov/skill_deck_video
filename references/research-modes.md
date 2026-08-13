# Research modes

This document governs the deck-video skill's Phase 0 intake and how editorial
style interacts with evidence standards. It defines the single upfront batch
of questions to ask the user, the defaults to use when the user says "your
call," and the rules that keep every storytelling mode honest against the
Fact Gate. Read this before starting Phase 0 of any run.

## Intake batch

Ask ONE batched round of questions at the start of Phase 0. Do not spread
these across multiple back-and-forth prompts. For every field below, "your
call" is an accepted answer — if the user gives it, apply the matching
default from "Recommended defaults."

1. **Central question or hypothesis**
   - What are we investigating?
   - Is there an initial hypothesis to test, or should the report remain
     exploratory?

2. **Research/editorial approach** — the user may pick one option or combine
   several:
   - rigorous scientific evidence review;
   - pop-science explainer;
   - science-fiction-informed framing;
   - fringe / "dark internet" claim investigation;
   - non-obvious signals and weak indicators;
   - balanced multi-lens report.

3. **Epistemic posture** — pick one:
   - argue for a thesis;
   - attempt to falsify a thesis;
   - map the evidence without choosing a side initially;
   - compare multiple scenarios.

4. **Audience and desired takeaway**
   - Who is this for, and what should they walk away believing or knowing?

5. **Delivery format and length**
   - live deck;
   - detailed deck;
   - narrated report video;
   - target duration or slide count.

6. **Scope and time boundary**
   - as-of date;
   - forecast horizon;
   - must-cover areas;
   - must-avoid areas.

7. **Research permissions and extras**
   - permission to use public-web Deep Research;
   - whether music should be generated automatically;
   - whether the agent may proceed without another editorial checkpoint.

8. **Visual register** — how visually ambitious the slides should be. This
   sets how the deck LOOKS, never what counts as true; the Fact Gate, the
   evidence rules and the anti-cliche bans are identical in all three:
   - **paper** — sober and documentary: type, charts and diagrams, pictures
     rare. Reads like a working paper.
   - **editorial** — magazine-like: real pictures on at least a third of
     slides, strong typography, charts where numbers matter.
   - **evocative** — cinematic: imagery that carries the wonder of the
     subject on half or more of the slides, big scale contrasts, still
     fact-gated and still free of AI cliches.
   Ask also whether any single slide should be the deck's showpiece.
   Definitions of each register, and what "wonder" is allowed to mean, are
   in `references/visual-style.md` (`## Visual register`).

## Recommended defaults

If the user answers "your call" for a field (or for all fields), apply the
matching default:

- evidence-mapping rather than a predetermined conclusion (epistemic
  posture: map the evidence without choosing a side initially);
- a rigorous scientific core with a pop-science narrative (research/editorial
  approach);
- science fiction only as framing, never as evidence (research/editorial
  approach, constrained further under "Style vs evidence standard" below);
- a dedicated weak-signals section (research/editorial approach);
- the strongest skeptical counter-case (central question / epistemic
  posture — always steelman the opposing view);
- current date as the as-of date (scope and time boundary);
- 12-18 minutes for a narrated report video (delivery format and length);
- neutral documentary tone and subtle or no music (research permissions and
  extras, and general delivery tone);
- **editorial** visual register (visual register) — pictures on at least a
  third of slides, charts where numbers matter; choose **evocative** when
  the subject itself is a source of wonder and the audience is general;
- full automatic continuation after the intake — no second editorial
  checkpoint unless the user asked for one (research permissions and
  extras).

## Style vs evidence standard

No chosen editorial or storytelling style may weaken the Fact Gate. Style
governs presentation — tone, framing, simplification, narrative device — it
never governs what counts as evidence or lowers the bar for a claim to be
treated as established. Apply the following per-mode rules on top of the
Fact Gate, not instead of it.

### Science-fiction approach

Use fiction only to introduce mental models or illustrative scenarios.
Label any fictional or speculative framing explicitly wherever it appears
(on-slide or in narration) so the audience can never mistake it for a
factual claim. Never use science-fiction material to support, illustrate as
proof, or stand in for an empirical claim. If a scenario is plausible but
unverified, present it as a scenario, not as evidence.

### Pop-science approach

Simplify language only after the rigorous research and Fact Gate checks are
complete — simplification is a presentation step, not a research shortcut.
Do not simplify away uncertainty: if the underlying evidence is mixed,
contested, or preliminary, the simplified narrative must still say so, even
if it does so in plainer language than the technical sourcing.

### Fringe / dark-internet approach

Treat this as a claim-audit mode, not a claim-adoption mode. Search public
fringe sources (forums, blogs, alternative-media sites reachable on the
public web) and trace each claim back to its original source before
reporting on it. Actual dark-web access is out of scope by default. Only
attempt it if the user explicitly supplies lawful sources and a separate,
already-authorized access mechanism — never infer or improvise access to
non-public networks.

### Weak-signals approach

Generate candidate indicators freely, but treat every candidate as a
hypothesis that still requires evidence before it can be reported as a
signal worth attention. Novelty alone is not proof: an indicator being new,
unusual, or previously unremarked is not sufficient grounds to present it as
meaningful without independent supporting evidence.
