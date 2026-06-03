# Plan: Core-Software.md v3.0 REWRITE

> **Trạng thái:** ✅✅ COMPLETED — 2026-06-02
> **Ngày tạo:** 2026-06-02
> **Ưu tiên:** PHASE A (rewrite TRƯỚC Body-Base.md)
> **Lý do ưu tiên:** Core-Software = bản đồ chính cho researcher. Mọi concept mới phải phản ánh ở đây trước.
> **Kết quả:** v2.2 (1,784L) → v3.0 (1,955L). 4 file mới tích hợp + 10+ version fixes + 4 reframes.
> **Backup:** _backup/Core-Software-v2.2-backup.md

---

## 0. TRƯỚC KHI BẮT ĐẦU — ĐỌC CÁC FILE SAU

### Bắt buộc đọc (để nắm concept mới):

1. **Compile-Taxonomy.md v3.0** (Chunk/) — TOÀN BỘ
   - KEY: §1 (1 Engine + 3 Modulators + Exposure Channels + Sleep Maintenance)
   - KEY: §3 (Trust = Amplifier not Gate)
   - KEY: §5 (Multi-Stream Compile)
   - KEY: §7 (Feedback Loop bidirectional)
   - KEY: §10 (Evolutionary Gradient)

2. **Compile-Sleep.md v1.0** (Chunk/) — §0-§5
   - KEY: §1 (Sleep ≠ exposure source — 6 mechanisms, ~1.5 exposure + ~4.5 optimization)
   - KEY: §4 (Sleep × Compile Architecture interaction)
   - KEY: §5 (Sleep Deprivation = Architecture Degradation)

3. **Trust.md v1.0** (Body-Base/) — TOÀN BỘ
   - KEY: §1 (Definition + 3 sub-dimensions: Authority/Competence/Intention)
   - KEY: §2 (Formation 4 nguồn)
   - KEY: §4 (Asymmetry: build chậm, collapse nhanh)
   - KEY: §6 (Trust × Valence: 2 observations của cùng 1 process)
   - KEY: §8 (Break conditions)
   - KEY: §9 (Trust × Power/Status)

4. **Self-Observation.md v1.0** (PFC/) — TOÀN BỘ
   - KEY: §0 (Thesis: Self-Observation = Feeling khi target = SELF)
   - KEY: §1 (3-component definition)
   - KEY: §2 (Trigger Principle v2: 3 delta types × 2 pathways)
   - KEY: §3 (2-Axis Model: Development Capacity × Activation Level)
   - KEY: §4 (Gradient Mức 0-6)
   - KEY: §7 (Keystone Property: fail → cascade 5+ systems)
   - KEY: §9 (Tool Not Virtue)

### Đọc nhanh (check version changes):

5. **Chunk.md v3.0** — §0 + §2 (xem thay đổi gì từ v2.3: architecture alignment, §2 trim→Compile-Taxonomy)
6. **Simulation-Engine.md v1.2** — header + xem thay đổi gì từ v1.0
7. **PFC-Operations.md v1.2** — header + xem thay đổi gì từ v1.0
8. **Collective-Body.md v2.2** — header + xem thay đổi gì từ v2.1
9. **Self-Pattern-Modeling.md v3.2** — header + xem thay đổi gì từ v3.1
10. **Entity-Valence-Dynamics.md v1.1** — header + xem thay đổi gì từ v1.0
11. **Imagine-Final.md v3.1** — header + xem thay đổi gì từ v3.0
12. **Attention-Spectrum.md v2.1** — §0 (file mới, chưa trong Core-Software)
13. **PFC-Label.md v1.1** — header

### Đọc Core-Software.md v2.2 hiện tại (TOÀN BỘ) trước khi viết.

---

## 1. SECTION-BY-SECTION REWRITE INSTRUCTIONS

### §0 — BA BẢN ĐỒ + TẠI SAO CYCLE-BASED

**Action:** REFINE (minor)

- §0.1: Giữ nguyên 2 bản đồ + Ask-AI tương tác. Không đổi.
- §0.2: Giữ nguyên "Tại sao v7.8 cycle-based" table. Không đổi.
- §0.3: Giữ nguyên 7 nguyên tắc thiết kế. Không đổi.
- **Thay đổi duy nhất:** YAML header — update Tiền đề đọc list:
  - Chunk.md v2.3 → v3.0
  - Compile-Taxonomy.md v3.0 (ĐÃ CÓ — giữ)
  - Compile-Sleep.md v1.0 (ĐÃ CÓ — giữ)
  - +Trust.md v1.0
  - +Self-Observation.md v1.0
  - Simulation-Engine.md v1.0 → v1.2
  - PFC-Operations.md v1.0 → v1.2
  - Collective-Body.md v2.1 → v2.2
  - Self-Pattern-Modeling.md v3.1 → v3.2
  - Entity-Valence-Dynamics.md v1.0 → v1.1 (companion VP v4.1)
  - Imagine-Final.md v3.0 → v3.1
  - +Attention-Spectrum.md v2.1
  - +PFC-Label.md v1.1
  - Body-Base.md v3.2 → v3.4 (hoặc v4.0 nếu Body-Base đã rewrite)

---

### §1 — KIẾN TRÚC CYCLE: SOFTWARE MAP

**Action:** REWRITE (§1.2 diagram + §1.3 mapping)

**§1.1** Ba góc nhìn — KEEP nguyên.

**§1.2** Software Map diagram — REWRITE:
- PFC box: THÊM "Self-Observation = APPLICATION-3 (Self, Present, Observe)"
- PFC box: THÊM "KEYSTONE: Self-Observation fail → cascade 5+ systems"
- Unconscious/Chunk box: ĐỔI "compile: repetition + emotional peak + multi-modal + sleep"
  → "Compile: 1 Engine (Exposure→Hebbian) + 3 Modulators + Sleep Maintenance"
- Unconscious/Chunk box: THÊM "3 Exposure Channels: External / Deliberate / Spontaneous"
- Unconscious/Agent box: THÊM "Trust.md v1.0: 3 sub-dims (Authority/Competence/Intention)"
- Feeling box: THÊM "Feeling hướng DOMAIN vs hướng SELF (Self-Observation)"

**§1.3** Hardware↔Software mapping table — UPDATE:
- Thêm row: "Trust mechanism" → "B (insula valence) + C (amygdala tagging) + A (mPFC per-entity)"
- Thêm row: "Self-Observation" → "B (anterior insula) + A (mPFC self-model)"
- Fix existing references nếu cần

**§1.4** Tại sao cycle — KEEP nguyên.

---

### §2 — DOMAIN

**Action:** KEEP (section vẫn solid, Domain.md v2.0 chưa đổi)

- Chỉ kiểm tra: mọi cross-ref version đúng.

---

### §3 — BODY-INPUT (L0 + L1)

**Action:** UPDATE (minor)

- §3.1 L0: KEEP nguyên.
- §3.2 L1: KEEP nguyên (17 categories vẫn chuẩn).
- §3.3 Baseline Adaptation: KEEP nguyên.
- **Thêm note cuối §3:** "Self-signal interoception (⑰) = prerequisite cho Self-Observation.md (APPLICATION-3). Damage → cascade failure."

---

### §4 — UNCONSCIOUS PROCESSING ⭐⭐⭐ SECTION LỚN NHẤT

**Action:** MAJOR REWRITE

#### §4.1 Chunk-System — REWRITE

**Mục tiêu:** Adopt "1 Engine + 3 Modulators" architecture từ Compile-Taxonomy v3.0.

**Cấu trúc mới đề xuất cho §4.1:**

```
§4.1 Chunk-System — Sole Substrate

  CHUNK = ATOM (giữ nguyên definition)
  
  COMPILE ARCHITECTURE (MỚI — từ Compile-Taxonomy v3.0):
    1 ENGINE: Exposure → Hebbian → Compiled Chunk
    - 4 compile mechanisms = 4 DẠNG exposure (không phải 4 mechanisms riêng)
    - No source tag = evidence cho 1 Engine
    
    3 MODULATORS:
    - Entity-Valence Bias (automatic): trust as valence meta-dimension, amplify rate + bias probability
    - 3 Exposure Channels (parallel): External / Deliberate / Spontaneous
    - PFC Modulation (deliberate): Hold/Suppress
    
    SLEEP MAINTENANCE (offline):
    - 6 mechanisms (~1.5 exposure + ~4.5 optimization)
    - Sleep ≠ exposure source #4. Sleep = offline maintenance system.
    - Chi tiết: Compile-Sleep.md v1.0
    
  3 COMPILE TYPES = DOMINANT MODULATOR CONFIGURATIONS (giữ labels, reframe mechanism):
    Experience (~90%): Engine + minimal modulators (direct exposure)
    Expertise (~5%): Engine + PFC sustained hold (PFC-dominant)
    Trust (~5%): Engine + Entity-Valence amplifier (Entity-Valence-dominant)
    → Cùng 1 Engine. Khác MODULATOR configuration.
    
  MULTI-STREAM COMPILE (MỚI — từ Compile-Taxonomy v3.0 §5):
    Content / Value / Entity / Behavior compile SONG SONG
    
  COMPILED QUALITY DIMENSION (giữ nguyên)
  
  ENTITY-COMPILED (giữ nguyên)
  
  4 CONNECTION TYPES (giữ nguyên)
  
  ACTIVATION DYNAMICS (giữ nguyên)
  
  "SCHEMA" = OBSERVATION LABEL (giữ nguyên)
  
  MODEL 3+1 (giữ nguyên — nhưng Trust reference → Trust.md v1.0)
  
  MODEL 3 CẤP (giữ nguyên)
```

**Thay đổi lớn:**
- BỎ: "4 COMPILE MECHANISMS: ① Repetition ② Emotional peak ③ Multi-modal ④ Sleep" — thay bằng "4 dạng exposure"
- BỎ: "5 EXTERNAL INSTALL MECHANISMS" block — integrate vào 3 Exposure Channels
- THÊM: 1 Engine thesis + 3 Modulators + 3 Exposure Channels
- THÊM: Sleep Maintenance concept (ngắn, ref Compile-Sleep.md)
- THÊM: Multi-Stream Compile (brief mention)
- SỬA: Trust language → "Entity-Valence Bias" (Compile-Taxonomy terminology)

#### §4.2 Body-Feedback — UPDATE (moderate)

- Giữ cấu trúc: Evaluative/Direct-State Reward + Dissonance + Dual-Pull + Body-Feedback-Precondition + Satiation + Hardware-Subsidy + Chunk Dynamics
- THÊM: Dissonance-Signal-Architecture v1.0 integration (đã partially done ở v2.1)
- Fix version refs: Reward-Signal-Architecture v2.0→v2.1, Body-Feedback-Mechanism v2.0→v2.1

#### §4.3 Cortisol — KEEP (solid)

- Fix version: Cortisol-Baseline.md v2.1 (đã đúng)

#### §4.4 Agent-Mechanism — REWRITE (restructure)

**Mục tiêu:** Integrate Trust.md v1.0 + restructure cho dễ navigate.

**Cấu trúc mới đề xuất:**

```
§4.4 Agent-Mechanism — Functions on Chunk Substrate

  ⭐ TRUST MECHANISM (MỚI — từ Trust.md v1.0):
    Trust = compiled prediction about entity's gap-fill RELIABILITY
    Trust ≠ Valence (2 chiều ĐỘC LẬP)
    3 sub-dimensions: Authority / Competence / Intention
    Formation: 4 nguồn (Direct > Observed > Schema > Context)
    Dynamics: build CHẬM (months), collapse NHANH (1 betrayal)
    Trust = meta-dimension modulating ALL valence channels
    Chi tiết: Trust.md v1.0
  
  SELF-PATTERN-MODELING (giữ nguyên, update v3.1→v3.2)
  
  ENTITY-ACCESS GRADIENT (giữ nguyên)
  
  BOND-ARCHITECTURE (giữ nguyên)
  
  RESONANCE DECLINE (giữ nguyên)
  
  BY-PRODUCT-SCALE (giữ nguyên)
  
  RESONANCE-SUSTAINABILITY (giữ nguyên)
  
  PHANTOM 4-FACTOR (giữ nguyên)
  
  EMPATHY (giữ nguyên, update v4.0)
  
  VALENCE (giữ nguyên, fix Entity-Valence-Dynamics v1.0→v1.1)
  
  IMAGINATION (giữ nguyên, update v3.0→v3.1)
```

**Thay đổi lớn:**
- THÊM Trust Mechanism block ĐẦU TIÊN trong Agent-Mechanism section (vì Trust = meta-dimension ảnh hưởng tất cả)
- UPDATE version refs throughout

---

### §5 — FEELING (Bridge)

**Action:** UPDATE (moderate)

- THÊM phân biệt: "Feeling hướng DOMAIN vs Feeling hướng SELF (= Self-Observation)"
- THÊM: "Self-Observation = Feeling khi target = SELF. Formal file: Self-Observation.md v1.0"
- Giữ nguyên: 7-layer fidelity, PFC=Lawyer, 7 loại feeling, temporal order
- Body-Knowing Inward ⊂ Self-Observation mention (brief)

---

### §6 — PFC (Observer + Orchestrator) ⭐⭐

**Action:** REWRITE (§6.5 expand, §6.7 NEW)

**§6.1-§6.4:** KEEP (solid — PFC observer, orchestrate, activation, configurations)
- Minor: update PFC-Operations v1.0→v1.2, PFC-Configuration v1.1 (giữ)

**§6.5** Simulation-Engine — UPDATE:
- v1.0 → v1.2
- Application table: update Self-Observation row with more detail
- +mention: "Self-Observation = APPLICATION-3, formal file: Self-Observation.md v1.0"

**§6.6** PFC-Operations — KEEP (solid)
- Version: v1.0 → v1.2

**§6.7** Self-Observation — NEW SECTION (15-25 dòng):

```
§6.7 Self-Observation — APPLICATION-3 (MỚI)

  Self-Observation = f(Interoception × PFC_Encoding × Attention_Direction=SELF)
  = Feeling khi target = SELF (vs Feeling hướng Domain)
  
  GRADIENT MỨC 0-6:
    0 Body-React → 1 Body-Awareness → 2 Self-Observation Basic
    → 3 Pattern-Recognition → 4 Process-Observation
    → 5 Meta-Observation → 6 Calibrated-Observe
  
  TRIGGER: Prediction-delta × Solution Difficulty
    Delta = 0 → Self-Observation ZERO (body smooth → invisible)
    Delta > 0 + compiled solution → Mức 2 (quick)
    Delta > 0 + no solution → escalate Mức 3→5
  
  KEYSTONE PROPERTY:
    Self-Observation fail → cascade 5+ systems degrade:
    Self-Pattern-Modeling, Dual Check, Somatic-Articulation-Loop, Imagine-Final, Moral
  
  TOOL NOT VIRTUE:
    Mức 2 ĐỦ routine life (~95%). Depth ≠ life quality.
    Domain feedback = differentiator (Einstein vs conspiracy theorist = cùng mechanism)
  
  Reference: Self-Observation.md v1.0
```

---

### §7 — BODY-OUTPUT

**Action:** KEEP (solid, chỉ 20 dòng)

---

### §8 — OBSERVATION PARAMETERS

**Action:** UPDATE (minor)

- Fix version refs: Status.md v2.0, Boredom.md v2.0, Connection.md v5.0, etc.
- Kiểm tra: có observation param nào mới không? (Có thể không)

---

### §9 — DEVELOPMENT TRAJECTORY

**Action:** UPDATE (minor)

- THÊM: Entity-Access developmental progression per age stage (Mức 0-1 → 2-3 → 3-4)
- THÊM: Self-Observation developmental progression reference
- Fix: Compilable Architecture ref → Body-Base.md v3.4 (hoặc v4.0)

---

### §10 — MULTIPLE TIMESCALES

**Action:** KEEP (solid, 15 dòng)

---

### §11 — KEY REFRAMES ⭐

**Action:** REWRITE (add new reframes)

Thêm 4 reframes mới:

```
#22. 1 Engine + 3 Modulators (Compile-Taxonomy v3.0)
    → ALL compile = Exposure → Hebbian. "3 types" = dominant modulator configs.
    → Trust = Amplifier (gradient Mức 0-5), KHÔNG phải Gate (binary).

#23. Sleep = Offline Maintenance System (Compile-Sleep v1.0)
    → Sleep có 6 mechanisms — chỉ ~1.5 exposure-based, ~4.5 optimization.
    → Sleep deprivation = architecture degradation, PFC first.

#24. Trust Mechanism Formalized (Trust.md v1.0)
    → Trust = compiled prediction about reliability (≠ valence).
    → 3 sub-dimensions: Authority / Competence / Intention.
    → Build chậm (months), collapse nhanh (1 betrayal).

#25. Self-Observation = APPLICATION-3 Formalized (Self-Observation.md v1.0)
    → Self-Observation = Feeling khi target = SELF.
    → Gradient Mức 0-6. Keystone: fail → cascade 5+ systems.
    → Tool Not Virtue: Mức 2 ĐỦ routine. Domain feedback = differentiator.
```

---

### §12 — HONEST ASSESSMENT

**Action:** UPDATE

- §12.1 Cái framework provides: THÊM Trust mechanism, Self-Observation formalization, 1 Engine architecture, Sleep Maintenance
- §12.2 Cái framework KHÔNG provides: giữ nguyên (vẫn đúng)
- §12.3 Open questions:
  - Check: Q11 (Entity-Compiled capacity) — có resolve thêm không?
  - Check: Q12 (Hardware-Subsidy molecular) — vẫn open
  - Check: Q13 (Compiled Quality re-tag) — có resolve thêm không?
  - THÊM mới nếu có từ 4 file mới
- §12.4 Number Convention: KEEP

---

### §13 — CROSS-REFERENCES

**Action:** REWRITE (fix ALL versions)

- Fix mọi version number theo danh sách ở mục 0
- THÊM sections: Trust.md v1.0, Self-Observation.md v1.0, Compile-Sleep.md v1.0, Attention-Spectrum.md v2.1
- RÚT GỌN: có thể gom một số sections, giảm từ 155 dòng → ~120 dòng
- Phương án: reference 01-File-Index.md cho full list, §13 chỉ giữ KEY references

---

## 2. QUALITY CHECKS SAU KHI VIẾT

- [ ] Mọi version number trong file khớp version thực tế
- [ ] 4 file mới đều được tích hợp nội dung (không chỉ mention tên)
- [ ] Software Map diagram (§1.2) phản ánh đầy đủ architecture hiện tại
- [ ] §4.1 dùng "1 Engine + Modulators" language nhất quán
- [ ] §4.4 có Trust Mechanism block
- [ ] §6 có Self-Observation section
- [ ] §11 có reframes #22-25
- [ ] Không có abbreviation nào (tuân thủ abbreviation cleanup)
- [ ] Thuật ngữ nhất quán: "Entity-Valence Bias" (không "trust amplifier" cũ)
- [ ] Tiền đề đọc list đầy đủ + đúng version
- [ ] Cross-references §13 đầy đủ + đúng version
- [ ] File vẫn SELF-CONTAINED (đọc Core-Software.md đủ hiểu overview, không cần đọc sub-files)

---

## 3. BACKUP

Trước khi rewrite:
- Copy Core-Software.md → backup/Core-Software-v2.2-backup.md

---

## 4. ƯỚC TÍNH

- Đọc prep: ~30 phút (4 file mới + 8 file check version)
- Rewrite: ~2-3 sessions tập trung
- Kết quả: v2.2 (1,784L) → v3.0 (~2,000-2,200L)
- Tăng ~200-400L chủ yếu từ: §4.1 (1 Engine), §4.4 (Trust), §6.7 (Self-Observation), §11 (reframes)
