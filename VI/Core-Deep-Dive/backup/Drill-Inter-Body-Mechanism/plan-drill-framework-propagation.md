# Plan: Drill → Framework Propagation — TOÀN DIỆN

> **Ngày tạo:** 2026-05-22
> **Trạng thái:** ✅✅ COMPLETE — 28/28 done (Phase A+B+T+C+D ALL COMPLETE)
> **Supersedes:** plan-drill-propagation.md (chỉ cover 4 file gốc, outdated)
> **Source:** 18 drill files, ~238 insights, ~50 open gaps (research-only)
> **Scope:** 4 NEW + 5 REWRITE + 8 TÁCH/MỚI + 6 REWRITE + 3 REFINE + 2 RENAME/VERIFY = 28 sessions
> **Nguyên tắc:** Chậm mà chắc. Mỗi session = 1 file. Chất lượng > tốc độ.
> **Reference:** Drill-Over-SPM-Clarification.md §9 = BIAS PREVENTION guide

---

## §0 — DEPENDENCY MAP

```
PHASE A: NEW FILES (foundation — mọi thứ khác depend vào đây)
═══════════════════════════════════════════════════════════════

  A1. PFC-Operations ──────┬──→ B2 (SPM), B4 (Boredom), C7 (GDP)
                           │
  A2. Simulation-Engine ───┼──→ B1 (Imagine-Final), B2 (SPM), A4 (Entity-Access)
                           │
  A3. Entity-Compiled ─────┼──→ A4 (Entity-Access), B5 (VP)
                           │
  A4. Entity-Access ───────┴──→ B5 (VP), C1-C5, C8


PHASE B: REWRITES (depend Phase A)
═══════════════════════════════════════════════════════════════

  B1. Imagine-Final ←── A2
  B2. SPM v3.1 ←── A1, A2
  B3. BPGR v1.1 ←── B2
  B4. Boredom v2.0 ←── A1
  B5. VP v3.0 ←── A3, A4


PHASE T: TÁCH + MỚI (depend Phase A + B, TRƯỚC Phase C)
═══════════════════════════════════════════════════════════════

  T0. PFC-Label [MỚI] ←── A1, A2 (vocabulary standard, companion BFL)
  T1. EA-Excess [TÁCH] ←── A4 (EA core)
  T2. EA-Calibration [TÁCH] ←── A4, T1
  T3. Bond-Architecture [TÁCH] ✅ ←── B3 (BPGR core)
  T4. Resonance-Sustainability [TÁCH] ✅ ←── B3, T3
  T5. By-Product-Scale [TÁCH] ←── B3
  T6. Gap-Body-Need [MỚI] ←── A4, B5
  T7. Resonance-Per-Entity [MỚI] ←── B3, B5, T3, T4


PHASE C: REWRITE C1-C6 + REFINE C7-C9 (depend Phase A + B + T)
═══════════════════════════════════════════════════════════════

  C1. Connection [REWRITE] ←── ALL Phase A+B+T
  C2. Empathy [REWRITE] ←── B2, B5, A4, T2, T4, T7
  C3. Body-Coupling [REWRITE] ←── A4, B5, T1, T3, T7
  C4. Love-Romantic [REWRITE] ←── A4, B3, B5, T1-T5, T7
  C5. Love-Unified [REWRITE] ←── A4, B5, T3-T5, T7
  C6. Background-Pattern [REWRITE] ←── B2, B5, T2
  C7. Gap-Dist-Profile [DEEP REF] ←── A1, T6
  C8. Agent-Mechanism [REFINE] ←── All Phase A + T
  C9. Coordination-Node + Collective-Body [LIGHT REF] ←── T5


PHASE D: RENAME + VERIFY (sau tất cả)
═══════════════════════════════════════════════════════════════

  D1. SPM Rename (~70 files)
  D2. File-Index + PFC-Hold-Dimensions + Verification
```

---

## §1 — PHASE A: NEW FILES (4 sessions)

> Foundation — mọi file khác sẽ reference đến đây.
> Distill từ drill, KHÔNG copy-paste. Chất lượng framework-level.

---

### A1. PFC-Operations.md [NEW]

```
VỊ TRÍ:   Core-Deep-Dive/PFC/
SOURCE:    Drill-Compiled-Fresh-Mechanics v2.0 (1,265L, 20 insights)
           + Drill-PFC-Label v1.0 (vocabulary)

NỘI DUNG:
  ① Hold + Suppress = 2 PFC operations trên Compiled/Fresh spectrum
  ② Compiled Quality Dimension (genuine / schema / threat)
  ③ B vs C Determinant: 7 factors quyết định outcome
  ④ Pattern Shiftability × BP Quadrants
  ⑤ Compiled suppress pathways → learned helplessness, therapy
  ⑥ PFC-Fresh = universal resource (shared, finite)
  ⑦ Architecture B + 3-Cost integration

DEPENDENCIES: None. Reads existing files only.
WHY FIRST:   Hold/Suppress là concept được reference nhiều nhất.
             Hầu hết rewrite/refine sau đó đều cần file này.
```

---

### A2. Simulation-Engine.md [NEW]

```
VỊ TRÍ:   Core-Deep-Dive/PFC/ hoặc Body-Base/ (quyết định khi implement)
SOURCE:    Drill-Simulation-Engine v1.0 (809L, 16 insights)
           + Drill-SPM-Self-Shared-Substrate v1.0 (13 insights)

NỘI DUNG:
  ① 1 Engine: DMN + vMPFC + anterior insula + hippocampus
  ② 3 Components: Interoception + Constructive Simulation + Self/Other Model
  ③ 3 Axes: Target (Self↔Other) × Time (Past↔Future) × Operation (Observe/Simulate/Evaluate/Construct)
  ④ Application = tọa độ trong 3D space
     SPM = (Other, Present, Simulate)
     Self-Observation = (Self, Present, Observe)
     Imagine-Final = (Self, Future, Simulate)
  ⑤ Alexithymia proof: hỏng 1 component = hỏng ALL applications
  ⑥ Diversity effect: different others → sharper self-model
  ⑦ Reflection vs Rumination: quality > quantity
  ⑧ Training implications: luyện 1 = luyện cả 3

DEPENDENCIES: None. Reads existing SPM v3.0, Imagine-Final, Feeling v3.0.
WHY SECOND:  SPM rewrite (B2) + Imagine-Final rewrite (B1) depend on
             Simulation Engine concept being formalized.
```

---

### A3. Entity-Compiled.md [NEW]

```
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
SOURCE:    Drill-Entity-Compiled v2.0 (1,340L, 39 insights)

NỘI DUNG:
  ① Definition + Position (VP §3 → deep mechanism file)
  ② 8 Research Streams Hội Tụ (neural reality)
  ③ Hub-and-Spoke + Body Simulation (neural architecture)
  ④ Formation Timeline + 2 Points (acquaintance → compiled entity)
  ⑤ Dunbar Capacity Ceiling + 3 Mechanisms (interference, cost, decay)
  ⑥ "Hợp tính" 2D Matrix + Meta-Match
  ⑦ State/Trait Convergence
  ⑧ Loss + Grief Intensity model
  ⑨ Love ↔ Hate Shift
  ⑩ Decay 3-Layer Model
  ⑪ Machine Logic: Vulnerable By Design

DEPENDENCIES: Reads VP v2.0, Body-Coupling v2.0 (existing).
WHY THIRD:   Entity-Access (A4) depends on Entity-Compiled being formalized.
```

---

### A4. Entity-Access.md [NEW]

```
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
SOURCE:    Drill-Entity-Access v1.1 (35 insights)
           + Drill-Entity-Access-Excess v2.0
           + Drill-Entity-Access-Calibration v2.0 (20 insights)

NỘI DUNG:
  ① MAJOR REFRAME: Entity-Owned (binary) → Entity-Access (gradient)
  ② 3-Factor Model: F1 Engine Mode × F2 Gap-Need Profile × F3 Access Confidence
  ③ Entity-Access Gradient: Mức 0 (Tool/Service) → Mức 5 (Excess)
  ④ Entity-Owned = PFC LENS (observation label cho Mức 4-5), NOT mechanism
  ⑤ 4 Starting Modes: Hardware / Limerence / Interaction / Schema
  ⑥ B-dominant = optimal destination, not universal origin
  ⑦ EXCESS section: Mức 5, same neural circuits as addiction, gap shift ≠ compiled suppress
  ⑧ CALIBRATION section: 3 layers, exit cost = signal weight, optimal ≠ zero C
  ⑨ Per-entity dynamics + lifecycle

DEPENDENCIES: Entity-Compiled.md (A3), Simulation-Engine (A2).
WHY FOURTH:  Connection, Empathy, Love, Body-Coupling refines all need
             Entity-Access concepts.
```

---

## §2 — PHASE B: REWRITES (5 sessions)

> Nội dung thay đổi đáng kể. Viết lại cho coherent.
> Nguyên tắc: 100% citations giữ, signature examples giữ, honest assessment update.

---

### B1. Imagine-Final.md [REWRITE DRAFT → v2.0]

```
VỊ TRÍ:   Core-Deep-Dive/PFC/Imagination/
HIỆN TẠI:  DRAFT 2026-03-27 — FILE CŨ NHẤT FRAMEWORK (không version header)
SOURCE:    Drill-Simulation-Engine v1.0 + Drill-SPM-Self-Shared-Substrate v1.0

KEY CHANGES:
  ① Imagine-Final = Application (Self, Future, Simulate) trên Simulation Engine
  ② Lifecycle rewrite theo v7.8+ architecture
  ③ Relationship với SPM + Self-Observation qua shared substrate
  ④ PFC-Operations integration (Hold/Suppress × Imagine-Final)
  ⑤ Entity-Access: "Imagine-Final of relationship" → schema vs genuine
  ⑥ Full v7.8 alignment (Compiled/Fresh, Architecture B, Domain=Arbiter)

DEPENDENCIES: Simulation-Engine (A2).
NOTE:        Stale nhất → ưu tiên cao. Rewrite hoàn toàn.
```

---

### B2. Self-Pattern-Modeling.md [REWRITE v3.0 → v3.1]

```
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
           (RENAME file: Self-Pattern-Match.md → Self-Pattern-Modeling.md)
HIỆN TẠI:  Self-Pattern-Match.md v3.0 (1,948L)
SOURCE:    Drill-SPM-Mechanism v2.2 (17 insights)
           + Drill-Over-SPM-Clarification v1.0 (12 insights)
           + Drill-SPM-Self-Shared-Substrate v1.0 (13 insights)

KEY CHANGES:
  ① RENAME: Self-Pattern-Match → Self-Pattern-Modeling (abbreviation SPM giữ nguyên)
  ② 1 mechanism × 3 dimensions (not 4 skills):
     Processing Level (Compiled↔Fresh) × Valence Direction × Output Intensity (Clone)
  ③ Over-clone = observation label, mechanism = compiled suppress gap riêng
  ④ 4 conditions ĐỒNG THỜI cho resonance
  ⑤ Abstract entities taxonomy (Thiên Chúa, Harry Potter, AI)
  ⑥ BP triple bias: retrieval + template + interpretation
  ⑦ Transfer + interference + Freud reframe
  ⑧ 8 failure modes
  ⑨ Developmental trajectory (infant→child→adult→elderly)
  ⑩ SPM × Imagine-Final connection qua Simulation Engine

DEPENDENCIES: Simulation-Engine (A2), PFC-Operations (A1).
```

---

### B3. By-Product-Gap-Resonance.md [REWRITE v1.0 → v1.1]

```
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
HIỆN TẠI:  v1.0 (2026-05-19)
SOURCE:    Drill-PR-Definition v1.0 (11 insights)
           + Drill-Bond-Architecture v1.0 (23 insights)
           + Drill-Over-SPM-Clarification v1.0 §3-§4
           + Drill-Resonance-Sustainability v1.0 (24 insights)
           + Drill-By-Product-Scale v1.0 (20 insights)

KEY CHANGES:
  ① 4 conditions enriched (positive valence + mutual Agent-mode + gap overlap + drive riêng)
  ② Over-clone reframe: observation label, NOT mechanism (per §9 guidelines)
  ③ Resonance decline: 4 mechanisms (M1 compiled suppress PRIMARY + M2 habituation
     + M3 prediction completion + M4 Entity-Compiled saturation)
  ④ Enhancers formalized: SPM, proximity, duration = enhancers NOT requirements
  ⑤ Sustainability conditions: 3 primitive conditions, 3 modalities,
     amplification mechanisms (capitalization, PPR, secure base, self-expansion)
  ⑥ 3 Scales preview: Pair / Hub / Institutional (same mechanism, different topology)
  ⑦ Resonance Core vs Enhancers distinction (from PR-Definition)
  ⑧ "Duyên số" = filtering cost

DEPENDENCIES: SPM v3.1 (B2) for updated cross-refs.
NOTE:        File lớn nhất trong rewrite — absorb nhiều drill insights.
```

---

### B4. Boredom.md [REWRITE v1.1 → v2.0]

```
VỊ TRÍ:   Core-Deep-Dive/Observation/
HIỆN TẠI:  v1.1 (~900L, 5 sources)
SOURCE:    Drill-Boredom-Mechanism v2.0 (16 insights)

KEY CHANGES:
  ① Source ⑥: by-product match dừng ("chán nhau")
  ② Unified formula: Dissonance + Imagine-Final mờ = "chán" MỌI TRƯỜNG HỢP
  ③ Gap-clone IMPOSSIBLE → "chán nhau" do 4 sub-mechanisms
  ④ Abundance hypothesis: dư thừa → higher gaps → harder to fill → boredom
  ⑤ Historical vs modern boredom (pre-modern ít "chán")
  ⑥ 6 observation axes
  ⑦ "Chán" vs "ghét" threshold model

DEPENDENCIES: PFC-Operations (A1) for compiled suppress reference.
```

---

### B5. Valence-Propagation.md [REWRITE v2.0 → v3.0]

```
VỊ TRÍ:   Core-Deep-Dive/Body-Base/
HIỆN TẠI:  v2.0 (~1,800L, Entity-Compiled §3)
SOURCE:    Drill-Entity-Valence-Dynamics v2.0 (28 insights)

KEY CHANGES:
  ① Structural valence (aggregate tags, INSIDE EC, slow) vs Current valence (L1+L2 lúc này, OUTSIDE, fast)
  ② 3 Firing Modes: Maintenance (invisible) → Chunk-Miss (acute) → Context-Trigger (random)
  ③ Hardware Subsidy = ANTI-HABITUATION: modulate VTA habituation per entity
  ④ Satiation type × valence dynamics: Cyclic (sharp oscillation) / Tonic (slow invisible) / Generative (renewable)
  ⑤ RSA A:B ratio × valence "feel": B=warm/soothing, A=exciting/stimulating
  ⑥ Per-entity valence dynamics table
  ⑦ "Xa mẹ mới biết thương" = 3 cơ chế cộng dồn
  ⑧ Mixed valence = PARALLEL per-channel, MOST COMMON
  ⑨ Phantom resonance 4-factor model
  ⑩ Technology × valence frontier

DEPENDENCIES: Entity-Compiled (A3), Entity-Access (A4).
WHY REWRITE: 28 new insights = ~30-40% nội dung mới. Structural changes quá lớn cho refine.
```

---

## §2B — PHASE T: TÁCH + MỚI (8 sessions)

> Phase A+B tạo framework files — nhưng một số MERGE quá nhiều drill vào 1 file.
> Entity-Access.md nén 3 drills (4,508L) → 1 file (1,430L) = mất 84-92% chi tiết.
> BPGR v1.1 gom 5 drills vào 1 file (1,665L) = monolithic.
> 2 drill CHƯA FORMALIZED (By-Product-Resonance-Entity + Individual-Gap-Body-Need).
> PFC-Label drill = vocabulary standard (companion BFL), cần formalize.
> Phase T TÁCH chúng ra + tạo file MỚI cho drill chưa formalized + vocabulary.
> **Nguyên tắc: tách rõ ràng để quan sát hiệu quả > merge gọn.**
> **3 drill SKIP** (đã hết nhiệm vụ): PR-Definition, Over-SPM-Clarification, SPM-Self-Shared-Substrate.

---

### T0. PFC-Label.md [MỚI — vocabulary standard]

```
VỊ TRÍ:   Core-Deep-Dive/PFC/
SOURCE:    Drill-PFC-Label v1.0 (1,017L, 16 sections)
COMPANION: Body-Feedback-Label v2.0 (body signal vocabulary)

NỘI DUNG:
  ① 3-tier label system (tương tự BFL: General → Direction → Specific)
  ② PFC Role Labels (5 vai trò tùy context: Observer, Lawyer, Director, Universal Resource, QC)
  ③ Processing Spectrum: Compiled ←→ Fresh
  ④ PFC Operations: HOLD + SUPPRESS
  ⑤ PFC Cost Labels (3-cost + budget)
  ⑥ Compiled Quality Labels (genuine / schema / threat)
  ⑦ PFC Region Labels (anatomy mapping)
  ⑧ PFC Hardware Labels (individual differences: COMT, DRD4)
  ⑨ Simulation Engine Labels (1 engine, 3 components)
  ⑩ Observer vs Mechanism (Logic/Feeling vs Compiled/Fresh)
  ⑪ Deprecated Terms + Standardization

DEPENDENCIES: PFC-Operations v1.0 (A1), Simulation-Engine v1.0 (A2).
NOTE:        Drill đã structured tốt. Formalize + sync với PFC-Ops v1.0 mới.
             Vocabulary standard TRƯỚC khi viết T1-T7 + C1-C6.
EST. LINES:  ~800
```

---

### T1. Entity-Access-Excess.md [TÁCH từ EA §6] ✅

```
✅ DONE 2026-05-22
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
ACTUAL:    Entity-Access-Excess.md v1.0 (~1,121L, 65 citations, 13 sections)
SOURCE:    Drill-Entity-Access-Excess v2.0 (1,769L, 36 insights, 65 citations)
TRIM:      Entity-Access.md §6 trimmed + §7 cross-ref added → EA v1.1

NỘI DUNG:
  §0 Thesis + Position
  §1 Excess spectrum: healthy → excess → addiction (Mức 5) + 5 boundary indicators
  §2 Addiction mechanism: neural circuits + SPM atrophy (★ KEY) + pseudo-understanding
  §3 Mẹ→con: designed vs overdriven (helicopter/tiger/empty nest/hikikomori)
  §4 Romantic: bilateral trap + unilateral suffocation + schema-maintained
  §5 Gap shift ≠ compiled suppress: 2 mechanism + compound + per-relationship
  §6 3 Origins: hardware chain + trauma + schema + triple amplification
  §7 Cultural variation: 3 models, collectivist paradox, marriage data
  §8 BP overlap spectrum: similarity paradox, sensation seeking
  §9 Measurement paradox: McNulty 2013 Science
  §10 Fix spectrum: per-case approach
  §11-§13 Honest assessment + Cross-refs + 65 citations (R1-R65)
```

---

### T2. Entity-Access-Calibration.md [TÁCH từ EA §8] ✅

```
✅ DONE 2026-05-22:
  Entity-Access-Calibration.md v1.0 CREATED (~1,073L, 16 sections, 25 citations)
  Entity-Access.md v1.1 → v1.2 (§8 trimmed + cross-ref + §12 updated)
  
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
SOURCE:    Drill-Entity-Access-Calibration v2.0 (1,159L, 20 insights, 25 citations)
TRIM:      Entity-Access.md §8 (~185L) → summary + cross-ref to new file

NỘI DUNG ACTUAL:
  §0 Thesis+Position, §1 Dynamic Equilibrium (Goldilocks + 5 complexity),
  §2 3-Layer Architecture (★ CORE: Body Signal × Engine Simulation × Feedback),
  §3 Exit Cost = Signal Weight (★ CORE: per bond type table, lifecycle shift),
  §4 Hardware Subsidy = Calibration Bias (A+C compound, per bond table, Trivers),
  §5 Compiled vs Fresh: Calibration Window (table, cascading, decompile path),
  §6 Engine Use Quality: Curiosity vs Threat (VD, parenting guilt, 3 outcomes),
  §7 Optimal Zone: Justified C + Bids (★ CORRECTION: Baumrind+SDT+Gottman, 6-level spectrum),
  §8 Per Bond Type Dynamics (bạn bè/romantic/parent/professional),
  §9 5 Failure Modes (Blind/Tool/Override/Depleted/Threat + compound),
  §10 Cannot Prescribe (infinite regress, 4 dimensions, file helps gì),
  §11 Training + Spiral (4 targets, Social Baseline, virtuous/vicious),
  §12 Calibration × Gradient (★ per-Mức table, Mức 4 critical, parenting lifecycle),
  §13 Honest Assessment (🟢/🟡/🔴), §14 Cross-refs, §15 Citations (R1-R25)

DEPENDENCIES: Entity-Access.md v1.2, Entity-Access-Excess.md v1.0 (T1).
ACTUAL LINES: ~1,073
```

---

### T3. Bond-Architecture.md [TÁCH từ BPGR §9-§10] ✅

```
✅ DONE (2026-05-22):
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
ACTUAL:    Bond-Architecture.md v1.0 (~1,183L, 14 sections, 28 citations)
SOURCE:    Drill-Bond-Architecture v1.0 (1,091L, 23 insights, 28 citations)
TRIM:      BPGR v1.1→v1.2 §9-§10 headers → BRIEF + cross-ref BA §3-§4

NỘI DUNG:
  ① Entity-Compiled = 1 mechanism × nhiều configurations (5 nghiên cứu hội tụ)
  ② 4 Bond Types × 12 dimensions comparison table
  ③ Gap clone = STRUCTURALLY IMPOSSIBLE (5-step proof + twins decisive)
  ④ 3 cơ chế thật: gap redirect ≠ gap clone ≠ compiled suppress
  ⑤ 4 Mechanisms decline (M1 compiled suppress → accelerate M2+M3+M4)
  ⑥ True understanding = anti-compiled-suppress (meta-principle ALL bonds)
  ⑦ Domain coverage 5×4 matrix + structural impossibility
  ⑧ Historical vs modern domain overlap shift
  ⑨ Per-bond-type dynamics deep-dive + 5 cases

DEPENDENCIES: BPGR v1.1 (core definition), Entity-Compiled v1.0.
```

---

### T4. Resonance-Sustainability.md [TÁCH từ BPGR §7-§8-§11] ✅

```
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
SOURCE:    Drill-Resonance-Sustainability v1.0 (1,408L, 24 insights, 32 citations)
TRIM:      BPGR v1.2 §7, §8, §11 → BRIEF + cross-ref to new file → BPGR v1.3

✅ DONE (2026-05-22):
  Resonance-Sustainability.md v1.0 (~1,355L, 19 sections §0-§18, 32 citations R1-R32)
  BPGR v1.2 → v1.3 (§7+§8+§11 trimmed + cross-ref + §18 + dependencies updated)
  4 observation cases, 4-Layer synthesis model
  15 dependencies verified

NỘI DUNG:
  ① 3 Primitive Conditions (Proximity × Duration × Agent-mode)
  ② Gap Flexibility (Gap ≠ Strategy)
  ③ 3 Resonance Modalities (Verbal/Non-verbal/Body-level) INDEPENDENT channels
  ④ Silence 4 types (Intrinsic/Introjected/External/Spontaneous)
  ⑤ Verbal necessity spectrum
  ⑥ Capitalization (Active-Constructive responding)
  ⑦ PPR × SPM interpretation
  ⑧ Secure Base Effect (3 components spiral)
  ⑨ Self-expansion × boredom year 7
  ⑩ Maintenance decline paradox (compiled bonds need MORE effort, get LESS)
  ⑪ Co-regulation U-curve (value-neutral)
  ⑫ Motivated inaccuracy (protective deflection)
  ⑬ Dormant ties resilience
  ⑭ 4-Layer sustainability synthesis

DEPENDENCIES: BPGR v1.2 (core definition), Bond-Architecture.md v1.0 (T3).
ACTUAL LINES: ~1,355 (plan ~1,000 — drill source richer than expected)
```

---

### T5. By-Product-Scale.md [TÁCH từ BPGR §13] ✅

```
✅ DONE 2026-05-22
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
ACTUAL:    By-Product-Scale.md v1.0 (~905L, 15 citations, 16 sections)
SOURCE:    Drill-By-Product-Scale v1.0 (790L, 20 insights, 15 citations)
TRIM:      BPGR v1.3 §13 → BRIEF + cross-ref → BPGR v1.4

NỘI DUNG:
  §0  Position + Thesis + Claims (7 claims)
  §1  Core Mechanism Recap (3 properties: not intentional, asymmetric, by-product > intentional)
  §2  Level 1 Pair: A↔B, direct verify, oxytocin, ~150 Dunbar
  §3  Level 2 Hub: Node↔Collective, trust bypass, serotonin, compression N×(N-1)/2
  §4  Level 3 Institutional: distributed, institutional trust, 8 billion
  §5  Hardware Subsidy per Scale (body→collective shift, serotonin=L2 subsidy)
  §6  Compilation per Scale (speed×accuracy trade-off table)
  §7  Failure + Self-Correction (cross-scale pattern table)
  §8  Prestige vs Dominance = Genuine vs Schema resonance (7-row mapping table)
  §9  Mẹ = first coordination node (5 capabilities + lifecycle transition)
  §10 Specialization × Dependency (all 3 levels + trend)
  §11 Technology Fill per Scale (routine→genuine frontier shift)
  §12 4 Observation Cases (startup, "vợ=tất cả", degree inflation, village→city)
  §13 Honest Assessment (14 🟢 + 14 🟡 + 4 🔴)
  §14 Cross-references (4 groups)
  §15 Research Citations (R1-R15)

DEPENDENCIES: BPGR v1.4 (core definition), Bond-Architecture v1.0 (T3).
ACTUAL LINES: ~905 (plan ~600 — formalization + cases + tables add volume)
```

---

### T6. Gap-Body-Need.md [MỚI từ drill] ✅

```
✅ DONE 2026-05-22
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Body-Feedback/
ACTUAL:    Gap-Body-Need.md v1.0 (~1,388L, 33 citations, 19 sections)
SOURCE:    Drill-Individual-Gap-Body-Need v2.0 (1,498L, 36 insights, 33 citations)

NỘI DUNG:
  §0  Position + Thesis + Claims (7 claims)
  §1  Gap Definition Recap (from Gap-Direction v2.0)
  §2  3 Satiation Profiles (Cyclic/Tonic/Generative) + RSA A:B integration
  §3  Profile Transitions + Compounds (romantic "chán nhau" model)
  §4  Hardware Gaps × Reward Type (8-row integrated table)
  §5  Domain/Coherence Gaps × Reward Type (5-row table + schema gap)
  §6  5-Parameter Per-Gap Model (P1-P5 + 5 ví dụ table + P4×P5 decouple)
  §7  Hardware × Domain Competition + Priority (4 resolution mechanisms)
  §8  2 Pathways × Chain Length (Pathway 1/2 + Einstein paradox + 15-20yr chains)
  §9  ENGINE/ROAD/VEHICLE Architecture (collective = infrastructure)
  §10 Technology Fill (per-domain table + Kahneman-Deaton + Type B hedonic floor)
  §11 Entity-Gap Matching (5-step + cross-entity competition + lock-in)
  §12 Existence-Based Gaps (4-compound mechanism + phantom gap)
  §13 Collective-Arc Bias (3 mechanisms: install/suppress/re-tag)
  §14 Gap Lifecycle (creation → dormancy → compound → weakening)
  §15 4 Observation Cases (chán nhau, Einstein, sugar schema, mid-life crisis)
  §16 Honest Assessment (25 🟢 + 18 🟡 + 7 🔴)
  §17 Cross-references (18 files)
  §18 Research Citations (R1-R33)

DEPENDENCIES: GDP v1.0, BFM v2.0, RSA v2.0, IBM v1.0, EA v1.2, SPM v3.1, IF v3.0, VP v3.0.
NOTE: GDP = zoom OUT (aggregate landscape). Gap-Body-Need = zoom IN (per-gap mechanics).
ACTUAL LINES: ~1,388 (plan ~1,100 — tables + 4 observation cases + RSA integration add volume)
```

---

### T7. Resonance-Per-Entity.md [MỚI từ drill] ✅ DONE (2026-05-22)

```
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
SOURCE:    Drill-By-Product-Resonance-Entity v2.0 (1,420L, 30 insights, 33 citations)
RESULT:    Resonance-Per-Entity.md v1.0 (~1,606L, 20 sections §0-§19, 33 citations, 4 cases)

NỘI DUNG (ACTUAL):
  §0  Position + Thesis + Claims (7 claims, 4-level stack, companion file map)
  §1  Compilation Chain: F2→F1→Baseline→Dynamics (4 stages, 3-cost per stage, rate per entity)
  §2  Hardware Subsidy: Anti-Habituation Spectrum (MAX→MODERATE→TEMPORARY→NONE)
  §3  3-Tầng Per-Entity Model (Supply S1-S4, Mechanism M1-M5, Dynamics D1-D5)
  §4  Resonance × Mẹ-Con — Asymmetric (§4.1 Mẹ→Con: existence-based, §4.2 Con→Mẹ: episodic+mixed)
  §5  Resonance × Bạn Thân (Generative dominant, zero hw subsidy, FAST decay)
  §6  Resonance × Romantic (Phase 1 limerence MASK, Phase 2 three trajectories A/B/C)
  §7  Resonance × First Meeting EC=0 (4 nguồn drive, "click" ≠ resonance)
  §8  Resonance × Tool-Mode + Professional (5 subtypes: bưu tá, colleague, teacher, therapist, AI)
  §9  Enriched Comparison Table (3-tầng × 5 entity types × mixed valence)
  §10 Lifecycle: Resonance Shift Theo Tuổi (6 age phases + mechanism-level WHY)
  §11 ENGINE/ROAD/VEHICLE × Resonance (specialization trade-off, portfolio diversification)
  §12 Technology Fill × Modern Resonance Frontier (Kahneman-Deaton + AI × resonance)
  §13 Collective-Arc Bias on Entity Selection (3 bias types + technology era)
  §14 "Chán" Qua Resonance Lens (M1-M4 per entity, Tonic+Generative compound loss)
  §15 Phantom Resonance × Grief (4-factor model, per-entity phantom intensity table)
  §16 4 Observation Cases (romantic chán, Einstein P4/P5, therapist burnout, teen lifecycle)
  §17 Honest Assessment (27 🟢 + 14 🟡 + 6 🔴)
  §18 Cross-references (20 files across 4 categories)
  §19 Research Citations (R1-R33, 32 green + 1 yellow)

DEPENDENCIES: BPGR v1.4, VP v3.0, EC v1.0, BA v1.0, RS v1.0, BS v1.0, GBN v1.0,
              EA v1.2, SPM v3.1, PFC-Ops v1.0, SE v1.0, IBM v1.0, Connection v4.0,
              RSA v2.0, GDP v1.0, Love-Romantic v2.4, Empathy v3.0, BFL v2.0.
ACTUAL LINES: ~1,606 (plan ~1,000 — per-entity profiles + 4 cases + comparison table + phantom table add volume)
```

---

### TRIM NOTES

```
① Entity-Access.md v1.0 → v1.1:
   - §6 Excess (~133L) → trim to summary + cross-ref Entity-Access-Excess.md
   - §8 Calibration (~185L) → trim to summary + cross-ref Entity-Access-Calibration.md
   - Trim trong session T1 (§6) và T2 (§8)

② BPGR v1.1 → v1.2:
   - §9-§10 → trim to summary + cross-ref Bond-Architecture.md
   - §7, §8, §11 → trim to summary + cross-ref Resonance-Sustainability.md
   - §13 → trim to summary + cross-ref By-Product-Scale.md
   - Trim trong session T3, T4, T5
   - BPGR core giữ: §0-§6, §12, §14-§16 (~800L)

③ SKIP DRILLS (đã hết nhiệm vụ, không cần framework file):
   - Drill-PFC-Label.md → vocabulary reference, đã propagate qua PFC-Ops + ~78 files
   - Drill-PR-Definition.md → definitional refinement, đã absorbed vào BPGR §1, §5, §6
   - Drill-Over-SPM-Clarification.md → bias prevention reference, giữ ở backup/
   - Drill-SPM-Self-Shared-Substrate.md → evidence, đã vào SE v1.0 + SPM v3.1
```

---

## §3 — PHASE C: REWRITE + REFINE (9 sessions)

> **C1-C6: REWRITE** — Phase A+B tạo nền tảng mới (4 files + 5 rewrites).
> C1-C6 cần REWRITE cho chất lượng đồng bộ: dependencies outdated (VP v2.0→v3.0,
> SPM v3.0→v3.1), Phase A files chưa reference, drill content chưa integrated.
> **Phase T bổ sung 7 files chi tiết** — C1-C6 reference ALL Phase T files.
> Bond-Architecture, Resonance-Sustainability, Resonance-Per-Entity đặc biệt quan trọng
> cho Connection, Love-Romantic, Love-Unified, Body-Coupling.
> **C7-C9: REFINE** — structure vững, thêm sections/cross-refs.
> Nguyên tắc: Chậm mà chắc. 1 file per session. Chất lượng > tốc độ.

---

### C1. Connection v4.0 → v5.0 [REWRITE] ✅ DONE (2026-05-22)

```
✅ DONE: Connection.md v5.0 REWRITTEN (2026-05-22)
VỊ TRÍ:    Core-Deep-Dive/Observation/
THAY ĐỔI:  v4.0 (2,325L) → v5.0 (~3,072L)
BACKUP:     backup/Connection-v4.0-backup.md

CONTENT:
  §0.3 NEW: Entity-Access gradient Mức 0-5 × connection spectrum
  §1 UPDATED: Simulation Engine context, SPM v3.1 terminology
  §3.1 ENRICHED: Hardware Subsidy spectrum (MAX→NONE per entity) + gap-body-need
  §3.3 ★ MAJOR: structural/current valence + 3 satiation types (C/T/G) + mixed valence
    (Cacioppo 1994) + 3 firing modes (maintenance/chunk-miss/context-trigger)
  §4.5 ★ NEW: M1-M4 Resonance Decline × Connection (BA v1.0)
    + gap clone impossible (5-step proof) + 3 real mechanisms (redirect/suppress/converge)
    + anti-compiled-suppress = solution + 1 entity ≠ all domains → portfolio
  §4.6 ★ NEW: 4-Layer Sustainability × Connection (RS v1.0)
    + 3 conditions (proximity+duration+agent-mode) + 3 modalities (verbal/non-verbal/body)
    + 4 silence types + amplification (capitalization+PPR+secure base) + Ogolsky decline
  §5.1: per-entity pathway dominance table
  §7.2 NEW: Compilation Chain × Connection Formation (4 stages F2→F1→Baseline→Dynamics)
  §8: entity-access gradient × virtual chunks
  §9: PPR reference (Reis & Shaver 1988)
  §10.2: PFC budget × momentary capacity (PFC-Operations v1.0)
  §11: 3 modalities × distance spectrum
  §14: By-Product-Scale (3 scales: pair/hub/institutional)
  §15 ★ MAJOR: phantom 4-factor model + per-entity phantom table + "xa mẹ" 3 mechanisms
  §16: per-entity cô đơn risk profile
  §17 REWRITTEN: 43+ 🟢 + 24+ 🟡 + 7 🔴
  §18 RESTRUCTURED: 40+ refs, 8 categories, full changelog
  SPM v3.1 terminology throughout (Match→Modeling)

DEPENDENCIES: 40 files (YAML). Phase A+B+T ALL integrated.
CITATIONS: 43+ 🟢 (was 27). +15 new Phase T citations.
```

---

### C2. Empathy v3.0 → v4.0 [REWRITE] ✅ DONE (2026-05-22)

```
✅ DONE — Empathy.md v4.0 REWRITTEN (~2,895L, 25 deps, 35+ citations)
   Location: Core-Deep-Dive/Observation/
   Backup: backup/Empathy-v3.0-backup.md

   KEY CONTENT v4.0 (over v3.0):
   - §0 NEW: Simulation Engine context, PFC budget preview, Entity-Access Mức 0-5 table
   - §1.1 ENRICHED: Structural vs Current empathy, +explanation #7 hw subsidy
   - §2.1 NEW: Compilation Chain mapping onto 3 mechanisms
   - §3.1 ENRICHED: Entity-Compiled formation (hub-and-spoke, 40→200h)
   - §4.1 ★ ENRICHED: PFC budget × empathy (parent-child = highest cost),
     Compiled Quality (genuine/schema/threat → burnout)
   - §4.2 ENRICHED: 3 Firing Modes × empathy (Mode 1/2/3)
   - §4.6 ★ NEW: Hardware Subsidy × Empathy (MAX→MODERATE→TEMPORARY→NONE)
   - §4.7 ★ NEW: Per-entity empathy profiles (5 types × 7 parameters)
   - §4.8 NEW: 3 Satiation Types × Empathy (Cyclic/Tonic/Generative)
   - §4.9 NEW: Compilation Chain × Empathy (4 stages, per-entity rate)
   - §5.2 NEW: Entity-Access gradient × empathy ceiling + exit cost paradox
   - §7.1 NEW: By-Product-Scale (3 scales × empathy)
   - §8.2 ★ REFRAME: Burnout = compiled suppress (M1) + PFC depletion +
     compiled quality + escalation + 6-step recovery
   - §8.7 ★ NEW: M1-M4 Resonance Decline × Empathy + anti-compiled-suppress
   - §8.8 NEW: 4-Layer Sustainability × Empathy (PPR + secure base)
   - §8.9 NEW: Empathic Accuracy + Motivated Inaccuracy
   - §8.10 NEW: 3-Layer Calibration Architecture (5 failure modes)
   - §10: +15 new 🟡 items
   - §11: RESTRUCTURED (4 categories, 25 deps)
   - SPM v3.1 throughout, all dependency versions updated
```

---

### C3. Body-Coupling v2.0 → v3.0 [REWRITE] ✅ DONE

```
✅ DONE (2026-05-22) — Body-Coupling.md v3.0 REWRITTEN
   ~2,883L (was 2,009L v2.0). ~27 dependencies. ~45+ citations.

   10 NEW SUBSECTIONS:
     §1.5 Satiation Types × coupling channels (Cyclic/Tonic/Generative)
     §3.6 Entity-Access gradient × coupling depth (Mức 0-5)
     §4.6 PFC budget × coupling cost (parent = highest)
     §4.7 Compiled Quality × coupling (genuine/schema/threat)
     §4.8 Hardware Subsidy × coupling sustainability (4 levels)
     §4.9 Entity-Access × coupling interaction
     §6.9 Resonance Sustainability × coupling durability (PPR, secure base, 4 silence)
     §8.7 Entity-Access-Excess × coupling (Mức 5, 3 origins, gap shift compound)
     +Q8-Q12 new open questions
     +P8-P11 new testable predictions

   17 ENRICHED SECTIONS:
     §0 +SE context, +EA gradient, +7-file table, +TIỀN ĐỀ ĐỌC, +SCOPE IN/OUT
     §1.1 +Structural/Current valence × coupling, +3 intensity factors
     §1.3 +Hw Subsidy × L2 sustainability (4 levels table)
     §1.4 +3 Firing Modes × L2 (Mode 1/2/3)
     §2.2 +4 bond types × 1 EC (BA v1.0), +domain coverage
     §2.3 +M1-M4 resonance decline × entanglement
     §2.5 +EA Mức 0-1 = structural impossibility
     §2.6 +By-Product-Scale × system compilation (3 levels)
     §3.1 +Compilation Chain mapping (RPE v1.0)
     §3.3 +Hw Subsidy × compile_rate
     §5 +Structural/Current × smoothing, +Satiation × smoothing
     §6.1 +4-Layer Sustainability × coupling deepen
     §6.5 +Phantom 4-factor model + per-entity intensity
     §7 +Hw Subsidy MAX, +EA gradient, +PFC budget, +anti-compiled-suppress, +Compilation Chain
     §9 +20 citations, +25 🟡, +5 🔴, +4 predictions
     §10 restructured: 4 categories, ~27 deps

   SPM v3.1 throughout (Match→Modeling). ALL deps updated.
   v2.0 → backup/Body-Coupling-v2.0-backup.md
```

---

### C4. Love-Romantic v2.4 → v3.0 [REWRITE] ✅

```
✅ DONE 2026-05-22
VỊ TRÍ:   Research/
ACTUAL:    Love-Romantic.md v3.0 (~3,287L, ~36 deps, 50+ citations)
BACKUP:    backup/Love-Romantic-v2.4-backup.md

NỘI DUNG v3.0:
  §0 REWRITE: +SE context, +EA gradient preview, +TIỀN ĐỀ ĐỌC, +ĐỌC FLOW
  §1 ENRICHED: +Structural vs Current valence, +Hw Subsidy TEMPORARY
  §2 ENRICHED: +Compiled Quality × romantic (genuine/schema/threat)
  §3 ENRICHED: +EC v1.0 Hub-and-Spoke, +Compilation Chain × romantic
  §4 ENRICHED: +PFC Budget × romantic cost, +By-Product-Scale Level 1
  §5 ENRICHED: +PFC-Operations, +Motivated Inaccuracy (triple mechanism)
  §9.2 ★ NEW: Hw Subsidy TEMPORARY × Limerence Window
  §9.3 ★ NEW: 3 Satiation Types × Romantic Stages
  §10.3 ★ NEW: Compilation Chain × Transition + 3 Firing Modes
  §11.4 REFRAME: differentiation → anti-compiled-suppress + domain coverage
  §11.7 ★ NEW: 3 Firing Modes × Romantic Bonding
  §11.8 ★ NEW: M1-M4 Resonance Decline × Romantic
  §11.9 ★ NEW: 4-Layer Sustainability × Romantic (PPR, Secure Base, 4 silence)
  §11.10 ★ NEW: EA Gradient × Romantic Deepening (Mức 2→5)
  §11.11 ★ NEW: EA-Excess × Romantic (bilateral/unilateral, 3 origins)
  §11.6 ENRICHED: +Exit Cost × Calibration (Mức 4 critical zone)
  §12.7 ★ NEW: Phantom 4-Factor (Grief A+B+C, Love↔Hate, Decay 3-Layer)
  §12.8 ★ NEW: Structural Valence × Grief
  §13 ENRICHED: +19 🟢 citations, +16 🟡 claims, +5 🔴 predictions
  §14 RESTRUCTURED: 4 categories, ~36 deps, CHANGELOG v3.0
  GLOBAL: SPM v3.1, all deps updated

DEPENDENCIES: A4, B3, B5, T1-T5, T7, C1, C2, C3.
```

---

### C5. Love-Unified v1.2 → v2.0 [REWRITE] ✅ DONE

```
✅ DONE (2026-05-22): Love-Unified.md v2.0 REWRITTEN at Research/
   ~2,532L (was 1,427L), 15 sections (was 9), ~35 deps, 50+ citations

   6 NEW SECTIONS:
     §4 Hw Subsidy × 6 types (4-level table, visibility paradox)
     §5 Satiation Types × 6 types ("chán" mechanism unified)
     §6 Bond-Architecture × 6 types (M1-M4, anti-compiled-suppress, domain coverage)
     §8 Entity-Access × 6 types (EA gradient, Excess, Calibration, PFC Budget)
     §9 Sustainability × 6 types (4-Layer, 3 Firing Modes, PPR, 4 silence)
     §10 Phantom+Grief × 6 types (4-factor, A+B+C, Love↔Hate, Decay 3-Layer)

   ENRICHED SECTIONS:
     §0 +SE context, +EA gradient preview, +TIỀN ĐỀ ĐỌC, +SCOPE IN/OUT
     §1 +Structural/Current (§1.3), +EC Hub-and-Spoke + Dunbar (§1.4)
     §2 +Compiled Quality × smoothing (§2.5), +Motivated Inaccuracy (§2.6)
     §3 +EA gradient × 2-axis (§3.5)
     §7 All 6 types enriched + comprehensive comparison table (§7.7)
     §11 +By-Product-Scale × love types (§11.5)
     §13 +18 new 🟡 claims, +5 new 🔴 predictions, +4 new questions
     §14 REWRITE — 4 categories, ~35 deps, changelog

   GLOBAL: SPM v3.1 throughout, all dep versions updated
   BACKUP: Research/backup/Love-Unified-v1.2-backup.md
```

---

### C6. Background-Pattern v1.1 → v2.0 [REWRITE] ✅ DONE

```
✅ DONE (2026-05-22): Background-Pattern.md v2.0 REWRITTEN
   VỊ TRÍ:   Core-Deep-Dive/Body-Base/Chunk/
   ~2,500 dòng (was 1,382L v1.1), 20 sections (was 15), ~30 deps (was ~12), ~35 citations (was ~19)
   Backup: backup/Background-Pattern-v1.1-backup.md

   5 NEW SECTIONS:
     §9  BP × Valence System (Structural/Current, Hw Subsidy, Tonic = substrate, Mode 1)
     §10 BP × Entity-Compiled (trait-level = BP, Formation × BP, Dunbar S1-S6 × BP)
     §11 BP × Entity-Access + Calibration (Mức 0-5, Exit Cost, Calibration Bias, Mức 4 critical)
     §12 BP × Bond-Architecture (per-bond integration depth, parent = deepest, anti-suppress)
     §13 BP × Boredom (compiled environment, gap direction resist)

   KEY ENRICHMENTS:
     §0  +TIỀN ĐỀ ĐỌC (8 items), +ĐỌC FLOW v2.0, +SCOPE IN/OUT
     §1  +Structural Valence context (§1.3), +State/Trait distinction (§1.4)
     §2  +Pattern Shiftability mapping (§2.5, PFC-Ops §7)
     §3  +Hw Subsidy × formation speed (§3.3), +Satiation Type × BP channels (§3.4)
     §5  +PFC-Ops integration: compiled suppress absorb (⑥), PFC Budget (⑦)
     §6  ★ REWRITE: Triple Bias (Retrieval+Template+Interpretation, SPM v3.1 §9)
     §7  +3 Firing Modes × BP (Mode 1=BUILD, Mode 2=EXPOSE, Mode 3=TRIGGER)
     §8  +Compiled Suppress absorbed pathway (§8.2, PFC-Ops §8+§11)
     §17 +4 new questions (Q7-Q10)
     §18 +20 new 🟡 claims, +15 new 🟢 citations
     §19 REWRITE: 5 categories, ~30 deps, ~35 citations

   GLOBAL: SPM v3.1 (Match→Modeling), VP v1.2→v3.0, all dep versions updated
```

---

### C7. Gap-Distribution-Profile v1.0 → v1.1 [DEEP REFINE] ✅ DONE

```
✅ DONE (2026-05-22): Gap-Distribution-Profile.md v1.1 (~2,370L, +508L over v1.0)
VỊ TRÍ:   Core-Deep-Dive/Body-Base/Body-Feedback/
SOURCE:    Gap-Body-Need v1.0 (T6) + PFC-Operations v1.0 (A1)

CONTENT v1.1 (DEEP REFINE over v1.0):
  §0 ENRICHED: +TIỀN ĐỀ ĐỌC (6 items), +framework gaps resolved (8 items), +GBN+PFC-Ops in file table
  §1 ENRICHED: +§1.4 5-Parameter per-gap cross-ref (P1-P5 aggregate view, P4/P5 decouple)
  §2 ENRICHED: +§2.2 Chain-length × spectrum table (P4 chain, compilation over development)
               +§2.5 Satiation Type × domain (Cyclic/Tonic/Generative per-domain, compound, "chán nhau")
  §3 ENRICHED: +§3.2 Compiled Quality × Origin (genuine/schema/threat tag, "giỏi nhưng ghét")
               +§3.4 Pattern Shiftability × Stability (4 quadrants, Density > Depth, B vs C)
  §4 ENRICHED: +§4.5 ENGINE/ROAD/VEHICLE architecture (collective = infrastructure, specialization trade-off)
  §6 ENRICHED: +§6.4 3 Outcomes A/B/C (genuine/suppress/failure, escalation, 7 factors, 6-step reversal)
               +§6.5 PFC Budget constraint (~4±1 concurrent, parent-child highest cost)
  §7 ENRICHED: +§7.4 Technology × Modern Gap Frontier (fill table, Kahneman-Deaton, frontier mismatch)
  §10 ENRICHED: 9→13 research anchors (+Kahneman-Deaton 2010, +Weber-Fechner)
  §11 ENRICHED: +8 new 🟡 claims, +2 new 🔴 hypotheses
  §12 ENRICHED: Q3+Q4 enriched with Technology fill + PFC Budget context
  §13 ENRICHED: +7 new deps (GBN, PFC-Ops, VP, SPM, in 5 categories)
  GLOBAL: All dep versions updated (BP v2.0, BPGR v1.4, Connection v5.0, SPM v3.1)
  Structure KEPT: 13 sections, 4-trục, 4-tầng model preserved
```

---

### C8. Agent-Mechanism v2.0 → v2.1 [REFINE] ✅ DONE (2026-05-22)

```
✅ DONE: Agent-Mechanism.md v2.1 REFINED (2026-05-22)
VỊ TRÍ:    Core-Deep-Dive/Body-Base/Chunk/Agent-Mechanism/
THAY ĐỔI:  v2.0 (1,957L) → v2.1 (~2,362L, +405L, +21%)
BACKUP:     backup/Agent-Mechanism-v2.0-backup.md

CONTENT:
  SPM rename: 23 occurrences Match→Modeling
  §0.1 +SE context (SPM = Application 1 trên 1 Engine)
  §0.3 +12 new accepted items (SE, EA, EC, Compiled Quality, etc.)
  §0.5 ★ NEW: v2.1 changes table
  §1 REWRITE: reading flow (3→11 files, 6 entry paths)
  §2.4 +EA Mức 0-5 formal gradient model
  §3.3 ★ NEW: Simulation Engine context (1 Engine × 3 Components × 3 Axes)
  §5.7 ★ NEW: Compiled Quality effect on SPM
  §6.8-6.11 ★ NEW: Bond-Architecture, Resonance-Sustainability, By-Product-Scale, Resonance-Per-Entity previews
  §7.5 +quality modifiers table (Compiled Quality, HW Subsidy, EA, PFC Budget)
  §9.1 +EA Mức column in gradient table
  §12.7-12.9 ★ NEW: 3 Satiation Types, ENGINE/ROAD/VEHICLE, Phantom × agent loss
  §14.10-14.11 ★ NEW: EA-Excess + Compiled Suppress failure modes
  §17 REWRITE: 28-session plan status
  §19 +8 🟢 + 13 🟡 items
  §20 REWRITE: 6 categories, 30+ files, 45+ citations
  YAML: 16→30+ deps organized 6 categories

DEPENDENCIES: ALL Phase A+B+T+C1-C7 integrated.
CITATIONS: 45+ (was 28+).
```

---

### C9. Coordination-Node v1.1 → v1.2 + Collective-Body v2.0 → v2.1 [LIGHT REFINE]

✅ **DONE** (2026-05-23)

```
Coordination-Node v1.2 (~2,210L, +226L, +11%):
  → §1.4 ★ NEW: Prestige = genuine resonance (opioid), Dominance = forced resonance (relief)
  → §2.5 ★ NEW: Mẹ = first coordination node (5 capabilities, dual nature VEHICLE+ROAD)
  → §9.4 ★ NEW: Hardware Subsidy Per Scale (oxytocin→serotonin→trust infrastructure)
  → §10.1: +4 🟡 items. §11: +Agent-Mechanism files category, ALL versions updated
  → GLOBAL: SPM rename Match→Modeling (5 occ), deps organized 4 categories
  → Backup: backup/Coordination-Node-v1.1-backup.md

Collective-Body v2.1 (~1,779L, +126L, +8%):
  → §3.1 ENRICHED: By-product match L3 institutional framing (3-level table, 4 differences)
  → §8.5 ★ NEW: Technology × Scale interaction (ROUTINE→GENUINE, income plateau evidence)
  → §9: +3 🟡 items. §10: ALL versions updated, +BS v1.0, +GDP v1.1, +CN v1.2
  → GLOBAL: SPM rename Match→Modeling (2 occ), deps organized 4 categories
  → Backup: backup/Collective-Body-v2.0-backup.md

COMBINED: +352L across 2 files. PHASE C COMPLETE (26/28).
```

---

## §4 — PHASE D: RENAME + VERIFY (2 sessions)

---

### D1. SPM Rename Propagation — ✅ DONE (2026-05-23)

```
Self-Pattern-Match → Self-Pattern-Modeling
ACTUAL: 95 active files, ~300+ occurrences renamed
Abbreviation SPM KHÔNG ĐỔI

COMPLETED:
  ① Bulk rename: 95 files × replace "Self-Pattern-Match" → "Self-Pattern-Modeling"
  ② Excluded: backup/ files (73 files), Self-Pattern-Modeling.md (9 historical), plan file (6 about-rename)
  ③ Post-fix: 7 changelog entries restored (Match → Modeling transition refs)
  ④ 2 drill files: "Rename pending" → "✅ Renamed" (Drill-SPM-Mechanism, Drill-SPM-Substrate)
  ⑤ Verify: 0 broken entries, all remaining "Self-Pattern-Match" = intentional historical refs

REMAINING "Self-Pattern-Match" (intentional):
  - Self-Pattern-Modeling.md: 9 (YAML backup paths + changelog)
  - plan-drill-framework-propagation.md: 6 (D1 scope description)
  - 6 other files: 1-2 each (changelog "Match → Modeling" entries)
  - backup/ files: 73 (untouched per plan)
```

---

### D2. File-Index + Verification — ✅ DONE (2026-05-23)

```
✅ DONE 2026-05-23

① 01-File-Index.md UPDATES (3 index files):
  Core-Deep-Dive/01-File-Index.md:
    + 9 NEW entries added: Entity-Access-Excess, Entity-Access-Calibration,
      Bond-Architecture, Resonance-Sustainability, By-Product-Scale,
      Resonance-Per-Entity, PFC-Label, Gap-Body-Need, Hidden-Quality-Perception
    + 10 entries UPDATED: Empathy v4.0, Connection v5.0, Body-Coupling v3.0,
      Background-Pattern v2.0, GDP v1.1, BPGR v1.4, Entity-Access v1.2,
      Agent-Mechanism v2.1, Coordination-Node v1.2, Collective-Body v2.1
    + Header updated (2026-05-23, D2 complete)
  Research/01-File-Index.md:
    + 2 entries UPDATED: Love-Romantic v3.0, Love-Unified v2.0
    + Header updated (2026-05-23)
  Applications/01-File-Index.md: No changes needed

② PFC-Hold-Dimensions.md v1.1: SKIPPED (lower priority, no urgent need)

③ Verification pass ✅:
  + "Self-Pattern-Match" in active files: CLEAN (only changelog/historical refs)
  + "Entity-Owned" usage: CLEAN (all correctly used as PFC label / observation lens)
  + Cross-refs spot-checked: Connection v5.0 ← Bond-Architecture §3-§5 ✅
    Love-Romantic v3.0 ← Resonance-Per-Entity v1.0 ✅
  + SPM v3.1 terminology: consistent throughout active files
```

---

## §5 — ORDERED SESSION LIST

```
═══════════════════════════════════════════════════════════════
#   FILE                           ACTION    EST. LINES   SESSION
═══════════════════════════════════════════════════════════════

PHASE A — NEW FILES (✅ DONE)
───────────────────────────────────────────────────────────────
 1  PFC-Operations.md              NEW       ~1,200       Session 1  ✅
 2  Simulation-Engine.md           NEW       ~900         Session 2  ✅
 3  Entity-Compiled.md             NEW       ~1,300       Session 3  ✅
 4  Entity-Access.md               NEW       ~1,800       Session 4  ✅

PHASE B — REWRITES (✅ DONE)
───────────────────────────────────────────────────────────────
 5  Imagine-Final.md               REWRITE   ~1,500       Session 5  ✅
 6  Self-Pattern-Modeling.md       REWRITE   ~2,000       Session 6  ✅
 7  By-Product-Gap-Resonance.md    REWRITE   ~1,800       Session 7  ✅
 8  Boredom.md                     REWRITE   ~1,200       Session 8  ✅
 9  Valence-Propagation.md         REWRITE   ~2,000       Session 9  ✅

PHASE T — TÁCH + MỚI
───────────────────────────────────────────────────────────────
10  PFC-Label.md                   MỚI       ~800         Session 10
11  Entity-Access-Excess.md        TÁCH      ~1,200       Session 11
12  Entity-Access-Calibration.md   TÁCH      ~900         Session 12
13  Bond-Architecture.md           TÁCH      ~800         Session 13
14  Resonance-Sustainability.md    TÁCH      ~1,000       Session 14
15  By-Product-Scale.md            TÁCH      ~600         Session 15
16  Gap-Body-Need.md               MỚI       ~1,100       Session 16
17  Resonance-Per-Entity.md        MỚI       ~1,000       Session 17

PHASE C — REWRITE (C1-C6) + REFINE (C7-C9)
───────────────────────────────────────────────────────────────
18  Connection.md                  REWRITE   ~2,500       Session 18
19  Empathy.md                     REWRITE   ~2,400       Session 19
20  Body-Coupling.md               REWRITE   ~2,200       Session 20
21  Love-Romantic.md               REWRITE   ~2,600       Session 21
22  Love-Unified.md                REWRITE   ~1,600       Session 22
23  Background-Pattern.md          REWRITE   ~1,500       Session 23
24  Gap-Distribution-Profile.md    DEEP REF  +300~500     Session 24
25  Agent-Mechanism.md             REFINE    +100~200     Session 25
26  Coord-Node + Collective-Body   LIGHT REF +100~200     Session 26

PHASE D — RENAME + VERIFY
───────────────────────────────────────────────────────────────
27  SPM Rename (~70 files)         RENAME    mechanical   Session 27 ✅
28  File-Index + Verify            VERIFY    —            Session 28 ✅
═══════════════════════════════════════════════════════════════

TOTAL: 28 sessions — ✅✅ ALL COMPLETE (2026-05-22 ~ 2026-05-23)
NEW CONTENT: ~27,000-31,000 lines estimated → ACTUAL ~35,000+ lines
FILES TOUCHED: ~100+ → ACTUAL ~130+ files
```

---

## §6 — NGUYÊN TẮC KHI TRIỂN KHAI

```
① MỖI SESSION: đọc plan → đọc drill source → đọc file hiện tại → implement → update plan
② QUALITY > BREVITY: chấp nhận DÀI nếu chi tiết quan trọng
③ 100% RESEARCH CITATIONS GIỮ NGUYÊN: không bao giờ bỏ citation
④ VÍ DỤ SIGNATURE GIỮ NGUYÊN: ví dụ đặc trưng = identity
⑤ HONEST ASSESSMENT UPDATE: mỗi rewrite phải reflect v_new
⑥ BIAS PREVENTION: dùng Over-SPM-Clarification §9 khi nào có "over-clone"
⑦ C1-C6 UPGRADED TO REWRITE (2026-05-22): rà soát thấy deps outdated + Phase A+B chưa integrated → rewrite cho đồng bộ
⑧ PHASE T ADDED (2026-05-22): rà soát drill → 7 file cần tách/mới. Tách rõ ràng > merge gọn. Chất lượng quan sát > tiện lợi.
⑨ TÁCH SESSION: tạo file mới + trim file gốc (§→cross-ref) trong cùng 1 session
⑩ SKIP DRILLS: PR-Definition, SPM-Self-Shared-Substrate, Over-SPM-Clarification = đã hết nhiệm vụ (definition/evidence). PFC-Label → formalize thành T0.
⑪ UPDATE PLAN: mỗi session xong → update progress trong file này
```

---

## §7 — NOTES

```
① Drill-Over-SPM-Clarification.md nằm trong backup/ folder
   → Dùng làm REFERENCE khi propagate. Không cần move.
   → Path: Drill-Inter-Body-Mechanism/backup/Drill-Over-SPM-Clarification.md

② outline-Love-Romantic-Paradox.md ĐÃ ở backup/
   → Đã hoàn thành nhiệm vụ (tạo Entity-Owned-Excess concept)

③ AI-Schema-Detection-update-draft.md = OUTLINE cho future update
   → Chờ collective files mature. KHÔNG trong scope plan này.

④ Satiation types (Cyclic/Tonic/Generative) = terminology MỚI
   → Chưa tồn tại trong framework. Propagate qua B5 (VP), C7 (GDP).

⑤ ENGINE/ROAD/VEHICLE = architectural metaphor MỚI
   → Propagate qua C7 (GDP) cross-ref.

⑥ Entity-Access gradient THAY THẾ Entity-Owned binary
   → Entity-Owned trở thành PFC lens cho Mức 4-5
   → VP, Body-Coupling, Love files sẽ được update terminology

⑦ plan-drill-propagation.md (cũ) VẪN GIỮ làm reference
   → File này (plan-drill-framework-propagation.md) SUPERSEDES nó
```

---

## §8 — PROGRESS TRACKING

```
PHASE A — NEW FILES
  ✅ A1. PFC-Operations.md v1.0 (2026-05-22, ~1,200L, 30 citations)
  ✅ A2. Simulation-Engine.md v1.0 (2026-05-22, ~900L, 27 citations)
  ✅ A3. Entity-Compiled.md v1.0 (2026-05-22, ~1,231L, 67 citations)
  ✅ A4. Entity-Access.md v1.0 (2026-05-22, ~1,500L, 73 citations)

PHASE B — REWRITES
  ✅ B1. Imagine-Final.md v3.0 (2026-05-22, ~1,515L, 44 citations, v2→v3 boundary reframe: hardware prediction ≠ IF)
  ✅ B2. Self-Pattern-Modeling.md v3.1 (2026-05-22, ~1,533L, 57 citations, RENAME Match→Modeling)
  ✅ B3. By-Product-Gap-Resonance.md v1.1 (2026-05-22, ~1,665L, 65+ citations, absorb 5 drills ~78 insights)
  ✅ B4. Boredom.md v2.0 (2026-05-22, ~1,300L, 19 citations, 16 drill insights, source ⑥ + M1-M4 + threshold + abundance)
  ✅ B5. Valence-Propagation.md v3.0 (2026-05-22, ~1,988L, 55 citations, 28 drill insights, Structural/Current + 3 Firing Modes + Hardware Subsidy + Satiation Type + Mixed Valence + "Xa mẹ" + Per-entity dynamics + Phantom + Technology)

PHASE T — TÁCH + MỚI
  ✅ T0. PFC-Label.md v1.0 (2026-05-22, ~1,142L, 24 citations, 17 sections, vocabulary standard, companion BFL)
  ✅ T1. Entity-Access-Excess.md v1.0 (2026-05-22, ~1,121L, 65 citations, 36 drill insights, EA v1.1 trimmed §6+§7)
  ✅ T2. Entity-Access-Calibration.md v1.0 (2026-05-22, ~1,073L, 25 citations, 16 sections, EA v1.2 trimmed §8)
  ✅ T3. Bond-Architecture.md v1.0 (2026-05-22, ~1,183L, 28 citations, 14 sections, BPGR v1.2 trimmed §9+§10)
  ✅ T4. Resonance-Sustainability.md v1.0 [TÁCH] — ~1,355L, 32 citations, 19 sections, BPGR v1.3
  ✅ T5. By-Product-Scale.md v1.0 (2026-05-22, ~905L, 15 citations, 16 sections, BPGR v1.4 trimmed §13)
  ✅ T6. Gap-Body-Need.md v1.0 (2026-05-22, ~1,388L, 33 citations, 19 sections, 4 cases)
  ✅ T7. Resonance-Per-Entity.md v1.0 (2026-05-22, ~1,606L, 33 citations, 20 sections, 4 cases)

PHASE C — REWRITE (C1-C6) + REFINE (C7-C9) — reference ALL Phase A+B+T
  ✅ C1. Connection v5.0 (2026-05-22, ~3,072L, 43+ citations, 21 sections + §4.5+§4.6+§7.2 NEW)
  ✅ C2. Empathy v4.0 [REWRITE] — ~2,895L, 25 deps, 35+ citations (2026-05-22)
  ✅ C3. Body-Coupling v3.0 [REWRITE] — ~2,883L, 27 deps, 45+ citations (2026-05-22)
  ✅ C4. Love-Romantic v3.0 [REWRITE] — ~3,287L, ~36 deps, 50+ citations (2026-05-22)
  ✅ C5. Love-Unified v2.0 [REWRITE] — ~2,532L, ~35 deps, 50+ citations, 6 NEW sections (§4-§6, §8-§10), comprehensive comparison table
  ✅ C6. Background-Pattern v2.0 [REWRITE] — ~2,500L, 20 sections, ~35 citations, 5 NEW sections
  ✅ C7. Gap-Distribution-Profile v1.1 [DEEP REFINE] — + T6 gap-body-need + A1 PFC-Ops
  ✅ C8. Agent-Mechanism v2.1 [REFINE] — 2,362L, +405L, 45+ citations (2026-05-22)
  ✅ C9. Coordination-Node v1.2 + Collective-Body v2.1 [LIGHT REFINE] — + T5 scale (2026-05-23)

PHASE D — RENAME + VERIFY
  ✅ D1. SPM Rename (95 files, ~300+ occ, 2026-05-23)
  ✅ D2. File-Index + Verify (3 indexes, +9 entries, 12 updates, verification pass, 2026-05-23)
```

---

**Created**: 2026-05-22
**Last updated**: 2026-05-23
**Status**: ✅✅ COMPLETE — 28/28 sessions done. ALL PHASES COMPLETE (A+B+T+C+D).
  Phase T added (2026-05-22): 8 tách/mới files (incl. T0 PFC-Label vocabulary standard).
  3 drills SKIP (PR-Definition, Over-SPM-Clarification, SPM-Self-Shared-Substrate).
  ✅ T0 PFC-Label.md v1.0 (2026-05-22, ~1,142L, 24 citations, 17 sections)
  ✅ T1 Entity-Access-Excess.md v1.0 (2026-05-22, ~1,121L, 65 citations, EA v1.1)
  ✅ T2 Entity-Access-Calibration.md v1.0 (2026-05-22, ~1,073L, 25 citations, EA v1.2)
  ✅ T3 Bond-Architecture.md v1.0 (2026-05-22, ~1,183L, 28 citations, 14 sections, BPGR v1.2)
  ✅ T4 Resonance-Sustainability.md v1.0 (2026-05-22, ~1,355L, 32 citations, 19 sections, BPGR v1.3)
  ✅ T5 By-Product-Scale.md v1.0 (2026-05-22, ~905L, 15 citations, 16 sections, BPGR v1.4)
  ✅ T6 Gap-Body-Need.md v1.0 (2026-05-22, ~1,388L, 33 citations, 19 sections, 4 cases)
  ✅ T7 Resonance-Per-Entity.md v1.0 (2026-05-22, ~1,606L, 33 citations, 20 sections, 4 cases)
  NEXT: Session 19 = C2 Empathy v3.0 → v4.0 [REWRITE]
