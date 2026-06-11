# Plan: Body-Base.md v4.0 REWRITE

> **Trạng thái:** ✅✅ COMPLETED — 2026-06-02
> **Ngày tạo:** 2026-06-02
> **Ưu tiên:** PHASE B (rewrite SAU Core-Software.md v3.0)
> **Lý do sau:** Body-Base reference Core-Software cho overview. Update sau khi Core-Software stable.
> **Kết quả:** v3.4 (1,527L) → v4.0 (1,249L). Trust REWRITE + Compile 1-Engine REWRITE + §0/§9 rút gọn + changelog trim + version sync.
> **Backup:** backup/Body-Base-v3.4-backup.md + backup/Body-Base-v3.4-changelog.md

---

## 0. TRƯỚC KHI BẮT ĐẦU — ĐỌC CÁC FILE SAU

### Bắt buộc đọc:

1. **Core-Software.md v3.0** (ĐÃ REWRITE ở Phase A) — TOÀN BỘ
   - Vì Body-Base reference Core-Software, cần đảm bảo nhất quán

2. **Trust.md v1.0** (Body-Base/) — TOÀN BỘ
   - KEY: §1 (3 sub-dimensions), §2 (4 nguồn formation), §4 (asymmetry)
   - KEY: §6 (Trust × Valence), §9 (Trust × Power/Status)
   - Body-Base.md §3 (Model 3+1) phải phản ánh Trust.md depth

3. **Compile-Taxonomy.md v3.0** (Chunk/) — §0-§4
   - KEY: §1 (1 Engine thesis + architecture), §3 (Trust = Amplifier not Gate)
   - Body-Base.md §4 phải adopt 1 Engine language

4. **Compile-Sleep.md v1.0** (Chunk/) — §0-§3
   - KEY: §1 (Sleep = maintenance, not exposure), §3 (6 mechanisms)
   - Body-Base.md §4.1 phải integrate maintenance concept

5. **Self-Observation.md v1.0** (PFC/) — §0, §7, §9
   - KEY: §7 (Keystone Property — cascade failure)
   - Body-Base = foundation layer. Self-Observation failure = body-base-level impact.

### Đọc nhanh (check version changes):

6. **Chunk.md v3.0** — §0-§2 (architecture alignment)
7. **Simulation-Engine.md v1.2** — header
8. **Collective-Body.md v2.2** — header + xem thay đổi
9. **Self-Pattern-Modeling.md v3.2** — header
10. **Entity-Valence-Dynamics.md v1.1** — header

### Đọc Body-Base.md v3.4 hiện tại (TOÀN BỘ) trước khi viết.

---

## 1. SECTION-BY-SECTION REWRITE INSTRUCTIONS

### YAML Header

**Action:** UPDATE

- Fix versions:
  - Chunk.md v3.0 → đã đúng
  - Compile-Taxonomy.md v3.0 → đã đúng
  - Compile-Sleep.md v1.0 → đã đúng
  - Trust.md v1.0 → đã đúng
  - Why-Body-Knows.md v1.2 → đã đúng
  - +Self-Observation.md v1.0 (THÊM dependency mới)
  - +Attention-Spectrum.md v2.1 (THÊM dependency mới)
  - Simulation-Engine.md v1.0 → **v1.2**
  - PFC-Operations.md (không version) → **v1.2**
  - Entity-Valence-Dynamics.md v1.0 → **v1.1**
  - Collective-Body.md v2.1 (implicit) → check **v2.2** khi ref
  - Self-Pattern-Modeling.md v3.1 → **v3.2**
  - Imagine-Final.md v3.0 (implicit) → **v3.1** khi ref

- scope/purpose section: update KEY CHANGES cho v4.0
- Trim: changelog history chỉ giữ v3.0 onwards (move v1.0-v2.1 to backup)

---

### §0 — VỊ TRÍ TRONG FRAMEWORK

**Action:** RESTRUCTURE (rút gọn)

**Vấn đề hiện tại:**
- Flow diagram = 50 dòng ASCII listing ~30 files → trùng lặp §10 Reading Guide
- Quá detailed cho "vị trí" section

**Đề xuất:**
- Giữ: Conceptual layer stack (10 dòng) — tốt, clear
- Giữ: "PFC-mediated drives = OPERATORS on L1" (5 dòng) — important
- Giữ: "BODY-NEED = aggregate output" (5 dòng)
- RÚT GỌN: Flow diagram từ 50 dòng → 15-20 dòng
  - Chỉ giữ 4 nhóm chính (Mechanism / Agent-Mechanism / Observation / Foundation+PFC)
  - Bỏ chi tiết sub-files (detail ở §10)
- THÊM: Self-Observation.md v1.0 trong PFC files section

**Ước tính:** 80 dòng hiện tại → ~50 dòng

---

### §1 — BODY-BASE LÀ GÌ

**Action:** UPDATE (moderate)

**§1.1 Formal Definition:** KEEP nguyên (solid)

**§1.2 3 Hardware Foundations → Compilable Architecture:** KEEP nguyên (solid)
- 3 boxes (General-Purpose Reward / Compilation / Social Hardware) vẫn chính xác
- "KẾT HỢP ①②③ = COMPILABLE ARCHITECTURE" vẫn đúng

**§1.3 Body-Need: 2-Source Aggregate:** UPDATE
- THÊM: Cross-ref Gap-Body-Need.md v1.0 §11 "entity-gap matching" (đã có nhưng strengthen)
- Fix: "Body-Feedback-Mechanism v2.1" reference (đã đúng)
- THÊM: brief mention Sleep Maintenance impact on body-need (sleep deprivation → body-need distorted)

**§1.4 Schema Phục Vụ Body-Base:** KEEP nguyên (solid)

---

### §2 — CORE PRINCIPLE: Body Evaluates Patterns, Not Reality

**Action:** KEEP (section vẫn solid — Treisman 1977, 6 cases, unified principle)

- Chỉ kiểm tra: "Why-Body-Knows.md §3" ref đúng version

---

### §3 — UNIFIED MODEL: 3 Components + 1 Bridge ⭐⭐⭐

**Action:** REWRITE (Trust section)

**Component 1 — Vô Thức:** KEEP nguyên (solid, 20 dòng)

**Component 2 — PFC:** UPDATE
- THÊM: "Self-Observation = APPLICATION-3 (keystone — fail → cascade 5+ systems)"
- THÊM: "Attention-Spectrum.md v2.1" ref
- Fix: Simulation-Engine.md v1.0 → v1.2

**Component 3 (Bridge) — Trust:** ⭐⭐⭐ REWRITE (hiện 27 dòng → ~45-55 dòng)

Cấu trúc mới đề xuất:

```
│ COMPONENT 3 (BRIDGE) — TRUST: AMPLIFY + MODULATE + CONNECT       │
│                                                                    │
│   DEFINITION (Trust.md v1.0):                                      │
│     Trust = compiled prediction about entity's gap-fill RELIABILITY │
│     Trust ≠ Valence: trust = PREDICTION (tương lai) ≠ assessment   │
│                                                                    │
│   3 SUB-DIMENSIONS:                                                │
│     ① Authority: entity CÓ QUYỀN trong domain?                    │
│     ② Competence: entity CÓ NĂNG LỰC trong domain?               │
│     ③ Intention: entity CÓ Ý TỐT cho tôi?                        │
│     3 chiều ĐỘC LẬP — high ở 1, low ở 2 có thể xảy ra           │
│                                                                    │
│   3 FUNCTIONS:                                                     │
│     AMPLIFY: trust = Entity-Valence Bias cho compile rate          │
│       (gradient Mức 0-5, NOT binary gate)                          │
│     MODULATE: trust modulate TOÀN BỘ valence profile               │
│     CONNECT: trust = ONLY mechanism cho complexity > 4±1           │
│                                                                    │
│   DYNAMICS:                                                        │
│     Build: CHẬM (months/years — cần consistency, not 1 lần tốt)   │
│     Collapse: NHANH (1 betrayal — negativity bias)                 │
│     → Asymmetry = evolutionary design: quick detect danger         │
│                                                                    │
│   FORMATION: 4 nguồn (Direct > Observed > Schema > Context)       │
│     ① Direct experience: chậm nhất, chính xác nhất (months)       │
│     ③ Schema inheritance: nhanh nhất, kém chính xác (hours)       │
│     = TẠI SAO trẻ tin thầy TRƯỚC khi đi học (installed trust)    │
│                                                                    │
│   ENTITY-ACCESS GRADIENT = formalized trust model:                 │
│     Mức 0 (stranger) → Mức 5 (self/child)                         │
│     Chi tiết: Entity-Access.md v1.2, Trust.md v1.0                 │
│                                                                    │
│   BOND-ARCHITECTURE = 4 bond types qua 1 mechanism (giữ nguyên)   │
│                                                                    │
│   Tại sao Trust = Bridge, không phải component: (giữ nguyên)      │
```

**Amplifier — External Tools:** KEEP nguyên (solid)

**Blackbox-1 + Blackbox-2 Convergence:** KEEP nguyên

---

### §4 — BODY COMPILE + COMPILED/FRESH AXIS ⭐⭐

**Action:** REWRITE (§4.1-§4.2, giữ §4.3)

**§4.1 PFC ≠ Compiler:** KEEP nguyên (solid — 5 PFC roles, 4 compile mechanisms, Einstein test)
- UPDATE: "④ Sleep consolidation — offline integration" → THÊM: "= Sleep Maintenance system (6 mechanisms: ~1.5 exposure + ~4.5 optimization). Sleep ≠ thêm exposure. Sleep = bảo trì + tối ưu chunks đã compile. Chi tiết: Compile-Sleep.md v1.0"
- Fix: Chunk.md v2.3 → v3.0

**§4.2 3 Compile Types:** REWRITE

Thay đổi organizing principle:

```
Hiện tại (v3.4):
  "3 COMPILE TYPES (Drill §3 — chi tiết: Compile-Taxonomy.md E4)"
  → Mô tả 3 types NHƯ RIÊNG BIỆT

Mới (v4.0):
  "COMPILE ARCHITECTURE: 1 ENGINE + 3 MODULATOR CONFIGURATIONS (Compile-Taxonomy.md v3.0)"
  
  ALL compile = 1 Engine: Exposure → Hebbian → Compiled Chunk.
  3 Compile Types = labels cho dominant modulator configurations:
  
  ┌──────────────┬──────────────────────────┬──────────────┐
  │ Type         │ Engine + Dominant Modulator│ % behavior  │
  ├──────────────┼──────────────────────────┼──────────────┤
  │ Experience   │ Engine + minimal modulators│ ~90%        │
  │ Expertise    │ Engine + PFC sustained hold│ ~5%         │
  │ Trust        │ Engine + Entity-Valence Bias│ ~5%        │
  └──────────────┴──────────────────────────┴──────────────┘
  
  Trust = AMPLIFIER (gradient Mức 0-5), KHÔNG phải GATE (binary).
  Trẻ bị ÉP HỌC (no trust) → VẪN compile kiến thức (engine chạy).
  Trust "đóng" → body EXPOSED to content → content compile.
  Trust KHÔNG gate content compile. Trust amplify VALUE compile.
  
  Chi tiết architecture: Compile-Taxonomy.md v3.0
```

- THÊM: "3 Exposure Channels: External / Deliberate / Spontaneous chạy SONG SONG"
- Fix: "Compile-Taxonomy.md E4" → "Compile-Taxonomy.md v3.0" (section numbering changed)

**§4.3 Compiled vs Fresh = Real Axis:** KEEP nguyên (solid — Inter-Body §3, Kahneman S1/S2)

---

### §5 — L0-L1 SUBSTRATE

**Action:** UPDATE (minor)

- §5.1 L0: KEEP
- §5.2 L1: KEEP
- §5.3 PFC-Mediated Operators: UPDATE
  - Fix: "Hardware-Subsidy" section — Entity-Valence-Dynamics.md v1.0 → v1.1
  - Có thể THÊM: trust per-entity mention linking to Trust.md v1.0
- §5.4 Modulatory vs Processing: KEEP

---

### §6 — 3-LAYER EVOLUTION

**Action:** KEEP (solid — Boyd & Richerson 2005, Tomasello 2009)

---

### §7 — 2-TIER CALIBRATION

**Action:** UPDATE (moderate)

- Giữ cấu trúc 2 tầng + 2 đường vào
- THÊM trong Tầng 2b (Trust-Injected):
  "Trust mechanism chi tiết: Trust.md v1.0 §2 (4 nguồn formation).
  Trust Compile = Engine + Entity-Valence Bias dominant (Compile-Taxonomy v3.0 §4)."
- Strengthen connection: "2b inject SEED → 2a verify + DEEPEN" with Trust.md formation stages

---

### §8 — CIRCUIT BREAKER MECHANISM

**Action:** KEEP (solid — 3 break pathways, Valence-Structural ceiling)

---

### §9 — BODY-FEEDBACK OVERVIEW

**Action:** REDUCE (rút ngắn)

**Vấn đề:** Section này = 70 dòng mô tả Body-Feedback chi tiết. Nhưng Body-Feedback.md v3.1 ĐÃ là entry point riêng cho Body-Feedback/ folder.

**Đề xuất:**
- RÚT GỌN từ 70 dòng → ~35-40 dòng
- Giữ: Dual-Pull (brief — 10 dòng), Body-Feedback-Precondition table (15 dòng), 3 Genuine Sources (10 dòng)
- BỎ: "Melody hay" 4 criteria (thuộc Melody Lens, không phải Body-Feedback)
- BỎ: Interface Loop 6-step chi tiết (đã ở Body-Feedback.md)
- THÊM pointer: "Chi tiết đầy đủ: Body-Feedback/Body-Feedback.md v3.1 (17 files, ~27,500L)"

---

### §10 — READING GUIDE CHO BODY-BASE/ FOLDER

**Action:** REWRITE (comprehensive update)

**Folder tree:** UPDATE
- Chunk/ section: +Compile-Taxonomy.md v3.0, +Compile-Sleep.md v1.0, Chunk.md v3.0
- Body-Base/ top-level: +Trust.md v1.0 (với description)
- PFC/ section: +Self-Observation.md v1.0
- Body-Feedback/: 17 files (đã đúng ở v3.4 nhưng double-check)
- Feeling/: +Body-Knowing.md v1.0 (đã ở v3.4)

**Reading Paths:** UPDATE
- Quick orientation: THÊM Trust.md v1.0 (vì trust = foundation)
- Core mechanism: Fix versions (Chunk v3.0, etc.)
- THÊM path mới: "Trust + Compile Architecture deep dive"
  1. Trust.md v1.0
  2. Compile-Taxonomy.md v3.0
  3. Compile-Sleep.md v1.0
  4. Chunk.md v3.0

---

### §11 — HONEST ASSESSMENT

**Action:** UPDATE

- 🟢 HIGH CONFIDENCE: THÊM Trust research (Mayer 1995, Colquitt 2007, Lewicki 2006) — từ Trust.md v1.0
- 🟡 MEDIUM CONFIDENCE: THÊM:
  - "Trust = compiled prediction about reliability" = framework synthesis
  - "Trust 3 sub-dimensions" = framework synthesis (extending Mayer 1995)
  - "1 Engine + 3 Modulators" = framework synthesis
  - "Sleep = 6-mechanism maintenance system" = framework synthesis
  - "Self-Observation Gradient Mức 0-6" = framework synthesis
  - "Self-Observation Keystone Property" = framework synthesis
- 🔴 LOW CONFIDENCE: check nếu có gì thêm

---

### §12 — CROSS-REFERENCES

**Action:** UPDATE (fix versions, add new refs)

- Fix ALL version numbers (danh sách ở mục 0)
- THÊM:
  - Trust.md v1.0 — compiled prediction, 3 sub-dims, formation, dynamics
  - Self-Observation.md v1.0 — APPLICATION-3, Mức 0-6, keystone
  - Compile-Taxonomy.md v3.0 — 1 Engine + 3 Modulators
  - Compile-Sleep.md v1.0 — Sleep Maintenance, 6 mechanisms
  - Attention-Spectrum.md v2.1 — attention hardware, COMT/DRD4

---

### CHANGELOG / CLOSING NOTE

**Action:** RESTRUCTURE

- Move detailed v1.0→v3.3 changelog to backup file: backup/Body-Base-v3.4-changelog.md
- File chỉ giữ: v3.4 summary (5 dòng) + v4.0 summary (5 dòng)
- Closing note: update với v4.0 highlights

**Ước tính giảm:** ~70 dòng changelog → ~15 dòng → TIẾT KIỆM ~55 dòng

---

## 2. QUALITY CHECKS SAU KHI VIẾT

- [ ] Core-Software.md v3.0 và Body-Base.md v4.0 KHÔNG mâu thuẫn nhau
- [ ] §3 Trust section phản ánh Trust.md v1.0 (3 sub-dims, formation, asymmetry)
- [ ] §4 Compile section dùng "1 Engine + Modulators" nhất quán
- [ ] §0 flow diagram rút gọn + vẫn accurate
- [ ] §9 rút gọn nhưng vẫn đủ overview value
- [ ] §10 Reading Guide complete (tất cả file mới có mặt)
- [ ] §12 Cross-refs ALL version đúng
- [ ] Mọi version number trong YAML deps đúng
- [ ] Không có abbreviation
- [ ] Entry point nature giữ nguyên: đọc file này TRƯỚC → chọn hướng đi sâu
- [ ] File length hợp lý: ~1,400-1,600L (không tăng, có thể giảm nhẹ)
- [ ] Changelog trimmed (old versions → backup)

---

## 3. BACKUP

Trước khi rewrite:
- Copy Body-Base.md → backup/Body-Base-v3.4-backup.md
- Tạo backup/Body-Base-v3.4-changelog.md (chứa detailed changelog v1.0→v3.4)

---

## 4. ƯỚC TÍNH

- Đọc prep: ~20 phút (ít hơn Phase A vì đã đọc 4 file mới)
- Rewrite: ~1-2 sessions tập trung
- Kết quả: v3.4 (1,527L) → v4.0 (~1,400-1,600L)
- Có thể GIẢM NHẸ nhờ: §0 rút gọn (-30L), §9 rút gọn (-30L), changelog trim (-55L)
- Tăng nhẹ từ: §3 Trust rewrite (+20L)

---

## 5. THỨ TỰ THỰC HIỆN TỔNG THỂ

```
SESSION 1: Phase A — Core-Software.md v3.0 REWRITE
  → Đọc prep (30 phút)
  → Backup v2.2
  → Rewrite section by section
  → Quality check

SESSION 2 (nếu cần): Phase A tiếp tục
  → Complete remaining sections
  → Final quality check
  → Commit v3.0

SESSION 3: Phase B — Body-Base.md v4.0 REWRITE
  → Đọc prep (20 phút, including Core-Software v3.0 mới)
  → Backup v3.4
  → Rewrite section by section
  → Quality check
  → Commit v4.0

SESSION 4 (optional): Post-rewrite verification
  → Cross-check Core-Software v3.0 ↔ Body-Base v4.0
  → Check 4 file mới reference đúng
  → Update 01-File-Index.md nếu cần
```
