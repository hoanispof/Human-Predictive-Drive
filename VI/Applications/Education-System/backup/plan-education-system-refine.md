# Plan: Education-System Folder Refine (Tầng 4 + Tầng 5)

> **Created:** 2026-05-25
> **Scope:** 8 active files (8,290L total) → ~9,700-10,300L target
> **Approach:** Mỗi session = 1 file. Chậm mà chắc. Chất lượng nội dung là ưu tiên số 1.
> **Context:** Post Phase A/B/T/C drills + Education-Mechanism/ folder refine DONE.
> ~25 new concepts cần propagate vào Tầng 4 + Tầng 5.
> **Predecessor:** plan-education-mechanism-refine.md (P1-P7 ALL DONE)

---

## Bối cảnh — Tại sao cần refine

```
Tất cả 8 files đã rewrite v2.0 (2026-05-11) — re-based từ "10 NL".
NHƯNG: Drill phases (2026-05-16 → 2026-05-25) tạo ~25 new concepts.
  + Education-Mechanism/ (Tầng 3) vừa refine xong (P1-P7)
  + Child-Dev/ (Tầng 2) cũng refine xong
  → Tầng 4 + Tầng 5 chưa update → LAGGING BEHIND

Files NÀY = APPLICATION files (Tầng 4+5):
  → KHÔNG cần giải thích mechanism sâu (đó là việc Tầng 1-3)
  → CẦN correctly APPLY new concepts vào application domain
  → CẦN update version refs, cross-refs, structural changes
```

---

## Kiến trúc hiện tại → Kiến trúc mới

```
HIỆN TẠI (8,290L, 8 files):                MỚI (~9,500-10,000L, 8 files):

Education-System/                           Education-System/
├── Education-System.md     (1,554L)        ├── Education-System.md     v3.0 REWRITE (~1,800-2,000L)
├── Hardware-Calibration.md (1,538L)        ├── Hardware-Calibration.md  v1.1 (~1,650L)
├── Curriculum-Framework.md (754L)          ├── Curriculum-Framework.md  v2.1 (~830L)
├── Era-Analysis-2025.md    (724L)          ├── Era-Analysis-2025.md     v2.1 (~790L)
├── 00_Overview.md          (363L)          ├── 00_Overview.md           v2.1 (~380L)
└── Country/VN/                             └── Country/VN/
    ├── VN-Education-Status.md  (1,406L)        ├── VN-Education-Status.md  v2.1 (~1,500L)
    ├── VN-Cultural-Factors.md  (1,143L)        ├── VN-Cultural-Factors.md  v2.1 (~1,230L)
    └── VN-Recommendations.md  (808L)           └── VN-Recommendations.md   v2.1 (~870L)
```

---

## Shared GAPs — ẢNH HƯỞNG TẤT CẢ FILES

### S1. Dependency version bumps (ALL files)

```
File referenced              Cũ        Mới          Impact
──────────────────────────── ────────  ────────────  ──────
Education-Mechanism.md       v1.0      v2.0          CRITICAL
Domain-Knowledge-Map.md     v1.0      v2.0          CRITICAL
Connection.md                v3.1      v5.0          HIGH
Agent-Mechanism.md           v1.0      v2.1          HIGH
Child-Dev-Mechanism.md       v1.0      v2.1          MEDIUM
Education-Arms-Race.md       v1.2      v1.3          LOW
Empathy-Education.md v2.0    active    → backup!     CRITICAL
  → REPLACED BY: Connection-Education.md v1.0 (NEW)
```

### S2. Structural changes

```
① "bộ đôi" (Mechanism + Domain-Knowledge-Map) → "bộ 3" (+ Connection-Education)
② Empathy-Education.md → backup/ → replaced by Connection-Education.md v1.0
③ Tầng 3 Observation/ files:
     WAS: Education-Arms-Race + Empathy-Education
     NOW: Education-Arms-Race + Connection-Education + Money-Education
④ Self-Pattern-Modeling Compiled → Self-Pattern-Modeling v3.1 (Match→Modeling rename)
⑤ Body-Feedback-Mechanism → v2.0 (3 dynamics)
```

### S3. New concepts HOÀN TOÀN VẮNG MẶT

```
CRITICAL (affect system design):
  - Hardware Subsidy (Valence-Propagation v3.0 §7): teacher=MODERATE, parent=MAX, AI=NONE
  - PFC Budget: arc design constraint, delivery pacing
  - Compiled Quality Dimension: genuine/schema/threat compile quality
  - Gap-Distribution-Profile v1.1: curriculum = gap landscape shaping

HIGH (affect roles + relationships):
  - Entity-Access v1.2: teacher-student relationship gradient Mức 0-5
  - Entity-Compiled v1.0: teacher becomes compiled entity (40→200h)
  - Dissonance-Signal-Architecture v1.0: Evaluative/Direct-State dissonance
  - Connection-Education.md v1.0: replaces Empathy-Education

MEDIUM (enrich specific sections):
  - Coordination-Node v1.2: school/teacher as coordination node
  - M1-M4 Resonance Decline: engagement decay in education
  - 4-Layer Sustainability: educational relationship sustainability
  - Simulation-Engine v1.0: AI model refinement
  - Imagine-Final v3.0: boundary reframe (hardware prediction ≠ Imagine-Final)

LOW (reference-level in Tầng 4):
  - Bond-Architecture v1.0, Phantom 4-factor, Boredom v2.0
  - Gap Direction, Pattern Shiftability, Triple Bias
  - 3 Satiation Types, 3 Firing Modes, Valence-Propagation v3.0
```

### S4. ENGINE/ROAD/VEHICLE integration (Option B)

```
Gap-Body-Need v1.0 §9:
  Hardware = ENGINE (source of ALL drives)
  Collective-Arc = ROAD (infrastructure to fill)
  Compilation = VEHICLE (individual's compiled chains, 15-20 năm)

CONFLICT: Education-System.md §0 ĐANG dùng ENGINE/FUEL/VEHICLE cho FILE architecture:
  Mechanism = ENGINE, Domain Map = FUEL, File này = VEHICLE DESIGN
  → Cần RECONCILE: 2 tầng abstraction khác nhau

Integration approach:
  → Weave ENGINE/ROAD/VEHICLE (human architecture) as LENS xuyên suốt
  → Education SYSTEM = part of ROAD (collective-arc infrastructure)
  → Student = ENGINE (hardware drives) + VEHICLE under construction
  → §0: reconcile 2 metaphors
  → §1-§4: stages = 4 giai đoạn build VEHICLE trên ROAD
  → §7-§8: teacher = ROAD GUIDE, parent = SAFE GARAGE
  → §10: constraints = ROAD LIMITATIONS
```

---

## Phase P1: Education-System.md — FULL REWRITE

> **Action:** v2.0 → v3.0 REWRITE (1,554L → ~1,800-2,000L)
> **Status:** NOT STARTED
> **Priority:** Highest — ANCHOR file, mọi file khác phụ thuộc
> **Approach:** Move v2.0 → backup/v2.0/. Write NEW from scratch.
> v2.0 content = REFERENCE (absorb best parts), không phải base để patch.

### Tại sao REWRITE thay vì REFINE

```
v2.0 (2026-05-11) có 5 Critical + 5 Major + 8 Moderate GAPs:
  → Patch 20+ chỗ = patchwork, coherence kém
  → ENGINE/ROAD/VEHICLE cần weave XUYÊN SUỐT từ §0 — không thể graft vào
  → 25 new concepts cần ORGANIC integration, không phải 🟡 blocks chèn vào
  → v2.0 dùng ENGINE/FUEL/VEHICLE cho file architecture → CONFLICT với
    Gap-Body-Need ENGINE/ROAD/VEHICLE → reconcile = rewrite §0-§1
  → v2.0 đã re-based tốt (10 NL → 8 nguyên lý) → content logic vẫn valid
    → REWRITE = keep structure + logic, rebuild WITH new concepts integrated

REWRITE ≠ viết lại từ zero:
  → v2.0 structure (13 sections, 4 stages, 5 roles) = PROVEN → KEEP
  → v2.0 content logic = VALID → ABSORB best parts
  → REWRITE = rebuild trên CÙNG architecture nhưng VỚI new concepts WOVEN IN
  → Khác REFINE: concepts không phải "thêm vào" mà "built into"
```

### Backup step

```
TRƯỚC KHI viết:
  1. Copy Education-System.md → backup/v2.0/Education-System.md
  2. Verify backup exists
  3. Then write new v3.0
```

### Scope đề xuất — v3.0

```
Education-System.md v3.0 — Hệ Thống Giáo Dục Tối Ưu

STRUCTURE GIỮ NGUYÊN (13 sections, proven):
  §0 — Mục đích + Imagine-Final
       REWRITE: ENGINE/ROAD/VEHICLE frame từ đầu
       Education = ROAD DESIGN + help build VEHICLE
       "bộ 3" (Mechanism + Domain-Knowledge-Map + Connection-Education)
       Gap-Distribution-Profile: education = gap landscape shaping

  §1 — Kiến trúc hệ thống tổng quan
       REWRITE: 4 stages = 4 giai đoạn build VEHICLE trên ROAD
       School = Coordination-Node per community
       5 roles + Hardware Subsidy spectrum per role

  §2 — Stage 2: Foundation Chunking (6-12)
       ABSORB v2.0 + INTEGRATE:
       +PFC Budget constraint (40-70%)
       +Compiled Quality Dimension (approach-tagged → genuine compile)
       +Hardware Subsidy (teacher MODERATE, parent MAX)
       +Gap-Distribution-Profile (diverse roads exposure)

  §3 — Stage 3: Depth + Identity (12-18)
       ABSORB v2.0 + INTEGRATE:
       +Entity-Compiled (teacher becomes compiled, departure = grief)
       +Entity-Access (teacher Mức 2-3 → mentor progression)
       +Dissonance-Signal-Architecture (identity crisis = Evaluative + Direct-State compound)
       +Imagine-Final v3.0 (boundary: hardware prediction ≠ Imagine-Final)
       +M1-M4 engagement decay, Boredom v2.0
       +PFC Budget expanding → abstract NOW accessible

  §4 — Stage 4: Specialization + Contribution (18-25+)
       ABSORB v2.0 + INTEGRATE:
       +ENGINE/ROAD/VEHICLE: specialization = deep VEHICLE on 1 ROAD
       +Specialization trade-off (fragile individually, powerful collectively)
       +Gap-Distribution-Profile (credential = gap homogenization)
       +Emergence Phase enriched (ENGINE running, VEHICLE chưa có)

  §5 — Bridge strategy tổng hợp
       ABSORB v2.0 + INTEGRATE:
       +Hardware Subsidy = WHY approach-bridge works
       +Compiled Quality Dimension (wrong bridge → threat-compiled)
       +Dissonance-Signal-Architecture (wrong bridge = Evaluative Dissonance compiled)
       +M1-M4 bridge inflation spiral
       +PFC Budget in bridge dosage

  §6 — Assessment design
       ABSORB v2.0 + INTEGRATE:
       +Compiled Quality Dimension (assess QUALITY not just depth)
       +PFC Budget (assessment = PFC cost → session design)

  §7 — Vai trò Teacher/Mentor
       ABSORB v2.0 + INTEGRATE:
       +Hardware Subsidy MODERATE (teacher subsidy quality matters)
       +Entity-Access gradient (Mức 2-3 per stage)
       +Entity-Compiled (teacher = compiled entity, 40→200h)
       +Coordination-Node (teacher = node per class)
       +4-Layer Sustainability (teacher-student relationship)
       +Bond-Architecture (teacher bond type)

  §8 — Vai trò Parent/Family
       ABSORB v2.0 + INTEGRATE:
       +Hardware Subsidy MAX (oxytocin, baby schema)
       +Entity-Access Mức 4-5 (highest)
       +Bond-Architecture (parent bond = deepest)

  §9 — Integration: School + Family + Self-learning + AI
       ABSORB v2.0 + INTEGRATE:
       +Simulation-Engine (AI = computational Simulation-Engine)
       +Hardware Subsidy spectrum (parent MAX → teacher MOD → AI NONE)
       +Phantom 4-factor (AI relationship = phantom type)

  §10 — Constraints + Reality
       ABSORB v2.0 + INTEGRATE:
       +Gap-Distribution-Profile (one-size = homogenization)
       +Dissonance-Signal-Architecture (system change = collective dissonance)
       +ROAD limitations (some roads don't exist for some countries)

  §11 — Honest Assessment
       REWRITE with v3.0 concepts
       +new 🟡 entries for all integrated concepts

  §12 — Kết nối
       COMPLETE REWRITE — all version bumps, new files, reorganized by category
```

### Concepts woven IN (not appended)

```
XUYÊN SUỐT (lens, not block):
  - ENGINE/ROAD/VEHICLE: §0-§4 + §10 — education = ROAD + help build VEHICLE
  - Hardware Subsidy: §5, §7-§9 — per-role subsidy quality
  - PFC Budget: §2-§4, §6 — per-stage constraint
  - Compiled Quality Dimension: §2-§6 — genuine/schema/threat
  - Gap-Distribution-Profile: §0, §2-§4, §10 — gap landscape shaping

PER-SECTION (targeted):
  - Entity-Access: §7-§8 (teacher/parent Entity-Access gradient)
  - Entity-Compiled: §7 (teacher = compiled entity)
  - Dissonance-Signal-Architecture: §3, §5, §10 (identity crisis, wrong bridge, system change)
  - Coordination-Node: §1, §7 (school/teacher as node)
  - M1-M4: §3, §5 (engagement decay, bridge inflation)
  - 4-Layer Sustainability: §7 (teacher-student)
  - Simulation-Engine: §9 (AI = computational Simulation-Engine)
  - Imagine-Final v3.0: §3 (boundary reframe)
  - Connection-Education: §0, §12 (replaces Empathy-Education)
  - Bond-Architecture: §7-§8 (bond types)
  - Phantom: §9 (AI phantom)
  - Boredom v2.0: §3 (M2+M4 loop)
  - Self-Pattern-Modeling v3.1: throughout
```

### Dependencies cần đọc trước khi viết

```
MUST READ (concepts cốt lõi — đọc ĐẦU session):
  - Education-System.md v2.0 TOÀN BỘ — content to absorb (REFERENCE, not base)
  - Education-Mechanism.md v2.0 §0.4 + §4 — bộ 3 architecture, Hardware Subsidy
  - Gap-Body-Need.md v1.0 §9 — ENGINE/ROAD/VEHICLE architecture
  - Connection-Education.md v1.0 §0 — position, scope
  - Valence-Propagation.md v3.0 §7 — Hardware Subsidy spectrum

SHOULD READ (enrichment):
  - Entity-Compiled.md v1.0 §3-§4 — formation timeline, departure
  - Entity-Access.md v1.2 §1-§2 — gradient Mức 0-5
  - Coordination-Node.md v1.2 §1.4 — prestige = genuine resonance
  - Gap-Distribution-Profile.md v1.1 §1-§2 — 4 trục, collective arc
  - Dissonance-Signal-Architecture.md v1.0 §1-§2 — Evaluative/Direct-State
  - PFC-Label.md v1.0 §5 — PFC Budget concept
  - Compiled-Fresh.md v2.0 §5 — Compiled Quality Dimension

CÓ THỂ ĐỌC THÊM nếu cần:
  - Simulation-Engine.md v1.0 §1-§2
  - Bond-Architecture.md v1.0 §1
  - Imagine-Final.md v3.0 §1 (boundary reframe)
  - Boredom.md v2.0 §3 (M1-M4 formula)
```

### Khi hoàn thành P1

```
  - [ ] v2.0 → backup/v2.0/Education-System.md
  - [ ] v3.0 viết mới, verified
  - [ ] Update 00_Overview.md refs (deferred → P5)
  - [ ] Review impact lên Hardware-Calibration refs (deferred → P2)
  - [ ] Review impact lên Curriculum-Framework refs (deferred → P3)
```

---

## Phase P2: Hardware-Calibration.md — MODERATE REFINE

> **Action:** v1.0 → v1.1 (1,538L → ~1,650L, +~112L)
> **Status:** NOT STARTED
> **Priority:** High — UNIQUE file, most durable

### GAPs

```
CRITICAL:
  1. Connection.md v3.1 → v5.0 (DIM 5 Social Processing source changed)
  2. Agent-Mechanism.md v1.0 → v2.1 (Self-Pattern-Modeling v3.1)
  3. +Hardware Subsidy in calibration context:
     → DIM observation INCLUDES: how student responds to subsidy
     → §3: calibrate SUBSIDY TYPE per hardware (not just content)
  4. +Compiled Quality Dimension in observation:
     → §2: observe compile QUALITY not just compile success
     → "Giỏi nhưng ghét" = threat-compiled = RED FLAG in observation

MAJOR:
  5. +Body-Feedback-Label 3-tier: §2 observation methodology enrichment
  6. +PFC Budget: §3 calibration constraint (high-PFC domains = costly)
  7. +Gap-Distribution-Profile: §3 per-individual gap landscape
  8. +Dissonance-Signal-Architecture: §5 miscalibration reframe (misread Evaluative vs Direct-State)

MODERATE:
  9. Entity-Access lens in teacher-student calibration relationship
  10. Entity-Compiled lens (teacher compiled → more accurate calibration)
  11. Self-Pattern-Modeling → v3.1 (1 mechanism × 3 dimensions)

METADATA:
  - Header: version bumps, +new deps, Connection v3.1→v5.0, changelog v1.1
  - §7 Cross-refs: complete update
```

### Dependencies cần đọc

```
  - Connection.md v5.0 §0-§1 (what changed from v3.1)
  - Valence-Propagation.md v3.0 §7 (Hardware Subsidy)
  - Compiled-Fresh.md v2.0 §5 (Compiled Quality Dimension)
  - Body-Feedback-Label.md v2.0 §1-§3 (3-tier precision)
```

---

## Phase P3: Curriculum-Framework.md — DEEP REFINE

> **Action:** v2.0 → v2.1 (754L → 990L, +236L)
> **Status:** ✅ DONE (DEEP REFINE — ENGINE/ROAD/VEHICLE xuyên suốt, +Connection-Education WHO, +Compiled Quality, +PFC Budget, +Gap-Distribution-Profile, +Dissonance-Signal-Architecture, cross-refs rewrite)
> **Priority:** Medium

### GAPs

```
CRITICAL:
  1. Empathy-Education → Connection-Education (§6 cross-refs, §0 "bộ 3")
  2. +Gap-Distribution-Profile: curriculum design = gap landscape shaping
     → §0: curriculum decides WHICH gaps form at population level
     → §5 "Cái cần bỏ": overload = gap homogenization

MAJOR:
  3. +PFC Budget: §2 Foundation Matrix depth targets need PFC cost awareness
  4. +Hardware Subsidy: §0 curriculum as subsidy vehicle
  5. +Compiled Quality Dimension: depth levels + quality (genuine/schema/threat)
  6. +Dissonance-Signal-Architecture: §5 curriculum overload = Evaluative + Direct-State compound

MODERATE:
  7. Domain-Knowledge-Map v1.0 → v2.0 refs
  8. Education-Mechanism v1.0 → v2.0 refs
  9. Education-Arms-Race v1.2 → v1.3
  10. Self-Pattern-Modeling rename

METADATA:
  - YAML header: version bumps, +new deps, changelog
  - §6 Cross-refs: complete update
```

---

## Phase P4: Era-Analysis-2025.md — LIGHT REFINE

> **Action:** v2.0 → v2.1 (724L → ~815L, +~91L)
> **Status:** ✅ DONE (LIGHT REFINE — +ENGINE/ROAD/VEHICLE alignment, +Simulation-Engine, +Phantom ⑦, +Gap-Distribution-Profile, +Hardware Subsidy, +Connection-Education, Self-Pattern-Modeling rename, all versions updated)
> **Priority:** Medium-Low (era snapshot, less concept-heavy)

### GAPs

```
MAJOR:
  1. +Simulation-Engine lens: §1 AI landscape (AI = computational Simulation-Engine)
  2. +Gap-Distribution-Profile: §5 era changing gap landscape
  3. +Hardware Subsidy: §5 era changes subsidy sources (AI = NONE)
  4. +Phantom 4-factor: §4 uncertainties (AI relationships = phantom type)

MODERATE:
  5. All dep version bumps (Education-Mechanism v1.0→v2.0, etc.)
  6. Empathy-Education → Connection-Education refs
  7. Self-Pattern-Modeling rename
  8. Education-Arms-Race v1.2 → v1.3

METADATA:
  - YAML header: version bumps, +new deps, changelog
  - §6 Cross-refs: complete update
```

---

## Phase P5: 00_Overview.md — REWRITE

> **Action:** v2.0 → v2.1 (363L → 406L, +43L)
> **Status:** ✅ DONE (REWRITE — +ENGINE/ROAD/VEHICLE context, +"bộ 3" architecture, all versions/stats updated, +Tầng 1 expanded refs, +restructure history v2.1)
> **Priority:** Low (follows folder structure, quick)

### GAPs

```
  1. Tầng 3 refs completely outdated:
     - Education-Mechanism.md v1.0 → v2.0
     - Domain-Knowledge-Map.md v1.0 → v2.0
     - "Observation/ (Education-Arms-Race, Empathy-Education)"
       → "Observation/ (Education-Arms-Race, Connection-Education, Money-Education)"
  2. "bộ đôi" → "bộ 3" framing (nếu có)
  3. Statistics update (line counts changed)
  4. Version numbers throughout
  5. Tầng 1-2 refs: version bumps
  6. FLOW diagram update
  7. Reading order update
  8. Restructure history: add v2.1 entry
```

---

## Phase P6: VN-Education-Status.md — MODERATE REFINE

> **Action:** v2.0 → v2.1 (1,406L → 1,531L, +125L)
> **Status:** ✅ DONE — MODERATE REFINE. 7 new concept lenses, deps 9→24 (7 categories), all versions current, cross-refs complete rewrite
> **Priority:** Medium

### GAPs

```
  1. All dep version bumps (Education-Mechanism v1.0→v2.0, etc.)
  2. Connection-Education replaces Empathy-Education
  3. +Hardware Subsidy lens on VN education:
     → VN teacher subsidy quality assessment
     → VN parent subsidy patterns (guilt-trip = corrupted subsidy)
  4. +Gap-Distribution-Profile: VN credential system = gap homogenization
  5. +Dissonance-Signal-Architecture: VN exam pressure = chronic Evaluative + Direct-State compound
  6. +PFC Budget: VN class size (40+) = impossible per-individual PFC calibration
  7. +Compiled Quality Dimension: VN memorization = schema-compiled dominant
  8. Cross-refs: complete update
```

---

## Phase P7: VN-Cultural-Factors.md — MODERATE REFINE

> **Action:** v2.0 → v2.1 (1,143L → 1,223L, +80L)
> **Status:** ✅ DONE — MODERATE REFINE. 5 new concept lenses per-factor, deps 6→20+ (7 categories), §2 map +new concept dimensions, all versions current, cross-refs rewrite
> **Priority:** Medium

### GAPs

```
  1. All dep version bumps
  2. Connection-Education replaces Empathy-Education
  3. +Hardware Subsidy per cultural factor:
     → "Tôn sư trọng đạo" = cultural Hardware Subsidy amplifier
     → "Cha mẹ hi sinh" = subsidy MAX but risk guilt-trip corruption
  4. +Entity-Access: cultural Entity-Access patterns (teacher Mức = high authority)
  5. +Compiled Quality Dimension: cultural pressure → threat-compiled risk
  6. §2 MAP TABLE: add new concept columns nếu phù hợp
  7. Cross-refs: complete update
```

---

## Phase P8: VN-Recommendations.md — FULL REWRITE

> **Action:** v2.0 → v2.1 FULL REWRITE (808L → 957L, +149L)
> **Status:** ✅ DONE — FULL REWRITE. 12 new concept lenses woven throughout. ENGINE/ROAD/VEHICLE + "bộ 3" xuyên suốt. Dissonance-Signal-Architecture "Direct-State TRƯỚC", Hardware Subsidy quality per role, Compiled Quality genuine>schema>threat, Gap-Distribution-Profile diversification, Entity-Access gradient, Simulation-Engine, Phantom, Coordination-Node prestige>dominance, Connection-Education 5 khía cạnh, 4-Layer Sustainability, PFC Budget. Header: 7-category deps (30+ entries). Cross-refs: complete rewrite (7 categories, 30+ entries). All versions current.
> **Priority:** Medium

### GAPs

```
  1. All dep version bumps
  2. Connection-Education replaces Empathy-Education
  3. +Hardware Subsidy: recommendations for improving subsidy quality
  4. +Gap-Distribution-Profile: credential reform as gap diversification
  5. +Dissonance-Signal-Architecture: recommendations for reducing chronic compound dissonance
  6. +PFC Budget: class size recommendation qua PFC lens
  7. +Compiled Quality Dimension: shift memorization → genuine compile
  8. Recommendations RE-EVALUATE qua new concepts (not just ref update)
  9. Cross-refs: complete update
```

---

## Execution Notes

```
THỨ TỰ BẮT BUỘC:
  P1 (Education-System) TRƯỚC → vì TẤT CẢ files khác phụ thuộc
  P2-P4 có thể flexible thứ tự (independent)
  P5 (00_Overview) SAU P1-P4 (follows structure)
  P6 TRƯỚC P7-P8 (VN-Status = data, P7-P8 derive từ P6)
  P8 SAU P7 (Recommendations derive từ Cultural analysis)

NGUYÊN TẮC:
  - Mỗi session = 1 phase cho chất lượng tối đa
  - Đọc dependency files ở đầu mỗi session (cold start context)
  - New concepts = LENS enrichment (5-10L per concept per section)
  - Files giữ identity: APPLICATION files, không phải mechanism catalog
  - ENGINE/ROAD/VEHICLE = lens XUYÊN SUỐT P1, light reference P2-P8

ESTIMATED: 8 phases, ~8-10 sessions
  (P1 REWRITE có thể cần 2 sessions vì viết mới ~1,800-2,000L)
  (P3+P4 có thể gộp 1 session, P5 nhanh)
```

---

## Progress Tracker

| Phase | File | Action | Status |
|-------|------|--------|--------|
| P1 | Education-System.md | FULL REWRITE v3.0 | ✅ DONE (1,554L → 1,627L, +73L) |
| P2 | Hardware-Calibration.md | MODERATE REFINE | ✅ DONE (1,538L → 1,689L, +151L) |
| P3 | Curriculum-Framework.md | DEEP REFINE | ✅ DONE (754L → 990L, +236L) |
| P4 | Era-Analysis-2025.md | LIGHT REFINE | ✅ DONE (724L → 815L, +91L) |
| P5 | 00_Overview.md | REWRITE | ✅ DONE (363L → 406L, +43L) |
| P6 | VN-Education-Status.md | MODERATE REFINE | ✅ DONE (1,406L → 1,531L, +125L) |
| P7 | VN-Cultural-Factors.md | MODERATE REFINE | ✅ DONE (1,143L → 1,223L, +80L) |
| P8 | VN-Recommendations.md | FULL REWRITE | ✅ DONE (808L → 957L, +149L) |
