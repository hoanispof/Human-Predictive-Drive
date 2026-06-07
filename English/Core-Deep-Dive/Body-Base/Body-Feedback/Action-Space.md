---
title: Action-Space — Per-Person Capability Landscape Observation
version: 1.0
created: 2026-05-19
source_version: Vietnamese v1.0
english_created: 2026-06-06
status: OBSERVATION FILE v1.0
scope: |
  OBSERVATION FILE: Each person has their own ACTION SPACE —
  the total set of capabilities available at any moment: what they know, what they can access,
  what they're permitted to do, and HOW MUCH of it they're AWARE of.
  Action-Space is NOT a per-gap property (covered by Gap-Direction.md).
  Action-Space = AGGREGATE SUPPLY-SIDE property —
  views the FULL options landscape OF ONE PERSON.
  Gap-Distribution-Profile = DEMAND side (what I WANT).
  Action-Space (THIS FILE) = SUPPLY side (what I CAN DO).
  ACTUAL BEHAVIOR = f(Gap-Distribution × Action-Space).
  4 axes: ① Compiled Capacity × ② Resource Access × ③ Freedom × ④ Awareness.
  3 types of constraint: Blocked / Dependent / Invisible (invisible = most dangerous).
  Positive/Negative spiral dynamics across the 4 axes.
  Formation model parallel to Gap-Distribution (collective infrastructure → social position → education → hardware).
purpose: |
  Gap-Distribution-Profile.md: DEMAND — where gaps cluster.
  MECHANISM FILES: per-concept (Status=resource, Autonomy=self-action, Obligation=cost...).
  THIS FILE: AGGREGATE SUPPLY-SIDE VIEW:
    → Views action space as a PER-PERSON PROFILE
    → Bridge: scattered capability concepts → unified supply-side observation
    → Observation tool: helps SEE the current capability landscape
    → Prediction tool: Gap-Distribution × Action-Space → behavioral prediction (4 quadrants)
    → Gap-Distribution × Action-Space = COMPLETE behavioral prediction framework
  = The missing aggregate view between "per-concept mechanism" and "aggregate behavior prediction"
dependencies:
  - Gap-Distribution-Profile.md v1.0 — sibling file, demand side, 4 axes, 4-layer formation
  - Gap-Direction.md v2.0 — per-gap mechanism, "unknown = no gap" (§5.3)
  - Status.md v2.1 — §1 Resource Access Map (axis ②)
  - Autonomy-Hardware.md v1.1 — §2 vmPFC/DRN controllability (axis ④ hardware)
  - Autonomy.md v1.1 — software development of autonomy (axis ④ software)
  - Compliance-Floor.md v2.0 — freedom constraints, 4-layer floor (axis ③)
  - Obligation.md v1.1 — obligation as constraint, 5-factor formula (axis ③)
  - Money-Analysis.md v1.0 — money = bridge technology (axis ②)
  - Inter-Body-Mechanism.md v1.0 — Compilable Architecture, PFC=Lawyer, 3-cost model
  - Chunk.md v2.2 — sole substrate, compilation
  - Body-Feedback-Label.md v2.0 — vocabulary reference
  - Connection.md v4.0 — Dunbar layers (social capital)
  - Drill-Entity-Compiled-Capacity.md v1.0 — Dunbar layers, Depth × Breadth = constant
  - Domain-Mapping-Drive.md v1.0 — reward from PROCESS, threshold
  - Background-Pattern.md v1.1 — Background-Pattern self-reinforcing, identity lock
  - Self-Created-Threat.md v1.0 — 4 types, awareness
  - Expansion-Saturation-Crisis.md v1.1 — Expansion→Discovery shift
research:
  - Sen 1999 (Nobel) — Capability Approach, development = freedom to achieve various lifestyles
  - Bandura 1977 — Self-efficacy, belief in capability → behavior prediction
  - Heckman 2006 — Early childhood intervention ROI = 7-10% annual
  - Kruger & Dunning 1999 — Competence ↔ self-assessment paradox (overestimate)
  - Maier & Seligman 2016 — Learned helplessness = DEFAULT, vmPFC learns "controllable"
  - Deci & Ryan 2000 — Self-Determination Theory, autonomy, competence, relatedness
  - Dunbar 1992, Zhou et al. 2005 — Social Brain Hypothesis, layered structure (~5/15/50/150)
  - Putnam 2000 — Social capital, bonding vs bridging
  - Bourdieu 1986 — 3 capitals, economic + social + cultural
  - Vroom 1964 — Expectancy Theory, behavior = f(expectancy × valence)
  - Kahneman & Deaton 2010 — Emotional well-being income plateau
  - Tedeschi & Calhoun 2004 — Post-traumatic growth
  - Chase & Simon 1973 — Expertise restructures perception
  - Dollard et al. 1939 — Frustration-aggression hypothesis
language: English
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Action-Space — Per-Person Capability Landscape Observation

> **Two people. Both want to escape poverty. Same neighborhood. Both 25 years old.**
> **Same gap. Same drive. Same body-need firing.**
>
> **Person A: speaks English, has a laptop, has friends in IT,**
> **knows they can learn to code.**
> **Person B: speaks only one language, has no computer,**
> **only knows their neighbors, doesn't know what "IT" is.**
>
> **SAME GAP. COMPLETELY DIFFERENT OPTIONS.**
> **Person A sees 5 paths forward. Person B sees 0.**
>
> **Not because B is lazy. Not because B doesn't want it.**
> **B DOESN'T KNOW ANY PATH EXISTS.**
>
> **Gap-Distribution-Profile: "What do I WANT?" — demand side.**
> **This file: "What CAN I do?" — supply side.**
>
> **Actual behavior = f(what you want × what you can do).**
> **Missing either side = you only see half the picture.**
>
> **And action space doesn't come naturally.**
> **It is FORMED by: collective infrastructure → social position →**
> **education + family → hardware + accumulated experience.**
>
> **This file: viewing action space as a PERSONAL PROFILE,**
> **WHERE it forms from, HOW to observe it, and WHAT it can predict.**

---

## Table of Contents

- §0 — POSITION + SCOPE
- §1 — DEFINITION: Action-Space = Supply-Side Profile
- §2 — 4 OBSERVATION AXES
- §3 — 3 TYPES OF CONSTRAINT
- §4 — SPIRAL DYNAMICS
- §5 — FORMATION MODEL
- §6 — SHIFT MECHANISMS
- §7 — EXPANSION QUALITY: DEPTH-FIRST PRINCIPLE
- §8 — Gap-Distribution × Action-Space: BEHAVIORAL PREDICTION
- §9 — CASES
- §10 — RESEARCH ANCHORS
- §11 — HONEST ASSESSMENT
- §12 — OPEN QUESTIONS
- §13 — CROSS-REFERENCES

---

## §0 — POSITION + SCOPE

```
⭐ THIS FILE IN THE FRAMEWORK:

  Core-Deep-Dive/Body-Base/Body-Feedback/ — OBSERVATION FILE.

  DIFFERENTIATED FROM NEARBY FILES:

    ┌──────────────────────────┬──────────────────────────────────────┐
    │ File                     │ Answers                              │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Gap-Distribution-        │ DEMAND: Where do gaps cluster?       │
    │ Profile.md v1.0          │ Per-person gap landscape.            │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ ⭐ THIS FILE              │ SUPPLY: Where are options available? │
    │ Action-Space.md          │ Per-person capability landscape.     │
    │                          │ Gap-Distribution × Action-Space      │
    │                          │ = behavioral prediction.             │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Status.md v2.1           │ Resource Access Map (1 DIMENSION).   │
    │                          │ This file uses THAT + 3 more axes.   │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Autonomy-Hardware.md     │ WHY self-action = reward.            │
    │                          │ = 1 mechanism WITHIN axis ④.         │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Obligation.md v1.1       │ Cost to MAINTAIN agent access.       │
    │                          │ = 1 constraint WITHIN axis ③.        │
    ├──────────────────────────┼──────────────────────────────────────┤
    │ Compliance-Floor.md v2.0 │ Minimum legal constraints.           │
    │                          │ = 1 constraint WITHIN axis ③.        │
    └──────────────────────────┴──────────────────────────────────────┘

  → Status, Autonomy, Obligation, Compliance-Floor = per-concept DEEP dives.
  → This file = AGGREGATE view (entire supply-side landscape)
  → COMPLEMENTS — does not duplicate existing mechanisms.


SCOPE IN:
  ✅ Action space as per-person aggregate supply-side property
  ✅ 4 observation axes (Compiled Capacity, Resource Access, Freedom, Awareness)
  ✅ 3 types of constraint (Blocked, Dependent, Invisible)
  ✅ Positive/Negative spiral dynamics across 4 axes
  ✅ Formation model (Collective Infrastructure → Hardware)
  ✅ Shift mechanisms per axis
  ✅ Gap-Distribution × Action-Space behavioral prediction (4 quadrants)
  ✅ Cases: observable examples
  ✅ Sen's Capability Approach as research anchor

SCOPE OUT:
  ❌ Per-concept mechanism → Status.md, Obligation.md, etc.
  ❌ Per-gap mechanism → Gap-Direction.md
  ❌ Demand side → Gap-Distribution-Profile.md
  ❌ Prescribing "what action space should look like" → framework = DESCRIPTIVE
  ❌ Per-era empirical data → application layer
```

---

## §1 — DEFINITION: Action-Space = Supply-Side Profile

### §1.1 — From per-concept to aggregate

```
⭐ MECHANISM FILES DESCRIBE PER-CONCEPT. THIS FILE DESCRIBES THE FULL SUPPLY-SIDE.

  Currently, the framework has:
    → Status.md: Resource Access Map (what I can access from which agent)
    → Autonomy.md: tendency toward self-direction (how much I prefer self-action)
    → Obligation.md: cost to maintain access (what I pay for access)
    → Compliance-Floor.md: legal limits (what I am NOT permitted to do)
    → Chunk.md: accumulation mechanism (how chunks compile)
    → Entity-Compiled-Capacity: Dunbar ceiling (how many relationships)

  This file ADDS:
    → Each person has a CAPABILITY SPACE at each moment
    → This space = TOTALITY: what they know + what they can access +
      what they're permitted + what they're aware of
    → = AGGREGATE SUPPLY-SIDE PROPERTY
    → = PER-PERSON, PER-MOMENT, CONTINUOUSLY CHANGING

  EXAMPLE:
    Person A at time T:
      Compiled Capacity: knows 3 languages, has IT degree, 10 years experience
      Resource Access: high income, 200-contact network, owns property
      Freedom: professional freedom, no debt, adult children
      Awareness: knows they can found a startup, knows the market, knows the risks
      → Action-Space A: VERY WIDE — many options available

    Person B at time T:
      Compiled Capacity: finished 9th grade, knows farming, physically healthy
      Resource Access: low income, knows only neighbors, no capital
      Freedom: must support aging parents, bank debt, only 1 occupation
      Awareness: doesn't know scholarships exist, doesn't know online courses exist
      → Action-Space B: VERY NARROW — few options available

  → A and B differ NOT because of IQ or "willpower"
  → But because ACTION SPACE differs → different options → different behavior → different life
```

### §1.2 — Action-Space as distribution (not a single point)

```
⭐ EACH PERSON = 1 DISTRIBUTION, NOT 1 POINT:

  LIKE Gap-Distribution §1.2 — Action-Space should NOT be described in one word:
    WRONG: "This person has a wide action space" (oversimplification)
    RIGHT: "This person has DEEP capacity in IT, MODERATE resource access,
           HIGH freedom, NARROW awareness outside their domain"

  Action-Space has a "PROFILE":
    → 4 axes INDEPENDENT — combining creates a unique per-person profile
    → Some axes WIDE (many options), some NARROW (few options)
    → Each axis has STRONG and WEAK zones
    → Example: Einstein 1905 — EXTREMELY DEEP capacity (physics) + NARROW resource (clerk)
               + OK freedom (had free time) + HIGH awareness (knew he was good at physics)

  Action-Space is CONTINUOUSLY CHANGING:
    → Each day compiles more chunks → axis ① expands
    → Earning/spending money → axis ② fluctuates
    → Laws change, obligations added/removed → axis ③ shifts
    → Meeting new people, reading, listening → axis ④ can expand SUDDENLY
    → = Dynamic, per-moment, NOT fixed

  Action-Space NOT FULLY SELF-KNOWN:
    → PFC = Lawyer (Inter-Body-Mechanism §7): self-assessment = BIASED
    → Axis ④ (Awareness) specifically describes the gap between ACTUAL and PERCEIVED
    → = Can only be OBSERVED, not PRECISELY MEASURED (like Gap-Distribution §1.2)
```

### §1.3 — Gap-Distribution × Action-Space = Behavioral Prediction

```
⭐⭐ ACTUAL BEHAVIOR = f(Gap-Distribution × Action-Space):

  Gap-Distribution (demand): "What do I WANT?" → where gaps cluster
  Action-Space (supply): "What CAN I do?" → where options are available
  Behavior: INTERSECTION OF THE TWO — only where gap AND option MEET → action

  4 QUADRANTS:

    ┌───────────────────────────────────┬──────────────────────────────────┐
    │ High Gap-Distribution + High Action-Space │ High Gap-Distribution + Low Action-Space │
    │                                   │                                  │
    │ = ACTIVE PURSUIT                  │ = FRUSTRATION / STUCK            │
    │ Want + can → action               │ Want + can't → suffering         │
    │ Example: researcher with a lab    │ Example: artist in poverty       │
    │ Example: entrepreneur with capital│ wanting to create art but forced │
    │ → Productive, confident           │ to work a factory job            │
    │                                   │ → Chronic dissonance, possible   │
    │                                   │   learned helplessness           │
    ├───────────────────────────────────┼──────────────────────────────────┤
    │ Low Gap-Distribution + High Action-Space  │ Low Gap-Distribution + Low Action-Space  │
    │                                   │                                  │
    │ = DRIFT / WASTE                   │ = SIMPLE / TRAPPED               │
    │ Can + don't want → NO DRIVE       │ Don't want + can't               │
    │ Example: person with every        │ → Narrow life, stable but limited│
    │ advantage but feeling "bored"     │ Example: isolated rural farmer — │
    │ → Lottery winner case             │ few gaps, few options, simple    │
    │ → "Has everything but doesn't     │ life → peaceful OR invisible trap│
    │    know what they want"           │                                  │
    └───────────────────────────────────┴──────────────────────────────────┘

  ⭐ MOST CRITICAL QUADRANT: High Gap-Distribution + Low Action-Space
    → This is the SUFFERING quadrant
    → Body fires real gap (demand exists) but NO WAY TO FILL IT (supply insufficient)
    → = Chronic cortisol holding (Cortisol-Baseline §7: Role ② sustained)
    → = If prolonged → learned helplessness (Maier & Seligman 2016)
    → = Education + resource access = 2 main levers to move toward Q1

  ⭐ Gap-Distribution AND Action-Space INFLUENCE EACH OTHER:
    → Action-Space expands → new domains accessible → new chunks → new gaps form → Gap-Distribution shifts
    → Gap-Distribution shifts → new drive → effort builds capacity → Action-Space expands
    → = FEEDBACK LOOP — not one-directional
    → Education primarily = expand Action-Space ④ (awareness) → trigger feedback loop


🟡 Gap-Distribution × Action-Space 4-quadrant model = framework synthesis
🟢 Behavior = f(capability × motivation): Vroom 1964 Expectancy Theory
🟢 Frustration when blocked: Dollard et al. 1939
```

---

## §2 — 4 OBSERVATION AXES

### §2.0 — Overview

```
⭐ 4 ORTHOGONAL AXES — EACH DESCRIBES A DIFFERENT DIMENSION OF ACTION SPACE:

  ┌────────────────┬──────────────────────┬──────────────────────────────────┐
  │ Axis           │ Question             │ Observable proxy                  │
  ├────────────────┼──────────────────────┼──────────────────────────────────┤
  │ ① Compiled     │ What do I KNOW,      │ Skills, education, languages,     │
  │   Capacity     │ what can I DO?       │ years experience, certifications  │
  ├────────────────┼──────────────────────┼──────────────────────────────────┤
  │ ② Resource     │ What can I           │ Income, savings, network size,    │
  │   Access       │ ACCESS?              │ tools, social capital             │
  ├────────────────┼──────────────────────┼──────────────────────────────────┤
  │ ③ Freedom      │ What am I            │ Legal constraints, obligations,   │
  │                │ PERMITTED to do?     │ dependencies, social norms        │
  ├────────────────┼──────────────────────┼──────────────────────────────────┤
  │ ④ Awareness    │ What do I KNOW       │ Self-assessment accuracy,         │
  │                │ I'm capable of?      │ domain exposure, meta-cognition   │
  └────────────────┴──────────────────────┴──────────────────────────────────┘

  4 axes INDEPENDENT — combine to create unique per-person profile.
  → ① says WHAT IS THERE. ② says WHAT CAN BE ACCESSED. ③ says WHAT IS PERMITTED. ④ says WHAT I KNOW ABOUT MYSELF.

  COMPARISON WITH Gap-Distribution 4 AXES:
    Gap-Distribution: ① WHERE gaps ② WHY there ③ HOW shaped ④ HOW STABLE
    Action-Space:     ① WHAT can do ② WHAT can access ③ WHAT allowed ④ WHAT aware of

  Gap-Distribution = DEMAND → "landscape of what I want"
  Action-Space = SUPPLY → "landscape of what I can do"
```

### §2.1 — Axis ① Compiled Capacity (what you know, what you can do)

```
⭐ COMPILED CAPACITY = TOTAL CHUNKS: KNOWLEDGE + SKILLS + PHYSICAL ABILITY:

  DEFINITION:
    → "Arsenal" available at time T
    → = Total chunks compiled: domain knowledge, motor skills, languages,
        social skills, physical fitness, professional expertise
    → = f(years exposure × domain fit × compile depth)

  2 SUB-DIMENSIONS:

    DEPTH (deep in one domain):
      → Years of deliberate practice/exposure → chunks compile deep
      → Deep = see patterns others miss (Chase & Simon 1973)
      → Deep = high reward when gap fills (compound effect)
      → Examples: chess master 20 years, surgeon 15 years, physicist 30 years

    BREADTH (wide across many domains):
      → Exposure to many domains → chunks compile across domains
      → Breadth = versatility, bridge function
      → Breadth = more options per situation
      → Examples: T-shaped designer, polyglot, generalist manager

    DEPTH × BREADTH ≈ CONSTANT (Drill-Entity-Compiled-Capacity §5):
      → Finite compilation resource — going deep in one domain = less for others
      → = Tradeoff, NOT failure
      → Specialist: narrow-deep. Generalist: broad-shallow. T-shaped: hybrid.


  ⭐ INVISIBLE BOUNDARY — MOST IMPORTANT:

    "Unknown = no gap" (Gap-Direction §5.3) applies DIRECTLY:
      → Compiled Capacity = BOTH actual capability AND boundary of awareness
      → Doesn't know Python exists → no gap about "wanting to learn Python"
                                   → no option "use Python to solve this"
      → = INVISIBLE CONSTRAINT (§3.3): doesn't know the option exists → NO SIGNAL

    IMPORTANT DISTINCTION:
      → ACTUAL capability (compiled chunks) = axis ① → measurable
      → PERCEPTION of capability = axis ④ → perception gap
      → Axis ① and ④ RELATED but DIFFERENT:
        ① "I know how to code in Python" (fact)
        ④ "I know that I know how to code in Python" (meta-awareness)
        ④ "I DON'T know that Go language exists" (invisible boundary)


  OBSERVABLE PROXIES:
    → Education level, certifications, years of experience
    → Skills demonstrated (not just claimed)
    → Languages spoken, tools mastered
    → Physical ability, health status
    → = Proxy — each proxy captures only PART of the picture

🟢 Expertise restructures perception: Chase & Simon 1973
🟢 Depth × Breadth tradeoff: Roberts et al. 2009 (Dunbar relationship layers)
🟢 "Unknown = no gap": Gap-Direction §5.3 (established framework principle)
```

### §2.2 — Axis ② Resource Access (what you can reach)

```
⭐ RESOURCE ACCESS = STATUS.MD RESOURCE ACCESS MAP EXTENDED:

  DEFINITION:
    → Status.md §1: "who gives me what without a fight"
    → This file REFRAMES: resource access = ALL resources that can be mobilized
    → = NOT ONLY social status — includes material + social + knowledge access

  3 TYPES OF RESOURCE:

    MATERIAL (physical):
      → Money, assets, tools, equipment, workspace
      → Money = bridge technology (Money-Analysis §1.2):
        → Standardizes cross-domain costs
        → Converts implicit → explicit obligation
        → Scales community exchange
      → = Options that MONEY CAN BUY

    SOCIAL CAPITAL (network):
      → Who is willing to help? → Dunbar layers (Entity-Compiled-Capacity §1.2)
        S1 ~5: intimate — willing to help unconditionally
        S2 ~15: close — help when asked
        S3 ~50: friends — help within their means
        S4 ~150: active — introductions, information
      → Network BREADTH + DIVERSITY (Putnam 2000):
        Bonding capital: network of SIMILAR people → emotional support
        Bridging capital: network of DIFFERENT people → access to new domains
      → = Options that NETWORK CAN OPEN

    KNOWLEDGE ACCESS (access to learning):
      → Internet, libraries, mentors, peer groups
      → DIFFERENT from axis ①: this is ACCESS (can reach), not COMPILED (already knows)
      → Example: having internet = POTENTIAL access (but not yet compiled)
      → Example: having a mentor = access to GUIDANCE (accelerates compile)
      → = Options that INFRASTRUCTURE ALLOWS


  ⭐ MONEY = MULTIPLIER FOR AXIS ②, NOT EVERYTHING:
    → Money BUYS material resource → axis ② expands
    → Money partially BUYS social access (events, clubs) → axis ② partial
    → Money CANNOT BUY compiled capacity → axis ① requires TIME
    → Money CANNOT BUY freedom directly → axis ③ requires legal/social change
    → Money CANNOT BUY awareness → axis ④ requires exposure + meta-cognition
    → = Money important but NOT sufficient for full Action-Space expansion

  ⭐ DIMINISHING RETURNS (Kahneman & Deaton 2010):
    → $0 → $30K/year: massive Action-Space expansion (survival → options)
    → $30K → $100K: moderate expansion (comfort → more options)
    → $100K → $1M: marginal expansion (premium access)
    → $1M+: near-zero expansion (luxury ≠ more options)
    → = Resource access has a CEILING — more money ≠ proportionally more Action-Space


  OBSERVABLE PROXIES:
    → Income, savings, assets
    → Network size + diversity
    → Access to mentors, experts
    → Infrastructure available (internet, library, transport)

🟢 Status = Resource Access Map: Status.md §1 (established framework)
🟢 Social capital: Putnam 2000, Bourdieu 1986
🟢 Income ↔ well-being plateau: Kahneman & Deaton 2010
🟢 Dunbar layers: Zhou et al. 2005
```

### §2.3 — Axis ③ Freedom (degree of freedom to act)

```
⭐ FREEDOM = EXTERNAL CONSTRAINTS: WHAT PREVENTS ME FROM USING ① AND ②:

  DEFINITION:
    → Compliance-Floor.md: "freedom = default, law = exception"
    → This axis: TOTAL external constraints currently limiting options
    → = Know (①) + Have (②) + PERMITTED (③) = option actually available

  4 SOURCES OF CONSTRAINT:

    LEGAL (law):
      → Compliance-Floor 4-layer: body-base + chunks + melody space + collective
      → "Cannot kill, steal, deceive, trespass" → appropriate constraints
      → "Cannot operate a business without a license" → bureaucratic constraint
      → "Cannot leave the country" (some regimes) → oppressive constraint
      → = NECESSARY constraints (protect others) + EXCESS (limit freedom beyond need)

    SOCIAL NORMS:
      → "Women shouldn't be engineers" (many societies)
      → "Must marry before 30" (Collective-Schema-Pressure)
      → NOT law but FUNCTIONING LIKE LAW:
        Violating → social punishment (Collective-Body §2: compile paths)
      → = Invisible constraint when unaware, visible when awareness increases

    OBLIGATIONS:
      → Obligation.md: compiled prediction about cost to maintain access
      → "Must support elderly parents" → constrains career options
      → "Bank debt" → constrains spending/risk-taking
      → "Must keep job for family" → constrains exploration
      → = Obligation REDUCES freedom BUT provides access (tradeoff)

    DEPENDENCY:
      → Children: depend on parents → freedom ≈ 0 (appropriate, developmental)
      → Employee: depends on boss → freedom at work = limited
      → Debt: depends on creditors → freedom = constrained
      → = Dependency = INVERSE of autonomy (Autonomy.md §3.1)


  ⭐ PHYSICAL CONSTRAINT = EDGE CASE:

    Most modern people ≈ NOT constrained by physical geography:
      → Watching ocean videos = compiling ocean chunks (shallower than a diver but still)
      → Internet + travel = access to nearly any domain
      → = Everything = patterns in the brain

    WHEN physical constraint EXISTS (prison, serious illness, severe disability):
      → Crushes axis ② (resource access) to ≈ 0
      → Crushes axis ③ (freedom) to ≈ 0
      → Axis ① (capacity) REMAINS (what is known is still known)
      → Axis ④ (awareness) REMAINS (what one knows one can do, is still known)
      → = Already captured in the 4 axes — no 5th axis needed

    Example: Stephen Hawking — ①④ very high, ②③ crushed by ALS
      BUT: technology (wheelchair, voice synthesizer) = partial restoration of ②③
      → = Physical constraint ≈ crashes ②③ but technology can partially compensate


  OBSERVABLE PROXIES:
    → Legal status (citizen, visa, undocumented)
    → Debt level, financial obligations
    → Family obligations (dependent parents, children)
    → Social norm pressure (cultural context)
    → Physical freedom (health, mobility, location)

🟢 Development = freedom: Sen 1999 (Capability Approach)
🟢 Compliance Floor = harm principle: Mill 1859
🟡 4 constraint sources = framework synthesis (integrating multiple files)
```

### §2.4 — Axis ④ Awareness (knowing what you are capable of)

```
⭐⭐ AWARENESS = GAP BETWEEN ACTUAL ACTION SPACE AND PERCEIVED ACTION SPACE:

  DEFINITION:
    → Axes ①②③ describe the ACTUAL ACTION SPACE (objective)
    → Axis ④ describes HOW MUCH YOU KNOW ABOUT YOURSELF (subjective)
    → Gap between actual and perceived = OBSERVATION TARGET OF THIS AXIS

  PFC = LAWYER (Inter-Body-Mechanism §7):
    → PFC is NOT a neutral judge
    → PFC = advocate for body-base: creates narratives defending actions body ALREADY wants
    → → Self-assessment = BIASED — always
    → = Why axis ④ is SEPARATE from ①②③


  3 STATES:

    UNDER-ESTIMATE: "I can't" but actually CAN
      → Learned helplessness: vmPFC atrophied → DRN not suppressed →
        default "helplessness" NOT OVERRIDDEN (Maier & Seligman 2016)
      → Compiled suppress: "acting independently = punishment" compiled from childhood
        (Autonomy.md §1.2: Child B scolded when they tried)
      → → Actual Action-Space wider than perceived → options IGNORED
      → → Body STILL fires reward for self-action (hardware) but
        software overrides → "know I should act but don't dare"

    ACCURATE: perception ≈ reality — RARE
      → Requires: wide domain exposure + meta-cognition + domain feedback
      → = "Know what I know, know what I DON'T know" (Socratic paradox)
      → = Optimal but ASYMPTOTIC — nobody is 100% accurate

    OVER-ESTIMATE: "I'm sure I can" but LACKING chunks
      → Dunning-Kruger 1999: low competence + low meta-cognition →
        "I'm good" (because don't know what they're missing)
      → Recent graduate: "4 years of university = expert" → reality shock
      → → Perceived Action-Space wider than actual → TRY but FAIL → recalibrates
      → → Failure = PAINFUL but = recalibration mechanism


  ⭐⭐ INVISIBLE CONSTRAINT: ESPECIALLY IMPORTANT

    Axis ④ connects to §3.3 (Invisible constraint):

    Not knowing an option EXISTS = NO GAP FOR IT:
      → Doesn't know scholarships exist → doesn't apply → opportunity missed
      → Doesn't know online learning exists → doesn't learn → capacity stuck
      → Doesn't know career path X exists → doesn't pursue → life path limited

    WHEN awareness INCREASES → invisible BECOMES visible:
      → "Oh, there's a way to do this?" → option SUDDENLY available
      → 1 conversation → 1 book → 1 video → axis ④ expands SUDDENLY
      → = CHEAPEST to expand (doesn't require years) but HARDEST to trigger
        (because invisible = doesn't know what to look for)

    EDUCATION = CONVERTING INVISIBLE → VISIBLE:
      → Education DOESN'T ONLY teach skills (axis ①)
      → Education PRIMARILY OPENS EYES (axis ④):
        "Oh, this domain exists. This career path exists."
      → → Invisible constraint → Blocked/Dependent → SOLVABLE
      → → = WHY education = the most powerful intervention


  OBSERVABLE PROXIES:
    → Degree of match between self-assessment and external assessment
    → Response when encountering new information: "oh, that's possible?" = expanding
    → Domain exposure breadth (how many fields does the person know exist)
    → Willingness to seek feedback + update self-model

🟢 Dunning-Kruger 1999: low competence → overestimate
🟢 Maier & Seligman 2016: learned helplessness = DEFAULT, vmPFC learns controllable
🟢 Bandura 1977: self-efficacy → behavior prediction
🟡 Invisible constraint taxonomy = framework synthesis
```

### §2.5 — 4 axes combined — Examples

```
🟡 5 PROFILE EXAMPLES (simplified — reality = more nuanced):

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 1: "Einstein at 25"                                       │
  │ ① Capacity: EXTREMELY DEEP (physics) + narrow (few other domains) │
  │ ② Resource: LOW (clerk, low salary, limited academic network)     │
  │ ③ Freedom: MODERATE (had free time, not pressured)               │
  │ ④ Awareness: HIGH (knew he was good at physics, knew the field)  │
  │                                                                   │
  │ ⭐ Action space NARROW but SUFFICIENT for HIS gap:                 │
  │ Only needs paper + time + intellect = ENOUGH for physics          │
  │ → Gap-Distribution × Action-Space MATCH: abstract gap + abstract  │
  │   capacity = productive                                           │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 2: "Factory worker"                                       │
  │ ① Capacity: NARROW (1 specialist skill, few other domains)        │
  │ ② Resource: LOW (low income, limited network, few tools)          │
  │ ③ Freedom: MODERATE (legal freedom, but debt + family obligations)│
  │ ④ Awareness: LOW (doesn't know other options exist)              │
  │                                                                   │
  │ ⭐ Narrow Action-Space × Narrow Gap-Distribution = narrow but STABLE life:  │
  │ No frustration (because doesn't know other options) → invisible trap         │
  │ NEEDS: education ④ → opens eyes → options visible → Gap-Distribution        │
  │ can shift                                                         │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 3: "Recent university graduate"                           │
  │ ① Capacity: EMERGING (academic knowledge, limited practical)      │
  │ ② Resource: LOW (little money, network = classmates)             │
  │ ③ Freedom: OPENING (few obligations, few dependencies)           │
  │ ④ Awareness: SEARCHING (knows many fields but not deep in any)   │
  │                                                                   │
  │ ⭐ Action-Space EXPANDING + Gap-Distribution FINDING ITS CENTER:   │
  │ "Quarter-life crisis" = Action-Space opening but Gap-Distribution  │
  │ not yet converging → many options but doesn't know what they want │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 4: "Child with controlling parents"                       │
  │ ① Capacity: LOW (still compiling, little experience)              │
  │ ② Resource: DEPENDENT (entirely dependent on parents)            │
  │ ③ Freedom: DEPENDENT (parents decide everything)                 │
  │ ④ Awareness: INVISIBLE (doesn't know other ways of living exist) │
  │                                                                   │
  │ ⭐ ALL 4 AXES LOW → ACTION SPACE ≈ 0:                              │
  │ No frustration because invisible constraint → doesn't know → stays│
  │ WHEN awareness grows (growing up, meeting friends, internet):     │
  │ ④ ↑ → sees options → "why am I controlled?" → frustration BEGINS │
  │ → Breaking free possible BUT axes ②③ still dependent → conflict  │
  └───────────────────────────────────────────────────────────────────┘

  ┌───────────────────────────────────────────────────────────────────┐
  │ PROFILE 5: "Lottery winner"                                       │
  │ ① Capacity: UNCHANGED (money doesn't buy skill)                  │
  │ ② Resource: EXPLOSIVE EXPANSION (money expands suddenly)         │
  │ ③ Freedom: INCREASES (fewer dependencies, fewer financial         │
  │             obligations)                                          │
  │ ④ Awareness: UNCHANGED (doesn't know what to do with money)     │
  │                                                                   │
  │ ⭐ AXIS ② EXPLODES + AXES ①④ CAN'T KEEP UP:                       │
  │ Gap-Distribution hasn't shifted yet → "wealthy but doesn't know  │
  │ what they want"                                                   │
  │ Options expand suddenly but gaps still at body-domain level       │
  │ → Over-consume body-domain fills → hedonic adaptation → empty    │
  │ Reward-Calibration §3.4: premature access → bypasses process     │
  └───────────────────────────────────────────────────────────────────┘

  ⚠️ THESE PROFILES ARE SIMPLIFIED. Reality = far more nuanced.
     Use to ILLUSTRATE the axes, NOT to categorize people.
```

---

## §3 — 3 TYPES OF CONSTRAINT

### §3.0 — Overview

```
⭐⭐ 3 TYPES OF CONSTRAINT — FUNDAMENTALLY DIFFERENT IN THE INSIDER'S EXPERIENCE:

  Same option missing. 3 DIFFERENT reasons. 3 DIFFERENT experiences.

  ┌────────────────┬──────────────────┬──────────────┬──────────────────────┐
  │ Type           │ Mechanism        │ Experience   │ Observable           │
  ├────────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ BLOCKED        │ Knows option,    │ Frustration  │ "I know there's a   │
  │                │ NOT PERMITTED    │ Anger        │ way but I'm not      │
  │                │ (axis ③ blocks)  │ Resistance   │ allowed" → Protest   │
  ├────────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ DEPENDENT      │ Knows option,    │ Acceptance   │ "I know there's a   │
  │                │ INSUFFICIENT     │ (temporary)  │ way but don't have   │
  │                │ resource         │ Planning     │ the conditions yet"  │
  │                │ (axis ② lacking) │              │ → Plan               │
  ├────────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ INVISIBLE      │ DOESN'T KNOW     │ NOTHING      │ No behavior related  │
  │                │ option exists    │ (no gap)     │ to the option        │
  │                │ (axis ④ = 0)    │ False peace  │ → Silent absence     │
  └────────────────┴──────────────────┴──────────────┴──────────────────────┘
```

### §3.1 — Blocked: knows but isn't permitted

```
⭐ BLOCKED = FRUSTRATION:

  Mechanism:
    → Person KNOWS option X exists (axis ④ has awareness)
    → Person HAS capacity/resource for X (axes ①② sufficient)
    → BUT axis ③ BLOCKS: law prohibits, norm prohibits, others prevent
    → → Gap EXISTS + fill path EXISTS + BLOCKED = frustration

  EXAMPLES:
    → Wants to run a business but law bans private enterprise
    → Wants to attend university but "women don't need education" (norm)
    → Wants a divorce but "think of the children" (obligation)
    → Wants to enter politics but "doesn't have the right background" (status gate)

  BODY RESPONSE:
    → Frustration = cortisol sustained (gap fires + fill path blocked)
    → Long-term: can lead to → protest / circumvention / suppression
    → 🟢 Dollard et al. 1939: frustration → aggression hypothesis

  ⭐ BLOCKED = HAS ENERGY → CAN RESOLVE:
    → Because knows the option + knows it's blocked → HAS A TARGET to address
    → Lobbying, advocacy, legal challenge, migration = strategies
    → = SOLVABLE (though costly)
```

### §3.2 — Dependent: knows but not yet resourced

```
⭐ DEPENDENT = TEMPORARY ACCEPTANCE:

  Mechanism:
    → Person KNOWS option X exists (axis ④ has awareness)
    → Person LACKS SUFFICIENT resource for X (axis ② lacking)
    → OR lacks sufficient capacity (axis ① lacking)
    → → Gap EXISTS + fill path EXISTS + CONDITIONS NOT YET MET = temporary acceptance

  EXAMPLES:
    → Wants to open a restaurant but not yet enough capital → saves → waits
    → Wants to pursue a PhD but not yet enough knowledge → keeps learning → waits
    → Wants to leave home but not yet old enough / earning enough → builds capacity → waits

  BODY RESPONSE:
    → Cortisol MODERATE (gap fires + fill path known + timeline unclear)
    → PFC can PLAN: "if I save X months → enough"
    → → Cortisol DECREASES when plan exists (certainty ↑)

  ⭐ DEPENDENT = HAS DIRECTION → MOTIVATING:
    → Knows option + knows what's missing → HAS DIRECTION to build toward
    → = Source of drive, not despair
    → Education, mentorship, resource building = strategies
    → = SOLVABLE given TIME
```

### §3.3 — Invisible: doesn't know the option exists

```
⭐⭐ INVISIBLE = MOST DANGEROUS — BECAUSE THERE IS NO SIGNAL:

  Mechanism:
    → Person DOESN'T KNOW option X exists (axis ④ = 0 for X)
    → → "Unknown = no gap" (Gap-Direction §5.3)
    → → NO GAP for X → NO DRIVE toward X
    → → NO FRUSTRATION → NO ENERGY TO SEARCH
    → → = "FALSE PEACE" — doesn't know they're being limited

  EXAMPLES:
    → 18th-century farmer: doesn't know "voting rights" exist → doesn't demand them
    → Controlled child: doesn't know "children have rights" → accepts everything
    → Worker: doesn't know "free online courses" exist → doesn't learn
    → Patient: doesn't know "therapy X" exists → doesn't seek it

  BODY RESPONSE:
    → NONE. This is THE PROBLEM.
    → Frustrated person SEARCHES for solutions (has energy).
    → Dependent person BUILDS toward solutions (has direction).
    → Invisible person DOES NOTHING — because THERE IS NO GAP.
    → = WHY invisible is the MOST DANGEROUS:
      Blocked = pain → seeks a way out
      Dependent = waiting → builds
      Invisible = peaceful → stuck FOREVER (unless someone "opens their eyes")

  ⭐ INVISIBLE → VISIBLE: THE MOMENT OF "OH":
    → 1 conversation: "Did you know there are overseas scholarships?"
      → ④ expands → gap FORMS → frustration/motivation BEGINS
    → 1 book: "This career path exists"
      → ④ expands → new option VISIBLE → decision now possible
    → Internet exposure: video showing a different way of living
      → ④ expands → awareness: "life can be like THIS?"
    → = CHEAPEST intervention (cost = 1 conversation)
      BUT HARDEST to trigger (invisible = can't search for what you don't know)

  ⭐ EDUCATION = ANTI-INVISIBLE MECHANISM:
    → Education DOESN'T ONLY teach skills (axis ①)
    → Education PRIMARILY converts INVISIBLE → VISIBLE (axis ④)
    → → Invisible options → Blocked or Dependent
    → → BLOCKED/DEPENDENT = SOLVABLE (because you know the problem + direction)
    → → = WHY "education is the foundation of development" (Sen 1999)

🟢 "Unknown = no gap": Gap-Direction §5.3 (established)
🟢 Capability = opportunity set: Sen 1999 (Nobel)
🟡 Invisible constraint taxonomy + "false peace" = framework synthesis
🔴 Invisible constraint = most dangerous (logical, untested empirically)
```

---

## §4 — SPIRAL DYNAMICS

### §4.1 — Positive spiral (privilege, compound advantage)

```
⭐ 4 AXES INTERACT → POSITIVE SPIRAL:

  ① → ②: Knowledge EXPANDS resource access
    → Knowing English → wider market → more income + network
    → Knowing the law → negotiate better → access legal resources
    → Deep domain skill → high-value output → more money

  ② → ①: Resource EXPANDS knowledge
    → Having money → access to education → compiles faster
    → Having network → mentors → guided compile → faster + deeper
    → Having tools → practice efficiently → compiles better

  ③ → ①②: Freedom ENABLES use of ① and ②
    → Time freedom → use YOUR capacity → build more
    → Financial freedom → invest resources → grow portfolio
    → = Being imprisoned → ①② become meaningless (capacity EXISTS but CANNOT USE)

  ④ → ①②③: Awareness ACTIVATES everything
    → Knowing options exist → seek capacity, resource, freedom
    → Knowing you can → USE ①②③ instead of ignoring them
    → = Not knowing you can → stuck (even if ①②③ are sufficient)

  POSITIVE SPIRAL:
    ① ↗ → ② ↗ → ③ ↗ → ④ ↗ → ① ↗↗ → ② ↗↗ ...
    Example: Education → job → money → freedom → know more options
             → more education → better job → ...

  = "PRIVILEGE" = positive spiral in ALL 4 axes simultaneously
  = COMPOUND ADVANTAGE — each axis reinforces the others

🟢 Heckman 2006: early childhood intervention compound returns
🟢 Bourdieu 1986: capital reproduction across generations
🟡 4-axis positive spiral = framework synthesis
```

### §4.2 — Negative spiral (poverty trap)

```
⭐ THE REVERSE → NEGATIVE SPIRAL:

  ① ↘ → ② ↘ → ③ ↘ → ④ ↘ → ① ↘↘ ...

  Example: Little education → few skills → low income → little freedom (debt, dependency)
           → little awareness (doesn't know options) → even less education → ...

  = "POVERTY TRAP" = negative spiral in ALL 4 axes simultaneously
  = COMPOUND DISADVANTAGE — each axis drags the others down

  ⭐ INVISIBLE CONSTRAINT MAKES THE TRAP MORE COMPLETE:
    → Negative spiral + invisible constraint = DOESN'T KNOW THEY'RE TRAPPED
    → Blocked: pain → seeks a way out
    → Invisible: "everybody lives this way" → stays put → trap deepens

🟢 Poverty trap: established development economics concept
🟢 Compound disadvantage: Wilson 1987 (The Truly Disadvantaged)
🟡 4-axis negative spiral + invisible amplification = framework synthesis
```

### §4.3 — Intervention points

```
🟡 INTERVENTION PER AXIS — ASYMMETRIC COST:

  ┌────────────┬──────────────────┬──────────────┬──────────────────────┐
  │ Axis       │ Intervention     │ Cost         │ Timeframe            │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ① Capacity │ Education,       │ HIGH         │ YEARS                │
  │            │ training, mentor │ (time+effort)│ (compile takes time) │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ② Resource │ Financial aid,   │ VARIABLE     │ IMMEDIATE-MEDIUM     │
  │            │ network access,  │ (depends on  │ (money = fast,       │
  │            │ infrastructure   │ amount)      │ network = slow)      │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ③ Freedom  │ Legal reform,    │ VERY HIGH    │ SYSTEMIC             │
  │            │ social change,   │ (collective  │ (generations)        │
  │            │ debt relief      │ action)      │                      │
  ├────────────┼──────────────────┼──────────────┼──────────────────────┤
  │ ④ Awareness│ Exposure, travel,│ CHEAPEST     │ SUDDEN POSSIBLE      │
  │            │ conversation,    │ (1 convo     │ (1 moment can change │
  │            │ internet, mentor │ can change)  │ everything)          │
  └────────────┴──────────────────┴──────────────┴──────────────────────┘

  ⭐ AXIS ④ PARADOX:
    → Cheapest intervention WHEN IT WORKS
    → Hardest to TRIGGER: invisible = can't search for what you don't know
    → REQUIRES: external catalyst (teacher, friend, internet, mentor)
    → = WHY "meeting the right person" can change a life

  ⭐ OPTIMAL INTERVENTION = ④ + ① SIMULTANEOUSLY:
    → Open eyes (④) + build capacity (①) → feedback loop BEGINS
    → Resource (②) follows as a consequence
    → Freedom (③) may need systemic support
    → = Sen 1999: development = expanding capabilities (= expanding Action-Space)

🟢 Education as development: Sen 1999, Heckman 2006
🟡 Intervention per axis + ④ paradox = framework synthesis
```

---

## §5 — FORMATION MODEL

### §5.0 — Overview: where does Action-Space form from?

```
⭐⭐ ACTION SPACE = f(4 LAYERS STACKED ON TOP OF EACH OTHER):
  (Parallel to Gap-Distribution §4 — 4 layers for DEMAND, this file's 4 layers for SUPPLY)

  ┌─────────────────────────────────────────────────────────────────┐
  │ LAYER 4: COLLECTIVE INFRASTRUCTURE (slowest, widest)             │
  │   Economy, technology, which systems EXIST?                      │
  │   → DEFINES: which options are AVAILABLE to the population      │
  │   → Rural 1960: building abstract-domain capacity nearly         │
  │     IMPOSSIBLE (no widespread universities, internet, global     │
  │     market)                                                      │
  │   → 2026: internet + AI → options EXPAND for everyone           │
  │   → Silicon Valley: startup infrastructure → entrepreneurship   │
  │     options ABUNDANT                                             │
  └────────────────────────────┬────────────────────────────────────┘
                               ▼ filtered through social position
  ┌─────────────────────────────────────────────────────────────────┐
  │ LAYER 3: SOCIAL POSITION (medium speed, medium breadth)          │
  │   Born where? Into which family? Which class?                   │
  │   → FILTERS: who accesses which options within the population   │
  │   → Born into wealth: axis ② high FROM THE START (inherited)   │
  │   → Born into poverty: axis ② low → negative spiral risk       │
  │   → Born into educated family: axes ①④ accelerated (guided     │
  │     compile)                                                     │
  │   (Bourdieu 1986: economic + social + cultural capital reproduce)│
  └────────────────────────────┬────────────────────────────────────┘
                               ▼ shaped through education + family
  ┌─────────────────────────────────────────────────────────────────┐
  │ LAYER 2: EDUCATION + FAMILY (faster, narrower)                   │
  │   Which school? What did parents teach? Exposed to what domains?│
  │   → BUILDS: specific capacity + awareness + initial resources   │
  │   → Good school → ① expands + ④ expands (exposure + meta-cog) │
  │   → Parents encourage → ④ accurate, self-efficacy compiles     │
  │   → Parents restrict → ④ under-estimates, learned helplessness │
  │   → = "Starting line" action space for each individual         │
  └────────────────────────────┬────────────────────────────────────┘
                               ▼ interacts with hardware
  ┌─────────────────────────────────────────────────────────────────┐
  │ LAYER 1: HARDWARE + ACCUMULATED EXPERIENCE (fastest, narrowest) │
  │   DRD4, COMT, health, direct experience, compilation history    │
  │   → MODIFIES: action space from the initial point              │
  │   → Hardware bias: DRD4 breadth → explore more → ④ expands    │
  │   → Direct experience: try → fail/succeed → ①④ calibrates     │
  │   → Years of practice → ① deepens in specific domains          │
  │   → = Personal trajectory WITHIN social constraints            │
  └─────────────────────────────────────────────────────────────────┘

  ALL 4 LAYERS SIMULTANEOUSLY, NOT SEPARATE.
  Each layer = constraint + install + opportunity.
  Output = THIS PERSON'S action space AT THIS MOMENT.

🟢 Social reproduction: Bourdieu 1986 (economic + social + cultural capital)
🟢 Early childhood ROI: Heckman 2006
🟡 4-layer formation as parallel to Gap-Distribution = framework synthesis
```

---

## §6 — SHIFT MECHANISMS

### §6.1 — Axis ① (Capacity) shift: takes YEARS

```
⭐ COMPILED CAPACITY EXPANDS = CHUNK COMPILATION:

  Mechanism:
    → Exposure → chunks accumulate → compile → capacity INCREASES
    → = SAME mechanism as gap formation (Gap-Direction §6)
    → Takes time: domain expertise = 5-10+ years deliberate practice

  CAN'T SHORTCUT:
    → Money buys courses but DOESN'T buy compile time
    → AI accelerates learning but DOESN'T skip compilation
    → = Chunks must compile through REPEATED EXPOSURE, not instantaneously

  ASYMMETRY: expands SLOWER than it contracts
    → Build: years of practice
    → Lose: disuse → decay (Chunk §3.3 anchor decay)
    → Health crisis → physical capacity crashes FAST
    → = Build slow, lose fast = asymmetric risk

🟢 Deliberate practice: Ericsson 2006
🟢 Chunk compilation requires time: established cognitive science
```

### §6.2 — Axis ② (Resource) shift: VARIABLE

```
⭐ RESOURCE ACCESS CAN CHANGE FAST OR SLOW:

  FAST EXPAND:
    → Lottery, inheritance, sudden income
    → Meeting an influential person → network expands
    → Technology access (getting a smartphone → internet → the world)

  SLOW BUILD:
    → Savings accumulate over years
    → Network builds through repeated interactions
    → Career progression → income increases gradually

  FAST CRASH:
    → Job loss → income → 0
    → Divorce → network splits
    → Economic crisis → savings destroyed
    → Health → medical costs → resource drain

  = MOST VOLATILE axis — subject to external events
```

### §6.3 — Axis ③ (Freedom) shift: DEPENDS ON EXTERNAL

```
⭐ FREEDOM SHIFT = LARGELY OUTSIDE INDIVIDUAL CONTROL:

  SYSTEMIC CHANGE:
    → Legal reform → population freedom ↑
    → Social norm shift → invisible constraints ↓ (women's rights)
    → Technology → new freedoms (internet bypasses information barriers)
    → = Individual BENEFITS from systemic change

  INDIVIDUAL CHANGE:
    → Pay off debt → financial freedom ↑
    → Children grow up → obligation reduces → freedom ↑
    → Leave toxic relationship → freedom ↑
    → = Possible but COSTLY (mode shift, access cost — Obligation §6)

  = Axis ③ = least individual CONTROL (compared to ①②④)
```

### §6.4 — Axis ④ (Awareness) shift: SUDDEN POSSIBLE

```
⭐⭐ AWARENESS = THE AXIS THAT CAN SHIFT MOST SUDDENLY:

  SUDDEN EXPAND:
    → 1 conversation: "Did you know this career path exists?"
    → 1 book: paradigm shift in thinking
    → 1 trip: seeing a different way of living → "wait, this is possible?"
    → Internet exposure: YouTube, social media → worlds unveiled
    → Mentor at the right moment: "you have this ability, did you know that?"

  AXIS ④ PARADOX:
    → CHEAPEST per unit: 1 conversation = $0
    → HARDEST to trigger: invisible = can't search for what you don't know
    → REQUIRES EXTERNAL CATALYST: someone must "open your eyes"
    → AI ERA: AI can detect invisible constraints + suggest options
      → = New awareness catalyst at scale (AI-Schema-Detection §6 potential)

  AWARENESS EXPAND ≠ CAPACITY EXPAND:
    → ④ expands: "oh, Python exists" = instant
    → ① expands: "I know Python" = months/years of compiling
    → = ④ OPENS THE DOOR, ① takes TIME TO WALK THROUGH IT
    → = WHY ④ + ① must go TOGETHER for effective intervention

🟡 Awareness sudden shift = framework synthesis
🟡 ④ paradox (cheapest + hardest) = framework insight
```

### §6.5 — Crisis → collapse → rebuild

```
⭐ MAJOR CRISIS CAN CRASH MULTIPLE AXES SIMULTANEOUSLY:

  Example: Job loss + divorce + illness:
    ① → Capacity still intact but context-dependent (skills tied to old industry)
    ② → Resource crashes (income → 0, network splits, medical costs)
    ③ → Freedom crashes (debt, obligations, dependencies increase)
    ④ → Awareness CAN INCREASE (crisis = "forced perspective shift")

  ⭐ CRISIS HAS 2 SIDES:
    → CRASH: multiple axes ↘ simultaneously → negative spiral risk
    → RESET: ④ awareness increases through forced exposure →
      "I was living the wrong way" → new direction possible
    → = Like Gap-Distribution §3.4: "LOCKED + MISMATCHED → reality FORCES shift"
    → = Crisis = PAINFUL but CAN lead to realignment

🟡 Crisis as reset mechanism = framework synthesis
🟢 Post-traumatic growth: Tedeschi & Calhoun 2004
```

---

## §7 — EXPANSION QUALITY: DEPTH-FIRST PRINCIPLE

### §7.1 — Core paradox: more awareness ≠ more capability

```
⭐⭐ PARADOX: EXPANDING ACTION SPACE IS NOT ALWAYS BETTER.

  §4 described positive spiral: 4 axes rising → compound advantage.
  §6 described shift mechanisms: how each axis expands.
  BUT: HOW you expand matters more than HOW MUCH you expand.

  EXAMPLE:
    Person A: reads widely, learns IT, finance, design, marketing, cooking,
    music... spends 1 week on each then jumps to the next.
    → Axis ④ (awareness) WIDE: knows 10 domains exist
    → Axis ① (capacity) SHALLOW: each domain ≈ 0 actual ability
    → = KNOWS 100 DOORS, CAN OPEN 0

    Person B: same time → compiles DEEP in just 1 domain (coding).
    → Axis ④ NARROW: only knows 1-2 domains
    → Axis ① DEEP: proficient at coding → CAN execute
    → = KNOWS 2 DOORS, CAN OPEN 1

    WHO ACCOMPLISHES MORE?
    → Person B: fewer options but HAS REAL CAPACITY → acts → reward → compounds
    → Person A: more options but NO CAPACITY → paralysis → frustration

  ⭐ AWARENESS PARADOX:
    → Axis ④ expands → more domains VISIBLE → more gaps FORM
      (because "knowing domain exists = gap begins to form" — Gap-Direction §5.3 in reverse)
    → But axis ① DOESN'T expand at the same speed (compile takes YEARS — §6.1)
    → = Awareness opens FAST, capacity builds SLOW
    → = Gap-Distribution expands (more gaps) + Action-Space mismatch (shallow capacity) = FRUSTRATION
    → = WORSE than invisible constraint:
      Invisible: doesn't know → peaceful (§3.3)
      Broad-shallow: knows EVERYTHING they DON'T HAVE → chronic frustration

🟡 Awareness-capacity mismatch = framework synthesis
🟢 Choice overload → paralysis: Schwartz 2004, Iyengar & Lepper 2000
```

### §7.2 — Threshold as gate: "potential" vs "real" action space

```
⭐ NOT ALL AWARENESS = "REAL" ACTION SPACE:

  Domain-Mapping-Drive §2.3 + Gap-Distribution §6.1 established:
    → THRESHOLD = critical mass of chunks needed for gap to FORM
    → BEFORE threshold: no gap → no drive → no reward → PFC must FORCE each time
    → AFTER threshold: gap formed → drive → reward → SELF-SUSTAINING

  APPLIED TO ACTION SPACE:

    POTENTIAL Action-Space (pre-threshold):
      → Knows domain exists (axis ④ has it)
      → But hasn't compiled enough chunks to EXECUTE (axis ① insufficient)
      → Each time wanting to use it → PFC must DRAFT from scratch → COSTLY
      → = "Knows Python exists" but can't code Python
      → = Options VISIBLE but NOT EXECUTABLE

    REAL Action-Space (post-threshold):
      → Has compiled enough → gap formed → reward loop → self-sustaining
      → Using this capacity = LOW COST (compiled, automatic)
      → = "Knows Python AND can code Python"
      → = Options VISIBLE AND EXECUTABLE

  ⭐ ACTION SPACE QUALITY = POST-THRESHOLD / TOTAL AWARENESS:
    → Person A: 10 domains known, 0 post-threshold → quality ≈ 0
    → Person B: 2 domains known, 1 post-threshold → quality HIGH
    → Person C: 10 domains known, 3 post-threshold → quality GOOD (T-shaped)
    → = This file describes Action-Space SIZE (§2). This section adds Action-Space QUALITY.

🟢 Threshold → self-sustaining drive: Domain-Mapping-Drive §2.3
🟢 Deliberate practice → expertise: Ericsson 2006
🟡 Potential vs Real Action-Space = framework synthesis
```

### §7.3 — 4 Expansion Profiles

```
⭐ 4 PROFILES — DEPENDING ON DEPTH × BREADTH ALLOCATION:

  ┌─────────────────────────────────────────────────────────────────────┐
  │ SCATTERED EXPLORER    ④ broad + ① shallow EVERYWHERE               │
  │                                                                     │
  │ Knows many domains → 0 domains post-threshold                      │
  │ → No self-sustaining drive in ANY domain                           │
  │ → Choice overload: N options → PFC overload → can't commit         │
  │ → Each domain: PFC must FORCE → costly → burnout → jumps to       │
  │   new domain → repeats → "knows a bit of everything, good at none" │
  │                                                                     │
  │ Gap-Distribution §3.3: many-shallow. Domain-Mapping-Drive §2.3:    │
  │ below threshold in ALL. Schwartz 2004: paradox of choice.          │
  │                                                                     │
  │ ⚠️ TRAP: looks like "learning" but actually = avoiding depth        │
  │ (depth = PFC sustained effort = uncomfortable PRE-threshold)       │
  │ → Surface novelty reward per new domain → jumping = novelty loop  │
  │   at the meta-level                                                │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │ DEEP SPECIALIST       ④ narrow + ① DEEP in 1                       │
  │                                                                     │
  │ 1 domain post-threshold → Background-Pattern locked →              │
  │ self-sustaining drive                                               │
  │ → 5 lock mechanisms (Gap-Distribution §6.3): gap self-generates,   │
  │   reward memory, identity locked, depth×specificity trap           │
  │ → PRODUCTIVE + SUSTAINABLE but VULNERABLE:                         │
  │   domain becomes obsolete → capacity suddenly worthless            │
  │   blind spots outside domain → missed opportunities               │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │ T-SHAPED EFFECTIVE    ④ broad + ① DEEP in 1-2 + moderate 3-5       │
  │                                                                     │
  │ Deep domain(s) = EXECUTION BASE (post-threshold, self-sustaining)  │
  │ Moderate domains = BRIDGE (enough chunks to communicate, direct)   │
  │ Broad awareness = SEE CONNECTIONS (④ informs ① direction)          │
  │                                                                     │
  │ DOESN'T TRY TO EXECUTE IN ALL DOMAINS — executes in deep ones,     │
  │ observes + directs in broad ones.                                   │
  │                                                                     │
  │ Examples: Jensen Huang = deep semiconductor/AI + broad business    │
  │ Example: Designer = deep integration + moderate code + moderate art │
  │ Gap-Distribution §3.3: T-shaped. Chase & Simon 1973: expertise +   │
  │ bridge function.                                                    │
  └─────────────────────────────────────────────────────────────────────┘

  ┌─────────────────────────────────────────────────────────────────────┐
  │ SERIAL DEPTH          ④ expanding + ① SEQUENTIAL deep               │
  │                                                                     │
  │ Deep A → cross threshold → THEN explore B → deep B → THEN C       │
  │ Each depth BUILDS ON previous (transfer patterns, meta-skills)     │
  │ → Polymath pattern: depth → breadth FROM depth → new depth         │
  │                                                                     │
  │ REQUIRES: time (each domain = years) + deliberate transitions      │
  │ RARE but powerful when present: Leonardo da Vinci, Elon Musk       │
  │ (Musk: PayPal → SpaceX → Tesla = serial depth, not scatter)       │
  │                                                                     │
  │ ⭐ KEY: NOT simultaneously shallow — SEQUENTIAL deep.               │
  │ = Depth-first EACH TIME, but MULTIPLE TIMES across a lifetime.     │
  └─────────────────────────────────────────────────────────────────────┘

  ⚠️ PROFILES = simplified. Most people = MIX, shifting over time.
```

### §7.4 — Depth-first principle: roots before branches

```
⭐⭐ WHY DEPTH-FIRST = OPTIMAL EXPANSION STRATEGY:

  ① THRESHOLD = IGNITION POINT (Domain-Mapping-Drive §2.3):
    → Before threshold: learning = PFC FORCES = costly = easy to quit
    → After threshold: learning = self-sustaining drive = FREE
    → = MUST cross threshold in AT LEAST 1 domain before expanding outward
    → = Not crossing any threshold = every domain = costly = scattered

  ② BACKGROUND PATTERN = STABILIZER (Background-Pattern §8):
    → Compile deep → Background-Pattern forms "I = person of domain X" → STABLE IDENTITY
    → Stable identity → explore outward = LOW RISK (has an anchor to return to)
    → No stable identity → explore = HIGH RISK (drift, no anchor)

  ③ DEPTH ENABLES BREADTH (transfer patterns):
    → Deep compile → meta-skills: "how to learn" not just "what I know"
    → Deep physics → transfer pattern recognition TO biology, economics
    → Deep coding → transfer systematic thinking TO design, business
    → = Depth in 1 DOESN'T limit to 1 — it ARMS for many domains

  ④ REWARD MEMORY SUSTAINS (Gap-Distribution §6.3 ②):
    → Deep domain → body compiled: [deep gap fill = MASSIVE opioid]
    → Reward memory = FUEL for continued effort
    → Scattered = no deep reward memory → no fuel → PFC must supply constantly

  ⭐ ANALOGY — TREE:
    → Deep roots + strong trunk → branches EXPAND SAFELY → won't topple in wind
    → No roots + branches everywhere → light wind → FALLS
    → Roots = depth (post-threshold domain). Branches = breadth (awareness expanding).
    → = ROOT-FIRST, THEN BRANCH.

🟢 Threshold → self-sustaining: Domain-Mapping-Drive §2.3, §5
🟢 Background-Pattern self-reinforcing: Background-Pattern §8
🟢 Transfer of expertise: established cognitive science
🟡 Depth-first as optimal expansion strategy = framework synthesis
```

### §7.5 — Premature expansion (parallel to Reward-Calibration §3.4)

```
⭐ PREMATURE EXPANSION = PARALLEL OF PREMATURE COMPILATION:

  Reward-Calibration §3.4 established:
    → Over-reward forces chunks to compile BEFORE sufficient foundation
    → → Chunks skew from the start → cascade

  PREMATURE EXPANSION = ANALOGOUS:
    → Options VISIBLE before capacity is READY
    → → Gaps form (because domain is known) BEFORE chunks are sufficient
    → → TRY but FAIL (because shallow) → compiles: "I'm not good at this domain"
    → → Skewed conclusion: "I'm not suited for it" (reality: not ENOUGH chunks yet)
    → → Quit → next domain → repeat → "tries everything, drops everything"

  EXAMPLES:
    → Student tries 5 majors in 2 years: each < threshold →
      concludes "I have no passion" → reality = hasn't compiled ENOUGH in ANY of them
    → Person reads self-help → knows 20 strategies → tries each for 1 week →
      none works → "self-help is useless" → reality = premature expansion
    → New gym-goer tries 10 sports/month → each not enough to see results
      → "exercise is useless" → reality = hasn't crossed threshold in ANY sport

  ⭐ IMPORTANT DISTINCTION:
    → "Bored because of mismatch" (hardware genuinely doesn't fit) ≠ "Bored because pre-threshold"
    → Both FEEL THE SAME: bored, drained, "don't enjoy it"
    → DIFFERENT: mismatch → the more you compile the more DRAINED you get.
      Pre-threshold → after threshold → ENJOY.
    → Domain-Mapping-Drive §2.3: "below threshold = learning feels like torture.
      Above threshold = learning feels like play."
    → = "Not enjoying it yet ≠ not suited for it. May = not enough chunks yet."

🟡 Premature expansion = framework synthesis (parallel Reward-Calibration §3.4)
🟢 Threshold ↔ enjoyment: Domain-Mapping-Drive §2.3
```

### §7.6 — Self-calibration: domain feedback is the only arbiter

```
⭐ HOW DO YOU KNOW IF YOU'RE EXPANDING IN THE RIGHT DIRECTION?

  Logic-Feeling-Balance.md: CANNOT prescribe → domain feedback = only arbiter.
  APPLIED: CANNOT prescribe expansion direction → only OBSERVE signals.

  3 SIGNALS FROM BODY (after STAYING LONG ENOUGH — at or near threshold):

    ① APPROACH SIGNAL WHEN ENGAGING:
      → Body approaches (curious, energized) when doing = domain FITS hardware
      → Body avoids (bored, drained) when doing = domain MISMATCH
      → ⚠️ PRE-THRESHOLD: both signals UNRELIABLE
        (not enough chunks → no gap → "bored" may = hasn't crossed threshold)
      → POST-THRESHOLD: signals RELIABLE (gap formed → body vote clear)

    ② COMPOUND REWARD OVER TIME:
      → Right direction: reward per session INCREASES (deeper gap → bigger reward)
      → Wrong direction: reward per session DECREASES (shallow → habituates → bored)
      → = "The more I do it the more I enjoy it" = right. "The more I do it the more bored I get" = wrong OR not enough yet.

    ③ TRANSFER PATTERNS EMERGE:
      → Right direction: connections to other domains appear ("oh, physics is like economics")
      → = Depth NATURALLY ENRICHING breadth
      → Wrong direction: isolated, no connections → narrow without bridge value

  ⭐ PRACTICAL OBSERVATION:
    → Try a domain → STAY LONG ENOUGH (cross threshold) → THEN evaluate
    → "Long enough" ≈ varies by domain (coding ~6-12 months, physics ~2-3 years)
    → Evaluate: approach signal + compound reward + transfer patterns?
    → YES → go deeper (depth-first)
    → NO (after sufficient time) → pivot to different domain (NOT scatter)
    → = FRAMEWORK DOES NOT PRESCRIBE the right direction. Only describes HOW to observe.

🟡 Self-calibration via body signals = framework synthesis
🟢 Logic-Feeling-Balance: domain feedback = only arbiter (established framework)
```

---

## §8 — Gap-Distribution × Action-Space: BEHAVIORAL PREDICTION (extended from §1.3)

```
⭐⭐ Gap-Distribution AND Action-Space INFLUENCE EACH OTHER — FEEDBACK LOOP:

  Action-Space → Gap-Distribution (supply shapes demand):
    → Action-Space expands → new domains accessible → new chunks compile → new gaps form → Gap-Distribution SHIFTS
    → Example: student enters a lab → accesses a new domain → chunks compile →
      gap "want to research deeper" FORMS → Gap-Distribution shifts toward abstract
    → = Expanded action space CREATES new demand

  Gap-Distribution → Action-Space (demand shapes supply):
    → Gap-Distribution shifts → new gaps → drive to build capacity → Action-Space expands
    → Example: gap "want to code well" → invests time learning → capacity ↑ → Action-Space expands
    → = Demand DRIVES supply expansion

  → = BIDIRECTIONAL FEEDBACK LOOP
  → = WHY initial conditions matter (Heckman 2006):
    Early Action-Space expansion → early Gap-Distribution shift → early feedback loop → compound advantage
    Late Action-Space expansion → late Gap-Distribution shift → late start → catching up is harder


  ⭐ Gap-Distribution × Action-Space MISMATCH = CORE OF MANY LIFE PROBLEMS:

    MISMATCH TYPE 1: "Want but can't"
      → Gap-Distribution: gap clear + fires strongly
      → Action-Space: options insufficient
      → = Chronic frustration → learned helplessness risk
      → Fix: expand Action-Space (education, resources, awareness)

    MISMATCH TYPE 2: "Can but don't want to"
      → Action-Space: options abundant
      → Gap-Distribution: gaps don't match available options
      → = Drift, waste, "bored despite having everything"
      → Fix: expose to new domains → Gap-Distribution shifts → gaps align with Action-Space

    ALIGNED: "Want AND can"
      → Gap-Distribution gaps match Action-Space options → action → reward → compounds
      → = Most productive, most fulfilling
      → = "Flow state" prerequisites: skill ≈ challenge (Csikszentmihalyi 1990)


🟡 Gap-Distribution ↔ Action-Space bidirectional feedback = framework synthesis
🟢 Flow: skill ≈ challenge: Csikszentmihalyi 1990
🟢 Initial conditions compound: Heckman 2006
```

---

## §9 — CASES

### §9.1 — Case: Parent-child relationship

```
🟡 CASE: Child doesn't open up to parents. Why?

  ACTION SPACE ANALYSIS OF THE CHILD:
    ① Capacity: HAS the words, HAS experiences they want to share
    ② Resource: HAS parents who are available
    ③ Freedom: RESTRICTED by PAST EXPERIENCES:
       → Opened up → was judged → compiled: "speaking = unsafe"
       → Opened up → old mistakes were dug up → compiled: "speaking = getting blamed"
       → Opened up → was interrupted → compiled: "my views don't matter"
    ④ Awareness: Child KNOWS they're restricted but DOESN'T KNOW how to escape it

  → Axis ③ (Freedom) BLOCKED BY COMPILED CONSTRAINT:
    → Action space "opening up" TECHNICALLY exists (①②④ sufficient)
    → BUT axis ③ has compiled constraint: "sharing = unsafe"
    → = Blocked constraint CREATED BY PARENTS (even unintentionally)

  PARENT FIXES = EXPAND CHILD'S AXIS ③:
    → Listen until child finishes (DON'T interrupt) → ③ expands: "speaking = safe"
    → Don't judge → ③ expands: "speaking = not being attacked"
    → Don't bring up old mistakes → ③ expands: "speaking ≠ having all mistakes replayed"
    → = RESTORE action space "sharing" by REMOVING compiled constraints

  ⭐ INSIGHT: constraint CAN BE CREATED BY OTHERS
    (even unintentionally, even lovingly — still = constraining action space)
```

### §9.2 — Case: 2 societies — same population, different collective Action-Space

```
🟡 COLLECTIVE ACTION SPACE CASE:

  ISOLATED RURAL VILLAGE 1960:
    Population Action-Space: ① deep farming ② subsistence
    ③ tight norms ④ only knows 1 way of living
    → POPULATION action space ≈ narrow, stable, invisible trap

  SILICON VALLEY 2026:
    Population Action-Space: ① multi-domain, deep tech ② VC funding, global network
    ③ liberal, few restrictive norms ④ exposure to MANY ways of living
    → POPULATION action space ≈ wide, dynamic, visible options

  = SAME SPECIES. SAME HARDWARE. DIFFERENT COLLECTIVE INFRASTRUCTURE.
  = Collective infrastructure = LAYER 4 in Formation Model (§5)
  = Individual Action-Space = f(collective Action-Space × social position × education × hardware)
```

### §9.3 — Case: Stephen Hawking — physical constraint + technology

```
🟡 PHYSICAL CONSTRAINT CASE:

  BEFORE ALS:
    ①②③④ = normal range → standard academic Action-Space

  AFTER ALS (progressive):
    ① Capacity: INTACT (physics knowledge remains)
    ② Resource: PARTIALLY CRASHED (needs care, high costs)
    ③ Freedom: CRASHED (body = prison, mobility ≈ 0)
    ④ Awareness: INTACT (knew he could still contribute)

  TECHNOLOGY COMPENSATES:
    → Wheelchair: partially restores ③ (mobility)
    → Voice synthesizer: partially restores ② (communication → network → output)
    → Research assistants: partially restores ② (collaboration)
    → = Technology = partial Action-Space RESTORATION for ②③

  ⭐ KEY INSIGHT: ①④ STILL INTACT → Gap-Distribution STILL FIRES →
    Frustration when ②③ blocked + awareness ④ that "I CAN"
    → Technology bridges Gap-Distribution ↔ Action-Space gap
    → Hawking remained productive BECAUSE ①④ high + technology compensated ②③
```

### §9.4 — Case: Gap-Distribution × Action-Space mismatch across a lifetime

```
🟡 LIFECYCLE Action-Space × Gap-Distribution TRAJECTORY:

  CHILDHOOD (0-12):
    Gap-Distribution: shifting, exploring → Action-Space: low all axes (dependent)
    → = MATCHED AT LOW: few gaps, few options → appropriate
    → Parent's job: GRADUALLY EXPAND child's Action-Space (education, exposure)

  ADOLESCENCE (12-20):
    Gap-Distribution: rapid shift, identity → Action-Space: expanding but uneven (①②③ growing)
    → = MISMATCHED: gaps form FASTER than Action-Space grows → frustration
    → "Want many things but can't yet" = typical teenage experience

  YOUNG ADULT (20-30):
    Gap-Distribution: converging → Action-Space: expanding fast (education complete, career starting)
    → = ALIGNMENT FORMING: Gap-Distribution direction + Action-Space capacity start matching
    → "Quarter-life crisis" = Gap-Distribution not yet converged + Action-Space expanding → too many options

  MID-ADULT (30-50):
    Gap-Distribution: mostly locked → Action-Space: high (peak career, resources, freedom)
    → = BEST MATCH: know what you want + can do it → productive peak
    → Risk: locked Gap-Distribution + shifting reality → mid-life crisis

  LATE ADULT (50+):
    Gap-Distribution: anchor exhausted? → Action-Space: declining (health, retirement)
    → = POTENTIAL MISMATCH: gaps change + capacity reduces
    → Meaning §2.2: "emptiness" when anchor gone + Action-Space narrows
```

---

## §10 — RESEARCH ANCHORS

```
⭐ 16 RESEARCH ANCHORS — SUPPORTING SPECIFIC CLAIMS:

  ┌─────────────────────────────┬──────────────────────────────────────────┐
  │ Claim                       │ Research                                  │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Development = expanding     │ 🟢 Sen 1999 (Nobel) — Capability         │
  │ capabilities (freedoms)     │ Approach                                  │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Self-efficacy → behavior    │ 🟢 Bandura 1977 — Self-Efficacy Theory   │
  │ prediction                  │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Early intervention has      │ 🟢 Heckman 2006 — 7-10% annual ROI      │
  │ compound returns            │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Low competence →            │ 🟢 Kruger & Dunning 1999 — metacognitive │
  │ overestimate capability     │ deficit                                   │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Helplessness = DEFAULT,     │ 🟢 Maier & Seligman 2016 — vmPFC learns │
  │ controllability LEARNED     │ "controllable", DRN default              │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Autonomy, competence,       │ 🟢 Deci & Ryan 2000 — Self-Determination │
  │ relatedness as basic needs  │ Theory                                    │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Social brain = capacity     │ 🟢 Dunbar 1992, Zhou et al. 2005 —       │
  │ ceiling ~150                │ Social Brain Hypothesis                   │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Social capital: bonding     │ 🟢 Putnam 2000 — Bowling Alone            │
  │ vs bridging                 │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ 3 capitals reproduce        │ 🟢 Bourdieu 1986 — economic, social,     │
  │ across generations          │ cultural capital                          │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Behavior = f(expectancy     │ 🟢 Vroom 1964 — Expectancy Theory        │
  │ × valence × instrumentality)│                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Post-traumatic growth       │ 🟢 Tedeschi & Calhoun 2004 —             │
  │ possible after crisis       │ (crisis → positive change)               │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Expertise restructures      │ 🟢 Chase & Simon 1973 — chess chunking   │
  │ perception                  │                                           │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Income ↔ well-being         │ 🟢 Kahneman & Deaton 2010 — emotional    │
  │ plateau ~$75K               │ well-being satiation                      │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Frustration → aggression    │ 🟢 Dollard et al. 1939 — frustration-    │
  │                             │ aggression hypothesis                     │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ More choices → more anxiety │ 🟢 Schwartz 2004 — Paradox of Choice     │
  │ less satisfaction           │ Iyengar & Lepper 2000 — jam study        │
  ├─────────────────────────────┼──────────────────────────────────────────┤
  │ Deliberate practice →       │ 🟢 Ericsson 2006 — expertise requires    │
  │ expertise                   │ sustained deep practice                   │
  └─────────────────────────────┴──────────────────────────────────────────┘
```

---

## §11 — HONEST ASSESSMENT

```
⭐ CONFIDENCE PER CONCEPT:

  🟢 ESTABLISHED (research confirmed):
    → Self-efficacy → behavior (Bandura 1977)
    → Learned helplessness = DEFAULT (Maier & Seligman 2016)
    → Dunning-Kruger effect (Kruger & Dunning 1999)
    → Social capital: bonding vs bridging (Putnam 2000)
    → Capital reproduction (Bourdieu 1986)
    → Early intervention compound returns (Heckman 2006)
    → Capability Approach (Sen 1999)
    → Dunbar layers (Zhou et al. 2005)
    → Post-traumatic growth (Tedeschi & Calhoun 2004)
    → Choice overload (Schwartz 2004, Iyengar & Lepper 2000)
    → Deliberate practice → expertise (Ericsson 2006)

  🟡 FRAMEWORK SYNTHESIS (consistent, testable, not mainstream term):
    → Action-Space as per-person aggregate supply-side property
    → 4-axis model (Compiled Capacity, Resource Access, Freedom, Awareness)
    → 3 types of constraint (Blocked, Dependent, Invisible)
    → Positive/Negative spiral dynamics
    → 4-layer formation model (Collective → Hardware)
    → Gap-Distribution × Action-Space behavioral prediction (4 quadrants)
    → Expansion quality: Potential vs Real Action-Space (post-threshold ratio)
    → 4 expansion profiles (Scattered / Specialist / T-Shaped / Serial Depth)
    → Depth-first principle (threshold → anchor → expand)
    → Premature expansion parallel to Reward-Calibration §3.4
    → Gap-Distribution ↔ Action-Space feedback loop
    → Shift mechanisms per axis (asymmetric costs)

  🔴 HYPOTHESIS (testable, not verified):
    → Invisible constraint = most dangerous (logical, untested empirically)
    → Axis ④ = cheapest + hardest intervention (plausible, no quantification)
    → Optimal Gap-Distribution × Action-Space alignment (may not exist — depends on context)
    → Shift velocity per axis (no data on actual speeds)
    → Technology compensates ②③ (Hawking = N=1, not generalizable)


  ⚠️ THIS FILE = OBSERVATION SYNTHESIS:
    → Synthesizes insights from ~15 files into 1 supply-side aggregate view
    → Does NOT create new mechanisms — reorganizes through per-person Action-Space lens
    → Value: SEEING the capability landscape → understand + predict + intervene
    → Does NOT prescribe → "what Action-Space should look like" = each person decides
    → Sen 1999: "each person chooses the life they have reason to value" = AGREED
```

---

## §12 — OPEN QUESTIONS

```
⭐ 6 OPEN QUESTIONS FOR FUTURE INVESTIGATION:

  Q1: CAN ACTION SPACE BE QUANTIFIED?
    → Gap-Distribution Q1 (same challenge): multi-dimensional, changes over time
    → Possible: QUALITATIVE observation (4-axis description) > any single number
    → Sen approach: "functionings" vs "capabilities" — capability = potential set
    → Research direction: capability index per population?

  Q2: CAN INVISIBLE CONSTRAINTS BE DETECTED BY AI?
    → AI-Schema-Detection §6: AI detects collective schemas
    → Extension: AI detects invisible constraints per person?
    → Challenge: invisible = person doesn't know → AI needs EXTERNAL data
    → Possible: compare person's behavior with population → detect "missing options"

  Q3: HOW DOES THE AI ERA SHIFT ACTION SPACE?
    → AI automates tasks → axis ① less important for some domains?
    → AI provides information → axis ④ expands for everyone?
    → AI creates new options → axis ② expands?
    → = Uncertain — the AI era = a natural experiment

  Q4: IS Gap-Distribution × Action-Space ALIGNMENT MEASURABLE?
    → If measurable: predict life satisfaction, productivity, mental health
    → Challenges: both Gap-Distribution and Action-Space are multi-dimensional
      → alignment = complex
    → Csikszentmihalyi flow: skill ≈ challenge → Gap-Distribution × Action-Space alignment = flow analog?

  Q5: DOES COLLECTIVE ACTION SPACE HAVE AN "OPTIMAL" DISTRIBUTION?
    → Should society maximize AVERAGE Action-Space? Or MINIMIZE variance?
    → Rawls 1971: maximize minimum → focus on lowest Action-Space individuals
    → Framework: does NOT prescribe, but CAN observe patterns

  Q6: HOW IS ACTION SPACE TRANSMITTED ACROSS GENERATIONS?
    → ① Capacity: education system + family investment
    → ② Resource: inheritance, network, social capital
    → ③ Freedom: legal rights, social position
    → ④ Awareness: family culture, breadth of exposure
    → = 4 transmission channels, ALL reproduce (Bourdieu)
    → = WHY social mobility is HARD
```

---

## §13 — CROSS-REFERENCES

```
⭐ PRIMARY (this file BUILDS ON):
  → Gap-Distribution-Profile.md v1.0 — SIBLING file (demand side ↔ supply side)
  → Gap-Direction.md v2.0 — "unknown = no gap" (invisible constraint)
  → Status.md v2.1 — §1 Resource Access Map (axis ②)
  → Autonomy-Hardware.md v1.1 — §2 vmPFC/DRN (axis ④ hardware)
  → Autonomy.md v1.1 — software development (axis ④ software)

⭐ MECHANISM (this file REFERENCES):
  → Inter-Body-Mechanism.md v1.0 — Compilable Architecture, PFC=Lawyer, 3-cost
  → Compliance-Floor.md v2.0 — axis ③ legal constraints
  → Obligation.md v1.1 — axis ③ obligation constraints
  → Money-Analysis.md v1.0 — axis ② money = bridge technology
  → Chunk.md v2.2 — compilation mechanism (axis ①)
  → Background-Pattern.md v1.1 — §8 self-reinforcing loop (§7 depth-first anchor)
  → Connection.md v4.0 — Dunbar layers (axis ② social capital)
  → Drill-Entity-Compiled-Capacity.md v1.0 — Depth × Breadth = constant
  → Domain-Mapping-Drive.md v1.0 — §2.3 threshold, §5 ignition point (§7)
  → Reward-Calibration.md v1.1 — §3.4 premature compilation (§7.5 parallel)
  → Logic-Feeling-Balance.md — domain feedback = only arbiter (§7.6)

⭐ OBSERVATION (this file CONNECTS):
  → Meaning.md v2.1 — life-level anchor × action space alignment
  → Self-Created-Threat.md v1.0 — awareness of self-created constraints
  → Expansion-Saturation-Crisis.md v1.1 — collective Action-Space mismatch
  → Domain-Mapping-Drive.md v1.0 — reward from PROCESS (axis ① growth)
  → Reward-Calibration.md v1.1 — over-reward × premature access (axis ②)

⭐ APPLICATION:
  → By-Product-Gap-Resonance.md v1.0 — axis ⑤ Constraint context reference
  → Education-Mechanism.md — education as Action-Space intervention
  → AI-Schema-Detection.md v2.0 — AI detecting invisible constraints (Q2)
```
