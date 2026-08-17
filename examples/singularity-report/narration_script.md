# Narration script — Are we approaching the technological singularity?

Voice: `en-US-AndrewMultilingualNeural`, rate -4%. Register: neutral documentary.
Every fact and number below appears in `notebooklm_source.md`. Nothing is added.

## Slide 1 — Are we approaching the technological singularity?

Let me put the question plainly, and then let me spoil the structure of the answer. On the
twelfth of August, twenty twenty-six, is artificial intelligence development approaching a
technological singularity? You will find confident answers in both directions, and most of them
are answering different questions without noticing. So this report does something slightly
unusual. It refuses to answer until the question has been split apart. Then it goes looking for
the specific measurements that would settle each piece, it takes seriously the strongest case
against whatever conclusion is forming, and it ends with a status rather than a verdict — a
statement of what is observed, what is not, and what would change the answer. Everything here
was researched on the public web, and everything on screen traces back to a source you will see
listed at the end.

## Slide 2 — Five different questions wearing one word

The word "singularity" is doing the work of at least five separate claims. First: general
capability is improving quickly. Second: artificial intelligence is automating the research and
engineering that produces the next system. Third: recursive self-improvement — a closed loop
where each generation genuinely shortens the time or the cost of producing a more capable
successor. Fourth: a break in the trend of economic growth. Fifth: a break in our institutions'
ability to observe and govern any of it. These have different evidence and different answers.
And there is one more distinction that decides everything. "A.G.I." and "superintelligence" name
a *level* of capability. The singularity names a *rate* — the claim that the rate of improvement
itself climbs without bound. A system can be extraordinarily capable while the rate stays
perfectly constant. An exponential is not a singularity.

## Slide 3 — What we can actually measure

That distinction tells us what to measure. Six instruments carry real signal in twenty
twenty-six. Task horizon: the length of task, measured in human-expert time, that an agent can
finish on its own at a stated success rate. The benchmark-to-practice gap: what an automated
grader scores, against what a human maintainer will actually accept. The share of engineering
work at the frontier labs done by AI. Algorithmic efficiency: the compute needed to reach a fixed
level of capability, over time. The macroeconomic statistics. And the physical delivery of
electrical power. Notice something about that list. Five of those six measure *capability*, or
they measure *consequences*. Only one of them, as we will see, measures the loop itself — and
the loop is the whole argument.

## Slide 4 — The capability clock is speeding up

Here is the strongest quantitative evidence that something real is happening. The evaluation
organisation METR measures how long a task an AI agent can complete autonomously, and tracks how
fast that horizon doubles. Across the twenty nineteen to twenty twenty-five baseline, the
horizon doubled roughly every one hundred and ninety-six and a half days. For models from after
twenty twenty-three, that fell to about one hundred and thirty-one days. For models from after
twenty twenty-four, about eighty-nine days — under three months. That is not simply fast
progress. That is the *rate* of progress increasing, which is exactly the kind of quantity the
singularity claim is about. Two honest caveats belong on the same screen. The suite has two
hundred and twenty-eight tasks, and the way the models were grouped into those cohorts was
decided after the fact. And this measures capability getting better — not AI research itself
getting faster. Hold on to that difference.

## Slide 5 — The loop is partly closed

The second piece of the case is that AI now writes a great deal of the software that builds AI.
Anthropic reports that, as of May twenty twenty-six, more than eighty per cent of the code merged
into its main codebase was written by Claude — up from low single digits before February twenty
twenty-five — and that a typical engineer merges about eight times as many lines per day as in
the twenty twenty-one to twenty twenty-four baseline. Google says seventy-five per cent of its
new code is AI-generated this year, up from about fifty per cent last year and twenty-five per
cent the year before. OpenAI's president puts their figure near eighty per cent. And it goes
below the application layer: an AI-driven optimisation loop, running its candidates on real
hardware and backtracking whenever performance regressed, produced a two-point-eight times
average speedup on the low-level kernels behind attention and mixture-of-experts. So part of the
loop genuinely is closed. But notice who is holding the measuring tape. Every one of those code
figures is reported by the company being measured, "new code" is never defined, and the number
does not separate boilerplate from the code that actually decides how the model works.

## Slide 6 — Ask for reliability and the horizon collapses

Now the other side, and it starts by reading the fine print on the number we just celebrated.
That twelve-hour horizon is a *fifty per cent* success horizon. It means the agent finishes a
twelve-hour task about half the time. Raise the bar to eighty per cent success, and for public
frontier models the horizon falls to roughly an hour and a half. The labs' own internal
configurations reach sixteen to twenty hours at the fifty per cent bar, and only three to four
hours at eighty per cent. For public models, twelve hours becomes one and a half. Unattended
research does not run at the fifty per cent bar. Nobody leaves a system alone overnight on a
coin-flip. And for scale: METR's evaluation put GPT-5's autonomous horizon at about two hours and
seventeen minutes, against METR's own threshold of concern for AI-accelerated development, which
sits above forty hours.

## Slide 7 — The benchmark and the maintainer disagree

The second problem is that benchmark scores do not survive contact with real software. On
SWE-bench Verified, proprietary models average seventy-nine point four per cent by the automated
grader. Then human maintainers reviewed two hundred and ninety-six AI-generated pull requests
that had already passed that grader — and rejected roughly half of them. Merge rates ran about
twenty-four percentage points below the automated scores. The reasons were mundane and damning:
logical bugs, regressions in unrelated parts of the codebase, and code that ignored the
repository's own conventions. And when the benchmark is rebuilt with held-out splits, commercial
repositories and contamination controls, state-of-the-art success falls from over seventy per
cent to about twenty-three. One caution about this chart: those three bars have three different
denominators. This is not a decline over time. It is the same capability, measured three ways,
giving three answers.

## Slide 8 — Autonomous science, and one correction

If AI were doing its own research, we would see it in the scientific record. An independent
evaluation of a well-known autonomous research system found that about forty-two per cent of the
experiments it proposed failed outright on code errors. Its literature review worked by keyword
rather than by meaning, so it classified long-established techniques as novel. The papers it
produced carried a median of five citations, and contained hallucinated numerical results. And
here is a correction this report owes you, because its own first research pass got it wrong. You
have probably heard that an AI wrote a paper that was published in *Nature*. It did not. The
March twenty twenty-six *Nature* paper is written by humans and describes the system. The one
AI-generated paper that did clear a workshop bar, with an average reviewer score of six point
three three, was withdrawn before publication by prior agreement. As of the middle of twenty
twenty-six, no paper written solely by an AI has been published in a major peer-reviewed journal.

## Slide 9 — Weak signals, and a framing device

So what should we watch that is not a benchmark? The measurable candidates are things like the
fraction of research steps that run with no human in the loop, automated experiment throughput
per researcher, how fast new evaluations can be built, and the wall-clock gap between model
generations. Two other proposals — how insurers price AI capability risk, and how the frontier
labs hire — currently rest on recruiting firms and insurance marketing, sources with a commercial
stake in the story. Those go on a watch list, not into an evidence base. And now, clearly
labelled: framing only, not evidence. I. J. Good's nineteen sixty-five intelligence explosion
assumes intelligence scales without friction, and ignores what each increment costs in compute.
Vernor Vinge's nineteen ninety-three essay needs a mathematical asymptote — progress going
vertical at a finite date — while what we actually measure are smooth curves gated by roughly
two-year gigawatt cluster build times. The later seed-AI and "foom" scenarios assume a
software-only takeoff that today's hardware limits contradict. These stories sharpen the
question. Nothing in this report rests on them.

## Slide 10 — The forecasters do not agree

You might hope the experts have settled this. They have not. Median expert forecasts for
human-level machine intelligence have moved closer over time: twenty fifty in a twenty eleven
survey, twenty sixty-one in twenty sixteen, twenty fifty-nine in twenty twenty-two, and twenty
forty-seven in the survey taken after GPT-4. Note that the compression is not even monotonic —
the twenty sixteen number is later than the twenty eleven one. But the sharper finding is what
happens when you ask two careful groups the same question in the same year. Superforecasters put
transformative AI at one per cent by twenty thirty and twenty-one per cent by twenty fifty. AI
domain experts put it at nine per cent and forty-six. A nine-fold gap by twenty thirty. That is
not noise; it is the honest state of the question. And every one of these numbers measures
belief, not capability.

## Slide 11 — What is actually blocking it

Four constraints, and two of them are more contested than you have been told. Model collapse —
the result that a system training on its own output degrades — is real mathematics, but it holds
only when externally grounded data vanishes. Frontier training keeps real data in the mix,
filters synthetic output through external verifiers like compilers and test suites, and grounds
optimisation in environments that can check an answer. Keeping as little as ten per cent real
seed data is enough to stabilise the run. Benchmark contamination is similar: it is real and
large — inflating one maths benchmark by up to twenty-two point nine per cent — but its headline
evidence turned out to be confounded, when a twenty twenty-six study removed the effect entirely
just by rewording the tasks. Two constraints are firmer. Parallelisation has a ceiling: you
cannot compress the serial depth of an experiment by running more of them, and a million
near-identical model instances do not think in a million different directions. And power is
simply slow. Utilities report time-to-power running one and a half to two years longer than
developers assume, and interconnection for new lines takes thirty-six to sixty months.
Meanwhile, twenty-year average US total factor productivity growth sits at zero point five three
per cent — though that flat line is weaker evidence than it looks, since the underlying
statistics are heavily revised and intangible investment is chronically under-counted.

## Slide 12 — The calibrated answer, 12 August 2026

So here is the answer, and it is a status, not a verdict. Observed: capability is improving, and
the rate of improvement has risen. AI writes a large share of the code inside the frontier labs.
AI measurably optimises the low-level software it runs on. Parts of the loop are genuinely
closed. Not observed: a compounding rise in the rate of AI research itself. And that is the
measurement that matters most, because it is the loop gain the entire classical argument depends
on. When METR ran a cross-lab pilot and asked precisely this, the finding was that although task
duration has been doubling roughly every four months since twenty twenty-four, developer audits
report that overall research and development velocity has *not yet* reached a two-times
compounding acceleration. The labs themselves, reporting to an outside evaluator, say the loop
has not closed at the level the claim requires. So: we are not measurably inside a technological
singularity. We are measurably inside a period of unusually fast capability growth in which AI
performs much of AI engineering. Those are different claims, and only the second is established.
Confidence: moderate — high on the individual measurements, lower on the synthesis, because the
decisive number is self-reported by the labs being evaluated.

## Slide 13 — What would change this, and where it came from

Five things would move this answer. Task horizons at the *eighty* per cent bar exceeding a full
working day. The cross-lab audit reporting that R&D velocity has reached sustained two-times
compounding acceleration. An externally audited measurement — not a self-report — of how much
core model and training-loop code AI actually writes. AI-authored papers repeatedly clearing full
peer review, without prior arrangement. And total factor productivity breaking its trend in a way
that survives revision. On method: three deep research passes, two hundred and sixty-four sources
imported with none discarded, every claim given a row in an evidence matrix with an exact
locator, ten claims dropped for citations that did not hold up, and every chart in this video
rendered from a data file rather than drawn. One last disclosure. All of this was researched on
the public web on the twelfth of August, twenty twenty-six. It has not been verified against
authoritative internal documentation. If you take one thing away, take the distinction: the
question is about a rate, and the rate that matters has not yet been observed to turn.
