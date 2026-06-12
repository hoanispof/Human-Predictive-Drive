# [POST] My Research: A Computational Cognitive Neuroscience Perspective on Alignment

> **Platform:** LessWrong
> **Link:** https://www.lesswrong.com/posts/MuLvZxMcy5WaKJu3H/my-research-a-computational-cognitive-neuroscience
> **Author:** Seth Herd
> **Ngày post:** 2026-06-05
> **Ngày lưu:** 2026-06-07
> **Ghi chú:** Full content via LessWrong GraphQL API. ~51K chars, 7 sections + footnotes.
>   File này = reference only, không edit.

---

## BÀI VIẾT GỐC (FULL)

*Note - title edited to be more descriptive.*

This is a summary of the work I've done and work I plan to do, and the theories of change and AI progress that motivate my work. I've been working full-time on alignment for three years and change, and thinking about brainlike AGI and its alignment increasingly often since 2004.

Here's the research agenda in one breath: I'm trying to predict what the first transformative AI will be, in enough mechanistic detail that we can predict likely failure modes of its alignment. That's in service of finding interventions that address those failure modes efficiently, so that they can realistically be implemented even if timelines are short and work is rushed. I'm using my background in computational cognitive neuroscience to predict what might be called loosely brainlike AGI: LLMs with added human-like cognitive capacities. This and my other approaches are adaptations of the integrative secondary research approach as well as the knowledge and perspective I have after working in a niche subfield we called computational cognitive neuroscience for about 23 years.

I'll give a summary in the rest of this section, then give a little more depth on each major thread of my work in the remaining sections. All of it is pretty brief.

### Approach and premises

Most alignment work falls roughly into one of two broad categories: empirical study of current systems ("prosaic alignment"), or theory about idealized agents ("agent foundations") (with much variation and many notable exceptions). There are two assumptions implicit in these approaches: the first is that the AI we're trying to align will be like current AI. The second is that we have no idea what the AI we need to align will look like, so we must work on the fully general problem. I think there's a neglected third option: carefully predicting properties of the first AIs in which it's really important to get alignment right. I'm trying to make alignment plans that both anticipate new difficulties and take advantage of the strengths of LLMs.

I'm trying to predict how LLMs might be augmented to reach takeover-capable AI (TCAI), beyond scaling the current approach. I'm looking at how developers might add systems for continuous learning and executive function, and how those would create new challenges for alignment. I present the case that this is the most likely route to the AI competent and agentic enough to control the future, and therefore the type of AI most crucial to align. (I don't think this is certain; something like Steve Byrnes' "Brain in a box in a basement" could overtake it, given some otherwise-helpful limitations inherent in the LLM approach).

I'm pleased to see more people reasoning explicitly and mechanistically about the transition from current LLMs to transformative and takeover-capable LLM-based AGI. There is visibly more now than three years ago. I think there's still too little of it for comfort. Of course no one is a pure empiricist or pure theorist, but in practice the field still seems fairly strongly divided by perspective, although the delta is encouraging.

My background gives me an unusual angle on predicting the form of our first TCAI. It's in "computational cognitive neuroscience", a rare type of integrative work. I worked for 23 years in a lab that built neural network models of brain function, ranging from basic attention and vision, to attention for executive function, to System 2 serial processing for complex thought and decision-making. These models were in service of integrative secondary research, a fancy name for reading a lot of empirical work and theory, and thinking hard and collaboratively about how it all fit together. I was lucky and privileged to spend most of my time reading and thinking about how brain systems come together to produce human thought and knowledge, and the computational principles of why it works as it does.

I think it's likely (50%-90%, uncertain) that the first TCAI will be advanced LLMs, scaffolded and trained to have cognitive faculties they now lack relative to humans. This is a specific bet, but I think some insights from taking this perspective apply to broader forms of network-based AGI. These are principally some degree of persistent memory/learning, metacognition for uncertainty and error detection, and executive function for planning and thought management. These together will enable autonomous, goal-directed, long-horizon work. I think the first TCAIs will probably be aligned much like current systems (RLHF, constitutional AI/deliberative alignment, character training), with some modest additions (§2.2), but those same alignment techniques will create different final alignment, based on emergent effects of those added cognitive capacities.

That is a bet on what might be called loosely brainlike cognition. Current LLMs are already surprisingly brainlike in some ways. LLMs are arguably much like humans' cortical areas for language (Broca's & Wernicke's areas). I think the brain's abundant recurrence serves a similar function to transformers' architecture of attention modulating connections from past serial token processing. Of course this mapping is rough, with many important differences. One is that LLMs capture more semantic knowledge or crystallized intelligence than human language cortices.

On this perspective, LLMs have a route to human-like competence with more human-like systems, training, and thinking. And the incentives are driving people to create those rapidly. Standard LLM scaleup receives the most effort, but substantial work is underway on novel systems and training methods for each of those missing elements of human cognition (reviewed in the work I summarize in the next section).

### Philosophy of the approach

Accurate, detailed predictions of how we'll try to align AGI would allow efficient use of limited alignment time and effort. My primary theory of change is that spreading clearer thinking about likely paths to AGI and alignment will improve our average efficiency and foresight on crucial alignment issues.

This research agenda is messier than focusing on specific technical problems or approaches, or assuming rather than predicting a particular form of AGI/TCAI. This first-principles, all-inclusive approach has substantial downsides, but seems like a useful bet in conjunction with those types of more focused work.

I think my work takes relatively neglected approaches. Gears-level models (in this case, of likely TCAI architectures) can be considered expensive and so rare Capital Investments. Such work may also be difficult to automate and so get little developer attention at crunch time (but see §4.2 on AI for epistemics). These issues do receive attention, and increasingly more, but I think they're still neglected relative to their potential impact.

The forms of first TCAI and alignment efforts will in part be shaped by commercial, social, and political forces. Thus, my work has spread somewhat to these topics, since work there seemed severely lacking when I started working on the problem.

---

## §2 — Technical work

My main work is in what might be called semi-technical alignment and predictions. It's making, refining, and sharing gears-level models of likely first TCAI, alignment techniques likely to be used for it, and likely failure points and risk models. The theory of change is spreading those models and claims as broadly as possible through writing and discussion, so that we've collectively thought more about the specifically relevant questions when crunch time hits.

### 2.1 Predicted paths to TCAI

TCAI won't work like a human brain, but it will likely incorporate some elements of human cognition.

**Memory (continuous learning):**
Episodic memory is now becoming useful: notes in coding scaffolds; there are vector memory systems in OpenClaw. Fine-tuning functions much like human semantic memory. Such beyond-session memory or learning during deployment creates an alignment stability problem (§5.2).

**Executive function and metacognition:**
This is the other major direction I see distinguishing LLM cognition from fully human-level competence. Scaffolding for task structure, plans, and long-term goals is just getting off the ground in coding scaffolds and agentic scaffolds like OpenClaw. I'm now hoping that better metacognition will produce better AI for epistemics and automated alignment, faster than it accelerates capabilities. This will of course be tricky to aim for, and it's not clear how hard anyone is trying.

My early work in 2023 focused on scaffolding LLMs into "language model cognitive architectures" (LMCAs). This turned out to be largely wrong about speed and ordering. AutoGPT and similar systems with vector-based memory systems and prompting for executive function did not quickly become useful. But these predictions were correct about the heavy focus on chain-of-thought or System 2 as a step from early LLMs to human-like cognitive competence.

### 2.2 Predicted paths to (mis)alignment

**Internal independent review** is another likely alignment technique for such scaffolded LLM systems. I called this internal independent review because it's internal to the agentic scaffold or harness. But it's independent, because a separate model instance could be called to review actions or plans before they're executed. This approach would span the line between AI control and alignment.

A review process, standing between an agent's main LLM "cognitive engine" and actions-you-don't-like, such as writing fanfic porn on your social media account, or making plans to overthrow humanity.

This could be a nontrivial addition to training-based LLM alignment, because such review happens before actions affect either the world or internal memories and beliefs. This approach still seems promising and likely to be included as we near AGI. Auto mode in Code and Codex is a minimal version. Such a review process could probably be circumvented by a highly intelligent base LLM, but it could be useful as part of a hodge-podge approach to an "alignment MVP" that is weakly and spikily superhuman, and could aid with automated alignment research.

**Goals selected from learned knowledge:** explored the implications of aligning pretrained LLMs, rather than performing alignment purely through RL. This refers to a whole class of alignment techniques, but centers on prompting LLMs as one means of aligning them. This sounds laughably weak as an alignment solution, but it still looks likely to be part of the first human-plus LLM AGI's alignment approach. Coding scaffolds maintain plan and subgoal lists, and inject current goals as prompts at intervals. The important perspective is that alignment will be an emergent property of a system, with the alignment of the core LLM an important part of the composite system's alignment, but not the only part.

**System 2 Alignment:** expanded on independent reviews for alignment, and related techniques. Writing this piece convinced me that techniques for capabilities will also provide new alignment techniques with low alignment taxes. It's valuable for efficiency and reputation to control models' thoughts and behaviors. That can be done with scaffolding and/or training to monitor and review actions, plans, and chains of thought. Extra efficiency is increasingly important as long-horizon tasks consume more expensive compute. The current scaffolding for plans and to-do lists in coding scaffolds like Claude Code and Codex is a nascent form of this type of scaffolding. I predict that these techniques will be expanded when Mythos and similarly capable models are released. I also looked at some ways these techniques could be circumvented by a scheming (deceptively aligned) base LLM.

---

## §3 — Research background in computational cognitive neuroscience

I joined a PhD program in 1999, and worked in that same lab until mid-2022. We built integrative models of how brain systems produce human thought; I focused on complex, serial thinking. We called this computational cognitive neuroscience, since we were trying to work across computer science, cognitive psychology, and various branches of neuroscience. We built theoretical and computational models of attention, executive function, serial deliberation, decision-making, episodic and working memory, and models combining those systems.

The point of that work wasn't the models themselves; it was the computational principles they illustrated, the why of human cognition. I spent most of my time reading and thinking about how brain systems come together, rather than building elaborate networks. I'm applying a similar research strategy to the similarly-difficult problem of understanding how future AGI will work and be aligned.

I hope this perspective gives me some relevant comparative advantages. One might be in seeing which cognitive functions LLM agents currently have and lack, relative to humans. Another could be seeing the emergent effects that adding those capacities could have on capabilities and alignment.

My neuroscience work included some theories I've never written about before, since I was worried they might accelerate progress in brainlike AGI (I now think they wouldn't and won't, since LLMs have eclipsed brainlike approaches).

**[Expandable section: Selected specifics of computational cognitive neuroscience career]**

My PhD advisor was Randy O'Reilly. His advisor was Jay McClelland, co-author of the Parallel Distributed Processing volumes (1986 & 1987) that established "connectionism" as an approach in cognitive psychology and neuroscience.

I progressively turned my studies to how neural networks' fundamentally parallel operation becomes the fundamentally serial operation of System 2 cognition, roughly chain-of-thought in humans.

My dissertation was on the neural mechanisms of visual search. This added detail and solid empirical backing to the theory of how attention is an emergent effect of neural networks, and it controls what we do and what we think about by essentially the same mechanisms by which it controls what we perceive. This is a pretty central mechanism for how the brain seems to pull off complex thought; it attends to (very roughly) one thought at a time for maximum processing power on each one, then serializes those into more complex chains of thought in System 2 processing.

**Serial processing from parallel networks:** The central answer I reached was a dynamic in which the brain naturally proceeds from one "thought" or brain-state to another, related one. This dynamic is created in a neat, simple way: neurons fire continuously to represent information; they "get tired" of firing by depletion of resources; this lets new neurons representing new information or "thoughts" start firing, but which ones are a product of the complex pattern of information in the last brain-state. This allows attractor dynamics, and serial progression or "chain of thought."

In 2013: "strategic cognitive sequencing" — a collection of small computational models that illustrated how brain systems could come together to strategically select next thoughts, and so do useful cumulative cognitive work.

In 2021: "neural mechanisms of human decision-making" — Selecting the right "next thought" is often a mini-decision. These quick, strategic "internal actions" are superimposed on the "automatic," emergent means of selecting a topic-relevant next thought through the attentional dynamics of constraint satisfaction in a laterally connected network. This happens in a system for internal action selection that's a rough copy of the system that controls selection of motor actions.

**Episodic memory and catastrophic forgetting:** The brain uses a separate system (hippocampus and medial temporal lobe) to learn fast without a high learning rate on the whole system, so that new knowledge can be stored but sequestered, to see if it's important enough to learn (and thereby overwrite previous memories). We do this by replaying important memories from the episodic memory store, thus "consolidating" important memories into our general semantic knowledge, at a speed and depth appropriate to their estimated importance.

---

## §4 — Societal influences on AI safety

### 4.1 Government and public opinion on AI progress

In "Whether governments will control AGI is important and neglected", I analyzed how government control could shift the alignment and AI risk challenges. It would likely reduce between-lab race dynamics, at the cost of accelerating a race with China. I now think government control before TCAI is likely, and international cooperation with China is plausible; but those are loosely held.

There's been an interesting blindspot going two ways: most of the public, including experts, assumes that AI is roughly static; they're not accounting for progress. Meanwhile, most of the AI safety community is assuming that public opinion is static, and won't change when AI changes. I think public opinion will change, like it rapidly changed from ignoring to obsessing about COVID.

In "If we solve alignment, do we die anyway?" I wondered if proliferation of intent-aligned AGI might create competitive dynamics along with new strategies and superweapons that might be almost as risky as misaligned AGI. This substantially shifted my hopes back from instruction-following to value-aligned AGI, since that keeps ASI out of the control of dangerous individual humans.

### 4.2 AI progress and epistemics

I analyzed how we might improve AI for epistemics by differentially improving metacognition for identifying uncertainty and correcting errors. This would reduce the "Median Doom-Path: Slop, not Scheming" risk — in which advanced AI helps us produce alignment solutions we can't evaluate, and helps us convince ourselves they will work, acting as yet another amplifier of our motivated reasoning and confirmation bias.

I believe that motivated reasoning and confirmation bias are polarizing beliefs about AI progress into camps of optimists that feel emotionally in conflict with pessimists or "doomers". This creates a very large risk that politicians and others with power over AI development will simply choose whichever beliefs they find convenient in the short term, since there's an available pool of "careful expert opinions" for either need.

---

## §5 — Alignment targets

### 5.1 Corrigibility/instruction-following vs. value alignment

DWIMAC or instruction-following alignment mitigates many deep problems with value alignment, if it's used even modestly wisely; the AI can be instructed to be maximally helpful and honest. There are of course problems, but I weakly believe these are easier in sum than those of value alignment. However, this approach has one enormous downside: it leaves humans in charge of the future, with increasingly lethal capabilities at their disposal.

Claude's new constitution seems primarily aimed at value alignment; yet it also weakly states remaining under human control as the first priority. The constitution reads to me as though Anthropic is collectively undecided on which or what mix of these alignment targets to aim at. OpenAI and DeepMind appear to be more oriented toward instruction-following as the target.

### 5.2 Stability as an alignment target

The need for any technical alignment solution to be robust to the inevitable goal drift and ontology shift from a system that learns continuously. My first publication on alignment was "Goal changes in intelligent agents" (2018).

I attempted to integrate the main threads of my research in "LLM AGI may reason about its goals and discover misalignments by default" (September 2025). This is an attempt to convey a gears-level model of the first takeover-capable AGI, in service of thinking through how its alignment might shift under the effects of improved reasoning, deployment in different tasks, and continual learning allowing for long time-horizon work.

---

## §6 — Future work

Listed in approximately descending level of priority:

1. **Refining gears-level models of aligned LLM AGI** — "nobody knows how hard alignment is, and that's a dangerous position to be in"
2. **Confirmation bias and motivated reasoning** — effects on alignment research and public opinion
3. **Metacognition to reduce LLM slop-related alignment risks** — differential improvement toward better epistemics
4. **Government will assert control of AGI projects** — increasingly obvious
5. **Sequence on continuous learning** — collaboration with Rohan Subramini / Aether Research
6. **Solving the whole problem** — "I doubt we'll find any one solution to the alignment problem"

---

## §7 — Collaboration

"I benefit from talking to people with different perspectives and expertise. Collaboration with people we disagree with is tricky, but in my experience, it's the fastest route to real progress in science."

"I also have some time to talk to people who are just getting started in alignment, particularly if their interests overlap with the type of integrative work I do."

---

## FOOTNOTES

**[1]** New alignment challenges will be introduced if and when AI has situational awareness, alignment change through reflection and continuous learning, and context changes from more diverse tasks and broader action affordances (particularly escape, explicit scheming, and takeover). My perspective could be framed as: prosaic alignment adjacent in models of AI and alignment techniques; agent foundations adjacent in risk models.

**[2]** I use the term takeover-capable AI to emphasize the threat model I'm addressing in this work. I use TCAI to include AI that takes control by deliberately and secretly aligning a stronger successor AI to itself, as in the scenario of AI 2027.

**[3]** I am thinking of people like Ryan Greenblatt, Alex Mallen, Daniel Kokotajlo, and others. The AI Futures Project and their AI 2027 scenario are the most visible examples of this type of gears-level prediction work.

**[4]** While I focus on loosely brainlike LLM-based AGI, some of the insights from taking this perspective apply more broadly. These include more pure versions of today's LLMs, ranging to more thoroughly RL-based approaches like Steve Byrnes' brain-like AGI as a possible first TCAI.

**[5]** Brains of course have many properties that current LLMs lack. One I don't focus on is the RL action-selection system, and the resulting self-directed continual RL learning. I emphasize similarities, because I think Humans provide an untapped wealth of evidence about alignment and future capabilities both.

**[6]** Some ideas that now seem obvious and important took a surprising amount of time and effort to develop and diffuse. Unfortunately, I think there are equally strong arguments for other areas of alignment research being neglected, since the overall effort is still small relative to the likely stakes.

**[7]** This parallels Michael Nielsen's excellent work in reconsidering alignment as a goal — spreading new capacities for destruction might be the biggest impact of technology in general and AI in particular.
