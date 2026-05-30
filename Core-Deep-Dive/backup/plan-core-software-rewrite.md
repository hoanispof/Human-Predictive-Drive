# Plan: Core-Software.md v1.0 → v2.0 — FULL REWRITE

> **Ngày tạo:** 2026-05-24
> **Session:** 6/6 (cuối cùng) trong plan-core-foundation-rewrite.md
> **File:** `Human-Predictive-Drive/Core-Software.md`
> **Vai trò:** SOFTWARE MAP — BẢN ĐỒ TRUNG TÂM của framework
> **Phương án:** VIẾT MỚI. v1.0 → backup/Core-Software-v1.0-backup.md

---

## 1. TẠI SAO VIẾT MỚI (KHÔNG update in-place)

Core-Software.md = file trung tâm nhất của framework.
- 16 version references lạc hậu (VP v1.4→v3.0, Empathy v2.0→v4.0, Connection v3.1→v5.0, ...)
- 14 concept lớn HOÀN TOÀN THIẾU (Simulation-Engine, Entity-Compiled, Entity-Access, Bond-Architecture, ...)
- Naming errors (Self-Pattern-Match → Self-Pattern-Modeling)
- Numbers outdated (13 files → 130+ files)

Update in-place = patch everywhere → chất lượng thấp, không đồng bộ.
Viết mới = tích hợp hữu cơ, đồng bộ 100% với state hiện tại.

---

## 2. CẤU TRÚC v2.0

GIỮ 13-section cycle architecture (structure ổn, đã được validate).
Nội dung VIẾT MỚI hoàn toàn cho mỗi section.

```
YAML Header — v2.0, prerequisites updated, scope expanded
§0 — BA BẢN ĐỒ + TẠI SAO CYCLE-BASED
     Giữ nguyên ý, update nhẹ language
§1 — KIẾN TRÚC CYCLE: SOFTWARE MAP
     §1.1 Ba góc nhìn (giữ)
     §1.2 Functional Cycle diagram (REWRITE: +Simulation-Engine, +Entity system, +Compiled/Fresh)
     §1.3 Hardware↔Software mapping (update)
     §1.4 Tại sao cycle, không layers (giữ)
§2 — DOMAIN
     +3 Domain Types (Reality / Abstract / Abstract-Dynamic)
     +Dual Check (body=QC, domain=arbiter)
     +3 Nguồn Constraint × shelf-life
     Condensed from v1.0 (domain detail → Domain.md v2.0)
§3 — BODY-INPUT (L0 + L1)
     Giữ nguyên ý, minor ref updates
     §3.1 L0 Alive (giữ), §3.2 17 categories (giữ), §3.3 Baseline (giữ)
§4 — UNCONSCIOUS PROCESSING ⭐ MAJOR REWRITE
     §4.1 Chunk-System — Sole Substrate
       +Entity-Compiled concept (hub-and-spoke, 40→200h)
       +Compiled Quality (genuine/schema/threat — compile-time lock)
       +Compiled/Fresh terminology update throughout
       Compile Types: giữ 3 types, update framing
       Model 3+1, Model 3 Cấp: giữ, update refs
     §4.2 Body-Feedback — Continuous Evaluation
       +RSA v2.0 (Evaluative/Direct-State, E₀→E₃)
       +3 Satiation Types (Cyclic/Tonic/Generative)
       +Hardware Subsidy (body subsidize entity processing)
       H10, Dual-Pull: giữ ý, update refs
       BFM v1.2→v2.0, GBN v1.0 integration
     §4.3 Cortisol — Amplifier
       Giữ nguyên ý, update Cortisol v2.0→v2.1
       +HPA paradox brief mention
     §4.4 Agent-Mechanism — Functions on Chunk Substrate ⭐
       RENAME from "Functions" → "Agent-Mechanism" (align với folder)
       +Simulation-Engine (1 engine, 3 components, 3 axes → ALL functions = applications)
       +Self-Pattern-Modeling v3.1 (Match→Modeling rename, Compiled/Fresh)
       +Entity-Access gradient Mức 0-5
       +Bond-Architecture (1 mechanism × 4 bonds, gap clone impossible)
       +M1-M4 Resonance Decline
       +By-Product-Scale (Pair/Hub/Institutional)
       +Resonance-Sustainability (4-Layer model)
       +Phantom 4-factor (entity loss)
       +Hardware Subsidy per entity
       Empathy v2.0→v4.0, Connection v3.1→v5.0, VP v1.4→v3.0
       Imagination → reframe as Simulation-Engine-APPLICATION-2
§5 — FEELING (Bridge Unconscious → PFC)
     +Feeling v3.0 (PFC=Lawyer integrated)
     +Compiled/Fresh framing (compiled feeling vs fresh)
     Giữ 7-layer, magnitude×clarity, temporal order
§6 — PFC (Observer + Orchestrator) ⭐ MAJOR REWRITE
     §6.1 PFC = Observer (giữ ý, update)
     §6.2 PFC Orchestrate (giữ ý, update)
     §6.3 PFC Activation (giữ ý)
     §6.4 PFC Configurations (update v1.0→v1.1)
     §6.5 NEW: Simulation-Engine (1 engine underneath ALL)
     §6.6 NEW: PFC-Operations (Hold + Suppress, Budget, Compiled Quality)
§7 — BODY-OUTPUT
     Giữ nguyên ý, minor update
§8 — OBSERVATION PARAMETERS
     Update ALL entries với current versions
     +Boredom (v2.0: unified formula, 6 sources, M1-M4)
     +Gap-Distribution-Profile mention
     Connection v3.1→v5.0 + new description
     Fix Self-Pattern-Modeling naming throughout
§9 — DEVELOPMENT TRAJECTORY
     +Compilable Architecture framing (Compilable-dominant destination)
     Giữ table, update refs
§10 — MULTIPLE TIMESCALES
     Giữ nguyên (section ổn)
§11 — KEY REFRAMES
     EXPAND: không chỉ từ v7.5 → bao gồm ALL post-drill reframes:
     +10 original (giữ) + NEW:
     11. Entity-Compiled = structural body-base integration
     12. Simulation-Engine = 1 engine, N applications
     13. PFC Budget = shared finite resource
     14. Compiled Quality = compile-time lock (genuine/schema/threat)
     15. Hardware Subsidy = body subsidize entity processing
     16. 3 Satiation Types = Cyclic/Tonic/Generative
     17. Entity-Access gradient = Mức 0-5
     18. Evaluative vs Direct-State Reward
     19. M1-M4 = 4 mechanisms resonance decline
     20. Self-Pattern-Match → Self-Pattern-Modeling (Match→Modeling)
§12 — HONEST ASSESSMENT
     §12.1 Framework provides: update numbers (130+ files, 35,000+ lines, 500+ citations)
     §12.2 Scope limits: giữ, refine
     §12.3 Open questions: review which resolved, add new
     §12.4 Number convention: giữ nguyên (ổn)
§13 — CROSS-REFERENCES
     ALL version numbers updated
     +New files from 28-session drill
     Organized by folder (Observation/ | Body-Base/ | PFC/ | Agent-Mechanism/ | Collective/ | Domain/)
```

---

## 3. PHASES TRIỂN KHAI

### Phase A: BACKUP + YAML (5 phút)
- [ ] Move v1.0 → backup/Core-Software-v1.0-backup.md
- [ ] Create new file with YAML header

### Phase B: §0-§1 Foundation + Cycle Diagram (~15%)
- [ ] §0 Ba Bản Đồ + Tại Sao Cycle-Based
- [ ] §1.1 Ba góc nhìn
- [ ] §1.2 Functional Cycle diagram (REWRITE — biggest diagram change)
- [ ] §1.3 Hardware↔Software mapping
- [ ] §1.4 Tại sao cycle

### Phase C: §2-§3 Domain + Body-Input (~10%)
- [ ] §2 Domain (+3 Types, +Dual Check, condensed)
- [ ] §3 Body-Input (minor update, keep L0+L1+baseline)

### Phase D: §4 Unconscious Processing (~25%) ⭐ LARGEST
- [ ] §4.1 Chunk-System (+EC, +Compiled Quality, +Compiled/Fresh)
- [ ] §4.2 Body-Feedback (+RSA v2.0, +3 Satiation, +HwS)
- [ ] §4.3 Cortisol (minor)
- [ ] §4.4 Agent-Mechanism (MAJOR: +Simulation-Engine, +EA, +BA, +M1-M4, +BS, +RS, +Phantom)

### Phase E: §5-§6 Feeling + PFC (~20%) ⭐ MAJOR
- [ ] §5 Feeling (+v3.0, +Compiled/Fresh)
- [ ] §6.1-§6.4 PFC Observer + Orchestrate (update)
- [ ] §6.5 NEW Simulation-Engine section
- [ ] §6.6 NEW PFC-Operations section

### Phase F: §7-§8 Body-Output + Observation Params (~10%)
- [ ] §7 Body-Output (minor)
- [ ] §8 Observation Parameters table (update ALL + add Boredom)

### Phase G: §9-§11 Development + Timescales + Reframes (~10%)
- [ ] §9 Development (+Compilable Architecture)
- [ ] §10 Timescales (minor)
- [ ] §11 Key Reframes (EXPAND: 10→20 reframes)

### Phase H: §12-§13 Honest Assessment + Cross-refs (~10%)
- [ ] §12 Honest Assessment (update numbers, review questions)
- [ ] §13 Cross-References (ALL versions, organized by folder)
- [ ] Closing note

### Phase I: VERIFY + CLEANUP
- [ ] Section header grep verify
- [ ] Cross-ref path check
- [ ] 01-File-Index.md update entry
- [ ] plan-core-foundation-rewrite.md tracking update (Session 6 ✅)
- [ ] Memory update

---

## 4. 14 CONCEPT MỚI — MAPPING VÀO SECTIONS

| # | Concept | Source | Target section(s) |
|---|---------|--------|-------------------|
| 1 | Simulation-Engine (1 engine, 3 comp, 3 axes) | Simulation-Engine v1.0 | §1.2 diagram, §4.4, §6.5 NEW |
| 2 | Entity-Compiled (hub-and-spoke, 40→200h) | EC v1.0 | §4.1, §4.4 |
| 3 | Entity-Access gradient Mức 0-5 | EA v1.2 | §4.4 |
| 4 | Bond-Architecture (1 mech × 4 bonds) | BA v1.0 | §4.4 |
| 5 | Hardware Subsidy (body subsidize entity) | VP v3.0 | §4.2, §4.4 |
| 6 | 3 Satiation Types (Cyclic/Tonic/Gen.) | GBN v1.0 | §4.2 |
| 7 | PFC-Operations (Hold/Suppress, Budget) | PFC-Ops v1.0 | §6.6 NEW |
| 8 | Compiled Quality (genuine/schema/threat) | PFC-Ops v1.0 | §4.1, §6.6 |
| 9 | M1-M4 Resonance Decline | BPGR v1.4 | §4.4 |
| 10 | By-Product-Scale (Pair/Hub/Inst.) | BS v1.0 | §4.4 |
| 11 | Resonance-Sustainability (4-Layer) | RS v1.0 | §4.4 |
| 12 | Phantom 4-factor (entity loss) | EVD v2.0 | §4.4 |
| 13 | Domain Types (Reality/Abstract/Abst-Dyn) | Domain v2.0 | §2 |
| 14 | Compiled/Fresh terminology | PFC-Ops v1.0 | Throughout |

---

## 5. VERSION UPDATES (16 files)

| Old version in v1.0 | Current version | Sections affected |
|---------------------|-----------------|-------------------|
| Self-Pattern-Modeling v2.3 | v3.1 (+RENAME) | §4.4, §8, §13, throughout |
| Empathy v2.0 | v4.0 | §4.4, §8, §13 |
| Connection v3.1 | v5.0 | §4.4, §8, §13 |
| VP v1.4 | v3.0 | §4.2, §4.4, §13 |
| Body-Coupling v1.1 | v3.0 | §13 |
| Feeling v2.1 | v3.0 | §5, §13 |
| RSA v1.0 | v2.0 | §4.2, §13 |
| Agent-Mechanism v1.0 | v2.1 | §4.4, §13 |
| Body-Base v3.1 | v3.2 | §4.1, §13 |
| BFM v1.2 | v2.0 | §4.2, §13 |
| Cortisol v2.0 | v2.1 | §4.3, §13 |
| Collective-Body v1.1 | v2.1 | §4.1, §13 |
| PFC-Config v1.0 | v1.1 | §6.4, §13 |
| Chunk v2.1 | v2.3 | §4.1, §13 |
| Compile-Taxonomy v2.0 | v2.0 (OK) | §4.1 |
| Body-Base-Example.md | (OK) | §12 |

---

## 6. NGUYÊN TẮC VIẾT

1. **MAP file**: chi tiết VỪA ĐỦ để hiểu flow + concept. Chi tiết sâu → pointer tới file chuyên sâu.
2. **Tích hợp hữu cơ**: concept mới = PHẦN CỦA cycle, KHÔNG phải "bolted on".
3. **Cross-refs chính xác**: mỗi reference = đúng file, đúng version, đúng section.
4. **Self-Pattern-Modeling v3.1**: tên mới TOÀN BỘ file. KHÔNG dùng "Self-Pattern-Match".
5. **Compiled/Fresh**: dùng terminology mới, KHÔNG dùng "Type A/Type B".
6. **Confidence tags**: 🟢/🟡/🔴 consistent.
7. **Numbers = calibration anchor**: giữ quy ước §12.4.
8. **Target size**: ~1,600-1,800 dòng (tăng nhẹ do 14 concept mới, nhưng gọn vì MAP).

---

## 7. FILES CẦN ĐỌC THÊM KHI VIẾT (nếu cần verify)

Đã đọc header/key sections (Phase 1):
- ✅ Core-Software.md v1.0 (full 1,408L)
- ✅ 01-File-Index.md (full)
- ✅ Simulation-Engine.md v1.0 (header + scope)
- ✅ PFC-Operations.md v1.0 (header + scope)
- ✅ Entity-Access.md v1.2 (header + scope)
- ✅ Entity-Compiled.md v1.0 (header + scope)
- ✅ Bond-Architecture.md v1.0 (header + scope)
- ✅ Gap-Body-Need.md v1.0 (header + scope)
- ✅ By-Product-Gap-Resonance.md v1.4 (header + scope)
- ✅ Domain.md v2.0 (header + scope)

Có thể cần đọc thêm khi viết sections cụ thể:
- Body-Base.md v3.2 (cho §4.1 sync)
- Boredom.md v2.0 (cho §8)
- Empathy.md v4.0 header (cho §8 Connection)
- Connection.md v5.0 header (cho §8)
- Imagine-Final.md v3.0 (cho §4.4 Imagination reframe)

---

> *"Core-Software = bản đồ trung tâm. Vẽ mới hoàn toàn cho đồng bộ 100%.
> 14 concept mới tích hợp hữu cơ. 16 versions cập nhật.
> Chậm mà chắc. Chất lượng cao nhất."*
