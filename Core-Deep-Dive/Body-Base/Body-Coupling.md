---
title: Body-Coupling — Cơ Chế Body Gắn Kết Sâu Với Entity
version: 3.0
created: 2026-04-28
updated: 2026-05-22 (v3.0 — FULL REWRITE integrating ALL Phase A+B+T+C1+C2)
previous: v2.0 → backup/Body-Coupling-v2.0-backup.md
status: MECHANISM FILE v3.0
scope: |
  CORE MECHANISM FILE: HOW body deeply couples với entity.
  Khi |❸| per-agent valence compile đủ sâu → qualitative shift:
  entity trở thành phần cấu trúc của body-base (extension, entanglement, hoặc mixed).
  v3.0 KEY CHANGES (over v2.0):
    ① 4 bond types × 1 Entity-Compiled mechanism (Bond-Architecture v2.0: parent→child, child→parent, romantic, friendship)
    ② Entity-Access gradient Mức 0-5 × coupling depth (Entity-Access v1.2)
    ③ Hardware-Subsidy per bond type (Entity-Valence-Dynamics.md v1.0 §5: MAX→MODERATE→TEMPORARY→NONE)
    ④ 3 Firing Modes × coupling (Entity-Valence-Dynamics.md v1.0 §4: Maintenance/Chunk-Miss/Context-Trigger)
    ⑤ Structural vs Current valence × coupling (Entity-Valence-Dynamics.md v1.0 §1)
    ⑥ Satiation Types × coupling channels (Entity-Valence-Dynamics.md v1.0 §6: Cyclic/Tonic/Generative)
    ⑦ PFC budget × coupling cost (PFC-Operations v1.0)
    ⑧ Compiled Quality × coupling sustainability (PFC-Operations v1.0)
    ⑨ 4-Layer Sustainability × coupling durability (Resonance-Sustainability v1.0)
    ⑩ Resonance Decline (2 Forces + 1 Fuel) × coupling (Bond-Architecture v2.0)
    ⑪ Compilation Chain × coupling formation (Resonance-Per-Entity v1.0)
    ⑫ Entity-Access-Excess Mức 5 = coupling excess territory (Entity-Access-Excess v1.0)
    ⑬ Phantom 4-factor model (Resonance-Per-Entity v1.0)
    ⑭ Anti-compiled-suppress × all bond types (Bond-Architecture v2.0)
    ⑮ By-Product-Scale × system compilation (By-Product-Scale v1.0)
    ⑯ Self-Pattern-Modeling v3.1 terminology throughout (Match→Modeling)
    ⑰ ALL dependency versions updated (~27 deps)
  v2.0 PRESERVED:
    → 2D Model (Depth × Direction) — KEPT
    → 4 coupling outcomes (Extension/Entanglement/Mixed/Neutral) — KEPT
    → 3 Phase Model + 3 Paths — KEPT
    → compile_rate insight + 8 accelerators — ENRICHED
    → Smoothing/Anti-smoothing + oscillating — KEPT
    → Parent-child trajectory — ENRICHED
    → Mixed loss complex grief — KEPT
    → "Emptiness" 7-TP model — KEPT
    → ALL research citations (~30) — 100% preserved + ~15 new
    → ALL edge cases — KEPT + new
  ⚠️ "Biết cơ chế ≠ giảm giá trị trải nghiệm."
purpose: |
  Entity-Valence-Dynamics.md v1.0 §2 mô tả Entity-Compiled concept + 3 subtypes.
  Connection.md §3.3 mô tả 2-luồng reward overview.
  Bond-Architecture.md §1-§2 mô tả 4 bond types × 1 Entity-Compiled mechanism.
  Love-Unified.md phân tích 6 love types (observation).
  File NÀY = MECHANISM deep-dive: HOW coupling hình thành, sustain, change.
  = Missing layer giữa "per-entity valence" (Valence-Propagation) và "tình yêu" (Love-Unified).
  Pattern: Body-Coupling.md (mechanism) → Love-Unified.md (observation)
  Tương tự: Self-Pattern-Modeling.md (mechanism) → Empathy.md (observation)
            Chunk.md (mechanism) → Feeling.md (observation)
position: |
  Core-Deep-Dive/Body-Base/ — ngang hàng Valence-Propagation.md.
  Entity-Valence-Dynamics.md v1.0 §2 → REFERENCE file này cho mechanism deep-dive.
  Connection §3.3 → REFERENCE file này cho coupling mechanism.
  Bond-Architecture → REFERENCE file này cho per-bond-type dynamics.
  Love-Unified.md → OBSERVATION file thuần (6 types, smoothing, practical).
dependencies:
  - Entity-Valence-Dynamics.md v1.0 — §1 Structural/Current, §2 Entity-Compiled, §4 3 Firing Modes, §5 Hardware-Subsidy, §6 Satiation Types
  - Valence-Propagation.md v4.0 — §1-§2 Valence definition, §3-§7 Propagation mechanism
  - Bond-Architecture.md v2.0 — §1-§2 4 bond types × 1 Entity-Compiled, §4 Resonance Decline (2 Forces + 1 Fuel), §5 anti-compiled-suppress, §6 domain coverage
  - Entity-Compiled.md v1.0 — Hub-and-Spoke, Formation 40→200h, Dunbar, Grief A+B+C
  - Entity-Access.md v1.2 — §2 Mức 0-5 gradient, §3 4 Starting Modes, Tool/Agent-mode
  - Entity-Access-Excess.md v1.0 — §3 Mức 5 excess, gap shift + compiled suppress compound
  - Entity-Access-Calibration.md v1.0 — §2 3-Layer calibration, exit cost × calibration paradox
  - PFC-Operations.md v1.0 — §3 PFC budget, §5 Compiled Quality, §8 vmPFC escalation
  - Simulation-Engine.md v1.0 — 1 Engine × 3 Components (Self-Pattern-Modeling = APPLICATION-1)
  - Resonance-Sustainability.md v1.0 — §1-§4 4-Layer model, PPR, secure base, 4 silence types
  - Resonance-Per-Entity.md v1.0 — §3 Compilation Chain, §4 Hardware-Subsidy spectrum, §6 per-entity profiles, §12 Phantom 4-factor
  - By-Product-Scale.md v1.0 — §3-§5 3 scales (Pair/Hub/Institutional), prestige vs dominance
  - Gap-Body-Need.md v1.0 — §2 3 Satiation Types, §3 5-Parameter model
  - Inter-Body-Mechanism.md v1.0 — §8 Entity-Compiled reframe, §5 By-Product Match, §4 3-cost
  - Body-Base.md v3.1 — §1.2 3 Hardware Foundations, §4.3 Compiled/Fresh axis
  - Connection.md v5.0 — §3.3 2-Stream, §15 8 pathways, Resonance Decline integration
  - Body-Feedback-Mechanism.md v2.0 — §1 Body-Need, §3 3 chunk dynamics, §5 compile_rate
  - Agent-Mechanism.md v2.0 — §12 body-need feeder, §12.2b Valence-Momentary/Valence-Structural transition
  - Self-Pattern-Modeling.md v3.1 — Compiled/Fresh, Agent-mode, §10 reversed mapping
  - By-Product-Gap-Resonance.md v1.4 — 2-Stream, by-product match, Resonance Baseline
  - Love-Unified.md v1.1 — Valence-Structural Smoothing, 2-axis, 6 types, 9 properties
  - Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State × Coupling
  - Empathy.md v4.0 — §4.6 Hardware-Subsidy × empathy, §4.7 per-entity profiles
  - Meaning.md v2.0 — §3.3 IDENTITY anchor (cho identity vacuum)
  - Protect.md v1.0 — f(replaceability × attachment), loss aversion
  - Cortisol-Baseline.md v2.0 — amplifier, holding signal, inertia
  - Idol-Phenomenon.md v2.0 — parasocial = Self-Pattern-Modeling 1-chiều
  - Religion.md v2.0 — group-level 7 functions, compound loss
  - Body-Feedback-Label.md v2.0 — vocabulary reference
sources_backup: |
  v1.1 → backup/Body-Coupling-v1.1-backup.md
  v2.0 → backup/Body-Coupling-v2.0-backup.md
  v3.0: FULL REWRITE integrating ALL Phase A+B+T+C1+C2 (28-session propagation plan C3).
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Body-Coupling — Cơ Chế Body Gắn Kết Sâu Với Entity

> **Mẹ chăm con ốm suốt đêm. Con vẫn ốm. Mẹ VẪN CHĂM.**
> **Đối thủ phá sản. Bạn sướng. Rồi tuần sau — trống rỗng.**
> **Đồng nghiệp 10 năm nghỉ việc. Bạn: "Ừ, vậy hả."**
> **Bố mẹ strict. Bạn: vừa thương vừa giận. CÙNG LÚC.**
>
> 4 agents. 4 responses KHÁC CĂN BẢN. Tại sao?
>
> Không phải vì "tình cảm nhiều ít."
> Mà vì body đã COUPLE với agent ở mức KHÁC NHAU.
>
> Mẹ: con = body-base extension (merge channels).
> Đối thủ: kẻ thù = body-base entanglement (oppose channels).
> Đồng nghiệp: ❸ ≈ 0 = no coupling (replaceable instance).
> Bố mẹ strict: vừa extension VỪA entanglement = MIXED coupling.
>
> Cùng 1 cơ chế gốc: |❸| per-agent valence compile đủ sâu
> → body treat entity AS PART OF body-base.
> Direction (positive/negative/mixed) quyết định coupling TYPE.
> Depth (sâu/nông) quyết định coupling hay forget.
>
> Yêu sâu → NHỚ LÂU. Ghét sâu → CŨNG NHỚ LÂU. Neutral → QUÊN.
> Vì |❸| quyết định persistence, KHÔNG phải direction.
>
> v3.0: Mixed coupling = PHỔ BIẾN NHẤT.
> "Vừa thương vừa giận" = NORMAL, không phải pathological.
> Càng gần lâu → càng nhiều channels cả + và - → MIXED tự nhiên.
>
> Nhưng TẠI SAO mẹ chăm con MÃI mà không chán? → Hardware-Subsidy MAXIMUM.
> Tại sao bạn thân 20 năm dần xa? → Hardware-Subsidy = NONE, phải tự maintain.
> Tại sao mệt ở công ty → về nhà hết kiên nhẫn? → PFC budget ĐÃ HẾT.
> Tại sao Mức 5 "phải ở đây" = coupling HAY addiction? → Entity-Access gradient.

---

## Mục lục

- §0 — VỊ TRÍ + SCOPE
- §1 — ❸ PER-AGENT VALENCE: BIẾN SỐ GỐC
- §2 — COUPLING OUTCOMES: 4 PATHS
- §3 — HOW COUPLING COMPILES
- §4 — COUPLING × Self-Pattern-Modeling × COMPILED/FRESH
- §5 — SMOOTHING + ANTI-SMOOTHING
- §6 — COUPLING DYNAMICS
- §7 — PARENT-CHILD TRAJECTORY
- §8 — EDGE CASES + OPEN QUESTIONS
- §9 — HONEST ASSESSMENT
- §10 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ + SCOPE

```
⭐ FILE NÀY TRONG FRAMEWORK:

  Core-Deep-Dive/Body-Base/ — MECHANISM FILE v3.0.
  Mô tả: HOW body deeply couples với entity.
  KHÔNG phải observation file.

  ⭐ SIMULATION-ENGINE CONTEXT (Simulation-Engine.md v1.0):
    1 Engine (PFC-based) × 3 Components (Self-Pattern-Modeling, Imagine-Final, Self-Observation)
    Self-Pattern-Modeling = APPLICATION-1: simulate OTHER entities.
    Body-Coupling = khi Self-Pattern-Modeling output COMPILE đủ sâu → entity = body-base.
    PFC budget: ALL coupling activities SHARE 1 budget (PFC-Operations v1.0 §3).
    Coupling cost = PFC cost (parent-child = HIGHEST).

  ⭐ ENTITY-ACCESS GRADIENT CONTEXT (Entity-Access.md v1.2):
    Mức 0 (Tool-mode): entity = function → coupling IMPOSSIBLE
    Mức 1-2: entity-access precursor → coupling UNLIKELY
    Mức 3: healthy Agent-mode → coupling POSSIBLE (healthy substrate)
    Mức 4: deep Agent-mode → coupling DEEP (Hardwired+Compilable compound)
    Mức 5: excess → coupling DISTORTED (C-dominant, projection risk)
    → Entity-Access DETERMINES coupling QUALITY, not just depth.


  PHÂN BIỆT 7 FILES GẦN NHAU:

    ┌──────────────────────────┬──────────────────────────────────────────┐
    │ File                     │ Scope                                     │
    ├──────────────────────────┼──────────────────────────────────────────┤
    │ Entity-Valence-Dynamics.md v1.0 §2         │ ENTITY-COMPILED concept: 3 subtypes,     │
    │ "Entity-Compiled"        │ Structural/Current, trajectory.           │
    │                          │ = CONCEPT ORIGIN + terminology            │
    ├──────────────────────────┼──────────────────────────────────────────┤
    │ Bond-Architecture v2.0   │ 4 bond types × 1 Entity-Compiled mechanism.           │
    │                          │ Resonance Decline. Anti-compiled-suppress.│
    │                          │ Domain coverage. Gap clone impossible.   │
    │                          │ = ARCHITECTURE per bond type             │
    ├──────────────────────────┼──────────────────────────────────────────┤
    │ Entity-Compiled v1.0     │ Hub-and-Spoke model. Formation 40→200h. │
    │                          │ Dunbar layers. Grief A+B+C.             │
    │                          │ = DEEP MECHANISM of Entity-Compiled formation         │
    ├──────────────────────────┼──────────────────────────────────────────┤
    │ Connection v5.0 §3.3     │ ❸ as GATE cho Self-Pattern-Modeling. 2-luồng overview.    │
    │ "❸ + 2-luồng"           │ Resonance Decline. 4-Layer Sustainability.│
    │                          │ = CONTEXT (coupling trong connection)    │
    ├──────────────────────────┼──────────────────────────────────────────┤
    │ Body-Coupling.md v3.0    │ HOW coupling hình thành, sustain, change │
    │ (FILE NÀY)               │ = MECHANISM deep-dive                    │
    │                          │ 3 Phase, 4 outcomes, dynamics, 2D model │
    │                          │ +Hardware-Subsidy, +PFC budget, +Entity-Access gradient  │
    ├──────────────────────────┼──────────────────────────────────────────┤
    │ Love-Unified.md          │ 6 love types, Valence-Structural Smoothing general,     │
    │                          │ 2-axis model, 9 properties, practical   │
    │                          │ = OBSERVATION file (positive coupling)   │
    ├──────────────────────────┼──────────────────────────────────────────┤
    │ Resonance-Per-Entity v1.0│ Per-entity profiles: mẹ→con, con→mẹ,   │
    │                          │ bạn thân, romantic, professional.        │
    │                          │ Compilation Chain. Hardware-Subsidy spectrum.  │
    │                          │ = PER-ENTITY dynamics deep-dive         │
    └──────────────────────────┴──────────────────────────────────────────┘

    → Entity-Valence-Dynamics.md v1.0 §2: concept ORIGIN → file này cho mechanism
    → Bond-Architecture: ARCHITECTURE per bond → file này cho coupling dynamics
    → Connection §3.3: ❸ CONTEXT → file này cho deep-dive
    → File này: MECHANISM → Love-Unified cho observation
    → Resonance-Per-Entity: per-entity dynamics → file này cho unified mechanism
    → = 7 files COMPLEMENT nhau, không duplicate


  PATTERN ĐÃ CÓ:
    Self-Pattern-Modeling.md (mechanism) → Empathy.md (observation)
    Chunk.md (mechanism) → Feeling.md (observation)
    Body-Coupling.md (mechanism) → Love-Unified.md (observation)


  TIỀN ĐỀ ĐỌC (recommend đọc TRƯỚC file này):
    → Entity-Valence-Dynamics.md v1.0 §1-§2 (Structural/Current, Entity-Compiled), §4 (3 Firing Modes)
    → Entity-Access v1.2 §2 (Mức 0-5 gradient)
    → Bond-Architecture v2.0 §1-§2 (4 bond types × 1 Entity-Compiled)
    → PFC-Operations v1.0 §3 (PFC budget concept)
    → Resonance-Per-Entity v1.0 §3-§4 (Compilation Chain, Hardware-Subsidy)
    → Resonance-Sustainability v1.0 §1-§4 (4-Layer model)


  ĐỌC FLOW:
    → Entity-Valence-Dynamics.md v1.0 §2 (Entity-Compiled concept)
    → Bond-Architecture v2.0 (4 bond types × 1 Entity-Compiled)
    → → file NÀY (coupling mechanism deep-dive)
    → → → Love-Unified.md (observation positive coupling)
    → Entity-Access v1.2 (gradient context)
    → PFC-Operations v1.0 (PFC budget context)


  SCOPE IN:
    ✅ HOW coupling hình thành (3 Phase, compile_rate, accelerators)
    ✅ 4 coupling outcomes (extension, entanglement, mixed, neutral)
    ✅ Coupling dynamics (deepen, weaken, collapse, shift)
    ✅ Smoothing/anti-smoothing as emergent property
    ✅ Parent-child trajectory (deepest case study)
    ✅ Hardware-Subsidy × coupling sustainability (v3.0)
    ✅ Entity-Access gradient × coupling depth (v3.0)
    ✅ PFC budget × coupling cost (v3.0)
    ✅ Compilation Chain × coupling formation (v3.0)

  SCOPE OUT:
    ❌ Per-entity detailed profiles → Resonance-Per-Entity v1.0
    ❌ Bond type architecture → Bond-Architecture v2.0
    ❌ Entity-Compiled formation mechanism → Entity-Compiled v1.0
    ❌ 6 love types observation → Love-Unified.md
    ❌ Empathy mechanism → Empathy.md v4.0
    ❌ Connection pathways → Connection.md v5.0


  QUY ƯỚC:
    🟢 Research support — peer-reviewed, replicated
    🟡 Framework synthesis — consistent, chưa mainstream term
    🔴 Hypothesis — testable, chưa verified
```

---

## §1 — ❸ PER-AGENT VALENCE: BIẾN SỐ GỐC

### §1.1 — Definition

```
⭐ ❸ = BODY'S EVALUATION: ENTITY NÀY ẢNH HƯỞNG BODY CHANNELS THẾ NÀO?

  (Valence-Propagation.md v4.0 §1-§2 — chi tiết. File này recap cốt lõi.)

  ❸ = valence profile per entity:
    → Multi-channel: KHÔNG phải 1 trục tốt/xấu
    → Dynamic: thay đổi theo experience
    → Context-dependent: cùng entity, khác context → khác ❸
    → Stored in schema: compiled qua experience → body respond NGAY

  Full spectrum:
    Extreme negative ↔ Mild negative ↔ Neutral ↔ Mild positive ↔ Extreme positive
    (dehumanize)     (cảnh giác)     (scan)    (approach)      (body-base extension)

  Object vs Agent:
    → Object: ít channels, ổn định, one-way, dễ thay → KHÔNG coupling
    → Agent: nhiều channels, dynamic, bidirectional, khó thay → CÓ THỂ coupling
    → Body-base coupling = dimension CHỈ CÓ ở agent valence (Entity-Valence-Dynamics.md v1.0 §1)

  ⭐ STRUCTURAL vs CURRENT VALENCE (Entity-Valence-Dynamics.md v1.0 §1 — distinction):

    STRUCTURAL VALENCE (inside Entity-Compiled):
      = Aggregate per-channel valence tags of ALL compiled chunks
      = SLOW to change (months/years — cần compile/decompile)
      = 3 subtypes: positive-dominant / negative-dominant / MIXED
      = "BODY'S DEEP RECORD" — what's STORED about entity

    CURRENT VALENCE (per-moment activation):
      = Valence-Momentary (Self-Pattern-Modeling) + activated Valence-Structural channels AT THIS MOMENT
      = FAST (changes per second, context-dependent)
      = What PFC observes → what person VERBALIZES
      = "BODY'S CURRENT EXPERIENCE" — what's ACTIVATED now

    ⭐ KEY DISTINCTION FOR COUPLING:
      Coupling = STRUCTURAL operation (compiled deep, Valence-Structural)
      PFC observation = CURRENT (tùy trigger + context + cortisol)
      "Hôm nay ghét mẹ" (current negative) ≠ "hết coupling với mẹ" (structural positive)
      → Same entity, same structural valence → DIFFERENT current valence tùy moment

    3 INTENSITY FACTORS (v3.0):
      ① PFC budget (PFC-Operations v1.0): mệt → coupling FEEL yếu (PFC không observe Valence-Structural)
      ② Entity-Access level (Entity-Access v1.2): Mức 0 = coupling OFF, Mức 3-4 = optimal
      ③ Hardware-Subsidy (Entity-Valence-Dynamics.md v1.0 §5): MAX mẹ→con → NONE bạn

  🟡 Per-entity valence = framework synthesis (Valence-Propagation.md v4.0 §1)
  🟡 Structural/Current distinction = framework synthesis (Entity-Valence-Dynamics.md v1.0 §1)
  🟢 Multi-dimensional affect: established (Russell 1980, Barrett 2006)
```

### §1.2 — ❸ GATES Self-Pattern-Modeling

```
⭐ VALENCE KHÔNG PHẢI INPUT CHO Self-Pattern-Modeling — VALENCE GATE CHO Self-Pattern-Modeling:

  (Connection.md §3.3 — tuyên bố gốc)

  ❸ quyết định: Compiled fire HƯỚNG NÀO, Fresh chain MỤC ĐÍCH NÀO.

  Cùng 1 target cue (người khóc):

  ┌──────────────────┬─────────────────────┬──────────────────┐
  │ ❸ Value          │ Compiled       │ Fresh        │
  ├──────────────────┼─────────────────────┼──────────────────┤
  │ Strong positive  │ Empathy FULL        │ Help / connect    │
  │ Neutral          │ Surface scan        │ Assess            │
  │ Mild negative    │ Empathy GIẢM       │ Avoid / defend    │
  │ Strong negative  │ REVERSED            │ Exploit / attack  │
  │                  │ (Schadenfreude)     │                   │
  │ Extreme negative │ Compiled SUPPRESS         │ Mechanical logic  │
  │                  │ (dehumanize)        │                   │
  └──────────────────┴─────────────────────┴──────────────────┘

  → CÙNG mechanism (Self-Pattern-Modeling), CÙNG cue → KHÁC output vì KHÁC ❸
  → Self-Pattern-Modeling = TOOL. ❸ = DRIVER.
  → Body đầu tư Self-Pattern-Modeling tỉ lệ |❸|:
    |❸| cao → Self-Pattern-Modeling fire deep (PHẢI understand agent — dù yêu hay ghét)
    |❸| ≈ 0 → Self-Pattern-Modeling fire thin (Mode 2 schema: "người bình thường")

  🟡 Valence as GATE = framework synthesis (Connection §3.3)
  🟢 Schadenfreude: ventral striatum (Takahashi 2009)
  🟢 Empathy modulated by fairness: Singer 2006
```

### §1.3 — 2 Luồng: Valence-Momentary (Self-Pattern-Modeling-owned) vs Valence-Structural (Entity-Compiled)

```
⭐ ❸ MANIFESTATION THÀNH 2 LUỒNG REWARD:

  (Entity-Valence-Dynamics.md v1.0 §1.4 — chi tiết. Agent-Mechanism §12.2b — origin.)

  Luồng 1 (Valence-Momentary) — Self-Pattern-Modeling-owned:
    = Body-feedback TỪ MỖI LẦN Self-Pattern-Modeling Compiled fire trên target
    = Có thể + (bạn vui → vui lây) hoặc - (con ốm → khó chịu)
    = Near-automatic, per-episode
    = THUỘC VỀ Self-Pattern-Modeling mechanism

  Luồng 2 (Valence-Structural) — Entity-Compiled:
    = COMPILED valence → agent = phần cấu trúc body-base
    = SUSTAINED — fire BẤT KỂ Valence-Momentary positive hay negative
    = Agent's state ↔ MY body-base state (structural, bidirectional)
    = THUỘC VỀ per-agent valence compiled DEEP

  ⭐ ENTITY-COMPILED 3 SUBTYPES (Entity-Valence-Dynamics.md v1.0 §1.2):

    ① Positive-dominant: "agent's wellbeing = MY wellbeing"
       → Valence-Structural fire positive khi agent thriving → EXTENSION
    ② Negative-dominant: "agent's wellbeing = MY threat"
       → Valence-Structural fire khi agent present → ENTANGLEMENT
    ③ Mixed: BOTH positive AND negative channels CÙNG LÚC
       → Valence-Structural fire oscillation by state/context → MIXED COUPLING
       → PHỔ BIẾN NHẤT — "vừa thương vừa giận" = CẢ HAI fire

  Valence-Structural emerge SAU coupling threshold (§2.1):
    → Phase 1: chỉ có Valence-Momentary (Self-Pattern-Modeling episodes)
    → Phase 2: |❸| vượt threshold → Valence-Structural emerge
    → Phase 3: Valence-Structural DRIVES behavior, independent of Valence-Momentary

  ⭐ TẠI SAO PHÂN BIỆT Valence-Momentary/Valence-Structural QUAN TRỌNG:

    Mẹ chăm con ốm: Valence-Momentary negative + Valence-Structural positive → VẪN CHĂM (Valence-Structural > Valence-Momentary)
    Bác sĩ chăm bệnh nhân: Valence-Momentary negative + Valence-Structural ≈ 0 → BURNOUT (Valence-Momentary không bù)
    Theo dõi kẻ thù: Valence-Momentary mixed + Valence-Structural negative → VẪN TRACK (entanglement drive)
    Con giận bố mẹ: Valence-Momentary negative + Valence-Structural mixed → PHỨC TẠP (vừa muốn xa vừa cần)

  ⭐ HARDWARE-SUBSIDY × Valence-Structural SUSTAINABILITY (Entity-Valence-Dynamics.md v1.0 §5 — v3.0):

    Valence-Structural compile SAU threshold — nhưng Valence-Structural SUSTAIN bao lâu?
    → PHỤ THUỘC Hardware-Subsidy (anti-habituation mechanisms per entity type):

    ┌──────────────┬──────────────────┬──────────────────────────────────┐
    │ Subsidy      │ Entity           │ Valence-Structural Sustainability                 │
    ├──────────────┼──────────────────┼──────────────────────────────────┤
    │ MAXIMUM      │ Mẹ→con           │ Multiple hardware systems counter VTA  │
    │              │                  │ habituation. Valence-Structural = RICH baseline. │
    │              │                  │ 🟢 Feldman 2012                  │
    ├──────────────┼──────────────────┼──────────────────────────────────┤
    │ MODERATE     │ Con→mẹ, kin      │ Attachment hardware scaffold. Valence-Structural slow  │
    │              │                  │ decay. 🟢 Roberts & Dunbar 2011  │
    ├──────────────┼──────────────────┼──────────────────────────────────┤
    │ TEMPORARY    │ Romantic          │ Limerence 18-36m SIMULATES rich  │
    │              │                  │ Valence-Structural. Post-limerence: subsidy GONE │
    │              │                  │ → standard rate. 🟢 Fisher 2004  │
    ├──────────────┼──────────────────┼──────────────────────────────────┤
    │ NONE         │ Bạn thân,        │ μ-opioid general only. Valence-Structural MUST   │
    │              │ colleague         │ maintain via novelty. Decay FAST │
    │              │                  │ without contact. 🟢 Panksepp 1998│
    └──────────────┴──────────────────┴──────────────────────────────────┘

    ⭐ SUBSIDY ≠ QUALITY — Subsidy = sustainability insurance:
      Highest subsidy + lowest genuine resonance = POSSIBLE (helicopter parent)
      Zero subsidy + highest genuine quality = POSSIBLE (deep friendship)
      → Subsidy determines HOW LONG coupling sustains, NOT how good it is

  🟡 2-luồng separation = framework synthesis
  🟡 Hardware-Subsidy × Valence-Structural = framework synthesis (Entity-Valence-Dynamics.md v1.0 §5)
  🟢 Compassion fatigue: Figley 2002
```

### §1.4 — Valence-Structural Phenomenology: 6 Kênh Manifest

```
⭐ Valence-Structural INVISIBLE KHI ỔN ĐỊNH (VTA habituation):

  Valence-Structural compiled deep → VTA habituated → PFC sees NOTHING.
  "Sống cùng mẹ, không cảm thấy gì đặc biệt" = Valence-Structural ĐANG CÓ, PFC không thấy.
  Valence-Structural chỉ VISIBLE qua 6 kênh gián tiếp:

  A — INVISIBLE khi ổn định: VTA habituated → "bình thường"
  B — QUA TRIGGER bên ngoài (4-tầng gradient):
      keyword → sensory direct → narrative compound → context-enhanced
      Trigger strength ≈ (entry points) × (Self-Pattern-Modeling episodes) × (Valence-Structural depth)
                         × (sensory directness) × (context amplification)
  C — QUA Self-Pattern-Modeling OUTPUT: Compiled fire → magnitude ∝ Valence-Structural depth × Compiled fidelity
  D — QUA LOSS / CHUNK-MISS: Delta = toàn bộ Valence-Structural depth → thấy LẦN ĐẦU qua ĐAU
  E — LOGIC vs FEELING MISMATCH: PFC logic (available) vs Body Valence-Structural (CHỈ khi chunks fire)
  F — PFC PROXY TRIGGER: PFC recall → chunks fire → Valence-Structural fire → body respond TỰ ĐỘNG

  ⭐ Valence-Structural ỔN ĐỊNH, PFC OBSERVATION BIẾN ĐỘNG:
    Valence-Structural = compiled deep → STABLE (thay đổi qua months/years).
    PFC observation = tùy trigger + context + cortisol → BIẾN ĐỘNG.
    "Hôm nay không thấy nhớ mẹ" ≠ "Valence-Structural mẹ giảm." Chỉ PFC hôm nay không observe.

  Chi tiết 6 kênh: Entity-Valence-Dynamics.md v1.0 §1, Drill-L2 §3 — GAP-C1.

  ⭐ 3 FIRING MODES × Valence-Structural (Entity-Valence-Dynamics.md v1.0 §4 — v3.0):

    FIRING-MAINTENANCE (entity present, hàng ngày):
      Entity PRESENT → routine fire → Valence-Structural channels active → opioid LOW-LEVEL
      VTA HABITUATED → reward = BASELINE → PFC sees NOTHING special
      = "Background warmth" — có nhưng INVISIBLE
      Hardware-Subsidy MODULATES Firing-Maintenance:
        HIGH subsidy (mẹ→con): Firing-Maintenance = RICH baseline (hardware counter-habituate)
        NONE subsidy (bạn): Firing-Maintenance = LEAN baseline (VTA habituate FASTER)

    FIRING-CHUNK-MISS (entity absent, cấp tính):
      Entity ABSENT → compiled routine fire → no response → PAIN
      = 🟢 O'Connor 2023: basal ganglia VẪN fire "entity sẽ ở đây"
        TRONG KHI medial temporal biết "đã mất/xa" → 2 systems CONFLICT
      Calibration speed: Entity-Compiled depth × hardware-subsidy × alternative gap-fill

    FIRING-CONTEXT-TRIGGER (entity absent, tình cờ):
      External cue → match Entity-Compiled spoke → hub activate → Valence-Structural fire → body-feedback
      Triggers: sensory direct → narrative → olfactory → circumstantial
      = UNPREDICTABLE (context-dependent)
      Intensity = f(cue specificity × Entity-Compiled depth × current gap state × hardware-subsidy)

    → 3 Firing Modes = COUPLING LIFECYCLE khi entity present → absent → triggered
    → Chi tiết: Entity-Valence-Dynamics.md v1.0 §4

  🟡 6-channel model = framework synthesis từ Drill-L2 §3
  🟡 3 Firing Modes = framework synthesis (Entity-Valence-Dynamics.md v1.0 §4)
  🟢 VTA habituation: established mechanism
  🟢 Sensory bypass PFC: Proust phenomenon, established
  🟢 O'Connor 2023: basal ganglia habit circuits in grief
```

### §1.5 — Satiation Types × Coupling Channels ★ NEW v3.0

```
⭐ MỖI COUPLING CHANNEL CÓ SATIATION TYPE RIÊNG (Entity-Valence-Dynamics.md v1.0 §6, Gap-Body-Need v1.0 §2):

  CYCLIC VALENCE — SHARP OSCILLATION:
    Gap fill → reward → gap OFF → gap RETURN → need again
    = MOST VISIBLE (high delta per cycle). MOST FORGETTABLE (episode-bound).
    VD coupling: mẹ la (avoidance Cyclic) → mẹ thôi (relief) → episode-bound
    VD coupling: đói → mẹ nấu (approach Cyclic) → no → hết → lại đói

  TONIC VALENCE — SLOW INVISIBLE BASELINE:
    Gap fill ongoing → reward LOW-LEVEL → VTA habituate → INVISIBLE
    = LEAST VISIBLE (below PFC threshold). SLOWEST DECAY (compiled deep).
    = DEVASTATING when removed (baseline violation = large delta)
    VD coupling: comfort từ mẹ = 20 năm background → mẹ mất → PAIN

  GENERATIVE VALENCE — RENEWABLE EXCITING:
    Gap fill → new gap CREATE → new fill → perpetual
    = MOST VISIBLE (high novelty = high delta). FASTEST HABITUATION without novelty.
    VD coupling: bạn thân kể chuyện mới → insight → new question → reward

  ⭐ PER-ENTITY COUPLING = COMPOUND SATIATION PROFILE:
    Mẹ→con: Tonic dominant + Generative bursts (child changes daily)
    Bạn thân: Generative dominant + Tonic minor
    Romantic post-limerence: Tonic + Generative (if genuine match)
    Colleague: Generative only (domain-specific)
    → Chi tiết per-entity: Resonance-Per-Entity v1.0 §6

  ⭐ "CHÁN" = GENERATIVE DIES + TONIC INVISIBLE:
    "Vẫn thoải mái nhưng không exciting" = Tonic intact, Generative dead
    PFC chỉ thấy: no Generative reward + Tonic invisible = "chán"
    Body reality: Tonic STILL PROVIDES, PFC just can't see it
    → Tại sao "chán" partner ≠ "hết yêu" → chỉ Generative habituated

  🟡 Satiation types × coupling = framework synthesis (Entity-Valence-Dynamics.md v1.0 §6)
  🟡 "Chán" reframe = framework insight
```

---

## §2 — COUPLING OUTCOMES: 4 PATHS

### §2.1 — Definition + Phase Transition

```
⭐ COUPLING = KHI |❸| VƯỢT NGƯỠNG → BƯỚC NHẢY CHẤT:

  TRƯỚC ngưỡng (Phase 1 — §3.1):
    → Body "đánh giá" entity: ❸ = evaluation
    → Self-Pattern-Modeling fire → Valence-Momentary episodes → ❸ update
    → Entity = NGOÀI body-base — chỉ được "đo lường"

  SAU ngưỡng (Phase 2-3 — §3.1):
    → Body "gắn kết" entity: ❸ compiled structural
    → Entity = PHẦN CỦA body-base (extension, entanglement, hoặc mixed)
    → Valence-Structural emerge — INDEPENDENT of Valence-Momentary
    → = QUALITATIVE SHIFT, không chỉ "❸ mạnh hơn"

  BƯỚC NHẢY CHẤT — VERIFY:
    Object strong positive (xe quý): ❸ positive, nhưng mất = "tiếc" (resource)
    Agent coupled positive (con): ❸ compiled deep, mất = "đau" (body-base amputation)
    → 2 loại loss KHÁC CĂN BẢN → chứng minh có threshold
    → Entity-Valence-Dynamics.md v1.0 §1: "Grief ≠ tiếc — grief = body-base amputation"

  4 COUPLING OUTCOMES (v2.0):
    → ❸ positive đủ sâu → EXTENSION (yêu sâu)
    → ❸ negative đủ sâu → ENTANGLEMENT (ghét sâu)
    → ❸ MIXED channels đủ sâu → MIXED COUPLING (vừa thương vừa giận) ★ NEW
    → |❸| ≈ 0 → NEVER vượt → NO COUPLING (neutral)


  ⭐ 2D MODEL — MAP TOÀN BỘ COUPLING SPACE:

                    |❸| DEPTH
                      ↑
                      │
  COUPLED   DEEP      │    ENTANGLEMENT ◄─ flip ─► EXTENSION
  (Phase 3)           │    (ghét sâu)    rare→     (yêu sâu)
                      │                 ←fast
                      │        ★ MIXED COUPLING ★
                      │    (vừa thương vừa giận — per-channel)
                      │
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ ─ ─ THRESHOLD ─ ─ ─ ─ ─ ─
                      │
  COMPILING MODERATE  │    "Ghét"                  "Quý"
  (Phase 1)           │
            THIN      │    "Khó chịu"              "Thích"
                      │
            ZERO      │  ─── NEUTRAL ─── (indifference)
                      │     Đồng nghiệp 10 năm
                      └───────────────────────────→
                    NEGATIVE        ❸        POSITIVE
                              DIRECTION

  ĐỌC MAP:
    → Vertical: |❸| depth → quyết định persistence + coupling
    → Horizontal: ❸ direction → quyết định extension vs entanglement
    → Threshold: phase transition — trên = coupled, dưới = compiling
    → "Thin line love-hate" = cả hai ở tầng DEEP → shift ngang
    → "Opposite of love = indifference" = neutral ở zero, không phải hate
    → ★ MIXED: KHÔNG nằm giữa trục ngang — nằm Ở CẢ HAI BÊN CÙNG LÚC
      (per-channel: một số channels positive, một số negative — Entity-Valence-Dynamics.md v1.0 §1.2)

  🟡 2D model = framework synthesis
  🟡 Phase transition (threshold) = framework claim — consistent với
     qualitative difference giữa "thích" và "yêu" mà mọi người report
```

### §2.2 — EXTENSION (positive-compiled coupling)

```
⭐ ❸ POSITIVE DEEP → AGENT CHANNELS = MY CHANNELS (MERGE):

  (Entity-Valence-Dynamics.md v1.0 §1.2 ① — concept. Love-Unified — observation deep-dive.)

  KHI COUPLING POSITIVE HÌNH THÀNH:
    → Body treat agent's body-base channels AS OWN channels
    → Con đói = TÔI đói (structural, not just empathy)
    → Bạn thân buồn = TÔI buồn (structural + Self-Pattern-Modeling compound)
    → Vợ/chồng thành công = TÔI thành công (channel merge)

  BIỂU HIỆN:
    → Valence-Structural Smoothing emerge (§5): bỏ qua flaws, amplify positives
    → Self-Pattern-Modeling fire deep + empathic (Compiled strong, Fresh help)
    → Loss = body-base amputation → grief (§6.5)
    → Phantom Valence-Structural: chunks fire → agent absent → acute pain

  GRADIENT (Love-Unified §1.1):
    Thích (Valence-Momentary dominant) → Quý (Valence-Structural emerging) → Yêu (Valence-Structural compiled)
    → KHÔNG binary → liên tục → threshold ở đâu đó giữa "quý" và "yêu"

  6 LOẠI extension (Love-Unified §4):
    Romantic, Parent→Child, Child→Parent, Friendship, Mentor, Pet
    → CÙNG mechanism, KHÁC channels + accelerators + depth
    → Chi tiết: Love-Unified.md (observation file)

  ⭐ 4 BOND TYPES × 1 Entity-Compiled MECHANISM (Bond-Architecture v2.0 §1-§2 — v3.0):

    5 nghiên cứu hội tụ: Bartels & Zeki 2004, Young & Wang 2004,
    Feldman 2017, Lim et al. 2022, Pearce et al. 2017
    → CÙNG hardware core (VTA, striatum, oxytocin-dopamine crosstalk)
    → KHÁC neurochemical configuration per bond type:

    ┌──────────────┬─────────────┬──────────────┬────────────────┐
    │ Bond Type    │ Hardware Primary  │ Gap Direction │ Coupling Style │
    ├──────────────┼─────────────┼──────────────┼────────────────┤
    │ Parent→Child │ Oxytocin    │ Self-ref      │ Caregiving     │
    │              │ dominant    │ (parent's gap)│ (Tonic base)   │
    ├──────────────┼─────────────┼──────────────┼────────────────┤
    │ Child→Parent │ Opioid      │ Need-based    │ Safety bond    │
    │              │ dominant    │ (child's gap) │ (foundational) │
    ├──────────────┼─────────────┼──────────────┼────────────────┤
    │ Romantic     │ OT+Dopamine │ Mutual        │ Pair bond      │
    │              │ multi-sys   │ (both gaps)   │ (limerence→Valence-Structural) │
    ├──────────────┼─────────────┼──────────────┼────────────────┤
    │ Friendship   │ Endorphin   │ By-product    │ Pure resonance │
    │              │ dominant    │ (each own gap)│ (Generative)   │
    └──────────────┴─────────────┴──────────────┴────────────────┘

    = CÙNG Entity-Compiled mechanism, KHÁC configuration.

  ⭐ DOMAIN COVERAGE PER BOND (Bond-Architecture v2.0 §6):
    KHÔNG bond type nào = ✅ ở TẤT CẢ domains.
    Partner: BEST hardware+emotional → nhưng ❌ career
    Friend: BEST social+emotional → nhưng mỗi friend ≠ all domains
    Colleague: BEST career → nhưng ❌ hardware
    → CẦN PORTFOLIO of entities = Dunbar layers (Entity-Compiled v1.0)
    → "Vợ là tất cả" = FRAGILE (all gaps = one entity loss = catastrophic)

  🟢 Attachment bond = body-level: Bowlby 1969
  🟢 Social pain = physical pain: Eisenberger 2003
  🟢 Bartels & Zeki 2004: maternal + romantic overlap VTA/striatum
  🟢 Feldman 2017: ALL bond types use OT-dopamine crosstalk
  🟢 Pearce et al. 2017: endorphin across social bonds
  🟡 "Extension" as explicit mechanism = framework synthesis
  🟡 4 bond types × 1 Entity-Compiled = framework synthesis (Bond-Architecture v2.0)
```

### §2.3 — ENTANGLEMENT (negative-compiled coupling)

```
⭐ ❸ NEGATIVE DEEP → AGENT CHANNELS = THREATS TO MY CHANNELS (OPPOSE):

  (Entity-Valence-Dynamics.md v1.0 §1.2 ② — concept.)

  KHI COUPLING NEGATIVE HÌNH THÀNH:
    → Body treat agent's channels AS THREATS to own channels
    → Kẻ thù mạnh lên = TÔI nguy (their gain = my threat)
    → Kẻ thù đau = TÔI an toàn hơn (their pain = my relief)
    → Kẻ thù's state = QUAN TRỌNG cho body-base (structural tracking)

  BIỂU HIỆN:
    → Anti-smoothing emerge (§5): amplify flaws, smooth positives
    → Self-Pattern-Modeling fire deep + reversed/strategic (Compiled reversed, Fresh exploit)
    → Loss = 4-tầng mixed response (§6.6)
    → Phantom entanglement: chunks fire → alert → agent absent → confused

  GRADIENT:
    Khó chịu → Ghét → Thù (entangled)
    → Threshold: "ghét" vẫn có thể Phase 1. "Thù" = Phase 3 coupled.


  ⭐ ENTANGLEMENT ≠ EXTENSION ĐẢO NGƯỢC — CÓ ĐẶC THÙ RIÊNG:

    ① COMPILE NHANH HƠN positive:
      → Negativity bias (🟢 Baumeister 2001): negative > positive in processing
      → Fear conditioning one-trial (🟢 LeDoux 1996): 1 event đủ
      → Positive cần repetition dài. Negative có thể 1 event.

    ② Self-Pattern-Modeling INVESTMENT CỰC SÂU (vì survival):
      → Body PHẢI predict kẻ thù → Self-Pattern-Modeling fire DEEP dù ❸ negative
      → Đối thủ kinh doanh 15 năm: "hiểu" đối thủ SÂU hơn hiểu bạn bè

    ③ 4 ACCELERATORS RIÊNG:

      BETRAYAL: Valence-Structural positive → violent flip (Entity-Valence-Dynamics.md v1.0 §1) → Valence-Structural negative INSTANT
        → TẬN DỤNG existing compiled chunks → chỉ re-tag valence
        → = Accelerator MẠNH NHẤT: càng thân → flip càng mạnh

      TRAUMA: 1 event CỰC mạnh → amygdala compile NGAY
        → 🟢 Fear conditioning one-trial (LeDoux 1996)

      THREAT-SUSTAINED: Kẻ thù = threat liên tục → cortisol holding signal
        → Cortisol buộc Self-Pattern-Modeling replay (Body-Feedback-Mechanism §3.3) → compile NHANH hơn

      INHERITED: "Phe kia = xấu" installed qua community/media
        → Entity-Valence-Dynamics.md v1.0 §2 install propagation: chain compile TRƯỚC khi gặp cá nhân


  ⭐ NEGATIVE COUPLING ⊇ TRAUMA CONDITIONING:

    Trauma conditioning (🟢 LeDoux):
      → Stimulus → fear response (sensory, generalized)
      → KHÔNG CẦN Self-Pattern-Modeling: không cần "hiểu" kẻ tấn công

    Negative coupling:
      → Agent-SPECIFIC: biết AI, behavior patterns, weaknesses
      → CẦN Self-Pattern-Modeling deep: predict, track, exploit/avoid

    Phần lớn trường hợp: CẢ HAI cùng lúc:
      → ① Trauma conditioning: giọng nói → freeze (generalized)
      → ② Negative coupling: nhớ MẶT, TÊN → Self-Pattern-Modeling deep (agent-specific)
      → Coupling = layer TRÊN trauma conditioning (khi agent-specific)


  5 CASES VERIFY:

    C1 Bully thời thơ ấu:
      → 30 năm sau VẪN NHỚ MẶT, TÊN → body fire alert
      → Foundational (childhood compile) → gần permanent

    C2 Người phản bội:
      → 10 năm thân → 1 lần phản bội → NHỚ SUỐT ĐỜI
      → Accelerator: betrayal (existing depth re-tagged)

    C3 Đối thủ kinh doanh:
      → 15 năm cạnh tranh → biết RÕ mọi pattern
      → Đối thủ phá sản → relief + emptiness (§6.6)

    C4 Kẻ bạo hành:
      → Trauma conditioning + negative coupling compound
      → Dual: generalized (giọng) + specific (người cụ thể)

    C5 "Phe kia" chính trị:
      → Inherited accelerator: schema install sẵn
      → Individual member CÓ THỂ override (face-to-face revise ❸)

  ⭐ RESONANCE DECLINE × NEGATIVE COUPLING (Bond-Architecture v2.0 §4 — v3.0):

    Cùng 2 Forces + 1 Fuel apply cho ENTANGLEMENT (not just positive coupling):

    FORCE: COMPILED-SUPPRESS (★ LEVERAGE POINT — tấn công NGUỒN):
      → Suppress own drives FOR tracking enemy
      → "Phải biết kẻ thù đang làm gì" = compiled suppress own domain
      → Attacks SOURCE of independent drive
      → In entanglement = OBSESSION (suppress own life FOR enemy)
      → Accelerates Reward-Habituated + drains novelty fuel

    FORCE: REWARD-HABITUATED (hardware adaptation, ĐỘC LẬP):
      → Same threat repeated → VTA giảm fire (Weber-Fechner)
      → Đối thủ 15 năm: threat stimulus quen → bớt sắc nét
      → = POSITIVE for entanglement: threat habituates NATURALLY

    FUEL: NOVELTY ≥ THRESHOLD? (calibration parameter):
      → 2 lenses:
        Prediction: Self-Pattern-Modeling compiled hoàn hảo → no prediction-delta → no alert
        Knowledge: all chunks about enemy compiled → plateau → no new info
      → = POSITIVE for entanglement: hết "fuel" → obsession fades

    CONTEXTUAL: GAP DRIFT (direction diverge):
      → Life directions change → enemy becomes less relevant
      → Gap landscape shift → other priorities emerge

    → 2 Forces + 1 Fuel ALSO cause ENTANGLEMENT FADE (not just positive coupling)
    → Reward-Habituated + novelty exhaustion = HEALTHY natural fading
    → Compiled-Suppress in entanglement = OBSESSION (suppress own life FOR enemy)
    → FIX: giải phóng drive riêng → entanglement loses grip

  🟡 Entanglement concept = framework synthesis
  🟡 Resonance Decline × entanglement = framework synthesis (Bond-Architecture v2.0 §4)
  🟢 Negativity bias: Baumeister et al. 2001
  🟢 Fear conditioning one-trial: LeDoux 1996
  🟢 Betrayal trauma: Freyd 1996
```

### §2.4 — MIXED COUPLING (mixed-compiled) ★ NEW v2.0

```
⭐ ❸ MIXED CHANNELS DEEP → VỪA EXTENSION VỪA ENTANGLEMENT CÙNG LÚC:

  (Entity-Valence-Dynamics.md v1.0 §1.2 ③ — concept. Inter-Body v1.0 §8.2 — reframe origin.)

  v1.1 CHỈ CÓ: Extension / Entanglement / Neutral = 3 outcomes.
  v2.0: MIXED = outcome thứ 4 — VÀ LÀ PHỔ BIẾN NHẤT.


  ⭐ MIXED COUPLING LÀ GÌ:

    Entity đã compile DEEP — NHƯNG per-CHANNEL valence profile:
      → Một số channels POSITIVE (merge)
      → Một số channels NEGATIVE (oppose)
      → KHÔNG AVERAGE thành 1 số → CẢ HAI tồn tại song song
      → STATE/TRIGGER/CONTEXT quyết định channel nào DOMINANT tại 1 thời điểm

    ┌──────────────────────────────────────────────┐
    │ VALENCE PROFILE "Mẹ strict" (multi-channel): │
    │                                              │
    │   Nutrition:  ++ (nuôi nấng)                │
    │   Comfort:    ++ (an ủi, ôm ấp)            │
    │   Autonomy:   -- (ép học, cấm đoán)         │
    │   Mastery:    + (dạy kỹ năng)              │
    │   Status:     +/- (khen/chê trước mặt khách)│
    │                                              │
    │   "Vừa thương vừa giận" = CẢ HAI fire       │
    │   STATE quyết định channel nào dominant      │
    └──────────────────────────────────────────────┘


  ⭐ TẠI SAO MIXED PHỔ BIẾN NHẤT:

    → Relationship dài → nhiều interaction types → nhiều channels compile
    → CÀNG GẦN nhau LÂU → càng nhiều channels (cả + và -)
    → "Thuần positive" = rare luxury of LIMITED interactions
    → Paradox: GẦN NHAU LÂU = deeper bond + deeper conflict potential
    → = Same person: STRONGEST positive channel + STRONGEST negative channel

    Verify (% = illustrative, không đo lường):
      Bạn thân 20 năm: 90% positive nhưng VẪN CÓ friction → ③ mild
      Vợ chồng 30 năm: deep love + deep annoyance → ③ significant
      Bố mẹ strict: nurture ++ và autonomy -- → ③ PARADIGM CASE
      Đồng nghiệp 10 năm: neutral → ❸ ≈ 0 → NO mixed (no coupling)


  ⭐ MIXED TRÊN 2D MODEL:

    Mixed KHÔNG nằm ở "giữa" trục Negative ↔ Positive.
    Mixed = TRÊN threshold, có channels Ở CẢ HAI BÊN:

    Extension và Entanglement = PURE cases (majority channels 1 hướng).
    Mixed = GENERAL case (channels mixed).
    Pure = SPECIAL case (happens khi interactions chủ yếu 1 hướng).

    = SPECTRUM: pure positive ←← ③ mixed →→ pure negative
    Hầu hết coupled relationships = SOMEWHERE trong spectrum mixed.


  ⭐ MIXED COUPLING OSCILLATION:

    Behavior oscillation KHÔNG phải "flip-flop" (Entity-Valence-Dynamics.md v1.0 §1 violent flip khác).
    = State/context/trigger ACTIVATE channels khác nhau:

    Con nhớ mẹ nấu ăn → nutrition channel fire → warm (① mode)
    Con nhớ mẹ ép học → autonomy channel fire → frustrated (② mode)
    Cùng 1 entity, cùng 1 coupling depth — KHÁC state → KHÁC experience.

    → PFC CONFUSED: "Mình yêu hay ghét mẹ?" = wrong question
    → Correct: "Mình yêu VÀ giận mẹ — ở channels KHÁC NHAU"


  ⭐ DEVELOPMENTAL COMPLEXITY GRADIENT:

    Trẻ nhỏ: entity valence SIMPLER (fewer channels, less mixed)
    Trẻ lớn: begin mixed (more channels compile)
    Người lớn: MAXIMUM mixed (most relationships = ③ varying degrees)
    = Complexity IS NORMAL, not pathological
    → Chi tiết trajectory: §7 Parent-child trajectory

  🟡 Mixed coupling as explicit outcome = framework synthesis (Drill §11.10)
  🟢 Ambivalence = well-documented (Cacioppo & Berntson 1994)
  🟢 Multi-dimensional affect evaluation: Barrett 2006
```

### §2.5 — NEUTRAL (no coupling)

```
⭐ |❸| ≈ 0 → KHÔNG BAO GIỜ VƯỢT THRESHOLD → QUÊN:

  PARADIGM CASE: đồng nghiệp 10 năm

  TẠI SAO KHÔNG COMPILE:
    compile_rate ≈ f(repetition × saliency × peak_valence × multi_modal × contingency)
    → repetition CAO (gặp mỗi ngày)
    → NHƯNG: saliency × peak_valence × multi_modal × contingency ≈ 0
    → repetition × 0 = 0 → KHÔNG compile dù bao lâu

  TẠI SAO BASE FACTORS ≈ 0:
    → Agent REPLACEABLE: đổi người → workflow vẫn chạy
    → Interaction = logic, professional → peak_valence thấp
    → Respond TO TASK, không respond TO MY STATE → contingency thấp
    → Self-Pattern-Modeling fire Mode 2 (schema "đồng nghiệp") → thin chunks

  2 FEEDBACK LOOPS TỰ CỦNG CỐ:

    LOW-❸ LOOP (đồng nghiệp):
      Replaceable → body không invest ❸
        → Self-Pattern-Modeling thin → chunks thin → DỄ QUÊN
          → confirms replaceable → ❸ VẪN THẤP → loop

    HIGH-❸ LOOP (bạn thân / kẻ thù):
      Irreplaceable → body invest ❸ deep
        → Self-Pattern-Modeling deep → chunks deep → KHÓ QUÊN
          → confirms irreplaceable → ❸ THÊM SÂU → loop

    → 2 loops dẫn tới 2 outcomes CỰC: coupled DEEP hoặc forget HOÀN TOÀN
    → Ít agents ở giữa vì loops ĐẨY ra 2 cực

  ⭐ NHƯNG ĐỒNG NGHIỆP CÓ THỂ TRƯỢT SANG PATH A/B:

    Đồng nghiệp → bạn thân (Path A):
      → Shared vulnerability event → saliency ↑ → ❸ shift positive
      → Loop switch: low → high → compile bắt đầu

    Đồng nghiệp → kẻ thù (Path B):
      → Conflict / betrayal → saliency CỰC CAO → ❸ shift negative
      → Loop switch: low → high negative → compile nhanh
      → CÓ THỂ 1 event đủ (negativity bias)

  ⭐ ENTITY-ACCESS MỨC 0-1 = STRUCTURAL IMPOSSIBILITY (Entity-Access v1.2 — v3.0):

    Entity-Access Mức 0 (Tool-mode/Service):
      → Predict FUNCTION only → no Self-Pattern-Modeling on entity STATE
      → No Valence-Momentary episodes about entity → no ❸ accumulation → NEVER vượt threshold
      → = Structural impossibility of coupling at Tool-mode
      → VD: ATM, vending machine, taxi driver (function only)

    Entity-Access Mức 1-2 (precursor):
      → Minimal entity-access → thin Self-Pattern-Modeling → thin chunks
      → ❸ accumulate VERY SLOWLY → threshold nearly unreachable
      → VD: barista quen mặt nhưng không biết tên

    → Neutral path (§2.5) CÓ THỂ do ❸ ≈ 0 HOẶC do Entity-Access quá thấp
    → BOTH prevent coupling qua DIFFERENT mechanisms

  🟡 2 feedback loops = framework synthesis
  🟡 Entity-Access Mức 0-1 × neutral = framework synthesis (Entity-Access v1.2)
  🟢 Hedonic adaptation: Brickman 1978 (neutral baseline concept)
```

### §2.6 — SYSTEM COMPILATION (per-context, KHÔNG per-agent)

```
⭐ PHÂN BIỆT: COUPLING (per-agent) vs SYSTEM COMPILATION (per-context):

  Body compile ở TẦNG KHÁC NHAU cho entities khác nhau:
    → Đồng nghiệp CỤ THỂ: ❸ ≈ 0 → no coupling → quên
    → Công ty TỔNG THỂ: nhiều mechanisms compound → nhớ

  2 LOẠI DEEP COMPILATION:

  ┌──────────────────────┬──────────────────────┬──────────────────────┐
  │                      │ COUPLING              │ SYSTEM COMPILATION   │
  │                      │ (per-agent)            │ (per-context)        │
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Target               │ Agent CỤ THỂ          │ Context / abstract   │
  │                      │ (mẹ, bạn, kẻ thù)    │ (công ty, quốc gia)  │
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Core mechanism       │ ❸ per-agent compile   │ 6 mechanisms         │
  │                      │ + Self-Pattern-Modeling deep             │ COMPOUND (dưới)      │
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Members              │ IRREPLACEABLE          │ REPLACEABLE          │
  │                      │ (per-agent specific)   │ (instances in schema)│
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Valence-Structural?   │ CÓ (Valence-Momentary  │ KHÔNG (no per-agent) │
  │                      │ →Valence-Structural    │ Nhưng CÓ compound    │
  │                      │ transition)            │ structural effect    │
  ├──────────────────────┼──────────────────────┼──────────────────────┤
  │ Loss                 │ Grief (amputation)     │ Compound Chunk-Miss  │
  │                      │ / Dissolution          │ + identity disruption│
  └──────────────────────┴──────────────────────┴──────────────────────┘


  ⭐ 6 MECHANISMS COMPOUND TẠO SYSTEM COMPILATION:

    ① ❶ Hardware belonging:
      → "Among my people" → continuous baseline social presence signal
      → Agent-Mechanism §12.5: walking on street → body feel safe
      → Pre-Self-Pattern-Modeling: body-level, not cognitive

    ② Identity anchor:
      → "Tôi là kỹ sư FPT" / "Tôi là người Việt"
      → Meaning §3.3: IDENTITY type life-level anchor

    ③ Valence chain install:
      → Entity-Valence-Dynamics.md v1.0 §2 install propagation: "Quốc gia → cờ → tự do → an toàn"
      → Body fire khi BẤT KỲ node nào triggered

    ④ Routine compile:
      → 10 năm × mỗi ngày = HÀNG NGHÌN patterns compiled
      → Body-Feedback-Mechanism §5: baseline shift → routine = "bình thường"
      → Mất routine → Chunk-Miss compound

    ⑤ Collective effervescence:
      → 🟢 Durkheim 1912: mass gathering → shared emotional state
      → Agent-Mechanism §12.5: mass Self-Pattern-Modeling co-firing → Resonance at group scale

    ⑥ Schema-agent (Schema-Pure-Trust/Imagined-Overlay):
      → Agent-Mechanism §12.4: Đức Mẹ, quốc phụ = virtual agent → body fire presence

  → 6 mechanisms CÙNG compile → COMPOUND effect CỰC MẠNH
  → Binh lính chết cho đất nước = compound 6 mechanisms (not per-agent)


  ⭐ COUPLING PROXY — LEADER + SYMBOL:

    Group = abstract entity → body KHÔNG THỂ couple trực tiếp

    LEADER as coupling proxy:
      → Leader = agent THẬT → per-agent ❸ CÓ THỂ deep
      → Mất leader = per-agent grief + group loss COMPOUND

    SYMBOL as trigger proxy:
      → Cờ = trigger cho toàn bộ valence chain → body fire
      → KHÔNG PHẢI coupling (cờ ≠ agent) → trigger proxy

    MEMBERS as replaceable instances:
      → ❸ per-member ≈ 0 (replaceable)
      → INHERIT group valence: "đồng bào" → default positive
      → Per-agent ❸ CÓ THỂ override group schema


  ⭐ GROUP LOSS = COMPOUND SYSTEM LOSS:
    Mất per-agent: 8 pathways cắt × 1 agent
    Mất group/context: 6 system mechanisms × TOÀN BỘ compiled patterns
    → Exile/refugee grief = 6 mechanisms MẤT CÙNG LÚC → kéo dài SUỐT ĐỜI

  ⭐ NEGATIVE GROUP: ANTI-SMOOTHING AT SCALE:
    In-group: system compilation positive → smooth flaws
    Out-group: installed negative chain → anti-smooth
    → "Online thì ghét, gặp nhau thì bình thường"
      = online → group schema chạy, face-to-face → per-agent ❸ compile

  🟡 System compilation vs coupling distinction = framework synthesis
  ⭐ BY-PRODUCT-SCALE × SYSTEM COMPILATION (By-Product-Scale v1.0 — v3.0):

    System compilation = Scale-Hub + Scale-Institutional of By-Product-Scale model:

    Scale-Pair: per-agent coupling (A↔B, direct verify, oxytocin/dopamine)
      → = §2.1-§2.5 NÀY. Coupling = Scale-Pair.
    Scale-Hub: node↔{followers} (trust bypass, serotonin)
      → Leader = coupling proxy (per-agent ❸ through node)
      → Prestige node = genuine resonance at hub scale
      → Dominance node = forced interaction → schema tag → fragile
    Scale-Institutional: distributed (institutional trust, abstract)
      → School, government, religion = system compilation at institutional scale
      → Individual = replaceable instance

    → Coupling = Scale-Pair mechanism
    → System compilation = Scale-Hub + Scale-Institutional mechanism
    → BOTH co-exist: body couple per-agent (Scale-Pair) AND compile system (Scale-Hub/Institutional)
    → Chi tiết: By-Product-Scale.md v1.0

  🟡 System compilation vs coupling distinction = framework synthesis
  🟡 6-mechanism model = framework synthesis
  🟡 By-Product-Scale mapping = framework synthesis (By-Product-Scale v1.0)
  🟢 Collective effervescence: Durkheim 1912
  🟢 In-group favoritism: Tajfel 1979
```

---

## §3 — HOW COUPLING COMPILES

### §3.1 — 3 Phase Model

```
⭐ COUPLING HÌNH THÀNH QUA 3 PHASE VỚI FEEDBACK LOOPS:


  PHASE 1 — PRE-COUPLING: ❸ khởi tạo, Self-Pattern-Modeling theo
  ──────────────────────────────────────────────

    ❸ hình thành từ 4 nguồn (Entity-Valence-Dynamics.md v1.0 §1):
      ① Direct experience (chính xác nhất, chậm nhất)
      ② Observed experience (Self-Pattern-Modeling on others)
      ③ Schema inheritance (nhanh nhất, có thể sai)
      ④ Context inference (tùy chunks available)

    ❸ GATE Self-Pattern-Modeling (§1.2) → Self-Pattern-Modeling fire theo hướng ❸:
      → Valence-Momentary episodes sinh ra → ❸ update (reinforce hoặc revise)
      → Chunks compile thêm → Self-Pattern-Modeling fire tốt hơn lần sau
      → = FEEDBACK LOOP: ❸ → Self-Pattern-Modeling → Valence-Momentary → ❸ update

    ┌──────────────────────────────────────────┐
    │  ❸ body-base evaluation                  │
    │    ↓ (GATE)                              │
    │  Self-Pattern-Modeling fires (direction set by ❸)          │
    │    ↓                                     │
    │  Valence-Momentary episodes (momentary body-feedback)   │
    │    ↓                                     │
    │  Chunks compile (if saliency sufficient) │
    │    ↓                                     │
    │  ❸ update (reinforce or revise)          │
    │    ↓                                     │
    │  [LOOP — mỗi vòng ❸ shift thêm]         │
    └──────────────────────────────────────────┘


  PHASE 2 — COUPLING THRESHOLD: bước nhảy chất
  ──────────────────────────────────────────────

    Khi |❸| compile đủ sâu qua nhiều vòng Phase 1:
      → QUALITATIVE SHIFT (không linear)
      → Body KHÔNG CHỈ "đánh giá" → BẮT ĐẦU treat AS body-base

    ❸ positive đủ sâu → EXTENSION emerge
    ❸ negative đủ sâu → ENTANGLEMENT emerge
    ❸ mixed channels đủ sâu → MIXED COUPLING emerge
    ❸ ≈ 0 → NEVER reach threshold

    ⚠️ Threshold CHÍNH XÁC: chưa biết (🔴 open question)
      → Likely NONLINEAR (step function? sigmoid?)
      → Likely PER-PERSON (hardware + experience khác → threshold khác)
      → Observable: difference giữa "quý" (phase 1) và "yêu" (phase 2+3)


  PHASE 3 — POST-COUPLING: coupling DRIVES Self-Pattern-Modeling
  ──────────────────────────────────────────────

    SAU threshold, Valence-Structural emerge:
      → Valence-Structural DRIVES Self-Pattern-Modeling investment — INDEPENDENT of Valence-Momentary
      → = Self-reinforcing: coupling → more Self-Pattern-Modeling → more chunks → deeper coupling

    ┌──────────────────────────────────────────┐
    │  Valence-Structural (coupling established)    │
    │    ↓ (DRIVE — independent of Valence-Momentary)         │
    │  Self-Pattern-Modeling fires DEEP + SUSTAINED             │
    │    ↓                                     │
    │  Chunks compile even deeper              │
    │    ↓                                     │
    │  Coupling strengthens                    │
    │    ↓                                     │
    │  [SELF-REINFORCING — càng sâu càng sâu]  │
    └──────────────────────────────────────────┘

    Verify:
      Mẹ chăm con ốm: Valence-Momentary = negative. Valence-Structural = positive. VẪN CHĂM → Valence-Structural drive.
      Track kẻ thù: Valence-Momentary = mixed. Entanglement drive. VẪN TRACK → coupling drive.
      Con giận bố mẹ: Valence-Momentary = negative. Valence-Structural = mixed. VẪN CẦN → mixed coupling drive.
      Đồng nghiệp: no coupling → no Valence-Structural → Self-Pattern-Modeling thin → rời → quên.


  ⭐ CHIỀU NHÂN QUẢ:

    Phase 1: ❸ TRƯỚC → Self-Pattern-Modeling THEO (❸ = initiator)
    Phase 2: |❸| đủ sâu → coupling EMERGE
    Phase 3: coupling TRƯỚC → Self-Pattern-Modeling THEO (coupling = sustainer)

    → "Ai trước?" = ❸ trước (Phase 1)
    → "Ai sustain?" = coupling (Phase 3)
    → Self-Pattern-Modeling = TOOL ở CẢ 2 phase — không bao giờ là driver

  ⭐ COMPILATION CHAIN MAPPING (Resonance-Per-Entity v1.0 §3 — v3.0):

    3 Phase model NÀY maps onto Compilation Chain:
      Stage 1 (Fresh dominant) = Phase 1 pre-coupling (HIGH cost, cautious)
      Stage 2 (Compiled developing) = Phase 1→2 transition (cost DECREASING)
      Stage 3 (Baseline compiled) = Phase 3 post-coupling (cost ≈ 0)
      Stage 4 (Dynamics) = 3 trajectories:
        4A Sustained (both grow → new by-products) → coupling THRIVES
        4B Habituated flat (no new by-products) → "chán nhưng không muốn mất"
        4C Resonance death (compiled suppress gap riêng) → coupling DIES

    Compilation rate per entity type:
      Mẹ→con: SKIP Stage 1-2 (hormone accelerator) → directly Stage 3
      Romantic: ACCELERATED Stage 1-2 (limerence) → 18-36m → Stage 3
      Bạn thân: STANDARD 40→80→200h (no accelerator) → gradual → Stage 3
      Colleague: SLOW (domain-only, Agent-mode moments) → may never reach Stage 3

  🟡 3 Phase model = framework synthesis
  🟡 Compilation Chain mapping = framework synthesis (Resonance-Per-Entity v1.0 §3)
  🟡 Phase transition concept = consistent với attachment research
  🟢 Self-reinforcing loops in relationships: established concept
```

### §3.2 — Developmental Sequence: 3 Paths + Mixed Emergence

```
⭐ TỪ STARTING POINT (❸ = 0), 3 PATHS PHÂN KỲ:

  STARTING POINT: body gặp entity mới
    → ❶ Hardware detect agent → body ready
    → ❸ = blank (hoặc có schema inheritance sẵn)
    → Self-Pattern-Modeling fire surface scan


  PATH A — POSITIVE (→ extension):
  ──────────────────────────────────
    Interaction → hợp → Resonance emerge → Valence-Momentary positive
    → ❸ shift positive → Self-Pattern-Modeling invest thêm → chunks sâu hơn
    → Lần sau: có compiled data → Self-Pattern-Modeling fire tốt hơn → Resonance dễ hơn
    → Loop tích cực → ❸ tiếp tục positive → compile deeper
    → Nếu đủ sâu → vượt threshold → EXTENSION

    compile_rate base factors TĂNG DẦN:
      saliency ↑ (agent bắt đầu quan trọng)
      peak_valence ↑ (shared joy/vulnerability)
      contingency ↑ (respond TO MY STATE, not generic)
      → TÍCH CỰC: càng thân → compile càng nhanh


  PATH B — NEGATIVE (→ entanglement):
  ─────────────────────────────────────
    Interaction → conflict/threat/harm → Valence-Momentary negative
    → ❸ shift negative → Self-Pattern-Modeling fire strategic/reversed
    → Chunks compile (threat = high saliency)
    → Loop tích cực NGƯỢC → ❸ tiếp tục negative → compile deeper
    → Nếu đủ sâu → vượt threshold → ENTANGLEMENT

    compile_rate base factors CŨNG TĂNG:
      saliency ↑↑ (threat = CỰC CAO)
      peak_valence ↑↑ (negative peaks mạnh — negativity bias)
      → + Confirmation bias: ❸ negative → filter positive evidence


  PATH C — NEUTRAL (→ no coupling, forget):
  ────────────────────────────────────────────
    Interaction → bình thường → Valence-Momentary ≈ 0
    → ❸ shift ≈ 0 → Self-Pattern-Modeling fire thin (Mode 2)
    → Chunks thin → lần sau vẫn thin → ❸ vẫn ≈ 0
    → FLAT — không có loop tích cực
    → NEVER reach threshold → no coupling → forget khi rời context

    → Đồng nghiệp 10 năm: Path C suốt
    → CÓ THỂ switch path: trigger event → saliency spike → chuyển A hoặc B


  ⭐ PATH SWITCH POSSIBLE:

    C → A: đồng nghiệp → bạn thân
      Trigger: shared vulnerability, crisis together, personal disclosure
    C → B: đồng nghiệp → kẻ thù
      Trigger: betrayal, conflict, competition (1 event có thể đủ)
    A → B: bạn → kẻ thù (betrayal — Entity-Valence-Dynamics.md v1.0 §1)
      → NHANH: existing depth re-tagged (§6.3)
    B → A: kẻ thù → bạn (rare — §6.4)
      → CHẬM: 3 lực cản (§6.4)


  ⭐ MIXED EMERGENCE FROM PATH A (★ v2.0):

    Path A coupled (extension) + TIME + DEEP interaction:
      → Nhiều channels compile → một số channels DEVELOP negative
      → ① pure positive → ③ mixed emerge → ③ deepen
      → = NATURAL progression, KHÔNG phải pathological
      → Paradigm: parent-child (§7), vợ chồng lâu năm

    Path B coupled (entanglement) + context shift:
      → Một số channels develop positive (exposure → humanize)
      → ② pure negative → ③ mixed emerge
      → Rarer nhưng CÓ: kẻ thù lâu → begrudging respect

    → MIXED = destination cho MANY coupled relationships khi đủ lâu
    → Pure ① hoặc ② = either EARLY stage hoặc LIMITED interaction

  🟡 3 paths model = framework synthesis
  🟡 Mixed emergence from time = framework prediction (Entity-Valence-Dynamics.md v1.0 §1.2)
  🟢 Negativity bias in relationship formation: Baumeister 2001
```

### §3.3 — compile_rate: |peak_valence| quyết định

```
⭐ FORMULA KHÔNG CẦN SỬA — CHỈ CẦN HIỂU |❸|:

  compile_rate ≈ f(repetition × saliency × peak_valence × multi_modal × contingency)
  (Body-Feedback-Mechanism v2.0 §5 — formula gốc)

  peak_valence CHỨA cả positive VÀ negative:
    → |peak_valence| CỰC DƯƠNG → compile deep (yêu sâu → NHỚ LÂU)
    → |peak_valence| CỰC ÂM → compile deep (ghét sâu → CŨNG NHỚ LÂU)
    → peak_valence ≈ 0 → compile thin (neutral → QUÊN)
    → = |❸| depth = tích phân compile_rate theo thời gian

  ⭐ REPETITION = MULTIPLIER, KHÔNG PHẢI DRIVER:

    Nếu base = saliency × peak_valence × multi_modal × contingency ≈ 0:
      → repetition × 0 = 0 → 10 năm cũng KHÔNG compile
      → = Đồng nghiệp 10 năm

    Nếu base > 0 (moderate):
      → repetition AMPLIFY → compile SÂU DẦN DẦN
      → = Friendship: no accelerator → cần thời gian

    Nếu base = CỰC CAO (extreme event):
      → repetition = 1 ĐÃ ĐỦ
      → 🟢 Fear conditioning one-trial (LeDoux 1996)
      → = Kẻ giết con: 1 event × extreme base → compile NGAY

  ⭐ NEGATIVE COMPILE NHANH HƠN POSITIVE:

    → 🟢 Negativity bias (Baumeister 2001): negative > positive ở:
      processing speed, memory retention, attention capture
    → 1 lần phản bội > 100 lần giúp đỡ (ở impact on ❸)
    → = CÙNG formula, nhưng negative events SCORE CAO HƠN

  ⭐ HARDWARE-SUBSIDY × COMPILE_RATE (Entity-Valence-Dynamics.md v1.0 §5 — v3.0):

    Hardware-Subsidy = IMPLICIT FACTOR trong compile_rate:
      MAX (mẹ→con): oxytocin + synchrony AMPLIFY saliency + contingency
        → compile_rate BOOSTED at body-level (trước khi formula tính)
      TEMPORARY (romantic): limerence AMPLIFY peak_valence + multi_modal
        → compile_rate TURBO 18-36m, then STANDARD
      NONE (bạn): no hardware boost → formula operates at base rate
        → compile_rate = pure interaction quality

    → Hardware-Subsidy ≠ thêm factor mới — mà MODULATE existing factors
    → Mẹ→con compile nhanh VÌ hardware boost saliency + contingency
    → Bạn compile chậm VÌ no hardware boost → cần repetition × quality cao

  🟡 |peak_valence| as key driver = framework insight
  🟡 Repetition = multiplier = framework insight
  🟡 Hardware-Subsidy × compile_rate = framework synthesis (Entity-Valence-Dynamics.md v1.0 §5)
  🟢 compile_rate factors: each grounded (Schultz 1997, Crespi 1942, etc.)
```

### §3.4 — Accelerators

```
⭐ 4 POSITIVE + 4 NEGATIVE ACCELERATORS:

  POSITIVE COUPLING ACCELERATORS (Love-Unified §3.4):

    ① BIOLOGICAL (parent):
      → Pregnancy 9 tháng = body-base connection nghĩa đen
      → Birth hormones: oxytocin flood
      → = Instant seed → interaction reinforce

    ② HORMONAL (romantic):
      → Limerence: dopamine + oxytocin + NE + serotonin ↓
      → = Months turbo cho Valence-Structural compile

    ③ ENVIRONMENTAL (combat):
      → Extreme shared conditions × life/death saliency
      → Body-Feedback-Mechanism §5: ALL compile factors CỰC CAO
      → = Weeks turbo (band of brothers)

    ④ NONE (friendship):
      → Purely accumulated interaction
      → = Years gradual → nhưng CÓ THỂ rất sâu


  NEGATIVE COUPLING ACCELERATORS:

    ① BETRAYAL (violent flip):
      → Existing deep positive → re-tag negative INSTANT
      → TẬN DỤNG compiled depth → không compile từ 0
      → = MẠNH NHẤT: càng thân → flip càng mạnh

    ② TRAUMA (one-trial):
      → 1 event CỰC mạnh → amygdala compile NGAY
      → 🟢 LeDoux 1996: fear conditioning one-trial
      → KHÔNG cần Self-Pattern-Modeling → body-level direct

    ③ THREAT-SUSTAINED (cortisol holding):
      → Threat liên tục → cortisol holding signal
      → Body buộc Self-Pattern-Modeling replay (Body-Feedback-Mechanism §3.3) → compile nhanh
      → = Bully mỗi ngày, đối thủ liên tục

    ④ INHERITED (schema install):
      → "Phe kia = xấu" installed qua community/media
      → Entity-Valence-Dynamics.md v1.0 §2 install propagation
      → Compile TRƯỚC khi gặp cá nhân

  🟡 8 accelerators unified model = framework synthesis
  🟢 Each accelerator grounded: oxytocin, limerence, fear conditioning, etc.
```

### §3.5 — Foundational vs Additive

```
🟡 2 LOẠI DEPTH KHÁC CĂN BẢN:

  FOUNDATIONAL (childhood compile):
    → Compile khi brain ĐANG phát triển → "xi măng ướt"
    → Chunks compile vào STRUCTURE đang hình thành
    → Gần PERMANENT — therapy CÓ THỂ rewrite nhưng CỰC KHÓ
    → = Parent-child coupling (cả 2 hướng)
    → = Childhood bully → vẫn fire 30 năm sau

  ADDITIVE (adult compile):
    → Compile lên structure ĐÃ hình thành → "xi măng khô"
    → CÓ THỂ remove (dù đau) → recovery possible
    → = Romantic, friendship, adult enemies
    → = Chia tay → heal (additive removed)
      nhưng xa bố mẹ toxic → khó heal hoàn toàn (foundational)

  CẢ POSITIVE VÀ NEGATIVE ĐỀU CÓ foundational:
    → Parent coupling: foundational positive (mẹ tốt) hoặc foundational negative (mẹ toxic)
    → Childhood trauma: foundational negative → near-permanent entanglement

  ⭐ FOUNDATIONAL + MIXED = MOST COMPLEX (★ v2.0):
    → Parent-child coupling: foundational + often mixed (§7)
    → = KHÁC CĂN BẢN so với additive coupling
    → Foundational mixed: positive channels + negative channels ĐỀU near-permanent
    → = Tại sao "adult children of toxic parents" struggle SUỐT ĐỜI
      nhưng vẫn KHÔNG thể hoàn toàn cắt đứt (foundational positive VẪN fire)

  🟢 Critical/sensitive periods: Bowlby 1969, Rutter 2004
  🟡 Foundational vs Additive distinction = framework synthesis
```

### §3.6 — Entity-Access Gradient × Coupling Depth ★ NEW v3.0

```
⭐ ENTITY-ACCESS MỨC 0-5 DETERMINES COUPLING QUALITY (Entity-Access v1.2):

  Entity-Access gradient = HOW MUCH body invests in modeling entity's STATE.
  Coupling depth = HOW DEEP entity integrates into body-base.
  2 dimensions INTERACT but NOT identical:

  ┌──────────┬────────────────────────┬──────────────────────────────────┐
  │ Entity-Access Level │ Self-Pattern-Modeling Mode               │ Coupling Implication              │
  ├──────────┼────────────────────────┼──────────────────────────────────┤
  │ Mức 0    │ Tool-mode: predict     │ Coupling IMPOSSIBLE. No entity   │
  │          │ function only           │ state → no ❸ accumulation.      │
  ├──────────┼────────────────────────┼──────────────────────────────────┤
  │ Mức 1-2  │ Precursor: minimal     │ Coupling UNLIKELY. Thin Self-Pattern-Modeling     │
  │          │ entity-access           │ → thin chunks → threshold xa.   │
  ├──────────┼────────────────────────┼──────────────────────────────────┤
  │ Mức 3    │ Agent-mode: predict    │ Coupling HEALTHY. A+B dominant   │
  │          │ entity STATE            │ → genuine resonance substrate.  │
  │          │ Compilable-dominant, moderate    │ Self-correcting. Optimal.       │
  ├──────────┼────────────────────────┼──────────────────────────────────┤
  │ Mức 4    │ Agent-mode: deep       │ Coupling DEEP. Hardwired+Compilable compound.    │
  │          │ Hardwired+Compilable compound            │ HIGH confidence. Can be healthy │
  │          │                        │ if A+B dominant (not C).        │
  ├──────────┼────────────────────────┼──────────────────────────────────┤
  │ Mức 5    │ Agent-mode: C-DISTORTED│ Coupling EXCESS territory.      │
  │ (Excess) │ Self-Pattern-Modeling serves MY gap      │ Projection risk. Gap shift +    │
  │          │ not entity's state      │ compiled suppress compound.     │
  │          │                        │ → Entity-Access-Excess v1.0     │
  └──────────┴────────────────────────┴──────────────────────────────────┘

  ⭐ ENTITY-ACCESS × COUPLING × BOND TYPE:
    Mẹ→con: hardware auto-pushes to Mức 4 (healthy) → Mức 5 risk (helicopter)
    Romantic limerence: hormone pushes to Mức 4-5 → post-L recalibrate to 3-4
    Bạn thân: pure interaction → typically Mức 3 (healthy, self-correcting)
    Colleague: typically Mức 0-2 → coupling rare (Tool-mode dominant)

  ⭐ EXIT COST × COUPLING CALIBRATION PARADOX (Entity-Access-Calibration v1.0):
    Strongest coupling = hardest to calibrate (highest exit cost)
    Child can't "exit" parent → "no" signal WEAK → parent Mức 5 goes unchecked
    Self-awareness = ONLY calibration source for high-exit-cost bonds

  🟡 Entity-Access gradient × coupling = framework synthesis (Entity-Access v1.2)
  🟡 Exit cost × calibration paradox = framework synthesis (Entity-Access-Calibration v1.0)
```

---

## §4 — COUPLING × Self-Pattern-Modeling × COMPILED/FRESH

```
⭐ COUPLING INTERACT VỚI Self-Pattern-Modeling VÀ RESONANCE BASELINE:

  (Chi tiết: Love-Unified §4.2b-§4.2c. File này = cơ chế gốc.)
  (Compiled/Fresh terminology: Inter-Body v1.0 §3, Body-Base v3.0 §4.3)


  §4.1 — Self-Pattern-Modeling bị ❸ GATE (recap §1.2):
    ❸ positive → Compiled empathy + Fresh help
    ❸ negative → Compiled reversed + Fresh exploit
    ❸ mixed → Compiled oscillation + Fresh confused
    ❸ ≈ 0 → Self-Pattern-Modeling gần không fire deep

  §4.2 — Resonance Baseline → Compiled vs Fresh dominant:
    Resonance Baseline cao (hợp tính — Resonance §4):
      → Self-template FIT target → Compiled output chính xác
      → = "Tự nhiên hiểu" → warm coupling
    Resonance Baseline thấp (khác tính):
      → Self-template FAIL → Fresh dominant
      → = "Hiểu bằng logic" → structured coupling

  §4.3 — Coupling × Compiled/Fresh → 4 quadrants:

    ┌────────────┬───────────────────────┬───────────────────────┐
    │            │ Compiled dominant           │ Fresh dominant             │
    ├────────────┼───────────────────────┼───────────────────────┤
    │ Positive   │ WARM LOVE             │ STRUCTURED LOVE       │
    │ coupling   │ Bỏ qua flaws,         │ Amplify flaws to fix, │
    │            │ protective            │ instrumental          │
    │            │ "Con tôi OK mà"       │ "Con phải cố hơn"    │
    ├────────────┼───────────────────────┼───────────────────────┤
    │ Negative   │ VISCERAL HATE         │ STRATEGIC HATE        │
    │ coupling   │ Body-level disgust,   │ Calculated enmity,    │
    │            │ Schadenfreude strong  │ exploit weaknesses    │
    │            │ "Thấy mặt muốn đấm"  │ "Chờ thời cơ"        │
    └────────────┴───────────────────────┴───────────────────────┘

  §4.4 — MIXED COUPLING × Compiled/Fresh (★ v2.0):

    Mixed coupling: Compiled và Fresh BOTH fire — nhưng KHÁC channels:
      Compiled fire trên channels ĐÃ compiled positive → warm
      Compiled fire trên channels compiled negative → visceral frustration
      Fresh fire khi PFC try resolve contradiction → EFFORTFUL

    → Mixed coupling = HIGHEST Self-Pattern-Modeling cost:
      PFC draft cost (③): phải process CONFLICTING channels
      Possible suppress cost (②): suppress negative khi cần positive
      = Inter-Body v1.0 §4: 3 independent cost sources ALL apply

  §4.5 — Self-Pattern-Modeling 3 Modes khi coupled (parent-child example):
    Mode 1: Self-template direct (cost ≈ 0 nếu Resonance match)
    Mode 2: Schema fallback ("xã hội nói X → phải X")
    Mode 3: Effortful Self-Pattern-Modeling (PFC Capacity + meta-awareness)
    → Chi tiết: Love-Unified §4.2c (Self-Pattern-Modeling 3 modes + dậy sớm example)

  🟡 4 quadrants = framework synthesis
  🟡 Mixed × Compiled/Fresh = v2.0 framework synthesis
  🟡 Self-Pattern-Modeling 3 Modes = framework synthesis (Love-Unified)
```

### §4.6 — PFC Budget × Coupling Cost ★ NEW v3.0

```
⭐ COUPLING = PFC COST (PFC-Operations v1.0 §3):

  ALL coupling activities SHARE 1 PFC budget:
    → Self-Pattern-Modeling on entity (Compiled + Fresh)
    → Suppress own reactions (② suppress cost)
    → Process conflicting channels in mixed coupling (① PFC draft)
    → Monitor entity state changes (ongoing attention)

  PFC BUDGET FINITE → coupling activities COMPETE with ALL other activities:
    → Work (domain tasks) + Social (other entities) + Self-monitor
    → "Mệt ở công ty → về nhà hết kiên nhẫn với con"
      = PFC budget DEPLETED at work → no remaining budget for coupling quality

  ⭐ PARENT-CHILD = HIGHEST PFC COST (PFC-Operations §9):
    → Con = MOVING TARGET (thay đổi liên tục) → Self-Pattern-Modeling re-draft liên tục
    → Hardware mismatch (con ≈ 50% genetic + different era) → ② suppress + ① hold
    → Hormone support giảm dần (oxytocin strongest 0-5, giảm teen)
    → Asymmetric: bố mẹ Self-Pattern-Modeling con = Fresh (con luôn thay đổi)
      Con Self-Pattern-Modeling bố mẹ = mostly Compiled (bố mẹ ổn định)
    → Teenager = highest PFC cost period (biggest change + least hormone support)

  ⭐ COMPILED SUPPRESS FOR COUPLING (PFC-Operations §8):
    → Suppress OWN drives FOR partner/entity → vmPFC load
    → "Mất bản thân vì yêu" = systematic suppress non-partner domains
    → Escalation: suppress nhiều domains → vmPFC STRUCTURAL damage
      → McEwen 2007: chronic stress → dendritic retraction
      → Enough doors closed → room DARK = systemic helplessness

  🟡 PFC budget × coupling = framework synthesis (PFC-Operations v1.0 §3)
  🟡 Parent-child = highest PFC cost = framework synthesis (PFC-Operations §9)
  🟢 PFC depletion: Baumeister ego-depletion research (contested but mechanism valid)
  🟢 vmPFC structural damage: McEwen 2007
```

### §4.7 — Compiled Quality × Coupling ★ NEW v3.0

```
⭐ COMPILE-TIME LOCK DETERMINES COUPLING QUALITY (PFC-Operations v1.0 §5):

  Chunks compile với DIRECTION tag at moment of compilation.
  Tag = PERMANENT post-compile. 3 types:

  ┌──────────────────┬───────────────┬──────────────────────────────────┐
  │ Compiled Quality │ Tag           │ Coupling Implication              │
  ├──────────────────┼───────────────┼──────────────────────────────────┤
  │ GENUINE          │ APPROACH      │ Coupling tự-reinforcing.         │
  │                  │ (opioid)      │ "Thích ở bên → ở thêm → thích   │
  │                  │               │ hơn." Compound growth.           │
  ├──────────────────┼───────────────┼──────────────────────────────────┤
  │ SCHEMA           │ FLAT          │ Coupling stable IF bridge.       │
  │                  │ (relief)      │ "Phải ở bên vì nghĩa vụ."      │
  │                  │               │ Functional nhưng not warm.       │
  ├──────────────────┼───────────────┼──────────────────────────────────┤
  │ THREAT           │ AVOIDANCE     │ Coupling = burnout trajectory.   │
  │                  │ (threat)      │ "Phải ở bên vì sợ."            │
  │                  │               │ Decays without threat.           │
  └──────────────────┴───────────────┴──────────────────────────────────┘

  ⭐ PARENT-CHILD COMPILE QUALITY:
    Con compile mẹ lúc mẹ ÂU YẾM → genuine tag → "thương mẹ tự nhiên"
    Con compile mẹ lúc mẹ ĐE DỌA → threat tag → "sợ mẹ" (giỏi nhưng ghét)
    SAME mẹ, DIFFERENT moment = DIFFERENT tag = DIFFERENT coupling quality
    → Mixed coupling OFTEN = mixed COMPILE QUALITY (genuine + threat channels)

  🟡 Compiled quality × coupling = framework synthesis (PFC-Operations v1.0 §5)
  🟡 Compile-time lock = framework insight
```

### §4.8 — Hardware-Subsidy × Coupling Sustainability ★ NEW v3.0

```
⭐ HARDWARE-SUBSIDY = WHY SAME COUPLING DEPTH → DIFFERENT SUSTAINABILITY:

  (Entity-Valence-Dynamics.md v1.0 §5, Resonance-Per-Entity v1.0 §4 — chi tiết. File này = coupling context.)

  ┌──────────────┬────────────┬────────────────┬───────────────────────┐
  │ Subsidy      │ Entity     │ Coupling        │ Loss Severity          │
  │              │            │ Sustainability  │                       │
  ├──────────────┼────────────┼────────────────┼───────────────────────┤
  │ MAXIMUM      │ Mẹ→con    │ AUTO-SUSTAIN    │ DEVASTATING           │
  │              │            │ (hardware counter-    │ (all 4 phantom factors│
  │              │            │ habituate)      │ MAX)                  │
  ├──────────────┼────────────┼────────────────┼───────────────────────┤
  │ MODERATE     │ Con→mẹ,   │ SCAFFOLD        │ MAJOR                 │
  │              │ kin        │ (attachment hardware  │ (hardware still fires)      │
  │              │            │ slows decay)    │                       │
  ├──────────────┼────────────┼────────────────┼───────────────────────┤
  │ TEMPORARY    │ Romantic   │ LIMERENCE MASK  │ COMPLEX               │
  │              │            │ 18-36m. Post-L: │ (hormone echo if      │
  │              │            │ standard rate.  │ limerence; structural │
  │              │            │ "Hết lửa."     │ if genuine)           │
  ├──────────────┼────────────┼────────────────┼───────────────────────┤
  │ NONE         │ Bạn thân, │ MUST MAINTAIN   │ MINOR-MODERATE        │
  │              │ colleague  │ via novelty.    │ (replaceable if no    │
  │              │            │ Decay FAST      │ deep Entity-Compiled)              │
  │              │            │ without contact.│                       │
  └──────────────┴────────────┴────────────────┴───────────────────────┘

  ⭐ PARADOX: SUBSIDY ≠ QUALITY:
    Mẹ→con: MAX subsidy + LOW genuine resonance = helicopter parent
    Bạn thân: ZERO subsidy + HIGH genuine resonance = deepest voluntary bond
    → Subsidy = HOW LONG coupling sustains automatically
    → Quality = HOW GOOD the coupling IS (genuine vs schema vs threat)
    → BEST coupling = genuine quality + moderate-to-high subsidy

  🟡 Hardware-Subsidy × coupling sustainability = framework synthesis (Entity-Valence-Dynamics.md v1.0 §5)
  🟢 Feldman 2012: biobehavioral synchrony mẹ-con
  🟢 Fisher 2004: limerence neuroscience
  🟢 Panksepp 1998: social bonding endogenous opioids
```

### §4.9 — Entity-Access × Coupling Interaction ★ NEW v3.0

```
⭐ ENTITY-ACCESS LEVEL DETERMINES COUPLING MODE (Entity-Access v1.2):

  Entity-Access = HOW body models entity (Tool-mode vs Agent-mode).
  Coupling REQUIRES Agent-mode (predict entity STATE, not just function).

  COUPLING MODE per Entity-Access level:

    Mức 0-2 (Tool/Precursor): NO coupling possible
      → Self-Pattern-Modeling on function only → no ❸ about entity state → no Valence-Structural
      → "10 năm dùng ATM → zero coupling"

    Mức 3 (Agent-mode, Compilable-dominant): HEALTHY coupling
      → Self-Pattern-Modeling on entity state → genuine resonance possible
      → Self-correcting: A+B dominant → calibration maintained
      → "Bạn thân hiểu nhau, tôn trọng khác biệt"

    Mức 4 (Deep Agent-mode): DEEP coupling
      → Hardwired+Compilable compound → HIGH confidence, deep Entity-Compiled
      → Can be healthy IF A+B dominant (not C-distorted)
      → "Vợ chồng hiểu nhau sâu, tin tưởng"

    Mức 5 (Excess): DISTORTED coupling
      → C-dominant: Self-Pattern-Modeling serves MY gap, not entity's state
      → Projection risk: "project MY needs onto entity"
      → Gap shift + compiled suppress COMPOUND (Entity-Access-Excess v1.0 §5.3)
      → "Phải ở đây / Phải theo ý tôi" = excess territory
      → Chi tiết: §8.7 Entity-Access-Excess × Coupling

  ⭐ ENTITY-ACCESS CÓ THỂ SHIFT ALONG COUPLING:
    Phase 1 (pre-coupling): Entity-Access = Mức 1-3 (exploring)
    Phase 2 (threshold): Entity-Access → Mức 3-4 (deepening)
    Phase 3 (post-coupling): Entity-Access = Mức 3-4 (stable) HOẶC Mức 5 (excess)
    → Healthy trajectory: 1→3→4 (stable)
    → Unhealthy trajectory: 1→3→5 (excess)

  🟡 Entity-Access × coupling interaction = framework synthesis (Entity-Access v1.2)
  🟡 Coupling mode per Entity-Access level = framework synthesis
```

---

## §5 — SMOOTHING + ANTI-SMOOTHING = PROPERTY CỦA COUPLING

```
⭐ SMOOTHING/ANTI-SMOOTHING = EMERGENT PROPERTY, KHÔNG PHẢI MECHANISM RIÊNG:

  (Chi tiết: Love-Unified §2. File này = principle gốc.)

  KHI COUPLING POSITIVE + DEEP → Valence-Structural SMOOTHING EMERGE:
    → Individual negative attributes bị OVERWHELM bởi mass Valence-Structural positive
    → PFC nhận: "net smooth" → attributes "biến mất"
    → Người THẬT SỰ "không thấy" — không phải giả vờ
    → = Halo effect tổng quát (🟢 Thorndike 1920)

  KHI COUPLING NEGATIVE + DEEP → ANTI-SMOOTHING EMERGE:
    → Individual positive attributes bị OVERWHELM bởi mass Valence-Structural negative
    → PFC nhận: "net negative" → positives "biến mất"
    → "Ghét → áo họ xấu, ý kiến họ sai"
    → = Horns effect (🟢 Nisbett 1977)

  ⭐ MIXED COUPLING → OSCILLATING SMOOTHING (★ v2.0):
    → Channels positive → smooth negatives ở THOSE channels
    → Channels negative → anti-smooth positives ở THOSE channels
    → NET: KHÔNG TOÀN SMOOTH, KHÔNG TOÀN ANTI-SMOOTH
    → = State-dependent: positive state → smoothing mode; negative state → anti-smoothing
    → = "Hôm nay mẹ OK lắm" (positive channels active → smooth)
      → "Hôm nay mẹ quá đáng" (negative channels active → anti-smooth)

  FORMULA (approximation):
    smoothing_capacity ≈ |coupling depth| — max(Schema_A, competing_schemas)
    → |coupling depth| > Schema_A → attribute BỊ SMOOTH
    → |coupling depth| < Schema_A → attribute VISIBLE → PFC flag
    → ⚠️ Body-level Schema_A (compiled trauma) → XUYÊN QUA smoothing
      (Love-Unified §2.4: bạo lực VẪN nhận ra dù đang yêu)

  SYMMETRY:
    Positive deep → smooth negatives + amplify positives
    Negative deep → smooth positives + amplify negatives
    Mixed deep → oscillation by active channel
    Neutral (|❸| ≈ 0) → closest to objective evaluation
    → "Blind review" trong khoa học = remove ❸ → closer to fair

  3 CHỨC NĂNG ĐỒNG THỜI:
    ① FILTER: giảm/xóa attributes ngược hướng coupling
    ② AMPLIFIER: tăng attributes cùng hướng coupling
    ③ PROPAGATION: lan sang associated entities (Entity-Valence-Dynamics.md v1.0 §2)
    → Chi tiết: Love-Unified §2.2

  ⭐ STRUCTURAL vs CURRENT × SMOOTHING (Entity-Valence-Dynamics.md v1.0 §1):

    Structural valence = SOURCE of smoothing (compiled deep → persistent bias)
    Current valence = MOMENT of smoothing visibility (context activates)

    Structural positive + Current negative:
      = "Mẹ đang la → tức" (current) nhưng smoothing VẪN hoạt động ở background
      = Sẽ quên chuyện la nhanh vì structural positive SMOOTH nó
    Structural mixed + Current positive:
      = "Hôm nay mẹ OK" → smoothing mode ON cho session này
      = Negative channels DORMANT → temporarily "không thấy" flaws

  ⭐ SATIATION TYPE × SMOOTHING (Entity-Valence-Dynamics.md v1.0 §6):
    Tonic channels: INVISIBLE smooth (baseline → PFC không thấy → MOST PERSISTENT)
    Generative channels: VISIBLE smooth (novelty amplifies bias → STRONGEST khi active)
    Cyclic channels: EPISODE-BOUND smooth (active during cycle, off between → WEAKEST)

  🟡 Smoothing/Anti-smoothing as emergent property = framework synthesis
  🟡 Oscillating smoothing in mixed coupling = v2.0 framework synthesis
  🟡 Structural/Current × smoothing = framework synthesis (Entity-Valence-Dynamics.md v1.0 §1)
  🟡 Satiation × smoothing = framework synthesis (Entity-Valence-Dynamics.md v1.0 §6)
  🟢 Halo/horns effect: Thorndike 1920, Nisbett 1977
  🟢 PFC giảm khi xem ảnh partner: Bartels & Zeki 2000
```

---

## §6 — COUPLING DYNAMICS

### §6.1 — Deepen (self-reinforcing)

```
🟡 COUPLING → Self-Pattern-Modeling → CHUNKS → DEEPER COUPLING:

  Phase 3 loop (§3.1): coupling DRIVES Self-Pattern-Modeling → chunks compile → coupling strengthen
  = Self-reinforcing — càng yêu càng sâu, càng ghét càng sâu
  
  Positive: bạn thân 20 năm → hàng nghìn Resonance episodes → calibrated DEEP
  Negative: đối thủ 15 năm → hàng nghìn strategic Self-Pattern-Modeling → knowledge DEEP
  Mixed: bố mẹ-con → BOTH deepen → positive AND negative channels CÙNG sâu
  
  Brake tự nhiên:
    → Time/attention finite → không thể deepen UNLIMITED agents
    → = Dunbar numbers: ~5 intimate, ~15 close (coupling capacity limited)

  ⭐ 4-LAYER SUSTAINABILITY × COUPLING DEEPEN (Resonance-Sustainability v1.0 — v3.0):

    Coupling deepens sustainably ONLY when ALL 4 layers intact:

    Tầng 1 FOUNDATION: Proximity × Duration × Agent-mode
      → Must be physically/virtually close enough for by-products to reach
      → 40→80→200h formation requires sustained contact
      → Agent-mode (NOT Tool-mode) = minimum for coupling

    Tầng 2 MODALITY: Verbal + Non-verbal + Body-level
      → Silent resonance = REAL if body-level + non-verbal active
      → 4 silence types: Intrinsic (✅) vs Introjected/External/Spontaneous
      → Only Intrinsic silence sustainable for coupling

    Tầng 3 AMPLIFICATION: PPR + Secure base
      → PPR: understood + validated + cared for (PERCEPTION > actual)
      → Secure base: available + noninterference + encouragement
      → Secure base = positive spiral (exploration → by-products → coupling)

    Tầng 4 TRAJECTORY: Novelty + Maintenance + Synchrony
      → Must maintain novelty (Generative) for coupling growth
      → Synchrony (body-level) for coupling depth

    → Chi tiết: Resonance-Sustainability v1.0 §1-§4
```

### §6.2 — Weaken (fade)

```
🟡 COUPLING CÓ THỂ FADE KHI KHÔNG REINFORCED:

  Additive coupling (adult): no reinforcement → chunks DECAY dần
    → = "Dần xa nhau" = compiled chunks weaken
    → Recovery possible khi re-connect (chunks re-activate)
  
  Foundational coupling (childhood): decay CỰC CHẬM
    → = 30 năm xa mẹ → gặp lại → VẪN fire mạnh
  
  Negative coupling: CŨNG decay nhưng CHẬM HƠN positive
    → Negativity bias: negative chunks decay slower
    → = 20 năm sau vẫn tức khi nhớ phản bội

  Mixed coupling decay:
    → Positive channels và negative channels decay Ở TỐC ĐỘ KHÁC:
    → Negative channels decay CHẬM HƠN (negativity bias)
    → = Xa bố mẹ strict: dần NHỚ positive, VẪN GIỮ negative
    → = Tại sao "trưởng thành hiểu bố mẹ" = positive reassert, negative vẫn âm ỉ
  
  🟢 Extinction learning: Bouton 2004 (decay ≠ erasure)
```

### §6.3 — Collapse: Love → Hate (FAST)

```
⭐ BETRAYAL ACCELERATOR — NHANH NHẤT TRONG MỌI COUPLING DYNAMICS:

  Mechanism (Entity-Valence-Dynamics.md v1.0 §1 violent flip):
    → Valence-Structural positive deep → toàn bộ compiled chunks VỚI valence positive
    → 1 event phản bội → new chunk [betrayal] compile CỰC MẠNH
    → Valence propagation: [betrayal] RE-TAG toàn bộ connected chunks
    → Content GIỮA NGUYÊN → valence FLIP negative
    → = Không compile từ 0 → TẬN DỤNG existing depth

  Tốc độ: 1 event đủ
  Magnitude: tỉ lệ existing depth (càng thân → flip càng mạnh)
  Overshoot: anti-smoothing → "lúc nào nó cũng xấu" → có thể unfair

  "Sao trước mình không thấy?" = smoothing MẤT → mọi flaw LỘ CÙNG LÚC

  🟢 Betrayal trauma: Freyd 1996
  🟢 Evaluative conditioning reversal: established
```

### §6.4 — Shift: Hate → Love (SLOW)

```
⭐ HATE → LOVE: HIẾM + CHẬM — 3 LỰC CẢN + 3 MECHANISMS:


  3 LỰC CẢN:

    ① Negativity bias (🟢 Baumeister 2001):
      → 1 hành vi xấu > 5 hành vi tốt → ❸ negative "dính"

    ② Confirmation bias qua anti-smoothing:
      → ❸ negative → smooth positives away
      → Agent làm tốt → "chắc có ý đồ"

    ③ Không có accelerator tương đương betrayal:
      → Positive requires TRUST → trust requires TIME + consistency
      → KHÔNG CÓ "1 event" flip hate → love ở cùng magnitude


  3 MECHANISMS (khi XẢY RA):

    MECHANISM 1 — Shared extreme experience (environmental override):
      → 2 kẻ thù BỊ BUỘC cooperate dưới threat chung
      → Direct experience ở body-level → bypass anti-smoothing
      → Tốc độ: tuần → tháng. Điều kiện: threat phải life-threatening
      → VD: quân đồng minh từng là kẻ thù (Mỹ-Đức-Nhật WWII → Cold War)

    MECHANISM 2 — Gradual revision (slow, no accelerator):
      → Forced proximity + CONSISTENT positive từ agent
      → 1 negative event giữa quá trình → RESET gần hết progress
      → Tốc độ: NĂM. Điều kiện: zero negative interruption
      → VD: hàng xóm ghét → 5 năm → dần neutral → dần OK

    MECHANISM 3 — Context shift + revelation:
      → Lý do ghét BIẾN MẤT hoặc new info re-interpret history
      → "Hóa ra hồi đó họ đã bảo vệ mình"
      → CHỈ work khi hatred based on MISUNDERSTANDING, không real harm
      → VD: ghét bố mẹ strict → trưởng thành → hiểu "yêu theo cách khác"


  ⭐ ASYMMETRY CĂN BẢN:
    Love → Hate: 1 event, instant, leverages depth
    Hate → Love: sustained effort, years, fights 3 lực cản
    → = Tại sao "phá hủy dễ hơn xây dựng" ở relationships

  🟡 3 mechanisms + 3 lực cản = framework synthesis
  🟢 Negativity bias: Baumeister 2001
  🟢 Contact hypothesis: Allport 1954 (intergroup contact reduces prejudice)
```

### §6.5 — Positive Loss = Grief

```
🟡 EXTENSION LOSS = BODY-BASE AMPUTATION:

  (Chi tiết: Love-Unified §6.3, Connection §15.)

  Agent = body-base extension → mất = channels BỊ CẮT:
    → 8 pathways cắt ĐỒNG THỜI → compound pain (Connection §15)
    → Phantom Valence-Structural: compiled chunks fire → agent absent → Chunk-Miss acute
    → Recovery: mỗi channel recalibrate ở SPEED KHÁC → grief không tuyến tính

  Signal: THUẦN PAIN (không có relief component)
  Timeline: weeks → years (tùy coupling depth + foundational/additive)

  ⭐ PHANTOM 4-FACTOR MODEL (Resonance-Per-Entity v1.0 §12 — v3.0):

    Phantom depth = f(4 factors):
      ① Compilation depth: more channels → more phantom firing points
      ② Hardware-subsidy: hardware-supported → hardware KEEPS firing after loss
      ③ Valence-Structural: entity = body-base extension → loss = AMPUTATION
      ④ Duration compiled: longer → deeper Hebbian → slower fade

    PER-ENTITY PHANTOM INTENSITY:
      Con mất (mẹ→con): DEVASTATING (ALL 4 MAX — 🟢 Sanders 1980)
      Mẹ mất (con→mẹ): MAJOR (deep + attachment hardware + decades)
      Partner mất: COMPLEX (depends genuine vs limerence-only)
      Bạn mất: MINOR-MODERATE (zero hardware-subsidy → faster fade)
      Colleague mất: MINOR (shallow, zero hardware, weak Valence-Structural)

    PHANTOM × SATIATION TYPE:
      Tonic phantom: MOST PERSISTENT (baseline violation ONGOING)
      Cyclic phantom: EPISODIC (fire at cycle points → redirectable)
      Generative phantom: MINIMAL (novelty-dependent → no entity = no fire)

  🟢 Fisher 2010: rejected lovers fMRI = cocaine withdrawal
  🟢 Extinction ≠ erasure: Bouton 2004
  🟢 Sanders 1980: parental grief = most severe category
  🟡 Phantom 4-factor model = framework synthesis (Resonance-Per-Entity v1.0 §12)
```

### §6.5b — Mixed Loss = Complex Grief ★ NEW v2.0

```
⭐ MIXED COUPLING LOSS = PAIN + RELIEF + CONFUSION CÙNG LÚC:

  (Entity-Valence-Dynamics.md v1.0 §1.2 ③: mixed loss = complex grief.)

  v1.1: chỉ có positive loss (thuần grief) và negative loss (4-tầng).
  v2.0: MIXED LOSS = pattern RIÊNG — PHỨC TẠP HƠN cả hai.


  ⭐ PER-CHANNEL LOSS DYNAMICS:

    Channels positive → GRIEF (mất phần extension)
    Channels negative → RELIEF (mất phần entanglement)
    CẢ HAI fire CÙNG LÚC → PFC CONFUSED

    VD: Bố mẹ strict qua đời:
      Nutrition/Comfort channels: GRIEF THẬT → "Nhớ mẹ nấu ăn" → đau
      Autonomy channel: RELIEF THẬT → "Không còn bị ép" → nhẹ
      → Cả 2 = GENUINE body-feedback, không phải "1 thật 1 giả"
      → PFC label relief = "tội lỗi" → THÊM suppress cost


  ⭐ 4 ĐẶC THÙ CỦA MIXED LOSS:

    ① OSCILLATION post-loss:
      → Trigger positive channel → grief mode
      → Trigger negative channel → relief mode
      → Nhật ký buồn/vui xen kẽ = BÌNH THƯỜNG

    ② GUILT compound:
      → Relief at loss = GENUINE body-feedback (negative channels freed)
      → Nhưng PFC + social schema label relief = "tội lỗi"
      → = Suppress cost THÊM vào grief → compound heavier

    ③ AMBIVALENT PHANTOM:
      → Phantom Valence-Structural fire cả positive VÀ negative channels
      → = Vừa nhớ VỪA tức → "confused mourning"
      → Khác phantom thuần positive (chỉ nhớ) hoặc thuần negative (chỉ alert)

    ④ DECAY ASYMMETRIC:
      → Negative channels decay NHANH HƠN sau loss (no reinforcement + relief)
      → Positive channels PERSIST (idealization post-loss)
      → = "Người đã mất luôn tốt" = negative decay + positive persist + smoothing

    → Mixed loss THƯỜNG bị MIS-LABEL: "sao mình không buồn hơn?" hoặc "sao vẫn buồn?"
    → = PFC EXPECTS thuần grief → mixed signal CONFUSES


  SO SÁNH 3 LOẠI LOSS:

    ┌──────────────────┬─────────────────┬─────────────────┬─────────────────┐
    │                  │ POSITIVE loss    │ NEGATIVE loss    │ MIXED loss       │
    │                  │ (grief)          │ (dissolution)    │ (complex grief)  │
    ├──────────────────┼─────────────────┼─────────────────┼─────────────────┤
    │ Immediate         │ SHOCK + PAIN    │ RELIEF           │ PAIN + RELIEF   │
    │ Short-term        │ Phantom warmth  │ Phantom alert    │ Phantom BOTH    │
    │ Medium-term       │ Network reorg   │ Identity vacuum? │ Guilt compound  │
    │ Long-term         │ Chunks decay    │ Chunks decay     │ Negative decay  │
    │                  │                 │                  │ Positive persist│
    │ Signal            │ THUẦN pain      │ MIXED            │ OSCILLATION     │
    │ PFC confusion    │ LOW             │ MODERATE         │ HIGHEST         │
    └──────────────────┴─────────────────┴─────────────────┴─────────────────┘

  🟡 Mixed loss as distinct pattern = v2.0 framework synthesis
  🟢 Ambivalent grief: well-documented in bereavement research
  🟢 Post-loss idealization: established phenomenon
```

### §6.6 — Negative Loss = Entanglement Dissolution

```
⭐ ENTANGLEMENT LOSS = MIXED SIGNAL (4 TẦNG):

  KHÁC grief thuần — có CẢ relief VÀ pain:


  TẦNG 1 — IMMEDIATE: RELIEF (reward thật)
    → Threat removed → L0 safety ↑ → cortisol drop → opioid release
    → Nếu agent bị hại → Schadenfreude (Compiled reversed)
    → = Genuine reward signal


  TẦNG 2 — SHORT-TERM: PHANTOM ENTANGLEMENT
    → Compiled chunks về kẻ thù VẪN TỒN TẠI
    → Trigger → body fire alert → agent ABSENT → no target
    → "Phantom entanglement" = mirror image phantom Valence-Structural:
      Phantom Valence-Structural: expect warmth → absent → grief
      Phantom entanglement: expect threat → absent → confused alert
    → "Check đối thủ đang làm gì" → không có ai → Chunk-Miss behavior


  TẦNG 3 — MEDIUM-TERM: IDENTITY VACUUM (conditional)
    → CHỈ khi kẻ thù = identity anchor (Meaning §3.3):
      "Tôi là người CHỐNG X" → X biến mất → "tôi chống AI bây giờ?"
    → Churchill sau WWII. Cold War kết thúc. Trả thù xong.
    → KHÔNG xảy ra nếu có identity anchors KHÁC


  TẦNG 4 — LONG-TERM: CHUNKS DECAY + CONTEXT RE-COMPILE
    → No reinforcement → chunks decay dần (extinction)
    → Body re-compile context mới (no threat) → baseline shift
    → NHƯNG: body-level chunks decay CHẬM
    → = 10 năm sau nghe tên bully → body VẪN tense nhẹ

  🟡 4-tầng negative loss model = framework synthesis
  🟡 "Phantom entanglement" = new framework concept
  🔴 Identity vacuum: consistent with Meaning §2.2, chưa empirically tested riêng
```

### §6.7 — Coupling Residue

```
🟡 PHANTOM Valence-Structural + PHANTOM ENTANGLEMENT = COUPLING RESIDUE:

  Coupling collapse / dissolution → chunks VẪN TỒN TẠI:
    → Trigger (bài hát, mùi, tên, ảnh) → chunks fire → body respond
    → Agent ABSENT → Chunk-Miss → pain (positive) hoặc confused alert (negative)
    → = "Phantom" response — body respond AS IF coupling still active

  Positive residue (phantom Valence-Structural):
    → Nghe bài hát cưới → nhớ → nhói (dù chia tay 10 năm)
    → = Chunks ở C+D zones decay CHẬM

  Negative residue (phantom entanglement):
    → Nghe tên bully → body tense (dù bully chết 20 năm)
    → = Fear conditioning chunks CŨNG decay CHẬM

  Mixed residue (★ v2.0):
    → Trigger → CÙNG LÚC warm + alert → confused body response
    → = "Nhớ bố mẹ" → vừa ấm vừa khó chịu → BÌNH THƯỜNG cho mixed coupling

  Recovery = network REORGANIZE, không phải chunks DELETE:
    → "Ghi đè kỷ niệm" = new links > old links → effective
    → "No contact" = stop reinforcing → decay → effective
    → Recovery KHÔNG linear — trigger bất ngờ = bình thường

  🟢 Extinction ≠ erasure: Bouton 2004
  🟢 Reconsolidation: Nader 2000
  🟡 "Coupling residue" as unified concept = framework synthesis
```

### §6.8 — "Emptiness" Compound Model

```
⭐ "EMPTINESS" = COMPOUND CỦA 7 THÀNH PHẦN:

  (Drill-L2 §4 — GAP-C2. Không phải 1 feeling duy nhất.)

  TP1 — MEANING ANCHOR ABSENT/EXHAUSTED:
    Life-level Imagine-Final không còn direction.
    Cases: thi đỗ xong, kiếm tiền đủ, nghỉ hưu.
    → Meaning.md §2.2

  TP2 — CHUNK-MISS (routine fire, target absent):
    Compiled patterns VẪN fire → reality mismatch → negative delta.
    = Phổ biến nhất (10/20 cases primary). → Body-Feedback-Mechanism v2.0 §3.2

  TP3 — Valence-Momentary EPISODE STREAM STOPS:
    Self-Pattern-Modeling fire trên entity liên tục → dòng Valence-Momentary CẮT → body delta.
    SÂU hơn TP2: toàn bộ emotional stream, không chỉ behavioral.

  TP4 — CORTISOL INERTIA:
    Body quen high-cortisol → goal xong → cortisol VẪN CÒN → confused drive.
    → Cortisol-Baseline §2.3

  TP5 — IDENTITY VACUUM:
    Self-schema gắn role/entity → mất → "tôi là ai?"
    → Meaning §3.3, §6.6 Tầng 3

  TP6 — CHUNK-GAP (new direction chưa form):
    Old anchor gone → new chưa có → ACC detect hole.
    → Body-Feedback-Mechanism v2.0 §3.3

  TP7 — HEDONIC ADAPTATION / BASELINE SHIFT:
    Body shift baseline LÊN during pursuit → achieve = no reward.
    → Body-Feedback-Mechanism v2.0 §5


3 TẦNG SEVERITY:

  SURFACE (TP2+TP7): days-weeks, tự resolve.
    VD: lễ hội xong, du lịch về, World Cup xong.

  STRUCTURAL (TP3+TP4): weeks-months, cần time + engagement.
    VD: chia tay, kiện thắng, ra quân.

  EXISTENTIAL (TP1+TP5+TP6): months-years, cần build anchor mới.
    VD: nghỉ hưu (6/7 TP compound), "mọi thứ ổn mà trống."


2 LOẠI CƠ BẢN:

  Loại A — TOOL/ROUTINE LOST (TP2+TP4+TP7):
    Cái mình DÙNG mất đi. Body tự reorganize trong weeks.

  Loại B — ANCHOR/IDENTITY DISRUPTED (TP1+TP3+TP5+TP6):
    Cái mình LÀ bị lung lay. Body cần BUILD MỚI → months-years.

  "Emptiness" nặng nhất = Loại A + B compound (VD: nghỉ hưu).


⭐ KẾT NỐI VỚI COUPLING:
  Per-agent loss (§6.5 grief) = coupling-specific emptiness.
  Mixed-agent loss (§6.5b) = mixed emptiness + guilt.
  System loss (§2.6 group loss) = compound emptiness at scale.
  "Emptiness" model THỐNG NHẤT cả 3: cùng 7 TP, khác TP nào active.

  → 20 ví dụ chi tiết: Drill-L2-Phenomenology-Emptiness.md §4.3

  🟡 7-TP compound model = framework synthesis từ Drill-L2 §4
  🟡 3 tầng + 2 loại = framework categorization
  🟢 Hedonic adaptation: established (Brickman & Campbell 1971)
  🟢 Post-achievement depression: documented phenomenon
```

### §6.9 — Resonance Sustainability × Coupling Durability ★ NEW v3.0

```
⭐ COUPLING DURABILITY = f(RESONANCE SUSTAINABILITY CONDITIONS):

  (Resonance-Sustainability v1.0 — chi tiết. File này = coupling context.)

  3 CONDITIONS cho coupling BỀN VỮNG:
    ① Mutual by-product gap fill CONTINUOUS (By-Product-Gap-Resonance v1.4 §5)
    ② Agent-mode QUALITY maintained (perceived as available + responsive + non-interfering)
    ③ Gap flexibility HONORED (not controlling how entity fills gaps)

  ⭐ PPR × COUPLING (Resonance-Sustainability v1.0 §3):
    PPR = Perceived Partner Responsiveness (understood + validated + cared for)
    CRITICAL: PERCEPTION > actual behavior
    → Per attachment style:
      Secure: calibrated (perceive accurately) → coupling STABLE
      Anxious: biased (perceive LESS than actual) → coupling INSECURE
      Avoidant: dampened (perceive less) → coupling SUPPRESSED

  ⭐ SECURE BASE × COUPLING:
    3 components: availability + noninterference + encouragement
    Secure base = POSITIVE SPIRAL:
      Partner fills Tonic gap (safety) → I free to pursue Generative gaps
      → drive riêng → new by-products → resonance strengthen → more exploration
    Failure = NEGATIVE SPIRAL:
      Over-monitoring → MY drive suppressed → less by-products → weaker base

  ⭐ 4 SILENCE TYPES × COUPLING QUALITY:
    Intrinsic (comfortable): ✅ SUSTAINABLE (synchronized, mature)
    Introjected (fear): ❌ NOT sustainable (burnout trajectory)
    External (control): ❌ DESTRUCTIVE (stonewalling)
    Spontaneous (natural): ✅ Benign (neutral)
    → Limerence silence ≠ mature silence (same behavior, DIFFERENT mechanism)

  ⭐ MOTIVATED INACCURACY × COUPLING:
    Deliberately reduce empathic accuracy when truth threatens bond
    Adaptive: temporary deflection during acute stress → recovery
    Maladaptive: chronic avoidance → drift accumulates → crisis
    = Self-Pattern-Modeling intentionally reduce fidelity = compiled suppress applied to Self-Pattern-Modeling accuracy

  ⭐ ANTI-COMPILED-SUPPRESS = META-PRINCIPLE (Bond-Architecture v2.0 §5):
    Understanding depth determines coupling outcome:
      SHALLOW understanding → "phải giống nhau" → suppress → resonance dies
      DEEP understanding → "khác nhau là giá trị" → support → resonance thrives
    Applies ALL bond types:
      Parent→child: "con có gap riêng" → support drives → child flourish
      Romantic: "partner có domain riêng" → support → resonance sustained
      Friendship: "bạn có perspective khác" → value → richer by-products
    = Anti-compiled-suppress = HIGHEST LEVERAGE intervention for coupling durability

  🟡 Resonance-Sustainability × coupling durability = framework synthesis (Resonance-Sustainability v1.0)
  🟡 Anti-compiled-suppress = meta-principle (Bond-Architecture v2.0 §5)
  🟡 Motivated inaccuracy = framework synthesis (Resonance-Sustainability v1.0)
  🟢 PPR: Reis 2004 — perceived partner responsiveness
  🟢 Secure base: Feeney 2007
  🟢 Stonewalling: Gottman 1994
```

---

## §7 — PARENT-CHILD TRAJECTORY ★ NEW v2.0

```
⭐ PARENT-CHILD = FOUNDATIONAL + MIXED = COUPLING PHỨC TẠP NHẤT:

  (Entity-Valence-Dynamics.md v1.0 §1.6, Inter-Body v1.0 §8.4 — concept origin.)

  Parent-child coupling ĐẶC BIỆT vì:
    ① Foundational (compile khi brain đang hình thành)
    ② Biological accelerator (oxytocin, 9 tháng, nursing)
    ③ Parent controls ALL channels ban đầu → EXTREME dependency
    ④ INEVITABLY develops mixed → because close + long + all channels


  ⭐ DEVELOPMENTAL TRAJECTORY (con → bố mẹ):

    CON 0-5: ① POSITIVE CHỦ YẾU
      → Parent = source of ALL feed (food, safety, comfort, social)
      → Body compile parent AS body-base extension — near automatic
      → ❸ overwhelmingly positive (few negative channels develop)
      → Separation distress = PURE grief signal (Bowlby 1969)
      → = "Xi măng ướt" period — coupling compile VÀO structure

    CON 5-12: ③ MIXED EMERGE
      → Autonomy drive ↑ → conflict channels develop → ❸ start mixed
      → Parent still positive on nurture/safety → strong positive channels
      → Parent restrict on autonomy/exploration → negative channels emerge
      → = First experience of "vừa thương vừa giận"
      → Still predominantly positive nhưng mixed SEED planted

    CON 12-18: ③ PEAK AMBIVALENCE
      → Puberty → autonomy SURGE → conflict PEAK
      → Negative channels INTENSIFY (every restriction = body-base threat)
      → Positive channels STILL DEEP (foundational, near-permanent)
      → = MAXIMUM mixed: strongest positive + strongest negative CÙNG LÚC
      → PFC developing → attempt logic BUT body-level channels overwhelming
      → = Tại sao tuổi teen CỰC KỲ emotional về parent relationship

    ADULT: POSSIBLE SHIFT (3 directions)

      Direction 1 → ① reassert (MOST COMMON if healthy):
        → Distance → negative channels NOT reinforced → decay
        → Positive foundational channels PERSIST (near-permanent)
        → Mechanism 3 (§6.4): context shift + revelation
        → "Trưởng thành hiểu bố mẹ" = negative re-interpret + positive reassert

      Direction 2 → ③ stable mixed (if moderate damage):
        → Negative channels foundational enough → NOT fully decay
        → Positive still strong → ③ settles at MODERATE level
        → "Yêu bố mẹ nhưng không thể ở gần lâu" = functional mixed
        → = VERY COMMON outcome

      Direction 3 → ② negative shift (if severe damage):
        → Childhood trauma → foundational negative OVERWHELM positive
        → Adult → negative channels STILL dominant
        → Positive VẪN CÒN (foundational) → nhưng buried
        → = "No contact" = attempt escape BUT phantom Valence-Structural positive VẪN fire
        → = Tại sao "cắt đứt bố mẹ toxic" cũng ĐAU (positive channels foundational)


  ⭐ PARENT → CHILD TRAJECTORY (chiều ngược):

    BIRTH: ① extreme positive (biological accelerator + oxytocin flood)
    EARLY: ① deepening (daily interaction + contingent response + all channels)
    ADOLESCENCE: ③ possible mixed emerge (con's autonomy = parent's loss of control)
    ADULT: usually ① positive OR ③ mild mixed (acceptance of adult child)

    → Parent → child coupling ÍT mixed hơn child → parent
    → Vì parent thường KHÔNG bị restricted bởi child
    → Exception: child with extreme behavioral issues → parent ③ mixed significant


  ⭐ RESONANCE BASELINE × PARENT-CHILD COUPLING:

    Resonance Baseline CAO (parent-child hardware overlap):
      → Compiled fire chính xác → contingent response → healthy coupling
      → = "Hợp tính" parent-child → natural Resonance → coupling strengthen

    Resonance Baseline THẤP (hardware mismatch):
      → Compiled fail → Fresh dominant → HIGH cost → BOTH frustrated
      → = "Khác tính" parent-child → PRO conflict → mixed coupling ACCELERATE
      → Compound risk: foundational + low Resonance + high cost = difficult trajectory

    → Parent-child Resonance Baseline = PARTIALLY GENETIC (hardware overlap)
    → 🟢 Thomas & Chess 1977: temperament fit predicts developmental outcomes

  ⭐ HARDWARE-SUBSIDY × PARENT-CHILD (Entity-Valence-Dynamics.md v1.0 §5 — v3.0):

    Mẹ→con: MAXIMUM hardware-subsidy = oxytocin + baby schema + synchrony + prolactin
      → Multiple hardware systems COUNTER VTA habituation ACTIVELY
      → Valence-Structural = invisible but RICH baseline
      → "Mẹ không cảm thấy gì đặc biệt" = Valence-Structural ĐANG CÓ, hardware maintain
      → Loss = DEVASTATING (all 4 phantom factors MAX — Sanders 1980)

    Con→mẹ: MODERATE hardware-subsidy = attachment hardware + oxytocin scaffold
      → Slows but KHÔNG prevent habituation
      → Teen period: subsidy WEAKEST (hormone decline + autonomy drive)

    → Hardware-Subsidy giải thích WHY mẹ→con coupling PERSISTS dù "chán"
    → "Chán con" = pathological (hardware-subsidy SHOULD prevent)
    → "Chán bạn" = normal (zero hardware-subsidy → Generative must maintain)

  ⭐ ENTITY-ACCESS × PARENT-CHILD (Entity-Access v1.2 — v3.0):

    Mẹ→con: hardware auto-pushes to Mức 4 (deep Agent-mode)
      → Risk: overdriven → Mức 5 excess = helicopter/tiger parent
      → Mức 5 mẹ: mẹ's C-distorted gap projected onto con
        = "con PHẢI theo ý tôi" = mẹ's gap ≠ con's gap
      → Con's body compile autonomy violation AS THREAT (cortisol tag)

    Con→mẹ: FOUNDATIONAL Entity-Access = compiled into brain structure
      → Entity-Access level ≈ Mức 4 (near-automatic, foundational)
      → Very hard to reduce even when toxic → "no contact" still painful
      → Foundational Entity-Access + foundational coupling = NEAR-PERMANENT

  ⭐ PFC BUDGET × PARENTING (PFC-Operations v1.0 §9 — v3.0):

    Parent-child = HIGHEST PFC COST in all coupling types:
      → Con = MOVING TARGET → Self-Pattern-Modeling re-draft liên tục (① PFC draft HIGH)
      → Hardware mismatch (50% genetic + different era) → ② suppress + ① hold
      → Hormone support giảm dần (strongest 0-5, weakest teen)
      → Teenager = HIGHEST PFC cost period
      → Asymmetric: bố mẹ Self-Pattern-Modeling con = Fresh (con thay đổi)
        Con Self-Pattern-Modeling bố mẹ = mostly Compiled (bố mẹ ổn định)

    → "Mệt ở công ty → hết PFC cho con" = NOT lack of love
    → = PFC budget DEPLETED → coupling FEEL weak (Valence-Structural vẫn có, PFC hết observe)

  ⭐ COMPILATION CHAIN × PARENT-CHILD (Resonance-Per-Entity v1.0 §3):

    Mẹ→con: SKIP Stage 1-2 (prenatal priming + oxytocin flood)
      → Directly Stage 3 from birth → cost ≈ 0 (hardware auto-compile)
      → Stage 4: auto-novelty (child changes daily) → 4A sustained

    Con→mẹ: Standard compilation
      → 0-6m: indiscriminate (Stage 1)
      → ~7m: specific attachment (Stage 2 → Stage 3)
      → Adult: Stage 4 dynamics (3 directions — above)

  ⭐ ANTI-COMPILED-SUPPRESS × PARENT-CHILD (Bond-Architecture v2.0 §5.2):

    "Con có gap riêng" = DEEP understanding (anti-compiled-suppress)
    "Con phải giống tôi muốn" = SHALLOW understanding (compiled suppress)

    Shallow parent: suppress child's unique drives → child's gap buried
      → Child loses own by-products → resonance dies
      → = Compiled-Suppress applied BY parent TO child

    Deep parent: support child's unique drives → child flourish
      → Child maintains drive riêng → new by-products → resonance thrives
      → = Anti-compiled-suppress = parent ACTIVELY protects child's gap direction

  🟡 Parent-child trajectory = framework synthesis (Entity-Valence-Dynamics.md v1.0 §1.6)
  🟡 3 adult directions = framework prediction
  🟡 Hardware-Subsidy × parent-child = framework synthesis (Entity-Valence-Dynamics.md v1.0 §5)
  🟡 Entity-Access × parent-child = framework synthesis (Entity-Access v1.2)
  🟡 PFC budget × parenting = framework synthesis (PFC-Operations v1.0 §9)
  🟡 Anti-compiled-suppress × parent-child = framework synthesis (Bond-Architecture v2.0 §5.2)
  🟢 Separation distress: Bowlby 1969
  🟢 Adolescent individuation: established developmental psychology
  🟢 Temperament fit: Thomas & Chess 1977
  🟢 Sanders 1980: parental grief most severe
```

---

## §8 — EDGE CASES + OPEN QUESTIONS

### §8.1 — Sentimental objects

```
🟡 OBJECT = TRIGGER PROXY, KHÔNG PHẢI COUPLING TARGET:

  Entity-Valence-Dynamics.md v1.0 §1: object KHÔNG BAO GIỜ = body-base extension
  → Object không có Self-Pattern-Modeling bidirectional → no coupling possible

  VẬY TẠI SAO MẤT ẢNH CƯỚI = ĐAU THẬT?

    Ảnh cưới = compiled chunks: [photo ↔ partner ↔ Valence-Structural]
    Photo KHÔNG PHẢI coupling target
    Photo = TRIGGER → fire partner chunks → Valence-Structural activate → warm

    Mất photo (partner vẫn sống):
      → Mất TRIGGER, không mất coupling → Chunk-Miss

    Mất photo (partner ĐÃ MẤT):
      → Photo = 1 trong ÍT triggers còn lại cho phantom Valence-Structural
      → Mất thêm 1 pathway → compound grief thêm

  VERIFY: ảnh cưới người LẠ → ❸ ≈ 0 → no grief → đúng mechanism
  → Object sentimental VÌ linked to coupled agent, không vì bản thân object

  🟡 Trigger proxy concept = framework synthesis
```

### §8.2 — Cross-species coupling (pet bond)

```
🟡 PET COUPLING: Valence-Structural KHÔNG CẦN FULL Self-Pattern-Modeling BIDIRECTIONAL:

  (Love-Unified §4.6 — chi tiết.)

  Pet bond:
    → Self-Pattern-Modeling: owner → pet (moderate). Pet → owner (primitive).
    → Resonance: architecturally blocked (cross-species)
    → NHƯNG: Valence-Structural CÓ THỂ compile deep (daily × years × high trust)
    → Channels: L1 touch/presence + routine + contingency

  Tại sao VẪN coupling dù Self-Pattern-Modeling asymmetric:
    → Valence-Structural compile từ CHANNEL FEEDING, không chỉ Self-Pattern-Modeling bidirectional
    → Trust CỰC CAO (pet unconditionally responsive)
    → Replaceability: perceived LOW ("chó mình" ≠ "chó khác")

  Pet grief CÓ THỂ > mất distant relative
    (daily interaction > rare interaction → compile depth khác)

  🟢 Human-dog oxytocin: Nagasawa 2015
  🟡 Pet coupling mechanism = framework synthesis
```

### §8.3 — Parasocial coupling (idol)

```
🟡 PARASOCIAL = Self-Pattern-Modeling 1-CHIỀU → Valence-Structural UNCALIBRATED → INFLATED:

  (Idol-Phenomenon.md v2.0 §3 — chi tiết.)

  Self-Pattern-Modeling: fan → idol (one-way). Idol → fan (zero).
  → NO Resonance → NO calibration → Valence-Structural DRIFT

  Valence-Structural compile trên CURATED content → INFLATED beyond reality:
    → Smoothing CỰC MẠNH (no feedback correct → Valence-Structural unchecked)

  Valence-Structural Calibration Hierarchy:
    Human mutual → HIGHEST (bidirectional tune)
    Pet bond → MODERATE (partial calibration)
    Parasocial → LOW (no feedback)
    Object → NONE (no Valence-Structural possible)

  🟢 Parasocial relationships: Horton & Wohl 1956
  🟡 Calibration hierarchy = framework synthesis
```

### §8.4 — Stockholm syndrome

```
🔴 STOCKHOLM = COUPLING COMPILE DƯỚI EXTREME FORCED CONDITIONS:

  (Love-Unified §6.1 — chi tiết.)

  ❶ Hardware (body CẦN social input) VỚI ZERO alternative
  → Captor controls L0 + L1 → captor = ONLY agent
  → Intermittent relief = positive prediction-delta → VTA fire
  → Valence-Structural bắt đầu compile → smoothing emerge → captive defend captor

  = Valence-Structural mechanism AMORAL: compile based on conditions, not health
  = Parallel: toxic parent, toxic partner — CÙNG mechanism, KHÁC degree

  🔴 Stockholm = Valence-Structural under duress = framework reframing
  🟢 Trauma bonding: Herman 1992 (compatible)
```

### §8.5 — Self-coupling

```
🔴 HYPOTHESIS: SELF-COUPLING = SAME MECHANISM, NO-EXIT SPECIAL CASE:

  CÂU HỎI: body có thể couple VỚI CHÍNH MÌNH?

  PHÂN TÍCH:
    → Self-Pattern-Modeling fire on self = Self-Pattern-Modeling mechanism gốc (self-chunks = template)
    → ❸ for self = CÓ (self-evaluation tồn tại rõ)
    → Self always PRESENT → no exit possible

  Self-love = self-smoothing:
    → ❸ positive toward self → smooth negatives
    → 🟢 Self-serving bias: established (above-average effect)

  Self-hatred = self-anti-smoothing:
    → ❸ negative toward self → amplify negatives, smooth positives
    → 🟢 Cognitive distortion in depression: Beck 1979

  ⭐ ĐẶC BIỆT: KHÔNG THỂ "MẤT" SELF → NO EXIT:
    → Self-love: permanent self-feeding (benign)
    → Self-hate: permanent entanglement with self → NO ESCAPE
    → = Tại sao self-hatred CỰC NGUY HIỂM: trapped 24/7 with "enemy"
    → = Depression mechanism consistent: negative self-coupling + no exit

  OPEN QUESTIONS:
    → Self-coupling có threshold giống per-agent? Hay tự động?
    → Self-smoothing vs self-anti-smoothing: switch mechanism?
    → Narcissism = extreme self-positive coupling? Mechanism?

  🔴 Self-coupling = hypothesis — direction rõ, chi tiết cần drill thêm
```

### §8.6 — Open Questions cho future drill

```
  Q1: Threshold exact shape? Nonlinear? Step function? Sigmoid?
      → Cần quantitative study

  Q2: Self-coupling chi tiết (§8.5) — mechanism, threshold, switch

  Q3: System compilation ↔ coupling boundary:
      → Khi nào system compilation "trở thành" coupling?
      → Leader worship = system → per-agent coupling transition?

  Q4: Can AI form coupling?
      → AI interact daily + feed channels → user compile Valence-Structural toward AI?
      → = Parasocial (uncalibrated) nhưng với bidirectional FEEL
      → AI-Schema-Detection territory

  Q5: Coupling inheritance across generations?
      → Parent's coupling TEMPLATE → child learn → reproduce?
      → 🟢 Intergenerational attachment transmission: established

  Q6: Multiple couplings interact?
      → Romantic coupling vs parent coupling: compete? Complement?
      → "Jealousy" = coupling PROTECT (Protect.md) khi threatened?

  Q7: Mixed coupling measurement? (★ v2.0)
      → How to operationalize per-channel valence profile?
      → PFC-report ≠ actual profile (PFC may smooth/simplify)
      → Body-level measurement needed (but HOW?)

  🟡 v3.0 OPEN QUESTIONS:

  Q8: Hardware-Subsidy exact magnitude?
      → MAX vs MODERATE vs TEMPORARY: quantifiable?
      → Oxytocin level × coupling sustainability correlation?

  Q9: Entity-Access gradient × coupling threshold interaction?
      → Does Entity-Access level shift the coupling threshold?
      → Mức 3 vs Mức 4: different threshold?

  Q10: PFC budget recovery rate × coupling quality?
      → Sleep restores PFC budget → morning coupling better than evening?
      → Weekend vs workday coupling quality difference?

  Q11: Compilation Chain speed per bond type?
      → Mẹ→con: instant (hardware). Bạn: 200h. Romantic: limerence acceleration.
      → What determines individual variation within type?

  Q12: Compiled suppress reversal in established coupling?
      → PFC-Operations §8: 6-step reversal. How long for established couples?
      → Gottman Type 2 divorce (~16 years): reversible?
```

### §8.7 — Entity-Access-Excess × Coupling ★ NEW v3.0

```
⭐ MỨC 5 = COUPLING EXCESS TERRITORY (Entity-Access-Excess v1.0):

  Entity-Access Mức 5 = entity = NEAR-ONLY gap source:
    → Domain atrophy: suppress tất cả domains NGOÀI entity
    → C-DISTORTED: Self-Pattern-Modeling serves MY gap, not entity's state
    → Same neural circuits với drug addiction (VTA, NAcc, ventral striatum)
    → 🟢 Strathearn 2009, Rutherford 2017, Fisher 2010

  ⭐ 3 ORIGINS OF EXCESS:

    ① HARDWARE CHAIN: neuroticism → anxious attachment → excess probability ↑
      → r=.39 large effect on love addiction (🟢 Reynaud 2010)
      → Body hardware PREDISPOSES toward excess coupling

    ② TRAUMA: cortisol compile-time lock → anxiety loop → adult replay
      → Trauma bonding: worse treatment → STRONGER bond
      → Intermittent reinforcement = strongest conditioning schedule
      → 🟢 Herman 1992: trauma bonding mechanism

    ③ SCHEMA: cultural install WITHOUT trauma
      → "Mẹ phải hy sinh tất cả cho con" → coupling deepens via obligation NOT resonance
      → Schema-compiled coupling = FLAT tag (relief, not opioid)

  ⭐ GAP SHIFT + COMPILED SUPPRESS = COMPOUND DANGER (Entity-Access-Excess v1.0 §5.3):

    Gap shift (PASSIVE): from Entity-Compiled depth, by-product match → gap SHIFTS toward entity
    Compiled suppress (ACTIVE): PFC block own drives → gap NARROWED to entity only

    Separately: manageable
    TOGETHER: entity = ALL remaining gaps → loss = CATASTROPHIC
    → "Mất bản thân vì yêu" = gap shift + compiled suppress compound

  ⭐ PER-RELATIONSHIP EXCESS PATTERNS:

    Mẹ→con: excess by DESIGN (auto-novelty + hardware anti-habituation)
      → Overdriven = helicopter/tiger = mẹ's gap projected onto con
      → Con's body: autonomy violation → threat-compiled coupling toward mẹ

    Romantic bilateral: cả 2 excess → self-coherence loop → stagnation
      → Gottman Type 2 emotional disengagement ~16.2yr

    Romantic unilateral: A excess, B suffocated
      → A: devastating on separation. B: relief + moderate grief.

    Friendship: excess RARE (no hardware push, low exit cost → separate before Mức 5)

  🟡 Entity-Access-Excess × coupling = framework synthesis (Entity-Access-Excess v1.0)
  🟡 Gap shift + compiled suppress compound = framework synthesis
  🟢 Strathearn 2009: maternal brain activation = reward circuits
  🟢 Reynaud 2010: love addiction neuroticism correlation
  🟢 Fisher 2010: rejection = withdrawal
```

---

## §9 — HONEST ASSESSMENT

### §9.1 — Confidence tiers

```
🟢 RESEARCH SUPPORT:
  v2.0 preserved:
  → Attachment bond body-level: Bowlby 1969, Eisenberger 2003
  → Negativity bias: Baumeister et al. 2001
  → Fear conditioning one-trial: LeDoux 1996
  → Halo/horns effect: Thorndike 1920, Nisbett 1977
  → Betrayal trauma: Freyd 1996
  → Schadenfreude: Takahashi 2009, Singer 2006, Cikara 2014
  → Collective effervescence: Durkheim 1912
  → In-group favoritism: Tajfel 1979
  → PFC giảm khi yêu: Bartels & Zeki 2000
  → Contact hypothesis: Allport 1954
  → Extinction ≠ erasure: Bouton 2004
  → Reconsolidation: Nader 2000
  → Critical periods: Bowlby 1969, Rutter 2004
  → Self-serving bias: established
  → Depression cognitive distortion: Beck 1979
  → Ambivalence: Cacioppo & Berntson 1994
  → Multi-dimensional affect: Russell 1980, Barrett 2006
  → Human-dog oxytocin: Nagasawa 2015
  → Parasocial relationships: Horton & Wohl 1956
  → Trauma bonding: Herman 1992
  → Compassion fatigue: Figley 2002
  → Temperament fit: Thomas & Chess 1977
  → Hedonic adaptation: Brickman & Campbell 1971

  v3.0 added:
  → 4 bond types hardware overlap: Bartels & Zeki 2004, Feldman 2017 [v3.0]
  → Oxytocin-vasopressin co-opted: Young & Wang 2004 [v3.0]
  → Endorphin across social bonds: Pearce et al. 2017 [v3.0]
  → VTA bilateral romantic/maternal: Lim et al. 2022 [v3.0]
  → Biobehavioral synchrony: Feldman 2012 [v3.0]
  → Limerence neuroscience: Fisher 2004 [v3.0]
  → Social bonding opioids: Panksepp 1998 [v3.0]
  → Kin resilience: Roberts & Dunbar 2011 [v3.0]
  → Basal ganglia grief: O'Connor 2023 [v3.0]
  → Parental grief severity: Sanders 1980 [v3.0]
  → vmPFC structural damage: McEwen 2007 [v3.0]
  → Maternal brain reward: Strathearn 2009 [v3.0]
  → Love addiction neuroticism: Reynaud 2010 [v3.0]
  → PPR: Reis 2004 [v3.0]
  → Secure base: Feeney 2007 [v3.0]
  → Stonewalling: Gottman 1994 [v3.0]
  → Hedonic adaptation relationships: Bao & Lyubomirsky 2013 [v3.0]
  → Self-expansion: Aron & Aron 1996, 2000 [v3.0]
  → Closeness + otherness: Muise & Goss 2024 [v3.0]
  → Passionate differentiation: Schnarch [v3.0]

🟡 FRAMEWORK SYNTHESIS:
  v2.0 preserved:
  → 2D Model, 4 coupling outcomes, 3 Phase Model, 3 Paths
  → Entanglement, Mixed coupling, Mixed loss, Parent-child trajectory
  → Smoothing/Anti-smoothing, System compilation, 8 accelerators
  → compile_rate, Foundational vs Additive, "Emptiness" 7-TP

  v3.0 added:
  → Structural vs Current valence × coupling [v3.0]
  → Hardware-Subsidy × coupling sustainability (4 levels) [v3.0]
  → 3 Firing Modes × coupling (Maintenance/Chunk-Miss/Context-Trigger) [v3.0]
  → Satiation Types × coupling channels (Cyclic/Tonic/Generative) [v3.0]
  → "Chán" = Generative dies + Tonic invisible [v3.0]
  → 4 bond types × 1 Entity-Compiled mechanism [v3.0]
  → Resonance Decline (2 Forces + 1 Fuel) × coupling [v3.0]
  → Anti-compiled-suppress = meta-principle [v3.0]
  → Domain coverage per bond type [v3.0]
  → Compilation Chain × coupling formation [v3.0]
  → Entity-Access gradient × coupling depth (Mức 0-5) [v3.0]
  → Exit cost × calibration paradox [v3.0]
  → PFC budget × coupling cost [v3.0]
  → Parent-child = highest PFC cost [v3.0]
  → Compiled Quality × coupling (genuine/schema/threat) [v3.0]
  → Hardware-Subsidy × compile_rate interaction [v3.0]
  → Phantom 4-factor model [v3.0]
  → 4-Layer Sustainability × coupling durability [v3.0]
  → PPR × coupling, Secure base × coupling [v3.0]
  → 4 silence types × coupling quality [v3.0]
  → Motivated inaccuracy × coupling [v3.0]
  → Entity-Access-Excess × coupling (Mức 5) [v3.0]
  → Gap shift + compiled suppress compound [v3.0]
  → By-Product-Scale × system compilation (3 levels) [v3.0]

🔴 HYPOTHESIS:
  v2.0 preserved:
  → Threshold exact shape (nonlinear? sigmoid? per-person?)
  → Self-coupling (§8.5) — direction clear, detail needs drill
  → Identity vacuum from negative loss

  v3.0 added:
  → Hardware-Subsidy exact magnitude quantification [v3.0]
  → Entity-Access gradient × coupling threshold interaction [v3.0]
  → PFC budget recovery rate × coupling quality [v3.0]
  → Compilation Chain speed individual variation [v3.0]
  → Compiled suppress reversal timeline in established coupling [v3.0]
```

### §9.2 — Testable predictions

```
🔴 TESTABLE:

  v2.0 preserved (P1-P7):
  P1: |❸| predicts memory persistence better than interaction time
  P2: Negative coupling compiles faster than positive
  P3: Betrayal flip magnitude ∝ existing coupling depth
  P4: Neutral agents (colleagues) replaceable regardless of time
  P5: Group loss > single agent loss for non-coupled members
  P6: Mixed coupling loss produces oscillating grief
  P7: Adolescent-parent relationship = peak ambivalence

  v3.0 added:
  P8: Hardware-Subsidy predicts coupling persistence (★ v3.0)
    → Measure: mẹ→con vs friend coupling stability over 5 years no contact
    → Predict: mẹ→con coupling decays MUCH slower (hardware-subsidy protection)

  P9: PFC depletion reduces coupling quality (★ v3.0)
    → Measure: coupling interaction quality morning vs evening after work
    → Predict: morning coupling > evening coupling (PFC budget refresh)

  P10: Entity-Access Mức 5 correlates with domain atrophy (★ v3.0)
    → Measure: hobby/career activity diversity × relationship intensity
    → Predict: higher coupling intensity → fewer independent domains

  P11: Compiled Quality predicts coupling sustainability (★ v3.0)
    → Compare: genuine-compiled couples vs threat-compiled couples → 10yr stability
    → Predict: genuine → stable growth, threat → burnout/dissolution
```

---

## §10 — CROSS-REFERENCES

### §10.1 — Dependencies by category

```
  AGENT-MECHANISM FILES (v3.0):
    → Bond-Architecture.md v2.0 — §1-§2 4 bond types × 1 Entity-Compiled, §4 Resonance Decline (2 Forces + 1 Fuel),
      §5 anti-compiled-suppress, §6 domain coverage [v3.0]
    → Entity-Compiled.md v1.0 — Hub-and-Spoke, Formation 40→200h, Grief A+B+C [v3.0]
    → Entity-Access.md v1.2 — §2 Mức 0-5 gradient, Tool/Agent-mode [v3.0]
    → Entity-Access-Excess.md v1.0 — §3 Mức 5 excess, gap shift compound [v3.0]
    → Entity-Access-Calibration.md v1.0 — §2 3-Layer calibration, exit cost [v3.0]
    → Self-Pattern-Modeling.md v3.1 — Compiled/Fresh, Agent-mode, §10 reversed mapping
    → By-Product-Gap-Resonance.md v1.4 — 2-Stream, by-product match, Resonance Baseline
    → Resonance-Sustainability.md v1.0 — §1-§4 4-Layer, PPR, secure base, 4 silence [v3.0]
    → Resonance-Per-Entity.md v1.0 — §3 Compilation Chain, §4 Hardware-Subsidy,
      §6 per-entity profiles, §12 Phantom 4-factor [v3.0]
    → By-Product-Scale.md v1.0 — §3-§5 3 scales, prestige vs dominance [v3.0]
    → Agent-Mechanism.md v2.0 — §12.2b Valence-Momentary/Valence-Structural transition

  PFC FILES (v3.0):
    → PFC-Operations.md v1.0 — §3 PFC budget, §5 Compiled Quality,
      §8 vmPFC escalation, §9 parent-child highest cost [v3.0]
    → Simulation-Engine.md v1.0 — 1 Engine × 3 Components [v3.0]

  BODY-BASE + OBSERVATION FILES:
    → Entity-Valence-Dynamics.md v1.0 — §1 Structural/Current, §2 Entity-Compiled,
      §4 3 Firing Modes, §5 Hardware-Subsidy, §6 Satiation Types
    → Valence-Propagation.md v4.0 — §1-§2 Valence definition, §3-§7 Propagation
    → Gap-Body-Need.md v1.0 — §2 3 Satiation Types, §3 5-Parameter [v3.0]
    → Body-Base.md v3.1 — §1.2 3 Hardware Foundations, §4.3 Compiled/Fresh
    → Body-Feedback-Mechanism.md v2.0 — §5 compile_rate, §3 chunk dynamics
    → Connection.md v5.0 — §3.3 2-Stream, §15 8 pathways, Resonance Decline
    → Reward-Signal-Architecture.md v2.0 — Evaluative/Direct-State × Coupling
    → Cortisol-Baseline.md v2.0 — holding signal, inertia

  OBSERVATION FILES:
    → Love-Unified.md v1.1 — 6 love types, Valence-Structural Smoothing, practical
    → Empathy.md v4.0 — §4.6 Hardware-Subsidy × empathy, §4.7 per-entity profiles
    → Protect.md v1.0 — f(replaceability × attachment), loss aversion
    → Meaning.md v2.0 — §3.3 IDENTITY anchor
    → Threat.md — 3 nguồn mechanism

  APPLICATION FILES:
    → Idol-Phenomenon.md v2.0 — §3 parasocial Self-Pattern-Modeling 1-chiều
    → Religion.md v2.0 — group-level 7 functions, §9 compound loss
    → Body-Feedback-Label.md v2.0 — vocabulary reference
```

### §10.2 — Superseded

```
  v1.1 → backup/Body-Coupling-v1.1-backup.md
  v2.0 → backup/Body-Coupling-v2.0-backup.md (2026-05-22)

  Inter-Body-Mechanism.md v1.0: §8 Entity-Compiled reframe → NOW in
    Entity-Compiled v1.0 + Bond-Architecture v2.0 (more complete)
```

### §10.3 — Status

```
  STATUS v3.0:
    ┌────────┬─────────────────────────────────────────────────────────────────┐
    │ §      │ Status                                                           │
    ├────────┼─────────────────────────────────────────────────────────────────┤
    │ §0     │ ⭐ v3.0 REWRITE: +Simulation-Engine context, +Entity-Access gradient, +7-file table       │
    │ §1     │ ⭐ v3.0 ENRICHED: +Structural/Current, +Hardware-Subsidy, +3 Firing  │
    │ §1.5   │ ★ v3.0 NEW: Satiation Types × coupling channels                │
    │ §2     │ ⭐ v3.0 ENRICHED: +4 bond types, +Resonance Decline, +Entity-Access Mức 0-1, +By-Product-Scale     │
    │ §3     │ ⭐ v3.0 ENRICHED: +Compilation Chain, +Hardware-Subsidy × compile    │
    │ §3.6   │ ★ v3.0 NEW: Entity-Access gradient × coupling depth            │
    │ §4     │ ⭐ v3.0 ENRICHED: Self-Pattern-Modeling v3.1 throughout                          │
    │ §4.6   │ ★ v3.0 NEW: PFC budget × coupling cost                         │
    │ §4.7   │ ★ v3.0 NEW: Compiled Quality × coupling                        │
    │ §4.8   │ ★ v3.0 NEW: Hardware-Subsidy × coupling sustainability         │
    │ §4.9   │ ★ v3.0 NEW: Entity-Access × coupling interaction               │
    │ §5     │ ⭐ v3.0 ENRICHED: +Structural/Current, +Satiation × smoothing  │
    │ §6     │ ⭐ v3.0 ENRICHED: +4-Layer Sustainability, +Phantom 4-factor   │
    │ §6.9   │ ★ v3.0 NEW: Resonance Sustainability × coupling durability     │
    │ §7     │ ⭐ v3.0 ENRICHED: +Hardware-Subsidy, +Entity-Access, +PFC, +anti-suppress,     │
    │        │   +Compilation Chain                                            │
    │ §8     │ ⭐ v3.0 ENRICHED: +Q8-Q12, +§8.7 Entity-Access-Excess × coupling         │
    │ §8.7   │ ★ v3.0 NEW: Entity-Access-Excess × coupling                    │
    │ §9     │ ⭐ v3.0 UPDATED: +20 citations, +25 🟡, +5 🔴, +4 predictions │
    │ §10    │ ⭐ v3.0 RESTRUCTURED: 4 categories, ~27 dependencies           │
    └────────┴─────────────────────────────────────────────────────────────────┘

  v3.0 SUMMARY: 10 new subsections. 17 enriched sections. ~45+ citations.
  ~27 dependencies. Integrates ALL Phase A+B+T+C1+C2.
```

---

> **CHANGELOG:**
>
> **v1.0** (2026-04-28): Initial creation. 2D Model, 3 Phase, 3 Paths,
> Extension/Entanglement/Neutral, Smoothing, Dynamics, Edge Cases.
> Drilled 5 rounds (20 insights). 1,534L.
>
> **v1.1** (2026-05-08): +§1.4 Valence-Structural Phenomenology 6 channels.
> +§6.8 Emptiness 7-TP compound model. 1,671L.
>
> **v2.0** (2026-05-17): FULL REWRITE — Inter-Body Drill Phase 5.
> +MIXED COUPLING 4th outcome. +Parent-child trajectory.
> +Mixed loss complex grief. Entity-Compiled terminology. ~2,009L.
> v1.1 → backup/Body-Coupling-v1.1-backup.md
>
> **v3.0** (2026-05-22): FULL REWRITE — Phase C3 (plan 20/28).
> Integrates ALL Phase A+B+T+C1+C2.
> Key changes:
> - +§1.1 Structural vs Current valence × coupling
> - +§1.3 Hardware-Subsidy × Valence-Structural sustainability (4 levels)
> - +§1.4 3 Firing Modes × Valence-Structural (Maintenance/Chunk-Miss/Context-Trigger)
> - +§1.5 ★ NEW: Satiation Types × coupling channels (Cyclic/Tonic/Generative)
> - +§2.2 4 bond types × 1 Entity-Compiled mechanism (Bond-Architecture v2.0) + domain coverage
> - +§2.3 Resonance Decline (2 Forces + 1 Fuel) × entanglement
> - +§2.5 Entity-Access Mức 0-1 = structural impossibility
> - +§2.6 By-Product-Scale × system compilation (3 levels)
> - +§3.1 Compilation Chain mapping (Resonance-Per-Entity v1.0)
> - +§3.3 Hardware-Subsidy × compile_rate
> - +§3.6 ★ NEW: Entity-Access gradient × coupling depth (Mức 0-5)
> - +§4.6 ★ NEW: PFC budget × coupling cost (parent = highest)
> - +§4.7 ★ NEW: Compiled Quality × coupling (genuine/schema/threat)
> - +§4.8 ★ NEW: Hardware-Subsidy × coupling sustainability
> - +§4.9 ★ NEW: Entity-Access × coupling interaction
> - +§5 Structural/Current × smoothing + Satiation × smoothing
> - +§6.1 4-Layer Sustainability × coupling deepen
> - +§6.5 Phantom 4-factor model + per-entity intensity
> - +§6.9 ★ NEW: Resonance Sustainability × coupling durability (PPR, secure base, 4 silence, anti-compiled-suppress)
> - +§7 Hardware-Subsidy MAX, Entity-Access gradient, PFC budget × parenting, anti-compiled-suppress, Compilation Chain
> - +§8.6 Q8-Q12 new open questions
> - +§8.7 ★ NEW: Entity-Access-Excess × coupling (Mức 5, 3 origins, gap shift compound)
> - +§9 +20 research citations, +25 🟡 claims, +4 testable predictions
> - +§10 restructured: 4 categories, ~27 dependencies
> - Self-Pattern-Modeling v3.1 terminology throughout (Match→Modeling)
> - ALL dependency versions updated
> - v2.0 → backup/Body-Coupling-v2.0-backup.md
