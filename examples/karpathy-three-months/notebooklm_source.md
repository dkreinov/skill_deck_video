# Andrej Karpathy on X: May–August 2026

**Audience: AI/ML practitioners. Source: @karpathy on X, 2026-05-12 → 2026-08-12.**

Every quote and every number in this document is taken verbatim from the posts
themselves, captured from a logged-in X session on 2026-08-12. Engagement figures
are as read at capture time and will drift. Nothing here comes from a news
article, a blog summary, or recollection.

---

## Why this window matters

Three months is normally too short a window to say anything about a person. This
one is an exception, because it opens with Karpathy changing jobs.

On **19 May 2026** he posted a four-sentence personal update announcing he had
joined Anthropic. It drew **149,750 likes** and **27,909,958 views** — by a wide
margin the largest response of anything he posted in the window, and roughly
three times the likes of the next-biggest post. Everything that follows in these
three months is, in effect, a practitioner narrating what the frontier looks like
from inside a frontier lab.

The volume is low and the signal is high. He posted **28 times** in the window,
counting both top-level posts and replies. Several of the most substantive items
are replies rather than top-level posts — a detail that matters for anyone trying
to follow him, because replies do not surface on the profile's default tab.

---

## The announcement

> "Personal update: I've joined Anthropic. I think the next few years at the
> frontier of LLMs will be especially formative. I am very excited to join the
> team here and get back to R&D. I remain deeply passionate about education and
> plan to resume my work on it in time."
> — 19 May 2026 · 149,750 likes · 27,909,958 views

Two things are worth pulling out. First, the stated motivation is that the next
few years will be "especially formative" — a bet on timing, not on any particular
technique. Second, education is explicitly deferred, not abandoned: he plans to
"resume my work on it in time."

The day before the announcement, on **18 May**, he was still in education mode and
posted a small, telling observation about the friction in teaching this material:

> "I was recording my nanochat video when I realized that 'first boot up an
> 8XH100 from your favorite provider!' would instantly get everyone stuck on step
> 1 of the video"
> — 18 May 2026 · 1,992 likes · 218,965 views

The joke lands because it is a real problem. The gap between a reproducible
teaching artifact and a piece of hardware most learners cannot rent is the thing
that makes frontier-scale education hard.

---

## Working software on a tap

On **9 June**, reacting to the Claude Fable 5 release, Karpathy wrote the longest
technical assessment of the window. He described Fable 5 as "the same underlying
model as Mythos but with added safeguards", called it SOTA "on everything by a
margin", and then made a point of separating benchmarks from felt experience:

> "*qualitatively* also, this is a major-version-bump-deserving step change
> forward (imo of the same order as Claude 4.5 was in November), peaking
> especially for long problem-solving sessions on very difficult problems."

He was candid about the rough edges too, noting the model "still has quirks" and
that "the safeguards are configured to be a little too trigger happy for launch,
which can hopefully be tuned over time." He also flagged a working practice and
immediately warned against it: it has "never felt this tempting to stop looking at
the code at all (but don't do this in prod!)".

The second half of the post is the more durable idea — an economic one:

> "I feel a lot of things changing as working software increasingly comes out on
> a tap. The Jevon's paradox kicks in and I feel my own demand for software
> growing substantially. You can ask for anything - explainers, visualizers,
> dashboards, bespoke single-use apps (e.g. a full wandb that is hyper-specific
> just for your project), you can 10X your test suite, auto-optimize code, run
> giant research projects with custom HTML for the results, anything!"
> — 9 June 2026 · 25,645 likes · 3,044,871 views

Jevons paradox is the observation that when a resource becomes cheaper to use,
total consumption of it goes up rather than down. Applied here: making software
cheap to produce does not reduce how much software gets written. It increases it,
because categories of software that were never worth building — the hyper-specific
single-use dashboard — suddenly are.

---

## The third redesign of LLM UI/UX

On **23 June** he made his most-viewed argument of the window (**8,140,553 views**),
and it is a claim about interface history rather than about model capability:

> "Imo this is the 3rd major redesign of LLM UIUX. The first paradigm was that
> the LLM is a website you go to, the second was that it is an app you download
> to your computer. This third one is that it is a self-contained, persistent,
> asynchronous entity with org-wide tools and context, working alongside teams of
> humans."

The four properties in that definition are load-bearing: **self-contained**,
**persistent**, **asynchronous**, and equipped with **org-wide tools and context**.
He is explicit that getting there is an engineering problem rather than a
modelling one — it requires "all of the under the hood engineering work to make
this 'just work' (e.g. across tools, integrations, compute environments, memory,
security, etc.)". Once that is done, "Claude basically joins the team in a
seamless way."

He returned to it the next day, on **24 June**, pushing back on people dismissing
the idea as trivially easy to build:

> "The basic idea is easy and v0 is a hackathon project. The product here is a
> lot closer to *it actually works*, for enterprise grade deployments... it's
> writing majority of code, it's deeply integrated, multiplayer, and it starts to
> feel like everyone is a manager. So I understand it looks easy to dismiss on
> quick reading but it's not some LLM Q&A with RAG over Slack... it's a different
> way of working entirely, for people and teams. **I work from Slack now.**"
> — 24 June 2026 · 1,657 likes · 476,414 views

"Everyone is a manager" is the compressed version of the whole thesis: if the
agent does most of the typing, the human's job shifts to specification, review,
and delegation.

---

## Down at the hardware

On **30 June** he surfaced from the application layer to admire the physics, in a
post about the engineering behind inference efficiency:

> "I was impressed to learn about some of the engineering wizardry (e.g. *very*
> low voltage domains, cluster scale memory, ...) that goes into tokens/watt
> maxxing of state of the art LLMs at interactive tokens/sec/user. Esp fun and
> memorable is the idea that this is engineering at the 'opposite' regime to that
> of power transmission lines: very low voltage high current (at tiny distances)
> vs. very high voltage & low current (at great distances)."
> — 30 June 2026 · 1,725 likes · 105,899 views

The metric worth noting is **tokens/watt at interactive tokens/sec/user** — that
is, efficiency measured under a latency constraint, not throughput in the
abstract.

---

## How to actually talk to these things

The most-liked *technique* post of the window came on **21 July** (**49,332 likes**,
**4,054,610 views**) and describes a workflow, not a model:

> "One pattern I find useful for working with LLMs is a nice long ramble session.
> Sometimes the LLM needs more bits to understand what you're trying to achieve,
> but you're too lazy to type them. In these cases I like to lean back, switch to
> /voice and just ramble for like 10 minutes, total mess, anything goes, full
> stream of consciousness... I find that the LLMs are somehow very good at
> reconstructing long incoherent rambles and often their echo of your own tangle
> of thoughts comes out quite a bit cleaner than what you started with. The
> result is that you improve the mind meld and have to correct things less from
> that point on."

The mechanism he is pointing at: the bottleneck in getting good output is the
number of bits of intent you transmit, and typing is a low-bandwidth channel that
people under-use out of laziness. Speech raises the bit rate. The model's
paraphrase back to you then serves as an alignment check — his phrase is "improve
the mind meld", and the payoff is having "to correct things less from that point
on."

Later the same day he noted something stranger, about models' models of
themselves:

> "It's interesting/amusing how their self-awareness gradually builds up and
> falls out from pretraining on tokens of us talking about them, but it's laggy
> and a bit incomplete. But I think e.g. it's starting to 'get' what I mean when
> I inform it I'm about to /compact its context etc"
> — 21 July 2026 · 998 likes · 84,675 views

The causal claim is precise: whatever self-awareness these systems display is
downstream of pretraining on text humans wrote *about* them, which makes it
necessarily **laggy** — the corpus describes previous generations, not the current
one.

On **15 July** he made a related point about what LLM ubiquity is doing to prose:

> "It's not just em dashes, it's that many other legitimate & useful language
> constructs are suddenly and somewhat arbitrarily super awkw and cringe"
> — 15 July 2026 · 4,159 likes · 241,916 views

---

## A rumor, briefly

On **26 July**, a rumor circulated that he had resigned. He denied it twice within
eight minutes — first flatly, at 01:43 UTC:

> "weird misinformation to find circling on twitter, no."
> — 693,890 views

and then, at 01:51 UTC, with a joke at the expense of how the rumor started:

> "I thought the way to announce such a thing was not to change your bio but to
> post the 10 paragraph essay that i just shared with the team?"
> — 3,026 likes · 270,405 views

Worth including not for the gossip but for a practical reason: both posts are
**replies**, so neither appears on his profile's default Posts tab. The most
newsworthy thing he said in July is invisible to anyone reading only that tab.

---

## Retiring the pelican

The technical centrepiece of the window landed on **2 August** (**27,882 likes**,
**4,631,178 views**). It opens by declaring a popular informal benchmark obsolete:

> "We're starting to leave the territory where you'd test an LLM by e.g. 'create
> an svg of pelican on a bicycle'."

His replacement test, and its result, stated exactly:

- Input: **the first paragraph of the Lord of the Rings**
- Budget: **a 1M token budget (~$10)**
- Ask: **a three.js render of it**
- Model: **Opus 5**
- Result: it "went off for **~2 hours**" and wrote **5,500 lines of code** that
  procedurally rendered the story
- His own verdict: "It's kind of janky but fun."

What he found notable was the nature of the task: the model "has to place and
orchestrate various polygon assets in (x,y,z) coordinates and write code that
animates it all, and that it even does anything at all."

Then the economic observation, which generalises past this one demo:

> "no one in their right mind would ever spend the time to write something this
> custom but LLMs have all the stamina and patience in the world, so it's an
> example where we go from 'no one would ever do this' to 'sure, why not, it's
> ~free'."

He sketched where it leads — "hyper custom worlds that you can imagine dropping
players into", joining the LoTR story "as a spectator NPC, or one of the
characters", which he calls "an ephemeral GTA of X on demand." He published the
result at **karpathy.ai/lotr-movie/**, noting he "uploaded the source here so it's
playable in the browser, forkable etc.", and signed off: "Look out for GTA
Hobbiton dropping before GTA VI :)". In a separate reply he confirmed the audio
came from **Eleven Labs**, adding that "LLMs can easily use the APIs (here I did
that part manually because I felt picky about the voice)."

### The failure mode it exposed

The third paragraph is the part practitioners should care about most, because it
is a negative result:

> "the domain of worlds/games exposes a weakness in LLMs: they can't easily audit
> their work because they aren't able to efficiently and natively perceive videos
> or play games within them. Here, Opus 5 had to very slowly and painstakingly
> take screenshots at different points, and it messed up a few times and created
> a bunch of jank. An example of raw capability (multimodal, gameplay) that I
> think is still quite lacking."

The specific gap is **the audit loop**. The model can generate a 5,500-line
animated world but cannot watch it run. Lacking native video perception, its only
recourse was sampling static screenshots — and the jank he describes is the direct
consequence. Generation has outrun verification, and the missing capability is
perceptual rather than generative.

---

## Where it points

The last post of the window, on **10 August**, is a one-liner:

> "It's going to feel so weird that historically you couldn't just talk to your
> computer like you'd talk to any other person"
> — 915 likes · 74,171 views

It is the same claim as the June UI/UX argument and the July ramble-session
workflow, stated as a prediction about how the present will look in hindsight.

Three months, one job change, and a consistent through-line: the interface is
becoming conversational, the cost of bespoke software is collapsing toward zero,
and the binding constraint is shifting from whether a model can produce something
to whether it — or you — can check that what it produced is right.

---

## Takeaway for practitioners

1. **Jevons applies to software.** Cheap generation grows total demand rather than
   shrinking it. The new category is the bespoke, single-use tool.
2. **The interface is the story.** Website → local app → persistent asynchronous
   teammate with org-wide tools and context. "Everyone is a manager."
3. **Raise your input bandwidth.** Rambling by voice for ten minutes transmits
   more intent than typing, and the model's paraphrase is a free alignment check.
4. **Verification is the frontier, not generation.** A model wrote 5,500 lines in
   two hours and then could not watch its own output run. Multimodal perception
   and gameplay are the named gaps.
5. **Follow the replies.** Some of his most substantive posts in this window —
   including the Fable 5 assessment and both rumor denials — are replies and never
   appear on the default profile tab.
