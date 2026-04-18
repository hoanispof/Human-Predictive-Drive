# Body-Input Enumeration — Testing the Substrate Reframe

> **Trạng thái:** OUTLINE — Phase R-3 complete, R-4 trở đi = fill
> **Ngày:** 2026-04-14
> **Mục đích:** Test reframe proposal — body-inputs as SUBSTRATE primitive,
> "channels" as shorthand for body-input aggregates, baseline adaptation
> as core mechanism, Novelty/Status/Protect as PFC drives acting on L1
> **Reference:** Body-Base-Example.md (50 cases, §13-§14 synthesis),
> Body-Base-Deep-Cases.md (DC1/DC3), Why-Body-Knows.md, Body-Dissonance.md,
> Empathy-Mirror.md, Calibration-Inputs-Analysis.md (draft)
> **Memory ref:** `project_calibration_inputs.md`,
> `project_pattern_match_insights.md`
> **⚠️ Status:** TEST FILE — không phải replacement cho Body-Base.md.
> File này test reframe có đứng vững không trước khi commit toàn bộ framework
> **Quy ước:** 🟢 Research support | 🟡 Framework inference | 🔴 Hypothesis

---

## §0 — MỤC ĐÍCH VÀ PHƯƠNG PHÁP

### §0.1 Tại sao file này tồn tại

File này được tạo **2026-04-14** sau khi bạn đặt câu hỏi fundamental về
substrate của body-base framework.

**Tình trạng framework trước file này**:

- **Body-Base-Example.md Phase B complete** — 50 extreme cases B1-B50,
  ~12,813 lines, với §12-§14 cross-case synthesis đã extract ~10
  architectural findings về channel architecture
- **Body-Base-Deep-Cases.md Phase DC-A complete + DC-B partial** — 2
  cases deep-filled (DC1 Tesla + Leonardo contrast, DC3 digital nomad
  vs ancestral tribal nomad), 10 cases placeholder chờ fresh analytical
  lens, multi-angle triangulation methodology established
- Cả hai files đã validate **channel list hiện tại** trong Body-Base.md
  §4 outline (Loud/Acute + Silent/Slow-Decay + Higher-Order — xem §1.1
  phần dưới)
- Phase C (Body-Base.md content fill) đang pending, dự kiến absorb các
  findings từ §14 Example + §F Deep-Cases vào foundation file

**Observation recurring gây khó chịu**:

Dù 50 cases đã analyzed với 9-field schema đầy đủ, một pattern vẫn tồn
tại — **cases đều multi-channel, khó isolate một channel "chính"**.

Example §13.3 explicit: "channel existence universal, individual calibration
variable." B20 asexuality extreme, B46 Proenneke thrived solo 30 năm,
B50 solitary crashed trong days. Cùng species, radically different
baseline requirements. Variation individual lớn đến mức raise question:
có phải variation nằm ở level substrate thấp hơn channel không?

Thêm nữa, §14.6 Example đã note rằng **status/fame/wealth/power là PFC
proxies, không phải body-base channels** — chúng không có direct receiver.
Nhưng existing framework vẫn list mastery/meaning ở §4.3 "higher-order
channels." Tension giữa framework structure (có channels) và framework
findings (một số không phải channels thực sự).

**Câu hỏi user đặt (session 2026-04-14)**:

> "Có thể body-base chỉ có L0 Alive + L1 body-inputs, với Novelty/Status/
> Protect là drives ở PFC tác động lên L1 thôi, không cần L2 quality riêng
> không? Mỗi input có adaptive baseline, deviate dưới baseline → dissonance,
> trên baseline → reward → shift baseline lên. 'Channels' như nature,
> social, movement chỉ là ngôn ngữ tiện chỉ cluster of body-inputs
> cùng deviate đồng thời, không phải distinct primitives."

**Lập luận cốt lõi của reframe**:
- Body liên tục nhận inputs qua giác quan trong domain real
- Mỗi input có baseline calibrated theo 2M năm ancestral environment +
  personal development
- Deviation dưới baseline → dissonance (bứt rứt → khó chịu → đau)
- Deviation trên baseline → reward → Novelty fires → baseline shifts up
  (hedonic treadmill mechanism)
- Loss of elevated baseline → dissonance at new higher expected floor
- "Channels" = shorthand vocabulary cho body-input clusters, không phải
  ontological primitives

**Mục đích file này**:

Test xem reframe substrate model có đứng vững không khi đối chiếu với:
1. **50 Phase B cases** (body-input substrate explain được bao nhiêu
   cases? Gaps ở đâu?)
2. **Existing theory** (Why-Body-Knows calibration 4-tier, Body-Dissonance
   signal mechanism, Empathy-Mirror mechanism, Feeling folder PFC
   observation)
3. **Research literature** (interoception Craig/Seth/Barrett, predictive
   processing, baseline adaptation Brickman/Frederick, supernormal
   stimulus Tinbergen, mere exposure Zajonc)

**Verdict options** sau khi test (§12):
- **Commit** — reframe đứng vững → Phase C Body-Base.md rewrite theo
  substrate model, Phase B/DC files trở thành evidence chapters
- **Patch** — reframe mostly works, identify specific patches, commit
  với modifications
- **Parallel** — giữ cả 2 models: channel = practical vocabulary,
  substrate = theoretical foundation
- **Reject** — reframe fails, identify why, alternative direction

**Tại sao cần test trước khi commit**: reframe đòi rewrite Body-Base.md
foundation file + affect cách mô tả mọi channels downstream. Không muốn
commit trước khi verify nó thực sự work trên evidence đã có. "Chậm mà
chắc."

### §0.2 Phạm vi và scope

**File này KHÔNG phải foundation replacement**:
- KHÔNG phải Body-Base.md rewrite (Phase C sẽ làm việc đó nếu reframe
  commits)
- KHÔNG phải data file như Body-Base-Example.md (evidence chapter)
- LÀ **test file** focused on ONE question: body-input substrate có
  đứng vững như framework foundation không?

**Target length**: ~2000-3000 lines. Đủ thorough cho test nhưng không
bloat thành foundation file.

**Những gì file này COVER**:

1. **Enumeration completeness** — liệt kê đầy đủ body-inputs với
   ancestral baseline + deviation spectrum (negative + positive) +
   adaptation mechanism + research citations (§2-§4)
2. **Mechanism coherence** — baseline adaptation + Novelty shifter +
   decay model có logically self-consistent không, có match established
   research không (§5)
3. **PFC drive operation** — Novelty/Status/Protect hoạt động trên
   body-inputs như operators có work không, không cần intermediate
   "quality channels" (§6)
4. **Dissonance re-mapping** — 6 nguồn dissonance trong Body-Dissonance.md
   §2.5 có map cleanly vào body-input deviations vs schema mismatches
   không (§7)
5. **Channel shorthand mapping** — existing channels (nature/agent/
   movement/touch/meaning/mastery) reduce về body-input aggregates có
   preserve practical vocabulary không, gaps ở đâu (§8)
6. **Case coverage test** — 15 selected cases từ Phase B + DC1 Tesla +
   DC3 nomad có explain được qua reframe không, PASS/PARTIAL/FAIL
   distribution thế nào (§9)

**Những gì file này BYPASS** (orthogonal với substrate question):

- **Cultural amplification** — §13.4 Example đã cover: "culture shapes
  channel expression, không phải architecture." Reframe không thay đổi
  kết luận này, substrate universal, amplification cultural
- **Collective architectures** — §13.6 Example cover individual/family/
  village/dynastic/civilizational scales. Emergent level trên substrate,
  reframe không affect
- **Individual calibration deep-dive** — §13.3 variation large, nhưng
  reframe tăng clarity: variation ở substrate baseline level, không
  phải channel existence level. Chi tiết deserve own section in future
  Body-Base.md
- **Development trajectory** — how body-inputs calibrate through
  childhood, sensitive periods, parenting effects. Deserve own section
  in future Body-Base.md §11
- **Intervention recommendations** — practical health advice (how much
  nature per week, how to reduce screen time, etc.). Downstream
  application, không phải substrate question

**Scope constraint principle**: file này là TEST, không phải commitment.
Nếu test PASSES → subsequent Phase C sẽ commit reframe thành full
foundation rewrite. Nếu test FAILS → framework giữ existing structure
với patches. Không đi quá xa trong file này.

### §0.3 Cấu trúc file

File này organize thành 13 sections chính, chia 5 phần:

**Phần 1 — Meta (§0-§1)**:
- §0 — Mục đích, phạm vi, cấu trúc (section này)
- §1 — Reframe proposal: mô hình cũ, mô hình mới, parsimony
  arguments, test criteria

**Phần 2 — Enumeration (§2-§4)**:
- §2 — Exteroceptive inputs: vision, audition, olfaction, gustation,
  tactile skin
- §3 — Proprioceptive inputs: proprioception, vestibular, kinesthetic
- §4 — Interoceptive inputs: thermoreception core, nociception,
  respiratory, cardiovascular, visceral, metabolic, hormonal-sensed,
  sleep/circadian, **§4.9 self-signal interoception meta**

**Phần 3 — Mechanism (§5-§7)**:
- §5 — Baseline adaptation mechanism (core theoretical section)
- §6 — PFC drives operating on body-inputs (Novelty/Status/Protect
  as operators, không phải layer)
- §7 — Dissonance re-mapping (6 nguồn từ Body-Dissonance.md §2.5)

**Phần 4 — Vocabulary + Test (§8-§9)**:
- §8 — "Channel" as shorthand (nature/agent/movement/... mapped to
  body-input aggregates)
- §9 — Test against 15 Phase B cases + DC1 Tesla + DC3 nomad

**Phần 5 — Integration + Verdict (§10-§13)**:
- §10 — Integration với Why-Body-Knows, Body-Dissonance, Empathy-
  Mirror, Feeling folder, future Body-Base.md
- §11 — Honest assessment (strengths + gaps + open questions)
- §12 — Verdict (Commit/Patch/Parallel/Reject)
- §13 — Sources

**Reading paths đề xuất**:

- **Quick assessment** (~30 phút đọc): §0 → §1 → §9.3 coverage report
  → §12 verdict. Đủ hiểu reframe disposition.
- **Theoretical focus**: §1 → §5 → §6 → §7 → §10.5. Mechanism và
  integration arguments.
- **Empirical focus**: §2 → §3 → §4 → §8 → §9. Enumeration và case
  test.
- **Full read**: sequential §0 → §13. Complete framework test.

**Cross-reference convention**: dùng "§X.Y" cho sections trong file này,
"Body-Base.md §X" cho existing framework files, "Example §X.Y" cho
Body-Base-Example.md sections, "Deep-Cases DC[N]" cho Body-Base-Deep-
Cases.md cases.

---

## §1 — REFRAME PROPOSAL

### §1.1 Mô hình cũ (current framework)

Body-Base.md §4 outline hiện tại organize channels thành **3 sub-categories**:

**§4.1 Loud/Acute Channels** (7 channels):
- §4.1.1 Oxygen (decay: seconds)
- §4.1.2 Water / Hydration (decay: hours-days)
- §4.1.3 Food / Nutrients (decay: days-weeks)
- §4.1.4 Temperature regulation (decay: minutes-hours)
- §4.1.5 Sleep / Circadian rhythm (decay: days-months)
- §4.1.6 Physical safety / pain avoidance (decay: immediate)
- §4.1.7 Elimination / waste removal (decay: hours-days)

Đặc điểm: signals **loud, specific, verbalizable**, mainstream medicine
covers. Research well-established per channel. Framework note các
channels này ít được discuss vì always-available, pathology mới reveal
importance.

**§4.2 Silent/Slow-Decay Channels** (8 channels — explicitly labeled
"NEW FRAMEWORK CONTRIBUTION" trong outline):
- §4.2.1 Movement (decay: days-months)
- §4.2.2 Nature exposure / physical environment (decay: weeks-months)
- §4.2.3 Agent input / social presence (decay: days-weeks)
- §4.2.4 **Living Pattern Input** (decay: weeks-months — labeled "MOST
  NOVEL CONTRIBUTION")
- §4.2.5 Physical touch / skin contact (decay: days-weeks)
- §4.2.6 Deep rest beyond sleep (decay: days-weeks)
- §4.2.7 Sensory diversity (decay: weeks-months?)
- §4.2.8 Silence / auditory recovery (decay: days-weeks?)

Đặc điểm: signals **diffuse, non-specific, hard to verbalize**. Detection
requires cross-boundary methodology. Storage + pattern fire mechanism
(Body-Base.md §7). Evolution calibrated ancestral environments, modernity
often mismatches. Research emerging (biophilia, Attention Restoration,
Shinrin-Yoku, Social Baseline Theory, Aquarium Effect).

**§4.3 Higher-Order Channels** (4 boundary cases):
- §4.3.1 Sexual expression
- §4.3.2 Skilled engagement / flow
- §4.3.3 Meaning / purpose
- §4.3.4 Mastery / self-efficacy

Framework position trong outline: "these boundary cases illustrate that
body-base isn't cleanly separated from higher-order needs. Framework
shows graduated dependency: pure body-base (food) → body-base với L2
component (sexual) → L2 với body-base component (flow) → L2/L3 (meaning)."

**Assumed primitives** trong mô hình cũ: mỗi channel = distinct body-need
với own crash timeline, own feeding pattern, own receptor architecture.
Framework inherits from survival-extreme methodology (Calibration-Inputs-
Analysis §4: Onoda, Proenneke, Knight, McCandless, prison, solitary)
+ passion-extreme methodology (Body-Base-Example.md 50 cases).

**Tensions observed trong existing framework**:

**(1) §14.6 Example**: "**Status/fame/wealth/power as PFC proxies**"
— framework explicitly says những thứ này **không có body-base receiver
trực tiếp**. Nhưng §4.3 vẫn list mastery/meaning/flow ở "higher-order
channels", blur line giữa "body-base channel thực sự" và "PFC construct
feels like channel nhưng không phải." Tension giữa framework structure
và framework findings.

**(2) §14.1 Example**: đề xuất **self-signal channel** (khả năng đọc
trạng thái nội bộ, channel-lexithymia parallel với Bird & Cook 2013)
add vào §4.2 hoặc refine §4.2.3 agent channel. Self-signal là
interoception — fundamentally different category từ "agent channel"
(đọc agent khác). Blur giữa READING capacity và TARGET channel hint
category error in channel taxonomy.

**(3) §13.3 Example**: "channel existence universal, individual
calibration variable." B20 asexuality extreme; B46 Proenneke thrived
solo 30 năm; B50 solitary crashed trong days. Cùng species, radically
different baseline requirements. Variation lớn đến mức hint variation
ở level substrate thấp hơn channel level.

**(4) Channels overlap heavily**: "nature" = vision (fractal patterns,
living motion, depth of field) + audition (ambient soundscape, water,
wind, birds) + olfaction (phytoncides, earth, plants) + thermal skin
(wind, sun, temperature variation) + movement (varied terrain engagement)
+ circadian (natural light). Cannot cleanly isolate which sub-component
is "the nature channel." Implies nature không phải primitive mà là
aggregate.

**(5) Cases multi-channel**: mọi case trong Phase B đều feed/starve
multiple channels đồng thời. Signal isolation nan giải. §13.5 documented
"channel coupling relationships" — meaning + belonging + certainty
coupled, identity + achievement coupled, mastery + community +
transmission coupled. Có thể đây KHÔNG phải separate channels coupled
together, mà là **overlapping body-input aggregates** sharing underlying
substrate.

Năm tensions này không "bug" của work cũ — chúng là **clues** rằng
substrate thấp hơn channel level đang vận hành. Reframe đề xuất làm
substrate đó explicit.

### §1.2 Mô hình mới (reframe)

Reframe đề xuất **3 layers** (không phải 4 như mô hình cũ):

#### §1.2.1 L0 — Alive threshold (binary cease-function)

**Input deviations crossing survival threshold** — binary, qualitative
jump giữa "sống" và "chết":

- Oxygen deprivation (minutes → cerebral hypoxia → death)
- Extreme hyper/hypothermia (hours → organ failure)
- Critical dehydration (days → circulatory collapse)
- Starvation (weeks → metabolic failure)
- Critical injury / blood loss (immediate → shock)
- Suffocation, drowning, electrocution (seconds → neural death)

**Qualitative property**: **BINARY, not graded**. Threshold crossed →
homeostatic function collapse → single-track survival response. Suppresses
all other processing (Body-Dissonance.md §2 "emergency" level: amygdala
hijack, tonic immobility, panic, shutdown ngất).

**Distinct from L1**: L1 có thể deviate mà vẫn homeostatic function
maintained (đói, mệt, khó chịu nhưng functional). L0 crossed → function
không còn. Two qualitatively different mechanisms, không cùng spectrum.

**Evolutionary logic**: L0 inputs có signals **loud, universal,
non-suppressible** vì mistakes here = dead. Negativity bias + loss
aversion amplified ở L0 level (Baumeister 2001, Kahneman & Tversky
1979). Evolution không chấp nhận false-negatives ở L0.

**Mapping với Body-Base.md §4.1 Loud/Acute channels**: L0 tier tương ứng
với extreme ends của §4.1 — oxygen deprivation (§4.1.1 severe), critical
dehydration (§4.1.2 severe), starvation (§4.1.3 severe), extreme temperature
(§4.1.4 critical), critical injury (§4.1.6 severe). §4.1 channels spectrum
từ mild (L1 territory) đến severe (L0 territory).

#### §1.2.2 L1 — Body-inputs với adaptive baseline

**The core substrate layer**. Liệt kê 3 sub-categories theo neuroscience
standard taxonomy:

**Exteroceptive inputs** (sensing external world) — §2:
- Vision (§2.1) — photons, spatial patterns, motion, depth, faces,
  biological motion, fractal dimension
- Audition (§2.2) — sound pressure waves, frequencies, locations,
  voices, environmental soundscape, silence quality
- Olfaction (§2.3) — chemical airborne, evolutionarily oldest, limbic
  direct access
- Gustation (§2.4) — taste receptors (sweet/salty/sour/bitter/umami/
  fat)
- Tactile skin (§2.5) — thermoreception skin + mechanoreception
  (pressure/texture/vibration) + affective touch C-tactile fibers

**Proprioceptive inputs** (sensing body position) — §3:
- Proprioception (§3.1) — muscle spindles + joint receptors + Golgi
  tendons → limb position awareness without vision
- Vestibular (§3.2) — inner ear semicircular canals + otoliths → head
  orientation, acceleration, gravity
- Kinesthetic (§3.3) — muscle activity dynamics, effort, fatigue,
  recovery metabolic signals

**Interoceptive inputs** (sensing internal state) — §4:
- Thermoreception core (§4.1) — hypothalamic core body temp regulation
- Nociception (§4.2) — tissue damage signaling, A-delta (fast sharp)
  + C-fibers (slow burning)
- Respiratory (§4.3) — breath rate, depth, CO2 chemoreception, effort
- Cardiovascular (§4.4) — heart rate, blood pressure, vagal tone,
  HRV interoceptive index
- Visceral (§4.5) — gut motility, organ states, nausea, fullness,
  enteric nervous system
- Metabolic (§4.6) — blood glucose, hydration, ghrelin/leptin, hunger/
  satiety, hypoglycemia
- Hormonal-sensed (§4.7) — cortisol/testosterone/oxytocin/dopamine/
  serotonin/endorphin effects felt as body states
- Sleep/Circadian (§4.8) — sleep architecture (REM/NREM), circadian
  alignment, rest state
- **Self-signal interoception (§4.9)** — **META-input**: capacity to
  read own internal state (insula, ACC, predictive interoception —
  Craig 2009, Seth 2013, Barrett 2017). Channel-lexithymia parallel
  với clinical alexithymia (Bird & Cook 2013).

**Tại sao 3 categories**: mirror neuroscience standard taxonomy của
sensory systems. Exteroception/Proprioception/Interoception là neural
architecture-level distinction, không phải arbitrary cluster. Mỗi
category có different afferent pathways, different cortical processing
(exteroception → primary sensory cortices; interoception → insula-ACC;
proprioception → somatosensory + cerebellum). Tách 3 category cho clarity
theoretical, không tách nhân tạo.

**Adaptive baseline property** — core mechanism của reframe:

Mỗi input có **evolved baseline range** (calibrated over 2M năm ancestral
environment) + **individual baseline** shifted bởi development trong
bounds của evolved range. Formally:

```
  Evolved baseline range  → calibrated over 2M năm ancestral environment
                           → boundaries cho individual variation
  Individual baseline     → shifted by development, personal calibration
                           → shifts within evolved bounds
  Current input quality   → measured vs individual baseline
                           → generates signal

  Deviation below baseline → dissonance (bứt rứt → khó chịu → đau)
                           → severity scales với deviation magnitude
  Deviation above baseline → reward → Novelty fires
                           → pattern repeat → baseline shifts upward
                           → hedonic treadmill (Brickman 1971)
  Loss of elevated baseline → dissonance at new higher expected floor
                           → silk → cotton feels rough
                           → gourmet → rice feels plain
                           → engineered beauty → reality feels bland
```

Repeated exposure to above-baseline input → **hedonic treadmill
effect**: baseline shifts upward, cái từng là reward trở thành new
normal. Explains tại sao wealth không làm người hạnh phúc permanently
(Kahneman), tại sao mastery phải tiếp tục progress (B30 Jiro 99 năm
"still not satisfied"), tại sao food gets boring without variation.

Asymmetry quan trọng: **baseline shift UP** (adaptation) nhanh hơn
**baseline shift DOWN** (de-adaptation). Evolution favors acquiring
novelty (opportunity) over losing it (threat/regression). Giải thích
pattern fire + storage + decay model đã mentioned trong Body-Base.md
§7 outline.

#### §1.2.3 L3 — PFC drives acting on L1

**KEY REFRAMING**: L3 **không phải layer of new needs** trên L1. L3 =
**OPERATORS acting on L1 body-inputs**. Three drives:

**Novelty operator**:
- Searches for above-baseline input quality
- Fires on positive prediction error (Berlyne 1960 optimal novelty;
  Schultz dopamine prediction error research)
- Drives baseline shifting upward — đây là **mechanism** cho hedonic
  treadmill ở §1.2.2
- Operates across ALL body-input categories — mọi input có thể là
  Novelty target
- Individual variation: DRD4 gene allele, temperament (Kagan high-
  reactive/low-reactive)
- Existing framework: Novelty.md đã cover drive level

**Status operator**:
- Organizes social environment để **amplify** hoặc **protect** L1
  input supply
- Community position → reliable agent co-presence inputs (vision,
  audition, touch, olfaction from other humans)
- Reputation → resource access → guaranteed metabolic inputs
- Dominance → protection from L1 threats
- Attention/recognition → agent mirroring inputs (via Empathy-Mirror)
- **Status itself has NO body-base receiver** — it's a PFC construct
  that **proxies** for L1 access
- Matches §14.6 Example finding: "status/fame/wealth/power as PFC
  proxies" — reframe làm explicit at framework level
- B2 billionaire emptiness, B36 fame emptiness = status achieved
  without L1 body-input payoff → empty

**Protect operator**:
- Guards L1 inputs from threats (L0 proximity, L1 damage, supply
  disruption)
- Extends via **Empathy-Mirror mechanism** (Empathy-Mirror.md) để
  include mirrored body-states của người khác
- Mirror creates bản sao (weaker) of other's body-state → fires own
  L1 inputs → Protect operator generates protect-other behavior
- Explains empathy-driven behavior như helping soldiers (user's
  "giúp bộ đội có gạo" question): mirror other's hunger/threat
  state → own L1 fires → Protect extends to them → feeding them
  = feeding own mirrored L1 via mechanism
- Không mysterious "feeling for others" — cụ thể: body-input mirroring
  + Protect operator

#### §1.2.4 Tại sao vẫn 3 layers, không phải 2

Bạn có hỏi: "Tại sao không 2 layers — body-input ↔ vô thức, drives ↔
PFC?"

Reframe giữ L0 distinct từ L1 vì:

**(a) Binary vs graded mechanism**:
- L0 = binary threshold (crossed hoặc không, cease-function)
- L1 = graded quality (deviation magnitude scales dissonance linearly)

**(b) Qualitatively different response systems**:
- L0 response = shutdown / single-track survival / amygdala hijack /
  autonomic extreme
- L1 response = homeostatic correction + behavioral adaptation +
  PFC participation possible

**(c) Evolution wired them differently**:
- L0 signals **loud, non-suppressible** (Body-Dissonance §2 emergency
  level)
- L1 signals softer, allow multitasking, PFC can modulate

**(d) Concrete test**: nhịn thở vài phút crosses L0 (cerebral hypoxia
starting) — response = panic, drive to breathe overrides everything.
Thở không khí trong lành vs ngột ngạt ở bình thường = L1 — dissonance
nhẹ, PFC có thể chịu để focus vào task.

Hai cái không cùng mechanism, không cùng spectrum. Merging chúng vào
"body-input ↔ unconscious" loses qualitative distinction.

#### §1.2.5 Cái gì bị removed từ mô hình cũ

**L2 Quality as separate layer** — removed.

"Quality" channels trong mô hình cũ (silk over cotton, gourmet over
rice, music over noise, beautiful scenery over urban) reframe là **L1
body-inputs với baseline shifted upward by Novelty operator**.

Slow-decay phenomenon (silent/slow-decay channels trong Body-Base.md
§4.2) reframe là **baseline adaptation + loss creates dissonance**.
Không cần category riêng cho "slow-decay channels."

Existing Body-Base.md §4.2 channels reframe thành **body-input aggregates
operated on by Novelty**:

| Channel cũ          | Body-input aggregate (reframe)                        |
|---------------------|-------------------------------------------------------|
| §4.2.1 Movement     | proprioception + kinesthetic + vestibular + cardio   |
| §4.2.2 Nature       | vision + audition + olfaction + thermal + circadian   |
| §4.2.3 Agent        | vision (faces) + audition (voices) + affective touch  |
|                     | + olfaction + empathy-mirror + oxytocin               |
| §4.2.4 Living ptn   | vision (bio motion) + audition (ambient life sounds)  |
| §4.2.5 Touch        | tactile skin + affective touch + proprioception       |
| §4.2.6 Deep rest    | self-signal awareness + parasympathetic + low demand  |
| §4.2.7 Sensory div  | Novelty variance across all sensory inputs            |
| §4.2.8 Silence      | audition baseline at low-amplitude natural soundscape |

§8 sẽ làm mapping này chi tiết với evidence từ research + cases.

§4.3 Higher-Order boundary cases reframe thành **drives tác động trên
L1 inputs**:

| Channel cũ         | Reframe (drive × body-input compound)                  |
|--------------------|--------------------------------------------------------|
| §4.3.1 Sexual      | hormonal-sensed + tactile + affective touch + Novelty  |
| §4.3.2 Flow        | proprio/kinesthetic + Novelty + self-signal absorption |
| §4.3.3 Meaning     | **primarily schema layer** + self-signal interoception |
| §4.3.4 Mastery     | Novelty on skill progression + self-signal + Status    |

Meaning đặc biệt: primarily schema-level construct, không phải pure
body-input. Reframe treat meaning là schema dissonance/coherence mechanism
mà ảnh hưởng baseline expectations across body-inputs. §7.1 detail.

**Cái không bị removed**:
- 3 body signals (Satisfaction/Reward/Dissonance) — unchanged
- 4-tier calibration theory từ Why-Body-Knows — unchanged
- Empathy-Mirror mechanism — unchanged (đã là mechanism)
- Feeling folder PFC observation interface — unchanged
- Dissonance spectrum từ micro đến emergency — unchanged, chỉ re-map
  sources
- Pattern fire + storage + decay — unchanged mechanism, applied ở
  baseline level thay vì channel level

### §1.3 Tại sao reframe parsimony cao hơn

Năm lập luận:

#### §1.3.1 Giải thích channel enumeration fuzziness

Channels trong mô hình cũ luôn mờ vì **chúng không tồn tại như
primitives**. Chúng là **aggregates**.

"Nature need" thực ra = mix of:
- Vision (fractal patterns D≈1.3-1.5, biological motion, depth of field,
  natural light spectrum)
- Audition (pink noise soundscape, water, wind, birds, distant animals)
- Olfaction (phytoncides, earth, plants, water)
- Thermoreception skin (wind, sun, temperature variation)
- Proprioception (varied terrain engagement)
- Circadian (natural light alignment)

Mỗi component có own receptor system, own neural pathway, own adaptation
dynamics. Không có single "nature receptor" trong body. "Nature channel"
chỉ tồn tại vì các components này co-occur trong ancestral environment.

Không ngạc nhiên chúng overlap (B6 nomad visual rich, nhưng ancestral
audio/olfactory/thermal different). Không ngạc nhiên chúng không tách
sạch trong Phase B analysis — vì ontologically chúng là **arbitrary
cluster boundaries** drawn trên substrate of overlapping body-inputs.

**Example application**: §13.5 Example documented "channel coupling
relationships" — meaning + belonging + certainty coupled, identity +
achievement coupled, mastery + community + transmission coupled.

Reframe interpretation: đây KHÔNG phải separate channels coupled together
through some mysterious mechanism. Đây là **overlapping body-input
aggregates + schema structures** sharing underlying substrate. Coupling
không phải phenomenon requires explanation, mà là **baseline fact** của
cluster boundaries khi vẽ trên substrate.

#### §1.3.2 Giải thích slow-decay without new category

Body-Base.md §4.2 label "NEW FRAMEWORK CONTRIBUTION" cho silent/slow-decay
channels (nature, movement, touch, agent, living pattern, etc.).

Reframe: **baseline adaptation + loss = mechanism**. Không cần category
riêng cho "slow-decay channels." Chỉ cần mechanism baseline adaptation
applied to appropriate body-input clusters + slow-decay = asymmetric
baseline decay time constant.

**Example**: "nature deficit disorder" (Louv 2005) reframe là body-input
cluster (visual fractal + audition ambient + olfactory phytoncides +
thermal variation + circadian natural light) collectively deviating
below ancestral baseline qua sustained urban exposure. Mỗi input adapt
individually (urban dwellers develop tolerance), aggregate effect =
diffuse unease. Không cần "nature channel" như primitive để explain
phenomenon.

**Parsimony gain**: remove one framework primitive ("slow-decay channel
category"), explain same phenomena với fewer concepts. Occam's razor
favor reframe.

#### §1.3.3 Giải thích iPad case elegantly

User's iPad example: PFC predict body-input improvement (visual quality
"wow", tactile interaction, portability), body test trong domain real,
thấy trade-offs negative (heavy cầm lâu, focus kém hơn đọc sách giấy,
precision kém hơn Wacom cho vẽ) vượt positive → pattern không shift,
iPad vào xó.

**Mô hình cũ explanation**: "quality channel prediction error" — PFC
predicts one channel will be fed, body finds it isn't, channel
expectations adjust. Clunky because "quality channel" concept isn't
well-defined.

**Mô hình mới explanation**: PFC predicts L1 changes (vision quality
improvement, tactile novelty, portability convenience). Body tests
trong real use. Trade-offs emerge (vestibular weight, attention
fragmentation, precision shortfall). Pattern adjustment outcome: iPad
doesn't shift baseline upward sustainably. Elegant because mechanism
is directly L1-level, không cần intermediate "quality channel" concept.

**Meta-lesson**: reframe KHÔNG add new machinery to explain this case.
It removes machinery (quality channel) và uses pure L1 + baseline
adaptation. Parsimony gain.

#### §1.3.4 Match existing §14.6 finding explicitly

Body-Base-Example.md §14.6 đã explicit:

> "Framework-level refinement: Body-Base.md phải explicitly distinguish
> **real body-base channels** từ **PFC proxies that feel like channels
> but aren't**. Status/fame/wealth are PFC constructs; body-base has
> no direct receiver for them."

Mô hình cũ treat status/fame/wealth ở §4.3 "higher-order channels"
boundary, tạo tension giữa framework structure và framework finding.

Reframe resolve tension **at framework level**: **status/fame/wealth =
PFC drives (Status operator) acting on body-inputs via proxy mechanism**.
Không phải channels, không phải body-needs. Là drives operating on L1
substrate via social infrastructure.

**Cases validating**:
- B2 billionaire achieves wealth → status drive satisfied → L1 body-inputs
  not fed by wealth directly → emptiness (body-input access not auto-follow
  wealth)
- B36 fame seeker achieves recognition → status drive fires → L1 body-inputs
  not fed by recognition directly → insufficient
- B38 power obsession → status drive → control over agents, nhưng no
  guaranteed L1 body-input feeding
- B40 Rothschild multi-generational dynasty → status đạt được, nhưng
  value comes from L1 proxying (resource security for descendants),
  not status itself

Reframe makes explicit what §14.6 already knew. No new evidence needed,
just clarification at framework level.

#### §1.3.5 Compatible với Empathy-Mirror mechanism logic

Empathy-Mirror.md đã treat empathy là **MECHANISM, không phải channel**:

> "Empathy-Mirror = cơ chế body tạo bản sao body-state của sinh vật
> khác trong body mình... Empathy KHÔNG phải channel (không phải
> body-need). Đây là MECHANISM — giống VTA detect biến động, giống
> cortisol sustain neurons."
>
> "Empathy-Mirror feed vào channels đã có — cross-cutting toàn bộ
> Body-Base."

Reframe extends **cùng logic** đến toàn bộ channel system: **"channels"
are all emergent from lower-level substrate**. Empathy precedent validates
treating channels not as primitives but as substrate patterns.

Frame mới consistent với frame cũ của Empathy-Mirror — empathy = mechanism,
channels = aggregates of body-inputs + schema structures. Cả hai level
sâu hơn primitives. Body-Input-Enumeration.md extends same reductive
move from "empathy is mechanism not channel" to "all channels are
aggregates not primitives."

**Meta-point**: framework đã sẵn sàng cho move này. Empathy-Mirror.md
đã dọn đường. Reframe không mâu thuẫn existing work, nó complete existing
reductive move.

#### §1.3.6 Tóm tắt parsimony argument

Reframe không reject findings của 50 Phase B cases. Nó REORGANIZE findings
ở level sâu hơn. Work cũ trở thành **evidence chapters** cho reframe,
không bị vứt.

Reframe explains TẠI SAO existing findings looked the way they did:
- Channel fuzziness → aggregates
- Slow-decay → baseline adaptation mechanism
- Multi-channel cases → substrate level variation
- Status/fame as proxies → Status drive operating on L1
- Coupling relationships → overlapping aggregates
- Individual variation → substrate calibration variation

Mô hình mới explain được tất cả mô hình cũ explain được, **plus** giải
thích tensions trong §14.1, §14.6, §13.3, §13.5 mà mô hình cũ để mờ.
Parsimony gain không chỉ qua removing concepts (L2 layer) mà còn qua
explaining more với less.

### §1.4 Test criteria

#### §1.4.1 Reframe PASS conditions

Reframe **PASSES** nếu tất cả các điều sau đều satisfied:

**(1) Enumeration completeness** (§2-§4 test):
- Mỗi body-input category (exteroceptive/proprioceptive/interoceptive)
  có thể enumerated với ancestral baseline + individual baseline
  + deviation spectrum (negative + positive) + adaptation mechanism
  + research citations
- Không có sensory/interoceptive category nào bị bỏ sót
- Self-signal interoception (§4.9) có architectural central role

**(2) Mechanism coherence** (§5 test):
- Baseline adaptation + Novelty shifter + decay model logically
  self-consistent
- Match established research: hedonic treadmill (Brickman 1971,
  Frederick 1999), supernormal stimulus (Tinbergen 1951), mere
  exposure (Zajonc 1968), Goldilocks optimal novelty (Berlyne 1960)
- Explain asymmetry giữa baseline shift up và down
- Evolutionary logic for why baseline adaptation exists

**(3) Drive operation coherent** (§6 test):
- Novelty/Status/Protect hoạt động trên body-inputs như operators
- Không cần intermediate "quality channels" để mediate
- Status drive reduces to L1 proxy mechanism cleanly
- Protect drive integrates với Empathy-Mirror mechanism cleanly

**(4) Dissonance mapping clean** (§7 test):
- 6 nguồn dissonance trong Body-Dissonance.md §2.5 map cleanly:
  - Info mismatch → schema layer
  - Body-state delta → L1 body-inputs
  - Threat schema → schema layer (with L1 prediction)
  - Physical damage → L1 (nociception) extreme or L0
  - Social damage → L1 agent co-presence inputs + empathy-mirror
  - Melody learning → schema layer
- Không gap uncovered
- 14-level spectrum §2 re-maps cleanly

**(5) Case coverage** (§9 test):
- Selected 15 cases + DC1 Tesla + DC3 nomad all explainable via
  reframe
- Majority PASS (reframe explains equally well or better), minority
  PARTIAL (reframe needs minor patches), zero FAIL (reframe cannot
  explain without adding epicycles)

**(6) Theory integration intact** (§10 test):
- Why-Body-Knows 4-tier calibration theory unchanged, enhanced
- Body-Dissonance signal mechanism unchanged
- Empathy-Mirror mechanism unchanged, extended logic consistency
- Feeling folder PFC observation interface unchanged
- No contradiction với existing framework foundations

**(7) No regression in explanatory power**:
- Reframe explain được mọi thứ mô hình cũ explain được
- PLUS giải thích tensions trong §14.6 proxies, §14.1 self-signal
  category, §13.3 variation scale, §13.5 coupling
- Parsimony gain (fewer primitives, more explanation)

#### §1.4.2 Reframe FAIL conditions

Reframe **FAILS** nếu any one of the following:

**(a) Irreducible channel**: một hoặc nhiều channels không reduce
được về body-input clusters mà không loss of meaning. Ví dụ candidate:
"meaning channel" có thể là pure schema-level construct không có
body-input payoff. Nếu meaning không fit, reframe cần patch hoặc
scope limitation.

**(b) Unexplainable case**: một case trong §9 test mà mô hình cũ
explain clean nhưng reframe không explain được. Cases candidate
risk: meaning-over-fed cases (B21 religious fanatic, B22 cult), nếu
meaning không reduce, cases này failure điểm.

**(c) Dissonance gap**: một dissonance type không thuộc L0/L1/schema
mapping. Risk candidates: "lấn cấn" (micro-mismatch) — có thuộc
schema level không, hay một category riêng?

**(d) Empirical contradiction**: research contradicts baseline
adaptation mechanism ở required scale. Ví dụ: nếu có input category
mà baseline hoàn toàn không adapt (evidence strong), reframe mechanism
fails cho category đó.

**(e) Epicycles required**: nếu để cover gaps cần add special cases
dần dần → framework more complex than original → parsimony lost.
Reframe phải cleaner than existing, không clunkier.

#### §1.4.3 Intermediate outcomes

Có thể không strict PASS/FAIL. Outcomes trung gian:

**PARTIAL PASS — patch needed**: most criteria met, 1-2 gaps
identified. Specific patches documented, verdict → commit với
patches (Option B trong §12).

**PARTIAL PASS — parallel models**: reframe works cho substrate,
channel language works cho practical vocabulary. Both preserved,
relationship documented (Option C trong §12).

**PARTIAL FAIL — scope limitation**: reframe works cho pure body-input
channels, không work cho schema-dominant channels (meaning, mastery).
Accept scope limit, document explicitly.

**FULL FAIL — reject**: systematic failures across multiple criteria,
no clean patches. Alternative direction needed.

#### §1.4.4 Decision rule

Verdict §12 integrates results từ:
- §2-§4 enumeration thoroughness
- §5-§7 mechanism coherence
- §9 case coverage distribution
- §10 integration verification
- §11 honest assessment (strengths vs gaps)

Decision là judgment call, không formula. Nhưng each criterion provides
evidence. Documented reasoning in §12.

---

## §2 — EXTEROCEPTIVE INPUTS

> **Section structure note**: mỗi input subsection follows schema:
> (a) what body measures, (b) ancestral baseline, (c) deviation
> spectrum negative, (d) deviation spectrum positive, (e) baseline
> adaptation examples, (f) key research, (g) Phase B case mapping,
> (h) individual variation note.

### §2.1 Vision (Mắt)

**(a) Body đo gì**

Vision system đo multi-dimensional:
- **Photons + wavelength distributions**: intensity (luminance), color
  spectrum
- **Spatial patterns**: edges, textures, shapes, **fractal dimension**
  (Taylor 2006 — D ≈ 1.3-1.5 optimal preference)
- **Motion**: temporal dynamics, với dedicated subsystem cho **biological
  motion** (point-light display research — brain has specialized detection
  for living movement)
- **Depth cues**: binocular disparity, accommodation, motion parallax,
  texture gradient
- **Faces**: fusiform face area (FFA) specialized processing
- **Light level cho circadian signaling**: SCN via melanopsin retinal
  ganglion cells (Berson 2002) — bypasses visual conscious pathway,
  direct biological clock feed

Vision không phải "một" input — là compound sub-input aggregate. Mỗi
sub-input có own neural pathway + adaptation dynamics.

**(b) Ancestral baseline** (2M năm hominid evolution)

Visual environment baseline tổ tiên:
- ~12-hour **daylight/darkness cycle** (equatorial origin)
- **Fractal dimension D ≈ 1.3-1.5** trong natural environments (cây, đất,
  bờ biển, lá, mây) — Taylor 2006 preference research
- **Living motion prevalent** trong field of view: humans, động vật, cây
  đung đưa, chim bay — biological motion baseline always present
- **Mixed vegetation + open sight lines** (Savanna hypothesis, Orians 1992)
- Natural color spectrum varied theo sunlight angle (sunrise, noon, sunset)
- **Horizon visible** — depth of field varied, distance cues available
- Face exposure: 30-150 individuals trong tribe (Dunbar number)
- **Darkness at night** — no artificial light pollution

Evolution calibrated visual system để detect deviation từ baseline này là
biologically meaningful.

**(c) Negative deviations → dissonance**

- **Darkness prolonged** (cave, cellar, solitary windowless): circadian
  disruption, vitamin D deficiency, mood decline, seasonal affective
  pattern
- **Static visual environment** (4 walls, office cubicle, no window):
  Kaplan attention fatigue, user phenomenology "đần đầu"
- **Absent biological motion** (sterile environment, solitary): Living
  Pattern Input deficit (§4.2.4 Body-Base.md) — brain baseline expects
  life nearby, sterile violates expectation
- **Visual overload** (urban density): over-firing, seek retreat, sensory
  fatigue
- **Fluorescent/blue light chronic**: circadian misalignment, melatonin
  suppression, "mệt mắt"
- **Too-low fractal dimension**: walls D≈1.0, uniform geometric
  environments → not engaging enough, Hagerhall EEG studies
- **Ugly scenes** (schema-mediated): rác, chaos, visual disorder — "nhìn
  ngứa mắt" (overlaps schema dissonance layer)

**(d) Positive deviations → reward → baseline shift**

- **Beautiful natural vistas**: above-baseline fractal + depth + color +
  living motion compound (Ulrich 1991 — hospital window view study
  reduced cortisol measurably)
- **Art, engineered beauty**: supernormal visual stimulus (Tinbergen
  principle applied to vision — architectural golden ratio, composition
  rules, color theory)
- **Sunset, aurora, rare phenomena**: high visual novelty + safety context
- **Attractive faces** (Langlois 1990): average-face preference, symmetry,
  neoteny → evolved supernormal composite face attraction
- **Biophilic architecture**: natural elements integrated (plants, water,
  wood textures) → reduces cortisol vs sterile design (Kellert research)

**(e) Baseline adaptation examples**

- **Urban dwellers**: adapted to high visual density, rural feels empty/
  sparse
- **Rural visitors to city**: overwhelmed, "too much," seek retreat
- **Instagram/HD screen users**: baseline shifted upward dramatically,
  unadorned reality feels dull, need more stimulation
- **Dark adaptation**: eyes adjust in minutes (rhodopsin chemistry — fast
  adaptation)
- **Cultural visual grammar**: East Asian field-focused attention vs
  Western object-focused (Masuda & Nisbett 2001) — shapes what visually
  "normal" means

Adaptation dynamics: baseline shift **upward** (toward engineered beauty,
high density) faster hơn shift **downward**. De-adapting to urban density
takes weeks rural exposure; re-adapting to urban happens in days.

**(f) Research citations**

- 🟢 Taylor, R. (2006). Fractal preference D≈1.3-1.5
- 🟢 Hagerhall, C. et al. (2004, 2008). Fractal EEG response
- 🟢 Kaplan, R. & Kaplan, S. (1989). "Experience of Nature" — Attention
  Restoration Theory
- 🟢 Ulrich, R. (1991). Stress Reduction Theory — hospital window study
- 🟢 Orians, G. (1992). Savanna hypothesis
- 🟢 Langlois, J. et al. (1990). Average face attractiveness
- 🟢 Masuda, T. & Nisbett, R. (2001). Cultural attention patterns
- 🟢 Berson, D.M. et al. (2002). Melanopsin retinal ganglion cells
  circadian
- 🟡 Salingaros, N. Biophilic design theory
- 🟡 Kellert, S. Biophilic design research

**(g) Phase B case mapping**

- **B46 Proenneke** (30 năm Alaska cabin): visual substrate rich daily —
  fractal patterns, biological motion of wildlife, horizon depth, natural
  light full spectrum. Validates vision substrate fed ancestral.
- **B45-B48 survival cases** (Onoda, Proenneke, Knight, McCandless): all
  rich natural visual substrate. When nature visual adequate, humans
  functional decades dù minimal agent input.
- **B50 solitary confinement**: visual deprivation extreme — static cell,
  no biological motion, no depth, fluorescent only. Rapid crash trong
  days. Validates vision critical L1 substrate.
- **B5 karoshi**: 12+ giờ office fluorescent, no natural light, static
  screen focus, minimal biological motion. Long-term visual substrate
  deprivation accumulates.
- **B6 digital nomad**: visual **variety** rich (new locations) BUT
  lacking consistent familiar visual patterns + embeddedness. Reveals
  visual variety ≠ visual substrate fed.
- **B35 screen addiction**: engineered visual supernormal (refresh rate,
  content density, constant novelty) → baseline shift extreme upward →
  unmediated reality feels dull.
- **DC1 Tesla** late-life isolation: visual input reduced (few visitors,
  hotel room), parasocial bonds với pigeons = partial biological motion
  feed.
- **DC3 ancestral nomad vs digital**: ancestral = varied landscapes +
  familiar community faces daily; digital = constant new landscapes +
  unfamiliar faces. Variety present both, substrate (consistency +
  embeddedness) absent in digital.

**(h) Individual variation**

- **Sensory Processing Sensitivity** (SPS, Aron 1997): ~15-20% population
  high sensitivity → lower tolerance cho visual overload
- **Introversion/extroversion**: affects visual stimulation tolerance
  optimal point
- **Cultural visual grammar**: East Asian field vs Western object attention
- **Aesthetic baseline**: shifted dramatically by cultural exposure
- **Age**: aging vision needs more light, less contrast tolerance
- **Genetic color vision variation**: 2-deuteranomaly, tetrachromats, etc.

Individual calibration variation LỚN cho vision, consistent với §13.3
Example finding "channel existence universal, individual calibration
variable."

### §2.2 Audition (Tai)

**(a) Body đo gì**

Auditory system đo:
- **Sound pressure waves**: amplitude (loudness dB), frequency (pitch Hz)
- **Frequency distribution**: timbre, harmonic content, spectral envelope
- **Spatial location**: interaural time difference (ITD) + interaural
  level difference (ILD) → 3D sound localization
- **Temporal patterns**: rhythm, envelope, transients, phase relationships
- **Language prosody**: emotional tone, intention, speaker identity
- **Environmental signature**: safety/threat cues từ ambient soundscape
- **Own body sounds**: heartbeat, breath, footsteps, chewing (crossover
  với interoception)
- **Silence quality**: presence hoặc absence của expected ambient patterns

Audition evolved primarily cho **threat detection** (predators, falling
objects, thunder) + **social communication** (voices, emotional prosody).

**(b) Ancestral baseline**

Auditory environment baseline tổ tiên:
- **Environmental ambient**: lá xào xạc, suối chảy róc rách, gió thổi,
  tiếng động vật xa, sóng biển, mưa nhẹ
- **Pink noise patterns** (1/f spectrum): natural acoustic environment
  follows pink noise statistics (Voss & Clarke 1975) — optimal for
  attention restoration
- **Social voices**: 30-150 tribe members conversing, laughter, singing,
  storytelling nearby
- **Occasional threat sounds**: sấm, tiếng thú ăn thịt xa, tiếng cây đổ,
  tiếng đồng loại kêu cứu
- **Silence only temporary**: ban đêm + trong shelter, never prolonged
  anechoic
- **Own bodily sounds audible**: footsteps trên terrain varied, breathing,
  chewing
- **NOT**: constant mechanical hum, traffic, appliance drone, total silence
  prolonged

**(c) Negative deviations → dissonance**

- **Noise pollution sustained**: traffic, machinery, 70+ dB chronic →
  cortisol elevation, hearing damage, attention fragmentation, sleep
  disruption (WHO 2011 noise burden research — major public health issue)
- **Total silence prolonged**: anechoic chamber, soundproof room → body
  detects own heartbeat + blood flow → anxiety, disorientation, "can hear
  your own breathing" — ancestral baseline never this silent
- **Acoustic isolation từ social sounds**: headphones + solitary life →
  agent auditory component starved
- **Mechanical drone chronic**: fluorescent ballast hum, AC, refrigerator,
  traffic → masks ancestral pink noise patterns, attention rarely rests
- **Discordant sounds**: pattern mismatch → schema-mediated dissonance
  ("bài này không hay")
- **Tinnitus**: internal auditory signal ghost, chronic dissonance input
- **Sudden loud sounds**: startle response, cortisol spike (threat
  residual)

**(d) Positive deviations → reward → baseline shift**

- **Nature ambient**: sóng biển rì rào, suối chảy róc rách, lá xào xạc,
  mưa nhẹ → optimal pink noise + pattern complexity (most restorative per
  research)
- **Quality music**: engineered acoustic novelty + coherence (North &
  Hargreaves 1995 — inverted-U pleasure × familiarity, Berlyne optimal
  novelty)
- **Loving voice tone**: evolved oxytocin response từ prosody + infant-
  directed speech
- **Laughter** (bạn bè kể chuyện): social reward audio signature,
  contagious (Provine 2000)
- **Rhythmic synchronization**: dance, chant, drumming — ancient social
  bonding mechanism, endorphin release
- **Silence contrast**: sau noise, silence feels reward — restoration

**(e) Baseline adaptation examples**

- **Urban dwellers** sleep through traffic (baseline shifted), rural
  silence wakes them ("too quiet")
- **Rural visitors to city**: overwhelmed trong days, sensory fatigue
- **Musicians**: develop elevated baseline cho acoustic complexity, simple
  music feels empty
- **Constant earbud users**: silence becomes intolerable, "quá yên tĩnh"
- **Vietnamese đường phố ồn ào**: acclimated baseline → visitors to
  Vietnam overwhelmed initially
- **Language learners**: phoneme perception baseline shifts with exposure
  (Kuhl 1992 — native language magnet effect, critical period ~age 7-10)

**(f) Research citations**

- 🟢 WHO (2011). "Burden of disease from environmental noise"
- 🟢 Kryter, K. (1994). "Handbook of Hearing and the Effects of Noise"
- 🟢 Goines, L. & Hagler, L. (2007). Noise pollution health review
- 🟢 Voss, R. & Clarke, J. (1975). "1/f noise in music and speech" —
  pink noise aesthetics
- 🟢 North, A. & Hargreaves, D. (1995). Music preference × familiarity
  inverted-U
- 🟢 Kuhl, P. (1992). Native language magnet effect
- 🟢 Zentner, M. (2008). Music preference development
- 🟢 Provine, R. (2000). "Laughter: A Scientific Investigation"
- 🟡 Baguley, D. et al. (2013). Tinnitus review — 10-15% prevalence

**(g) Phase B case mapping**

- **B46 Proenneke**: rich natural audio daily — wildlife calls, water,
  wind, minimal mechanical intrusion. Validates audition substrate fed
  ancestrally.
- **B50 solitary**: silence deprivation paradox — too much mechanical
  silence AND lack of natural soundscape + social voices. Multi-dimensional
  auditory starvation.
- **B5 karoshi**: office HVAC hum, colleague conversations, phone rings
  → mechanical baseline dominates, ancestral auditory substrate largely
  absent.
- **B28 chess master**: silence REQUIRED for deep concentration — flow
  state needs reduced auditory competition. Silence as positive resource.
- **B41 artist mania**: music immersion — engineered acoustic stimulus
  at high intensity → baseline shift dramatic.
- **B9 Blue Zone farmer**: rich natural soundscape + community voices
  daily, minimal mechanical.
- **B11 codependent**: social audio always present but unidirectional
  (listening to other's state), no own voice space.
- **DC1 Tesla** late-life: hotel room limited social voices, mechanical
  city sounds, parasocial bonds với pigeons provide limited biological
  audio feed.
- **DC3 ancestral nomad**: communal audio daily — chanting, conversation,
  child sounds, shared soundscape vs digital nomad often isolated audio
  (earbuds, translated text, asynchronous communication).

**(h) Individual variation**

- **Auditory processing sensitivity**: misophonia (specific trigger sounds
  cause extreme reaction), hyperacusis, central auditory processing
  disorders
- **Tinnitus prevalence**: 10-15% adult population (Baguley 2013) — permanent
  auditory input shift
- **Musical training**: shifts baseline for acoustic complexity tolerance
- **Language learning age**: native phoneme baseline locked ~age 7-10
- **Age**: presbycusis (high-frequency hearing loss) progressively shifts
  elderly baseline
- **ADHD**: often co-occurs với auditory distraction sensitivity

Variation substantial, với specific pathologies (misophonia, tinnitus)
shifting personal baseline dramatically.

### §2.3 Olfaction (Mũi)

**(a) Body đo gì**

Olfactory system đo:
- **Airborne chemical molecules**: ~400 functional olfactory receptor
  genes trong humans (Buck & Axel 1991 Nobel research 2004)
- **Complex chemical signatures**: blends forming recognizable smells
  (rose, bread, smoke, rotting meat)
- **Distinctive property**: evolutionary OLDEST sense — direct limbic
  system access (olfactory bulb → amygdala + hippocampus without
  thalamic routing like other senses)
- **Proust effect** (Herz research): olfactory-memory coupling particularly
  strong because of direct limbic pathway
- **Pheromone detection**: classical pheromone research mixed in humans,
  some evidence for chemical communication of emotional/health state

Distinctive từ các senses khác: olfactory signals bypass thalamic filtering
→ direct emotional + memory coupling. Explains why smells trigger
strong emotional memories.

**(b) Ancestral baseline**

Olfactory environment baseline tổ tiên:
- **Natural mixed smells**: vegetation (leaves, flowers, grass, wood,
  pine), earth (damp, dry, rich), water (fresh, salty, stagnant)
- **Food smells**: meat cooking over fire, ripening fruit, fermentation,
  roasting nuts
- **Smoke**: fire ubiquitous daily signal
- **Other bodies**: familiar individual scents (infant-mother especially —
  infants recognize mother by smell), tribe member familiar odors
- **Animal smells**: prey, predator, livestock (after domestication)
- **Seasonal variations**: spring bloom, autumn decay, winter cold
- **Own body smell** variable với activity + infrequent bathing
- **Phytoncides**: plant antimicrobial compounds released into air,
  constant forest exposure — Li 2010 research shows measurable immune
  effects

NOT: perfume concentrated, deodorant masking, plastic, chemical cleaners,
exhaust fumes, constant sanitized environment, total odor elimination.

**(c) Negative deviations → dissonance**

- **Rotting food, sewage, decay**: evolved disgust response (Rozin
  research) — strong avoidance signal, vagal nausea reaction
- **Chemical pollution**: exhaust, industrial, paint fumes → irritation +
  learned aversion + actual damage
- **Total odor elimination**: sterile hospital, clean-room — evolved
  expectation of ambient smell violated, "feels wrong"
- **Persistent unfamiliar smells**: new environment → low-level baseline
  alert, takes days to habituate
- **Masked body odors chronic**: heavy perfume, deodorant chronic → agent
  olfactory substrate compromised (cannot smell individual identity)
- **Stale indoor air**: CO2 buildup, absence of ventilation → indirect
  signal (fresh air return = reward)
- **Loss of smell** (anosmia, COVID-19 legacy): diffuse dysphoria, food
  less rewarding, environmental connection reduced

**(d) Positive deviations → reward → baseline shift**

- **Flowers, fresh vegetation**: evolved attraction cues, positive
  emotional response reliable
- **Cooking smells**: food reward signal ancestral
- **Clean bodies familial**: familial/group recognition + bonding
- **Specific attractants**: human preferences variable but some common —
  vanilla, citrus, roasted coffee, baking bread
- **Forest smells (phytoncides)**: Li 2010 Shinrin-Yoku research —
  measurable immune boost (NK cell activity tăng), mood improvement
- **Pleasant memory triggered**: Proust effect — smells reliably evoke
  past positive emotional states

**(e) Baseline adaptation examples**

- **Olfactory adaptation FAST**: trong minutes of constant smell exposure,
  perception fades — receptor desensitization mechanism
- **Baseline shift slower**: urban dwellers adapt to traffic fumes as
  "normal" over years, harder to de-adapt
- **Cigarette smokers**: olfactory function declines progressively, adjust
  baseline (and lose ability to perceive own smoke smell)
- **Perfume wearers**: own scent fades from perception quickly, tend to
  over-apply
- **Cultural olfactory norms**: what smells "normal" varies dramatically
  — Vietnamese nước mắm, Scandinavian lutefisk, French aged cheese, Korean
  doenjang. Evolved preferences heavily shaped by cultural exposure.

Asymmetry: olfactory adaptation dominant mechanism (fastest of all senses),
allows survival in varied smell environments but creates long-term baseline
drift that's hard to reverse.

**(f) Research citations**

- 🟢 Buck, L. & Axel, R. (1991). Olfactory receptor gene family — Nobel
  Prize 2004
- 🟢 Li, Q. (2010). Shinrin-Yoku phytoncides immune effects
- 🟢 Herz, R. (2004). Proust effect — odor-memory connection
- 🟢 Rozin, P. Disgust research — olfactory component
- 🟢 Wilson, D.A. & Stevenson, R. (2006). "Learning to Smell: Olfactory
  Perception"
- 🟡 Wedekind, C. et al. (1995). MHC mate preference via smell — replicated
  partially
- 🟡 Human pheromone research mixed quality
- 🟢 Hummel, T. et al. Olfactory testing research — "Sniffin' Sticks"
  methodology

**(g) Phase B case mapping**

- **B46 Proenneke**: rich natural olfactory environment daily — forest
  (phytoncides), water, animals, cooking smells. Validates olfactory
  substrate fed ancestrally.
- **B5 karoshi**: office neutral/air-conditioned environment, no natural
  smells, masked colleague scents, processed food only. Long-term
  olfactory substrate reduced to near-zero natural input.
- **B50 solitary**: sterile cell, minimal olfactory variation, no food
  cooking smells, no natural environment. Sensory deprivation olfactory
  dimension pronounced.
- **B31 ultra-processed food**: engineered food smells (artificial
  flavorings, vanillin concentrated, masking agents) → supernormal
  olfactory stimulus + baseline shift upward (Hall 2019 NIH research
  shows over-eating difference).
- **B9 Blue Zone farmer**: rich olfactory daily — soil, plants, livestock,
  cooking, community smells, seasonal variation.
- **B6 digital nomad**: olfactory variety (new cities each week) BUT
  baseline never establishes — lack of familiar smells that signal "home"
  + safety + belonging. Olfactory novelty ≠ olfactory substrate.
- **DC1 Tesla** hotel late-life: minimal olfactory ancestral feed (urban
  air, processed food, hotel room sterility).
- **DC3 ancestral nomad**: familiar tribal olfactory environment daily
  (same people, same animals, same cooking, same landscape smells) vs
  digital nomad constant olfactory novelty without baseline establishment.

**(h) Individual variation**

- **Genetic variation LARGE**: ~400 olfactory receptor genes, each
  individual has different pseudogene patterns → perceive same molecule
  differently (classic example: androstenone — ~30% don't smell it,
  others find it pleasant or foul)
- **Age**: olfactory function declines with age, early Alzheimer's sign
- **COVID-19 legacy**: post-infection anosmia/parosmia affects baseline
  significantly
- **Hormonal cycling**: women's smell sensitivity varies with menstrual
  cycle (higher during ovulation)
- **Training**: sommeliers, perfumers, flavor experts develop elevated
  detection + discrimination
- **Nasal patency**: chronic congestion, septum deviation → reduced
  olfactory input

Individual variation genetic basis LARGE, cultural shaping substantial,
making "universal" olfactory claims problematic.

### §2.4 Gustation (Lưỡi)

**(a) Body đo gì**

Gustation system đo:
- **5 basic tastes**: sweet, salty, sour, bitter, umami
- **Fat** được establish là 6th taste (Running et al. 2015) — specific
  receptor CD36
- **CO2 detection**: carbonation sensing
- **Temperature + mouthfeel**: texture, viscosity, thermal (crossover với
  tactile + thermoreception)

**Critical distinction**: **taste ≠ flavor**. Flavor = taste + retronasal
olfaction + tactile mouthfeel + thermal. ~80% của "taste" experience
thực ra đến từ olfactory component (giải thích tại sao cảm thấy mất vị
khi nghẹt mũi). Gustation phần ngọt/mặn/chua/đắng/umami là nhỏ hơn
olfaction phần.

Evolved calibration: taste receptors detect biologically meaningful
molecules — sugars (energy), salt (minerals), umami (protein/amino acids),
bitter (potential toxins, evolved caution).

**(b) Ancestral baseline**

Evolved food environment:
- **Seasonal sugar variation**: ripe fruit theo mùa, limited access, no
  refined sugar
- **Limited salt**: animal blood, mineral springs, salt licks — rare and
  biologically critical
- **Bitter compounds common**: nhiều plants có bitter alkaloids, evolved
  caution but gradual acceptance through cultural learning
- **Protein intermittent**: meat when hunt successful, insects, eggs
  occasional
- **Fat relatively rare**: nuts seasonal, animal marrow + fatty meat
  occasional
- **Ancestral diet composition estimates** (Eaton & Konner 1985): ~30-35%
  carbs (mostly complex + fiber), 20-35% protein, 30-40% fat (mostly
  unsaturated + animal)
- **Food neophobia**: evolved caution với unfamiliar tastes (potential
  toxins) + food preference via social learning (Rozin research)
- **Breastmilk as first calibration**: species-specific sweet-fat
  composition, establishes infant baseline

NOT: constant sugar availability, refined salt saturation, ultra-processed
engineered flavors, caloric density 3-5× ancestral, year-round fruit
varieties.

**(c) Negative deviations → dissonance**

- **Bitter toxins**: evolved strong rejection signal (protective) — even
  children reject bitter instinctively
- **Spoiled food**: rejection signals (often olfactory-driven)
- **Nutrient deficiency cravings**: research mixed — salt craving reliable
  during sodium depletion, others less documented
- **Unfamiliar tastes**: neophobia dissonance, takes 8-15 exposures để
  establish preference (Rozin)
- **Over-saturation**: too much salt, sugar, fat at once → palate fatigue
  + nausea + vagal response
- **Blandness prolonged**: baseline-adapted tongues find ancestral whole
  food unpleasant ("tasteless")

**(d) Positive deviations → reward → baseline shift**

- **Sweet**: high-energy signal, evolved strong reward (ancestral = ripe
  fruit = vitamins + calories, rare)
- **Salt**: mineral signal, evolved strong reward (ancestral = rare
  biologically critical)
- **Umami**: protein signal, evolved reward (ancestral = meat, fermented,
  aged foods)
- **Fat**: caloric density signal, evolved reward (ancestral = nuts,
  marrow, fatty meat)
- **All 4 were HIGH VALUE ancestrally** — now engineered to **supernormal
  levels** (Tinbergen principle applied to food — Barrett 2010)
- **Variety/novelty**: novel flavors trigger dopamine reward, cross-
  cultural exploration
- **Social food context**: eating together amplifies food reward

**(e) Baseline adaptation examples** (dramatic trong gustation)

- **High-sugar diet**: baseline shifts upward within days-weeks, normal
  fruit tastes bland, need escalating sweetness
- **Low-sugar diet reversal**: re-sensitization over weeks, natural
  sweetness returns, processed food becomes "too sweet"
- **Salt**: similar dynamics — high-salt processed food → fresh food
  tastes bland, low-salt diet re-sensitizes
- **Umami glutamate**: MSG + similar concentrated umami → baseline shift
  upward
- **Ultra-processed food**: engineered combinations (sugar + fat + salt)
  exceed any natural food → supernormal stimulus → overconsumption
- **Hall 2019 NIH clinical study**: ultra-processed diet vs whole food
  diet, same calories offered, same macros — participants ate **500 more
  kcal/day** on ultra-processed diet, measurable gain. Direct evidence
  of baseline distortion mechanism.

Asymmetry: baseline shift UP fast (days-weeks of processed food exposure),
shift DOWN slower (weeks-months of whole food return).

**(f) Research citations**

- 🟢 Hall, K. et al. (2019). "Ultra-processed diets cause excess calorie
  intake and weight gain" — Cell Metabolism NIH clinical trial
- 🟢 Running, C. et al. (2015). Fat as 6th taste
- 🟢 Eaton, S.B. & Konner, M. (1985). "Paleolithic nutrition: a
  consideration of its nature and current implications" — NEJM
- 🟢 Rozin, P. Food psychology, neophobia, acquired tastes research
  multiple publications
- 🟢 Tinbergen, N. (1951). Supernormal stimulus principle
- 🟢 Barrett, D. (2010). "Supernormal Stimuli" — food chapter
- 🟡 Wrangham, R. (2009). "Catching Fire: How Cooking Made Us Human" —
  cooking hypothesis
- 🟢 Kim, U.K. et al. (2003). PTC/TAS2R38 bitter receptor genetics

**(g) Phase B case mapping**

- **B31 ultra-processed food obsession** — primary case. Supernormal
  stimulus engineered → baseline shift extreme → L1 gustation corruption
  + overconsumption. Hall 2019 directly supports.
- **B48 McCandless**: food scarcity extreme → death from starvation +
  potentially toxic plant consumption (bitter caution failed due to
  desperation)
- **B50 solitary confinement**: food bland, minimal flavor variation →
  gustation deprivation component (though L0 caloric needs met)
- **B5 karoshi**: cafeteria food, convenience processed → baseline
  shifted, nutritional quality compromised long-term
- **B9 Blue Zone diet**: rich whole food — vegetables, legumes, some
  animal, fermented — ancestral-adjacent gustation substrate
- **B46 Proenneke**: self-caught fish, self-grown vegetables, simple
  whole foods → gustation aligned với ancestral baseline
- **B27 Vietnamese craft village**: traditional cuisine preservation =
  ancestral gustation baseline maintained intergenerational
- **B14 extended family**: cooking tradition transmission = multi-
  generational gustation calibration
- **DC3 ancestral nomad**: seasonal wild foods, hunted game, gathered
  plants → varied whole foods; digital nomad = street food international
  but often processed + irregular

**(h) Individual variation**

- **PTC sensitivity** (phenylthiocarbamide, TAS2R38 gene): genetic marker
  → super-tasters ~25%, non-tasters ~25%, medium ~50% — dramatic
  cross-population variation
- **TAS2R bitter receptor variants**: affect vegetable preferences
  (Brussels sprouts, coffee, tonic water, bitter greens)
- **Cultural exposure**: shapes adult tolerance for spicy, fermented,
  bitter, sour foods dramatically
- **Hormonal cycling**: pregnancy shifts preferences (aversions +
  cravings well-documented)
- **Age**: taste receptors decline với age, salt + sweet thresholds
  often elevated
- **Gut microbiome**: increasingly recognized as modulator of food
  preferences via gut-brain axis signaling

Individual variation genetic basis significant, cultural shaping dominant
cho adult preferences.

### §2.5 Tactile-Skin (Da xúc giác)

**(a) Body đo gì**

Skin là **largest sensory organ** của cơ thể, multi-subsystem:

**Thermoreception skin** — hot/cold sensing via TRP channel receptors:
- TRPV1 (heat detection, capsaicin response)
- TRPM8 (cold detection, menthol response)
- Response to ambient temperature + contact temperature

**Mechanoreception** — pressure, texture, vibration:
- **Meissner corpuscles** (light touch, fine texture, flutter)
- **Pacinian corpuscles** (vibration, deep pressure)
- **Merkel cells** (sustained pressure, fine spatial detail)
- **Ruffini endings** (skin stretch)

**Nociception cutaneous** — tissue damage signaling (crossover với §4.2
interoceptive nociception)

**Affective touch (C-tactile afferents)** — **quan trọng nhất cho reframe**:
- **CT fibers**: specialized slow-conducting C-fibers respond optimally
  to slow gentle stroking at skin temperature (~32°C), at ~3-10 cm/s
  velocity (Löken 2009)
- **Direct insula projection** → subjective pleasantness, không phải
  discriminative touch
- **SEPARATE neural pathway từ discriminative mechanoreception** —
  McGlone 2014 research established as distinct system
- Evolved cho **social grooming, infant care, pair bonding**
- Triggers **oxytocin release**
- Found trong hairy skin only (palms + soles KHÔNG có CT fibers —
  evolutionary clue: CT system for social touch, not object
  manipulation)

**Critical insight**: affective touch là **separate input channel** từ
discriminative touch, và chính là cái mà "touch hunger" phenomenon
refers to. Discriminative touch có thể được feed bởi object handling,
nhưng affective touch CHỈ được feed qua social/gentle stroking patterns.

**(b) Ancestral baseline**

- **Weather variation**: daily thermal cycles, seasonal shifts, wind,
  sun, rain — skin thermoreceptors constantly engaged
- **Clothing**: natural fibers (leather, plant fibers, wool) — varied
  textures and weights
- **Frequent social touch**: grooming (parallel primate research —
  grooming is bonding activity), holding infants most of day, carrying
  children, sleeping in contact with family/tribe, physical comforting
- **Ground contact varied**: bare feet hoặc minimal footwear on varied
  terrain
- **Object handling**: tools, food preparation, water, materials — varied
  tactile feedback daily
- **Sleep contact**: co-sleeping ancestral pattern (especially infants +
  children, often adults in cold climates)
- **Close kin proximity**: touch throughout life stages

NOT: constant climate control, synthetic uniform fabric, touch deprivation,
isolated sleep, minimal object handling, primarily screen/keyboard
interaction.

**(c) Negative deviations → dissonance**

- **Cold/heat damage**: nociception + thermoreception extreme (crosses
  into L0 territory at dangerous levels)
- **Itch chronic**: inflammatory, allergic, persistent dissonance input
- **Friction/irritation**: rough fabric, blistering, chafing
- **Social touch absence** = **SKIN HUNGER** phenomenon:
  - Field 2010 research — nursing home residents, preterm infants
    measurably worse without touch (weight gain, developmental delay)
  - **Harlow 1958** monkey studies — cloth mother vs wire mother —
    touch contact more important than feeding cho attachment
  - **Romanian orphanage studies** (Zeanah, Nelson research) — touch
    deprivation causes permanent developmental damage, brain structural
    changes
- **Touch aversion** (opposite — overwhelming touch, trauma, sensory
  processing disorder): also dissonance, different architecture
- **Affective touch absent specifically**: sexual touch without affective
  CT stimulation feels "empty," hugs feel different từ sexual touch,
  massage different từ either — CT system distinct
- **Constant uncomfortable clothing**: tight, synthetic, wrong fit —
  chronic low-level mechanoreception dissonance

**(d) Positive deviations → reward → baseline shift**

- **Warmth in cold**: thermal comfort reward
- **Gentle affective touch (CT activation)**: oxytocin release → bonding
  reward (Löken 2009, McGlone 2014)
- **Massage**: sustained pressure + affective touch compound
- **Body contact sleep**: co-sleeping, cuddling → autonomic regulation,
  vagal tone improvement
- **Silk, cashmere, soft textures**: supernormal mechanoreceptor stimulus
- **Warm bath, sauna**: thermal reward + skin relaxation compound
- **Hugs**: specific evolved social touch pattern, reliable oxytocin
  response
- **Sexual touch**: specific evolved pleasure + bonding mechanism (hormonal
  + CT + affective)

**(e) Baseline adaptation examples**

- **Cold tolerance**: winter exposure shifts baseline (Wim Hof method,
  Finnish sauna culture, Siberian cold adaptation)
- **Silk baseline**: wearing silk long-term → cotton feels rough khi
  switch
- **Climate control chronic**: AC year-round → temperature sensitivity
  elevated, both heat and cold tolerance reduced
- **Rough fabric baseline**: hemp shirts, burlap, work clothes → become
  comfortable với exposure over weeks
- **Touch-deprived individuals**: sometimes adapt to absence partially
  but not fully — often become touch-seeking hoặc touch-averse when
  re-exposed (paradoxical)
- **Skin-to-skin infant contact**: shapes adult touch baseline partially
  (research suggests, not fully established)

**(f) Research citations**

- 🟢 Field, T. (2010, 2014). Touch research — therapy effects, infant
  development, "Touch" book
- 🟢 Löken, L. et al. (2009). "Coding of pleasant touch by unmyelinated
  afferents in humans" — Nature Neuroscience CT fiber foundational
- 🟢 McGlone, F. et al. (2014). "Discriminative and affective touch:
  sensing and feeling" — Neuron review
- 🟢 Harlow, H. (1958). "The nature of love" — monkey surrogate mother
- 🟢 Zeanah, C. & Nelson, C. Bucharest Early Intervention Project —
  Romanian orphanage studies
- 🟢 Morrison, I. et al. C-tactile social touch research
- 🟢 Hertenstein, M. et al. (2009). Touch communicates distinct emotions
- 🟢 Olausson, H. et al. (2002). CT-fiber loss patient research — "GL
  patient" case study
- 🟢 Carter, C.S. Oxytocin-bonding research
- 🟡 Montagu, A. (1971). "Touching: The Human Significance of the Skin"
  — foundational theoretical work

**(g) Phase B case mapping**

- **B19 touch hunger/skin contact extreme** — primary case. Direct evidence
  of touch as body-input với measurable deprivation effects. Validates
  affective touch (CT fiber activation) as distinct input category.
- **B13 love addict**: limerence phase = touch over-feed compound với
  novelty + hormonal → baseline shifts dramatically → "crash" when access
  lost. Classic supernormal stimulus pattern on CT + oxytocin system.
- **B50 solitary confinement**: touch deprivation prolonged → measurable
  psychological damage (Grassian 2006 review). Multi-dimensional touch
  starvation.
- **B46 Proenneke** (30 năm Alaska solo): touch từ environment (tools,
  water, wood, clothing) rich; social affective touch absent → **partial
  touch substrate fed, not total**. Survived decades với mechanoreception
  fed from object interaction, CT system starved but not crashed.
- **B12 parentified child**: role-reversed touch — child giving rather
  than receiving comfort → specific touch deprivation pattern (give but
  don't receive CT activation)
- **B11 codependent**: touch present but với anxiety/control pattern,
  not affective free touch → CT activation compromised by threat system
  co-activation
- **Romanian orphanage literature**: foundational evidence touch
  deprivation causes permanent developmental damage — referenced broadly
  trong developmental body-base research
- **DC1 Tesla** late-life: social affective touch absent, parasocial
  với pigeons không activate human CT system adequately (pigeon touch
  ≠ human gentle stroking)
- **DC3 ancestral nomad**: daily contact với tribe members, co-sleep,
  grooming — rich CT substrate; digital nomad often isolated sleeping,
  minimal social touch, massage/sex only when paid or partnered

**(h) Individual variation**

- **SPS sensitivity**: high SPS individuals more sensitive to tactile
  stimulation, seek softness + avoid rough
- **Autism spectrum**: varied touch preferences, often hypersensitive
  hoặc hyposensitive → touch baseline different from neurotypical
- **Trauma history**: touch aversion vs touch seeking vary dramatically
  với abuse history
- **Cultural touch norms**: high-touch cultures (Mediterranean, Latin,
  Middle East) vs low-touch (Nordic, East Asian) — dramatic cross-
  cultural variation trong casual touch frequency
- **Age**: elderly often touch-deprived, particular need documented trong
  nursing home research
- **Attachment style**: secure vs insecure attachment affects adult
  touch comfort + seeking patterns
- **Gender**: women generally receive more casual touch trong most cultures,
  men report more touch deprivation

Individual variation substantial, cultural shaping dominant cho
non-intimate touch norms, developmental history foundational.

---

**§2 EXTEROCEPTIVE INPUTS — section complete**

5 exteroceptive inputs enumerated (vision, audition, olfaction,
gustation, tactile skin). Each với 8-field schema. Key findings cho
reframe from §2:

1. **Vision, audition, tactile** đều là **compound aggregates** (vision
   = photons + fractals + bio motion + faces + circadian; tactile =
   thermoreception + mechanoreception + nociception + CT affective).
   Không có single "vision channel" primitive.

2. **Affective touch (CT fibers)** validates reframe approach: explicitly
   documented là separate pathway from discriminative touch, directly
   feeds oxytocin/bonding system. Example của sub-input level analysis
   that "touch channel" obscures.

3. **Baseline adaptation** documented across all 5 inputs với research
   evidence: olfactory fastest (minutes), visual moderate (weeks-months),
   gustation dramatic (days-weeks with strong evidence từ Hall 2019
   NIH), auditory substantial, tactile slower but real.

4. **Supernormal stimulus** documented across all 5: engineered visual
   beauty (Instagram/HD), engineered music, concentrated olfactory
   (perfumes), ultra-processed food, silk/texture. Each confirms
   baseline shifting mechanism.

5. **Individual variation LARGE** across all 5, với genetic basis
   significant (olfactory receptor pseudogenes, TAS2R bitter, SPS,
   color vision variants). Supports §13.3 Example finding về
   variation at substrate level.

Reframe §2 assessment: **exteroception enumeration PASSES test criteria
§1.4.1(1)** — complete enumeration với baseline mechanism, supported
by research across all 5 categories.

---

## §3 — PROPRIOCEPTIVE INPUTS

### §3.1 Proprioception (Vị trí cơ thể)

**(a) Body đo gì**

Proprioception = "sixth sense" per Sherrington (1906) — khả năng biết
vị trí và trạng thái của cơ thể **không cần nhìn**:

- **Muscle spindles**: detect muscle length + rate of change (intrafusal
  fibers trong mỗi skeletal muscle)
- **Golgi tendon organs**: detect muscle tension tại tendon-muscle junction
- **Joint receptors**: detect joint angle + pressure (Ruffini + Pacinian
  endings trong joint capsules)
- **Skin mechanoreceptors**: augment proprioception qua stretch signals
- **Efference copy**: motor cortex sends copy của motor commands to
  proprioceptive integration — predicts what position should be, compared
  với actual feedback

Integrates vào **body schema** — ongoing unconscious model của limb
positions. Input liên tục vào **cerebellum + somatosensory cortex**.

**(b) Ancestral baseline**

- **Varied postures throughout day**: squatting, sitting trên ground,
  kneeling, walking, climbing, carrying, lying different positions
- **Ground-level living**: squatting instead of chair sitting, sleeping
  on ground, cooking at ground level
- **Weight bearing varied**: carrying infants, water, tools, game animals
- **Balance challenges regular**: uneven terrain, climbing, river crossing,
  tree climbing
- **No prolonged single posture**: activities rotate throughout day,
  muscle groups alternate
- **Rich proprioceptive variety**: crawling, bending, reaching, stretching
  integrated into daily survival activities

NOT: 8+ hours same chair position, minimal weight bearing, predictable
flat surfaces, prolonged screen-neck posture.

**(c) Negative deviations → dissonance**

- **Prolonged static posture** (sedentary desk work): mỏi cơ, stiffness,
  proprioceptive "drift" — position sense degrades
- **Single-position dominance**: same chair, same desk height, same
  viewing angle → muscle imbalance, chronic tension
- **Low weight bearing**: muscles atrophy, proprioceptive precision
  declines
- **Neck flexion chronic** (phone/laptop): cervical proprioceptive
  disruption, "tech neck"
- **Lower back chronic tension**: sedentary + weak core → ongoing
  dissonance
- **Loss of varied movement**: proprioceptive variety collapses →
  "không biết body mình ở đâu"
- **Floor/ground contact absent** (always furniture): proprioceptive
  patterns evolved for ground-level activities atrophy

**(d) Positive deviations → reward → baseline shift**

- **Flow state trong physical activity**: dance, martial arts, sport,
  climbing → "in the body" feeling, proprioceptive integration peak
- **Varied movement patterns**: yoga, calisthenics, functional training
- **Weight-bearing exertion**: carrying, lifting → proprioceptive
  feedback rich
- **Balance challenges**: surfing, skateboarding, slackline → heightened
  proprioceptive precision
- **Skilled craft work**: fine motor + gross motor integration (pottery,
  woodworking, instrument playing) — combined proprioception + tactile
  + vision flow
- **Body awareness practices**: Feldenkrais, Alexander Technique,
  meditation with body scan

**(e) Baseline adaptation examples**

- **Sedentary baseline**: chronic desk workers adapt to limited movement,
  re-engagement painful initially, proprioceptive precision reduced
- **Athletic training**: shifts proprioceptive baseline upward, finer
  precision develops
- **Dancer/martial artist**: extremely refined proprioceptive baseline
- **Injury + recovery**: proprioceptive retraining after joint injuries
  (ACL, shoulder) documented trong physical therapy
- **Age**: proprioception declines với age → falls increase, balance
  retraining programs established
- **Yoga practitioners**: measurable proprioceptive acuity improvement

**(f) Research citations**

- 🟢 Sherrington, C. (1906). "The Integrative Action of the Nervous
  System" — proprioception foundational
- 🟢 Proske, U. & Gandevia, S. (2012). "The proprioceptive senses"
  review — Physiological Reviews
- 🟢 Tuthill, J. & Azim, E. (2018). Proprioception review — Current
  Biology
- 🟢 Damasio, A. Embodied cognition + body schema research
- 🟢 Craig, A.D. (2003). Body map processing
- 🟡 Vaynman, S. & Gomez-Pinilla, F. Exercise + BDNF + cognition research

**(g) Phase B case mapping**

- **B5 karoshi**: sedentary office 12+ hours daily → proprioceptive
  substrate starved, chronic posture dissonance, "tech neck"
- **B9 Blue Zone farmer**: daily physical labor varied → ancestral-
  adjacent proprioceptive substrate fed
- **B46 Proenneke**: cabin building, chopping wood, hunting, fishing —
  varied proprioceptive daily
- **B50 solitary**: restricted physical space, limited movement variety
  → proprioceptive deprivation
- **B1 workaholic burnout**: sedentary + stress → proprioceptive neglect
  component of burnout pattern
- **B10 ultra-marathon**: proprioceptive over-feed, extreme variety,
  risk of RSI + overuse
- **B28 chess master**: sedentary mental work — paradox of high cognitive
  engagement với minimal proprioceptive input
- **B27 Vietnamese craftsman**: refined hand-eye + proprioception trong
  craft work — ancestral-adjacent substrate
- **DC3 ancestral nomad**: varied daily physical activities với community;
  digital nomad = varied locations but similar sedentary laptop work
  across all of them

**(h) Individual variation**

- **Athletic training history**: baseline shifted by sport/dance/martial
  arts exposure
- **Age**: declines naturally, accelerated by disuse
- **Injury history**: ACL tear, shoulder dislocation, etc. can permanently
  alter proprioceptive precision in affected joint
- **Ehlers-Danlos Syndrome**: connective tissue disorder → proprioception
  often compromised
- **Congenital conditions**: rare proprioceptive loss patients (like
  Ian Waterman case — lost proprioception, had to consciously guide
  every movement)
- **Occupational**: fine motor workers (surgeons, musicians, craftsmen)
  have elevated baseline

Variation via training significant, age-related decline universal.

### §3.2 Vestibular (Cân bằng)

**(a) Body đo gì**

Vestibular system, trong inner ear, đo:
- **Head orientation**: otolith organs (utricle + saccule) detect linear
  acceleration + gravity vector
- **Rotational acceleration**: 3 semicircular canals detect rotation
  around 3 axes (yaw, pitch, roll)
- **Integration với vision**: vestibulo-ocular reflex (VOR) stabilizes
  gaze during head movement — critical for clear vision while walking
- **Integration với proprioception**: vestibular signals combined với
  proprioceptive to form unified body-in-space sense
- **Gravity baseline**: continuous 1G reference, evolved for Earth's
  gravitational environment

Processing qua vestibular nuclei → cerebellum + cortex. Affects balance,
spatial orientation, motion sickness detection.

**(b) Ancestral baseline**

- **Varied motion daily**: walking (most common), running (chase, flee),
  climbing, carrying children (rocking motion), jumping, swimming,
  dancing
- **Terrain variation**: uneven ground challenges vestibular regularly
- **Upright biped challenges**: human walking itself is vestibular-intensive
- **Rocking**: babies rocked, people sway to music, rhythmic movement
  inherent
- **No prolonged stillness**: daily life has ongoing motion integration
- **No artificial acceleration**: evolved for walking-speed motion
  primarily, occasional running

NOT: prolonged sitting (minimal head movement), car travel (passive high
acceleration), flying, rollercoasters, VR headsets, motion simulators.

**(c) Negative deviations → dissonance**

- **Prolonged stasis** (bedrest, sedentary office): vestibular "atrophy",
  motion sickness upon re-engagement, balance reduced
- **Passive high acceleration**: car, airplane, ship → motion sickness
  (vestibular signals conflict với visual stability cues)
- **Simulator sickness**: VR, cinema large screen → visual motion without
  vestibular confirmation → nausea
- **Vertigo**: BPPV (benign paroxysmal positional vertigo), vestibular
  neuritis → extreme dissonance, disorientation
- **Aging vestibular decline**: falls increase dramatically with
  vestibular function loss
- **Static + low proprioceptive** compound: modern office work → mild
  chronic vestibular deficit

**(d) Positive deviations → reward → baseline shift**

- **Flying, gliding**: evolved to detect unusual motion as high novelty
  signal
- **Swinging** (playground, hammocks): rhythmic acceleration reward —
  children universally love
- **Diving, climbing**: vestibular complexity reward
- **Extreme sports**: surfing, skateboarding, skiing, base jumping,
  paragliding → supernormal vestibular stimulation
- **Dance**: complex vestibular patterns coupled với rhythm → social
  reward compound
- **Rocking soothes**: evolved infant calming mechanism, persists into
  adulthood (rocking chairs, hammocks)

**(e) Baseline adaptation examples**

- **Sailors develop "sea legs"**: vestibular adapts to boat motion over
  days, then "land sickness" after return (baseline shifted)
- **Astronauts zero-G**: dramatic vestibular reorganization, symptoms
  upon return to Earth
- **Figure skaters, ballerinas**: trained vestibular tolerance cho rapid
  spins
- **Motion sickness**: improves với exposure (gradual desensitization)
- **VR users**: adapt partially to simulator environment, but not
  completely

**(f) Research citations**

- 🟢 Fitzpatrick, R. & Day, B. Vestibular research
- 🟢 Brandt, T. & Dieterich, M. Vestibular cortex research
- 🟢 Angelaki, D. & Cullen, K. (2008). Vestibular system neuroscience
- 🟢 Guedry, F. Motion sickness research
- 🟡 Reason, J. (1978). Sensory conflict theory of motion sickness

**(g) Phase B case mapping**

- **B7 extreme sports**: supernormal vestibular stimulation (base jumping,
  BASE, extreme skiing) → direct case of vestibular as reward channel
  engineered to extreme
- **B10 ultra-marathon**: sustained rhythmic vestibular + cardiovascular
  + kinesthetic compound — endorphin + flow
- **B50 solitary**: static confinement → vestibular substrate minimal,
  compounds with proprioceptive deprivation
- **B5 karoshi**: sedentary office → vestibular deficit chronic
- **B46 Proenneke**: natural terrain walking, hunting, fishing — varied
  vestibular daily
- **B9 Blue Zone**: daily varied physical work → vestibular adequate
- **DC1 Tesla** late-life: hotel room sedentary → vestibular minimal
  feed
- **DC3 ancestral nomad**: walking between locations, carrying children,
  riding animals → rich vestibular; digital nomad = primarily sitting
  in airplanes/cafes với occasional tourism

**(h) Individual variation**

- **Motion sickness susceptibility**: genetic + developmental factors,
  women generally more susceptible
- **Vestibular migraine**: affects ~1% population, chronic vestibular
  dysfunction
- **Age**: declines progressively, major fall risk factor elderly
- **Inner ear pathology**: Meniere's disease, vestibular neuritis →
  permanent altered baseline
- **Athletic training**: dancers, gymnasts, pilots have dramatically
  elevated baseline tolerance

### §3.3 Kinesthetic (Vận động cơ bắp)

**(a) Body đo gì**

Kinesthetic input = **dynamic muscle activity sensing**, distinct từ
proprioception (vị trí) vì focus vào **chuyển động + exertion**:

- **Muscle tension dynamics**: contraction/relaxation, force production
- **Muscle stretch**: length changes over time
- **Metabolic signals**: lactate accumulation (fatigue), adenosine
  (energy depletion), pH changes
  - **Respiratory coupling**: exertion drives breath rate, heart rate
  - **Effort sense**: subjective sense of "how hard I'm working"
  - **Recovery signals**: post-exertion relaxation, muscle repair signaling
  - **BDNF (brain-derived neurotrophic factor)** release during exercise —
    couples kinesthetic to cognitive effects

    Distinct từ proprioception vì proprioception focuses on **position** (static
    state), kinesthetic on **dynamics** (rate of change, effort, metabolic
    state).

    **(b) Ancestral baseline**

    Hunter-gatherer activity levels extensively studied:
    - **Walking 8-15 km/day** common (Hadza, !Kung, etc. — Pontzer research)
    - **Varied intensity**: walking steady + occasional running (hunting,
      fleeing) + sustained exertion (carrying, building)
      - **Labor varied**: digging, climbing, lifting, carrying children,
        gathering, construction
        - **Recovery cycles**: hard exertion followed by rest + social time
        - **Dance**: rhythmic kinesthetic + social universal across cultures
        - **Craft activity**: fine + gross motor compound
        - **Play**: children continuous movement, adults less but present

        NOT: 8+ hours sedentary, one brief gym session (evening warrior pattern),
        zero weight bearing all day, chronic under-use.

        **(c) Negative deviations → dissonance**

        - **Sedentary chronic**: chronic muscle under-use → atrophy, restlessness,
          mood dysregulation, "sitting is the new smoking" (Mayo Clinic research)
          - **Restless legs syndrome**: extreme kinesthetic deficit signaling
          - **Chronic pain from disuse**: weak core → back pain, weak legs → knee
            pain compound
            - **Exercise withdrawal**: regular exercisers skipping sessions → mood
              decline, irritability, sleep disturbance
              - **Mood dysregulation**: exercise as established antidepressant effect
                reverses when absent
                - **Over-exertion without recovery**: chronic kinesthetic over-feed
                  without recovery → overtraining syndrome, testosterone collapse,
                    fatigue, immunosuppression

                    **(d) Positive deviations → reward → baseline shift**

                    - **Exercise endorphins**: runner's high (endocannabinoid research updated
                      this from pure endorphin — Fuss 2015)
                      - **Flow state trong physical activity**: mastery + effort + challenge
                        balance
                        - **Exertion recovery cycle**: hard effort then rest reward — parasympathetic
                          rebound
                          - **Mastery of difficult movement**: climbing a hard route, executing
                            a perfect skill
                            - **BDNF surge**: exercise-induced BDNF couples kinesthetic to cognitive
                              reward
                              - **Muscular development**: visible strength progress reward
                              - **Group exertion**: running với friends, team sports, dance — social
                                reward compound

                                **(e) Baseline adaptation examples**

                                - **Couch potato → gym goer shift**: muscles respond within weeks,
                                  baseline kinesthetic tolerance shifts
                                  - **Retired athlete decline**: baseline drops fast without maintenance
                                  - **Fitness improves mood**: general established effect, suggests baseline
                                    kinesthetic substrate fed
                                    - **Ultra-endurance athletes**: extreme baseline shift, "normal" effort
                                      levels feel under-stimulating
                                      - **Manual labor workers**: elevated baseline, transitioning to sedentary
                                        work often produces mood decline

                                        **(f) Research citations**

                                        - 🟢 Ratey, J. (2008). "Spark: The Revolutionary New Science of Exercise
                                          and the Brain" — BDNF + mood + cognition
                                          - 🟢 Blumenthal, J. Exercise as antidepressant clinical trials
                                          - 🟢 Dishman, R. Exercise neuroscience
                                          - 🟢 Pontzer, H. Hunter-gatherer energy expenditure research
                                          - 🟢 Mayo Clinic. Sedentary behavior mortality research
                                          - 🟢 Fuss, J. et al. (2015). Runner's high via endocannabinoid (not just
                                            endorphin) — updated mechanism
                                            - 🟢 Vaynman, S. & Gomez-Pinilla, F. BDNF exercise research

                                            **(g) Phase B case mapping**

                                            - **B9 Blue Zone farmer**: daily physical labor 8-12+ hours → ancestral-
                                              adjacent kinesthetic substrate fed, longevity correlation
                                              - **B5 karoshi**: sedentary 12-16 hours workday → kinesthetic substrate
                                                starved, compounds other channels into burnout
                                                - **B10 ultra-marathon**: kinesthetic over-feed, engineered extreme →
                                                  tests upper limit of channel
                                                  - **B1 workaholic burnout**: sedentary + stress → kinesthetic neglect
                                                    component
                                                    - **B46 Proenneke**: chopping wood, hunting, fishing, cabin maintenance
                                                      → rich daily kinesthetic feed
                                                      - **B47 prison cases** (Knight or prison structure cases): often forced
                                                        sedentary, kinesthetic restricted → compound với other deprivations
                                                        - **B28 chess master**: sedentary high cognitive → paradox of intensive
                                                          mental work với minimal physical
                                                          - **B27 craftsman**: fine + gross motor compound, kinesthetic fed through
                                                            craft
                                                            - **DC1 Tesla**: late-life sedentary lab/hotel → kinesthetic minimal feed
                                                            - **DC3 ancestral nomad**: walking long distances + daily labor + dance
                                                              ceremonies; digital nomad = typically low kinesthetic (sitting laptop)

                                                              **(h) Individual variation**

                                                              - **Physical baseline** wildly variable — genetic VO2max, muscle fiber
                                                                type ratios
                                                                - **Age**: muscle mass declines với sarcopenia, kinesthetic tolerance
                                                                  reduces
                                                                  - **Injury history**: affects specific movement patterns chronically
                                                                  - **Chronic illness**: CFS, fibromyalgia affect exertion capacity
                                                                    dramatically
                                                                    - **Training state**: untrained vs highly trained individuals have
                                                                      different baseline at same chronological age
                                                                      - **Occupational**: manual laborers vs office workers maintain different
                                                                        baselines throughout life

                                                                        ---

                                                                        **§3 PROPRIOCEPTIVE INPUTS — section complete**

                                                                        3 proprioceptive inputs enumerated. Key findings cho reframe từ §3:

                                                                        1. **Three categories distinct in mechanism**: proprioception (position),
                                                                           vestibular (head orientation/acceleration), kinesthetic (muscle
                                                                              dynamics + metabolic). Each với own receptors + neural pathways.

                                                                              2. **"Movement channel" trong current framework reduces cleanly** to
                                                                                 proprioceptive + vestibular + kinesthetic compound. B9 Blue Zone
                                                                                    "daily movement" = all 3 fed simultaneously; B5 karoshi "sedentary"
                                                                                       = all 3 starved simultaneously. Movement không phải primitive —
                                                                                          aggregate of 3 proprioceptive sub-inputs.

                                                                                          3. **Baseline adaptation documented** trong all 3 với exercise/training
                                                                                             research.

                                                                                             4. **Supernormal stimulus** applies (B7 extreme sports, B10 ultra-
                                                                                                marathon) — validates reframe across proprioceptive category.

                                                                                                5. **Ancestral baseline very specific**: 8-15 km/day walking, varied
                                                                                                   postures, weight bearing, recovery cycles — well-documented, provides
                                                                                                      concrete reference cho "what body expects."

                                                                                                      Reframe §3 assessment: **proprioception enumeration PASSES test
                                                                                                      criteria §1.4.1(1)** cho proprioceptive category.

---

## §4 — INTEROCEPTIVE INPUTS

> **Section note**: interoception = body reading its own internal
> state. Critical category because most "slow-decay channel" crashes
> in Phase B cases occur through interoceptive dissonance that body
> cannot clearly verbalize (Bird & Cook alexithymia parallel).

### §4.1 Thermoreception core (Nhiệt độ cơ thể)

**(a) Body đo gì**

Distinct từ skin thermoreception §2.5. Core temp regulation là **interoceptive**
— body reading its own internal temperature state:

- **Hypothalamic preoptic area** — core temp set point ~37°C
- **Core vs skin distinction**: skin có thể deviate đáng kể trong khi
  core vẫn được maintained — active regulation task
- **Peripheral thermoreceptors** feed vào core regulation (§2.5 crossover)
- **Behavioral thermoregulation**: seek shade, shiver (trước khi cold-damage),
  sweat, thirst for water, adjust clothing
- **Cardiovascular coupling**: vasodilation cho cooling, vasoconstriction
  cho warming
- **Metabolic coupling**: brown adipose tissue heat production, thyroid
  baseline

**(b) Ancestral baseline**

- **Diurnal variation** ~0.5°C (thấp nhất sáng sớm, cao nhất chiều)
- **Seasonal shifts** nhẹ
- **Core maintained tight range** 36.5-37.5°C normal
- **Behavioral thermoregulation primary**: clothing, shelter, fire, water
- **Periodic challenges**: cold nights, hot midday, fever từ illness
- **Fasting states** affect baseline slightly (lower in deep fasting)

**(c) Negative deviations → dissonance**

- **Hyperthermia** (>39°C sustained): L1 strong dissonance → L0 territory
  (heat stroke >40°C fatal)
- **Hypothermia** (<35°C sustained): L1 → L0 territory
- **Chronic climate control** (constant AC/heating): thermal adaptive
  response atrophies, tolerance narrows
- **Fever**: active L1 signal của infection — body intentionally raises
  set point
- **Hot flashes** (menopause): disruption signal from hormonal cause
- **Cold intolerance** elderly/frail: baseline drift + less regulatory
  capacity

**(d) Positive deviations → reward → baseline shift**

- **Warmth in cold** (fire, sauna, hot bath): evolved reward strong
- **Cooling in heat** (shade, water plunge, breeze): evolved reward
- **Contrast therapy** (cold plunge + sauna): supernormal variant,
  dopaminergic + endorphin compound
- **First warm coffee on cold morning**: familiar thermal reward pattern
- **Brown adipose tissue activation**: via cold exposure → metabolic +
  mood effects (van Marken Lichtenbelt research)

**(e) Baseline adaptation examples**

- **Cold adaptation documented**: Wim Hof method (Kox et al. 2014 showed
  voluntary autonomic modulation), Finnish sauna culture, winter swimming
  communities, Siberian/Inuit populations
- **Heat adaptation**: desert dwellers, athletes training in heat, sauna
  practitioners
- **Climate-controlled populations**: progressively lose thermal tolerance
  over years — narrow comfort range dramatically
- **Transition difficulties**: moving between climate zones takes
  weeks-months of acclimation

**(f) Research citations**

- 🟢 Satinoff, E. Thermoregulation research foundational
- 🟢 Morrison, S.F. Central thermoregulation neuroscience
- 🟢 Romanovsky, A. Thermoregulation review
- 🟢 van Marken Lichtenbelt, W. Brown adipose tissue cold exposure
- 🟢 Kox, M. et al. (2014). Wim Hof method autonomic control study
- 🟡 Huttunen, P. Finnish sauna research

**(g) Phase B case mapping**

- **B5 karoshi**: constant AC office → thermal adaptive response atrophy,
  narrow comfort range
- **B46 Proenneke**: Alaska extreme cold, adapted over 30 năm — extreme
  baseline shift possible
- **B45 Onoda** 29 năm jungle: tropical heat adaptation
- **B48 McCandless**: hypothermia contributed to death state
- **B50 solitary**: controlled temperature, thermal variation minimal →
  adaptive capacity atrophy
- **DC3 ancestral nomad**: daily thermal variation (sun exposure,
  night cooling, seasonal shifts); digital nomad = typically climate-
  controlled hotels/cafes

**(h) Individual variation**

- **Menopause, thyroid disorders, autonomic disorders**: dramatic baseline
  shifts
- **Cold tolerance genetic variation**: brown adipose tissue activation
  ability differs
- **Age**: thermoregulation capacity declines, elderly more vulnerable
  hot/cold extremes
- **Hormonal cycling**: women's baseline shifts ~0.3°C with ovulation
- **Fitness state**: affects thermoregulation during exertion

### §4.2 Nociception (Đau)

**(a) Body đo gì**

Pain system distinct từ discriminative tactile (§2.5) trong multiple
dimensions:

- **A-delta fibers**: fast, thin myelinated (~20 m/s) → "first pain"
  sharp, localized, protective reflex trigger
- **C-fibers**: slow, unmyelinated (~1 m/s) → "second pain" burning,
  diffuse, longer-lasting
- **Specific receptors**: TRPV1 (heat, capsaicin), TRPA1 (noxious cold,
  chemicals), acid-sensing ion channels, mechanical nociceptors
- **Chemical signaling**: substance P (nociceptive neurotransmitter),
  prostaglandins (inflammation), bradykinin (tissue damage)
- **Gate control** (Melzack & Wall 1965): spinal dorsal horn modulates
  nociceptive signals — explains tại sao rubbing injury giúp reduce pain,
  tại sao distraction works
- **Dual dimension**: sensory-discriminative (where, how intense) via
  somatosensory cortex + affective-motivational (how bad it feels) via
  anterior cingulate cortex (ACC)
- **Descending modulation**: endogenous opioid + serotonergic + noradrenergic
  pathways từ brainstem có thể suppress nociception (stress-induced analgesia,
  placebo effect)

**(b) Ancestral baseline**

- **Occasional pain**: injuries (cuts, bruises, fractures), illness,
  childbirth, menstruation, dental problems, parasites
- **Chronic pain less common**: modern epidemic proportions không ancestral
  norm
- **Recovery expected**: most pain resolved, không chronic
- **Social context**: communal care for injured, pain expression
  communicates need
- **Evolutionary role**: warning system for damage — mistakes here (missed
  pain) = death, hence high-intensity signal

**(c) Negative deviations → dissonance (full spectrum)**

Maps directly to Body-Dissonance.md §2 spectrum từ nhẹ đến emergency:
- **Nhẹ**: đau đầu, mỏi cơ, đau nhẹ
- **Trung**: đau rõ, cần attention
- **Mạnh**: gãy xương, bỏng, đau bụng cấp → suppress most activities
- **Cực**: đau cực độ → shock, body-wide shutdown, suppress everything
- **Chronic pain**: maladaptive persistent nociception → baseline
  shifted, central sensitization
- **Allodynia**: non-painful stimuli become painful (wind on skin hurts)
- **Hyperalgesia**: mild pain becomes severe
- **Phantom limb**: nociception signal without tissue damage (brain
  map persistence)
- **CIPA** (Congenital Insensitivity to Pain with Anhidrosis, SCN9A
  mutation): **LETHAL CONDITION** — patients die young từ unnoticed
  injuries → direct proof pain is necessary, không phải "optional"

**(d) "Positive" deviations — controlled pain contexts**

Nociception unique vì có những contexts engineered để reward từ pain:

- **Pain-ritual** (B18 body modification): controlled pain triggers
  endorphin + endocannabinoid release, combined với ritual meaning →
  reward compound
- **Exercise burn** (lactic acid accumulation): mild nociception coupled
  với kinesthetic flow reward
- **Spicy food** (TRPV1 activation): cultural reward từ mild nociception
  — chili peppers universally adopted
- **BDSM contexts**: controlled pain + safety + bonding → specific reward
  compound
- **Childbirth**: pain với strong meaning context → tolerable for many
  (though epidural demand suggests không all)
- **Tattooing**: controlled pain + permanence + identity → ritual compound

Pattern: pain alone = dissonance. Pain + control + meaning context =
sometimes reward. **Context-dependent interpretation** rare trong body-
inputs.

**(e) Baseline adaptation**

- **Chronic pain sensitization**: central nervous system amplifies pain
  over time trong some patients (fibromyalgia, neuropathic pain)
- **Chronic pain desensitization**: some patients adapt, pain tolerance
  increases
- **Pain threshold varies với mood, context, attention**: anxiety amplifies,
  distraction reduces, meaning shapes
- **Placebo/nocebo effects dramatic**: expectation significantly shapes
  actual pain experience (Bingel research)
- **Meditation training**: documented pain modulation through attention
  restructuring (Zeidan research)

**(f) Research citations**

- 🟢 Melzack, R. & Wall, P. (1965). Gate control theory — Science paper
  foundational
- 🟢 Wall, P. (2000). "Pain: The Science of Suffering" book
- 🟢 Melzack, R. (1999). Neuromatrix theory of pain
- 🟢 Woolf, C. Central sensitization research
- 🟢 Cox, J.J. et al. (2006). SCN9A CIPA genetic research
- 🟢 Bingel, U. et al. Placebo/nocebo neuroscience
- 🟢 Zeidan, F. Meditation + pain fMRI research
- 🟢 Basbaum, A. et al. (2009). "Cellular and molecular mechanisms of
  pain" review

**(g) Phase B case mapping**

- **B18 body modification / pain ritual**: primary case of "positive pain"
  context. Intentional nociception + ritual meaning → endorphin + bonding
  compound. Tests limits của reframe — how nociception becomes reward via
  context.
- **B7 extreme sports**: pain tolerance elevated, meaning context, crashes
  possible
- **B10 ultra-marathon**: sustained nociception managed via flow state +
  endorphin + meaning
- **B46 Proenneke**: occasional injury pain, self-treated, ancestral
  pattern
- **B50 solitary**: physical confinement pain, chronic back issues common
- **Chronic pain in modern populations generally**: major framework concern,
  points to modern mismatch (chronic stress, sedentary, inflammation diet,
  reduced recovery)
- **B48 McCandless**: terminal illness pain, không treated

**(h) Individual variation**

- **SCN9A variants**: pain sensitivity spectrum (từ CIPA complete
  insensitivity đến extreme erythromelalgia sensitivity)
- **Fibromyalgia, CFS, central sensitization syndromes**: chronic
  amplified nociception
- **Cultural pain norms**: childbirth expression, dental procedures,
  stoicism norms variable
- **Gender differences**: women generally report higher pain sensitivity
  (research consistent)
- **Pain catastrophizing**: cognitive style affecting subjective experience
- **Attachment style** affects pain response
- **Genetic opioid receptor variants**: OPRM1 variants affect pain +
  reward response

### §4.3 Respiratory (Thở)

**(a) Body đo gì**

Respiratory sensing + control system:
- **Breath rate**: respiratory rate ~12-20/min resting adult, shifts
  với activity và state
- **Depth**: tidal volume, diaphragmatic vs thoracic pattern
- **CO2 chemoreception**: **PRIMARY trigger** to breathe — carotid bodies
  + aortic bodies + central chemoreceptors trong medulla. O2 levels
  secondary trigger (chỉ khi severely low)
- **Nasal vs mouth breathing**: nose preferred evolutionarily (filters,
  humidifies, produces nitric oxide)
- **Effort sense** (dyspnea): subjective "air hunger" — complex integration
  của CO2 + respiratory muscle effort + lung stretch
- **Vagus nerve integration**: breath directly affects parasympathetic
  tone via **respiratory sinus arrhythmia (RSA)** — Porges polyvagal
  theory
- **Diaphragmatic movement** signals visceral massaging, autonomic
  modulation

Breathing unique vì **voluntary + involuntary**: conscious control possible
+ automatic baseline. Bridge between conscious và autonomic nervous
systems.

**(b) Ancestral baseline**

- **Nasal breathing primarily** (anthropological skull evidence — Nestor
  2020 reviews)
- **Diaphragmatic breathing resting** — chest breathing emerged as modern
  pattern
- **Air quality varied but generally cleaner** than modern urban
- **Breath hold capacity** developed via aquatic activities, carrying
  loads
- **Breath work integrated** trong cultural practices: singing, chanting,
  labor grunts, meditation traditions
- **Periodic exertion recovery** cycles

NOT: chronic shallow chest breathing, mouth breathing chronic, polluted
air, sleep apnea, anxiety hyperventilation.

**(c) Negative deviations → dissonance**

- **Suffocation**: L0 immediate (minutes to brain damage)
- **Asthma**: chronic restriction, bronchoconstriction, dissonance
  acute và chronic
- **Panic hyperventilation**: over-breathing → CO2 drops → respiratory
  alkalosis → dizzy, tingling, more panic → positive feedback loop
- **Shallow chronic breathing**: anxiety feedback loop — shallow breath
  → sympathetic activation → more anxiety
- **Mouth breathing chronic**: especially sleep → sleep apnea, dental
  issues, dry airway, less nitric oxide
- **Poor air quality**: pollution, smoke, mold → chronic respiratory
  irritation, inflammation
- **COPD progression**: dyspnea chronic, dissonance constant
- **Sleep apnea**: intermittent O2 drops → chronic cardiovascular
  + cognitive damage
- **Altitude sickness**: acute low O2 → headache, fatigue, nausea
  (dissonance compound)

**(d) Positive deviations → reward → baseline shift**

- **"Fresh air effect"**: forest, mountain, coast — direct relief
  reward. Phytoncides + cleaner air + circadian light + vestibular
  walking compound
- **Controlled breathing practices**: pranayama (yogic), Wim Hof method,
  coherent breathing (~6 breaths/min resonance), box breathing
- **Post-exertion recovery breaths**: parasympathetic rebound, relief
  reward
- **First breath of morning outside**: familiar reward pattern
- **Altitude training**: paradoxical adaptation rewards
- **Sighs**: natural reset mechanism, deep breath after tension

**(e) Baseline adaptation**

- **Altitude acclimation**: erythropoiesis shifts over weeks, baseline
  O2 carrying capacity adapts
- **Fitness affects breath baseline**: athletes have lower resting rate,
  higher vital capacity
- **Chronic anxiety** shifts baseline upward (shallower, more frequent
  breathing — chest-dominant)
- **Meditation training** shifts baseline (slower, deeper, more
  diaphragmatic — extensively documented)
- **Wim Hof method** shows voluntary control of normally automatic
  autonomic responses via breath training (Kox 2014)

**(f) Research citations**

- 🟢 Porges, S. (2011). Polyvagal theory — respiratory sinus arrhythmia
  central
- 🟢 Feldman, J. & Del Negro, C. Respiratory neuroscience
- 🟢 Brown, R. & Gerbarg, P. Breath therapy clinical research
- 🟢 Nestor, J. (2020). "Breath: The New Science of a Lost Art" —
  literature review + anthropological evidence
- 🟢 Kox, M. et al. (2014). Wim Hof method autonomic modulation via
  breath — controlled trial
- 🟢 Lehrer, P. & Gevirtz, R. Heart rate variability biofeedback
  via breath research
- 🟢 Zaccaro, A. et al. (2018). "How breath-control can change your life"
  review

**(g) Phase B case mapping**

- **B5 karoshi**: shallow chest office breathing, poor air quality
  fluorescent office, chronic sympathetic
- **B25 contemplative practice**: breath awareness explicit, documented
  HRV + autonomic shifts
- **B50 solitary**: restricted air quality (poorly ventilated cells),
  chronic stress breathing pattern
- **B46 Proenneke**: clean forest air daily, varied exertion patterns,
  ancestral-adjacent breath pattern
- **B10 ultra-marathon**: extreme respiratory training, adaptation
- **B28 chess master**: often noted shallow breath during intense
  concentration
- **Panic disorder + anxiety cases generally**: breath-anxiety feedback
  loops documented
- **DC3 ancestral nomad**: clean outdoor air daily; digital nomad = varied,
  often urban polluted

**(h) Individual variation**

- **Asthma, COPD, sleep apnea** prevalence substantial
- **Lung capacity genetic variation**
- **Altitude-born individuals** (Tibetan, Andean) baseline different
  genetically (hypoxia-inducible factor variants)
- **Training**: singers, wind instrument players, divers, athletes
  dramatically different baselines
- **Nasal anatomy**: septum deviation, chronic congestion affect daily
  breathing pattern
- **Anxiety/panic disorder**: chronic breath dysregulation

### §4.4 Cardiovascular (Nhịp tim, huyết áp)

**(a) Body đo gì**

Cardiovascular interoception = body sensing own heart/vascular state:
- **Heart rate (HR)**: resting ~60-100 bpm adult, shifts với activity
  và emotional state
- **Blood pressure**: detected via **baroreceptors** (carotid sinus +
  aortic arch) — feedback for autonomic regulation
- **Heart rate variability (HRV)**: beat-to-beat variation (không constant
  interval) — **interoceptive gold standard** measure, reflects vagal
  tone + sympathetic-parasympathetic balance
- **Vagal tone**: parasympathetic dominance measure, correlates với
  emotional regulation + social engagement (Porges polyvagal theory)
- **Subjective heart sensation**: interoceptive awareness — khả năng
  cảm nhận tim đập (varies dramatically between individuals — Schandry
  heartbeat detection task)
- **Cardiovascular là Craig insula's MAIN interoceptive input**: insula
  processes cardiovascular signals as foundation của interoceptive
  awareness

HRV is particularly important: **high HRV = healthy**, reflects adaptive
flexibility of autonomic system. Low HRV = chronic stress, depression,
poor emotional regulation.

**(b) Ancestral baseline**

- **Varied heart rate** throughout day (exertion + rest cycles)
- **Low resting HR** do fitness baseline
- **High HRV** reflecting varied demands + adequate recovery
- **Recovery cycles** after exertion — parasympathetic rebound
- **Acute stress responses** với recovery — không chronic elevation
- **No sustained cognitive stress** trong ancestral environment

NOT: chronic elevated HR từ work stress, sustained sympathetic activation,
low HRV, hypertension chronic từ sedentary + processed food.

**(c) Negative deviations → dissonance**

- **Chronic tachycardia**: anxiety, stress, poor fitness → sustained
  elevated HR
- **Hypertension chronic**: often silent but damages over time — "silent
  L1 deficit" until L0 event (stroke, heart attack)
- **Postural hypotension**: fainting upon standing, elderly common
- **Palpitations**: awareness of irregular heartbeats, dissonance
- **Arrhythmias**: chronic or paroxysmal dysregulation
- **Low HRV**: associated với depression, chronic stress, poor emotional
  regulation, mortality risk
- **Heart disease progression**: L1 → L0 boundary phenomenon
- **Panic attacks**: sudden sympathetic surge → perceived heart crisis
  → more anxiety feedback

**(d) Positive deviations → reward → baseline shift**

- **Flow state**: HR elevated BUT HRV maintained — "optimal arousal"
- **Exercise**: controlled HR elevation + recovery → fitness baseline
  improvement
- **Parasympathetic activation**: relaxation, meditation, oxytocin
  activation, affective touch → HRV increase
- **Resonance breathing** (~0.1 Hz or ~6 breaths/min): maximizes HRV
  through RSA — Lehrer & Gevirtz biofeedback research
- **Cardiovascular fitness progress**: measurable HR decrease over
  training
- **Social engagement**: safe social interaction activates ventral vagal
  complex, increases HRV (Porges)

**(e) Baseline adaptation**

- **Fitness** lowers resting HR, increases HRV — measurable trong weeks-
  months
- **Chronic stress** elevates baseline HR, lowers HRV (sympathetic
  dominance)
- **Age** decreases HRV progressively (nhưng trainable)
- **Meditation training** shifts HRV upward — extensive research literature
- **HRV biofeedback** training documented effects on baseline
- **Sedentary deconditioning** reverses fitness gains, shifts baseline
  unhealthy direction trong weeks

**(f) Research citations**

- 🟢 Porges, S. (2011). "The Polyvagal Theory" — foundational
- 🟢 Thayer, J. & Lane, R. HRV và emotional regulation
- 🟢 Craig, A.D. (2003, 2009). Interoception insula research —
  cardiovascular primary
- 🟢 Schandry, R. (1981). Heartbeat perception task — foundational
  interoceptive awareness measure
- 🟢 Appelhans, B. & Luecken, L. HRV emotional regulation meta-analysis
- 🟢 Lehrer, P. & Gevirtz, R. HRV biofeedback research
- 🟢 Thayer, J. et al. Meta-analyses HRV + health outcomes
- 🟡 McCraty, R. HeartMath research (some methodology issues but baseline
  findings useful)

**(g) Phase B case mapping**

- **B5 karoshi**: chronic elevated HR, low HRV từ sustained work stress
  → cardiovascular strain documented in karoshi syndrome
- **B1 workaholic burnout**: chronic cardiovascular strain, cortisol +
  HR compound
- **B25 contemplative**: meditation shifts HRV upward measurably
- **B11 codependent**: elevated HR từ chronic attunement stress, low
  HRV common trong this pattern
- **B46 Proenneke**: natural exertion + recovery, healthy cardiovascular
  baseline ancestral-adjacent
- **Flow state cases** (B28 chess, B30 Jiro, B44 open source): HR may
  rise but HRV maintained trong "optimal arousal" zone
- **General heart disease epidemiology**: modern cardiovascular disease
  rates = framework concern point about modern baseline
- **DC1 Tesla** late-life stress + insomnia: cardiovascular decline
  documented

**(h) Individual variation**

- **Genetic cardiovascular disease risk**: familial hypercholesterolemia,
  QT variants, etc.
- **Fitness level**: dramatic baseline shifts available — trained
  athlete's resting HR 40-50, sedentary 70-90
- **Autonomic disorders**: POTS (Postural Orthostatic Tachycardia
  Syndrome), dysautonomia, vagal syncope
- **Age and hormonal**: menopause affects HRV, testosterone affects
  baseline
- **Stress history**: chronic trauma affects baseline long-term
- **Interoceptive awareness**: dramatic individual variation — some
  people can count heartbeats, others cannot

### §4.5 Visceral (Nội tạng, dạ dày, ruột)

**(a) Body đo gì**

Visceral interoception = body sensing organ states, especially digestive
system. **The "second brain"** (Gershon 1998):

- **Enteric nervous system**: ~100-500 triệu neurons trong gut — more
  than spinal cord. Can function largely autonomously.
- **Gut-brain axis via vagus nerve**: **80% afferent** fibers carry gut
  signals UP to brain (chỉ 20% efferent motor commands DOWN). Body
  predominantly "listens" to gut.
- **Gut motility**: peristalsis, transit time, reverse peristalsis
  (nausea/vomit trigger)
- **Stomach state**: fullness (stretch receptors), emptying, acidity
- **Intestinal signals**: gas, bloating, urgency, fullness
- **Microbiome signaling**: bacterial metabolites (short-chain fatty
  acids, serotonin precursors — ~90% body serotonin made trong gut)
- **Visceral pain**: distinct quality từ cutaneous — diffuse, hard to
  localize, referred pain common
- **Nausea**: integrated signal từ multiple sources (toxins, motion,
  visceral pain, hormonal)
- **Satiety**: CCK (cholecystokinin), leptin, PYY, stretch receptor
  compound
- **Organ sense (insula processing)**: subjective "gut feelings" —
  literal interoceptive signals không chỉ metaphorical

Gut-brain research explosion last 15 năm reveals gut as major
interoceptive input, previously underappreciated.

**(b) Ancestral baseline**

- **Intermittent feeding**: không constant — some hours empty, periodic
  feast, occasional fast
- **Whole foods** varied seasonally
- **Rich microbiome input**: varied food sources, fermentation,
  environmental microbes, co-sleeping transfer
- **Moderate fiber**: wild plant foods fiber-rich
- **No refined sugar constant**, no ultra-processed
- **Fermented foods across cultures**: bacteria input deliberate
- **Seasonal food variation**: microbiome responds to seasonal shifts

NOT: constant snacking, ultra-processed food, low fiber, antibiotic
exposure constant, sanitized environment killing microbial diversity,
sedentary slowing motility.

**(c) Negative deviations → dissonance**

- **Nausea**: intense acute dissonance, vagal-mediated
- **Constipation**: pressure + transit dysregulation
- **Bloating**: pressure + dysbiosis signal, common modern complaint
- **Visceral pain**: appendicitis, IBS flares, gastritis, gut infection
- **IBS (Irritable Bowel Syndrome)**: ~10-15% population, chronic
  visceral dissonance without organic damage — gut-brain axis
  dysregulation classic example
- **Food intolerance/allergy reactions**: immune + visceral compound
- **Antibiotic microbiome disruption**: mood effects documented (gut-brain
  axis)
- **Gut-brain axis dysregulation → mood effects**: anxiety, depression
  correlations (Mayer research, Cryan & Dinan)
- **"Khó chịu không rõ lý do"** often has visceral component unrecognized

**(d) Positive deviations → reward → baseline shift**

- **Satiety after needed food**: warm, calm parasympathetic feeling,
  post-prandial rest reward
- **Digestive ease**: no signal = good signal (interoceptive silence)
- **Probiotic/fermented food**: microbiome support reward (culturally
  developed across many traditions — yogurt, kimchi, sauerkraut, nước
  mắm, miso, kombucha)
- **Fresh whole food impact**: felt effect post-meal vs processed food
- **Fasting-refeed cycle**: evolutionarily matched pattern, some individuals
  report cognitive + mood benefits (research ongoing, caution needed)
- **Social meals**: combined với social reward → amplified

**(e) Baseline adaptation**

- **Dietary adaptation**: gut microbiome changes within days-weeks của
  diet change (David et al. 2014 rapid diet microbiome response)
- **Fiber tolerance** builds với gradual exposure (sudden increase causes
  dissonance)
- **FODMAP sensitivity** variable, shifts với exposure
- **Stress shifts gut motility**: acute = slow, chronic = dysregulation
  patterns
- **Cultural diet baseline**: lifetime dietary pattern shapes gut baseline
  dramatically
- **Antibiotic disruption**: recovery takes weeks-months, sometimes
  incomplete

**(f) Research citations**

- 🟢 Mayer, E. (2016). "The Mind-Gut Connection" book
- 🟢 Cryan, J. & Dinan, T. Gut-brain axis research extensive
- 🟢 Gershon, M. (1998). "The Second Brain" — foundational
- 🟢 Sonnenburg, J. & E. Microbiome research, "The Good Gut"
- 🟢 Wu, G. & Bushmanc, F. American Gut Project
- 🟢 David, L. et al. (2014). Rapid diet-microbiome response — Nature
- 🟢 Craig, A.D. (2002, 2009). Interoception insula — visceral central
- 🟢 Enck, P. et al. Enteric nervous system research
- 🟢 Yano, J. et al. (2015). Gut microbiome controls serotonin synthesis
- 🟢 Foster, J. & McVey Neufeld, K.A. (2013). Gut-brain axis depression
  + anxiety

**(g) Phase B case mapping**

- **USER'S OWN PHENOMENOLOGY** (từ session): "ăn đồ ăn lạ no quá → khó
  tiêu → khó ngủ → người khó chịu 1-2 ngày, phải ăn cơm mới bình thường
  lại" — **direct visceral dissonance cascade**. Classic example của
  gut-brain axis + microbiome disruption + baseline mismatch (gut adapted
  to cơm-rice baseline, departure từ baseline causes multi-day
  dysregulation). Demonstrates visceral channel as distinct body-input
  với own baseline dynamics.
- **B31 ultra-processed food**: gut disruption + brain effects documented,
  microbiome dysbiosis từ low fiber + high processed food
- **B5 karoshi**: stress-induced GI problems common trong workaholic pattern
- **B48 McCandless**: toxic plant ingestion → severe visceral pain +
  starvation → contributed to death (Hedysarum alpinum seed toxicity
  hypothesis)
- **B13 love addict**: limerence → "butterflies in stomach" (visceral
  coupling với emotional/hormonal state, literal visceral signal)
- **B50 solitary**: stress-induced GI problems documented trong
  confinement research
- **B9 Blue Zone diet**: fermented foods, legumes, vegetables → rich
  microbiome baseline, ancestral-adjacent
- **B14 extended family**: multi-generational dietary tradition → gut
  baseline inherited/maintained
- **DC3 ancestral nomad**: diverse natural food microbiome vs digital
  nomad = varied international foods, sometimes "traveler's stomach"
  từ constant microbiome challenges

**(h) Individual variation**

- **IBS prevalence** ~10-15% population
- **FODMAP sensitivity** highly variable
- **Lactose tolerance genetics**: LCT gene persistence variable (northern
  European adapted, other populations reduced)
- **Microbiome diversity**: large individual variation, genetic +
  environmental
- **Autoimmune gut conditions**: celiac, IBD, Crohn's
- **Food allergies**: genetic + developmental
- **Cultural diet baseline**: immigrants moving to different food
  environment often experience multi-year gut adaptation difficulty

### §4.6 Metabolic (Đói, no, khát)

**(a) Body đo gì**

Metabolic interoception = body sensing energy + hydration state:
- **Blood glucose**: detected by pancreatic islet cells + brain glucose
  sensors (hypothalamus, brainstem)
- **Hydration state**: osmolality detected by hypothalamic osmoreceptors,
  triggers thirst
- **Hunger hormones**: **ghrelin** (stomach, rises before meals, "hunger
  hormone"), counteracted by **leptin** (adipose, long-term satiety
  signaling), **CCK** (intestine, acute satiety after eating)
- **Satiety integration**: PYY, GLP-1, stretch receptors gut, blood
  glucose + insulin
- **Hypoglycemia detection**: L1 → L0 territory at severe, brain
  prioritizes glucose over all else
- **Energy state sense**: subjective fatigue, alertness, "running on
  empty" feeling
- **Electrolyte balance**: subtle signaling, salt craving reliable
- **Core metabolic rate** baseline affects subjective energy

Metabolic crosses L0 boundary at extremes: severe hypoglycemia,
dehydration, starvation → survival emergency.

**(b) Ancestral baseline**

- **Intermittent feeding**: not constant — some hours empty, periodic
  larger meals, occasional fasts (hours to days)
- **Seasonal food variation**: abundance + scarcity cycles
- **Water từ food + natural sources**: variable availability
- **Physical activity metabolism coupling**: exertion = increased needs,
  recovery = replenishment cycles
- **Breastfeeding baseline**: extended infant feeding, establishes early
  metabolic calibration
- **No refined sugar constant** — glucose spikes không chronic
- **Limited caloric density** relative to modern processed food

NOT: 3+ meals/day scheduled, constant snacking, refined carbs hourly,
sweetened beverages constant, ultra-processed caloric density, chronic
over-feeding.

**(c) Negative deviations → dissonance**

- **Hunger nhẹ** (đói nhẹ): L1 mild signal, seeking food behavior
- **Hunger mạnh**: L1 stronger, irritability, reduced cognitive function
- **Hypoglycemia** (hạ đường huyết): **L0 territory** — shakiness, sweating,
  confusion, coma nếu severe
- **Dehydration**: headache → cognitive decline → organ failure spectrum
- **Chronic over-feeding**: insulin resistance, metabolic syndrome,
  leptin resistance → "always hungry" despite adequate stores
- **Erratic glucose swings** (reactive hypoglycemia): processed carb
  diet → spikes and crashes → mood swings, fatigue, anxiety
- **Salt depletion** (rare in modern diet, common historically): specific
  craving + fatigue
- **Starvation** (B48 McCandless): L0 eventually fatal

**(d) Positive deviations → reward → baseline shift**

- **Satiety after needed food**: warm, calm parasympathetic reward
- **Thirst quenched**: immediate relief reward
- **First coffee morning**: familiar caffeine + ritual reward
- **Feast after fasting**: evolved amplified reward pattern
- **Social meals**: metabolic satisfaction + social reward compound
- **Post-exertion refueling**: depleted state + replenishment reward
- **Electrolyte replenishment** after exertion

**(e) Baseline adaptation**

- **Meal schedule shifts hunger timing**: Mary Dallman research — ghrelin
  rises at expected meal times, not at true hunger. 3-meal schedule
  creates 3 hunger peaks daily.
- **Fasting adaptation**: ghrelin actually DECREASES with extended fasting
  (counterintuitive), body metabolically adapts
- **Insulin resistance shifts baseline**: chronic high carb → insulin
  resistance → constant hunger despite adequate calories
- **Microbiome modulates appetite**: gut bacteria influence hunger
  signaling
- **Cultural meal patterns**: Mediterranean vs American snacking patterns
  create different baselines

**(f) Research citations**

- 🟢 Pontzer, H. Hunter-gatherer energy expenditure + metabolism research
- 🟢 Ludwig, D. Carbohydrate-insulin model of obesity
- 🟢 Cummings, D. Ghrelin research foundational
- 🟢 Friedman, J. & Halaas, J. (1998). Leptin discovery + obesity
- 🟢 Dallman, M. "Feast or famine" research — meal anticipation
- 🟢 Taubes, G. "The Case Against Sugar" (popular science, literature
  review)
- 🟢 Mattson, M. Intermittent fasting research
- 🟢 Hall, K. NIH metabolic ward research

**(g) Phase B case mapping**

- **B48 McCandless** (Into the Wild): starvation + toxic plant ingestion
  = L0 metabolic failure, classic survival extreme
- **B45 Onoda** 29 năm jungle: adapted intermittent feeding, metabolic
  resilience extreme
- **B46 Proenneke**: self-provisioning Alaska, varied seasonal metabolism
- **B31 ultra-processed food obsession**: insulin resistance + leptin
  resistance pattern, baseline dysregulation
- **B5 karoshi**: erratic eating, skipped meals, caffeine substitute,
  metabolic dysregulation
- **B9 Blue Zone diet**: plant-heavy, whole food, moderate calorie,
  ancestral-adjacent metabolic pattern
- **B10 ultra-marathon**: extreme energy expenditure, metabolic adaptation
  extreme, occasional hypoglycemia risk
- **B50 solitary**: L0 metabolic met but narrow, no variation
- **DC3 ancestral nomad**: feast-fast cycles, seasonal; digital nomad =
  irregular scheduled, often processed

**(h) Individual variation**

- **Metabolic health**: dramatic variation, insulin sensitivity varies
  10x+
- **Diabetes prevalence**: T1 autoimmune + T2 lifestyle
- **Intermittent fasting responsiveness** varies dramatically
- **Ethnic metabolic differences**: Asian populations different T2
  diabetes risk, Native American populations thrifty genotype
- **Microbiome-mediated differences**: gut bacteria modulate metabolic
  response
- **Age**: metabolic rate declines, insulin sensitivity often reduces
- **Exercise tolerance**: VO2max, lactate threshold individual variance

### §4.7 Hormonal-sensed states

**(a) Body đo gì**

Hormones KHÔNG phải interoceptive inputs theo nghĩa strict — chúng là
**outputs** của other processes (endocrine glands, feedback loops). Nhưng
chúng **BECOME inputs** đến body state sensing vì effects của chúng trên
autonomic + interoceptive systems được felt as body states.

Framework interpretation: hormones are **body state modulators** mà PFC
đọc qua downstream effects (heart rate, muscle tension, gut state,
energy, mood).

Key hormones felt as body states:

- **Cortisol**: chronic stress "feeling" — tense, alert, irritable,
  fatigue paradoxical (Sapolsky extensive research)
- **Testosterone**: drive, motivation, confidence — felt as energetic
  assertiveness
- **Estrogen / progesterone**: cyclical state shifts, mood modulation,
  sensitivity changes
- **Oxytocin**: bonding warmth, calm, social reward (Carter, Insel
  research)
- **Dopamine**: "wanting" not "liking" (Berridge distinction), motivation,
  anticipation energy
- **Serotonin**: mood floor, sense of "OK-ness", equanimity
- **Endorphins + endocannabinoids**: pain relief, euphoria, runner's
  high (Fuss 2015 endocannabinoid update)
- **Melatonin**: sleep readiness, darkness response
- **Adrenaline/noradrenaline**: arousal, alertness, stress response
- **Thyroid** (T3, T4): baseline energy metabolism

**Critical insight**: hormones không có "receptor" cho reading như
other inputs. Body senses them via **effects on other systems**. Nhưng
subjective states they produce are real, felt, and affect behavior.

**(b) Ancestral baseline**

- **Cyclical variation**: cortisol diurnal cycle (high AM, low PM),
  testosterone seasonal + diurnal, estrogen cyclical
- **Matched to demands**: acute stress spikes followed by recovery,
  not chronic elevation
- **Touch + bonding frequent** → oxytocin baseline maintained
- **Physical activity + recovery** → testosterone responsive
- **Natural light + dark cycles** → melatonin properly timed
- **Social validation regular** → dopamine tonically fed
- **Age-appropriate hormonal shifts**: puberty, reproductive, menopause
  biologically normative

NOT: chronic cortisol elevation, testosterone collapse từ sedentary +
stress, oxytocin starvation từ touch deprivation, dopamine dysregulation
từ engineered supernormal stimuli.

**(c) Negative deviations → dissonance**

- **Chronic cortisol elevation**: "wired but tired", immune suppression,
  cognitive decline, belly fat accumulation, depression risk (Sapolsky
  "Why Zebras Don't Get Ulcers")
- **Cortisol blunting** (late-stage chronic stress): anergia, inability
  to respond to stress, burnout endpoint
- **Testosterone collapse từ overtraining**: "overtraining syndrome" —
  fatigue, mood decline, libido loss, documented trong endurance
  athletes (B10 pattern)
- **Estrogen/progesterone dysregulation**: PMS, perimenopause symptoms,
  mood instability
- **Oxytocin deprivation từ touch starvation**: diffuse unease, bonding
  difficulty, depression risk
- **Dopamine dysregulation**: either blunted (addiction recovery
  phase, depression anhedonia) hoặc hypersensitive (addiction active)
- **Serotonin depletion**: depression, mood floor gone
- **Endorphin absence** chronic: low pain tolerance, general dysphoria
- **Melatonin disruption** (blue light late, shift work): sleep
  dysregulation

**(d) Positive deviations → reward → baseline shift**

- **Eustress** (positive stress): acute cortisol + recovery → resilience
  building
- **Bonding warmth** (oxytocin from affective touch, eye contact, safe
  social): calm reward state
- **Flow state**: dopamine + endorphin + noradrenaline compound — peak
  engagement reward
- **Post-exertion endorphin**: runner's high, euphoria
- **Testosterone boost từ success**: documented winner's effect, confidence
  amplification
- **Sexual bonding**: oxytocin + dopamine + endorphin compound peak

**(e) Baseline adaptation** — **critical cho reframe**

Hormonal systems show **strongest adaptation/hedonic treadmill patterns**:

- **Chronic stress re-baselines cortisol**: HPA axis shifts, "new normal"
  established, hard to return
- **Hedonic treadmill on dopamine**: supernormal stimuli (processed food,
  social media, drugs) shift dopamine baseline dramatically, natural
  reward becomes insufficient
- **Testosterone response to training**: upregulation với consistent
  training, downregulation với overtraining
- **Oxytocin response blunting**: addiction research shows social bonds
  weaken as drug reward hijacks system
- **Tolerance buildup** in drug use: neural adaptation → diminishing
  returns → escalation

**All major addictions** reflect hormonal/neurotransmitter baseline
shifting gone wrong. Opioid tolerance, alcohol tolerance, stimulant
tolerance — direct evidence cho reframe's baseline adaptation mechanism.

**(f) Research citations**

- 🟢 Sapolsky, R. "Why Zebras Don't Get Ulcers" + stress research
  extensive
- 🟢 Carter, C.S. Oxytocin + bonding research foundational
- 🟢 Insel, T. Social bonding neurobiology
- 🟢 Schultz, W. Dopamine prediction error research
- 🟢 Berridge, K. Wanting vs liking distinction
- 🟢 Fuss, J. et al. (2015). Endocannabinoid runner's high update
- 🟢 Nesse, R. "Good Reasons for Bad Feelings" — evolutionary psychiatry
- 🟢 Wrangham, R. + Bronson, F. Seasonal hormonal research
- 🟢 Young, L. Prairie vole bonding oxytocin research

**(g) Phase B case mapping**

- **B5 karoshi**: chronic cortisol elevation → HPA dysregulation → burnout,
  karoshi syndrome documented
- **B1 workaholic burnout**: similar cortisol pattern + dopamine
  dysregulation
- **B13 love addict**: limerence phase = dopamine + oxytocin surge →
  crash after withdrawal, classic addiction pattern on bonding system
- **B10 ultra-marathon / overtraining**: testosterone collapse documented
  trong extreme endurance athletes, cortisol elevated chronically
- **B31 ultra-processed food / substance addictions**: dopamine baseline
  shifted, tolerance, escalation
- **B11 codependent**: chronic cortisol from attunement stress, oxytocin
  dysregulated (seeking without receiving equally)
- **B19 touch hunger**: oxytocin starvation primary
- **B35 screen addiction**: dopamine baseline shifted từ engineered
  supernormal stimulus
- **B46 Proenneke**: ancestral-matched hormonal rhythms (light cycles,
  physical activity, seasonal variation, though minimal oxytocin từ
  social source)
- **B25 contemplative**: documented HPA modulation, increased serotonin
  + endocannabinoid tone

**(h) Individual variation**

- **Genetic hormone receptor variants**: OXTR oxytocin receptor, DRD4
  dopamine receptor variants significant
- **Cycle phase** (women): mood + sensitivity varies dramatically
- **Age**: hormonal shifts across life stages normative
- **Stress reactivity**: HPA axis reactivity varies genetically +
  developmentally
- **Trauma history**: affects HPA baseline long-term
- **Exercise state**: affects multiple hormonal systems
- **Medications**: SSRIs, hormonal contraceptives, corticosteroids —
  pharmacological baseline shifts

### §4.8 Sleep / Circadian

**(a) Body đo gì**

Sleep/circadian là **body-input state shift**, không phải instantaneous
signal. Body senses its own sleep state + circadian phase:

- **Sleep drive / homeostatic sleep pressure**: **adenosine** accumulation
  during wake → drowsiness. Caffeine blocks adenosine receptors (mechanism
  of stimulant effect)
- **Circadian rhythm**: **suprachiasmatic nucleus (SCN)** in hypothalamus
  = master clock, entrained by light via melanopsin retinal ganglion
  cells
- **Melatonin**: signals darkness → sleep readiness, released by pineal
  gland when SCN detects low light
- **Sleep architecture stages**:
  - **NREM 1-2**: light sleep, transition
  - **NREM 3 (slow wave sleep)**: deep restorative, physical recovery,
    growth hormone release, immune function
  - **REM**: dreaming, memory consolidation (especially emotional),
    neural cleaning, creative insight
- **Wake state continuum**: from deep sleep → drowsy → alert → hyperalert
- **Subjective fatigue sense**: energy level, mental clarity
- **Circadian alignment sensing**: "morning person" vs "night person"
  feeling, jet lag dissonance

Sleep uniquely bridges conscious/unconscious — body enters wholly
different operational state mỗi 24 giờ. This is not just a sensing
activity but a **state transition** of the entire organism.

**(b) Ancestral baseline**

- **Sunset-to-sunrise sleep**: entrained by natural light cycle (~8-9
  hours pre-industrial)
- **Possibly biphasic**: some historical evidence cho "first sleep" +
  "second sleep" với awake period middle of night (Ekirch 2005)
- **Group sleeping**: co-sleeping ancestral norm, individual sleep
  modern anomaly
- **No artificial light late**: melatonin rises naturally post-sunset
- **Temperature drop** environment supports sleep physiology
- **Variable exertion** daily → proper sleep drive buildup
- **No caffeine + alcohol + medications**: natural sleep chemistry

NOT: artificial light until bedtime, blue screens pre-sleep, chronic
sleep debt, shift work, fragmented sleep, caffeine afternoon, constant
alarm wake.

**(c) Negative deviations → dissonance**

- **Insomnia**: sleep initiation hoặc maintenance difficulty, chronic
  dissonance
- **Fragmented sleep**: sleep apnea, restless legs, frequent waking →
  reduced REM + deep sleep → daytime consequences
- **Sleep debt chronic**: cumulative deficit, cognitive decline,
  immune suppression, metabolic dysregulation
- **Shift work**: circadian misalignment → elevated disease risk
  (IARC classifies shift work as "probable carcinogen")
- **Jet lag**: circadian phase shift dissonance, resolves over days
- **Blue light exposure late**: melatonin suppression, delayed sleep
  onset
- **Hyperarousal**: anxiety, cortisol elevation → can't fall asleep
- **Sleep apnea**: intermittent hypoxia + fragmentation → cardiovascular
  + cognitive damage
- **Seasonal affective disorder**: circadian + light dysregulation
  syndrome

**(d) Positive deviations → reward → baseline shift**

- **Deep restorative sleep**: morning feels renewed, cognitive + physical
  restoration
- **Morning light exposure**: melatonin suppression properly timed,
  circadian phase anchoring
- **Natural sleep-wake cycle**: rhythm feels "right"
- **Brief afternoon nap** (where culturally appropriate): 20-30 min
  improves afternoon function
- **Sleep-dependent memory consolidation**: learning benefits overnight
- **REM-dependent emotional processing**: "sleep on it" effect real

**(e) Baseline adaptation**

- **Shift work partial adaptation**: chronic shift workers adjust
  partially nhưng never completely — permanent mild dysregulation
- **Jet lag recovery**: ~1 day per hour timezone shift typically
- **Seasonal adaptation**: circadian responds to seasonal light changes
- **Sleep debt accumulation**: cannot fully "catch up" on lost sleep
  — some damage cumulative
- **Chronotype flexibility**: limited (genetic component large),
  partial shift possible through consistent schedule
- **Meditation affects sleep architecture**: documented improved deep
  sleep

**(f) Research citations**

- 🟢 Walker, M. (2017). "Why We Sleep" — comprehensive literature review
- 🟢 Foster, R. & Kreitzman, L. "Rhythms of Life" — circadian foundational
- 🟢 Czeisler, C. Circadian research
- 🟢 Siegel, J. Sleep neuroscience research
- 🟢 Stickgold, R. Memory consolidation during sleep
- 🟢 Berson, D.M. et al. (2002). Melanopsin retinal ganglion cells
- 🟢 Ekirch, R. (2005). "At Day's Close" — historical biphasic sleep
- 🟢 Wever, R. Free-running circadian rhythm experiments
- 🟢 IARC (2007). Shift work carcinogenicity classification

**(g) Phase B case mapping**

- **B1 workaholic burnout**: chronic sleep debt central to burnout
  pattern
- **B5 karoshi**: extreme sleep deprivation documented, direct
  cardiovascular impact
- **B10 ultra-marathon**: sleep disruption during events, recovery
  demands
- **B50 solitary**: sleep disruption from artificial light, stress,
  routine disruption
- **B46 Proenneke** Alaska: natural light cycle, ancestral-matched
  sleep
- **B35 screen addiction**: blue light late → melatonin suppression,
  sleep onset delay, fragmented sleep
- **B9 Blue Zone**: regular sleep patterns, earlier bedtimes documented
- **B25 contemplative**: meditation improves sleep architecture
- **Shift workers generally**: framework concern about modern circadian
  damage
- **DC1 Tesla** late-life insomnia: documented, contributed to cardiovascular
  decline

**(h) Individual variation**

- **Chronotype genetic**: PER1, PER2, CLOCK gene variants determine
  "morning lark" vs "night owl" tendency — largely fixed
- **Sleep need variation**: adults 7-9 hours average, some genetic
  short-sleepers (DEC2 variant) need ~6 hours
- **Age**: sleep architecture changes (less deep sleep elderly, more
  fragmentation)
- **Sleep disorders**: insomnia ~10% population, sleep apnea ~5-10%,
  narcolepsy rare
- **Menstrual cycle**: affects sleep quality
- **Hormonal transitions**: puberty, perimenopause disrupt baseline

### §4.9 Self-signal interoception (meta)

**⭐ ARCHITECTURAL KEYSTONE**: §4.1-§4.8 liệt kê specific interoceptive
inputs (thermoreception, nociception, respiratory, cardiovascular,
visceral, metabolic, hormonal, sleep). **§4.9 là READING CAPACITY**
— without it, tất cả các inputs khác fire nhưng body "cannot hear."
Đây là prerequisite cho body-base health bất kể các inputs khác có
được met không.

Đây cũng là section directly address **channel-lexithymia barrier**
documented trong Body-Base-Deep-Cases.md methodology — một số individuals
có "silent channels" mà họ cannot verbalize. Self-signal interoception
gap là mechanism underlying đó.

**(a) Body đo gì**

Self-signal interoception = **body sensing body's own state**, meta-
level sensing capacity:

- **Insula** (especially anterior insula — AI): primary interoceptive
  hub, Craig 2002/2009 foundational research
- **Anterior cingulate cortex (ACC)**: affective-motivational dimension
  của interoception, valence assignment
- **Ventromedial prefrontal cortex (VMPFC)**: integration of bodily
  feelings into decision making (Damasio somatic marker hypothesis)
- **Posterior insula**: primary interoceptive cortex, first-order
  representation
- **Predictive interoception** (Seth 2013, Barrett 2017): brain
  continuously generates predictions about body state, matches against
  actual signals, prediction errors drive updates

**Three levels của interoceptive awareness** (Garfinkel et al. 2015):
1. **Interoceptive accuracy**: objective performance on heartbeat
   detection, respiratory tracking tasks
2. **Interoceptive sensibility**: subjective self-report of body
   awareness
3. **Interoceptive awareness** (metacognitive): match between accuracy
   + sensibility = knowing what you know about your body

**Key insight**: all 3 dimensions trainable + variable + clinically
relevant.

Framework interpretation: self-signal interoception là the **READING
CAPACITY** that makes other inputs functional. Body có thể fire dissonance
signals (from §4.1-§4.8) nhưng nếu reading capacity compromised, PFC
không access được signal → silent deficit (§6 Body-Base.md outline
concept).

**(b) Ancestral baseline**

- **Developmental calibration via caregiver mirroring**: infants learn
  interoceptive awareness through being mirrored — caregiver labels
  baby's state ("you're hungry," "you're tired," "that hurt") → baby
  learns to read own states
- **Emotional labeling**: cultures với rich emotional vocabulary support
  interoceptive awareness development
- **Secure attachment**: foundation for interoceptive trust (Fonagy
  mentalizing research)
- **Rest with self-awareness**: downtime, meditation-adjacent practices,
  time alone with body
- **Body-based cultural practices**: dance, ritual, breathing, martial
  arts — embodied traditions
- **Physical labor với recovery**: body state salient, attention to
  fatigue + recovery

NOT: constant external stimulation preventing self-attention, emotional
labeling absent, dissociation normalized, alexithymic culture, screen
dependency suppressing self-reading, addiction self-medicating signal.

**(c) Negative deviations → dissonance (KEY framework content)**

**Clinical alexithymia** (Bird & Cook 2013): inability to identify +
describe emotions — documented condition affecting ~10% population.
Strong correlation với:
- Autism (Bird research shows alexithymia, not autism per se, drives
  emotional difficulties)
- Depression
- Somatic symptom disorders
- Eating disorders (cannot distinguish hunger from emotional states)

**Dissociation**: trauma adaptation, disconnection từ body signals.
Protective acutely, damaging chronically.

**Trauma-induced suppression**: body signals become dangerous (PTSD,
complex trauma) → suppression learned, body becomes "enemy territory"
— van der Kolk "The Body Keeps the Score"

**Chronic self-signal deafness từ codependency**: B11 pattern —
constant attunement to other's state → own state awareness atrophies.
Parallels caregiving burnout.

**Addiction self-medication**: substances suppress uncomfortable body
signals → reading capacity degrades from disuse → addiction worsens
→ positive feedback loop

**Helicopter parenting starvation** (B15): children whose states are
always intercepted and managed by parents → don't develop own
interoceptive reading capacity → adults với alexithymic tendencies

**Modern screen culture**: constant external attention demand → minimal
self-attention → atrophy of interoceptive capacity at population level
(emerging research)

**Parentification** (B12): children who serve as emotional caregiver
to adults → own needs suppressed → self-signal becomes dangerous
(expressing own needs punished)

**(d) Positive deviations → reward → baseline shift**

- **Meta-cognitive body awareness**: mindfulness practices measurably
  improve interoceptive accuracy (Farb research)
- **Meditation documented effects**: Vipassana, MBSR, various traditions
  improve insula thickness, interoceptive accuracy
- **Gendlin focusing capacity**: specific technique cho accessing
  "felt sense" — proto-verbal body knowledge
- **Somatic therapy techniques**: trauma-focused body-based therapy
  (SE, Somatic Experiencing, sensorimotor psychotherapy) rebuilds
  interoceptive connection
- **Contemplative traditions**: Buddhism (body scan), yoga, Tai Chi
  — explicit interoceptive training methods
- **Flow states**: paradoxically involve "loss of self" but may enhance
  interoceptive integration (research ongoing)

**(e) Baseline adaptation**

- **Contemplative training elevates**: 8-week MBSR shows measurable
  insula changes (Hölzel 2011)
- **Trauma suppresses**: persistent even after trauma resolution in
  some cases
- **Developmental critical periods**: infancy + early childhood
  foundational, adult training can partially compensate
- **Gradual reclaim**: therapy-based interoceptive rehabilitation shows
  progress over months-years
- **Self-medication degradation**: addiction recovery includes
  rebuilding interoceptive accuracy

**(f) Research citations — cornerstone of reframe**

- 🟢 Craig, A.D. (2002). "How do you feel? Interoception: the sense of
  the physiological condition of the body" — Nat Rev Neurosci foundational
- 🟢 Craig, A.D. (2009). "How do you feel — now? The anterior insula
  and human awareness" — Nat Rev Neurosci
- 🟢 Seth, A.K. (2013). "Interoceptive inference, emotion, and the
  embodied self" — Trends Cogn Sci
- 🟢 Barrett, L.F. (2017). "How Emotions Are Made" + "The theory of
  constructed emotion" — Social Cogn Affect Neurosci
- 🟢 Bird, G. & Cook, R. (2013). "Mixed emotions: the contribution of
  alexithymia to the emotional symptoms of autism"
- 🟢 Garfinkel, S. et al. (2015). "Knowing your own heart: distinguishing
  interoceptive accuracy from awareness" — 3-dimensional model
- 🟢 Damasio, A. Somatic marker hypothesis, "Descartes' Error"
- 🟢 Hölzel, B. et al. (2011). MBSR insula changes fMRI study
- 🟢 Farb, N. et al. Mindfulness + interoception research
- 🟢 van der Kolk, B. (2014). "The Body Keeps the Score" — trauma +
  body
- 🟢 Gendlin, E. (1978). "Focusing" — felt sense accessing
- 🟢 Fonagy, P. Mentalizing theory
- 🟢 Herbert, B.M. et al. Interoceptive sensitivity research

**(g) Phase B case mapping**

- **B11 codependent**: primary case — chronic outward attunement →
  self-signal interoception atrophy. Classic "doesn't know what they
  feel" presentation.
- **B12 parentified child adult**: role reversal developmental → own
  needs/signals suppressed → alexithymic adult
- **B15 helicopter parent effect on child**: child never develops
  own interoceptive reading because parent pre-empts
- **B25 contemplative practitioner**: self-signal trained explicitly,
  measurable improvement
- **B46 Proenneke** Alaska solo 30 năm: isolation forces self-reliance
  → self-signal must develop, adapted successfully (contrast với B47
  who didn't)
- **B35 screen addiction**: constant external attention → self-attention
  atrophy
- **B31 ultra-processed food addiction**: emotional eating = substituting
  food for emotional self-reading
- **B16 sex addiction**: substance-like pattern of signal suppression
- **Addiction cases generally**: self-medication pattern
- **DC1 Tesla** late-life: increasing disconnection from own state,
  obsessive rumination without body self-care
- **DC3 ancestral nomad**: embedded community provides mirroring +
  self-signal support; digital nomad lacks consistent mirroring from
  stable relationships

**(h) Individual variation**

- **Developmental history foundational**: attachment, caregiving quality,
  trauma exposure shape baseline dramatically
- **Autism + alexithymia overlap**: ~50% autistic individuals meet
  alexithymia criteria (Bird research)
- **Genetic factors**: emerging research on interoceptive variation
- **Culture-specific vocabulary**: languages với rich emotional
  vocabulary may support development
- **Gender**: research suggests women slightly higher interoceptive
  accuracy average (small effect)
- **Age**: declines with age, trainable throughout life
- **Practice-based**: dramatic variation in those with/without
  contemplative training

---

**§4 INTEROCEPTIVE INPUTS — section complete**

9 interoceptive inputs enumerated. Key findings cho reframe từ §4:

**1. Interoception là critical substrate** cho body-base framework —
more important than exteroception cho slow-decay phenomena. Most
channel-lexithymia barriers trace to interoceptive gaps.

**2. §4.9 self-signal interoception META giải thích "silent deficits"
mechanism**: body signals fire but reading capacity compromised →
deficits accumulate without PFC awareness. Đây là architectural core
của Body-Base.md §6 "silent deficiency phenomenon" concept — reframe
makes mechanism explicit.

**3. Hormonal systems show strongest hedonic treadmill patterns** —
addiction research directly validates reframe's baseline adaptation
mechanism across dopamine, cortisol, oxytocin, opioid systems.

**4. Gut-brain axis (§4.5) documented extensively** — visceral
interoception fundamental to mood + cognition, previously
underappreciated.

**5. Sleep/circadian (§4.8) unique as state-transition input**, not
just signaling. Framework should treat this separately from other
interoceptive signals.

**6. User's own phenomenology** (gut + cơm vs lạ → multi-day
dysregulation) directly demonstrates visceral interoception baseline
mechanism — grounded, personal validation.

**7. Cardiovascular (§4.4) = Craig's primary interoceptive input** —
HRV as interoceptive gold standard measure establishes framework's
core substrate claim with established research.

**8. Chronic modern conditions** (burnout, chronic pain, metabolic
syndrome, insomnia, addiction) all reflect interoceptive
dysregulation + baseline shifted environments. Framework concern
amplifies.

Reframe §4 assessment: **interoception enumeration PASSES test
criteria §1.4.1(1)** cho interoceptive category. §4.9 self-signal
interoception provides architectural keystone missing từ mô hình cũ
(§14.1 Example identified need, reframe makes central).

**§2-§4 ENUMERATION COMPLETE**. All exteroceptive + proprioceptive +
interoceptive body-inputs enumerated với research evidence + Phase B
case mapping + individual variation acknowledgment. Ready for §5
baseline adaptation mechanism (theoretical core).

---

## §5 — BASELINE ADAPTATION MECHANISM

### §5.1 Evolved baseline (ancestral calibration range)

**Câu hỏi foundational**: Tại sao mỗi body-input có baseline ở specific
range? Tại sao không random, không arbitrary?

**Câu trả lời**: Baselines là **evolved default setpoints** được
calibrate qua 2M+ năm natural selection. Mỗi receptor system, mỗi
adaptation dynamic, mỗi reward/dissonance response được shaped bởi
which responses survived và reproduced trong ancestral environment.

#### §5.1.1 Ancestral environment — concrete reference per input

Nhiều input categories có evolved baseline cụ thể documented:

**Vision** (§2.1): fractal dimension D ≈ 1.3-1.5 (Taylor 2006), 12-hour
daylight cycle, natural color spectrum varied, biological motion
prevalent, mixed vegetation + open sight lines (Savanna hypothesis).

**Audition** (§2.2): pink noise 1/f natural soundscape (Voss & Clarke
1975), social voices từ 30-150 tribe, silence only temporary, own
bodily sounds audible.

**Tactile** (§2.5): frequent affective social touch (grooming, carrying,
co-sleep), varied natural textures, varied ground contact, object
handling daily.

**Kinesthetic** (§3.3): walking 8-15 km/day (Pontzer hunter-gatherer
research), varied exertion + recovery cycles, weight-bearing labor.

**Gustation** (§2.4): ~30-35% carbs (complex), 20-35% protein, 30-40%
fat (Eaton & Konner 1985), seasonal variation, bitter compounds common,
refined sugar/salt absent.

**Sleep/Circadian** (§4.8): sunset-to-sunrise entrained by natural
light, possibly biphasic (Ekirch 2005), group sleeping, no artificial
light late.

**Hormonal** (§4.7): cortisol diurnal cycle với recovery periods,
testosterone seasonal + diurnal, oxytocin frequent từ social bonding,
dopamine tonically fed through regular rewards.

**Metabolic** (§4.6): intermittent feeding, feast-fast cycles, seasonal
variation, physical activity coupling.

Mỗi body-input có ancestral baseline **empirically documented** via
research across multiple independent traditions (anthropology,
paleontology, hunter-gatherer studies, evolutionary biology, comparative
primate research).

#### §5.1.2 Evolution mechanism

Natural selection theo logic của Why-Body-Knows.md §4 Tier 1:

```
  Gen A: body reward pattern X (near ancestral baseline)
    → survive → reproduce → gene propagates ✅
  Gen B: body reward pattern Y (far from ancestral baseline)
    → die → not reproduce → gene drops ❌

  Over 2M năm × triệu thế hệ × triệu individuals:
    → Only genes rewarding near-baseline patterns survived
    → Baseline = "what worked for survival ancestors"
    → Body HIỆN TẠI = survivors' descendants
```

Baselines không random — chúng là **compiled survival wisdom** stored
trong genome. Similar logic applies to all body-input categories.

#### §5.1.3 Key property: evolved default, not learned

Baselines **tồn tại trước individual development**:
- Newborn responds to sweet taste → evolved preference (ancestral =
  ripe fruit = energy + vitamins)
- Infants prefer natural face patterns → evolved (face recognition
  system pre-wired)
- Startle reflexes pre-wired at birth
- Circadian rhythm emerges từ genes + light cycle regardless of
  teaching
- Emotional expression universals across cultures (Ekman research)

Individual development **không CREATE** baseline — chỉ **shifts** nó
trong evolved bounds.

**Example**: human visual system có evolved fractal preference D ≈
1.3-1.5 (Taylor 2006). Person nào raised trong high-rise urban
environment sẽ có individual baseline shifted toward tolerating lower
D — nhưng preference cho fractal patterns vẫn remains latent (emerges
khi exposed to nature as adult, measurable via EEG response —
Hagerhall).

Baseline range là **innate architecture**, individual calibration là
**within-range tuning**.

#### §5.1.4 Connection to Why-Body-Knows §4 4-tier calibration

Why-Body-Knows §4 describes 4 calibration tiers:
- **Tier 1 evolution** (2M năm): establishes **baseline ranges**
- **Tier 2 development** (lifetime): **shifts within range**
- **Tier 3 culture** (transgenerational): **amplifies + shapes expression**
- **Tier 4 AI** (current): **accelerates tier 3**

**§5.1 (this section) = Tier 1 explicit**. Evolved baselines are the
outcome của Tier 1 calibration. **§5.2 = Tier 2** individual baseline
shifting. **§5.3 = the mechanism** của shifting (Novelty operator +
delta rule). **Tier 3-4** shape which individuals end up with which
baselines.

Reframe không contradict Why-Body-Knows 4-tier theory — nó **specifies
substrate** cho các tiers đó operate on. Tiers operate on **body-input
baselines**, not on "channels" as primitives.

#### §5.1.5 Mismatch problem (connection to Why-Body-Knows §5 evolution lag)

Key framework concern: modern environment deviates dramatically từ
ancestral baseline across **ALL input categories simultaneously**:

| Input         | Ancestral baseline        | Modern deviation              |
|---------------|---------------------------|-------------------------------|
| Vision        | Fractal D≈1.3-1.5         | Flat walls D≈1.0, screens    |
| Audition      | Pink noise + voices       | Mechanical drone, isolation   |
| Olfaction     | Natural mixed smells      | Sterile/chemical              |
| Gustation     | Whole foods varied        | Ultra-processed supernormal   |
| Touch         | Frequent affective        | Sparse, minimal affective     |
| Kinesthetic   | 8-15 km/day varied        | Sedentary 8+ giờ              |
| Sleep         | Natural light-entrained   | Artificial late, fragmented   |
| Hormonal      | Cyclical + recovery       | Chronic stress, no recovery   |
| Self-signal   | Mirroring development     | External attention demand    |

**Evolution lag**: body reward system calibrated cho ancestral range,
currently operating trong environment where baselines cannot be met
simultaneously. Explains much of modern chronic condition epidemic
(burnout, depression, chronic pain, metabolic syndrome, insomnia,
addiction — all forms of L1 deviation accumulation).

Framework reference point: when asking "what SHOULD body-input state
be?", ancestral baseline = reference answer. Không nostalgic idealization
— empirical reference for what body was designed to handle. Modern
design should respect this baseline where feasible.

### §5.2 Individual baseline (developmental calibration)

**Mô hình**: individual development shifts baseline within evolved
range via repeated exposure + neural adaptation + receptor sensitivity
adjustment + behavioral habituation. Mỗi person builds own baseline
profile khác nhau dù sharing same species architecture.

#### §5.2.1 Four sub-mechanisms operating simultaneously

**(i) Neural adaptation**: sensory cortex + subcortical structures
adjust response curves based on exposure history. Example: prolonged
bright light → cone sensitivity shifts, dim environments require
adjustment period. Documented across all sensory modalities.

**(ii) Receptor sensitivity adjustment**: down-regulation của receptors
với sustained ligand exposure, up-regulation với reduced exposure.
Classic drug tolerance mechanism, applies universally to neurotransmitter
+ hormone signaling. Basis for hedonic treadmill ở biochemical level.

**(iii) Behavioral habituation**: learned prediction của input →
anticipatory response → felt quality của input changes. Example:
expected noise doesn't startle like unexpected noise even at same
amplitude. Predictive processing framework (Seth, Clark) — brain
subtracts predictions from actual signal to focus on surprise.

**(iv) Schema-level calibration**: PFC compiled schemas về "normal"
state shape how body-inputs are interpreted. Cultural vocabulary cho
emotions shapes emotional perception (Barrett constructed emotion
theory). Language affects perceptual categories (linguistic
relativity weak form).

Tất cả 4 mechanisms operating simultaneously across all body-input
categories. Individual baseline = result của integrated adjustment
across levels.

#### §5.2.2 Examples per input category

**Auditory baseline shift**:
Person raised trong urban noise → auditory baseline shifted toward
tolerating high amplitude → rural silence feels uncomfortable initially
("quá yên tĩnh"). Person raised trong quiet rural → urban feels
overwhelming ("quá ồn"). Neither is "normal" or "abnormal" — both
within evolved range but individually calibrated.

**Touch baseline shift**:
Abundant infant/childhood touch → secure affective touch baseline →
adult seeks + receives comfortably. Touch-deprived childhood → baseline
shifted toward either avoidance (trauma pattern) hoặc hyper-seeking
(compensation pattern). Romanian orphan research documented permanent
developmental effects — critical period calibration.

**Gustation baseline shift**:
High-sugar diet từ childhood → sweet baseline elevated → fruit tastes
bland, need more concentrated sugar. Whole food diet từ childhood →
sweet baseline lower → processed food "too sweet." Cultural cuisine
exposure shapes adult preferences dramatically.

**Olfactory baseline shift**:
Cultural exposure creates "normal" smell baseline — Vietnamese nước
mắm, Korean kimchi, French aged cheese, Scandinavian lutefisk. Adults
encountering outside cultural baseline perceive as unpleasant (Rozin
disgust research). Adult can learn new cuisines nhưng initial baseline
takes years to shift.

**Self-signal interoception baseline shift** (§4.9):
Developmental caregiver mirroring creates interoceptive reading
baseline. Well-mirrored child → adult với strong self-signal capacity.
Alexithymic parents hoặc helicopter parenting (B15) → child with
blunted self-signal baseline — adult interoceptive rehabilitation
possible but difficult.

**Thermal baseline shift**:
Childhood climate exposure shapes thermal comfort range. Tropical
childhood → narrow cold tolerance. Arctic childhood → extensive cold
tolerance. Adult transitions take years.

#### §5.2.3 Developmental critical periods

Một số baselines **locked during critical periods**:

- **Native language phoneme perception**: Kuhl 1992 native language
  magnet effect, largely fixed by age 7-10. Adult learners retain
  accent.
- **Color category perception**: shaped by language vocabulary early,
  more flexible than phonemes but still developmental
- **Face processing preferences**: visual experience early life shapes
  adult recognition (own-race effect, face-race learning during infancy)
- **Attachment style**: ~age 1-3 caregiver interaction establishes adult
  bonding patterns (Ainsworth, Bowlby)
- **Taste preferences foundation**: early feeding (breast milk, first
  solid foods) establishes baseline tolerance
- **Interoceptive reading** (§4.9): early caregiving provides foundation,
  adult training can only partially compensate
- **Circadian chronotype**: genetic + early environment, relatively
  fixed adulthood (PER/CLOCK gene variants)

Critical period closure = baseline less flexible. Adult exposure shifts
baseline, nhưng không freely như during critical period. Implication
for parenting: early environment shapes adult body-base foundation
architecture.

#### §5.2.4 Cumulative exposure effects

Unlike acute events, baseline shifts **accumulate over time**:
- Years của urban life cumulate auditory baseline shift
- Decades của sedentary work cumulate kinesthetic baseline lowering
- Sustained high cortisol cumulates hormonal baseline shift
- Chronic processed food cumulates metabolic baseline shift
- Extended touch deprivation cumulates affective touch baseline alteration

**Pattern**: small changes × sustained time = large shift. Individual
doesn't notice day-to-day shift, but total shift over decades dramatic.
Explains tại sao B1 workaholic burnout appears "sudden" after 5-20
years — cumulative baseline drift reached crisis threshold.

#### §5.2.5 Variation explanation (§13.3 Example reframed)

Body-Base-Example.md §13.3 finding: "channel existence universal,
individual calibration variable." B20 asexuality extreme, B46 Proenneke
solo 30 năm, B50 solitary crash in days. Reframe interpretation:

- **Species-universal architecture** = evolved body-inputs (§5.1)
- **Individual-specific calibration** = personal baseline within
  evolved range (§5.2)
- **Variation location**: at **baseline level**, không ở "channel
  existence" level

B20 asexual individual không "missing sexual channel" — có evolved
hormonal + arousal architecture, but baseline calibrated such that
no sexual partner needed cho homeostatic comfort. B46 Proenneke không
"missing social channel" — social architecture intact, baseline
calibrated such that low-frequency contact suffices. B50 solitary
crashes fast because baseline calibrated cho regular social contact
baseline.

Reframe gives **cleaner explanation**: species-universal architecture,
individual-specific calibration. Variation at **substrate (baseline)
level** thay vì "primitive (channel existence)" level.

Đây là one of strongest parsimony gains của reframe: explains §13.3
finding more cleanly than channel framework could.

### §5.3 Novelty as baseline shifter

**⭐ CORE MECHANISM OF REFRAME**. Section này giải thích how baselines
shift — the mechanism that makes "quality channels" trong mô hình cũ
**emerge without needing to be primitives**.

#### §5.3.1 Delta rule — the baseline update formalism

Formally:

```
  BL(t+1) = BL(t) + α × (input_quality(t) - BL(t))

  where:
    BL(t)            = current baseline at time t
    input_quality(t) = input quality at time t
    α                = learning rate (depends on input category)
    BL(t+1)          = updated baseline
```

Đây là **delta rule** — standard learning theory formalism (Rescorla
& Wagner 1972), originally formulated cho classical conditioning,
applied broadly trong perceptual adaptation research (Helson 1964
adaptation-level theory).

**Key properties**:
- **Positive delta** (input > baseline): baseline moves upward toward
  input level
- **Negative delta** (input < baseline): baseline moves downward toward
  input level (nhưng asymmetric — see §5.4)
- **Learning rate α varies by input category**:
  - Olfactory: very fast (minutes cho receptor, weeks cho baseline)
  - Visual: moderate (weeks-months)
  - Gustation: dramatic (days-weeks, Hall 2019 evidence)
  - Hormonal: slow (weeks-months), but profound
  - Sleep/circadian: moderate (days-weeks shift work studies)
  - Self-signal: slowest (years, often developmental-locked)
- **Iterative**: each exposure moves baseline incrementally, accumulates

Delta rule foundation từ Helson 1964 "adaptation-level theory" — direct
theoretical predecessor cho baseline concept across psychology +
neuroscience.

#### §5.3.2 Novelty drive as the engine

Novelty drive (L3 — existing framework Novelty.md) fires on **positive
prediction error** — detected deviation above expected baseline.

**Mechanism sequence**:
1. Body detects input quality via receptors (§2-§4)
2. Compares current input to baseline expectation (predictive processing)
3. Nếu input > baseline → **positive prediction error** → VTA dopamine
   fire → reward signal → seek repeat
4. Repeated exposure → baseline shifts upward (delta rule)
5. Baseline elevated → same input now AT baseline → no prediction error
   → no reward
6. Seeking escalation để re-experience positive prediction error
7. **Hedonic treadmill established**

Đây là **the same mechanism** underlying:
- **Addiction escalation**: dose tolerance, need higher doses cho same
  effect (neuroadaptation research extensive)
- **Hedonic adaptation trong happiness research**: lottery winners
  return to baseline happiness (Brickman, Frederick)
- **Novelty-seeking behavior**: Berlyne optimal novelty, Zuckerman
  sensation seeking
- **Supernormal stimulus attraction**: Tinbergen 1951 original research,
  Barrett 2010 modern applications
- **Mere exposure effect**: Zajonc 1968 — repeated exposure shifts
  preference
- **Limerence → mature bond transition**: Fisher fMRI research —
  dopamine baseline habituation

**Framework claim**: these aren't separate phenomena — they're all
**manifestations của the same baseline-shifting mechanism** operating
on different body-input categories. Reframe unifies chúng under one
mechanism.

#### §5.3.3 Examples across all body-input categories

Reframe applies baseline shifting to every input:

**Vision (§2.1)**:
- Instagram/HD screens → elevated visual baseline → unadorned reality
  feels dull
- Art gallery exposure → aesthetic baseline shifts → "untrained" eye
  returns less reward
- Urban density → static visual fatigue

**Audition (§2.2)**:
- Produced music mastered + compressed → elevated acoustic baseline →
  unmixed live music feels flat
- Constant earbud use → silence baseline shifted → "quá yên tĩnh"
- Musicians trained ear → complex harmonic baseline elevated

**Olfaction (§2.3)**:
- Perfume regular use → own scent baseline elevated → over-applying
- Cigarette smoking → olfactory baseline degraded, tolerance cho own
  smoke
- Processed food smells engineered → natural food smells bland

**Gustation (§2.4)**:
- **Hall 2019 NIH** is direct experimental evidence: ultra-processed
  vs whole food diet, same macros offered, participants ate **500
  kcal/day more** on ultra-processed. **Direct measurement của baseline
  distortion mechanism**.
- High-sugar diet → fruit tastes bland
- High-salt diet → fresh food tastes unsalted
- Umami exposure → natural taste feels empty

**Tactile (§2.5)**:
- Silk wear → cotton feels rough (user's own example)
- Climate control constant → narrow comfort range
- Frequent affective touch → baseline elevated, deprivation acute →
  hedonic treadmill trên bonding system (B13 love addict pattern)

**Kinesthetic (§3.3)**:
- Exercise regular → fitness baseline elevates, previous challenges
  feel easy, need more cho same reward
- Ultra-endurance athletes → normal effort under-stimulating (B10)
- Sedentary → low baseline, movement feels difficult initially

**Sleep (§4.8)**:
- Caffeine regular → adenosine receptor upregulation → cần caffeine
  cho baseline function
- Late blue light → melatonin baseline shifted

**Hormonal (§4.7)** — **strongest empirical evidence**:
- Dopamine supernormal stimuli (processed food, social media, drugs)
  → baseline shifted → natural rewards insufficient
- Chronic stress → cortisol baseline shifted → "normal" feels stressful
- Oxytocin bonding → deprivation acute, hedonic treadmill
- **All major addictions** reflect hormonal baseline shifting gone wrong
  — direct empirical validation

**Self-signal interoception (§4.9)**:
- Meditation training → elevated awareness baseline
- Trauma suppression → low baseline, reconnection difficult

**Pattern across all examples**: **baseline shifting mechanism is
universal** across body-input categories. Không special property của
"quality channels" — basic feature của how sensory/physiological systems
adapt to environment.

#### §5.3.4 "Quality channels" dissolve into baseline-shifted L1

**Core theoretical claim**: mô hình cũ "quality channels" (silk vs
cotton, gourmet vs rice, music vs noise) **are not distinct channels**.
They are **L1 body-inputs at above-baseline quality**, với Novelty
operator firing → baseline shifts.

Không cần "quality" as framework primitive. Quality IS:
- Input quality at moment t
- Delta vs personal baseline
- Novelty-driven feedback seeking further above-baseline inputs

Đây là **removing a framework primitive** (L2 quality layer) — Occam's
razor parsimony gain.

Body-Base.md §4.2 "Silent/Slow-Decay Channels" (labeled "NEW FRAMEWORK
CONTRIBUTION") reframe như **body-input aggregates operated on by
Novelty**. The "contribution" was identifying the phenomenon correctly,
không necessarily explaining it. Reframe provides explanation at
substrate level.

#### §5.3.5 Research foundation (cornerstone citations)

- 🟢 **Helson, H. (1964)**. "Adaptation-Level Theory: An Experimental
  and Systematic Approach to Behavior" — direct theoretical foundation
  cho baseline concept, formalized mechanism across perceptual domains
- 🟢 **Rescorla, R. & Wagner, A. (1972)**. Classical conditioning
  learning rule — basis cho delta rule applied here
- 🟢 **Brickman, P. & Campbell, D.T. (1971)**. "Hedonic relativism and
  planning the good society" — foundational hedonic treadmill hypothesis
- 🟢 **Frederick, S. & Loewenstein, G. (1999)**. "Hedonic adaptation"
  comprehensive review — documents adaptation across wellbeing, wealth,
  health, life events
- 🟢 **Lykken, D. & Tellegen, A. (1996)**. "Happiness is a stochastic
  phenomenon" — set point theory, wellbeing returns to baseline
- 🟢 **Tinbergen, N. (1951)**. "The Study of Instinct" — supernormal
  stimulus foundational (birds prefer giant eggs, fish prefer brighter
  mates)
- 🟢 **Barrett, D. (2010)**. "Supernormal Stimuli" — Tinbergen principle
  applied to modern human environments (food, sex, media, gambling)
- 🟢 **Zajonc, R.B. (1968)**. Mere exposure effect — repeated exposure
  shifts preference
- 🟢 **Berlyne, D.E. (1960)**. "Conflict, Arousal, and Curiosity" —
  optimal novelty inverted-U curve
- 🟢 **Schultz, W.** dopamine prediction error research — VTA encoding
  reward prediction error, không absolute reward. Neuroscience
  confirmation của delta rule operating trong reward system
- 🟢 **Kahneman, D. et al.** Wealth-happiness plateau research — hedonic
  adaptation empirical documentation
- 🟢 **Wilson, T. & Gilbert, D.** "Affective forecasting" — people
  systematically overestimate lasting effect của positive + negative
  events → "impact bias" từ underestimating baseline adaptation
- 🟢 **Thaler, R.** Endowment effect + reference point economics —
  behavioral economics parallel đến baseline concept
- 🟢 **Fisher, H.** fMRI limerence research — dopamine baseline
  habituation trong relationships

**Note quan trọng**: baseline shifting mechanism là **extensively
documented trong independent research traditions** (psychophysics,
learning theory, economics, neuroscience, wellbeing research, addiction
research). Reframe KHÔNG inventing new mechanism — synthesizing
established research into one core mechanism cho body-base framework.
Đây là major confidence factor cho reframe validity.

#### §5.3.6 Connection to existing Novelty.md framework file

Reframe không replace Novelty.md — **clarifies its role** trong updated
architecture.

**Mô hình cũ**: Novelty là one of three pattern drives (với Status,
Protect) at L3 trong framework.

**Mô hình mới**: Novelty drive = **L3 operator acting on L1 body-input
baselines**. Novelty.md describes the drive's characteristics (individual
variation via DRD4 gene, developmental trajectory, pathological patterns,
cultural variation). Reframe specifies **what Novelty drive operates
ON** = L1 body-input baselines.

Updates for Body-Base.md integration:
- Novelty drive = L3 operator, không L3 "layer of needs"
- Operates on body-input baselines via delta rule
- Generates hedonic treadmill effects across all input categories
- Explains "quality channel" phenomena without needing L2 primitive
- Novelty.md content remains valid; framework positioning updated

Đây là an example của how reframe integrates với existing framework
files — không discarding, re-positioning within cleaner architecture.

### §5.4 Decay of adaptation

**Core asymmetry**: baseline **shift UP** (adaptation) nhanh hơn
baseline **shift DOWN** (de-adaptation). Explains nhiều phenomena
trong reframe + existing framework.

#### §5.4.1 Two decay patterns

**Pattern A — Input removed → baseline stays elevated temporarily →
dissonance at new expected floor**:

- Silk → cotton: cotton feels rough because baseline didn't reset
  instantly
- Gourmet → rice: rice tastes bland because gustation baseline elevated
- High-end coffee → instant: instant tastes weak
- Smartphone screen → old monitor: old feels dim, low-resolution
- Affective touch frequent → deprivation: painful absence (B13 pattern)
- Music produced compressed → natural sound: feels thin

Over time (weeks-months depending on input), baseline re-adapts downward,
removed input no longer causes dissonance. **Rate varies by input
category**:
- Olfactory: fastest (days-weeks)
- Visual: weeks-months
- Gustation: weeks-months (Hall 2019 and follow-ups)
- Hormonal: months-years
- Sleep/circadian: weeks
- Self-signal: slowest (years, often developmental-locked)

**Pattern B — Input continuously at high level → habituation → no longer
reward, becomes new floor**:

- Gourmet every meal → no longer exciting, expected
- Constant silk → normal, nothing special
- Daily meditation → baseline elevated, normal state feels subtly off
- Constant affective touch → expected, absence acute
- Luxury accommodation routine → "deserved," no longer appreciated

Both patterns operate simultaneously. **Pattern A** explains "withdrawal"-
like dissonance after removal. **Pattern B** explains "diminishing
returns" phenomenon — tại sao new rewards don't satisfy as long as
expected (wealth trap, luxury habituation).

#### §5.4.2 Asymmetry: shift UP fast, shift DOWN slow

Empirical observation recurring across research domains:
- **Addiction recovery** takes months-years vs addiction development
  takes weeks-months (neuroadaptation research)
- **Weight loss maintenance** difficult because fat baseline reluctant
  to reset downward — body "defends" elevated baseline via metabolic
  adaptation (Ludwig research)
- **Fitness loss** faster than fitness gain (retired athletes decline
  trong weeks, training over months-years)
- **Tolerance buildup** (drugs, caffeine) faster than tolerance decay
- **Baseline mood elevation** từ meditation slower than mood drop from
  stress
- **Material standard elevation** stays preferred even after losing
  access (B2 billionaire crash pattern vs formerly-poor families who
  adapted)

**Pattern recurrent**: UP fast, DOWN slow. Không một domain xung đột
với this observation.

#### §5.4.3 Evolutionary logic cho asymmetry

Tại sao evolution favors this asymmetric pattern?

**Hypothesis**: evolutionary advantage goes to individuals who:
- **Quickly exploit new opportunities** (fast adaptation up to take
  advantage của new food source, new territory, new mate quality)
- **Slowly relinquish old assets** (slow adaptation down to maintain
  capacity nếu situation reverses, don't abandon high baseline
  prematurely)

Quick "up" = seizing opportunity. Slow "down" = maintaining capacity
in case conditions change. Both favor survival/reproduction.

Trade-off for modern humans: rapid supernormal exposure + slow recovery
= **progressive baseline drift upward** without clean reset opportunity.

**Consequences trong modern environment**:
- Engineered supernormal stimuli hijack "up" mechanism rapidly
- Recovery to ancestral baseline takes much longer than acquisition
- Modern humans rarely return fully to ancestral baseline before new
  supernormal exposure arrives
- **Cumulative effect**: population-level baseline drifts upward across
  generations (sugar tolerance, screen time tolerance, noise tolerance)

#### §5.4.4 Connection to Body-Base.md §7 "pattern fire + storage + decay"

Body-Base.md §7 outline proposes "pattern fire + storage + decay" model
cho slow-decay channels. Reframe interpretation:

- **Pattern fire** = input at above-baseline quality → Novelty drive
  fires → positive prediction error → dopamine reward
- **Storage** = baseline shifted upward, maintaining elevated expectation.
  "Storage" không phải separate phenomenon — nó **IS** elevated baseline
- **Decay** = slow re-baselining downward when input removed (Pattern A
  trong §5.4.1)

Cùng mechanism described in §5.3 + §5.4. Body-Base.md §7 concept was
correct at descriptive level, reframe provides **mechanism explanation**:
it's baseline adaptation operating asymmetrically at L1 level.

**Parsimony gain**: không cần "storage" as separate framework component —
storage IS elevated baseline. Không cần "pattern fire" as separate
mechanism — it's Novelty drive detecting positive delta. Reduction from
3 concepts (fire/storage/decay) to 1 (asymmetric baseline adaptation)
với same explanatory power.

#### §5.4.5 Practical implications

Reframe has practical implications cho body-base health recommendations:

**(i) Prevention > recovery**: once baseline shifted upward via
supernormal stimulus, return to ancestral baseline slow + difficult.
Better to prevent shift than recover từ shift.

**(ii) Gradual exposure**: shifting baseline in healthy direction takes
time. Dietary change, exercise habit, meditation practice all require
weeks-months cho baseline adjustment. Expecting immediate results sets
up failure.

**(iii) Environmental design > willpower**: nếu environment continuously
provides supernormal stimuli, baseline will drift upward regardless of
individual effort. §14.6 Example finding "environment > willpower"
validated through mechanism.

**(iv) Cultural/generational shifts cumulate**: collective baseline
drift (everyone more exposed to screens, processed food, chronic stress)
= population-level shift. Reframe has implications cho societal
environment design, not just individual choices.

**(v) Recovery periods matter**: sustainable practices include variation
+ rest cycles. §13.9 "sustainable compound signature" includes temporal
rhythm precisely because baseline adaptation requires recovery opportunity.

### §5.5 Threshold vs gradient revisited

Body-Base-Example.md **§13.7 finding**: "channels appear to operate với
both gradient và threshold characteristics, depending on channel type."
Reframe maps này cleanly to L0/L1 distinction.

#### §5.5.1 Threshold inputs (L0 territory)

**Threshold characteristic**: cross threshold → cease-function →
emergency response. Binary outcome relative to threshold, không graded
near threshold.

**Threshold inputs**:
- **Oxygen**: minutes without → cerebral hypoxia → death
- **Extreme body temperature**: hyperthermia >42°C / hypothermia <28°C
  → organ failure
- **Water**: days without → circulatory collapse
- **Food**: weeks without → metabolic failure
- **Critical injury**: immediate tissue damage → shock → organ failure
- **Extreme blood loss**: immediate
- **Suffocation, drowning, electrocution**: seconds

Đây là **L0 Alive threshold** inputs. Near threshold, signals are
**loud, universal, non-suppressible** — evolution ensured no false-
negatives. Mistakes at L0 = death, hence amplified signal strength.

**Signal properties**:
- Suppress all other processing (Body-Dissonance §2 emergency level)
- Single-track survival response
- Autonomic + amygdala + sympathetic dominance
- PFC can be bypassed

#### §5.5.2 Gradient inputs (L1 territory)

**Gradient characteristic**: deviation magnitude scales dissonance
linearly. Response intensity proportional to deviation từ baseline.

**Gradient inputs** (most L1 body-inputs):
- Sensory exteroception (vision, audition, olfaction, gustation, tactile
  — except extreme pain/damage)
- Proprioception, vestibular, kinesthetic
- Most interoception (cardiovascular, respiratory, visceral, hormonal,
  sleep, self-signal)
- Deviations trong middle range generate graded dissonance, không
  threshold

**Signal properties**:
- Softer, more nuanced
- Allow multitasking
- PFC participation + modulation possible
- Body-Dissonance §2 micro/nhẹ/trung levels map here

#### §5.5.3 Inputs với BOTH properties

Some inputs exhibit **threshold at extremes + gradient in middle range**:

**Oxygen**: normal breathing = gradient (fresh air quality vs stale
slight dissonance, §4.3 respiratory); deprivation = threshold (L0).

**Water**: moderate dehydration = gradient (thirst, headache, cognitive
decline); severe = threshold (L0 circulatory collapse).

**Food**: moderate hunger = gradient (discomfort, reduced function);
starvation = threshold (L0 metabolic failure).

**Temperature**: mild discomfort = gradient (warmer/cooler preferred,
§4.1); extreme = threshold (heat stroke / hypothermia L0).

**Nociception**: mild-moderate pain = gradient (uncomfortable but
functional, §4.2); extreme = threshold (shock, suppression of all
else, §2 emergency level).

**Sleep**: moderate deprivation = gradient (fatigue, cognitive decline);
extreme total sleep deprivation = L0 proximity (eventual death documented
trong sleep deprivation research).

Những inputs này demonstrate **gradient-to-threshold transition** as
magnitude increases. Framework should handle đây: same input category
spans L0 và L1 depending on magnitude.

#### §5.5.4 Reframe interpretation

**§13.7 Example finding** (threshold vs gradient channels) reframes as:
- Threshold = L0 territory (either side của survival threshold)
- Gradient = L1 territory (deviation magnitude scales response)
- Some body-inputs span both as magnitude varies

Maps cleanly to L0/L1 reframe distinction từ §1.2.1 và §1.2.2.
**Validates reframe's decision** to keep L0 + L1 distinct (không merge
into 2-layer model as user initially suggested).

Evidence basis: § 13.7 finding was derived from 50 Phase B cases, provides
empirical support cho L0/L1 separation. Reframe không introduces
artificial distinction — recognizes pattern already visible trong data.

#### §5.5.5 Implications cho crash speed formula

Body-Base-Example §13.7 observed: **"crash speed ∝ depth of multi-channel
starvation × acuteness of starved channels."**

Reframe interpretation:
- **Single-channel starvation at gradient range**: slow accumulation,
  gradual decline over months-years (B6 digital nomad năm 7-12 pattern)
- **Multi-channel simultaneous starvation**: faster crash từ compound
  effect (B50 solitary, B1 workaholic burnout final stage)
- **Threshold crossing (L0)**: immediate crisis regardless của other
  inputs (B48 McCandless starvation, B50 solitary crosses multiple L0
  risks simultaneously)

Formula approximation remains valid trong reframe:

```
  Crash speed ∝ (depth × breadth of starvation) + L0 proximity
```

Where:
- **Depth** = magnitude of deviation từ baseline (gradient territory)
- **Breadth** = number of simultaneously starved inputs
- **L0 proximity** = discrete bonus nếu any input approaches threshold

Reframe maintains Example's findings với cleaner mechanism. Crash speed
không separate phenomenon requiring explanation — it's integral result
của gradient vs threshold input behavior + baseline mismatch.

### §5.6 Tại sao baseline adaptation tồn tại (evolutionary explanation)

**Câu hỏi fundamental**: Tại sao baselines shift at all? Tại sao không
just fire reward every time silk được mặc? Tại sao không maintain fixed
expectation cho all inputs?

**Answer**: Because **detection of change matters more than detection
of absolute level** for survival.

#### §5.6.1 Information-theoretic logic

Animals need to notice **VARIATION** (predator appearing, food found,
weather shift, novel object, territory change), không compute absolute
values of ambient conditions. Sensory systems universally implement
**adaptation to baseline** because it **maximizes information extraction**
từ environment.

Nếu body fired reward constant cho every instance của safe environment,
signal would be saturated, novelty couldn't be detected, important
changes missed. **Baseline adaptation ensures**:
- **Above-baseline events** generate positive signal (opportunity
  detection)
- **Below-baseline events** generate negative signal (threat detection)
- **At-baseline events** generate little signal (homeostatic "normal")

Đây maximizes information từ limited neural bandwidth. Same logic applies
across sensory modalities + interoceptive + hormonal systems.

**Classical neuroscience findings supporting this**:
- **Retinal ganglion cells** respond to **contrast** (change từ
  background), không absolute brightness
- **Auditory cortex** respond to **frequency changes** + **onset/offset**,
  không steady tones
- **Interoception** respond to **deviations** từ homeostatic set point,
  không absolute body state
- **Dopamine VTA** encodes **prediction error**, không absolute reward
  (Schultz foundational research)

**Baseline adaptation là fundamental property** của how nervous systems
process information, không something special to "quality channels."
Universal feature của neural architecture.

#### §5.6.2 Evolutionary tradeoff

Adaptation brings **survival benefits**:
- Survive trong varied environments (arctic, desert, tropical, alpine,
  marine, forest)
- Exploit new food sources when encountered (omnivorous flexibility)
- Adjust to seasonal variation automatically
- Adjust to social/territorial changes
- Rapid response to environmental shifts without genetic change needed

Nhưng creates **chronic chasing behavior**:
- **Hedonic treadmill** (Brickman, Frederick, Lykken set point research)
- **"Never satisfied"** phenomenology across contemplative traditions
- **Rapid return to subjective baseline** after positive events
- **Affective forecasting errors** (Wilson & Gilbert impact bias)
- **Addictive escalation** possible when supernormal stimuli encountered

**Tradeoff is not a design flaw** — it's the cost of having an adaptive
system at all. Fixed responses would fail trong varied environments;
adaptive responses succeed trong variation but create treadmill side
effect.

#### §5.6.3 Documented evidence across research domains

**Wealth-happiness plateau** (Kahneman 2010, Diener research):
Lottery winners return to baseline happiness ~1 năm. Wealth beyond
basic needs doesn't sustainably elevate wellbeing. Accident victims
(including spinal cord injuries) also return somewhat toward baseline
— less than winners toward their baseline but more than expected.
Classic hedonic adaptation evidence trong real-world life events.

**Mastery keeps progressing** (B30 Jiro 99 năm "still not satisfied"):
Tại sao mastery never completes? Because skill achievement shifts
baseline — what was "advanced" yesterday is "baseline" today, need
harder challenges cho same reward. Body-Base-Example.md §13.9 finding
về unbounded mastery horizon = baseline shifting at skill level.

**Food gets boring without variation**:
Constant same food loses reward despite nutritional adequacy. Baseline
shifts, novel variations required cho reward firing. Cultural cuisines
developed infinite variety partially cho này reason. Also explains tại
sao "forbidden fruit" taste better than commonly available.

**Wealth trap** (B2 billionaire post-success emptiness):
Money can elevate standard của living → L1 body-inputs improved →
initial reward. Over time, elevated standard becomes baseline → no
longer rewarding. Seeking further wealth provides less incremental
reward. Crash when goal reached và baseline drifts beyond reachable
further gains.

**Relationship limerence → mature bond transition**:
Fisher fMRI research documented limerence = dopamine baseline elevation
cho specific person. Over months, baseline habituates, dopamine response
reduces. Mature bond operates on different neural substrate (oxytocin,
vasopressin) không requiring constant novelty. Relationships that depend
on limerence phase cannot sustain — baseline adaptation inevitable.

**Addiction tolerance**: direct pharmacological evidence của baseline
shifting. Drug dose requires escalation over time để maintain same
effect. Receptor downregulation measurable. When drug removed, withdrawal
= dissonance từ elevated baseline minus current (zero) input.

**Blue Zone longevity patterns** (B9 case): populations với stable
traditional environments show better wellbeing outcomes — possibly
because baselines don't drift continuously, stable reference allows
steady-state function. Modern comparison: rapid environmental change
prevents baseline stabilization.

#### §5.6.4 Framework implications

Reframe doesn't treat baseline adaptation as "bug" to fix — it's
**fundamental feature** của nervous system architecture. Framework
should:

**(i) Acknowledge adaptation as inevitable**: không promise permanent
happiness elevation, không claim interventions can bypass adaptation
dynamics. Honest framework.

**(ii) Design environments respecting adaptation dynamics**: ancestral-
adjacent environments where baselines can stabilize healthily.

**(iii) Build sustainable practices với variation + recovery cycles**:
§13.9 Example sustainable compound signature includes temporal rhythm
và recovery — because those respect adaptation dynamics.

**(iv) Avoid engineering supernormal stimuli** that exploit adaptation.
Environment design matters more than individual willpower (§14.6
Example finding).

**(v) Foster ancestral-adjacent environments** where baselines stable
+ healthy. Reference point for healthy design.

Trying to achieve **permanent elevated subjective state** = fighting
neural architecture. Framework should instead build practices that work
**với** adaptation dynamics.

Points to Body-Base.md §13 integration framework — sustainable compound
signature (§13.9 Example) includes variation + recovery cycles precisely
because those respect adaptation dynamics. Pathological patterns (B1
workaholic, B10 ultra-marathon, B21 religious fanatic, B31 food, B35
screen) all violate adaptation rhythms, cumulative consequences predictable.

---

**§5 BASELINE ADAPTATION MECHANISM — section complete**

6 sub-sections covering theoretical core của reframe. Key findings:

**1. Evolved baselines are compiled survival wisdom** (§5.1) —
species-universal architecture từ 2M năm calibration

**2. Individual baselines shift within evolved range** (§5.2) via 4
mechanisms (neural adaptation, receptor sensitivity, habituation,
schema calibration) — explains §13.3 Example variation finding

**3. Novelty operator as baseline shifter** (§5.3) — core reframe
mechanism với extensive independent research validation (Helson,
Brickman, Frederick, Tinbergen, Zajonc, Berlyne, Schultz, Kahneman,
Wilson & Gilbert, Fisher)

**4. Asymmetric decay** (§5.4) — UP fast, DOWN slow, explains Body-
Base.md §7 "pattern fire + storage + decay" với cleaner mechanism
(parsimony gain)

**5. Threshold vs gradient** (§5.5) — maps §13.7 Example finding to
L0/L1 distinction, validates reframe layer structure

**6. Evolution explanation** (§5.6) — baseline adaptation is fundamental
information-processing feature, không "bug"; framework should work
với adaptation, không against

Reframe §5 assessment: **mechanism coherence PASSES test criterion
§1.4.1(2)** — delta rule + Novelty operator + asymmetric decay provide
coherent theoretical foundation với extensive independent research
support.

Ready for §6 PFC drives acting on body-inputs.

---

## §6 — PFC DRIVES ACTING ON BODY-INPUTS

### §6.1 Novelty drive

Mechanism của Novelty drive đã được covered trong §5.3 (baseline shifter).
Section này elaborates Novelty as PFC drive specifically, không phải
body-input.

#### §6.1.1 Novelty drive properties

**Novelty drive là L3 operator, không body-input**:
- Không có dedicated receptor cho "novelty"
- Fires on **prediction error** (Berlyne optimal novelty theory, Schultz
  dopamine prediction error research)
- Mechanism: VTA dopamine neurons encode positive prediction error →
  motivational signal → seek repeat
- Operates **ACROSS all body-input categories** — mọi input (§2-§4)
  có thể là novelty target

**Core function**: Novelty drive detects above-baseline input quality,
fires reward, drives seeking, ultimately shifts baseline upward via
delta rule (§5.3). Mechanism covered there.

**Section này focuses on Novelty as drive characteristics** — how it
operates as PFC construct rather than L1 substrate.

#### §6.1.2 Novelty drive behaviors

Novelty drive manifests across domains:
- **Curiosity/exploration**: seeking new information, new environments
- **Mastery pursuit**: skill progression (baseline shifts với competence)
- **Travel/variety seeking**: new places, new foods, new experiences
- **Creative work**: generating novel patterns, combinations
- **Learning**: acquiring new chunks (Melody-Arc.md arc dynamics)
- **Relationship novelty**: limerence, new romantic intensity
- **Consumption novelty**: variety trong food, fashion, entertainment
- **Thrill seeking**: extreme sports (B7), vestibular novelty

Each domain represents Novelty drive operating on different body-input
category. **One drive, many expressions**.

#### §6.1.3 Individual variation

- **DRD4 gene variants**: 7-repeat allele associated với novelty seeking,
  migration patterns (higher frequency trong populations with historical
  migration)
- **Temperament**: Kagan high-reactive vs low-reactive infant research
  predicts adult novelty tolerance
- **Zuckerman Sensation Seeking Scale**: individual differences
  measurable, 4 dimensions (thrill, experience, disinhibition, boredom
  susceptibility)
- **Developmental trajectory**: Novelty seeking peaks adolescence, declines
  gradually with age (evolved pattern — youth explores, elders maintain)
- **Clinical spectrum**: extreme high (ADHD, novelty addiction, sensation
  seeking pathology) to extreme low (depression anhedonia, rigid
  behavioral patterns)

Framework reference: Novelty.md existing file covers these dimensions.

#### §6.1.4 Pathological patterns when Novelty drive hijacked

**Supernormal stimulus exploitation**: when environment engineered to
provide rapid repeated above-baseline inputs, Novelty drive fires
continuously → baseline shifts rapidly → natural rewards insufficient
→ addiction pattern.

Cases:
- **B31 ultra-processed food**: food engineered supernormal → Novelty
  constantly fires → baseline shifts → overconsumption (Hall 2019 NIH
  evidence)
- **B35 screen addiction**: content engineered for constant novelty →
  attention hijacked → unmediated reality feels dull
- **B33 gambling**: reward unpredictability + supernormal stimulus →
  Novelty exploitation
- **B32 substance addictions**: dopamine system directly hijacked →
  Novelty drive bypassed biologically
- **B13 love addict**: limerence novelty supernormal → crash when faded
  → seek new limerence object

**Pattern**: Novelty drive is evolved for ancestral variety levels, does
không handle modern engineered supernormal environment well. Framework
concern (§14.6 Example "environment > willpower").

#### §6.1.5 Connection to existing Novelty.md

Mô hình cũ: Novelty là one of three pattern drives trong framework.

Mô hình mới: Novelty drive = **L3 operator acting on L1 body-input
baselines** via delta rule mechanism. Novelty.md file content remains
valid; framework positioning updated.

Updates cho Body-Base.md integration:
- Novelty drive = L3 operator (không "layer of needs")
- Operates on body-input baselines via delta rule từ §5.3
- Individual variation via DRD4, temperament, developmental history
- Exploitation via supernormal stimuli = major framework concern

Reframe integrates, không replace existing Novelty.md work.

### §6.2 Status drive

**⭐ Critical reframe claim**: Status là **NOT a body-input**. Status
là **PFC construct** that organizes social environment to amplify
hoặc protect L1 body-input supply. Đây là **explicit resolution** của
tension §14.6 Example identified ("status/fame/wealth as PFC proxies").

#### §6.2.1 Status mechanism — how PFC construct proxies L1 access

Status operator organizes social environment via several mechanisms:

**(i) Community position → reliable agent co-presence inputs**:
- Higher status individual has more social contact (voices, faces, touch)
- Lower status isolated individual has less contact → L1 agent co-presence
  aggregate (§8 mapping) starved
- Evolution link: ancestral low-status = less group protection + resources
  → actually dangerous. Status seeking was survival-relevant.

**(ii) Reputation → resource access → guaranteed metabolic inputs**:
- Status provides access to food, water, shelter
- Reputation in social group correlates với resource allocation
- Losing reputation → resource loss → L0/L1 threat
- Ancestral modern: money/wealth = reputational proxy cho resource
  access guarantee

**(iii) Dominance → protection từ L1 threats**:
- Dominant position deters predators (human + other)
- Territorial protection secured
- Physical safety correlates với rank in group hierarchies

**(iv) Attention/recognition → agent mirroring inputs**:
- Being recognized → agent eye contact, faces oriented toward you →
  visual agent input fed
- Being acknowledged → voice response → auditory agent input fed
- Being praised → via Empathy-Mirror → mirrored positive states →
  oxytocin/dopamine proxy feed

**(v) Status trajectory → predictable L1 supply**:
- Ascending status → increasing body-input security
- Descending status → anticipated loss triggers stress response
- Stable status → homeostatic calm

#### §6.2.2 Tại sao status FEELS like a need

Nếu status is PFC proxy không body-input, tại sao chúng ta FEEL it as
powerful as body-input needs?

**Answer**: Status reliably CONVERTS to body-input access, so PFC learns
to seek status as proxy signal. Over development, PFC couples status
perception tightly to L1 access prediction → status itself becomes
motivationally compelling dù không direct receiver.

**Mechanism**:
1. Infant learns caregiver acknowledgment correlates với food, warmth,
   touch (direct L1 access)
2. Child learns group acceptance correlates với safety + resources
3. Adolescent learns social rank correlates với mate access, opportunity
4. Adult generalizes to abstract status markers (money, fame, power)
5. PFC now treats status markers as predictive của L1 supply
6. Seeking status fires reward pathway dù direct L1 fed không occurs

**Result**: status feels like a primary need nhưng actually operates
at one level abstraction từ direct body-input supply.

**Failure mode**: nếu status achieved WITHOUT L1 payoff → empty feeling
(B2, B36, B38). This is diagnostic của PFC proxy mechanism — body-base
không fed directly, expectation violated.

#### §6.2.3 Evidence từ documented status research

**Marmot Whitehall Studies**: British civil servants, lower occupational
grade → higher all-cause mortality, heart disease. Controlled for income,
diet, smoking. Lower status → chronic stress → cortisol → L1 cardiovascular
+ immune suppression → actual L1 damage. Documents status → L1 pathway
mechanism.

**Sapolsky baboon research**: Dominance hierarchy in wild baboons →
cortisol patterns, reproductive success, health outcomes. Subordinate
males chronic stress, dominant males different stress profile. Ancestral
evidence for status → L1 linkage.

**Boehm egalitarianism research**: Hunter-gatherer societies actively
suppress excessive dominance. Suggests status hierarchies are evolved
concern, cultures evolved counter-mechanisms. Status drive is real +
potent enough to require cultural management.

**Sapolsky "Behave"**: integrated review của status neuroscience +
behavior research.

#### §6.2.4 §14.6 Example finding resolved

Body-Base-Example.md §14.6 finding: "Status/fame/wealth/power as PFC
proxies... body-base has no direct receiver for them."

Reframe resolves tension explicitly:
- **Status/fame/wealth/power = PFC operators**
- **Organized to proxy L1 access**
- **Not body-inputs themselves**
- **Direct pursuit without L1 payoff = emptiness**

**Cases validating**:
- **B2 billionaire post-wealth emptiness**: wealth achieved → status
  satisfied → BUT L1 body-inputs not auto-fed by wealth → emptiness.
  Status drive fired reward prediction, L1 reality didn't follow.
- **B36 fame seeker emptiness**: fame achieved → recognition everywhere
  → BUT parasocial mirrors don't provide depth → L1 intimate bonding
  starved despite max attention.
- **B38 power obsession**: control over agents → status satisfied →
  BUT L1 bonding compromised by dominance dynamics (fear-based không
  affective).
- **B40 Rothschild multi-generational dynasty**: status trajectory
  spanning generations → value comes từ L1 proxying cho descendants,
  không status itself. Sustainable because grounded trong real L1
  outcomes (family security, knowledge transmission).
- **B5 karoshi / workaholic burnout**: status pursuit via work hours
  → group recognition → BUT L1 sleep/rest/social/movement all starved
  simultaneously → eventually crashes.

#### §6.2.5 Connection to Drive.md existing framework file

Drive.md (existing framework) describes 3 drives broadly. Reframe
specifies **Status drive's mechanism**: organizes social environment
để proxy L1 access.

Updates for framework:
- Status drive = L3 operator, không body-need
- Operates via social environment organization
- Proxies L1 access through 5 mechanisms (§6.2.1)
- Pathological when pursued without L1 payoff (empty status)
- Healthy when grounded trong actual L1 outcomes (B27 craftsman status
  within community + L1 craft + transmission)

Drive.md content remains valid; Status drive re-framed at mechanistic
level.

### §6.3 Protect drive

Protect drive guards L1 body-inputs từ threats. **Critical property**:
operates at multiple scales, extends via Empathy-Mirror to include
others' body-states.

#### §6.3.1 Protect drive scales

Protect drive operates across several scales:

**(i) Self-protection**: avoiding direct body damage
- Reflex responses (withdrawal từ pain, startle, fear)
- Risk avoidance behavior
- Seeking shelter, food security, warmth
- Self-care practices (hygiene, exercise, rest)

**(ii) Extended self**: offspring, family, in-group
- Parental investment (strongest documented instinct)
- Family protection
- Tribal/community protection
- Kin-directed behavior (Hamilton inclusive fitness)

**(iii) Empathy-Mirror level** — mirrored body-states của others trigger
protect drive extending
- Seeing vulnerable infant → protect response despite không own child
- Seeing injured person → helping response
- Seeing suffering → relief seeking (hence charitable giving)
- Seeing threatened community member → defensive response

#### §6.3.2 Critical integration với Empathy-Mirror.md

Empathy-Mirror.md đã establish **empathy là mechanism**: body creates
mirror (bản sao weaker) của other's body-state trong own body. The
mirrored state fires own L1 body-inputs at lower intensity than actual
experience but real enough to generate motivational response.

**Protect drive + mirror integration**:

1. Observe other sinh vật in some body-state (suffering, hungry, cold,
   threatened)
2. Empathy-Mirror creates weak copy trong own body — mirrored sensory
   + visceral + hormonal state (§4.1-§4.9 replicated at lower amplitude)
3. Own L1 body-inputs fire (weaker but real) → dissonance signal
4. Protect drive activates to resolve dissonance → but target is OTHER's
   state
5. Action: help other → their L1 resolves → mirror updates → own L1
   dissonance resolves
6. Reward: mirrored resolution fires reward pathway → positive feedback
   loop cho helping behavior

**Critical insight**: protect-other behavior không mysterious altruism
— it's **self-maintenance via mirrored state resolution**. Helping
other = feeding own L1 via mirror mechanism. Elegant framework
integration.

#### §6.3.3 "Giúp bộ đội có gạo" phenomenon — bạn đặt câu hỏi này

Bạn đã hỏi trong earlier session: "tại sao Protect chỉ bảo vệ body-base,
vậy sao lại empathy? căm thù quân giặc xâm lược, tin tưởng vào Bác Hồ,
tin tưởng vào tự do dân tộc, tin tưởng vào làng xã tương lai đẹp hơn(trong
đó có chính mình) => thương yêu cho gạo bộ đội, không nhất thiết phải bộ
đội trực tiếp giúp gì mình."

Reframe explanation qua Protect + Empathy-Mirror mechanism:

1. **Empathy-Mirror with soldiers**: observe bộ đội suffering (hunger,
   cold, danger, exhaustion) → mirror creates weak copies in own body
   → own L1 dissonance fires
2. **Schema layer embedding**: "I am part of làng xã, future includes
   me, victory includes my L1 security" → bộ đội victory = L1 security
   for self
3. **Compound mirror + schema**: helping bộ đội via gạo = resolving
   mirrored dissonance + ensuring future L1 security via group
4. **Reward**: giving gạo generates reward (mirror resolution + Status
   reward group-based + Protect satisfaction) despite seeming "selfless"
5. **No magic**: behavior fully explained via existing mechanisms —
   body-input mirroring + Protect drive + schema-level extension
   ("we are one group")

**Không mysterious "altruism"**. Just body-input mirroring + Protect
drive + schema layer group extension. Framework explains via mechanism.

This also explains:
- **Parents sacrificing for children** — strong empathy mirror + direct
  kin investment + schema "my child's future"
- **Religious/cult giving** — empathy mirror + schema "we are one"
  + Status reward from group
- **Soldiers dying cho country** — empathy mirror + schema "protect
  family" + Status honor reward
- **Charitable giving to strangers** — empathy mirror của suffering +
  Status mild reward + schema "human family"

Không cần "true altruism" as framework concept. Everything reduces to
body-input mirroring + Protect drive + schema-level group extension.
**Parsimony gain**.

#### §6.3.4 Protect drive pathology patterns

When Protect drive malfunctions:

**Hypervigilance** (PTSD, chronic anxiety): threats detected where
không actual threats → chronic Protect activation → HPA axis
dysregulation → L1 cardiovascular/cortisol damage paradoxically
from over-protection

**Over-protection** (B15 helicopter parent): Protect drive applied
excessively → prevents child developing own L1 capacities (kinesthetic,
self-signal, resilience) → paradoxical damage

**Selective protection** (in-group vs out-group): Protect drive for
in-group + aggression toward out-group → tribalism, nationalism,
religious conflict. Evolved for small-group survival, scaled pathologically.

**Protective neglect** (avoidant attachment): learned detachment as
protection strategy → L1 affective touch starved paradoxically from
protective withdrawal.

**Codependent over-caring** (B11): protect extended without self-
protection → own L1 starved caring for others who take but don't
reciprocate → B11 pattern.

#### §6.3.5 Connection to Threat.md + Empathy-Mirror.md files

**Threat.md existing framework** covers threat detection mechanisms
(L0 immediate, L1 anticipatory, social threats). Reframe positions
Protect drive as L3 operator that **responds to threat detection**.
Threat.md describes what's detected; §6.3 describes what responds.

**Empathy-Mirror.md existing framework** covers mechanism của mirror.
Reframe integrates: mirror provides body-state replication, Protect
drive acts on mirrored state. Two files complementary — mirror does
replication, Protect does response.

Updates cho framework integration:
- Protect drive = L3 operator
- Operates on detected L0/L1 threats (from Threat.md)
- Extended via Empathy-Mirror to others' body-states
- Scales: self / kin / in-group / generalized empathy
- Pathological when over-applied or selective

Three existing files (Threat.md, Empathy-Mirror.md, + §6.3 Protect
drive here) form integrated protect subsystem in framework.

### §6.4 Summary: L3 as substrate operators, không layer

**Key reframe claim**: L3 drives **không exist AT a higher level above
L1**. They are **OPERATORS that act on L1 body-inputs**.

#### §6.4.1 Three operators summary

**Novelty operator** (§6.1):
- Shifts L1 baselines upward via delta rule mechanism
- Detects positive prediction error (above-baseline input)
- Fires VTA dopamine reward
- Drives exploration, mastery, variety seeking
- Operates across ALL body-input categories

**Status operator** (§6.2):
- Organizes social environment để proxy L1 access
- NOT a body-input itself — PFC construct
- 5 mechanisms: community position, reputation, dominance, recognition,
  trajectory
- Feels like a need because reliably converts to L1 supply
- Pathological when pursued without L1 payoff (B2, B36)

**Protect operator** (§6.3):
- Guards L1 từ L0/L1 threats detected
- 3 scales: self, extended self, empathy-mirror generalized
- Integrates với Empathy-Mirror.md mechanism
- Explains "altruistic" behavior via mirror + protect dissonance
  resolution
- Pathological when over-applied or tribalistic

#### §6.4.2 Tại sao "operators" không "layer"

Existing framework described L3 as "pattern drives" — functional role
description, không architectural layer.

**Mô hình cũ confusion**: "L3 pattern drives" sometimes implied separate
needs layer above L1 physiological. This tempted framework to treat
meaning, mastery, status, etc. as distinct body-base needs với own
crash patterns.

**Mô hình mới clarification**: L3 drives don't occupy a different
architectural layer với own receptors. They are PFC-level **operators**
acting on the same L1 substrate as direct sensory/interoceptive
processing.

**Functional difference, không architectural layer**:
- L1 receptors feed body-input signals upward
- L3 operators shape how body engages với environment để optimize
  L1 supply
- Both operate on same substrate, different functional roles

Parallel analogy: CPU và GPU in computer both process instructions,
different specialized roles, không "layers" of different computing.
Similarly L1 processes direct input, L3 processes optimization/
prediction/social dynamics — all ultimately serving L1 maintenance.

#### §6.4.3 Implications cho §14.6 Example finding

§14.6 Example identified tension: "Status/fame/wealth as PFC proxies,
not body-base channels." Mô hình cũ couldn't resolve cleanly — these
were treated as higher-order channels despite framework recognition
that they lack direct receivers.

**Reframe resolves**: status/fame/wealth operate via Status drive (L3
operator), không body-base channels. The distinction mô hình cũ felt
but couldn't express cleanly is made explicit in reframe architecture.

Same applies to meaning, mastery, identity, fame, wealth — **none
of these are body-input channels**. They are either:
- L3 operators (Novelty/Status/Protect)
- Schema-level constructs (meaning, identity)
- Compound pursuits that engage multiple L1 inputs via L3 operators

**Parsimony gain**: fewer primitives (no L2 quality, no higher-order
channels), cleaner architecture.

#### §6.4.4 What L3 drives do NOT do

Important clarifications:
- **Do không add new body-inputs**: they operate on existing L1
- **Do không have dedicated receptors**: all signal through L1 pathway
- **Do không generate independent reward**: reward fires through L1
  substrate (dopamine, oxytocin, endorphins — all reaching body state)
- **Do không provide alternative to L1 feeding**: ultimately all
  must ground in L1 supply, or empty (B2, B36 pattern)

When someone says "I need to feel meaningful," reframe interpretation:
schema-level coherence + L3 Status operator (recognition of contribution)
+ L1 feeding (via social engagement + mastery/kinesthetic + self-signal).
Meaning "need" reduces to schema + drives + L1 aggregate.

Healthy frameworks acknowledge L3 drives operate on L1 substrate, don't
replace it. Pathological frameworks treat L3 pursuits as substitutes
cho L1 feeding → crash patterns (most of Phase B 50 cases reflect this
mismatch).

---

## §7 — DISSONANCE RE-MAPPING

### §7.1 Body-Dissonance.md §2.5 six sources revisited

Body-Dissonance.md §2.5 documents **6 nguồn gây dissonance**. Reframe
re-maps chúng to clarify which operate at L1 body-input level vs schema
level.

#### §7.1.1 The 6 sources from existing framework

Từ Body-Dissonance.md §2.5:
1. **Information mismatch** (prediction error)
2. **Body-state delta** (homeostasis)
3. **Threat schema** (anticipate negative)
4. **Physical damage** (nociception)
5. **Social damage** (connection phá)
6. **Melody learning** (investment cost)

Reframe classification + detailed mapping:

#### §7.1.2 Source 2 — Body-state delta (L1 BODY-INPUT DIRECT)

**Existing definition**: "Body-need chưa met — đói, mệt, nóng, lạnh,
khát"

**Reframe mapping**: Đây chính là L1 body-input deviation below baseline,
**exactly** reframe's substrate mechanism. Mọi input trong §2-§4 generates
body-state delta dissonance khi deviate dưới baseline:
- Metabolic (§4.6): đói, khát → L1 dissonance
- Sleep (§4.8): mệt → L1 dissonance
- Thermoreception (§4.1): nóng, lạnh → L1 dissonance
- Respiratory (§4.3): dyspnea → L1 dissonance
- Hormonal (§4.7): cortisol high feeling "wired tired"
- Visceral (§4.5): bloating, nausea
- etc. (all interoceptive categories)

**Source 2 là explicit confirmation** that existing framework already
recognized body-inputs as dissonance substrate. Reframe doesn't
introduce new concept here — it makes explicit what was implicit.

#### §7.1.3 Source 4 — Physical damage (L1 NOCICEPTION or L0 THRESHOLD)

**Existing definition**: "Tissue damage — nociception (A-delta fast,
C slow)"

**Reframe mapping**: Direct match to §4.2 nociception category.
- **Mild-moderate damage** → L1 nociception gradient signal
- **Severe damage** → L1 → L0 territory (§5.5 threshold/gradient
  transition, shock response)
- Same neural pathway (A-delta + C-fiber), same receptors, same
  processing

No mapping difficulty. Source 4 là explicit L1 body-input dissonance
at nociception level.

#### §7.1.4 Source 5 — Social damage (L1 AGGREGATE + MIRROR DISRUPTION)

**Existing definition**: "Connection phá — bị reject, mất mặt, cô lập.
Social pain = physical pain pathway (Eisenberger 2003)"

**Reframe mapping** (more nuanced than Source 4):

Social damage không phải single L1 input. Nó là **aggregate of specific
L1 inputs going silent** + Empathy-Mirror mechanism disruption:

- **Loss of agent co-presence inputs**: voices, faces, touch, olfaction
  all reduced → aggregated L1 deficit
- **Loss of mirror reciprocity**: not being seen → own self-signal
  validation compromised (§4.9)
- **Hormonal shift**: oxytocin reduced, cortisol elevated (§4.7 chronic
  pattern)
- **Eisenberger 2003 finding** (social pain activates dACC same as
  physical pain) validates: social damage IS body-input dissonance,
  through aggregate mechanism
- **Nociception-like processing** because evolution repurposed pain
  pathway cho social threats (loss of group = death ancestral)

**Key reframe claim**: Social damage **không phải separate category**
— nó aggregate effect của specific L1 inputs (agent co-presence
subinputs + mirror mechanism + hormonal) going silent simultaneously.

Social dissonance feels distinct because aggregate is distinct, nhưng
mechanism is compound L1 deviation.

#### §7.1.5 Source 1 — Information mismatch (SCHEMA LAYER)

**Existing definition**: "Prediction error — có gì đó khác, không đủ
info, model sai, confused"

**Reframe mapping**: Đây **không phải L1 level**. Đây là **schema layer
dissonance** — PFC predictions vs outcomes.

Mechanism: PFC maintains schema-level predictions about world, actions,
expected outcomes. When prediction fails (action → unexpected result,
observation → unexpected pattern), schema-level dissonance fires.

**Examples**:
- Tin rằng bạn thân → bị phản bội → schema shock
- Predict 5 phút xong task → 2 giờ không xong → frustration
- See familiar face trong unfamiliar place → "wait, that's strange"
- Read book, learn new concept contradicting prior belief → cognitive
  dissonance

**Not L1 substrate**. Information mismatch operates at PFC schema level,
downstream từ body-input processing. Different mechanism, different
neural substrate (PFC executive networks vs insula/sensory).

Schema dissonance can **trigger** L1 responses (anxiety → cortisol →
body-input cascade), but originates at schema level.

#### §7.1.6 Source 3 — Threat schema (SCHEMA LAYER predicting L1)

**Existing definition**: "Anticipate negative — lo lắng, sợ tương lai,
chưa xảy ra"

**Reframe mapping**: Schema layer predicting future L1 threats.

Mechanism: PFC generates scenarios of possible future states, evaluates
threat potential, fires anticipatory response. Không phải current L1
signal, but schema-level prediction about future L1 threats.

**Examples**:
- Lo lắng về bài thi sắp đến → schema prediction về potential L1 impact
  (social rejection, future resource loss)
- Sợ bị sa thải → schema prediction về future L0/L1 security
- Sắp phỏng vấn → schema anticipation

**Feeds into L1 via cortisol + cardiovascular anticipatory response**
(body prepares cho predicted threat) — but **origin is schema layer**.

Threat schema dissonance shares substrate với information mismatch
(both PFC-level), shares mechanism với fear response (autonomic
anticipation), nhưng originates từ schema-level prediction about
future L1.

#### §7.1.7 Source 6 — Melody learning (SCHEMA LAYER restructuring)

**Existing definition**: "Chunks mới khó merge với melody cũ. Valley
dissonance trong arc. 'Mình có đang đi đúng không?'"

**Reframe mapping**: Schema layer chunks restructuring. Dissonance
emerges from intermediate schema states feeling incoherent during
learning/growth process.

Mechanism: learning new domain requires chunks restructuring. Intermediate
states (old schema partially demolished, new schema not yet coherent)
feel dissonant — cognitive equivalent of being mid-reorganization.
Melody-Arc.md documents this as "the valley" in arc structure.

**Not L1 substrate**. Learning dissonance operates at PFC schema level.
Feeds L1 cortisol (effortful learning = metabolic cost) but originates
trong schema restructuring.

**Examples**:
- 3 tháng học concept mới, chưa thấy kết quả → arc valley → "mình đang
  đi đâu?"
- Changing worldview after major event → old schema crumbling, new
  unclear
- Career transition → identity schema restructuring

#### §7.1.8 Key insight — 3+3 split

```
  Body-Dissonance.md §2.5 sources:

  BODY-INPUT LAYER (L1 substrate):
    Source 2 — Body-state delta          → direct L1 deviation
    Source 4 — Physical damage           → L1 nociception (or L0)
    Source 5 — Social damage             → L1 aggregate (agent + mirror)

  SCHEMA LAYER (PFC level):
    Source 1 — Information mismatch      → PFC prediction error
    Source 3 — Threat schema             → PFC future-L1 anticipation
    Source 6 — Melody learning           → PFC schema restructuring
```

**3 sources body-input level, 3 sources schema level**. Clean split.

#### §7.1.9 Tại sao this matters

Reframe proposes: dissonance **không unified mechanism**, it's **TWO
different mechanisms feeding same PFC observation**:

**L1 body-input dissonance**:
- Fast onset (seconds to minutes)
- Specific localization possible
- Direct neural substrate (insula, nociception, interoception)
- Resolved via fixing body-input (eat, sleep, warm up, repair injury,
  restore contact)

**Schema-level dissonance**:
- Slower onset (minutes to hours to days)
- Diffuse localization
- PFC/executive substrate (anterior cingulate, dlPFC)
- Resolved via schema update (new information, planning, processing,
  integration)

Both feel như "khó chịu" to PFC observation (Feeling folder PFC
interface), nhưng mechanisms + resolutions differ.

**Framework implication**: therapeutic + optimization approaches must
distinguish. L1 dissonance needs body-level intervention. Schema
dissonance needs cognitive/emotional processing. Confusing these =
treating schema dissonance với body intervention (ineffective) hoặc
treating body dissonance với cognitive therapy (ineffective).

Current framework's 6 sources already implicitly recognized distinction
— reframe makes explicit. Parsimony gain by grouping.

### §7.2 Dissonance spectrum remapping

Body-Dissonance.md §2 documents **14-level spectrum** từ micro (lấn cấn)
to emergency (ngất, panic). Reframe re-examines spectrum through L0/L1/
schema lens.

#### §7.2.1 Spectrum levels re-classified

**EMERGENCY level** (~90-100% body resource — suppress all else):
- Fight/flight/freeze (amygdala hijack) → L1 extreme OR L0 threshold
  crossed
- Panic (hoảng loạn) → typically schema overload + L1 cortisol spike
- Extreme pain → L1 nociception extreme OR L0 injury
- Shutdown (ngất, vagal syncope) → circuit breaker across L0/L1

**Classification**: emergency dissonance dominantly L0/L1 territory.
Body prioritizes survival-critical signals as emergency-loud.

**MẠNH level** (~60-90% body resource — immediate action):
- Sợ (fear) → typically schema threat prediction OR L1 acute threat
- Tức giận (anger) → schema boundary violation + L1 hormonal (testosterone
  + adrenaline)
- Đau rõ → L1 nociception gradient strong
- Ghê tởm (disgust) → L1 visceral/olfactory + evolved rejection signal

**Classification**: mix of L1 (pain, disgust) + schema (fear, anger).
Strong signals because actionable responses required.

**TRUNG BÌNH level** (~30-60% body resource — cần chú ý):
- Khó chịu (discomfort, body-state delta) → L1 gradient moderate
- Bực (irritation, frustration) → schema prediction error (Source 1)
- Bất an (unease, diffuse) → schema or mild L1 vague
- Lo lắng (anxiety, worry) → schema threat anticipation (Source 3)

**Classification**: split between L1 moderate and schema-level. Body
engages attention nhưng không emergency.

**NHẸ level** (~10-30% body resource — information, không urgent):
- Chán (boredom) → schema + Novelty drive low activation
- Băn khoăn (doubt, uncertainty) → schema prediction incomplete
- Bứt rứt (restlessness) → schema direction unclear + mild L1 kinesthetic
- Lấn cấn (micro-mismatch) → schema early warning

**Classification**: dominantly schema-layer. Mild signals, information
feedback without immediate action required.

#### §7.2.2 Pattern — intensity correlates với layer

**Observation across spectrum**:

```
  Intensity            Predominant layer
  ────────────────────────────────────────
  Emergency            → L0/L1 (survival-critical)
  Mạnh                  → L1 + schema (action-critical)
  Trung bình           → L1 + schema (attention-required)
  Nhẹ                  → Schema dominant (information)
```

**Higher intensity ↔ L0/L1 proximity**. **Lower intensity ↔ schema
layer dominance**.

#### §7.2.3 Tại sao pattern?

**Evolutionary logic**:

- **L0/L1 dissonance** directly tied to survival outcomes. Mistakes here
  = death. Evolution wired these signals **loud, non-suppressible,
  resource-dominating** because false-negatives lethal.
- **Schema-layer dissonance** is newer evolutionary layer (PFC executive
  functions expanded với hominid evolution). Schema errors important
  but less immediately lethal than L0/L1. Can afford to be **softer,
  more deliberative, flexible**.

**Consequence**: body prioritizes signals theo evolutionary age +
survival criticality:
1. L0 threshold (oldest, most critical) — loudest
2. L1 gradient deviations — loud proportional to magnitude
3. Schema prediction errors — softer, more nuanced
4. Schema restructuring (melody learning) — softest, sustainable

Framework từ Why-Body-Knows.md §4 (4-tier calibration) consistent:
L0/L1 substrate = Tier 1 evolution foundation, schema layer = Tier
2-4 built on top.

#### §7.2.4 Mixed dissonance common

Nhiều dissonance experiences **mix both layers**:

**Example 1 — Job loss anxiety**:
- Schema threat prediction (Source 3) = "what will I do, bills?"
  → anticipatory cortisol
- L1 secondary effects: chronic cortisol → sleep disruption → fatigue
  → cardiovascular strain
- Both layers active, compound effect

**Example 2 — Relationship conflict**:
- Schema prediction error (Source 1) = "I thought we agreed" → frustration
- L1 social aggregate (Source 5) = reduced warmth, missing affective
  touch
- Schema threat (Source 3) = "will this relationship end?"
- Three sources active simultaneously

**Example 3 — Chronic burnout**:
- L1 body-state delta (Source 2): sleep deprived, sedentary, no movement,
  social starved
- L1 hormonal: chronic cortisol elevated
- Schema meaning: "why am I doing this?"
- Schema prediction: "this will never end"
- Mixed L1 + schema simultaneously

**Implication**: real-world dissonance rarely pure single-source. Framework
should handle compounds while maintaining mechanism distinction cho
intervention purposes.

#### §7.2.5 Resolution approaches differ per layer

**L1 body-input dissonance** → body-level intervention:
- Eat, drink, warm up, cool down
- Sleep, rest, recover
- Movement, exertion
- Touch, social contact
- Natural environment exposure
- Medical treatment (physical injury, illness)

**Schema-level dissonance** → cognitive/emotional processing:
- Information seeking (fill info gap)
- Planning (resolve uncertainty)
- Reappraisal (shift interpretation)
- Meaning integration (new experience integration)
- Therapy (schema restructuring)
- Time (allow learning arc valley passage)

**Mixed dissonance** → both approaches, typically sequentially or in
parallel. Body interventions can create space cho schema processing
(exercise → mental clarity → problem solving). Schema interventions
can reduce body impact (therapy → stress reduction).

**Framework warning**: common mistake is treating one layer's dissonance
với wrong intervention:
- Schema dissonance từ meaning crisis → "just meditate more" không
  fixes schema gap
- L1 dissonance từ sleep debt → "just think positively" không fixes
  L1 deficit
- Both → chronic suboptimal state

Reframe provides diagnostic framework cho matching intervention to
source.

---

**§7 DISSONANCE RE-MAPPING — section complete**

Key findings:

1. **6 sources split cleanly 3+3** at L1 body-input level vs schema
   level

2. **Dissonance intensity correlates với layer**: emergency → L0/L1,
   nhẹ → schema. Evolution prioritizes survival-critical signals.

3. **Real-world dissonance usually mixed**, but mechanism distinction
   matters cho intervention

4. **Framework implication**: body-level interventions for L1 dissonance,
   cognitive/processing interventions for schema dissonance, matched
   compound response for mixed

Reframe §7 assessment: **dissonance mapping PASSES test criterion
§1.4.1(4)** — 6 sources map cleanly to reframe architecture, no gaps,
cleaner than existing flat-list framing.

**§5 + §6 + §7 MECHANISM LAYER COMPLETE**. Body-input substrate
enumerated (§2-§4), baseline adaptation mechanism established (§5),
PFC drives operate on L1 (§6), dissonance re-mapped cleanly (§7).
Theoretical core của reframe is now filled.

Ready cho §8 (channel shorthand mapping) và §9 (case test).

---

## §8 — "CHANNEL" AS SHORTHAND

### §8.1 Why channels were useful framing

Reframe **không discard** channel language — clarifies what channels
ARE ontologically. Section này explains tại sao channel vocabulary
emerged + served framework purposes tốt + remains useful as shorthand.

#### §8.1.1 Channel language advantages

**(i) PFC-accessible cluster-level descriptions**:
PFC thinks trong clusters, không trong raw sensory data. "I need nature
today" is more intuitive hơn "I need above-baseline fractal vision +
pink noise audition + phytoncide olfaction + thermal variation +
proprioceptive engagement." Channel shorthand matches natural cognitive
granularity.

**(ii) Matches intuitive phenomenology**:
Người nói "I'm touch-starved" before framework exists. "I need sunshine"
as cultural expression. These are phenomenological descriptions của
body-input aggregate deficits. Channel vocabulary emerged organically
vì it matches how body-input deficits are subjectively experienced —
not as specific individual receptor deficits, but as cluster-level
"missing something."

**(iii) Enables cross-case pattern matching**:
Body-Base-Example.md 50 cases grouped by channel domain (work/nature/
social/physical/meaning/mastery/consumption/status/expression). This
clustering enabled comparison — B1 workaholic và B5 karoshi share
"achievement channel dominance" pattern, easily recognized. Without
cluster language, each case would be unique combination of L1
deviations.

**(iv) Communicable to non-technical audience**:
"Body-input substrate + baseline adaptation + L3 operators" is precise
but inaccessible. "Your nature channel is starved" is comprehensible to
lay audience. Framework needs BOTH levels of language — technical for
theoretical claims, channel shorthand cho communication + practical
guidance.

**(v) Historically preceded reframe**:
Framework work (Body-Base.md, Body-Base-Example.md) used channel
language. Downstream files (Body-Personal-Optimization.md, Body-
Parenting-Optimization.md) built on channel concepts. Reframe không
require rewriting all this — channel language remains valid as
shorthand, just ontological status clarified.

#### §8.1.2 Legitimate usage không conflicting với reframe

Channel language valid WHEN:
- Practical guidance ("get more movement this week")
- Phenomenological description ("you sound touch-starved")
- Cross-case pattern recognition ("this is a nature deficit case")
- Clustering for communication
- Historical reference to existing framework files

Channel language problematic WHEN treated as:
- Theoretical primitives (they're not)
- Ontologically fundamental (aggregates, không primitives)
- Having own receptors (no, they're clusters of body-input receptors)
- Independent needs at their own layer (no, they're L1 patterns)
- Distinct primitives that couple (they overlap because shared substrate)

Reframe rule: **channel language tiện cho practical + phenomenological
contexts, body-input terminology required for architectural claims**.

### §8.2 Channel-to-body-input mapping

Section này provides systematic mapping từ Body-Base.md §4 channel list
to reframe body-input aggregates. Every channel trong existing framework
reduced to L1 substrate + (where applicable) L3 operator + schema
coupling.

#### §8.2.1 §4.1 Loud/Acute channels — mostly direct L1 match

**§4.1.1 Oxygen** → **§4.3 Respiratory** (direct)
- Crosses L0/L1 threshold at deprivation
- No aggregation needed — single input category

**§4.1.2 Water / Hydration** → **§4.6 Metabolic** (direct)
- Osmoreceptor signaling, crosses L0 at severe dehydration
- Single input category

**§4.1.3 Food / Nutrients** → **§4.6 Metabolic + §4.5 Visceral + §2.4
Gustation**
- Metabolic: blood glucose, ghrelin/leptin, satiety integration
- Visceral: gut-brain axis, enteric signaling, gut fullness
- Gustation: taste preferences, flavor experience
- Aggregate of 3 categories — "food" as phenomenological channel =
  metabolic + visceral + gustatory substrate combined

**§4.1.4 Temperature regulation** → **§4.1 Thermoreception core + §2.5
Tactile thermoreception**
- Core + skin thermoreception aggregate
- Crosses L0 at extremes

**§4.1.5 Sleep / Circadian** → **§4.8 Sleep / Circadian** (direct)
- Single input category, state-transition type

**§4.1.6 Physical safety / pain** → **§4.2 Nociception**
- Direct match for pain component
- Safety as anticipatory = Protect drive (§6.3) + L0 proximity detection

**§4.1.7 Elimination / waste removal** → **§4.5 Visceral**
- Direct visceral subcategory

**Pattern**: §4.1 Loud/Acute channels map mostly 1-to-1 or near-direct
to single body-input categories. These are **least aggregated** — close
to primitives themselves. Mô hình cũ correctly identified these as
"loud" because they map directly to receptors với loud signals.

#### §8.2.2 §4.2 Silent/Slow-Decay channels — aggregate compounds

Đây là where channel language most diverged từ body-input primitives.
Reframe provides detailed aggregate mappings:

**§4.2.1 Movement channel** = aggregate of:
- **§3.1 Proprioception**: varied postures, limb awareness
- **§3.3 Kinesthetic**: muscle activity, effort, recovery dynamics
- **§3.2 Vestibular**: varied acceleration, balance challenges
- **§4.4 Cardiovascular**: HR elevation + recovery cycles
- **§4.6 Metabolic**: energy expenditure cycles
- **§4.7 Hormonal**: endorphin, BDNF, dopamine exercise response

At ancestral baseline levels (8-15 km/day varied labor + recovery).

**§4.2.2 Nature exposure channel** = aggregate of:
- **§2.1 Vision**: fractal patterns D≈1.3-1.5, biological motion, depth,
  natural light spectrum
- **§2.2 Audition**: pink noise natural soundscape, water/wind/leaves
- **§2.3 Olfaction**: phytoncides, earth, plant volatiles (Shinrin-Yoku
  research)
- **§2.5 Tactile skin**: wind, sun, varied thermal, outdoor texture
- **§4.1 Thermoreception core**: natural thermal variation
- **§3.1 Proprioception**: varied terrain engagement
- **§4.8 Sleep/Circadian**: natural light cycle alignment
- **§4.3 Respiratory**: cleaner air, phytoncide inhalation

At ancestrally-calibrated baseline levels. "Nature channel" is
**aggregate of 7-8 input categories simultaneously**, không single
primitive. Explains tại sao nature phenomenologically feels so
important — it's meeting multiple L1 baselines simultaneously. Also
explains tại sao partial substitutes (just fractal screen, just bird
sounds) don't fully satisfy — only some of the aggregate is met.

**§4.2.3 Agent/social channel** = aggregate of:
- **§2.2 Audition**: voices, laughter, breathing sounds of others,
  language prosody
- **§2.1 Vision**: faces, biological motion specifically human,
  gestures, expressions
- **§2.3 Olfaction**: individual body scents, familiar recognition
- **§2.5 Tactile**: affective touch (C-tactile fibers) ESPECIALLY
  important, grooming, contact
- **§4.7 Hormonal**: oxytocin release via bonding, cortisol reduction
  via safe social
- **§4.9 Self-signal**: validation của own state via other's reading/
  mirroring
- **Empathy-Mirror mechanism** (cross-cutting): bidirectional body-state
  mirroring creates proxy L1 firing

Plus **Status operator** (§6.2) often involved — agent contact organizes
status dynamics.

**Agent channel = aggregate of ~6 L1 categories + mirror mechanism +
Status operator involvement**. Explains tại sao social isolation (B50
solitary) crashes faster than nature isolation (B46 Proenneke) —
multiple input categories starve simultaneously trong social deprivation,
while nature isolation may leave some categories fed.

**§4.2.4 Living Pattern Input** = **sub-aggregate của vision + audition**:
- **§2.1 Vision**: biological motion detection specifically — dedicated
  neural system
- **§2.2 Audition**: ambient living sounds (birds, insects, distant
  human life, livestock)

Explains Aquarium Effect (Cracknell 2016) — cá swimming fires biological
motion visual input, shifts body-base state toward "domain alive."
Không full nature channel (missing thermal, olfactory, phytoncides,
proprioceptive) nhưng partial feed.

**§4.2.5 Physical touch channel** = aggregate of:
- **§2.5 Tactile skin mechanoreception**: pressure, texture, vibration
- **§2.5 Tactile affective (CT fibers)**: SPECIFICALLY the oxytocin
  pathway
- **§3.1 Proprioception**: body contact position awareness
- **§4.7 Hormonal**: oxytocin release, cortisol dampening

"Touch channel" reduces to tactile subsystem aggregate. CT affective
fiber pathway is **distinct mechanism** — explains tại sao sexual
touch ≠ hugs ≠ massage even though all "touch."

**§4.2.6 Deep rest channel** = aggregate of:
- **§4.4 Cardiovascular**: HRV elevated, parasympathetic dominance
- **§4.3 Respiratory**: slow deep diaphragmatic
- **§4.9 Self-signal interoception**: attention turned inward, body
  awareness maintained
- **§4.7 Hormonal**: cortisol reduction, melatonin readiness, growth
  hormone release
- **Novelty drive SUPPRESSION**: not seeking new input, allowing
  habituation
- **Protect drive SUSPENSION**: safety context allowing guard down

"Deep rest" is both L1 aggregate AND suspension of L3 operators. Explains
tại sao sleep alone không rest (sleep fills §4.8 Sleep/Circadian but
if preceded by hours screen time, Novelty drive still firing).

**§4.2.7 Sensory diversity channel** = **Novelty operator variance across
all sensory inputs**:
- Not a body-input — it's the Novelty operator applied variably across
  §2-§4 inputs
- Deprivation = all sensory inputs at same constant level → Novelty
  operator never fires → flat subjective state
- B50 solitary cell = extreme sensory diversity deprivation compound

**§4.2.8 Silence channel** = **§2.2 Audition baseline at low-amplitude
natural soundscape**:
- Not separate primitive — it's audition input category at specific
  condition
- Absence của noise pollution
- Not literal silence (anechoic causes anxiety) but baseline ambient
- Contemplative traditions specifically use này

#### §8.2.3 §4.3 Higher-order channels — schema + L3 + body-input compounds

**§4.3.1 Sexual channel** = compound of:
- **§4.7 Hormonal**: testosterone, estrogen, oxytocin, vasopressin
- **§2.5 Tactile affective**: CT fibers, oxytocin release
- **§4.4 Cardiovascular**: arousal response
- **§4.5 Visceral**: genital sensation + arousal
- **§6.1 Novelty drive**: strongly involved, limerence baseline shift
- **Schema layer**: meaning, identity, relationship context

Sexual is **L1 body-input aggregate + L3 Novelty drive + schema
compound**. Không pure body-input. B20 asexual variation = different
Novelty drive calibration + different schema, không "missing channel."

**§4.3.2 Skilled engagement / flow channel** = compound of:
- **§3.1 Proprioception** (for physical skills)
- **§3.3 Kinesthetic** (for physical skills)
- **§4.9 Self-signal** (awareness suspended or heightened paradoxically)
- **§4.4 Cardiovascular** (optimal arousal)
- **§6.1 Novelty drive** (skill progression driving reward)
- **Schema layer** (skill chunks + progression arc)

Flow is **schema + Novelty drive + multiple L1 aggregate compound**.
Not a body-input primitive. Operates via skill chunks trong schema
interacting với body-inputs.

**§4.3.3 Meaning / purpose channel** = **PRIMARILY schema layer**:
- Not a body-input cluster
- Coherent narrative shifts schema structure
- Affects §4.9 self-signal interoception ("I know who I am")
- Affects baseline expectations for all body-inputs (via goal-directed
  action selection)

Meaning "channel" operates **at schema layer**, not L1. Meaning
dissonance (existential drift, purposelessness) = schema instability
that propagates to body-input engagement (motivation loss → movement
reduced → all L1 gradually decline).

**Reframe claim**: meaning is **NOT a body-input channel** — it's schema
coherence that affects body-input engagement via PFC mediation. B21
religious fanatic, B22 cult member, B23 young zealot all show extreme
meaning pursuit → compensates for other L1 deficits (physical, social,
kinesthetic) temporarily via compound reward (meaning + Status group +
Protect schema).

**§4.3.4 Mastery channel** = compound of:
- **§6.1 Novelty drive** (skill progression = baseline shifting upward)
- **§4.9 Self-signal** (competence validation via successful performance)
- **§6.2 Status drive** (social validation từ recognition)
- **Body-input category varies với skill type**: proprioception +
  kinesthetic (physical mastery), auditory + self-signal (musical),
  visual (artistic), schema-level (intellectual)
- **Schema layer**: skill chunks + progression + transmission loop

Mastery = **compound of Novelty drive + Self-signal + Status drive +
schema + variable body-inputs**. Not single primitive. §13.9 Example's
sustainable compound signature captures this — mastery fed through
multiple mechanisms, not one channel.

#### §8.2.4 Mapping summary

```
  Existing channel                →  Reframe mapping

  LOUD/ACUTE (direct L1 match):
  Oxygen                          →  §4.3 Respiratory
  Water                           →  §4.6 Metabolic
  Food                            →  §4.6 + §4.5 + §2.4 aggregate
  Temperature                     →  §4.1 + §2.5 thermal aggregate
  Sleep                           →  §4.8 Sleep/Circadian
  Safety/Pain                     →  §4.2 Nociception + Protect
  Elimination                     →  §4.5 Visceral sub

  SILENT/SLOW-DECAY (compounds):
  Movement                        →  §3.1 + §3.3 + §3.2 + §4.4 + §4.6
                                     + §4.7 hormonal
  Nature                          →  §2.1 + §2.2 + §2.3 + §2.5 + §4.1
                                     + §3.1 + §4.8 + §4.3 aggregate
  Agent/social                    →  §2.1 + §2.2 + §2.3 + §2.5(CT)
                                     + §4.7 + §4.9 + Empathy-Mirror
  Living pattern                  →  §2.1 biomotion + §2.2 ambient
  Touch                           →  §2.5 (4 subsystems) + §3.1 + §4.7
  Deep rest                       →  §4.4 + §4.3 + §4.9 + §4.7
                                     + L3 operator suspension
  Sensory diversity               →  §6.1 Novelty variance across §2-§4
  Silence                         →  §2.2 Audition baseline condition

  HIGHER-ORDER (compounds with drives + schema):
  Sexual                          →  §4.7 + §2.5(CT) + §4.4 + §4.5
                                     + §6.1 Novelty + schema
  Flow                            →  §3.1 + §3.3 + §4.9 + §4.4
                                     + §6.1 Novelty + schema chunks
  Meaning                         →  PRIMARILY schema, affects §4.9
  Mastery                         →  §6.1 + §4.9 + §6.2 + variable L1
                                     + schema
```

**Every channel from existing framework reduces cleanly** to body-input
aggregates và/hoặc L3 operators và/hoặc schema structures. No residue
requiring new primitives.

**Parsimony assessment**: reframe replaces ~19 channels với ~17 body-input
primitives + 3 L3 operators + schema. Similar count overall, but reframe
primitives are architecturally homogeneous (all at substrate level với
same mechanism) rather than mixed layers (loud/silent/higher-order).
Architectural cleanness gained.

### §8.3 Tại sao channels cannot be cleanly enumerated

Reframe explains the persistent problem trong framework development:
**"how many channels?" has no principled answer**. Existing Body-Base.md
§4 lists ~19 channels across 3 categories, Body-Base-Example.md §14
proposed ~7 additional candidates. Feeling-Sources.md has different
granularity. Why does number vary?

**Answer**: because channels are **arbitrary cluster boundaries** drawn
over a substrate of overlapping body-inputs + schema structures.
Framework designer can draw boundaries at different resolutions,
each yielding different "channel count."

#### §8.3.1 Arbitrary granularity

**Coarse clustering** (5-7 channels):
- Physical (food/water/sleep/safety)
- Movement
- Social
- Nature
- Meaning/Purpose
Useful cho broad life assessment, intuitive phenomenology.

**Medium clustering** (~12-15 channels):
- Body-Base.md §4 current list
- Useful cho detailed analysis, case pattern matching

**Fine clustering** (~25-30):
- Add: living pattern, silence, sensory diversity, generosity,
  attention, pain-ritual, autonomy, dominance, epistemic humility, etc.
- Useful cho very specific interventions, research precision

**Continuous resolution** (research ideal):
- Body-input categories at sensory receptor resolution
- Baselines measured per-input
- Variation documented per individual
- Needs biological measurement, AI-assisted monitoring

**All levels valid depending on resolution needed**. Framework shouldn't
force one level — it should specify granularity appropriate to purpose.

#### §8.3.2 Parallel — emotion categorization problem

Psychology has same problem với emotions:
- **Ekman (1972)**: 6 basic emotions (happy, sad, angry, fearful,
  disgusted, surprised)
- **Plutchik (1980)**: 8 basic + combinations
- **Cowen & Keltner (2017)**: 27 distinct emotional categories via
  principal component analysis của self-report data
- **Barrett constructed emotion**: emotions không discrete categories,
  emerge từ core affect + conceptual categorization
- **Continuous dimensional models**: valence × arousal × dominance

Each valid depending on question asked. Research tradition uses different
resolutions cho different purposes. "How many emotions?" has no
principled answer because emotions are **emergent patterns** trong
underlying affective + physiological + cognitive systems.

**Body-base channels are analogous**: emergent patterns trong underlying
body-input substrate. Number of channels depends on clustering resolution,
không inherent ontological count.

#### §8.3.3 Common cluster boundaries emerge không inevitable

Certain clusterings appear across frameworks because of:

**(i) Functional coherence**: inputs that co-vary in ancestral environment
naturally cluster (nature inputs all correlate với outdoor activity)

**(ii) Co-deprivation patterns**: inputs that often go starved together
get grouped (movement + nature co-deprived trong sedentary office work)

**(iii) Phenomenological accessibility**: clusters at levels PFC can
articulate (not too granular to be overwhelming, not too coarse to be
useless)

**(iv) Cultural + linguistic shaping**: cultures develop vocabulary cho
certain clusters based on what matters trong their context

These factors explain WHY certain clusterings emerge repeatedly, không
that they reflect ontological primitives. Cluster boundaries are
**pragmatic + culturally-shaped**, không ontologically required.

#### §8.3.4 Implication cho framework work

Reframe doesn't try to "fix" channel count. Instead:

1. **Acknowledge arbitrary granularity** explicitly
2. **Use body-input primitives** for architectural claims
3. **Use channel shorthand** for practical + communication purposes
4. **Match resolution to purpose**: diagnostic vs intervention vs research
5. **Not defend specific channel count** as "correct"

Framework can use "nature channel" while knowing it's aggregate, không
primitive. Can use "17 body-input categories" while knowing those are
themselves aggregate của sensory receptor systems that could be
decomposed further (vision = photon detection + edge + motion +
biological motion + face + etc., each of those further decomposable).

**All levels of description valid + useful at their level**. Reframe
provides **substrate level** description; channel level + higher levels
remain useful for their respective purposes.

### §8.4 Preserved usage vs reframe usage

**Framework policy recommendation**: channel language CONTINUES trong
framework writing as convenient shorthand, với explicit ontological
status clarification. Rule-based guidance cho when to use channel
language vs body-input language.

#### §8.4.1 Ontological status clarification

**Channel = emergent cluster** của:
- Body-input primitives (L1 substrate)
- Và/hoặc L3 operators (Novelty/Status/Protect)
- Và/hoặc schema structures (PFC-level constructs)
- Clustered at functional + phenomenological level
- Not ontologically fundamental
- Not possessing own receptors

**Channel = useful shorthand**, không architectural primitive. Framework
should maintain này distinction explicit.

#### §8.4.2 When to use channel language

Channel vocabulary appropriate trong:

**(i) Practical guidance**:
- "Your movement channel needs more attention this week"
- "The nature channel suggests you get outdoors"
- "Touch channel deprivation is part of this pattern"
- Appropriate cho health advice, intervention recommendations, life
  coaching contexts

**(ii) Phenomenological description**:
- "He's touch-starved"
- "She needs a creative channel outlet"
- "This case shows meaning channel dominance"
- Appropriate cho describing subjective experience + case clustering

**(iii) Cross-case pattern matching**:
- Body-Base-Example.md chapter titles
- Case categorization (achievement, nature, social, etc.)
- Group-level clinical observations

**(iv) Communication với non-technical audience**:
- Health writing
- Educational materials
- Client communication

**(v) Reference to existing framework files**:
- Body-Base.md §4 uses channel language
- Don't break cross-references by rewriting all files
- Channel language remains valid reference

#### §8.4.3 When to use body-input terminology

Body-input (L1) language required cho:

**(i) Architectural/theoretical claims**:
- "The substrate of body-base is..."
- "Mechanism operates on L1 body-inputs via..."
- "Reframe substrate analysis shows..."
- Precision required cho theoretical rigor

**(ii) Framework-level analysis**:
- Drive operator interactions (§6)
- Baseline adaptation dynamics (§5)
- Dissonance source mapping (§7)
- Research integration

**(iii) Biological/clinical precision**:
- Specific interoceptive deficits
- Sensory processing disorders
- Neurological investigations

**(iv) Research design**:
- Measurement targets
- Experimental variables
- Hypothesis specification

#### §8.4.4 Rule

**Simple rule**: say "channel" when practical guidance + phenomenology
+ communication, say "body-input" when architecture + theory + research
precision.

Body-Base.md foundation file should use **both**:
- Channel language for reader accessibility
- Body-input language for architectural claims
- Explicit relationship clarified via §8.4 rule

Downstream files (Body-Personal-Optimization.md, Body-Parenting-
Optimization.md) remain mostly channel-language because they're
practical guidance.

#### §8.4.5 Backward compatibility

Reframe commits NO breaking changes:
- Existing framework files retain channel terminology
- Body-Base.md §4 Phase C fill may use channel vocabulary for accessibility
- Reframe adds substrate layer (§5-§7 mechanism) as complementary, không
  replacement for communication-level
- Users của existing framework don't need to learn new vocabulary unless
  doing theoretical work

**Reframe = ADDITIONAL architectural layer**, không replacement của
existing work. Parsimony gain + architectural clarity without compatibility
break.

---

## §9 — TEST AGAINST PHASE B CASES

### §9.1 Selection criteria

§9 tests reframe against selected subset của 50 Phase B cases + 2
Deep-Cases. Goal: demonstrate reframe capacity to explain documented
cases without adding epicycles + identify genuine gaps.

#### §9.1.1 Selection principles

**(i) Span pathological và sustainable**: both crash patterns (most
cases) và sustainable intense pursuit (B27/B30/B46). Reframe must
explain both successful và failed patterns.

**(ii) Span channel category diversity**: cases representing nature,
social, movement, touch, achievement, meaning, mastery, consumption
starvation/over-feed patterns. Ensures reframe tests across body-input
types.

**(iii) Span confidence levels**: include well-documented historical
cases (🟢) và general pattern cases (🟡). Reframe shouldn't require
unusual case granularity.

**(iv) Include Deep-Cases triangulation**: DC1 Tesla + DC3 digital
nomad vs ancestral = multi-angle analyzed cases, strongest test cho
reframe validity.

**(v) Include challenging candidates**: meaning-over-fed cases (B21-B23
religious fanatic, B22 cult) are reframe test cases — if reframe cannot
explain meaning-dominant patterns, significant gap identified.

#### §9.1.2 Test procedure per case

For each selected case:

1. **Case summary**: brief scenario recap
2. **Old framework description**: channels identified by Body-Base-
   Example.md §13 validation table
3. **Reframe description**: body-input aggregates + L3 operators +
   schema structures + baseline dynamics
4. **Comparative notes**: what reframe adds / clarifies / loses
5. **Confidence assessment + verdict**: PASS / PARTIAL / FAIL

#### §9.1.3 Selected cases (15 total, 2 batches)

**Batch 1 (7 cases — tested trong §9.2.1-§9.2.7)**:
1. B1 workaholic burnout — multi-input starvation pattern
2. B2 billionaire post-wealth emptiness — Status proxy mechanism test
3. B5 karoshi — cultural amplification + multi-input crash
4. B6 digital nomad — agent depth vs breadth distinction
5. B11 codependent — self-signal interoception primary
6. B13 love addict — limerence baseline shifting mechanism
7. B18 body modification / pain ritual — context-dependent nociception

**Batch 2 (8 cases — tested trong §9.2.8-§9.2.15)**:
8. B27 Vietnamese craftsman village — sustainable compound positive
   prescription
9. B30 Jiro 99-năm mastery — unbounded mastery mechanism
10. B31 ultra-processed food — supernormal gustation evidence
11. B35 screen addiction — engineered visual + attention capture
12. B46 Proenneke 30-năm Alaska — exteroceptive rich, minimal agent
13. B50 solitary confinement — multi-input simultaneous deprivation
14. DC1 Tesla + Leonardo contrast — mastery + community compound absent
15. DC3 ancestral nomad vs digital — body-input differential analysis

#### §9.1.4 Expected outcome predictions (before testing)

**Expected PASS** (reframe explains cleanly): B1, B5, B6, B11, B13,
B27, B30, B31, B35, B46, B50, DC1, DC3

**Expected STRONG PASS** (reframe significantly clearer): B2 (status
proxy), B11 (self-signal), B6 (depth/breadth), DC3 (differential)

**Challenge cases**: B18 (context-dependent nociception), meaning
cases generally — test reframe's handling of schema-L1 coupling

**FAIL candidates**: none clearly identified pre-test, but reframe
should confront possibility

### §9.2 Cases tested

#### §9.2.1 B1 Workaholic burnout

**Case summary**: Successful professional, intense achievement pursuit
over 10-20 years, eventually crashes — chronic fatigue, cynicism,
reduced efficacy, cardiovascular strain, relationship damage, often
sudden onset despite gradual buildup.

**Old framework (channel language)**: Achievement/work channel dominant,
starved channels: movement, nature, social (beyond work colleagues),
touch, deep rest, meaning, self-signal.

**Reframe (body-inputs + drives + schema)**:

L1 body-inputs starved simultaneously (multi-input compound deficit):
- **§4.8 Sleep/Circadian**: chronic sleep debt, fragmented, blue light
  late
- **§3.3 Kinesthetic + §3.1 Proprioception**: sedentary 10-12+ giờ daily
- **§4.7 Hormonal**: chronic cortisol elevation, testosterone decline,
  dopamine baseline shifted via work-reward supernormal
- **§4.4 Cardiovascular**: chronic sympathetic dominance, HRV low
- **§4.3 Respiratory**: shallow chest breathing, anxiety feedback
- **§4.5 Visceral**: stress-induced GI dysregulation
- **§2.5 Tactile affective (CT)**: minimal social affective touch
- **§2.1 Vision**: fluorescent chronic, no fractal nature
- **§4.9 Self-signal interoception**: suppressed via cognitive overdrive

L3 drives operating pathologically:
- **Novelty drive** hijacked via achievement supernormal → baseline
  shifts, needs more work-reward cho same satisfaction
- **Status drive** culturally reinforced, work identity fused
- **Protect drive** schema-level anxiety ("must succeed to be safe")

Schema layer: "success = safety" prediction, "rest = laziness" cultural
schema, identity fused với work role.

**Crash mechanism**: cumulative L1 deficit reaches threshold where
self-regulation fails. §13.7 Example formula applies: depth × breadth
of starvation = crash speed. ~9 L1 inputs starved simultaneously +
hormonal baseline elevated from Novelty hijacking = eventual multi-
system failure.

**Comparative notes**: Mô hình cũ described pattern at channel
aggregation level. Reframe adds precision — specifies EXACTLY which 9
L1 categories starved với mechanism cho each, explains tại sao crash
often "sudden" (multiple thresholds crossed near-simultaneously),
clarifies tại sao achievement itself doesn't fix dissatisfaction
(Novelty baseline shifted).

**Verdict**: **PASS**. Reframe adds precision without losing coverage.
Mechanism clearer than "channel starvation" aggregate description.

#### §9.2.2 B2 Billionaire post-wealth emptiness

**Case summary**: Individual achieves financial goal ($100M+, successful
IPO, etc.), reports unexpected emptiness, depression, "lost purpose"
phenomenology. Common pattern documented across successful entrepreneurs,
athletes post-peak, artists post-success.

**Old framework (channel language)**: Money/achievement channel
saturated, meaning channel empty. Status channel paradox — achieved
yet empty.

**Reframe (body-inputs + drives + schema)**:

L1 body-inputs status: typically **adequate or surplus** (wealth provides
access to all L1 supply — food, shelter, healthcare, some social, some
movement opportunity, etc.). Key observation: L1 không primary deficit.

L3 Status drive: satisfied trong achievement trajectory up to completion.
BUT **without L1 payoff** — achievement satisfied drive's prediction,
but doesn't auto-feed body-inputs directly. Drive expectation delivered,
reality didn't match ("I thought I'd feel different").

Schema layer: identity fused với pursuit. Pursuit completed = identity
vacuum. Meaning dissonance (Source 3 + 6 trong §7.1) at schema level.

**Mechanism**: classic Status drive pathology. Drive fired reward
anticipation during pursuit (years of anticipatory dopamine). Achievement
removed pursuit, drive went quiet. L1 didn't automatically adjust upward
(money buys things but doesn't force affective touch, doesn't create
meaning, doesn't shift self-signal).

**Critical reframe finding**: **§14.6 Example exact scenario**. Status/
wealth = PFC proxy without direct L1 receiver. Direct pursuit without
ensuring L1 payoff = empty.

**Comparative notes**: Reframe **significantly clearer** than mô hình
cũ. Old framework said "money doesn't feed meaning channel" without
mechanism. Reframe specifies: Status drive operates on social environment
organization, money achieves that, but L1 body-inputs don't follow
automatically. Có gap between drive satisfaction và substrate maintenance.

B40 Rothschild contrast validates: multi-generational architecture
grounded trong L1 outcomes (descendants' security, knowledge transmission)
sustainable precisely because money continuously proxies real L1 supply,
không disconnected pursuit.

**Verdict**: **STRONG PASS**. Reframe resolves §14.6 tension
architecturally. Mechanism significantly cleaner.

#### §9.2.3 B5 Karoshi (Japanese overwork death)

**Case summary**: Japanese worker culturally expected to work 80-100
hours/week, eventually dies từ cardiovascular failure, suicide, or
stress-related illness. Well-documented phenomenon với legal recognition
in Japan.

**Old framework (channel language)**: Work channel culturally-forced
dominance. Movement, sleep, social (beyond work colleagues), nature,
touch, rest all starved. Cultural amplification forcing single-channel
extreme.

**Reframe (body-inputs + drives + schema)**:

L1 body-inputs starved extreme (worse than B1 workaholic):
- **§4.8 Sleep**: 4-5 giờ chronic
- **§3.1/§3.3 Proprio + Kinesthetic**: 12-16 giờ sedentary
- **§4.7 Hormonal**: extreme cortisol chronic, testosterone collapse
- **§4.4 Cardiovascular**: chronic hypertension, HRV very low — **actual
  L1 → L0 pathway via cardiovascular failure**
- **§2.1 Vision**: fluorescent office near-total
- **§2.5 Tactile affective**: minimal, culturally restricted
- **§4.3 Respiratory**: chronic shallow
- **§4.5 Visceral**: gastritis, ulcers common
- **§4.9 Self-signal**: actively suppressed via cultural norms ("gaman"
  endurance)

L3 drives amplified culturally:
- **Status drive** = cultural amplification of work hierarchy recognition
- **Protect drive** = shame-avoidance, schema-level "failure = family
  shame"
- **Novelty drive** mostly absent — repetitive work lacks novelty

Schema layer: cultural narrative "worker = honor", "quitting = dishonor",
"fatigue = weakness to overcome." Cultural amplification (§13.4 Example
finding) of Protect drive via shame mechanism.

**Crash mechanism**: L1 → L0 crossing via cardiovascular. Multi-input
deficit compounds, hormonal extreme, cardiovascular eventually fails.
Literal death từ multi-input starvation forced by cultural amplification.

**Comparative notes**: Reframe specifies the **cultural layer operates
on substrate through schema**. §13.4 finding ("culture shapes expression
not architecture") validated — cultural narrative amplifies Protect
drive schema, which forces behavioral patterns that starve L1. Substrate
reacts predictably to starvation regardless of cultural meaning. **Body
doesn't care what culture says**.

B14 Vietnamese extended family contrast: same cultural amplification
principle, different direction — amplifies family/community = L1 agent
aggregate fed richly.

**Verdict**: **PASS**. Reframe adds cultural-schema-substrate
integration clarity. Mechanism clearer.

#### §9.2.4 B6 Digital nomad long-term

**Case summary**: Professional travels continuously 7-12+ năm, visits
dozens of countries, social media documents "free" lifestyle, eventually
crashes trong loneliness, meaning crisis, health decline. Pattern recurring
across digital nomad community, especially năm 7-12 into lifestyle.

**Old framework (channel language)**: Nature/movement channels over-fed
via varied travel, social channel depth starved despite quantity contact,
meaning channel uncertain.

**Reframe (body-inputs + drives + schema)** — **DC3 analysis applies**:

L1 body-inputs fed:
- **§2.1 Vision** varied (new locations constantly)
- **§3.1/§3.2/§3.3 Proprio/vestibular/kinesthetic** varied
- **§2.5 Tactile thermal** varied
- **§6.1 Novelty drive** firing constantly on travel novelty

L1 body-inputs ambiguously fed:
- **§2.2 Audition** — varied soundscapes but less ancestral pink noise
  embedded
- **§2.3 Olfaction** — varied but no baseline establishment ("no home
  smell")
- **§2.4 Gustation** — varied but often processed street food

L1 body-inputs starved:
- **§2.5 Tactile affective (CT)** — no sustained bonds → minimal
  sustained affective touch
- **§4.9 Self-signal interoception** — no consistent mirroring from
  stable relationships → gradual erosion
- **§4.7 Hormonal oxytocin** — minimal sustained bonding → baseline
  dysregulation
- **§2.3 Olfaction familiar** — no "home smell" baseline cho security
  signal

L3 drives:
- **Novelty drive** hijacked via travel supernormal → baseline shifts,
  normal becomes boring
- **Status drive** partly fed via social media + nomad community
- **Protect drive** lacks anchor (no stable tribe)

Schema layer: "freedom" ideology masks accumulating affective-relational
deficit. Self-narrative justifies sustained pattern.

**Crash mechanism**: năm 7-12 pattern observed because affective touch
+ self-signal interoception + hormonal bonding cumulative deficit
reaches threshold. Not sudden — slow accumulation, eventually can't
compensate.

**Comparative notes**: Reframe provides **depth vs breadth distinction**
mô hình cũ couldn't cleanly state. "Social channel" is aggregate —
quantity breadth ≠ depth substrate. Digital nomad has quantity (many
casual contacts) but minimal CT affective + sustained self-signal
mirroring + oxytocin bonding patterns. Mô hình cũ said "social channel
fed" but couldn't explain tại sao empty. Reframe specifies WHICH
sub-components fed vs starved.

DC3 ancestral nomad contrast validates: same "movement/travel" context,
radically different body-input outcome (tribal affective touch rich,
self-signal via lifetime mirroring, familiar olfactory always present).

**Verdict**: **STRONG PASS**. Reframe provides granular distinction
resolving paradox that troubled mô hình cũ.

#### §9.2.5 B11 Codependent

**Case summary**: Person chronically attuned to partner's/parent's/child's
emotional state, own needs suppressed, extreme outward focus, eventual
identity confusion, burnout, relationship stuck patterns. Extensively
documented trong clinical psychology.

**Old framework (channel language)**: Social channel dominant but
pathological. Self-awareness starved.

**Reframe (body-inputs + drives + schema)**:

L1 body-inputs:
- **§4.9 Self-signal interoception SEVERELY STARVED** — primary deficit.
  Chronic outward attunement → own state reading atrophies → clinical
  alexithymic tendencies
- **§2.5 Tactile affective (CT)** — present but asymmetric (giving,
  not receiving)
- **§4.7 Hormonal oxytocin** — dysregulated, seeking without equal
  reciprocation
- **§4.4 Cardiovascular** — chronic elevated HR từ attunement stress,
  HRV low
- **§4.7 Hormonal cortisol** — chronic elevated

L3 drives:
- **Protect drive** applied excessively to other, không self — extended
  empathy без self-protection
- **Status drive** via being needed (approval proxy)

Schema layer: "my worth = their approval/needs met", attachment anxiety,
often developmental origin (parentification, trauma)

**Critical reframe finding**: **§4.9 self-signal interoception as
architectural keystone directly validated**. Codependency is primarily
self-signal deficit với downstream effects on other L1 categories.
Reframe identifies clear primary deficit rather than vague "social
channel pathological."

**Comparative notes**: Reframe gives clear diagnostic and intervention
pointer. §4.9 training (mindfulness, Gendlin focusing, somatic therapy)
= targeted treatment. Mô hình cũ's "social channel pathological" was
harder to operationalize.

B15 helicopter parent contrast: B15 causes B11-type patterns trong
children (§4.9 self-signal atrophy developmental).

**Verdict**: **STRONG PASS**. Direct validation of §4.9 keystone
section. Reframe identifies architectural primary deficit.

#### §9.2.6 B13 Love addict

**Case summary**: Person pursues romantic intensity repeatedly, limerence
phase rewarding, inevitable fading → crash → seek new limerence object.
Pattern recurring với multiple partners. Documented trong attachment
research + addiction parallels.

**Old framework (channel language)**: Romantic/pair-bonding channel
supernormal pursuit. Love addiction.

**Reframe (body-inputs + drives + schema)** — **direct baseline
shifting mechanism**:

Limerence phase (first 6-18 tháng) L1 supernormal feeding:
- **§4.7 Hormonal**: dopamine surge, oxytocin surge, vasopressin (pair
  bonding), testosterone responsive, norepinephrine elevated
- **§2.5 Tactile affective (CT)**: frequent intensity
- **§2.1 Vision**: face-focused attention peak
- **§2.2 Audition**: voice + laughter reward amplified
- **§2.3 Olfaction**: partner scent preference peak
- **§4.4 Cardiovascular**: elevated through anticipation + presence

Net effect: **multi-input simultaneous supernormal feeding**. Baseline
shifts upward dramatically across body-input categories — classic
delta rule mechanism from §5.3.

Post-limerence (~18 tháng onward):
- Hormonal baseline habituated — dopamine no longer peaks với same
  person
- Oxytocin shifts toward mature bond pattern (different substrate)
- Baseline SHIFTED UPWARD means normal relationship now feels
  UNDERSTIMULATING
- **Dissonance at new elevated baseline** when stimulus decreases

Solution trong pathological pattern: **seek new limerence** to re-fire
supernormal stimulus. New partner = fresh dopamine peak. Classic
addiction escalation pattern.

L3 drives:
- **Novelty drive** hijacked via limerence supernormal across multiple
  hormonal + sensory axes
- **Protect drive** attaches to object then shifts

**Research**: Fisher fMRI research directly documents limerence dopamine
pattern. Reframe matches established research cleanly.

**Comparative notes**: Reframe gives **direct baseline shifting
mechanism explanation**. Mô hình cũ described "over-pursuit" without
mechanism. Reframe shows identical mechanism to substance addiction
(baseline shifts + tolerance + withdrawal) operating on natural bonding
system. Hedonic treadmill applied to romantic love.

Therapeutic implication: same approach as addiction recovery —
mechanism clarity enables intervention.

**Verdict**: **PASS**. Clear baseline shifting + hedonic treadmill
mechanism explanation.

#### §9.2.7 B18 Body modification / pain ritual

**Case summary**: Intentional pain via tattoo, piercing, scarification,
branding, often trong ritual context. Cultural practice across many
societies, modern subcultures also. Pain seeking when pain usually
dissonance.

**Old framework (channel language)**: Candidate "pain-ritual channel"
trong §14.1 Example. Nociception engineered for endorphin + meaning
compound.

**Reframe (body-inputs + drives + schema)**:

L1 body-inputs activated:
- **§4.2 Nociception**: controlled pain trong A-delta + C-fiber pathway
- **§4.7 Hormonal**: endorphin + endocannabinoid release post-pain
  (Fuss 2015 research update)
- **§4.9 Self-signal**: heightened awareness during + after ritual

L3 drives:
- **Status drive** via tribal membership, mark of group identity
- **Protect drive** via ritual safety context

Schema layer critical:
- **Ritual framing**: controlled, meaningful, supervised
- **Identity integration**: mark of passage, belonging, transformation
- **Safety context**: không random pain, structured
- **Community witness**: mark recognized by group

**Context-dependent interpretation** — reframe's unique §4.2 finding:
pain alone = dissonance, pain + control + meaning context = sometimes
reward compound.

**Mechanism explanation**: nociception fires + endorphin response +
schema-level meaning integration → compound reward. Ritual provides:
- Pain with predictability (không random threat)
- Pain with meaning (integration into identity)
- Pain with community validation (Status reward)
- Pain with safety context (Protect drive reassured)
- Endorphin response (L1 reward)

All combine cho rewarding experience despite nociception firing.

**Comparative notes**: Reframe **doesn't need new "pain-ritual channel"
primitive**. §14.1 candidate addition unnecessary. Existing §4.2
nociception với context-dependent interpretation covers phenomenon
cleanly.

**Parsimony gain**: remove candidate channel from framework list.
Existing body-input + schema + drive framework covers phenomenon
without additional primitives.

**Verdict**: **PASS với parsimony gain**. Reframe removes need cho
additional primitive.

#### §9.2.8 B27 Vietnamese craftsman village

**Case summary**: Multi-generational craft village (lacquer, ceramic,
silk weaving), craft practiced 40+ năm per individual, transmission
to next generation, community embeddedness, reported sustained
satisfaction, longevity documented across similar Vietnamese craft
villages.

**Old framework**: Mastery + community + transmission compound
sustainable (§13.9 Example signature). Nature embedded. Multi-channel
integration.

**Reframe**:

L1 body-inputs fed richly:
- **§3.1/§3.3 Proprio + kinesthetic**: daily craft work, refined motor
  skills with variation
- **§2.1 Vision**: fractal natural + fine detail + familiar faces
- **§2.2 Audition**: ambient village sounds + voices + craft sounds
- **§2.3 Olfaction**: natural + traditional food + craft material smells
- **§2.5 Tactile**: affective touch từ sustained bonds + craft material
- **§4.7 Hormonal**: oxytocin regular, stable cortisol patterns
- **§4.9 Self-signal**: validated via community mirroring over lifetime
- **§4.8 Sleep**: regular, natural light entrained
- **§4.5/§4.6 Visceral/metabolic**: traditional whole foods

L3 drives (healthy operation):
- **Novelty drive** fed via craft progression (unbounded mastery horizon)
- **Status drive** fed via community recognition, role fulfillment,
  skill reputation — grounded trong real L1 outcomes, không empty proxy
- **Protect drive** satisfied through embedded community safety

Schema layer: Meaning inherited từ tradition (không constructed), identity
stable, cultural narrative supports pattern. **Meaning coherent via
schema embedding** rather than pursuit.

**Comparative notes**: Reframe shows **what sustainable compound looks
like at substrate level** — multiple L1 categories fed simultaneously
at ancestral-adjacent levels, drives operating healthily, schema stable.
Framework's **positive prescription** (§13.9) validated via body-input
substrate lens. Status drive healthy here precisely because grounded
in actual L1 outcomes (contrast với B2 billionaire empty status).

**Verdict**: **STRONG PASS**. Architectural grounding cho sustainable
compound signature.

#### §9.2.9 B30 Jiro Ono 99-năm mastery

**Case summary**: Jiro Ono, Tokyo sushi master, 99+ năm, still claiming
"not satisfied." Unbounded mastery horizon documented trong "Jiro Dreams
of Sushi" film. Longevity, cognitive preservation, sustained engagement.

**Old framework**: Mastery channel unbounded horizon characteristic.
Transmission via son + apprentices.

**Reframe**:

Mechanism = **Novelty drive operating on skill progression indefinitely**.
Skill mastery follows delta rule — each new level shifts baseline, needs
new micro-challenge cho reward. Jiro's "still not satisfied" is Novelty
drive continuously finding next refinement target.

L1 fed via daily skilled practice:
- **§3.1/§3.3 Proprio + kinesthetic** via refined hand motor skills
- **§2.1 Vision** via fine detail discrimination training over decades
- **§2.4 Gustation + §2.3 Olfaction** via flavor expertise development
- **§4.9 Self-signal** via competence calibration
- **§4.7 Hormonal dopamine** via Novelty drive on skill micro-progress
- **§2.5 Tactile** via daily fish handling refinement

Sustainable because:
- Multi-input L1 feeding through craft
- Social embedding (apprentices, customers, community recognition)
- **Unbounded horizon** means drive stays fed — never complete
- Stable schema (role clear)
- Transmission loop operational (son takes over)

**Critical insight**: unbounded mastery = **exploitation of Novelty
drive operating on continuously-shifting baseline** in constructive
direction. Unlike hedonic treadmill pathology (chasing new stimuli
ever-escalating), mastery uses **same mechanism** but direction is
skill refinement, not consumption escalation.

**Comparative notes**: Reframe demonstrates mechanism is **morally
neutral** — baseline shifting can be exploited pathologically (addiction
B31/B35) or constructively (mastery B27/B30). Same neural mechanism,
different direction, radically different outcomes.

**Verdict**: **PASS**. Reframe explains unbounded horizon cleanly
through Novelty + baseline mechanism.

#### §9.2.10 B31 Ultra-processed food obsession

**Case summary**: Individual develops compulsive eating of ultra-processed
food, gradual baseline distortion, metabolic syndrome, overweight,
documented widely trong obesity research. Public health epidemic scale.

**Old framework**: Food channel supernormal stimulation. Taste baseline
shifted.

**Reframe — Hall 2019 NIH study = direct experimental evidence**:

Mechanism = **classic baseline shifting measurable trong controlled trial**:
- **§2.4 Gustation** baseline shifted upward (engineered sugar/salt/fat/
  umami compounds exceed natural food levels)
- **§2.3 Olfaction** engineered flavorings shift baseline
- **§4.6 Metabolic**: leptin resistance, insulin dysregulation, ghrelin
  dysregulation
- **§4.5 Visceral**: microbiome dysbiosis, low fiber, inflammation
- **§4.7 Hormonal dopamine**: baseline shifted via reward engineering
- **§6.1 Novelty drive** hijacked via food variety (fast food menus
  engineered)

**Hall 2019 Cell Metabolism clinical trial**: same participants, same
macros + calories offered, ultra-processed diet → **+500 kcal/day
overconsumption** measurable. Direct empirical measurement của baseline
distortion mechanism. **Cannot overstate strength** của this as
experimental evidence cho reframe.

Body-Base.md §4.1.3 food channel reframes to §4.6 metabolic + §4.5
visceral + §2.4 gustation aggregate, với Novelty drive hijacking.

**Comparative notes**: Reframe matches experimental evidence cleanly.
Hall 2019 is **strongest empirical support** cho baseline adaptation
mechanism trong framework's entire research base. Mô hình cũ's "food
channel supernormal" was descriptively correct; reframe mechanism
specified operationally.

**Verdict**: **STRONG PASS**. Direct experimental validation.

#### §9.2.11 B35 Screen addiction / attention capture

**Case summary**: Individual spends 6-12+ giờ daily on screens (phone,
computer, TV), attention fragmented, sleep disrupted, emotional
regulation impaired, social relationships suffer. Generation-scale
phenomenon now.

**Old framework**: Attention channel captured (§14.1 candidate primitive).
Novelty channel overstimulated. Multi-channel starvation từ displacement.

**Reframe**:

L1 engineered supernormal across multiple inputs:
- **§2.1 Vision**: refresh rate + content density + variability
  algorithmic
- **§2.2 Audition**: engineered audio stimulation
- **§6.1 Novelty drive**: hijacked via content variability algorithms
- **§6.2 Status drive**: social media validation mechanics (likes, views)
- **§4.7 Hormonal dopamine**: intermittent reinforcement peaks engineered

L1 starved simultaneously via displacement:
- **§3.1/§3.3 Proprio/kinesthetic**: sedentary screen time
- **§2.5 Tactile affective (CT)**: no human touch while screen
- **§4.9 Self-signal interoception**: **actively suppressed by external
  attention capture** — key mechanism
- **§4.8 Sleep**: blue light + arousal → disrupted
- **§2.1 Vision natural baseline**: far-focus, fractal, natural light
  absent
- **§4.4 Cardiovascular**: sedentary low HRV
- **§2.2 Audition natural pink noise**: replaced by mechanical + content

**Attention capture mechanism reframed**: không separate "attention
channel." Phenomenon = external attention demand → prevents §4.9
self-signal interoception → body-state awareness atrophies → L1 signals
go unheard → cumulative deficit → addictive escalation từ baseline
shifting + hedonic treadmill.

§14.1 candidate primitive ("attention as meta-channel") unnecessary.
Reframe handles via existing mechanisms: §4.9 self-signal + Novelty
drive hijacking + §2-§4 L1 multi-input deprivation từ displacement.

**Comparative notes**: **Parsimony gain** — removes candidate primitive.
Attention phenomenon captured via existing architecture cleanly.
Framework doesn't need additional primitives; existing mechanisms
suffice.

**Verdict**: **PASS với parsimony gain**. Second parsimony gain (first
was B18 pain-ritual). Reframe eliminates 2 candidate primitives from
§14.1 additions list.

#### §9.2.12 B46 Richard Proenneke 30-năm Alaska

**Case summary**: Proenneke, retired mechanic, built cabin in Alaska
1968, lived solo 30 năm (to age 82), documented trong journals + films.
Thrived despite minimal social contact. Contrast với B47 Chris Knight
(awkward post-isolation), B48 McCandless (died), B50 solitary
confinement (crashes days).

**Old framework**: Nature channel rich, agent channel minimal nhưng
không zero (annual visits), meaning via self-reliance.

**Reframe**:

L1 fed richly via natural environment + daily labor:
- **§2.1 Vision**: wildlife biological motion daily, fractal landscape,
  horizon depth
- **§2.2 Audition**: natural pink noise, wildlife sounds, stream, wind
- **§2.3 Olfaction**: phytoncides, seasonal variation
- **§2.5 Tactile**: varied textures, thermal variation, ground contact
- **§3.1/§3.2/§3.3 Proprio/vestibular/kinesthetic**: cabin building,
  wood chopping, hunting, fishing daily — ancestral-matched movement
- **§4.1 Thermoreception**: daily varied, adapted over years
- **§4.8 Sleep/Circadian**: natural light entrained perfectly
- **§4.9 Self-signal**: developed strong over solo decades, no external
  attention demand
- **§4.5/§4.6 Visceral/metabolic**: self-caught/self-prepared natural
  foods

L1 minimal but not zero:
- **§2.5 Tactile affective (CT)**: minimal — letters, annual visits
- **§4.7 Hormonal oxytocin**: minimal bonding với humans, possibly bond
  với environment itself (research unclear on substitute mechanism)

L3 drives:
- **Novelty drive**: fed via seasonal/weather/wildlife variation + skill
  progression (cabin improvements continuous)
- **Status drive**: minimal external, strong self-mastery satisfaction
- **Protect drive**: embedded trong self-reliance, environmental mastery

Schema: meaning via coherent self-reliance narrative, identity stable.

**Tại sao sustainable** (contrast với B47/B48/B50):
- **Multi-input L1 rich feeding** (không B50 deprivation)
- **Chose lifestyle vs forced** (schema alignment matters)
- **Kinesthetic labor + natural environment** vs forced stillness
- **Food secure** vs starvation (B48)
- **§4.9 Self-signal developed** vs suppressed
- **Annual visits + letters** preserve minimal mirroring (vs B50 zero)

**Comparative notes**: Reframe explains **tại sao one person thrived
30 năm while others crashed** at fine-grained L1 analysis level. Mô
hình cũ's "nature rich, agent minimal" couldn't explain specific case
outcomes. Reframe: 8-9 L1 categories fed at ancestral-adjacent levels
+ mastery engine cho Novelty + self-signal developed = sustainable
compound. **Specific L1 profile matters more than coarse channel
counts**.

**Verdict**: **STRONG PASS**. Distinguishes sustainable solo pattern
từ pathological solo at architectural level.

#### §9.2.13 B50 Solitary confinement

**Case summary**: Long-term solitary confinement, severe psychological
damage documented (Grassian 2006). Rapid crash trong days-weeks,
permanent damage sau months-years. UN classifies prolonged solitary
as torture.

**Old framework**: All silent channels starved simultaneously. Multi-
channel deprivation.

**Reframe**:

**Multi-input simultaneous deprivation across almost all L1 categories**:

- **§2.1 Vision**: static cell, no biological motion, no depth, no
  fractal
- **§2.2 Audition**: isolation + occasional mechanical noise
- **§2.3 Olfaction**: sterile, minimal variation
- **§2.4 Gustation**: institutional food, minimal variation
- **§2.5 Tactile affective**: extreme CT fiber deprivation
- **§3.1/§3.2/§3.3 Proprio/vestibular/kinesthetic**: restricted 6m²
- **§4.1 Thermoreception**: controlled, no variation
- **§4.3 Respiratory**: poor ventilation often
- **§4.7 Hormonal cortisol**: chronic elevation
- **§4.8 Sleep**: disrupted by artificial light + noise + cell checks
- **§4.9 Self-signal**: initially high (only thing to read), degrades
  từ rumination + trauma
- **§4.6 Metabolic**: L0 adequate but minimal reward

L3 drives:
- **Novelty drive**: starved, no variation to fire on
- **Status drive**: deprivation of agent validation, dignity stripped
- **Protect drive**: chronic activation, no safety context

Schema: threat chronic, identity erosion.

**Crash speed via §5.5 formula**: depth × breadth × L0 proximity.
Solitary = extreme depth (multiple inputs near-zero) × extreme breadth
(most L1 starved) → fastest crash pattern documented. Sometimes crosses
L0 via suicide.

**Contrast với B46 Proenneke** (same "isolation" surface label, radically
different L1 profile):
- Proenneke: rich natural multi-input feeding, chose, kinesthetic
  active, stable food
- B50: multi-input deprivation, forced, restricted, controlled

Reframe makes distinction **architectural, not just descriptive**.

**Comparative notes**: Reframe identifies specifically which L1
categories starved, explains extreme crash severity, explains tại sao
B46 sustainable while B50 crashes. Same "isolation" word, entirely
different substrate profile.

**Verdict**: **STRONG PASS**. Multi-input compound deprivation mechanism
explains pattern severity + provides contrast framework.

#### §9.2.14 DC1 Tesla + Leonardo contrast (Deep-Cases)

**Case summary**: Nikola Tesla late-life isolation, hotel rooms, financial
instability, parasocial bond với pigeons, cognitive decline. Contrasted
với Leonardo da Vinci old age — patronage, community, transmission,
sustained mastery. Both mastery-dominant creatives, radically different
outcomes. DC1 deep-case analyzed via multi-angle triangulation.

**Old framework**: Tesla = mastery + community + transmission compound
absent. Leonardo = compound present. §13.9 sustainable compound
signature.

**Reframe**:

Tesla late-life L1 profile:
- **§2.1 Vision**: hotel room, minimal biological motion (partial từ
  pigeons)
- **§2.2 Audition**: urban mechanical + limited voices
- **§2.3 Olfaction**: minimal variation
- **§2.5 Tactile affective (CT)**: minimal — pigeon touch không human
  CT equivalent
- **§4.7 Hormonal**: chronic cortisol từ financial stress, minimal
  oxytocin
- **§4.9 Self-signal**: probably high nhưng increasingly isolated từ
  validation
- **§4.4 Cardiovascular**: decline documented
- **§4.8 Sleep**: documented insomnia
- **§4.5/§4.6 Visceral/metabolic**: poor nutrition

Leonardo old-age L1 profile:
- All similar categories fed via patronage environment
- Community daily (students, patrons, household)
- Affective touch sustained relationships
- Oxytocin via bonding
- §4.9 self-signal validated via community mirroring
- Stable nutrition, sleep, environment
- Craft continuous

Both mastery-dominant, **differential = L1 body-input aggregate access**
+ **Status drive healthy (embedded) vs pathological (isolated
pursuit)**.

**DC1 critical finding**: patronage as **channel-supporting infrastructure**,
không channel itself. Reframe integration: patronage = environment that
enables stable L1 supply + community mirroring + status stability. Operates
on body-input substrate indirectly through social structure.

Multi-angle triangulation identified 10 candidate variables. Reframe
interpretation: **multiple L1 variables differ simultaneously**, không
single channel difference.

**Comparative notes**: Reframe shows mastery alone doesn't determine
outcome — **L1 substrate stability matters**. Both were masters; only
one had sustaining substrate environment. Maps cleanly to §13.9
sustainable compound. Patronage mechanism clarified.

**Verdict**: **STRONG PASS**. Deep case multi-angle methodology validates
reframe via substrate differential.

#### §9.2.15 DC3 ancestral nomad vs digital nomad (Deep-Cases)

**Case summary**: Hunter-gatherer và pastoralist nomads (!Kung, Hadza,
Inuit, Saami, Mongols, Bedouin, Maasai, Roma, Tibetan, Aboriginal)
documented sustainability over millennia. Digital nomads commonly crash
năm 7-12. Both "nomadic" at surface level but radically different
outcomes. DC3 deep-case analyzed via differential analysis.

**Old framework**: Movement channel fed both, agent channel differs.
§13.6 multi-scale collective architecture relevant.

**Reframe — 10-variable differential**:

Ancestral nomad L1 profile:
- **§2 exteroception**: all fed via natural environment (fractal D,
  pink noise, phytoncides, varied thermal)
- **§2.5 Tactile affective**: daily via tribe
- **§3 proprio/kinesthetic**: daily labor + walking + varied terrain
- **§4.4/§4.3 cardio/respiratory**: adapted
- **§4.7 Hormonal**: stable oxytocin via tribal bonding, cortisol cyclical
- **§4.8 Sleep**: natural entrained, co-sleeping
- **§4.9 Self-signal**: developed via lifetime mirroring trong stable
  community
- **§4.5 Visceral**: traditional microbiome stable over generations
- **§4.6 Metabolic**: seasonal cycles matched

Digital nomad L1 profile:
- **§2 exteroception**: varied nhưng không ancestral-matched
- **§2.5 Tactile affective**: sparse (casual encounters, paid services)
- **§3 proprio/kinesthetic**: typically **SEDENTARY** laptop work despite
  travel context
- **§4.7 Hormonal oxytocin**: minimal sustained bonding
- **§4.9 Self-signal**: erodes từ lack of consistent mirroring
- **§4.5 Visceral**: microbiome challenges constant ("traveler's stomach")
- **§4.8 Sleep**: jet lag, disrupted
- **§6.1 Novelty drive**: hijacked via travel supernormal

**6-8 features differ simultaneously**. "Movement/travel" activity
context misleading — ancestral nomads moved embedded trong community
với rich L1 substrate; digital nomads move through **L1 deserts**.

**DC3 framework finding**: "movement" = activity context, không body-
base channel. Reframe validates: movement serves multiple L1 inputs
(proprio/kinesthetic/vestibular/cardiovascular) only when ancestral-
pattern embedded. Digital nomad movement doesn't serve same inputs
because surface context sits on different substrate.

**"Freedom" ideology masks starvation**: schema narrative explains
subjective justification despite accumulating deficit (parallel đến
B5 karoshi cultural amplification, different schema content).

**Comparative notes**: Reframe provides **differential variable
analysis** directly. 10 variables mapped to L1 + drives + schema.
Multi-variable compound failure identified. Mô hình cũ's channel
framework couldn't express này distinction — reframe's substrate
granularity required.

**Verdict**: **STRONG PASS**. Deep case methodology explicitly validates
reframe approach.

### §9.3 Coverage report

Tabulation của 15 selected cases test results.

#### §9.3.1 Summary table

| Case  | Title                          | Category                      | Verdict          |
|-------|--------------------------------|-------------------------------|------------------|
| B1    | Workaholic burnout             | Achievement/multi-input starve| PASS             |
| B2    | Billionaire post-wealth empty  | Status proxy mechanism        | STRONG PASS      |
| B5    | Karoshi (Japanese overwork)    | Cultural amplification + L0   | PASS             |
| B6    | Digital nomad long-term        | Agent depth vs breadth        | STRONG PASS      |
| B11   | Codependent                    | §4.9 self-signal primary      | STRONG PASS      |
| B13   | Love addict                    | Baseline shifting mechanism   | PASS             |
| B18   | Body mod / pain ritual         | Context-dependent nociception | PASS + parsimony |
| B27   | Vietnamese craftsman village   | Sustainable compound          | STRONG PASS      |
| B30   | Jiro 99-năm mastery            | Unbounded Novelty direction   | PASS             |
| B31   | Ultra-processed food           | Hall 2019 direct evidence     | STRONG PASS      |
| B35   | Screen addiction               | Attention capture mechanism   | PASS + parsimony |
| B46   | Proenneke 30-năm Alaska        | Sustainable solo              | STRONG PASS      |
| B50   | Solitary confinement           | Multi-input crash             | STRONG PASS      |
| DC1   | Tesla + Leonardo contrast      | Substrate differential        | STRONG PASS      |
| DC3   | Ancestral vs digital nomad     | Differential 10-variable      | STRONG PASS      |

#### §9.3.2 Distribution analysis

**Verdict distribution**: 15/15 PASS, 0 PARTIAL, 0 FAIL.

Breakdown:
- **STRONG PASS**: 9 cases (60%) — reframe significantly clearer than
  mô hình cũ, adds architectural precision
- **PASS with parsimony gain**: 2 cases (13%) — reframe eliminates
  candidate framework primitive (pain-ritual channel, attention meta-
  channel)
- **PASS**: 4 cases (27%) — reframe equally good, no loss, mechanism
  clearer

**No FAIL, no PARTIAL identified trong selected 15 cases**. Reframe
passes test criterion §1.4.1(3) — case coverage comprehensive.

#### §9.3.3 Pattern observations across cases

**Pattern 1 — Reframe consistently adds precision**:
Mô hình cũ described patterns at channel aggregation level. Reframe
consistently specifies:
- **WHICH** specific L1 categories starved/fed
- **HOW** L3 operators interact với L1
- **MECHANISM** của baseline adaptation
- **WHY** crash speed/severity varies (§5.5 formula)

No case where mô hình cũ was more precise than reframe.

**Pattern 2 — Sustainable vs pathological distinction clearer**:
B27 (sustainable craftsman), B30 (sustainable mastery), B46 (sustainable
solo) all contrasted với pathological equivalents (B1 workaholic,
B13 love addict, B50 solitary) at body-input substrate level. **Multi-
input L1 feeding + healthy drive operation** = sustainable. **Multi-
input starvation + drive hijacking** = pathological. Same mechanism,
different directions.

**Pattern 3 — "Surface label" misleading**:
Cases sharing surface labels ("nomad", "isolation", "mastery pursuit")
radically different at substrate level:
- B46 Proenneke vs B50 solitary (both "isolation") — opposite L1
  profiles
- DC3 ancestral vs digital nomad (both "nomadic") — opposite L1
  substrates
- B30 Jiro vs B26 scholar (both "mastery", B26 not tested but noted trong
  §13 Example table) — opposite community embedding

Reframe's substrate granularity **enables distinction** that channel
framework couldn't express cleanly.

**Pattern 4 — Empirical evidence supports mechanism**:
- **Hall 2019 NIH** (B31) = direct experimental validation của baseline
  shifting
- **Fisher fMRI** (B13) = direct neural validation của limerence baseline
- **Grassian 2006** (B50) = solitary research supports multi-input
  compound crash
- **Marmot Whitehall** (implicit B1/B5) = status → L1 pathway
- **Bird & Cook 2013** (B11) = alexithymia research validates §4.9
  self-signal category
- **Harlow, Romanian orphans** (via B19 touch reference) = touch as
  L1 input

Framework không invoking mechanisms absent từ research literature —
synthesizing established findings.

**Pattern 5 — Parsimony gains real**:
2 candidate primitives eliminated (pain-ritual, attention meta-channel).
Reframe reduces framework complexity while maintaining explanatory
power. Occam's razor favor.

**Pattern 6 — §4.9 self-signal interoception architecturally central**:
B11 codependent, B12 parentified, B15 helicopter parent (developmental
originator), B35 screen addiction (attention capture erodes self-signal),
B1 workaholic burnout (suppression), B25 contemplative (training) —
**many cases' crux involves self-signal deficit or repair**. Validates
§4.9 as architectural keystone, not just one-of-many inputs.

#### §9.3.4 Assessment coverage criterion

Test criterion §1.4.1(3): "Case coverage — most cases PASS or PARTIAL,
zero FAIL."

**Actual result**: 15/15 PASS (100%), exceeds criterion requirement.

Reframe **passes §1.4.1(3) case coverage criterion** with margin.

No test case invalidated reframe. Cases that might have been FAIL
candidates (meaning-dominant) were clarified by reframe (meaning =
schema layer, not body-input cluster) rather than failing.

### §9.4 Gaps found

Despite 15/15 PASS outcome, honest assessment identifies **5 real gaps**
requiring additional framework work. These không invalidate reframe but
specify areas where reframe needs patches, clarifications, hoặc scope
limits.

#### §9.4.1 Gap 1 — Meaning cases not directly tested

**Issue**: §9 selected 15 cases không include B21-B23 religious fanatic,
B22 cult member, B24 terminal illness meaning reorientation — cases
where meaning pursuit is primary dynamic. Meaning-dominant cases were
identified trong §9.1 as "challenge candidates" but not actually tested.

**Why this is a gap**: reframe claims meaning = primarily schema layer,
không body-input cluster (§8.2.3). This is strong architectural claim
mà should be tested against meaning-dominant cases explicitly.

**Mitigation**: §8.2.3 analysis of meaning channel → schema layer
mapping is **descriptive**, không proven. Gap cannot be closed without
case-level test of meaning-dominant patterns.

**Severity**: MEDIUM. Framework scope clarification at stake. Reframe
might need meaning-case patches hoặc explicit scope limitation statement.

**Recommended action**: Phase C Body-Base.md fill should include
meaning-case analysis section using selected B21-B24 cases. Alternatively,
next round của §9 testing should include these 3-4 meaning cases.

#### §9.4.2 Gap 2 — Collective architecture cases reduction question

**Issue**: B14 Vietnamese extended family, B27 craftsman village, B40
Rothschild multi-generational dynasty, B9 Blue Zone farmer — sustainable
cases operating at **collective scales** (family, village, dynasty,
community). §13.6 Example explicitly documents multi-scale phenomenon.

**Question**: Do these reduce to individual body-input feeding (reframe
substrate level)? Hoặc is collective structure itself a level framework
should preserve?

**Reframe's current stance** (§0.2 bypassed): collective architectures
orthogonal đến substrate reframe. This is a **scope decision**, không
resolution.

**Honest gap**: reframe doesn't clearly specify WHICH aspects of B14/B27/
B40 reduce to individual L1 feeding vs emerge from collective structure.
E.g., does B40 Rothschild multi-generational project feed "meaning" at
individual level via schema extension, hoặc create collective structure
that serves individual L1 through non-individual mechanism?

**Mitigation**: reframe acknowledges this is scope limitation.
Individual-level substrate analysis doesn't preclude collective emergent
phenomena at higher scales. Both can be valid at their own levels.

**Severity**: MEDIUM. Affects framework completeness but not substrate
validity.

**Recommended action**: future framework work should document multi-
scale relationship explicitly. Body-Base.md Phase C should include
"multi-scale architectures" section referencing §13.6 findings. Reframe
substrate level can coexist với collective level framework.

#### §9.4.3 Gap 3 — Evolutionary explanation for Status drive strength

**Issue**: Reframe claims Status drive = PFC proxy, không body-input.
Nhưng Status drive feels enormously powerful (B2/B36/B38/B40 cases show
individuals pursuing status for decades, often at cost of L1 feeding).
**Tại sao proxy is so strong?**

**Current reframe explanation** (§6.2.2): PFC learns status → L1 supply
correlation over development, generalizes to abstract status markers.
But this doesn't fully explain **why evolution selected for status
pursuit so strongly** if it's "just" a proxy.

**Possible resolution** (not yet developed):
- Evolution directly selected cho status pursuit because status
  reliably correlated với L1 access trong ancestral environment
- Status-pursuit genes propagated even though status itself has no
  receptor — because status pursuers accessed more L1 resources
- Evolved default to seek status ~= evolved default to seek food (both
  indirect paths to L1 stability)

**Research needed**: comparative primate research on dominance hierarchies,
mortality correlations với social rank (Sapolsky baboons, Marmot
Whitehall), evolutionary psychology literature.

**Severity**: LOW-MEDIUM. Reframe works functionally without resolving
này, but theoretical completeness would benefit.

**Recommended action**: §6.2 could be expanded với evolutionary psychology
section. Body-Base.md Phase C should include cross-references đến
evolutionary psychology primate research.

#### §9.4.4 Gap 4 — Schema-body coupling mechanism needs clarification

**Issue**: Reframe distinguishes body-input dissonance (L1) from schema
dissonance (PFC level) cleanly (§7). But **mechanism của coupling**
giữa these two layers remains vague.

**Observed coupling**:
- Meaning loss → body dissonance ("lạc lõng")
- Chronic schema anxiety → L1 cortisol → cardiovascular damage
- L1 deficit → schema interpretation shift ("I'm tired → I'm failing")
- Schema success → L1 dopamine reward
- Body feedback shapes PFC predictions (predictive processing)

**Current framework hints**: Predictive processing (Seth, Barrett,
Clark) framework suggests schema-body coupling via active inference —
body signals become priors for PFC, PFC predictions shape body
responses. Bidirectional tight coupling.

**Gap**: Body-Input-Enumeration.md doesn't fully integrate predictive
processing framework. §4.9 self-signal interoception references Seth/
Barrett but doesn't elaborate active inference fully.

**Severity**: MEDIUM. Theoretical completeness gap.

**Recommended action**: Future work (Body-Base.md Phase C hoặc separate
file) should integrate predictive processing framework more thoroughly.
Active inference gives formal mechanism cho schema-body coupling.

#### §9.4.5 Gap 5 — Individual calibration variation documentation

**Issue**: Reframe claims variation lives at substrate (baseline) level
rather than channel existence level (§5.2.5). Cleaner than mô hình cũ's
§13.3 "channel existence universal, individual calibration variable."

**Nhưng**: reframe doesn't provide **how much variation is normal** vs
pathological vs within-range. B20 asexuality extreme example: is that
within normal human baseline range, hoặc at edge extreme? Framework
should specify.

**Current state**: §5.1 mentions "within evolved bounds" but doesn't
specify bounds. §5.2 describes mechanism của shifting without specifying
magnitude variance normative ranges.

**Gap**: framework lacks quantitative specification của normal baseline
variance. Probably needs biological measurement beyond framework scope.

**Severity**: LOW. Framework scope boundary, không invalidation.

**Recommended action**: Body-Base.md Phase C should acknowledge scope
limit explicitly. Future AI-enabled monitoring may provide quantitative
baselines.

#### §9.4.6 Gap summary

**5 gaps identified**:
1. Meaning cases not directly tested (MEDIUM severity)
2. Collective architectures reduction question (MEDIUM)
3. Status drive strength evolutionary explanation (LOW-MEDIUM)
4. Schema-body coupling mechanism via predictive processing (MEDIUM)
5. Quantitative baseline variation specification (LOW)

**None are FAIL-level**. All are either:
- **Scope limitations** to acknowledge explicitly
- **Additional work** to complete in Phase C hoặc future files
- **Research integration** from other traditions (evolutionary psych,
  predictive processing)

Reframe **passes test criteria overall** but với honest gap
acknowledgment. Phase C Body-Base.md fill should address gaps 1-4 as
part of foundation file work.

**Gap 5 (quantitative variation)** is likely beyond framework's
descriptive scope and requires biological measurement research.
Framework should state explicit scope limit.

### §9.5 Verdict per case

Summary verdict across 15 selected cases + implications cho §12
overall verdict.

#### §9.5.1 Verdict categories used

- **STRONG PASS**: reframe significantly clearer than mô hình cũ,
  adds architectural precision, mechanism cleaner
- **PASS với parsimony gain**: reframe explains case AND eliminates
  candidate framework primitive
- **PASS**: reframe equally good as mô hình cũ, mechanism clearer,
  no loss
- **NEUTRAL**: reframe equivalent to mô hình cũ, neither adds nor
  loses (not used — no case fell in này category)
- **PARTIAL FAIL**: reframe needs patch to handle case (not used)
- **FAIL**: reframe cannot explain without adding epicycles (not used)

#### §9.5.2 Final verdicts per case

```
  STRONG PASS (9 cases):
    B2   Billionaire post-wealth emptiness
    B6   Digital nomad long-term
    B11  Codependent (§4.9 self-signal primary)
    B27  Vietnamese craftsman village
    B31  Ultra-processed food (Hall 2019 evidence)
    B46  Proenneke 30-năm Alaska
    B50  Solitary confinement
    DC1  Tesla + Leonardo contrast
    DC3  Ancestral vs digital nomad

  PASS với parsimony gain (2 cases):
    B18  Body modification / pain ritual
    B35  Screen addiction / attention capture

  PASS (4 cases):
    B1   Workaholic burnout
    B5   Karoshi
    B13  Love addict
    B30  Jiro 99-năm mastery
```

**15/15 PASS. 0 FAIL. 0 PARTIAL.**

#### §9.5.3 Pattern interpretation

**Strong pass dominance (60%)**: reframe significantly better than mô
hình cũ trong 9/15 cases. Not marginal improvement — substantial
architectural clarity gained. Pattern suggests reframe is not just
"equally good" reformulation but genuinely improved framework.

**Parsimony gains (13%)**: 2 candidate primitives eliminated (pain-
ritual, attention meta-channel). Reframe reduces framework complexity
while maintaining explanatory power. Rare combination — most framework
revisions trade parsimony for explanation.

**No failures**: tested 15 cases chosen for diversity (pathological vs
sustainable, different channel starvations, different confidence levels,
Deep-Cases), reframe handled all. Strong evidence of architectural
validity.

#### §9.5.4 Framework-level implications

**For §12 verdict**: §9 test results strongly support **Option A —
COMMIT** reframe (rewrite Body-Base.md Phase C using substrate model).
No cases identified suggesting reject hoặc even patch path.

**Honest qualifiers**:
- Meaning cases not directly tested (§9.4.1 gap) — commit với explicit
  future work on meaning-dominant cases
- 5 gaps identified (§9.4.6) — commit với acknowledgment, plan to
  address in Phase C hoặc future work
- No empirical contradictions found

**Framework recommendation**: proceed với Body-Base.md Phase C rewrite
using reframe substrate model. Address gaps as part of Phase C content
fill. Preserve existing framework files (Body-Base-Example.md, Deep-
Cases.md, Why-Body-Knows.md, Body-Dissonance.md, Empathy-Mirror.md,
Feeling/ folder) as-is — reframe integrates with them without breaking.

#### §9.5.5 Confidence assessment

**Confidence level in reframe validity**: HIGH, based on:

1. **Empirical evidence**: Hall 2019 NIH direct experimental validation
2. **Research integration**: 50+ citations across independent traditions
   (adaptation psychology, learning theory, supernormal stimulus,
   interoception, neuroscience, economics)
3. **Case coverage**: 15/15 PASS includes historical + contemporary,
   pathological + sustainable, individual + collective
4. **Parsimony gains**: 2 primitives eliminated
5. **Internal consistency**: §5 mechanism + §6 drives + §7 dissonance
   remap + §8 channel shorthand all coherent
6. **Backward compatibility**: existing framework preserved

**Remaining uncertainty**: 5 gaps identified (§9.4), primarily requiring
additional theoretical integration (predictive processing) hoặc
additional testing (meaning cases) hoặc acknowledging scope limits
(quantitative variation).

**Confidence**: sufficient để commit reframe as Phase C architectural
foundation. Not so high as to claim "final framework" — science is
iterative.

---

**§9 TEST AGAINST PHASE B CASES — section complete**

Key findings:
1. **15/15 PASS** distribution
2. **No FAIL** identified despite diverse case selection
3. **Reframe significantly clearer** trong 60% của cases
4. **2 parsimony gains** eliminate candidate primitives
5. **5 gaps acknowledged** honestly, not invalidating
6. **Empirical evidence** from Hall 2019 + multiple research traditions
7. **Recommendation**: proceed with Commit verdict in §12

**§9 passes test criterion §1.4.1(3)** — case coverage criterion met
với margin.

Ready cho §10 integration với existing framework, §11 honest assessment,
§12 verdict, §13 sources.

---

## §10 — INTEGRATION WITH EXISTING FRAMEWORK

### §10.1 Why-Body-Knows.md relationship

**Relationship**: COMPATIBLE + REFINED. Reframe không contradict Why-
Body-Knows, specifies its substrate explicitly.

#### §10.1.1 4-tier calibration theory unchanged

Why-Body-Knows §4 describes **4 tiers của body calibration**:
- **Tier 1 evolution** (2M năm): gene-level calibration cho ancestral
  environment
- **Tier 2 development** (individual lifetime): personal calibration
  via experience
- **Tier 3 culture** (transgenerational): shared calibration via
  tradition + language + teaching
- **Tier 4 AI** (current): rapid chunk access accelerating Tier 3

**Reframe stance**: 4-tier theory unchanged. Reframe **specifies WHAT
gets calibrated**: body-input baselines (§5.1-§5.2).

#### §10.1.2 Baseline adaptation maps onto Tier 2

Reframe §5 baseline adaptation mechanism is explicit **Tier 2 mechanism**:
- Individual development shifts baselines within evolved bounds
- 4 sub-mechanisms (neural adaptation, receptor sensitivity, habituation,
  schema calibration) documented trong §5.2
- Delta rule formalism provides quantitative Tier 2 specification
- Novelty operator (§5.3) is the drive mechanism

Why-Body-Knows described Tier 2 at high level; reframe §5 provides
substrate-level mechanism. **Complementary, không conflicting**.

#### §10.1.3 Why body check is reliable — reframe strengthens argument

Why-Body-Knows core claim: body signals are reliable because 4 tiers của
calibration ensure body reward system ≈ domain reward system via proxy.

**Reframe strengthens**:
- **Specifies WHICH signals are calibrated**: body-input substrate
- **Clarifies MECHANISM**: baseline adaptation + Novelty drive + drives
  operating on substrate
- **Identifies failure mode**: evolution lag (§1.2 mismatch table, §5.1.5)
  — modern environment deviates từ ancestral baseline across all
  inputs simultaneously
- **Explains reliability limits**: body signals ĐÚNG for ancestral
  environment, less reliable cho modern supernormal stimuli where
  baseline shifting exploited

#### §10.1.4 Body-input substrate as calibration target

Key integration: Why-Body-Knows asks "tại sao body biết?" — answers via
4-tier calibration. Reframe asks "cái gì được calibrated?" — answers
body-input baselines.

Together:
- **Why**: body trustworthy → 4 tiers calibration
- **What**: body-input substrate baselines → reframe §5
- **How**: Novelty drive + delta rule + asymmetric decay mechanism
- **When reliable**: ancestral-adjacent environments
- **When unreliable**: supernormal stimuli hijacking baseline

**No contradiction, no replacement**. Reframe integrates với Why-Body-
Knows at substrate level without breaking theory.

#### §10.1.5 Integration action item

Phase C Body-Base.md should cross-reference Why-Body-Knows.md §4 explicitly
when introducing body-input baselines + §5 mechanism. Why-Body-Knows
file itself does không need changes — reframe work happens trong
Body-Base.md foundation file.

### §10.2 Body-Dissonance.md relationship

**Relationship**: COMPATIBLE + EXTENDED. Reframe builds directly on
Body-Dissonance framework, adds substrate mapping.

#### §10.2.1 3-signal structure unchanged

Body-Dissonance describes 3 body signals:
- **Body-Satisfaction**: "đủ rồi, dừng" — homeostasis met
- **Body-Reward**: "hay, tiếp tục" — harmony building
- **Body-Dissonance**: "chưa ổn, thay đổi" — mismatch detected

**Reframe stance**: signal architecture unchanged. 3 signals continue
operating as documented. Reframe adds specificity về substrate generating
these signals.

#### §10.2.2 6 sources re-mapped (§7.1 this file)

Body-Dissonance §2.5 documented 6 nguồn dissonance. Reframe §7.1
re-mapped cleanly:
- **Body-input layer** (L1): Source 2 body-state delta, Source 4
  physical damage, Source 5 social damage
- **Schema layer** (PFC): Source 1 information mismatch, Source 3
  threat schema, Source 6 melody learning

**3+3 split** provides cleaner categorization than mô hình cũ's flat
6-source list. Reframe makes explicit the two mechanisms feeding
PFC "khó chịu" observation — body-input dissonance + schema dissonance
— that had different resolution paths but weren't architecturally
distinguished.

#### §10.2.3 14-level spectrum re-mapped (§7.2 this file)

Body-Dissonance §2 documents 14-level spectrum từ micro (lấn cấn) đến
emergency (ngất, panic). Reframe §7.2 mapped intensity to layer:
- Emergency → L0/L1 extreme
- Mạnh → L1 strong or schema strong
- Trung bình → L1 moderate or schema mismatch
- Nhẹ → schema dominant or mild L1

Pattern: intensity correlates với layer (L0/L1 loud, schema softer).
Evolutionary logic: survival-critical signals louder.

#### §10.2.4 Dissonance mechanism unchanged, substrate clarified

Body-Dissonance described dissonance as signal mechanism. Reframe
clarifies **substrate producing dissonance** but không changes mechanism
itself. Hormones, neural pathways, intensity levels all identical.

Key addition: **§4.9 self-signal interoception** as body's capacity
để read own state. Without §4.9 functional, other dissonance signals
fire nhưng PFC doesn't hear → silent deficits (mô hình cũ's §6
"silent deficiency phenomenon" concept gets mechanism).

#### §10.2.5 Integration action item

Body-Dissonance.md file itself doesn't need changes. Phase C Body-Base.md
should reference:
- Body-Dissonance §2.5 (6 sources) trong reframed §7.1 format
- Body-Dissonance §2 (spectrum) trong reframed §7.2 format
- Add §4.9 self-signal interoception concept as prerequisite
- Silent deficiency phenomenon (Body-Base.md §6 outline) explained via
  §4.9 erosion mechanism

**Body-Dissonance.md preserved as specialized signal layer file**,
complementary to substrate file.

### §10.3 Empathy-Mirror.md relationship

**Relationship**: COMPATIBLE — Empathy-Mirror dọn đường cho reframe.

#### §10.3.1 Precedent: empathy as mechanism, không channel

Empathy-Mirror.md đã explicit treat empathy as **MECHANISM**, không
channel. Quote từ Empathy-Mirror.md §1:

> "Empathy-Mirror = cơ chế body tạo bản sao body-state của sinh vật
> khác trong body mình... Empathy KHÔNG phải channel (không phải
> body-need)... Empathy feed vào channels đã có."

**Reframe extends cùng logic to all channels**: if empathy is mechanism
not channel, tại sao stop there? Reframe generalizes: **all "channels"
are aggregates/mechanisms operating on lower-level substrate (body-
inputs)**.

Empathy-Mirror dọn đường cho reductive move at broader framework level.
Reframe completes pattern Empathy-Mirror started.

#### §10.3.2 Mirror feeds body-inputs, không channels

Empathy-Mirror described mirror as feeding "channels." Reframe updates:
mirror feeds **body-inputs via mirrored body-state replication**.

Mechanism trong reframe:
1. Observe other being trong body-state (hungry, cold, suffering,
   euphoric, etc.)
2. Empathy-Mirror creates **bản sao yếu hơn** của other's body-state
   trong own body
3. Own body-inputs (§2-§4) fire ở lower intensity than direct experience
4. Mirrored state generates own L1 signal (dissonance or reward)
5. Drives operate on mirrored state: Protect drive extends,
   Novelty/reward activates

Specifics của which body-inputs fire depend on which other body-state
mirrored:
- See hungry child → own metabolic (§4.6) + visceral (§4.5) fire weakly
- See suffering → own nociception (§4.2) fire weakly (Eisenberger 2003
  social pain research)
- See euphoria → own hormonal (§4.7) dopamine/oxytocin fire weakly
- See fear → own threat response + cortisol (§4.7) fire
- See love/bonding → own oxytocin fire

**Framework integration**: mirror creates proxy L1 firing at lower
amplitude than direct experience, via same neural substrates used cho
direct experience. Consistent với Why-Body-Knows §3 finding về
simulate using same pathways as real experience.

#### §10.3.3 Protect drive extension via mirror (§6.3)

§6.3 Protect drive section integrates này specifically:
- Mirror provides weak copy của other's threatened state
- Own L1 fires weakly
- Protect drive extends to "protect other's L1" via mirror mechanism
- Action resolves mirrored dissonance by resolving other's actual state

Explains **helping behavior without mysterious altruism** — reduces to
body-input mirroring + Protect drive response.

User's "giúp bộ đội có gạo" question answered via Empathy-Mirror +
Protect drive + schema group extension (§6.3.3).

#### §10.3.4 Integration action item

Empathy-Mirror.md file doesn't need changes. Phase C Body-Base.md
should:
- Reference Empathy-Mirror.md as mechanism precedent (first framework
  file to treat phenomenon as mechanism not channel)
- Integrate empathy mechanism trong §6.3 Protect drive coverage
- Cross-reference cho explaining pro-social behavior via body-input
  mirroring

**Empathy-Mirror.md preserved as specialized mechanism file**. Reframe
extends its logic without breaking its claims.

### §10.4 Feeling folder relationship

**Relationship**: COMPATIBLE + ANCHORED. Feeling folder describes PFC
observation layer; reframe anchors substrate layer. Two different
architectural levels, complementary.

#### §10.4.1 Feeling folder content recap

Feeling/ folder (~6,924 lines across 4 files: Feeling.md, Feeling-
Sources.md, Feeling-Accuracy.md, Feeling-Research.md + Self-Pattern-
Match.md, Pattern-Resonance.md, Feel-Development.md, Feel-Example-Draft.md)
describes:
- **7-layer feeling system**: evolutionary framing của feeling as PFC
  observation interface
- **Self-Pattern Match + Pattern Resonance**: replacement of "mirror
  metaphor" với specific mechanisms
- **5-axis development trajectory**: how feeling capacity develops
- **Math analogy**: conceptual modeling frame
- **124 feeling examples**: empirical grounding
- **PFC observation interface**: feeling = how PFC reads body state

#### §10.4.2 Feeling as observation layer, body-input as substrate layer

**Two different architectural layers**:

**Body-Input substrate** (this file, §2-§4):
- WHAT body inputs exist
- HOW baselines calibrate
- WHICH receptors generate signals
- Mechanism-level description

**Feeling observation** (Feeling/ folder):
- HOW PFC accesses body state
- WHAT feelings emerge từ body state observation
- WHICH modalities + accuracy dimensions exist
- Experience-level description

**Relationship**: feeling = PFC observing body-input substrate. Feeling
folder describes observation mechanism; Body-Input-Enumeration describes
what's observed.

#### §10.4.3 §4.9 self-signal interoception as biological basis

Reframe's **§4.9 self-signal interoception** (architectural keystone)
is biological substrate cho Feeling folder work:
- Feeling = PFC reading body state
- §4.9 = body's capacity to read itself
- Without §4.9 functioning, there's nothing cho PFC to read
- Alexithymia (Bird & Cook 2013) = §4.9 deficit → feeling impairment

**Self-Pattern Match + Pattern Resonance** (Feeling folder concepts)
rest on §4.9 foundation. Body must first sense its own state (§4.9)
before PFC can pattern-match that state against chunks (Feeling layer).

#### §10.4.4 Complementary not competitive

Feeling folder documented ~6,924 lines. Reframe substrate work ~8,700
lines (this file). **Not competing frameworks** — addressing different
architectural levels:

| Question                      | File                                |
|-------------------------------|-------------------------------------|
| What substrate exists?        | Body-Input-Enumeration.md (this)    |
| How does substrate adapt?     | Body-Input-Enumeration.md §5        |
| How does PFC observe body?    | Feeling/ folder                     |
| What feelings emerge?         | Feeling/ folder                     |
| Why body signals trusted?     | Why-Body-Knows.md                   |
| How body signals mismatch?    | Body-Dissonance.md                  |
| How body mirrors others?      | Empathy-Mirror.md                   |

Each file addresses specific architectural question. Framework coherent
across multiple files without redundancy.

#### §10.4.5 Integration action item

Feeling folder files don't need changes. Phase C Body-Base.md should:
- Reference Feeling/ folder as observation interface layer
- Clarify §4.9 self-signal interoception as biological basis cho feeling
- Cross-reference để complete framework picture
- Point learners to Feeling folder cho observation-level deep dive

**Feeling folder preserved as specialized observation interface**
complementary to substrate file.

### §10.5 Body-Base.md Phase C dưới reframe

Nếu reframe commits (§12 recommendation), Body-Base.md Phase C content
fill should restructure around substrate model while preserving existing
framework integration.

#### §10.5.1 Recommended Body-Base.md restructure

**Current Body-Base.md outline structure** (from earlier read):
```
§0  VỊ TRÍ TRONG FRAMEWORK
§1  ĐỊNH NGHĨA BODY-BASE
§2  3 BODY SIGNALS
§3  4 LAYERS OF CALIBRATION
§4  BODY-BASE CHANNELS (§4.1 Loud/Acute, §4.2 Silent/Slow-Decay,
    §4.3 Higher-Order)
§5  SIGNAL TIMELINE MODEL
§6  SILENT DEFICIENCY PHENOMENON
§7  STORAGE + DECAY + PATTERN FIRE MODEL
§8  CROSS-CHANNEL INTERACTIONS
§9  INDIVIDUAL VARIATION (Extreme Profiles)
§10 CULTURAL VARIATION
§11 DEVELOPMENT TRAJECTORY
§12 CONNECTION TO FEELING SYSTEM
§13 FRAMEWORK INTEGRATION
§14 HONEST ASSESSMENT
§15 OPEN QUESTIONS
§16 CROSS-REFERENCES
```

**Recommended restructure dưới reframe**:
```
§0  VỊ TRÍ TRONG FRAMEWORK (update cross-references)
§1  ĐỊNH NGHĨA BODY-BASE (add substrate framing)
§2  3 BODY SIGNALS (reference Body-Dissonance.md unchanged)
§3  4 LAYERS OF CALIBRATION (reference Why-Body-Knows.md)
§4  BODY-INPUT SUBSTRATE (REWRITTEN)
    §4.1 Exteroception (vision/audition/olfaction/gustation/tactile)
    §4.2 Proprioception (proprio/vestibular/kinesthetic)
    §4.3 Interoception (thermo/nociception/respiratory/cardiovascular/
                        visceral/metabolic/hormonal/sleep/self-signal)
    §4.4 L0 vs L1 threshold/gradient distinction
    §4.5 Channel shorthand mapping (reference existing vocabulary)
§5  BASELINE ADAPTATION MECHANISM (REWRITTEN)
    §5.1 Evolved vs individual baseline
    §5.2 Novelty operator + delta rule
    §5.3 Asymmetric decay
    §5.4 Supernormal stimulus exploitation
§6  PFC DRIVES AS L1 OPERATORS (REWRITTEN from "higher-order channels")
    §6.1 Novelty drive
    §6.2 Status drive (as PFC proxy, không channel)
    §6.3 Protect drive (with Empathy-Mirror integration)
§7  DISSONANCE SUBSTRATE (REWRITTEN from silent deficiency)
    §7.1 Body-input dissonance vs schema dissonance split
    §7.2 Self-signal interoception as prerequisite
    §7.3 Silent deficiency explained via §4.9 erosion
§8  MULTI-INPUT COMPOUND INTERACTIONS (reference §13 Example findings)
§9  INDIVIDUAL VARIATION AT SUBSTRATE LEVEL (reference §13.3 Example)
§10 CULTURAL AMPLIFICATION (reference §13.4 Example)
§11 DEVELOPMENT TRAJECTORY (baseline calibration during critical periods)
§12 CONNECTION TO FEELING SYSTEM (reference Feeling/ folder)
§13 SUSTAINABLE COMPOUND SIGNATURE (reference §13.9 Example 10 features)
§14 HONEST ASSESSMENT (gaps, limitations, research needs)
§15 OPEN QUESTIONS
§16 CROSS-REFERENCES
```

#### §10.5.2 Content source mapping

Phase C content sources:
- **§4 Body-input substrate**: reframe §2-§4 condensed (this file's
  substrate enumeration → Body-Base.md architecturally central section)
- **§5 Baseline mechanism**: reframe §5 (this file's theoretical core)
- **§6 Drives**: reframe §6 (this file's drive operators)
- **§7 Dissonance substrate**: reframe §7.1 split + §4.9 mechanism
- **§8-§10**: absorb from Body-Base-Example.md §13-§14 findings
- **§11 Development**: new section integrating critical periods research
- **§13 Sustainable compound**: §13.9 Example signature directly
- **§14 Honest assessment**: reframe §11 this file + gap acknowledgments

#### §10.5.3 Content preserved từ Body-Base.md outline

**Keep unchanged**:
- §0 entry point, framework position
- §1 definition (with substrate framing added)
- §2 3 signals (reference Body-Dissonance.md)
- §3 4-tier calibration (reference Why-Body-Knows.md)

**Restructured (same content, reframed substrate)**:
- §4 channels → body-inputs
- §5 signal timeline → baseline adaptation
- §6 silent deficiency → via §4.9 mechanism
- §7 pattern fire storage decay → absorbed into §5 baseline asymmetric
  decay

**Absorbed từ Phase B Example findings**:
- §13.3 individual variation → §9 substrate level
- §13.4 cultural amplification → §10 cultural
- §13.5 channel coupling → §8 multi-input interactions
- §13.7 threshold/gradient → §4.4 L0/L1 distinction
- §13.9 sustainable compound → §13 prescriptive core
- §14 all refinements → integrated throughout

#### §10.5.4 Preservation policy

**Existing framework files preserved as-is**:
- Why-Body-Knows.md — unchanged
- Body-Dissonance.md — unchanged
- Empathy-Mirror.md — unchanged
- Body-Base-Example.md — unchanged, referenced as evidence chapters
- Body-Base-Deep-Cases.md — unchanged, referenced as deep evidence
- Feeling/ folder — unchanged, referenced as observation interface
- Body-Personal-Optimization.md — unchanged (channel language preserved
  per §8.4 policy)
- Body-Parenting-Optimization.md — unchanged

**Only Body-Base.md Phase C content fill** uses reframe architecture.
Backward compatibility maintained.

#### §10.5.5 Estimated Body-Base.md length under reframe

Reframe Body-Base.md estimate: **~3500-4500 lines** — similar to original
estimate before Body-Input-Enumeration.md test. Reframe doesn't bloat
Body-Base.md vì:
- §4 substrate can summarize, reference this file cho details
- §5-§7 mechanism can summarize, reference this file
- §8-§14 application sections remain similar length
- This file (Body-Input-Enumeration.md ~8,700 lines) serves as **deep
  evidence + theoretical foundation** referenced by Body-Base.md, không
  replaced by it

Two files together: Body-Base.md = foundation accessible to framework
users, Body-Input-Enumeration.md = deep theoretical test + evidence
chapter. Complementary role.

#### §10.5.6 Implementation approach

**Phase C recommendation**:
1. Read this entire Body-Input-Enumeration.md file để internalize reframe
2. Rewrite Body-Base.md §4 as body-input substrate (moderate depth,
   reference this file cho full)
3. Rewrite §5-§7 as mechanism sections (condensed)
4. Rewrite §8-§13 absorbing Example + Deep-Cases findings
5. Update §14 với honest assessment + gap acknowledgment
6. Delete Calibration-Inputs-Analysis.md (content absorbed)
7. Update memory files + plan.md reflecting Phase C completion

Phase C token budget estimate unchanged từ plan.md (~60-100K tokens),
with reframe providing clearer organizational structure than pre-test
approach.

---

## §11 — HONEST ASSESSMENT

### §11.1 What reframe explains better

10 specific improvements over mô hình cũ:

#### §11.1.1 Channel enumeration fuzziness — SOLVED

Mô hình cũ struggled với "how many channels?" debate (Body-Base.md §4
~19 channels, §14.1 Example proposed 7+ additions, Feeling-Sources.md
different granularity). Reframe dissolves question: channels are
aggregates với arbitrary cluster boundaries, no principled count.
Cluster at granularity appropriate to purpose (coarse cho communication,
fine cho research).

#### §11.1.2 Status/fame/wealth as PFC proxies — EXPLICIT

§14.6 Example identified tension ("PFC proxies không direct receiver")
but couldn't resolve architecturally. Mô hình cũ listed these at §4.3
higher-order channels despite recognition gap. Reframe: Status drive
as L3 operator proxying L1 access, explicit mechanism. B2 billionaire /
B36 fame / B38 power cases validated empty-status phenomenon.

#### §11.1.3 Individual calibration variation AT SUBSTRATE LEVEL

§13.3 Example finding "channel existence universal, individual
calibration variable" — framework tension between "universal" claim
và "variable" observation. Reframe: variation at substrate baseline
level. Species-universal architecture, individual-specific calibration.
B20 asexuality + B46 Proenneke + B50 solitary all explained same way.

#### §11.1.4 Supernormal stimulus as GENERAL mechanism

Mô hình cũ mentioned supernormal stimulus trong specific contexts (food
§4.1.3 refinement, §14.6 candidate). Reframe: Tinbergen principle
applies universally across body-input categories. One mechanism explains
food (Hall 2019), sex (B13/B16), visual (B35 screen), auditory (engineered
music), social validation (likes), gambling (B33). Not ad-hoc, not
food-specific.

#### §11.1.5 Baseline adaptation as CORE mechanism với empirical evidence

Mô hình cũ described "slow-decay channels" phenomenologically. Reframe:
**baseline adaptation via delta rule** = core mechanism. **Hall 2019
NIH clinical trial** directly measures mechanism (+500 kcal/day on
ultra-processed diet). Research foundation extensive: Helson 1964
adaptation-level, Brickman 1971 hedonic treadmill, Frederick 1999,
Tinbergen 1951, Zajonc 1968, Schultz dopamine PE. Reframe synthesizes
established research into coherent framework mechanism.

#### §11.1.6 Empathy precedent extended consistently

Empathy-Mirror.md đã treat empathy as mechanism, không channel. Mô hình
cũ inconsistent — empathy as mechanism OK, other phenomena still as
channels. Reframe: consistent reductive logic — all "channels" emerge
từ lower-level substrate. Completes reductive pattern Empathy-Mirror
started. Architectural consistency gained.

#### §11.1.7 §14.1 self-signal becomes ARCHITECTURAL KEYSTONE

Mô hình cũ listed "self-signal" trong §14.1 candidate additions,
peripheral architectural position. Reframe: **§4.9 self-signal
interoception as META input**, prerequisite cho body-base health.
Explains channel-lexithymia barrier from Deep-Cases methodology. B11/
B12/B15 cases validate central role. Bird & Cook 2013 alexithymia
research anchors. Elevation từ peripheral candidate to architectural
keystone.

#### §11.1.8 Slow-decay phenomenon MECHANIZED

Body-Base.md §7 outline had "pattern fire + storage + decay" concept —
descriptive but mechanism vague. Reframe §5.4: **asymmetric baseline
adaptation** (UP fast, DOWN slow). Storage = elevated baseline. Decay =
slow re-baselining. 3 concepts reduce to 1 mechanism. Parsimony gain
at mechanism level. Evolutionary logic provided (§5.6).

#### §11.1.9 15/15 case coverage với empirical diversity

§9 test spanning:
- Pathological patterns (B1/B5/B11/B13/B31/B35/B50)
- Sustainable patterns (B27/B30/B46, DC1 Leonardo side)
- Cultural variation (B5 Japanese, B14 Vietnamese implicit, B27 village)
- Collective scales (B27/B40 references)
- Multi-angle Deep-Cases (DC1 Tesla + Leonardo, DC3 nomad differential)
All 15 PASS. No case where reframe was worse. 60% STRONG PASS distribution.

#### §11.1.10 Two PARSIMONY GAINS eliminating candidate primitives

B18 pain-ritual channel (§14.1 candidate) eliminated via existing §4.2
nociception + schema context-dependent interpretation. B35 attention
meta-channel (§14.1 candidate) eliminated via §4.9 self-signal +
Novelty drive hijacking + L1 displacement. **Framework complexity
reduced while explanatory power maintained**. Rare combination.

**Pattern across 10 improvements**: reframe consistently **adds precision
via specified mechanism while reducing framework primitives**. Not
marginal improvement — substantial architectural gain.

### §11.2 What reframe still doesn't explain

Honest acknowledgment: 5 areas where reframe is incomplete or requires
additional work. Not invalidations, but scope limits + future work needs.

#### §11.2.1 Meaning cases not directly tested

**Status**: §9 selected 15 cases không include B21-B23 religious fanatic
/ cult / young zealot / B24 terminal illness meaning reorientation.
Meaning-dominant cases identified trong §9.1 as challenge candidates
but skipped in actual testing.

**What reframe says**: meaning = primarily schema layer, không body-input
cluster (§8.2.3). Schema instability propagates đến body-input baselines
via PFC mediation.

**Gap**: claim not directly tested. Meaning-dominant cases might reveal
reframe can't handle them without patches. Or might validate scope
limitation (meaning cases need schema-layer framework, not body-input
framework).

**Mitigation**: Phase C Body-Base.md should include meaning-case
section explicitly. Either tests reframe on meaning cases (1 round of
§9 extension) or explicitly scopes meaning to schema-layer treatment.

#### §11.2.2 Mastery compound under-specified

**Status**: §8.2.3 mapped mastery = Novelty drive + self-signal + Status +
variable L1 + schema chunks. Multiple elements compound.

**Gap**: Reframe doesn't clearly resolve whether mastery is "compound
of existing elements" (parsimonious reframe claim) vs "emergent property
requiring dedicated theory" (potentially separate phenomenon). B30
Jiro PASS test shows reframe can describe mastery, nhưng mastery
pursuit-patterns (arc trajectory, transmission dynamics, community
embedding) deserve more theoretical work.

**Mitigation**: future framework work could develop mastery-specific
theory layered on top của reframe substrate, không contradicting it.
Similar đến how emotions have constructed-emotion theory layered on
interoception substrate.

#### §11.2.3 Collective architectures scope limit

**Status**: §0.2 explicitly bypassed collective architectures as
orthogonal to substrate reframe. B14/B27/B40/B9 represent multi-scale
phenomena.

**Gap**: reframe doesn't specify whether collective-level structure
reduces to individual-level substrate (eliminative reduction) hoặc
emerges as irreducible higher-level phenomenon. §13.6 Example finding
documents multi-scale existence without resolving reduction question.

**Mitigation**: individual-level substrate analysis valid regardless
của reduction question. Framework can describe both levels without
committing đến metaphysical reduction claim. Body-Base.md Phase C can
have separate "multi-scale architectures" section.

#### §11.2.4 Schema-body coupling mechanism — predictive processing needed

**Status**: Reframe split L1 vs schema dissonance cleanly (§7.1). Both
feed PFC observation differently. Coupling between layers acknowledged
but mechanism under-specified.

**Gap**: How exactly does schema dissonance (information mismatch,
threat prediction, melody learning) couple to body-input dissonance?
Predictive processing framework (Seth, Barrett, Clark active inference)
provides formal answer: body signals = priors for PFC, PFC predictions
shape body responses, bidirectional tight coupling. **Not fully integrated
into reframe**.

**Mitigation**: future framework work should integrate predictive
processing more thoroughly. §4.9 self-signal interoception section
references Seth/Barrett but doesn't elaborate active inference fully.
Body-Base.md Phase C should integrate.

#### §11.2.5 Cultural specificity beyond amplification

**Status**: §13.4 Example adopted — "culture shapes expression không
architecture." §5.2 notes cultural calibration, §6.2 notes cultural
Status reinforcement.

**Gap**: mechanism của cultural SHAPING of body-input baselines
under-specified. Languages shape perception (linguistic relativity),
vocabularies shape emotional perception (Barrett constructed emotion),
narratives shape meaning interpretation (Vygotsky), rituals shape body
practices. These operate at schema layer affecting body-input engagement,
but reframe doesn't detail mechanism comprehensively.

**Mitigation**: cultural specificity is extensive research domain its
own. Framework can acknowledge cultural layer operates via schema
mediation without fully specifying mechanism. Cross-reference other
research traditions instead of duplicating.

#### §11.2.6 Summary

**5 gaps, all legitimate limitations**:
1. Meaning cases not directly tested (can be addressed via extended
   §9 testing trong Phase C)
2. Mastery compound needs more work (future theoretical layer)
3. Collective architectures scope limit (acknowledge, không reduce)
4. Schema-body coupling mechanism (integrate predictive processing)
5. Cultural specificity beyond amplification (reference external research)

**None are FAIL-level**. All are scope limits or work-to-do items.
Reframe passes 7/7 test criteria từ §1.4.1 với honest gap acknowledgment.

### §11.3 Open questions

6 open questions raised by reframe, flagged cho future work:

#### §11.3.1 How much of L3 reduces to L1 operators?

Reframe positions L3 as operators acting on L1. But operators still
have their own mechanisms (Novelty dopamine PE, Status social cognition,
Protect threat response). Are those mechanisms reducible further to
L1, hoặc genuinely autonomous PFC-level processes?

Two possible framings:
- **Strong reduction**: L3 operators = complex patterns in L1 processing,
  no additional substrate needed
- **Weak reduction**: L3 operators have own mechanisms (PFC executive
  functions) that act on L1 substrate, both layers real

Current reframe adopts weak reduction pragmatically. Strong reduction
would require further theoretical work. Not resolved.

#### §11.3.2 Schema vs body-input dissonance — truly separate or interwoven?

Reframe split cleanly at §7.1. But predictive processing (Seth, Barrett,
Clark) suggests body signals and schema predictions are tightly interwoven
via active inference — not clearly separable.

Are these:
- **Separable layers** (reframe's current framing — clean 3+3 split)
- **Interwoven levels** (predictive processing framing — continuous
  bidirectional coupling)
- **Both valid at different analytical resolutions**?

Honest position: reframe's split is useful simplification, predictive
processing provides more complete model. Phase C should integrate both.

#### §11.3.3 How does reframe handle development trajectory?

Children calibrate body-input baselines during development (§5.2
mentioned critical periods). Reframe doesn't fully describe arc:
- How are baselines established initially?
- When do critical periods close?
- What interventions work cho adult baseline adjustment?
- How does child's §4.9 self-signal develop?

Existing Body-Base.md §11 outline has "Development Trajectory" section
cho fill. Future framework work should integrate developmental
psychology research (attachment theory, infant research, sensitive
periods).

#### §11.3.4 Does reframe have different intervention implications?

Mô hình cũ led to channel-level interventions ("get more nature", "more
exercise", "more social"). Does reframe lead to different recommendations?

Likely partial differences:
- **§4.9 self-signal training** (mindfulness, Gendlin focusing, somatic
  therapy) gets elevated importance
- **Environmental design > willpower** (§14.6 echo) reinforced
- **Compound interventions** > single-channel interventions
- **Baseline preservation** > "recovery" (prevention priority)

Framework-level intervention recommendations should be updated. Body-
Personal-Optimization.md + Body-Parenting-Optimization.md may need
reference updates, though channel-language shorthand remains valid.

#### §11.3.5 AI monitoring implications?

Reframe specifies measurement targets: body-input baselines, current
states, adaptation dynamics. AI-enabled continuous monitoring (wearables,
HRV tracking, sleep monitoring, activity tracking, etc.) could enable
real-time body-input awareness never previously possible.

Future framework development: AI-augmented body-base optimization could
use reframe architecture as foundation cho personalized interventions.
Framework has implications beyond current human capacity.

#### §11.3.6 Framework aesthetic — commit reframe vs preserve channel familiarity?

Meta-question: reframe is theoretically cleaner, but channel language
is familiar and accessible. Framework design must balance:
- Theoretical rigor (reframe wins)
- Accessibility (channel language wins)
- Continuity với existing files (channel language preserves)
- Integration with research (reframe integrates better)

§8.4 rule resolved này at vocabulary level: use both, matched to context.
But framework aesthetic question remains: present reframe as "deeper
layer" in foundation file (Body-Base.md), or relegate to appendix?

Recommendation: present reframe as central architecture trong Body-Base.md
§4-§7, với channel shorthand as §4.5 mapping section. Preserve accessibility
trong downstream files. Phase C implementation decision.

#### §11.3.7 Summary

6 open questions flagged cho future work. None block reframe commit.
All represent legitimate ongoing theoretical development. Framework is
iterative — reframe is current best synthesis, not final word.

### §11.4 Requires biological measurement for precision

Honest scope acknowledgment: reframe framework is **descriptive + testable
hypothesis-generating**, không quantitatively precise. Precise substrate
measurement requires biological/medical research beyond framework's scope.

#### §11.4.1 What framework provides

- **Descriptive architecture**: body-input substrate enumerated, mechanisms
  specified, drives integrated
- **Testable hypotheses**: baseline adaptation rates, individual variation
  ranges, deprivation thresholds, supernormal stimulus effects all
  operationally defined
- **Measurement targets**: framework tells researchers WHAT to measure
  (body-input baselines + adaptation dynamics + deviation signals)
- **Cross-disciplinary synthesis**: integrates adaptation psychology,
  learning theory, interoception neuroscience, predictive processing,
  behavioral economics trong one architecture
- **Framework cho intervention design**: even without quantitative
  precision, architecture guides intervention targets

#### §11.4.2 What framework doesn't provide

- **Quantitative baselines** per individual
- **Precise adaptation rates** per input category
- **Individual variation ranges** empirically measured
- **Critical period boundaries** precisely dated
- **Dose-response relationships** cho interventions
- **Biomarkers** cho body-input state real-time

These require:
- Wearable device development (HRV, sleep, activity widely available;
  interoceptive monitoring less so)
- Clinical research protocols
- Longitudinal studies
- Biological measurement advances
- AI-augmented data processing

#### §11.4.3 AI era implications

**AI + wearables** may enable body-input state monitoring unprecedented
trong history:
- Continuous HRV tracking (interoceptive cardiovascular proxy)
- Sleep architecture detection
- Activity pattern tracking
- Light exposure monitoring
- Social interaction detection (smartphone data)
- Future: potentially direct interoception biomarkers

**Framework role**: provides architectural map cho what these measurements
MEAN. Raw data without theoretical framework = noise. Reframe architecture
= interpretation framework cho future quantitative data.

Reframe positions body-base framework cho AI-era development of
body-input tracking và personalized intervention. Even without current
quantitative precision, framework provides foundation future research
can build on.

#### §11.4.4 Honest positioning

Reframe is **theoretical synthesis grounded trong existing research**,
không "finished" quantitative framework. Next-stage work needs:
- Biological measurement integration
- Clinical trial validation
- AI monitoring tool development
- Intervention effectiveness studies

Framework provides testable scaffolding cho this work. Not a medical
protocol, không a clinical treatment, không a scientific proof.
**Descriptive architectural framework + hypothesis generator** là
appropriate characterization.

**This scope limitation is feature, không bug**. Framework avoids
overreach claims. Clear về what it provides và what it doesn't.

---

## §12 — VERDICT

### §12.1 Reframe disposition

Based on §9 case coverage results + §11 honest assessment, verdict
integrates multiple criteria.

#### §12.1.1 Test criteria results summary

From §1.4.1 PASS conditions:

1. **Enumeration completeness** (§2-§4): ✅ PASS — 17 body-input
   sub-sections với full schema (baseline, deviations, adaptation,
   research, cases, variation)
2. **Mechanism coherence** (§5): ✅ PASS — delta rule + Novelty operator
   + asymmetric decay + evolutionary explanation với extensive research
   support
3. **Drive operation coherent** (§6): ✅ PASS — Novelty/Status/Protect
   operators cleanly explained, Empathy-Mirror integration, user's
   "giúp bộ đội" question resolved
4. **Dissonance mapping clean** (§7): ✅ PASS — 6 sources map to
   body-input layer (3) vs schema layer (3) cleanly
5. **Case coverage** (§9): ✅ PASS — 15/15 cases (60% STRONG PASS,
   13% parsimony gain, 27% PASS)
6. **Theory integration intact** (§10): ✅ PASS — Why-Body-Knows +
   Body-Dissonance + Empathy-Mirror + Feeling folder all compatible,
   enhanced
7. **No regression** (§11.1): ✅ PASS — 10 improvements documented,
   zero regressions identified

**All 7 test criteria PASS**.

#### §12.1.2 Four verdict options analysis

**Option A — COMMIT**: reframe is parsimonious, compatible với existing
findings, improves explanatory structure, eliminates 2 candidate
primitives, passes all test criteria. Phase C Body-Base.md rewrite
using substrate model. Existing Phase B/DC work preserved as evidence
chapters.

**Analysis**: strong fit based on §9 results. 15/15 PASS + 2 parsimony
gains + no case where reframe was worse than mô hình cũ. Recommendation
candidate.

**Option B — PATCH**: reframe mostly works but needs patches cho
meaning/mastery/collective/predictive processing gaps. Implement reframe
as dominant model với acknowledged patches.

**Analysis**: §11.2 identified 5 gaps, but all are "scope limits"
hoặc "future work items", không "require patches to handle cases."
No test case FAILED needing patch. Option A already accommodates future
work as Phase C content fill items. Option B doesn't add value over A.

**Option C — PARALLEL MODELS**: keep both channel model and substrate
model. Channel = practical vocabulary, substrate = theoretical foundation.
Document relationship.

**Analysis**: §8.4 already handles parallel vocabulary usage at lexical
level (channel shorthand vs body-input terminology). That's compatible
với Option A commit, không alternative to it. Option C is partially
adopted within Option A framework.

**Option D — REJECT**: if §9 tests revealed systematic failures impossible
to patch.

**Analysis**: §9 results directly contradict rejection. No systematic
failures. Option D ruled out by evidence.

#### §12.1.3 Recommendation: Option A — COMMIT

**Framework decision recommendation**: **COMMIT reframe** as Phase C
Body-Base.md architectural foundation.

**Reasoning**:
1. All 7 test criteria from §1.4.1 PASS
2. 15/15 case coverage PASS, 60% STRONG PASS distribution
3. 2 parsimony gains (pain-ritual, attention meta-channel eliminated)
4. Extensive research integration (50+ citations across independent
   traditions)
5. Empirical validation via Hall 2019 NIH direct experimental evidence
6. Compatible with all existing framework files (Why-Body-Knows, Body-
   Dissonance, Empathy-Mirror, Feeling folder) — no breaking changes
7. User's "giúp bộ đội có gạo" question answered satisfyingly
8. §8.4 rule preserves channel language cho accessibility
9. 5 gaps identified honestly, all addressable trong Phase C content
   fill, none are FAIL-level
10. Mechanism-level clarity significantly better than mô hình cũ

**Commit qualifiers**:
- Commit reframe **as theoretical foundation**, không as "final framework"
- Address 5 gaps (§11.2) trong Phase C content fill where feasible
- Acknowledge scope limits (§11.4) về quantitative precision
- Preserve existing files (Phase B/DC/theory files/Feeling/ folder)
- Update Body-Base.md Phase C using §10.5 recommended restructure
- Delete Calibration-Inputs-Analysis.md as content absorbed

**Confidence level**: HIGH. Evidence supports commit decisively. Not
perfect framework, but significantly better than mô hình cũ và
theoretically consistent.

#### §12.1.4 What commit means operationally

Commit doesn't mean:
- Framework is "done"
- No future revisions
- Reframe is metaphysically correct
- Channel language abandoned

Commit means:
- Body-Base.md Phase C content fill proceeds với reframe substrate model
- Framework architecture documented clearly
- Memory + plan.md updated reflecting Phase R completion
- Future work items flagged (§11.2 gaps, §11.3 open questions)
- Research integration continues
- Iteration expected

### §12.2 Next steps

Based on §12.1 Commit recommendation, concrete next steps for framework
development.

#### §12.2.1 Phase R (reframe test) completion

**Phase R-8b** (current phase) completes Body-Input-Enumeration.md
test file với §11-§13 fill. After R-8b:

**Phase R-9** (memory + plan update):
- Update `memory/project_calibration_inputs.md` with reframe commit
  decision + key findings
- Update `memory/project_pattern_match_insights.md` with architectural
  updates
- Update `memory/MEMORY.md` index line
- Update `Body-Base/plan.md` với Phase R completion status + Phase C
  restart plan

After R-9, Phase R complete. Test file complete và documented.

#### §12.2.2 Phase C Body-Base.md content fill (post-commit)

Following §10.5 recommended restructure, Phase C fills Body-Base.md
với reframe substrate model:

**Step 1 — Read this test file** để internalize reframe architecture

**Step 2 — Restructure §4** as body-input substrate:
- §4.1 Exteroception (condensed reference to this file §2)
- §4.2 Proprioception (condensed reference to §3)
- §4.3 Interoception (condensed reference to §4, especially §4.9
  keystone)
- §4.4 L0/L1 distinction (§5.5 summary)
- §4.5 Channel shorthand mapping (§8.2 summary)

**Step 3 — Rewrite §5-§7** mechanism sections:
- §5 Baseline adaptation mechanism (condensed reference to this file §5)
- §6 PFC drives operating on L1 (condensed reference to §6)
- §7 Dissonance substrate với L1/schema split (reference §7)

**Step 4 — Integrate §8-§14** absorbing Example + Deep-Cases findings:
- §8 Multi-input compound interactions (§13.5 Example)
- §9 Individual variation substrate level (§13.3 Example)
- §10 Cultural amplification (§13.4 Example)
- §11 Development trajectory (new, critical periods)
- §13 Sustainable compound signature (§13.9 Example 10 features)

**Step 5 — Address §11.2 gaps** trong Phase C content where feasible:
- Gap 1 (meaning cases): extend §9-equivalent với B21-B24 trong Body-
  Base.md application sections
- Gap 2 (collective): dedicated multi-scale section
- Gap 3 (status drive evolution): expand §6.2 với evolutionary psychology
- Gap 4 (schema-body coupling): integrate predictive processing (Seth,
  Barrett, Clark)
- Gap 5 (quantitative): acknowledge scope limit explicitly

**Step 6 — Delete Calibration-Inputs-Analysis.md** (content absorbed
into Body-Base.md §4 và this test file)

**Step 7 — Update cross-references** trong downstream files:
- Body-Personal-Optimization.md (likely minimal changes — channel
  language preserved per §8.4)
- Body-Parenting-Optimization.md (likely minimal changes)
- Feeling/ folder files (add reference to §4.9 keystone)

#### §12.2.3 Timeline estimate

**Phase R-9**: 1 session (~30 min memory + plan update)

**Phase C Body-Base.md fill**: 1-3 sessions estimated — foundation file
quality investment. Token budget estimated 60-100K per plan.md.

**Downstream updates**: 1 session (cross-reference sync)

**Total to complete framework work**: 3-5 additional sessions after
Phase R completion.

#### §12.2.4 Memory + plan updates needed (Phase R-9)

**`project_calibration_inputs.md`** updates:
- Mark reframe Phase R complete với Commit decision
- Document key findings (substrate reframe, §4.9 keystone, 2 parsimony
  gains, 15/15 case coverage)
- Flag Phase C as next phase

**`project_pattern_match_insights.md`** updates:
- Add body-input substrate as architectural extension to Pattern Match
  framework
- Cross-reference §4.9 self-signal interoception as biological basis
- Note reframe relationship to existing architecture

**`MEMORY.md` index** update:
- Line 15 update reflecting Phase R complete + reframe committed
- Status from "Phase B complete + DC-B partial" → "Phase R reframe test
  complete, commit, Phase C pending"

**`Body-Base/plan.md`** updates:
- Phase R completion documented
- Phase C restart plan using reframe substrate model
- Timeline update
- Gap acknowledgment list

#### §12.2.5 Success criteria for Phase R completion

Phase R is complete when:
- [x] Body-Input-Enumeration.md test file fully filled (§0-§13)
- [x] Reframe verdict reached (Commit)
- [x] 5 gaps acknowledged honestly
- [x] Next steps documented clearly
- [ ] Memory files updated (R-9 pending)
- [ ] plan.md updated (R-9 pending)
- [ ] Phase C restart clearly defined

Ready to proceed với Phase R-9 after §13 sources section complete.

---

## §13 — SOURCES

Comprehensive research citations organized by topic. All references
cited trong body của this test file. Framework synthesizes established
research across many independent traditions.

#### §13.1 Interoception research (architectural foundation)

- 🟢 **Craig, A.D.** (2002). "How do you feel? Interoception: the sense
  of the physiological condition of the body." Nat Rev Neurosci 3:655-666
- 🟢 **Craig, A.D.** (2009). "How do you feel — now? The anterior insula
  and human awareness." Nat Rev Neurosci 10:59-70
- 🟢 **Seth, A.K.** (2013). "Interoceptive inference, emotion, and the
  embodied self." Trends Cogn Sci 17:565-573
- 🟢 **Barrett, L.F.** (2017). "How Emotions Are Made: The Secret Life
  of the Brain"
- 🟢 **Bird, G. & Cook, R.** (2013). "Mixed emotions: the contribution
  of alexithymia to the emotional symptoms of autism." Translational
  Psychiatry 3:e285
- 🟢 **Garfinkel, S. et al.** (2015). "Knowing your own heart:
  distinguishing interoceptive accuracy from interoceptive awareness."
  Biological Psychology 104:65-74
- 🟢 **Damasio, A.** "Descartes' Error" + somatic marker hypothesis
- 🟢 **Hölzel, B. et al.** (2011). MBSR insula changes fMRI study
- 🟢 **Farb, N. et al.** Mindfulness + interoception research
- 🟢 **van der Kolk, B.** (2014). "The Body Keeps the Score"
- 🟢 **Gendlin, E.** (1978). "Focusing" — felt sense accessing
- 🟢 **Fonagy, P.** Mentalizing theory
- 🟢 **Herbert, B.M. et al.** Interoceptive sensitivity research

#### §13.2 Baseline adaptation + hedonic treadmill

- 🟢 **Helson, H.** (1964). "Adaptation-Level Theory: An Experimental
  and Systematic Approach to Behavior" — direct theoretical foundation
- 🟢 **Rescorla, R. & Wagner, A.** (1972). Classical conditioning
  learning rule — delta rule basis
- 🟢 **Brickman, P. & Campbell, D.T.** (1971). "Hedonic relativism and
  planning the good society"
- 🟢 **Frederick, S. & Loewenstein, G.** (1999). "Hedonic adaptation"
  review
- 🟢 **Lykken, D. & Tellegen, A.** (1996). "Happiness is a stochastic
  phenomenon"
- 🟢 **Diener, E. et al.** Wellbeing set point research

#### §13.3 Supernormal stimulus + Novelty

- 🟢 **Tinbergen, N.** (1951). "The Study of Instinct" — supernormal
  stimulus foundational
- 🟢 **Barrett, D.** (2010). "Supernormal Stimuli"
- 🟢 **Berlyne, D.E.** (1960). "Conflict, Arousal, and Curiosity"
- 🟢 **Zajonc, R.B.** (1968). Mere exposure effect
- 🟢 **Schultz, W.** Dopamine prediction error research
- 🟢 **Berridge, K.** Wanting vs liking distinction
- 🟢 **Kahneman, D. et al.** Wealth-happiness plateau
- 🟢 **Wilson, T. & Gilbert, D.** Affective forecasting / impact bias
- 🟢 **Thaler, R.** Endowment effect + reference point economics

#### §13.4 Vision (§2.1)

- 🟢 **Taylor, R.** (2006). Fractal preferences D≈1.3-1.5
- 🟢 **Hagerhall, C. et al.** (2004, 2008). Fractal EEG response
- 🟢 **Kaplan, R. & Kaplan, S.** (1989). "The Experience of Nature" —
  Attention Restoration Theory
- 🟢 **Ulrich, R.** (1991). Stress Reduction Theory — hospital window
  study
- 🟢 **Orians, G.** (1992). Savanna hypothesis
- 🟢 **Langlois, J. et al.** (1990). Average face attractiveness
- 🟢 **Masuda, T. & Nisbett, R.** (2001). Cultural attention patterns
- 🟢 **Berson, D.M. et al.** (2002). Melanopsin retinal ganglion cells
- 🟡 **Kellert, S.** Biophilic design theory

#### §13.5 Audition (§2.2)

- 🟢 **WHO** (2011). "Burden of disease from environmental noise"
- 🟢 **Kryter, K.** (1994). "Handbook of Hearing and the Effects of Noise"
- 🟢 **Goines, L. & Hagler, L.** (2007). Noise pollution health review
- 🟢 **Voss, R. & Clarke, J.** (1975). "1/f noise in music and speech"
- 🟢 **North, A. & Hargreaves, D.** (1995). Music preference × familiarity
  inverted-U
- 🟢 **Kuhl, P.** (1992). Native language magnet effect
- 🟢 **Zentner, M.** (2008). Music preference development
- 🟢 **Provine, R.** (2000). "Laughter: A Scientific Investigation"
- 🟡 **Baguley, D. et al.** (2013). Tinnitus review

#### §13.6 Olfaction (§2.3)

- 🟢 **Buck, L. & Axel, R.** (1991). Olfactory receptor gene family —
  Nobel 2004
- 🟢 **Li, Q.** (2010). Shinrin-Yoku phytoncides immune effects
- 🟢 **Herz, R.** (2004). Proust effect — odor-memory connection
- 🟢 **Rozin, P.** Disgust research — olfactory component
- 🟢 **Wilson, D.A. & Stevenson, R.** (2006). "Learning to Smell"
- 🟡 **Wedekind, C. et al.** (1995). MHC mate preference via smell

#### §13.7 Gustation (§2.4)

- 🟢 **Hall, K. et al.** (2019). "Ultra-processed diets cause excess
  calorie intake and weight gain" — Cell Metabolism — **direct
  experimental validation of baseline shifting mechanism**
- 🟢 **Running, C. et al.** (2015). Fat as 6th taste
- 🟢 **Eaton, S.B. & Konner, M.** (1985). "Paleolithic nutrition" — NEJM
- 🟢 **Rozin, P.** Food psychology, neophobia research
- 🟢 **Kim, U.K. et al.** (2003). PTC/TAS2R38 bitter receptor genetics
- 🟡 **Wrangham, R.** (2009). "Catching Fire" cooking hypothesis

#### §13.8 Tactile + affective touch (§2.5)

- 🟢 **Field, T.** (2010). Touch research foundational
- 🟢 **Löken, L. et al.** (2009). C-tactile afferents pleasant touch —
  Nature Neuroscience
- 🟢 **McGlone, F. et al.** (2014). "Discriminative and affective touch"
  — Neuron review
- 🟢 **Harlow, H.** (1958). "The nature of love" — monkey surrogate
  mother
- 🟢 **Zeanah, C. & Nelson, C.** Bucharest Early Intervention Project —
  Romanian orphanages
- 🟢 **Morrison, I. et al.** C-tactile social touch research
- 🟢 **Hertenstein, M. et al.** (2009). Touch communicates distinct
  emotions
- 🟢 **Olausson, H. et al.** (2002). CT-fiber loss patient research
- 🟢 **Carter, C.S.** Oxytocin-bonding research
- 🟡 **Montagu, A.** (1971). "Touching: The Human Significance of the
  Skin"

#### §13.9 Proprioception + vestibular + kinesthetic (§3)

- 🟢 **Sherrington, C.** (1906). "The Integrative Action of the Nervous
  System" — proprioception foundational
- 🟢 **Proske, U. & Gandevia, S.** (2012). "The proprioceptive senses"
  — Physiological Reviews
- 🟢 **Tuthill, J. & Azim, E.** (2018). Proprioception review — Current
  Biology
- 🟢 **Fitzpatrick, R. & Day, B.** Vestibular research
- 🟢 **Brandt, T. & Dieterich, M.** Vestibular cortex research
- 🟢 **Angelaki, D. & Cullen, K.** (2008). Vestibular system neuroscience
- 🟢 **Guedry, F.** Motion sickness research
- 🟢 **Reason, J.** (1978). Sensory conflict theory of motion sickness
- 🟢 **Ratey, J.** (2008). "Spark" — BDNF + mood + cognition
- 🟢 **Blumenthal, J.** Exercise as antidepressant clinical trials
- 🟢 **Dishman, R.** Exercise neuroscience
- 🟢 **Pontzer, H.** Hunter-gatherer energy expenditure research
- 🟢 **Fuss, J. et al.** (2015). Runner's high endocannabinoid update

#### §13.10 Thermoreception + metabolic + visceral (§4.1, §4.5, §4.6)

- 🟢 **Satinoff, E.** Thermoregulation research
- 🟢 **Morrison, S.F.** Central thermoregulation neuroscience
- 🟢 **van Marken Lichtenbelt, W.** Brown adipose tissue cold exposure
- 🟢 **Kox, M. et al.** (2014). Wim Hof method autonomic control
- 🟢 **Ludwig, D.** Carbohydrate-insulin model of obesity
- 🟢 **Cummings, D.** Ghrelin research foundational
- 🟢 **Friedman, J. & Halaas, J.** (1998). Leptin discovery
- 🟢 **Dallman, M.** "Feast or famine" research
- 🟢 **Mattson, M.** Intermittent fasting research
- 🟢 **Mayer, E.** (2016). "The Mind-Gut Connection"
- 🟢 **Cryan, J. & Dinan, T.** Gut-brain axis research
- 🟢 **Gershon, M.** (1998). "The Second Brain" — foundational
- 🟢 **Sonnenburg, J. & E.** "The Good Gut" — microbiome research
- 🟢 **David, L. et al.** (2014). Rapid diet-microbiome response
- 🟢 **Yano, J. et al.** (2015). Gut microbiome + serotonin synthesis
- 🟢 **Foster, J. & McVey Neufeld, K.A.** (2013). Gut-brain axis
  depression + anxiety

#### §13.11 Nociception + pain (§4.2)

- 🟢 **Melzack, R. & Wall, P.** (1965). Gate control theory — Science
- 🟢 **Wall, P.** (2000). "Pain: The Science of Suffering"
- 🟢 **Melzack, R.** (1999). Neuromatrix theory
- 🟢 **Woolf, C.** Central sensitization research
- 🟢 **Cox, J.J. et al.** (2006). SCN9A CIPA genetic research
- 🟢 **Bingel, U. et al.** Placebo/nocebo neuroscience
- 🟢 **Zeidan, F.** Meditation + pain fMRI research
- 🟢 **Basbaum, A. et al.** (2009). Cellular mechanisms of pain review

#### §13.12 Respiratory (§4.3)

- 🟢 **Porges, S.** (2011). "The Polyvagal Theory"
- 🟢 **Feldman, J. & Del Negro, C.** Respiratory neuroscience
- 🟢 **Brown, R. & Gerbarg, P.** Breath therapy clinical research
- 🟢 **Nestor, J.** (2020). "Breath: The New Science of a Lost Art"
- 🟢 **Lehrer, P. & Gevirtz, R.** HRV biofeedback via breath
- 🟢 **Zaccaro, A. et al.** (2018). Breath-control review

#### §13.13 Cardiovascular (§4.4)

- 🟢 **Thayer, J. & Lane, R.** HRV + emotional regulation
- 🟢 **Schandry, R.** (1981). Heartbeat perception task
- 🟢 **Appelhans, B. & Luecken, L.** HRV emotional regulation meta-analysis
- 🟢 **Thayer, J. et al.** HRV + health outcomes meta-analyses
- 🟡 **McCraty, R.** HeartMath research

#### §13.14 Hormonal + sleep (§4.7, §4.8)

- 🟢 **Sapolsky, R.** "Why Zebras Don't Get Ulcers" + stress research
- 🟢 **Insel, T.** Social bonding neurobiology
- 🟢 **Nesse, R.** "Good Reasons for Bad Feelings" — evolutionary
  psychiatry
- 🟢 **Young, L.** Prairie vole bonding oxytocin research
- 🟢 **Walker, M.** (2017). "Why We Sleep"
- 🟢 **Foster, R. & Kreitzman, L.** "Rhythms of Life"
- 🟢 **Czeisler, C.** Circadian research
- 🟢 **Siegel, J.** Sleep neuroscience
- 🟢 **Stickgold, R.** Memory consolidation sleep research
- 🟢 **Ekirch, R.** (2005). "At Day's Close" — biphasic sleep
- 🟢 **IARC** (2007). Shift work carcinogenicity classification

#### §13.15 Predictive processing framework

- 🟢 **Seth, A.K.** (2013, 2014). Predictive interoception
- 🟢 **Clark, A.** (2013). "Whatever next? Predictive brains"
- 🟢 **Barrett, L.F.** (2017). Constructed emotion theory

#### §13.16 Status + evolutionary psychology

- 🟢 **Sapolsky, R.** Baboon dominance hierarchies research
- 🟢 **Marmot, M.** Whitehall studies — status + health
- 🟢 **Boehm, C.** Hierarchy + egalitarianism research
- 🟢 **Sapolsky, R.** "Behave" — integrated review
- 🟢 **Eisenberger, N.** (2003). Social pain = physical pain pathway

#### §13.17 Existing framework files referenced

- **Why-Body-Knows.md** — META layer, calibration theory
- **Body-Dissonance.md** — signal layer, 6 sources + 14-level spectrum
- **Body-Base-Example.md** — 50 cases + §12-§14 synthesis
- **Body-Base-Deep-Cases.md** — DC1 Tesla + Leonardo, DC3 nomad
  differential, multi-angle methodology
- **Empathy-Mirror.md** — mechanism precedent
- **Calibration-Inputs-Analysis.md** — draft (absorbed, scheduled cho
  deletion)
- **Feeling/ folder** — PFC observation interface (7 files ~6,924 lines)
- **Body-Base.md** — foundation file (Phase C pending rewrite)
- **Body-Personal-Optimization.md** — application
- **Body-Parenting-Optimization.md** — application
- **Novelty.md** — existing drive framework file
- **Drive.md** — existing drive framework file
- **Threat.md** — existing threat framework file

#### §13.18 Research citation summary

**Total citations**: ~80+ research references across 16 topic areas
spanning interoception neuroscience, adaptation psychology, learning
theory, supernormal stimulus research, sensory neuroscience (all
modalities), gut-brain axis, polyvagal theory, sleep research,
predictive processing, evolutionary psychology, behavioral economics.

**Research quality**: majority 🟢 established research, few 🟡 framework
inference or partially-replicated findings, no 🔴 hypothesis-only
claims trong core arguments.

**Framework value**: synthesizes established research across multiple
traditions into unified architecture. Không inventing mechanisms —
integrating + applying existing research to body-base framework context.

---

## §T — OUTLINE COMPLETION STATUS

**Phase R-1** (Foundation read): ✅ COMPLETE 2026-04-14
**Phase R-2** (Evidence extract): ✅ COMPLETE 2026-04-14
**Phase R-3** (Outline file): ✅ COMPLETE 2026-04-14
**Phase R-4a** (Fill §0 methodology + §1 reframe): ✅ COMPLETE 2026-04-14
**Phase R-4b** (Fill §2 exteroception — 5 inputs): ✅ COMPLETE 2026-04-14
**Phase R-5a** (Fill §3 proprioception — 3 sub-sections): ✅ COMPLETE 2026-04-14
**Phase R-5b** (Fill §4.1-§4.5 interoception batch 1): ✅ COMPLETE 2026-04-14
**Phase R-5c** (Fill §4.6-§4.9 interoception batch 2 + keystone): ✅ COMPLETE 2026-04-14
**Phase R-6a** (Fill §5 baseline adaptation mechanism): ✅ COMPLETE 2026-04-14
**Phase R-6b** (Fill §6 drives + §7 dissonance remap): ✅ COMPLETE 2026-04-14
**Phase R-7a** (Fill §8 channel shorthand mapping): ✅ COMPLETE 2026-04-14
**Phase R-7b** (Fill §9.1 + §9.2 first 7 cases): ✅ COMPLETE 2026-04-14
**Phase R-7c** (Fill §9.2 last 8 cases): ✅ COMPLETE 2026-04-14
**Phase R-7d** (Fill §9.3 coverage + §9.4 gaps + §9.5 verdict): ✅ COMPLETE 2026-04-14
**Phase R-8a** (Fill §10 integration với existing framework): ✅ COMPLETE 2026-04-14
**Phase R-8b** (Fill §11 assessment + §12 verdict + §13 sources): ✅ COMPLETE 2026-04-14
**Phase R-9** (Memory + plan.md update): ⏳ PENDING

**Final verdict** (§12.1): **COMMIT reframe** — all 7 test criteria
PASS, 15/15 case coverage, 2 parsimony gains, 5 gaps acknowledged
honestly, research foundation extensive. Phase C Body-Base.md rewrite
recommended using reframe substrate model.

**Actual file length**: ~10,000+ lines (significantly exceeds original
2000-3000 estimate — reflects depth + quality investment across
substrate enumeration, mechanism theory, case testing, and integration
analysis).

**Gap acknowledgments** (§11.2):
1. Meaning cases not directly tested (MEDIUM)
2. Mastery compound needs more work (MEDIUM)
3. Collective architectures scope limit (MEDIUM)
4. Schema-body coupling mechanism (MEDIUM — predictive processing
   integration)
5. Cultural specificity beyond amplification (LOW-MEDIUM)

**2 parsimony gains**:
- B18 pain-ritual channel primitive eliminated
- B35 attention meta-channel primitive eliminated

**Research foundation**: ~80+ citations across 16 topic areas spanning
interoception neuroscience, adaptation psychology, sensory systems,
gut-brain axis, predictive processing, evolutionary psychology.

---

**END OF BODY-INPUT-ENUMERATION.MD TEST FILE**

**Phase R (reframe test) essentially complete**. Phase R-9 (memory +
plan update) is administrative closing step. Then Phase C Body-Base.md
content fill can proceed using committed reframe substrate model.

**Test file serves dual purpose**:
1. **Immediate**: tests reframe validity (conclusive PASS)
2. **Long-term**: evidence chapter + theoretical foundation referenced
   by Body-Base.md foundation file

Body-Input-Enumeration.md = deep theoretical synthesis. Body-Base.md
Phase C = accessible foundation file referencing this. Both preserved
in framework architecture long-term.
