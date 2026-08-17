# Narration script — Three Months of Karpathy

Spoken register. Technical tokens spelled out for TTS. Every fact traces to
`notebooklm_source.md`; the narration simplifies but never adds.

Spelling conventions applied for speech: "at karpathy" for @karpathy,
"eight-times-H-one-hundred" for 8XH100, "three-point-J-S" for three.js,
"slash voice" for /voice, "slash compact" for /compact, "tokens per watt" for
tokens/watt, "U-I-U-X" for UIUX.

---

## Slide 1 — Title

Between the twelfth of May and the twelfth of August, twenty twenty-six, Andrej Karpathy posted twenty-eight times on X. Not a lot. But it was an unusually eventful three months, and this is what he said, in his own words.

## Slide 2 — The window at a glance

Twenty-eight posts, counting both top-level posts and replies. Two of them tower over the rest. The most-liked, at nearly one hundred and fifty thousand likes, is the announcement that opens this window. The most-viewed, at over eight million, is an argument about interface design. One note before we start: these engagement numbers were captured on the twelfth of August, and they keep climbing.

## Slide 3 — "I've joined Anthropic"

On the nineteenth of May, four sentences. Quote: Personal update. I've joined Anthropic. I think the next few years at the frontier of large language models will be especially formative. I am very excited to join the team here and get back to R and D. I remain deeply passionate about education and plan to resume my work on it in time. End quote. One hundred and forty-nine thousand, seven hundred and fifty likes. Nearly twenty-eight million views. Roughly three times the likes of anything else he posted all summer. Notice the last sentence — education is deferred, not abandoned.

## Slide 4 — Stuck on step 1

The day before that announcement, he was still teaching. And he ran into the wall that makes teaching this material hard. Quote: I was recording my nanochat video when I realized that "first boot up an eight-times-H-one-hundred from your favorite provider" would instantly get everyone stuck on step one of the video. End quote. It's a joke, but it's a real problem. The gap between a reproducible lesson and hardware most learners cannot rent is exactly where frontier-scale education breaks down.

## Slide 5 — Fable 5: benchmarks vs. feel

On the ninth of June, reacting to the Claude Fable Five release, he wrote the longest technical assessment of the window. He noted it is the same underlying model as Mythos, with added safeguards, and that it is state of the art on everything by a margin. But the benchmarks were not his point. Qualitatively, he said, this is a major-version-bump-deserving step change forward, of the same order as Claude four-point-five was in November, and it peaks on long problem-solving sessions on very difficult problems. He was candid about the rough edges too: the model still has quirks, and the safeguards are, in his words, a little too trigger happy for launch.

## Slide 6 — Jevons paradox for software

The second half of that same post is the more durable idea, and it's an economic one. Quote: I feel a lot of things changing as working software increasingly comes out on a tap. The Jevons paradox kicks in and I feel my own demand for software growing substantially. End quote. Jevons paradox says that when something gets cheaper to use, we consume more of it, not less. Applied here: making software cheap to write does not mean less software. It means more — because things nobody would ever have built become worth building. His example is a full weights-and-biases dashboard, hyper-specific to just your project.

## Slide 7 — The third redesign of LLM UI/UX

The twenty-third of June brought his most-viewed post of the window, over eight million views. And it's a claim about interface history, not about model capability. First paradigm: the language model is a website you go to. Second: it's an app you download to your computer. Third — and this is where he says we are now — it is a self-contained, persistent, asynchronous entity, with organization-wide tools and context, working alongside teams of humans. He is clear that getting there is an engineering problem, not a modelling one. Tools, integrations, compute environments, memory, security.

## Slide 8 — "I work from Slack now"

The next day he defended the idea against people calling it trivial. The basic version, he agreed, is a hackathon project. The real thing is enterprise-grade, deeply integrated, multiplayer, and it writes the majority of the code. And then the line that captures the whole shift: it starts to feel like everyone is a manager. He signs off — I work from Slack now.

## Slide 9 — The opposite regime

At the end of June he came up for air from the application layer to admire the physics. The metric he highlights is tokens per watt, measured at interactive tokens per second per user — efficiency under a latency constraint, not throughput in the abstract. And the detail he found memorable: this is engineering at the opposite regime from power transmission. Inference silicon runs very low voltage and high current, over tiny distances. Transmission lines run very high voltage and low current, over great distances. Mirror images.

## Slide 10 — The long ramble session

His most-liked technique post, on the twenty-first of July, is not about a model at all. It's about how you talk to one. Lean back, switch to slash voice, and ramble for ten minutes. Total mess, full stream of consciousness. Why? Because, in his words, sometimes the model needs more bits to understand what you're trying to achieve, but you're too lazy to type them. Speech raises your bandwidth. And what comes back is often cleaner than what you put in. He calls the payoff improving the mind meld — you have to correct things less from that point on.

## Slide 11 — Laggy self-awareness

Later the same day, something stranger. He observes that these models' self-awareness builds up and falls out of pretraining on tokens of us talking about them. Which means it is necessarily laggy, and a bit incomplete — the text describes previous generations, not the one you're talking to. Though he notes it is starting to get what he means when he tells it he's about to slash compact its context.

## Slide 12 — Off the clock

Not everything was work. In mid-July he complained that it isn't just em dashes — that many perfectly legitimate language constructs have suddenly become awkward and cringe. In June he was in awe of SpaceX. And, asked what he actually does, he described himself as working on the brains that glide our von Neumann probes around, make contact, and establish galactic harmony. All that.

## Slide 13 — A rumor, twice denied

On the twenty-sixth of July a rumor went around that he had resigned. He killed it twice in eight minutes. First, flatly: weird misinformation to find circling on Twitter, no. Then, eight minutes later, with a joke about how the rumor started: I thought the way to announce such a thing was not to change your bio, but to post the ten paragraph essay that I just shared with the team. Worth knowing for a practical reason — both of those are replies. Neither shows up on his profile's default tab.

## Slide 14 — Retiring the pelican

Then, on the second of August, the technical centerpiece. He opens by retiring a benchmark: we're starting to leave the territory, he says, where you'd test a language model by asking it to create an S-V-G of a pelican on a bicycle. His replacement test is precise. Give Opus Five the first paragraph of The Lord of the Rings. Give it a one million token budget — about ten dollars. Ask for a three-point-J-S render. Opus went off for about two hours and wrote five thousand five hundred lines of code that procedurally rendered the story. His verdict — it's kind of janky, but fun. The deeper point is economic. Nobody in their right mind would hand-write something this custom. But models have all the stamina in the world. So we move from "no one would ever do this" to "sure, why not, it's basically free."

## Slide 15 — It cannot watch its own work

But the third paragraph of that post is the part practitioners should sit with, because it's a negative result. Worlds and games, he says, expose a weakness. The models can't easily audit their work, because they can't efficiently and natively perceive video, or play games inside them. Opus Five had to slowly and painstakingly take screenshots at different points. It messed up a few times and created a bunch of jank. Think about what that means. The model wrote five and a half thousand lines of an animated world, and then could not watch it run. Generation has outrun verification, and the missing piece is perceptual, not generative.

## Slide 16 — Where it points

The last post of the window is a single line. Quote: It's going to feel so weird that historically you couldn't just talk to your computer like you'd talk to any other person. End quote. Which is the same claim as the June interface argument and the July voice workflow, just pointed at the future. So: four things to take away. Cheap generation grows demand for software, it doesn't shrink it. The interface is becoming a teammate, and everyone becomes a manager. Raise your input bandwidth — talk, don't type. And verification, not generation, is where the frontier now sits.
