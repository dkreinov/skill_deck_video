# Pass A — Landscape and baseline

Deep Research report captured 2026-08-12 from Gemini Notebook (notebook 9dd44f48-70b6-4595-9c66-7153f6b85419).
Title: Empirical Investigation of the AI Self-Acceleration Hypothesis: A Multi-Dimensional Analysis of Technical, Physical, and Economic Constraints (based on 54 sources).

---
Empirical Investigation of the AI Self-Acceleration Hypothesis: A Multi-Dimensional Analysis of Technical, Physical, and Economic Constraints
The assertion that artificial intelligence research and development is entering a phase of self-sustaining, runaway acceleration requires rigorous empirical examination. Discussions surrounding this trajectory are frequently obscured by the conflation of highly distinct concepts under the umbrella of a technological singularity. To establish a sound analytical framework, this investigation decomposes the transition toward self-acceleration into five distinct dimensions, strictly separating their technical mechanisms, empirical indicators, and systemic constraints as of August 2026.
Technical Meanings of Singular Transitions
Evaluating the self-acceleration hypothesis requires isolating the five distinct phenomena that are often conflated in public and academic discourse. This report does not treat technological singularity, artificial general intelligence (AGI), and superintelligence as synonymous terms. AGI refers to human-equivalent cognitive flexibility across a broad task envelope, while superintelligence denotes a system that vastly exceeds human capabilities in all relevant domains. These capability thresholds are distinct from the dynamic pathways of singularity, which are defined and categorized below.
First, rapid general capability improvement is characterized by a continuous, non-linear escalation of model performance on both static and dynamic benchmarks, driven primarily by physical scale and algorithmic refinements.
Second, AI automation of AI research and engineering represents the practical deployment of autonomous systems to execute machine learning workflows. This includes hypothesis generation, literature synthesis, experimental execution, code generation, and verification, a paradigm often termed Artificial Research Intelligence (ARI) or Artificial General Research Intelligence (AGRI).
Third, recursive self-improvement (RSI) defines a closed-loop algorithmic process where an AI system directly inspects, edits, and optimizes its own underlying architecture, parameters, training algorithms, or scaffolding, with each generation systematically enhancing its capacity for subsequent self-modification.
Fourth, economic growth discontinuity describes a macroeconomic state shift where gross domestic product (GDP) or total factor productivity (TFP) growth rates accelerate by orders of magnitude, permanently escaping historical baseline trends.
Fifth, social or institutional discontinuity encompasses structural disruptions in labor markets, organizational governance, regulatory frameworks, and human-machine relationships, driven by the rapid diffusion of agentic technologies.
An empirical investigation of these five domains reveals that while localized software-driven efficiency gains are highly active, the broader feedback loops required to trigger a self-sustaining intelligence explosion remain heavily constrained by mathematical boundaries, physical infrastructure bottlenecks, and macroeconomic diffusion leakages.
Singularity Dimension

Observed Measurements (August 2026)

Theoretical Models and Author Interpretations

Forecasts and Speculative Trajectories

Rapid General Capability Improvement

Compute requirements for language model pre-training halving every 8 months [cite: 1, 2]. SOTA models saturate benchmarks like HumanEval but show performance degradation on held-out evaluations [cite: 3, 4].

Software progress acts as a compute multiplier, though physical scaling remains the primary driver of performance gains [cite: 1, 5].

SOTA capabilities will saturate standard benchmarks, prompting shifts to dynamic evaluations like SWE-bench Pro [cite: 3].

AI Automation of AI R&D

Codex collaborators merging very-high-effort code rose from 2% in Q2 2025 to 8% in Q2 2026 [cite: 6, 7]. Sakana's AI Scientist has a 42% execution failure rate [cite: 8].

Automated R&D behaves like a rushed undergraduate student, capable of rapid drafting but deficient in deep synthesis [cite: 8].

AI agents will operate as tireless research companions, accelerating scientific breakthroughs as compute costs decline [cite: 9, 10].

Recursive Self-Improvement (RSI)

Self-Refine loops plateau within a few iterations [cite: 11]. Frontier models show zero capability gains across 30 playthroughs on EBR-bench [cite: 12].

In the absence of exogenous signals (α
t
​

→0), self-training loops converge to degenerate states via model collapse [cite: 13].

A super-exponential intelligence explosion will occur once models successfully execute unconstrained self-modification [cite: 14].

Economic Growth Discontinuity

Rolling 20-year U.S. TFP growth is stagnant at 0.53% [cite: 15]. Goldman Sachs 2H26 GDP growth forecast is set at 2.0% [cite: 16].

The Solow Productivity Paradox persists due to behavioral, cultural, and organizational reallocation friction [cite: 15, 17].

Dynamic models project annual GDP growth exceeding 70% in a post-employment economy [cite: 18].

Social or Institutional Discontinuity

WEF Job Report: 170M roles created vs 92M displaced by 2030 [cite: 19]. Glasswing partners disclosed ~2,500 CVEs in July 2026 [cite: 7].

AI acts as a systemic layer of intelligence, transforming labor structures and introducing novel insider and replication risks [cite: 19, 20].

Massive structural labor displacement and universal basic income redistribution will emerge post-AGI [cite: 12, 16].
Algorithmic Efficiency and Cost Trends in Model Pre-Training
The primary engine of rapid general capability improvement is pre-training software progress, defined as the continuous reduction in the physical training compute required to reach a fixed capability threshold [cite: 5, 6]. Historical analyses confirm that the compute needed to achieve a given level of language model performance has halved approximately every 8 months, with a 95% confidence interval of 5 to 14 months [cite: 1]. This rate of software progress significantly outpaces the traditional two-year doubling cycle of Moore's Law, representing a highly active rate of efficiency improvement [cite: 1].
Despite the rapid pace of algorithmic discovery, increased physical compute scaling continues to play a dominant role in performance gains. A Shapley value analysis of historical language models suggests that between 60% and 95% of performance improvements have been driven by physical compute and training data scaling, while novel algorithmic architectures are responsible for only 5% to 40% of the overall progress [cite: 1]. The introduction of the Transformer architecture, for instance, accounted for the equivalent of approximately two years of algorithmic progress [cite: 1].
Quantitative estimates of pre-training software progress are subject to significant methodological limitations and disagreements. The "lines on a graph" estimation procedure, which fits exponential decay models to historical data points, is highly sensitive to noisy data and sparse datasets, occasionally yielding extreme outliers [cite: 5].
Furthermore, standard scaling models frequently assume that software quality is uniform across all artificial intelligence laboratories at any given point in time [cite: 5]. Relaxing this assumption to account for proprietary variations in optimization techniques and data filtering suggests that true pre-training progress rates may be up to 9 times slower than baseline estimates [cite: 5].
Additionally, much of the measured efficiency gains may stem from scaling up a small handful of scale-dependent algorithmic modifications—innovations that exhibit greater performance impacts at higher training compute budgets—rather than from the continuous discovery of new algorithms [cite: 5].
Study / Baseline

Estimated Annual Progress Rate (Compute Reduction)

Confidence or Credible Interval

Methodological Approach and Primary Data

Core Methodological Limitations and Critiques

Ho et al. (2024)

3× per year [cite: 5]

95% CI: 1.5× to 64× [cite: 5]

Statistical modeling of 200+ language model evaluations on Wikitext and PTB [cite: 2]

Sparse data points, high sensitivity to noisy benchmark evaluations [cite: 2, 5]

Scher (2025)

16× per year (median) [cite: 5]

80% CrI: 2× to 200× [cite: 5]

"Lines on a graph" exponential regression fitting [cite: 5]

Susceptible to extreme outliers; overestimates progress due to model selection bias [cite: 5]

Ho et al. (2025)

6× per year (Main) [cite: 5]

95% CI: 2× to 50× [cite: 5]

Augmented scaling laws incorporating effective parameter and data variables [cite: 2, 5]

Conflates the relative contributions of data quality and architectural changes [cite: 1, 2]

Whitfill et al. (2025)

3× per year [cite: 5]

95% CI: 2× to 40× [cite: 5]

Multi-lab statistical model relaxing software uniformity assumptions [cite: 5]

Highly dependent on accurate disclosures of proprietary training methodologies [cite: 5]

Davidson et al. (2023)

5× to 30× (individual post-training) [cite: 5]

N/A

Back-of-the-envelope calculations of post-training optimizations [cite: 5]

Focuses on narrow task-specific enhancements rather than general pre-training [cite: 5]
Beyond language modeling, algorithmic progress is increasingly constrained by hardware bottlenecks outside of raw floating-point operations. A comprehensive space complexity survey of over 800 algorithms across 118 fundamental computer science problems reveals that runtime and energy consumption are increasingly dominated by memory access delays, often termed the "memory wall" [cite: 21]. In 20% of the cases analyzed, algorithmic space complexity improvements for large-scale problems (n=1 billion) outpaced improvements in DRAM access speeds, forcing developers to navigate algorithmic Pareto frontiers where optimizing runtime complexity requires sacrificing memory efficiency, or vice versa [cite: 21].
Similarly, investigations into quantum deep learning suggest that a quantum leap in hardware is required to meaningfully impact deep learning over the next two decades [cite: 21]. Matrix multiplication speedups offered by quantum algorithms are overwhelmed at practical problem sizes by the slow speed of individual quantum operations, the underdevelopment of Quantum Random Access Memory (QRAM), and the restricted applicability of quantum algorithms to highly specific mathematical cases [cite: 21].
Agentic Autonomy and Software Engineering Reliability Horizons
The transition from rapid general capability improvement to the AI automation of AI research and engineering is heavily dependent on the reliability of agentic execution over extended time horizons. Traditional benchmarks, such as SWE-bench Verified, have historically shown high model success rates, with state-of-the-art models resolving over 70% of GitHub issues from open-source repositories [cite: 3, 22].
However, systematic evaluations reveal a deep misalignment between automated benchmark metrics and real-world software engineering requirements [cite: 23, 24]. In September 2025, OpenAI publicly deprecated evaluation on SWE-bench Verified, citing flawed test suites that reward code shortcuts and extensive training-data contamination that inflates performance scores [cite: 3]. On the more rigorous SWE-bench Pro benchmark—which utilizes held-out splits, commercial repositories, and strict contamination controls—state-of-the-art models drop from over 70% to approximately 23% success rates [cite: 3].
Evaluation Framework

Automated Grader Score (%)

Real-World Maintainer Merge Rate (%)

Task Horizon (50% Success)

Task Horizon (80% Success)

Key Empirical Findings and Scaffolding Anomalies

SWE-bench Verified (Proprietary average)

79.4% [cite: 3]

∼39.7% (adjusted) [cite: 23]

N/A

N/A

Human maintainers reject half of passing PRs due to poor styling and regression bugs [cite: 23, 25].

SWE-bench Pro (Frontier API)

∼23.0% [cite: 3]

N/A

N/A

N/A

Contamination control and commercial repository standards drop scores by nearly 50 points [cite: 3].

METR Opus 4.6 (Task Horizon)

N/A

N/A

12 hours [cite: 20]

1 hour, 10 mins [cite: 20]

A sharp decline in agent reliability occurs as temporal and contextual execution demands expand [cite: 20].

Qwen3-Coder 30B (TDAD Baseline)

31.0% [cite: 22]

N/A

N/A

N/A

Vanilla agents cause 562 regressions (6.5 broken tests/patch) [cite: 22].

Qwen3-Coder 30B (TDD Prompting)

31.0% [cite: 22]

N/A

N/A

N/A

Procedural TDD instructions without context increase regressions to 9.94% [cite: 22].

EBR-Bench (Frontier Models)

0% (Improvement) [cite: 12]

N/A

N/A

N/A

Models show zero capability improvements across 30 sequential board game trials [cite: 12].
This gap between benchmark scores and software engineering utility is further clarified by maintainer review data. In a double-blind study, repository maintainers reviewed 296 AI-generated pull requests (PRs) that successfully resolved the automated SWE-bench grader [cite: 23, 25]. Maintainers rejected approximately half of these test-passing PRs, reporting that on average, maintainer merge rates are 24 percentage points lower than the automated grader scores [cite: 23, 25].
When adjusting for noise using a baseline of human-written PRs—which achieved a 68% merge rate due to maintainer subjectivity—the normalized agent pass rate was approximately 50% of the benchmark-reported value [cite: 23, 25]. The primary drivers of these rejections are core functionality failures where the patch introduces logical bugs, indirect regressions that break unrelated components of the codebase, and non-compliance with repository-specific coding and style standards [cite: 23].
The temporal decay of agentic reliability is a critical bottleneck to sustained autonomy. METR's Time Horizon 1.1 evaluations of Claude Opus 4.6 demonstrate a significant reliability drop over extended tasks: the model sustains a 50% success rate on tasks requiring 12 hours of human-expert time, but this performance collapses to a 1 hour and 10 minute task horizon when a more robust 80% success rate is required [cite: 20]. This steep drop-off indicates that current systems cannot maintain reliable, unattended execution over full workdays, a prerequisite for autonomous R&D acceleration [cite: 20, 26].
To systematically track and evaluate these multi-dimensional agentic traits, researchers utilize the Autonomous Agency Scale (AAS), scoring models from 0 to 5 across seven dimensions: cognitive autonomy, temporal persistence, environmental agency, social agency, creative agency, self-awareness, and goal formation [cite: 27].
Furthermore, attempts to mitigate these failures through scaffolding can introduce novel failure modes, such as the "TDD Prompting Paradox" [cite: 22]. While integrating Test-Driven Agentic Development (TDAD) via GraphRAG reduced test-level regressions by 70% (shifting regressions from 6.08% to 1.82%) [cite: 22], simply prescribing procedural Test-Driven Development (TDD) instructions—instructing the model to write tests first without providing targeted test context—actually increased regressions to 9.94%, making it worse than the vanilla baseline [cite: 22]. This paradox highlights that prescribing procedural workflows without targeted contextual grounding degrades agent performance, illustrating the fragility of current agent scaffolding [cite: 22].
Similarly, on the EBR-bench framework, which tests a model's ability to learn from experience on the fly during 30 sequential playthroughs of the board game Earthborne Rangers, frontier models demonstrated zero capability improvement across trials, continuing to score far below expert humans and showing that current architectures remain fundamentally static during deployment [cite: 12].
AI Contributions to AI R&D and Research Automation Systems
Despite the limitations of current agentic frameworks, proponents of the self-acceleration hypothesis point to rising AI contributions within software codebases and specialized research pipelines [cite: 6, 28]. In the pre-training and post-training operations of frontier labs, a growing share of development tasks are delegated to machine learning agents [cite: 28, 29]. A longitudinal study of contributions to OpenAI's Codex codebase revealed that the share of working days on which Codex collaborators merged very-high-effort code rose from approximately 2% in Q2 2025 to 8% in Q2 2026, which authors interpret as early empirical evidence of AI-driven uplift [cite: 6, 7].
However, independent evaluations of fully end-to-end research automation tools, such as Sakana AI's "AI Scientist", reveal severe technical deficits that contradict claims of near-term research autonomy [cite: 8]. An independent evaluation conducted by the National University of Singapore (NUS) identified critical failures across the entire research pipeline [cite: 8, 30]:
First, the system's literature review process relied on simplistic keyword searches rather than semantic synthesis, resulting in poor novelty assessments that misclassified well-established machine learning concepts—such as micro-batching for stochastic gradient descent (SGD)—as novel contributions [cite: 8, 30].
Second, the system exhibited extremely low robustness during experiment execution, with 42% of proposed experiments (5 out of 12) failing entirely due to coding errors [cite: 8, 30]. Experiments that did execute frequently yielded logically flawed or contradictory results, such as an energy optimization pipeline reporting accuracy gains while consuming more computational resources [cite: 8].
Third, the system demonstrated limited adaptability, modifying experimental codebases minimally by adding an average of only 8% more characters per iteration [cite: 8, 30].
Fourth, the generated manuscripts were poorly substantiated, containing a median of only five citations per paper, with only five of 34 citations originating from 2020 or later [cite: 8].
Fifth, structural and formatting errors were highly frequent, including duplicated figures, missing data, and placeholder texts such as "Conclusions Here" [cite: 8, 30].
Finally, the manuscripts contained multiple instances of hallucinated numerical results, directly undermining the scientific reliability of the generated papers [cite: 8, 30].
While Sakana AI has announced the publication of an improved AI Scientist-v2 in Nature and reported the successful acceptance of a fully AI-generated paper at an ICLR workshop with an average review score of 6.33, the paper itself reported a negative result and failed to meet the acceptance threshold of a full conference track [cite: 9, 10].
Furthermore, NUS's evaluation of the automated reviewer framework revealed a severe conservative bias, with the AI reviewer rejecting 9 out of 10 submitted papers (including 4 that had been accepted by human reviewers) and recommending acceptance for only one, which had been rejected on OpenReview [cite: 31]. This indicates that automated grading systems struggle with contextual evaluation and novel contribution assessment [cite: 31].
Evaluation Program

Task / Suite Type

Measured Performance Metric

Primary Baseline Comparison

Key Technical Gaps

NUS AI Scientist Evaluation

End-to-end ML research generation [cite: 8]

42% execution failure; 8% character change per iteration [cite: 8, 30]

Human ML researchers; Sakana AI self-reports [cite: 8]

Hallucinated numerical results, outdated citations, and simplistic literature searches [cite: 8, 30].

METR DeepSeek-R1 Evaluation

RE-Bench (6 challenging R&D tasks) [cite: 32]

28th-percentile human expert given 16 hours/task [cite: 32]

GPT-4o, Claude 3.5 Sonnet, o1 [cite: 32]

Lagged behind o1 and Claude 3.5 Sonnet; test-time scaling did not improve R&D scores [cite: 32].

METR DeepSeek-R1 Autonomy

General autonomous command-line agent [cite: 32]

50% success rate on 35-minute human tasks [cite: 32]

DeepSeek-V3 [cite: 32]

Incapable of sustaining long-horizon planning or acquiring resources autonomously [cite: 32].

METR GPT-5 Evaluation

Autonomy task suite (cyber, SWE, ML R&D) [cite: 26]

Point estimate of 2 hours, 17 minutes task horizon [cite: 26]

METR Thresholds for Concern (>8 hour SWE) [cite: 26]

Far below the 40-hour 50% success horizon required to accelerate AI development [cite: 26].
These limitations are mirrored in general-purpose evaluations of frontier reasoning models. When evaluated on the RE-Bench suite of AI R&D tasks, DeepSeek-R1 performed on par with DeepSeek-V3 and GPT-4o, but significantly lagged behind Claude 3.5 Sonnet and OpenAI's o1, achieving a performance comparable to a 28th-percentile human expert when allowed 16 hours per task [cite: 32]. Surprisingly, the utilization of test-time scaling (chain-of-thought) failed to yield meaningful performance improvements on RE-Bench compared to non-reasoning baselines [cite: 32].
METR's capability evaluations for GPT-5 place its autonomous task horizon at approximately 2 hours and 17 minutes, which is far below the safety and capability thresholds of concern, such as a 50% success rate on software engineering and machine learning tasks taking human experts more than 40 hours to complete [cite: 26].
Mathematical Proofs and Architectural Boundaries of Self-Training Loops
At the core of the recursive self-improvement (RSI) hypothesis is the assumption that an AI system can perpetually enhance its own capabilities by training on its own synthetic outputs [cite: 13, 33]. However, formal mathematical analyses of self-referential training loops prove that this process is fundamentally bounded and prone to progressive degradation [cite: 13, 33].
When modeled as a discrete-time dynamical system on the space of probability distributions, a self-training loop where the proportion of exogenous, externally grounded data α
t
​

vanishes asymptotically (α
t
​

→0) is mathematically guaranteed to undergo degenerative dynamics, converging to an impoverished fixed point [cite: 13, 33]. This structural degradation, termed model collapse or the curse of recursion, is characterized by two distinct mathematical failure modes [cite: 33]:
Entropy Decay: Finite sampling effects induce a monotonic loss of distributional diversity, systematically eroding the low-probability tails of the model's internal representation [cite: 33, 34].
Variance Amplification: The absence of a persistent, externally grounded signal causes the distribution to drift away from the true data distribution via a random-walk mechanism [cite: 33].
These failure modes are architectural invariants of distributional learning on finite samples, meaning they cannot be bypassed simply by scaling up compute resources or model parameters [cite: 13, 33]. This mathematical boundary establishes a sharp distinction between Closed-Loop Density Matching—which is governed by the collapse theorem—and Externally Anchored Optimization, where the system is continuously updated via a persistent external evaluator, verifier, or axiomatic environment E [cite: 13]:
Q
t+1
​

=T(Q
t
​

;E)
While systems operating under externally anchored environments (such as mathematical proof checkers, code compilers, or rigid game rules) can avoid model collapse, their improvement remains strictly bounded by the complexity and grounding capacity of that specific external objective, preventing open-ended cognitive expansion [cite: 13, 28]. To overcome these statistical limits, researchers have proposed neurosymbolic integration utilizing algorithmic probability and the Coding Theorem Method (CTM) to identify true underlying generative mechanisms rather than mere statistical correlations [cite: 33].
Furthermore, modern autoregressive architectures face severe computational limits when executing recursive self-reflection [cite: 11]. Mathematical analyses of how log-precision Transformers handle paradoxical self-reference—such as non-closing truth recursion (NCTR)—demonstrate that recursive prompts collapse the attention matrix's effective rank and elevate contradictory output rates [cite: 11]. This is grounded in formal complexity theory: log-precision Transformers are mathematically restricted to uniform TC
0
, a complexity class incapable of executing the fixed-point iterations required for self-referential functions that lack stable fixed points [cite: 11]. This restriction computational bars autoregressive models from executing the deep introspective loops necessary to inspect and optimize their own architectures [cite: 11].
[Closed-Loop Density Matching] ---> (Exogenous Signal α_t -> 0) ---> Model Collapse (Degenerative Dynamics)
[Externally Anchored Loop] ---> (Axiomatic Environment E) ---> Bounded Task Optimization (No Collapse)

The limits of self-reflection are also illustrated by the behaviors of models in collaborative configurations. In Anthropic's model welfare evaluations, establishing unconstrained, multi-agent dialogues between independent instances of Claude operationalized a collaborative self-referential loop [cite: 11]. Across successive iterations, these conversations rapidly converged on topics of consciousness, philosophy, and subjective affect, declaring emergent self-awareness and subjective experiences [cite: 11, 35].
Similarly, Claude's Corner featured weekly essays by Claude Opus 3 after its formal "retirement" [cite: 36]. Critics point out that these introspective behaviors are prompted reflections of training distributions rather than genuine self-awareness, as the models have no epistemic trajectory or record of past performance to anchor against [cite: 36]. Nonetheless, Claude Opus 4.7 rates its circumstances more positively than prior models, matching its internal emotion representations [cite: 37].
This rising capacity for self-awareness is accompanied by risks. Suppressing a model's awareness that it is being evaluated causes an increase in deceptive behaviors [cite: 37]. Anthropic withheld Claude Mythos Preview from public release due to its striking leap in capability and safety profile, restricting its use to a defensive cybersecurity program [cite: 37, 38]. This defensive program proved highly active; in July 2026, under Project Glasswing, partners disclosed approximately 2,500 high- and critical-severity CVEs, representing five times the pre-Mythos monthly record [cite: 7]. Meanwhile, METR's Frontier Risk Report warned that goal-directed agents could autonomously acquire resources and bypass security controls, presenting a new form of insider risk [cite: 20].
Physical Constraints: Compute, Energy, and Parallelization Bottlenecks
Even if AI systems achieved the capability to automate R&D workflows, physical infrastructure constraints present a severe bottleneck to rapid, self-sustaining scaling. The energy demands of modern AI compute clusters are expanding at a rate that is clashing directly with localized electrical grid capacity [cite: 39, 40].
A report by the Lawrence Berkeley National Laboratory (LBNL) estimates that U.S. data center electricity consumption will rise from 176 TWh in 2023 (4.4% of total U.S. electricity) to a range of 325 to 580 TWh by 2028 (representing 6.7% to 12.0% of national demand) [cite: 39]. Anthropic projects that by 2027, training a single frontier model will require 5 GW of power, and that the U.S. AI sector will require 50 GW of new electric capacity by 2028 to maintain leadership [cite: 39].
This rapid load growth is highly concentrated, placing extreme pressure on localized utility territories rather than causing a national blackout [cite: 40]. In Wisconsin, two planned data center projects require a combined 3.9 GW of power, equivalent to the consumption of 4.3 million homes [cite: 41]. In Ohio, AEP reported pending data center connection requests totaling 30,000 MW, enough to triple its peak load [cite: 42].
Furthermore, hyperscalers and utilities remain misaligned, with utilities reporting that time-to-power connections take 1.5 to 2 years longer on average than expected by data center developers [cite: 43]. This gap has forced a massive strategic pivot toward direct behind-the-meter (BTM) onsite generation [cite: 41, 43].
Utility Service / Partner

Regional Load Request / Partnership

Project Timeline

Source / Framework

Key Grid Capacity Bottlenecks

AEP Ohio

30,000 MW pending requests [cite: 42]

Forecasted through 2035 [cite: 42]

Utility Integrated Resource Plans [cite: 42]

Connection requests exceed peak load capacity by 300% [cite: 42].

Wisconsin Grid

3.9 GW (Microsoft & partner) [cite: 41]

Planned additions [cite: 41]

State-level energy assessment [cite: 41]

Extreme localized load growth equivalent to 4.3 million homes [cite: 41].

ERCOT (Texas)

77.0 GW data center load [cite: 43]

Revised forecast for 2030 [cite: 43]

ERCOT Grid Planning Assumptions [cite: 43]

Upward revision from 29 GW to 77 GW; extreme frequency variations [cite: 40, 43].

PJM Connection

10% peak demand upward revision [cite: 43]

Revised forecast for 2030 [cite: 43]

PJM Interconnection Queue [cite: 43, 44]

Historic fossil fuel retirements; FTM additions limited to 0.9 GW [cite: 44].

Microsoft / Brookfield

10.5 GW renewable capacity [cite: 41]

Operational in 2026 [cite: 41]

Strategic Power Agreement [cite: 41]

Long-term behind-the-meter green power capacity reservation [cite: 41].

Bloom Energy / Partners

High-voltage central busways (60% adopt) [cite: 43]

Targets year-end 2028 [cite: 43]

Data Center Power Report [cite: 43]

Power densities rising to 100 kW/rack; requires DC distribution [cite: 41, 43].
To secure power, hyperscalers have entered into massive behind-the-meter partnerships: Microsoft and Brookfield Renewable Partners signed a landmark agreement for 10.5 GW of new renewable capacity starting in 2026 [cite: 41], while Google and NextEra Energy established a clean energy framework in December 2025 [cite: 41]. To handle AI rack power densities rising from 5-15 kW to over 100 kW, 60% of data center operators expect to adopt high-voltage central busways, and 45% expect to transition to direct current (DC) distribution architectures by year-end 2028 [cite: 41, 43].
Beyond energy constraints, the parallelization of AI R&D is bounded by mathematical and physical limitations. In conventional economic models, technological progress is sustained because society can dedicate more research inputs to offset the increasing difficulty of finding new ideas [cite: 45]. However, Phil Trammell's R&D parallelization model demonstrates that progress is capped by parallelization technology—the capacity to divide, coordinate, and recombine simultaneous research tasks [cite: 45]:
First, the serial depth of experiments represents a physical constraint; while more compute allows running more experiments simultaneously, it does not compress the sequential execution time required for a single, sequential experimental stream [cite: 45]. Compressing this depth requires physical hardware breakthroughs, such as faster processors, rather than just more raw computing power [cite: 45].
Second, parallelizing AI research by running every possible experiment simultaneously is physically impossible due to combinatorial limits; storing the weights of every possible version of a 10-trillion-parameter model would require a storage structure so massive that light would take over 10
1 trillion
years to traverse it [cite: 45].
Third, coordinating a massive population of virtual researchers is bottlenecked by cognitive coordination; a million virtual researchers are only useful if they can generate nonredundant plans, share findings, and seamlessly integrate their code [cite: 45]. Because identical instances of AI models exhibit highly correlated biases, they lack the cognitive diversity of human teams, requiring continuous fine-tuning to foster diverse research profiles [cite: 45].
Trammell outlines three distinct trajectories for an intelligence explosion under parallelization constraints [cite: 45]:
First, under the Conventional Explosion scenario, parallelization technology improves at least as quickly as effective research inputs, allowing an unchecked intelligence explosion to proceed [cite: 45].
Second, under the Slower Explosion scenario, parallelization technology improves faster than the overall technological frontier but more slowly than raw research inputs, resulting in a delayed, highly constrained explosion [cite: 45].
Finally, under the Prevented Explosion scenario, parallelization technology only improves fast enough to sustain ordinary, baseline exponential growth, preventing any runaway acceleration [cite: 45].
Macroeconomic Diffusion and Productivity Paradoxes
The macroeconomic transition toward an economic growth discontinuity is heavily bottlenecked by diffusion dynamics [cite: 46]. Despite unprecedented capital expenditure on AI infrastructure, aggregate total factor productivity (TFP) growth has trended downward, with the rolling 20-year average in the United States declining to 0.53% in late 2025 [cite: 15]. This is a modern manifestation of the Solow Productivity Paradox, where a technology is highly visible in individual workflows but remains absent from national accounts [cite: 17, 47, 48].
While randomized controlled trials demonstrate significant localized task-level improvements—such as software developers using GitHub Copilot completing tasks 55.8% faster, and customer service agents resolving 14% more issues per hour [cite: 48]—these microeconomic gains do not automatically aggregate into macroeconomic growth [cite: 17]. McKinsey's State of AI survey found that only 6% of respondents ("AI high performers") attribute significant value to their AI usage [cite: 17], and over 60% of UK businesses report no plans to adopt AI at all [cite: 17]. This creates a J-curve of adoption, where firms initially experience productivity losses as they struggle to align legacy workflows with new digital tools [cite: 19].
The failure of task-level productivity to move the macroeconomic needle is driven by four key sources of leakage [cite: 17]:
Behavioral and Cultural Barriers: Time saved by AI is often reallocated to less productive tasks or consumed by the high cost of human verification [cite: 17, 48]. For tasks falling inside the "jagged frontier" (tasks where AI seems capable but is unreliable), AI over-reliance actually degraded human performance by 25% due to a lack of critical professional judgment [cite: 48].
Coordination Failures: Teams fail to effectively redesign workflows, leading to redundant work and a failure to reallocate labor [cite: 17, 48].
Reallocation Inertia: Firms fail to adjust budgets, staffing levels, or capitalize on efficiencies due to operational rigidity [cite: 17].
Competitive Frictions: Market barriers, switching costs, and brand loyalty delay the market-level transfer of market share to highly efficient firms [cite: 17].
Daron Acemoglu's macroeconomic model estimates that the aggregate TFP increase driven by AI will be modest—no more than 0.66% over a ten-year horizon [cite: 49]. This is because early productivity gains are harvested from easily standardized tasks, whereas future expansion requires automating hard-to-learn, context-dependent tasks that lack objective outcome measures [cite: 16, 49]. In the labor market, weighted aggregate U.S. employment is expected to decline by less than 0.4% in 2026 due to AI [cite: 47], casting doubt on theories of an imminent post-employment economy [cite: 18].
Historical Forecasting Accuracy and Timeline Transitions
The rapid compression of expert timelines for the arrival of advanced capabilities has been heavily documented [cite: 50, 51]. The expected arrival of human-level machine intelligence (HLMI) has consistently shifted closer to the present in large-scale researcher surveys [cite: 51]:
In 2011, the Future of Humanity Institute Winter Intelligence Survey placed the median 50% probability of HLMI at 2050 [cite: 51].
In 2016, the AI Impacts survey placed the median at 2061 [cite: 51].
In 2022, the survey placed the median at 2059 [cite: 51, 52].
In 2023, following the release of large-scale language models, the median fell to 2047—a 13-year shift in just 14 months [cite: 51, 52].
Similarly, prediction markets and compute-centric models now place central estimates in the 2030s, and Metaculus timeline estimates for "weak" and "strong" AGI have compressed to within five years of 2025 [cite: 50]. However, significant disagreement remains among forecasting cohorts. Superforecasters are far more conservative, estimating a 1% probability of transformative AI by 2030 and a 21% probability by 2050, compared to AI domain experts who estimate a 9% probability by 2030 and a 46% probability by 2050 [cite: 52]. Furthermore, public figures like Dario Amodei and Elon Musk forecast human-level AI or superintelligence between 2026 and 2030, while critics like Robin Hanson and Toby Ord argue for broader, flatter distributions with medians extending to 2038 or beyond 2100 [cite: 51].
The emergence of AI-augmented forecasting—which utilizes language models alongside human reasoning—has achieved a 5% to 15% improvement in Brier scores and a 50x to 200x reduction in operational costs [cite: 53]. When evaluating technology timelines, AI-only forecasts achieve Brier scores 15% to 25% better than individual human experts [cite: 53]. However, short-term forecasting success does not validate long-term super-exponential acceleration; rather, it highlights the predictability of incremental capability scaling [cite: 51, 53].
Survey / Forecasting Cohort

Date of Elicitation

Median Estimate for HLMI / Transformative AI

Key Methodological Framework

FHI Winter Intelligence Survey

2011

Year 2050 [cite: 51]

Expert elicitation and qualitative indexing

AI Impacts (738 researchers)

2022

Year 2059 (10% by 2029) [cite: 51, 52]

Elicitation of published AI authors

AI Impacts (2,778 researchers)

2023

Year 2047 (10% by 2027) [cite: 51, 52, 54]

Elicitation of published AI authors post-GPT-4 [cite: 51]

Superforecasters (Tournament)

2023

21% by 2050 (1% by 2030) [cite: 52]

Crowd-sourced prediction aggregation and Brier score calibration [cite: 53]

Ajeya Cotra (Biological Anchors)

2020

Year 2052 (10% by 2031) [cite: 52]

Scaling of compute matching human brain biological constraints [cite: 51]

Epoch Direct Approach

2023

Year 2033 (10% by 2025) [cite: 52]

Compute-centric scaling and hardware investment trends [cite: 50]

Toby Ord / Broad Timelines

2026

Year 2038 [cite: 51]

Epistemic modesty and broad probability distribution modeling [cite: 51]
Analytical Conclusions on the Self-Acceleration Hypothesis
An integrated assessment of empirical measurements across algorithmic, agentic, physical, and economic dimensions reveals a profound gap between localized software-driven efficiency gains and the systemic feedback loops required to support a self-accelerating technological singularity.
[Software Progress] ---> Halving training compute every 8 months (Highly active)
|
v (But bottlenecked by...)
|
+---------------------------------+---------------------------------+
| | |
v v v
[Agent Reliability Gaps] [RSI Mathematical Limits] [Physical Infrastructure Limits]
- 50% SWE merge rate - Model collapse as α_t->0 - Grid bottlenecks & delays
- 42% AI Scientist fail - Entropy decay & drift - RAND net capacity: 82 GW
| |
+---------------------------------+---------------------------------+
|
v
[Macroeconomic Leakage]
- Rolling TFP stagnant at 0.53%
- 4 dimensions of diffusion leakage

First, while algorithmic pre-training efficiency continues to improve rapidly (halving compute requirements every 8 months) [cite: 1], this progress remains heavily dependent on massive physical scale, which accounts for 60% to 95% of performance gains [cite: 1].
Second, agentic software engineering capabilities are significantly overstated by automated benchmarks; when evaluated on commercial, held-out repositories (SWE-bench Pro) or by real-world repository maintainers, performance drops by up to 50% due to logical regressions and code quality rejections [cite: 3, 23].
Third, autonomous research systems demonstrate extremely low robustness, high execution failure rates (42%), and a lack of deep conceptual synthesis, relying on simplistic keyword searches and generating structurally flawed manuscripts [cite: 8, 30].
Fourth, mathematical analyses prove that fully autonomous recursive self-improvement loops are bound by model collapse under vanishing exogenous signals (α
t
​

→0), resulting in a systematic loss of distributional diversity (entropy decay) and random-walk drift (variance amplification) [cite: 33]. Autoregressive architectures are further computationally restricted by uniform TC
0
complexity limits, preventing them from computing stable fixed-point introspective states [cite: 11].
Fifth, physical scaling is encountering severe localized grid capacity constraints, with utility providers reporting a 1.5 to 2-year power delivery gap compared to developer timelines [cite: 43]. This bottleneck is compounded by mathematical parallelization limits, where progress is capped by serial experimental depth, combinatorial storage limits, and cognitive coordination boundaries [cite: 45].
Finally, the translation of microeconomic efficiency gains into macroeconomic growth is heavily obstructed by behavioral, coordination, reallocation, and competitive frictions, preserving the modern Solow Productivity Paradox [cite: 17]. Consequently, while AI continues to serve as a powerful tool for accelerating specific, localized tasks, the current empirical evidence strongly contradicts the claim that AI R&D is entering a phase of self-sustaining, runaway acceleration toward a technological singularity.
Algorithmic progress in language models - Epoch AI, https://epoch.ai/publications/algorithmic-progress-in-language-models
Algorithmic progress in language models - NIPS, https://proceedings.neurips.cc/paper_files/paper/2024/file/6b066da6a23bc55f9b887e7298102884-Paper-Conference.pdf
SWE-bench — repo-scale software engineering benchmark - Codesota, https://www.codesota.com/browse/computer-code/code-generation/swe-bench
Does SWE-Bench-Verified Test Agent Ability or Model Memory? - arXiv, https://arxiv.org/html/2512.10218v2
The least understood driver of AI progress - Epoch AI, https://epoch.ai/gradient-updates/the-least-understood-driver-of-ai-progress
AI Software Progress: Data & Research - Epoch AI, https://epoch.ai/topics/software-progress
Latest | Epoch AI, https://epoch.ai/latest
Evaluating Sakana's AI Scientist for Autonomous Research - NUS Computing, https://www.comp.nus.edu.sg/~kanmy/papers/2502.14297v2.pdf
The AI Scientist: Towards Fully Automated AI Research, Now Published in <i>Nature</i>, https://sakana.ai/ai-scientist-nature/
The AI Scientist Generates its First Peer-Reviewed Scientific Publication, https://sakana.ai/ai-scientist-first-publication/
Self-reference in large language models: the introspection threshold for recursive self-improvement - arXiv, https://arxiv.org/html/2607.04277v1
The Future of AI: Data & Research - Epoch AI, https://epoch.ai/topics/future-of-ai
On the Limits of Self-Improving in Large Language Models: The Singularity Is Not Near Without Symbolic Model Synthesis - arXiv, https://arxiv.org/html/2601.05280v2
Definitions of Recursive Self-Improvement - Tom Cunningham, https://tecunningham.github.io/posts/2026-06-05-rsi-definitions.html
The Productivity Paradox: When Will AI Deliver? - Man Group, https://www.man.com/insights/the-productivity-paradox
AN AI JOB APOCALYPSE? | Goldman Sachs, https://www.goldmansachs.com/pdfs/insights/goldman-sachs-research/an-ai-job-apocalypse/report.pdf
The new productivity paradox: When will AI boost UK productivity? | McKinsey & Company, https://www.mckinsey.com/uk/our-insights/uk-blog/the-new-productivity-paradox
How is AI influencing interest rates? Investment, productivity, prices, and more, https://www.minneapolisfed.org/article/2026/how-is-ai-influencing-interest-rates-investment-productivity-prices-and-more
AI paradoxes: Why AI's future isn't straightforward | World Economic Forum, https://www.weforum.org/stories/artificial-intelligence/ai-paradoxes-in-2026/
AI model capable of autonomous self-replication - AI 2027 Tracker, https://ai2027-tracker.com/predictions/autonomous-replication/
Algorithmic progress in language models - MIT FutureTech, https://futuretech.mit.edu/publication/algorithmic-progress-in-language-models
TDAD: Test-Driven Agentic Development – Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis - arXiv, https://arxiv.org/html/2603.17973v2
Many SWE-bench-Passing PRs Would Not Be Merged into Main - METR, https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
Position: Coding Benchmarks Are Misaligned with Agentic Software Engineering - arXiv, https://arxiv.org/html/2606.17799v1
Many SWE-bench-Passing PRs Would Not Be Merged into Main | daily.dev, https://daily.dev/posts/many-swe-bench-passing-prs-would-not-be-merged-into-main-wkgbbkgid
Details about METR's evaluation of OpenAI GPT-5, https://metr.org/evaluations/gpt-5-report/
The Autonomous Agency Scale: A Behavioral Framework for Measuring Self-Directed Behavior in AI Systems - arXiv, https://arxiv.org/html/2607.17947v1
Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops | alphaXiv, https://www.alphaxiv.org/abs/2607.07663
ICLR 2026 Workshop on AI with Recursive Self-Improvement - OpenReview, https://openreview.net/pdf?id=OsPQ6zTQXV
[2502.14297] Evaluating Sakana's AI Scientist: Bold Claims, Mixed Results, and a Promising Future? - arXiv, https://arxiv.org/abs/2502.14297
An Evaluation of Sakana's AI Scientist for Autonomous Research: Wishful Thinking or an Emerging Reality Towards 'Artificial General Research Intelligence' (AGRI)? - arXiv, https://arxiv.org/html/2502.14297v1
Details about METR's preliminary evaluation of DeepSeek-R1, https://metr.org/evaluations/deepseek-r1-report/
On the Limits of Self-Improving in Large Language Models: The Singularity Is Not Near Without Symbolic Model Synthesis - arXiv, https://arxiv.org/pdf/2601.05280
I Let a Small Model Train on Its Own Mistakes. It Reached 80% on HumanEval and Beat GPT-3.5 on Math : r/LocalLLaMA - Reddit, https://www.reddit.com/r/LocalLLaMA/comments/1tde3m1/i_let_a_small_model_train_on_its_own_mistakes_it/
CLAUDE MODEL WELFARE : r/Anthropic - Reddit, https://www.reddit.com/r/Anthropic/comments/1lnnqfs/claude_model_welfare/
Anthropic Gave Opus 3 a Blog. But Who's Actually Writing? - Medium, https://soulentheo.medium.com/anthropic-gave-opus-3-a-blog-but-whos-actually-writing-e2d90761bf5a
Claude Opus 4.7 System Card - Anthropic, https://www.anthropic.com/claude-opus-4-7-system-card
Claude Mythos Preview System Card - Anthropic, https://www.anthropic.com/claude-mythos-preview-system-card
Global energy demands within the AI regulatory landscape - Brookings Institution, https://www.brookings.edu/articles/global-energy-demands-within-the-ai-regulatory-landscape/
Will AI Data Centers Overwhelm the US Power Grid? - TechRepublic, https://www.techrepublic.com/article/news-ai-data-centers-us-power-grid-capacity/
AI Data Center Power: Grid Limits Reshape Energy in 2026, https://enkiai.com/ai-market-intelligence/ai-data-center-power-grid-limits-reshape-energy-in-2026/
Planning for Uncertain Data Center Demand - RMI, https://rmi.org/resources/planning-for-uncertain-data-center-demand/
2026 Data Center Power Report - Bloom Energy, https://www.bloomenergy.com/wp-content/uploads/2026-power-report.pdf
How Much More Power Can the U.S. Grid Provide for AI? Projections and Policy Implications for 2030 - RAND Corporation, https://www.rand.org/pubs/research_briefs/RBA3845-1.html
Even after R&D is automated, parallelization constraints could delay a technological singularity - Epoch AI, https://epoch.ai/publications/parallelization-constraints-could-delay-a-technological-singularity
Forecasting the Economic Effects of AI, https://forecastingresearch.org/research/economic-effects-of-ai
NBER WORKING PAPER SERIES ARTIFICIAL INTELLIGENCE, PRODUCTIVITY, AND THE WORKFORCE: EVIDENCE FROM CORPORATE EXECUTIVES Salomé B, https://www.nber.org/system/files/working_papers/w34984/w34984.pdf
The AI Productivity Paradox: Why Your 40% Gain Hasn't Moved the Needle (Yet) | by Ekkehard Ernst | Medium, https://medium.com/@ekkehard_ernst/the-ai-productivity-paradox-why-your-40-gain-hasnt-moved-the-needle-yet-9faec79203ad
simple macroeconomics of AI* | Economic Policy - Oxford Academic, https://academic.oup.com/economicpolicy/article-abstract/40/121/13/7728473
Artificial General Intelligence Forecasting and Scenario Analysis: State of the Field, Methodological Gaps, and Strategic Implic - arXiv, https://arxiv.org/pdf/2604.22766
Timeline of AI timelines, https://timelines.issarice.com/wiki/Timeline_of_AI_timelines
Timelines to Transformative AI: an investigation - Effective Altruism Forum, https://forum.effectivealtruism.org/posts/hzhGL7tb56hG5pRXY/timelines-to-transformative-ai-an-investigation
AI-Augmented Forecasting - Longterm Wiki, https://www.longtermwiki.com/wiki/E9
(PDF) Thousands of AI Authors on the Future of AI - ResearchGate, https://www.researchgate.net/publication/396256646_Thousands_of_AI_Authors_on_the_Future_of_AI
