# ~~Plan: Compile Architecture Refine~~ — SUPERSEDED

> **SUPERSEDED 2026-06-01:** Tách thành 3 plan riêng biệt cho chất lượng cao hơn:
> - **Plan 1/3:** Child-Development/plan-compile-refine-child-dev.md (4 files, +540L)
> - **Plan 2/3:** Education-Mechanism/plan-compile-refine-education-mechanism.md (7 files, +366L)
> - **Plan 3/3:** Education-System/plan-compile-refine-education-system.md (8 files, +157L)
> Dependency: Plan 1 → Plan 2 → Plan 3 (sequential). Total: 19 files, +1,063L, ~5-7 sessions.
>
> ---
> **Original plan below (kept for reference):**
>
> **Created:** 2026-06-01
> **Trigger:** Compile-Taxonomy.md v3.0 + Compile-Sleep.md v1.0 hoàn thành → 5 reframe lớn chưa lan tới Human-Learning + Education-System
> **Scope:** ~16 active files across 3 folders → refine (KHÔNG rewrite toàn bộ)
> **Approach:** Mỗi session = 1-2 file. Compact session trước mỗi file. Chất lượng > tốc độ.
> **Estimated:** ~5-6 sessions

---

## Bối cảnh: 5 Reframe từ CT v3.0 + CS v1.0

```
COMPILE-TAXONOMY v3.0 (1,635L, 2026-06-01):

  REFRAME 1: "4+1 Channel Compile" → "1 Engine + 3 Modulators + 3 Exposure Channels"
    OLD: ① Repetition ② Emotional Peak ③ Multi-modal ④ Sleep ⑤ External Install
    NEW: 1 Engine (Hebbian) + 3 Modulators (Entity-Valence | PFC | Sleep)
         + 3 Exposure Channels (External | Deliberate | Spontaneous)
    → Tất cả file dùng "4+1 kênh compile" cần update

  REFRAME 2: Trust = Amplifier (NOT Gate)
    OLD: Trust = binary gate ("tin → compile, không tin → block")
    NEW: Trust = gradient amplifier Mức 0-5, ÁP DỤNG cho VALUE compile,
         KHÔNG áp dụng cho CONTENT compile
    → "Giỏi nhưng ghét" = content ✓ value ✗

  REFRAME 3: Multi-Stream Compile (4 parallel streams)
    NEW: Content / Value / Entity / Behavior compile ĐỘC LẬP
    → Cùng 1 event = 4 compilations khác nhau
    → Approach/avoidance tag ÁP DỤNG chủ yếu cho Value + Behavior stream
    → Content stream compile KHÔNG PHỤ THUỘC tag (chỉ cần exposure)

  REFRAME 4: Critical Asymmetry
    NEW: PFC → Entity-Valence = CHẬM (tuần/tháng, cost CAO, gián tiếp)
         Entity-Valence → PFC = NHANH (ms, cost ZERO, trực tiếp override)
    → "Biết mà không làm" = PFC biết (content) nhưng Entity-Valence override (value)
    → "Love the teacher" hiệu quả hơn "explain importance"

  REFRAME 5: 6 Trade-offs of Compile Short (Trust Compile risks)


COMPILE-SLEEP v1.0 (1,318L, 2026-06-01):

  REFRAME 6: Sleep = Offline Maintenance (NOT exposure source)
    OLD: Sleep = "4th compile channel" (ngang hàng Repetition, Emotional Peak...)
    NEW: Sleep = offline maintenance system
         ~1.5 exposure-based (Replay, Creative Linking, Gist)
         ~4.5 optimization-based (SHY, Consolidation, Decoupling)
    → Phần LỚN sleep = OPTIMIZATION, không phải compile mới
    → 6 mechanisms phân loại rõ

  REFRAME 7: Sleep × Compile Architecture interactions
    NEW: Sleep × Engine (Replay + SHY), Sleep × Entity-Valence (Decoupling),
         Sleep × Exposure Channels (blocks External, offline Spontaneous),
         Sleep × PFC (catecholamine recharge)

  REFRAME 8: Waking Rest ≈ 30% only (DMN, incubation, walking — KHÔNG thay thế sleep)
```

---

## Nguyên tắc refine

```
① NỘI DUNG CỤ THỂ KHÔNG ĐỔI — chỉ reframe CƠ CHẾ TỔNG QUÁT
   VD: mọi ví dụ (bò, mút tay, piano, bơi) VẪN ĐÚNG
   VD: approach/avoidance tag VẪN ĐÚNG — chỉ ENRICH thêm multi-stream

② KẾT LUẬN THỰC TẾ KHÔNG ĐỔI
   "Ngủ đủ = quan trọng" — chỉ giải thích CHÍNH XÁC hơn TẠI SAO
   "Cách dạy quyết định tag" — chỉ thêm chiều VALUE vs CONTENT
   "4-step progression" — chỉ MAP sang Trust/Experience taxonomy

③ THÊM, KHÔNG XÓA
   Thêm Multi-Stream explanation, Critical Asymmetry, 6-mechanism sleep
   Không xóa cấu trúc section hiện có — enrich bên trong

④ VERSION BUMP consistent
   Child-Dev files: v2.0 → v2.2 (refine, not rewrite)
   Education-Mechanism files: bump minor version
   Education-System files: bump minor version
```

---

## Dependency Map

```
NGUỒN (đã xong, KHÔNG SỬA):
  Compile-Taxonomy.md v3.0  ← SOURCE OF TRUTH cho compile architecture
  Compile-Sleep.md v1.0     ← SOURCE OF TRUTH cho sleep mechanism

TIER 1 — MECHANISM FILES (sửa trước, vì downstream reference):
  ┌─────────────────────────────────────────────────────┐
  │ S1: Child-Development-Mechanism.md  v2.0 → v2.2    │
  │     §2 reframe + §3 multi-stream + sleep alignment  │
  │     + Critical Asymmetry + Trust/Experience mapping  │
  │     ~2,641L → ~2,900-3,000L (thêm ~300L)           │
  │                                                     │
  │ S2: Education-Mechanism.md  v2.0 → v2.1             │
  │     §2 architecture reframe + §2.8 sleep enrichment │
  │     + Trust/Experience/Expertise mapping             │
  │     + Critical Asymmetry cho arc design              │
  │     ~1,713L → ~1,900L (thêm ~200L)                 │
  └─────────────────────────────────────────────────────┘
        ↓ downstream reference

TIER 2 — PRACTICAL FILES (reference Mechanism, cần align):
  ┌─────────────────────────────────────────────────────┐
  │ S3: Natural-Development.md  v2.1 → v2.2            │
  │     §3 sleep reframe (6-mechanism) + §1 terminology │
  │     ~2,405L → ~2,500L (thêm ~100L)                 │
  │                                                     │
  │ S4: Skill-Introduction.md  v2.1 → v2.2             │
  │     §2 Trust vs Experience mapping cho 4-step       │
  │     + Multi-Stream tag clarification                │
  │     ~2,277L → ~2,400L (thêm ~120L)                 │
  │                                                     │
  │ S5: Compile-Type-Learning.md  v1.2 → v1.3          │
  │     Align architecture 1E+3M + Multi-Stream         │
  │     + Trust=Amplifier distinction                   │
  │     ~1,235L → ~1,350L (thêm ~120L)                 │
  └─────────────────────────────────────────────────────┘
        ↓ downstream reference

TIER 3 — APPLICATION FILES (high-level, inherit từ Tier 1-2):
  ┌─────────────────────────────────────────────────────┐
  │ S6: Education-System.md  v3.0 → v3.1               │
  │     + Compile type awareness per stage              │
  │     + Critical Asymmetry cho teacher role            │
  │     + Sleep section enrich                          │
  │     ~1,627L → ~1,700L (thêm ~80L)                  │
  │                                                     │
  │     Curriculum-Framework.md  v2.1 → v2.2            │
  │     + Per-domain compile type optimal mix            │
  │     ~990L → ~1,030L (thêm ~40L)                    │
  │                                                     │
  │     00_Overview.md  v2.1 → v2.2                     │
  │     + Cross-ref CT v3.0 + CS v1.0                   │
  │     ~380L → ~395L (thêm ~15L)                      │
  └─────────────────────────────────────────────────────┘

TIER 4 — MINOR ALIGNMENT (terminology + cross-refs only):
  ┌─────────────────────────────────────────────────────┐
  │ S6 (same session as Tier 3):                        │
  │   Mother-Optimization.md  v2.1 → v2.2              │
  │     Terminology: "4+1 channel" → "compile engine"   │
  │     ~2,563L → ~2,570L (thay ~10 chỗ)               │
  │                                                     │
  │   Domain-Knowledge-Map.md  v2.0 → v2.1             │
  │     Terminology alignment                           │
  │     ~999L → ~1,010L                                 │
  │                                                     │
  │   Connection-Education.md  v1.0 (MINIMAL)           │
  │     Đã reference CT v3.0 ✅ — chỉ verify           │
  │                                                     │
  │   Expansion-Saturation-Crisis.md  v1.2 (MINIMAL)    │
  │     Đã có Trust/Experience — verify + cross-ref     │
  │                                                     │
  │   Education-Arms-Race.md  v1.3 (MINIMAL)            │
  │     Cross-ref only                                  │
  │                                                     │
  │   Money-Education.md  (MINIMAL)                     │
  │     Cross-ref only                                  │
  │                                                     │
  │   VN files (3 files) — cross-ref updates            │
  │   Era-Analysis-2025.md — cross-ref update           │
  │   Hardware-Calibration.md — cross-ref update         │
  └─────────────────────────────────────────────────────┘
```

---

## Session Plan Chi Tiết

### Session 1: Child-Development-Mechanism.md v2.0 → v2.2

**File:** Research/Human-Learning/Child-Development/Child-Development-Mechanism.md
**Current:** v2.0, 2,641L
**Target:** v2.2, ~2,900-3,000L

**Thay đổi cụ thể:**

```
§2 — "4+1 CHANNEL COMPILE" → REFRAME

  §2.0 (NEW): Compile Architecture Overview
    → 1 Engine (Hebbian) + 3 Modulators + 3 Exposure Channels
    → Diagram showing architecture (thay cho "4+1 kênh")
    → Cross-ref Compile-Taxonomy.md v3.0

  §2.1 (REFRAME): 4 Internal Compile → Compile Engine + Modulators
    → ① Repetition/LTP → = COMPILE ENGINE (Hebbian, bất biến)
    → ② Emotional Peak → = Entity-Valence Bias modulator dominant
    → ③ Multi-modal → = Exposure channel richness (multi > single)
    → ④ Sleep → = Offline Maintenance (NOT kênh compile ngang hàng)
        → Cross-ref Compile-Sleep.md v1.0 (6 mechanisms)
        → Thêm note: "Trẻ sơ sinh ngủ 14-17h → ~4.5 optimization + ~1.5 replay"
    → VÍ DỤ CỤ THỂ KHÔNG ĐỔI — chỉ reframe heading + cơ chế

  §2.2 (REFRAME): External Install → Trust Compile Channel
    → 5 cơ chế external (co-attention, imitation, social referencing,
      label, cultural) = Trust Compile pathway
    → Map: Trust Compile = fast bootstrap, Experience Compile = slow verify
    → ADD: Trust → Experience transition mechanism
    → Cross-ref Compile-Type-Learning.md v1.2

  §2.5 (ADD ~100L): Multi-Stream Compile for Child Development
    → 4 streams: Content / Value / Entity / Behavior
    → VD trẻ: chạm lửa 1 lần →
        Content: "lửa = nóng" (compiled)
        Value: "lửa = nguy hiểm" (avoidance tag)
        Entity: "mẹ nói đúng" (trust +)
        Behavior: "rụt tay" (avoidance motor)
    → = 4 compilations KHÁC NHAU từ 1 event
    → Giải thích "biết nhưng vẫn chạm lại" = Content compiled,
      Behavior chưa compiled đủ mạnh (trẻ nhỏ)

§3 — APPROACH/AVOIDANCE TAG (ENRICH, không restructure)

  §3.1 (ADD ~50L): Multi-Stream Tag Clarification
    → Tag approach/avoidance ÁP DỤNG chủ yếu cho VALUE + BEHAVIOR stream
    → CONTENT stream compile KHÔNG PHỤ THUỘC tag
    → = "Giỏi toán nhưng ghét toán" ở trẻ = Value avoidance, Content OK
    → = Reframe "cùng nội dung khác tag" → chính xác hơn:
        "cùng exposure → content compile GIỐNG, value compile KHÁC"

  §3.2 (ADD ~50L): Critical Asymmetry Cho Parenting
    → PFC → Entity-Valence: mẹ GIẢI THÍCH "toán quan trọng" = CHẬM, tốn PFC
    → Entity-Valence → PFC: mẹ tạo TRẢI NGHIỆM vui với toán = NHANH, free
    → = "Làm mẫu + tạo hứng thú" > "giải thích + thuyết phục"
    → = Tại sao Hardware-Subsidy (mẹ bên cạnh) hiệu quả hơn lời nói

§8 hoặc §11 — CROSS-REFERENCES update
    → Thêm: Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
    → Update dependency list trong frontmatter
```

**Dependencies:** Compile-Taxonomy.md v3.0 ✅, Compile-Sleep.md v1.0 ✅
**Backup:** v2.0 → backup/

---

### Session 2: Education-Mechanism.md v2.0 → v2.1

**File:** Research/Human-Learning/Education-Mechanism/Education-Mechanism.md
**Current:** v2.0, 1,713L
**Target:** v2.1, ~1,900L

**Thay đổi cụ thể:**

```
§0 (UPDATE): Dependencies + position
    → Thêm CT v3.0 + CS v1.0 vào dependency list

§1 (REFRAME ~30L): Context Shift section
    → "4+1 kênh compile" → "1 Engine + 3 Modulators"
    → 5-parameter formula VẪN ĐÚNG — chỉ context architecture

§2 — ARC DESIGN PRINCIPLES (ENRICH)

  §2.2 (ADD ~40L): Multi-Stream cho Direction > Level
    → Approach/avoidance tag = VALUE + BEHAVIOR stream
    → Content compile KHÔNG phụ thuộc direction
    → = "Ép vẫn học được NỘI DUNG — nhưng VALUE compile = avoidance"
    → = Arc design cần optimize VALUE stream, không chỉ content delivery

  §2.6 (ADD ~30L): Critical Asymmetry cho Imagine-Final
    → Teacher tạo Imagine-Final qua Entity-Valence path (nhanh, rẻ)
      > Teacher giải thích Imagine-Final qua PFC path (chậm, đắt)
    → = "Show, don't tell" có cơ sở cơ chế

  §2.8 (ENRICH ~80L): Sleep Consolidation → Sleep Maintenance
    → Reframe: sleep = offline maintenance (NOT kênh compile)
    → Thêm: 6 mechanisms tóm tắt (detail → CS v1.0)
        SHY (prune weak) | Replay (re-exposure) | Active Consolidation (RAM→ROM)
        Creative Linking (REM novel combo) | Emotional Decoupling | Gist Extraction
    → Thêm: sleep deprivation = PFC degrades FIRST
    → Thêm: waking rest ≈ 30% (DMN, incubation — KHÔNG thay thế sleep)
    → KẾT LUẬN VẪN ĐÚNG: "ngủ đủ = phần của học" — mechanism CHÍNH XÁC hơn

  (NEW §2.9 or insert): Trust/Experience/Expertise Compile × Arc Design
    → Trust Compile: fast install, phase 1 (bootstrap)
    → Experience Compile: slow verify, phase 2 (depth)
    → Expertise Compile: years, phase 3 (mastery)
    → Arc design = optimize TRANSITION Trust → Experience
    → Cross-ref Compile-Type-Learning.md v1.2 §3

§3 — BRIDGE (ADD ~20L)
    → Bridge = shift Entity-Valence Bias toward subject
    → Critical Asymmetry: entity-based bridge > PFC-based explanation
    → = "Love the teacher" = Entity-Valence path = fastest bridge

§6 — CROSS-REFERENCES update
```

**Dependencies:** Session 1 (Child-Dev-Mechanism) done first
**Backup:** v2.0 → backup/

---

### Session 3: Natural-Development.md v2.1 → v2.2 + Skill-Introduction.md v2.1 → v2.2

**2 files cùng session vì changes nhỏ hơn và liên quan chặt.**

**File 1: Natural-Development.md**
**Current:** v2.1, 2,405L
**Target:** v2.2, ~2,500L

```
§1 (TERMINOLOGY ~10 replacements):
    → "4+1 kênh compile" → "Compile Engine + Modulators"
    → "compile channel" → "compile architecture"
    → Nhẹ nhàng, không restructure

§3 — GIẤC NGỦ (ENRICH ~80L):
  §3.1 (REFRAME):
    → "3 chương trình chạy khi ngủ" → "6 cơ chế offline maintenance"
    → Nhóm lại:
      Optimization (majority): SHY + Active Consolidation + Emotional Decoupling
      Exposure-related (minority): Hippocampal Replay + Creative Linking + Gist
    → "Ngủ = não ĐANG MAINTENANCE" (thay cho "não đang compile")
    → VẪN GIỮ practical content (thời lượng ngủ, nap, REM...)

  §3.2 (ADD note):
    → REM 50% ở sơ sinh → phần lớn = Circuit Testing + Creative Linking
    → Emotional Decoupling ở trẻ = calibrate initial emotional tags

  §3.4 (ADD note):
    → Nap = consolidation window → enrich: nap 20min vs 90min khác mechanism
    → 20min: SHY partial + light replay
    → 90min: full cycle → SHY + Replay + Creative Linking possible

§7 (ADD ~15L): Multi-Stream observation
    → Bố mẹ observe body signal → giờ phân biệt rõ hơn:
    → Trẻ "biết" nhưng "không làm" = Content compiled, Behavior chưa compiled
    → = BÌNH THƯỜNG, không phải "hư"
```

**File 2: Skill-Introduction.md**
**Current:** v2.1, 2,277L
**Target:** v2.2, ~2,400L

```
§1 (ADD ~30L): Trust vs Experience Compile mapping
    → Bước 1-3 ≈ Experience Compile pathway (trải nghiệm trực tiếp)
    → Bước 4 External instruction = Trust Compile install
    → OPTIMAL = Trust bootstrap (bước 4) → Experience verify (practice)
    → = 4 bước KHÔNG CHỈ gắn tag đúng — còn đảm bảo
      Experience Compile DẪN TRƯỚC Trust Compile
    → Cross-ref Compile-Type-Learning.md v1.2 §3

§2 (ADD ~40L): Multi-Stream × 4-step
    → Bước 1-2: chủ yếu VALUE stream compile (approach/neutral)
    → Bước 3: VALUE + CONTENT + BEHAVIOR stream bắt đầu
    → Bước 4: CONTENT stream dominant + VALUE đã positive
    → = Skip bước 1-3 → Value stream = avoidance → dù Content compile OK
      → "biết nhưng ghét" = failure mode chính

§2.5 (ADD ~20L): Withdrawal qua Multi-Stream lens
    → "Con muốn dừng" CÓ THỂ =
      a) Value stream avoidance (cách dạy sai) → đổi approach
      b) Content satiation (đã compile đủ) → move on
      c) Habituation (VTA) → thêm novelty
    → Phân biệt rõ hơn nhờ multi-stream

§2.6 (ADD ~30L): Critical Asymmetry × Skill
    → Bố mẹ giải thích "piano quan trọng" = PFC path → CHẬM
    → Bố mẹ chơi piano vui trước mặt con = Entity-Valence path → NHANH
    → = "Sống mẫu" có cơ sở cơ chế rõ ràng
    → Hardware-Subsidy + Entity-Valence = compound approach tag
```

**Dependencies:** Session 1 done (Mechanism updated → refs correct)

---

### Session 4: Compile-Type-Learning.md v1.2 → v1.3

**File:** Research/Human-Learning/Education-Mechanism/Compile-Type-Learning.md
**Current:** v1.2, 1,235L
**Target:** v1.3, ~1,350L

```
§0 (UPDATE): Cross-ref CT v3.0 + CS v1.0

§1 (REFRAME ~40L): 3 Compile Types → Dominant Modulator Configurations
    → Experience Compile = Engine + minimal modulators, External dominant
    → Trust Compile = Engine + Entity-Valence Bias dominant, fast bootstrap
    → Expertise Compile = Engine + PFC Modulation sustained, years
    → = CÙNG Engine, KHÁC modulator mix → KHÁC output quality
    → ADD: Trust = Amplifier (NOT Gate) distinction
      → Áp dụng cho VALUE compile, KHÔNG phải content
      → = "Giỏi nhưng ghét" chính xác hóa

§1.4 (ADD ~30L): Multi-Stream × Pi Example
    → Archimedes (Experience): Content ✓ + Value ✓ (approach, tự tìm)
    → Student rote (Trust only): Content ✓ + Value ✗ (neutral/avoidance)
    → Curious student (Trust → Experience): Content ✓ + Value ✓ (approach, verify)
    → = Multi-Stream giải thích TẠI SAO cùng π nhưng khác output

§4 (ADD ~20L): Per-Domain → Multi-Stream insight
    → Toán 60% Trust: Content stream OK qua Trust, Value stream CẦN Experience
    → Sport 99% Experience: cả 4 streams compile qua Experience → integrated
    → Screen: Content stream partial, VALUE + ENTITY stream gần zero
      → = Screen Trust Compile WEAKEST FORM vì chỉ compile 1/4 streams

§5 (ADD ~20L): Body-Check = Multi-Stream verification
    → Mechanical repetition: Content stream strengthen, Value stream UNCHANGED
    → Body-check repetition: Content + Value + Behavior streams ALL update
    → = Body-check = MULTI-STREAM compile, mechanical = SINGLE-STREAM

§6 (ADD ~10L): Cross-ref CT v3.0 + CS v1.0 cho design principles
    → Thêm: "Sleep consolidation khác nhau per compile type"
      → Experience Compile: nhiều Replay + Gist (multi-modal data)
      → Trust Compile: nhiều Active Consolidation (RAM→ROM transfer)
      → Expertise Compile: nhiều Creative Linking (novel combinations)

§8 CROSS-REFERENCES update
```

**Dependencies:** Session 1-2 done

---

### Session 5: Education-System.md v3.0 → v3.1 + Curriculum-Framework.md v2.1 → v2.2

**2 files cùng session — changes moderate.**

**File 1: Education-System.md**
**Current:** v3.0, 1,627L → v3.1, ~1,700L

```
§1 (ADD ~30L): Compile Architecture awareness
    → Education = guided compile optimization
    → 1 Engine + 3 Modulators → education DESIGN modulators, KHÔNG thay engine
    → Trust Compile = primary education pathway → cần design transition to Experience

§2 (ADD ~20L per stage): Per-Stage Compile Type awareness
    → Stage 2 (6-12): Trust Compile dominant (teacher install)
      + Experience verify (practice, projects)
    → Stage 3 (12-18): Trust → Experience transition critical
      + Expertise Compile seeds (depth domains)
    → Stage 4 (18+): Expertise Compile dominant
      + Trust Compile for new domains

§7 (ADD ~30L): Teacher Role × Critical Asymmetry
    → Teacher Entity-Valence path > Teacher PFC instruction path
    → = "Thầy/cô mà học sinh TIN = value compile approach"
    → = "Thầy/cô giải thích hay = content compile OK, value có thể neutral"
    → = Entity-Access Mức 3-4 + Critical Asymmetry = most effective teaching

§2.8 reference update: → CS v1.0, 6-mechanism framework
```

**File 2: Curriculum-Framework.md**
**Current:** v2.1, 990L → v2.2, ~1,030L

```
§2 (ADD ~20L): Foundation Delivery × Compile Type
    → Literacy: Trust Compile dominant (phonics rules) + Experience verify (reading practice)
    → Numeracy: DANGER zone — Trust Compile avoidance tag phổ biến nhất
      → Need Experience Compile first (concrete manipulation)
    → Somatic: Experience Compile ~99% (no shortcut)
    → Social: Trust Compile 30% (frameworks) + Experience 70% (interaction)
    → Creative: Experience Compile dominant — Trust Compile can KILL (§3 Arms Race)
    → Meta-learning: Trust Compile for strategies + Experience for self-observation

§4 (ADD ~20L): Sequencing × Multi-Stream
    → Per-stage: ensure VALUE stream positive BEFORE content volume increases
    → Stage 2: VALUE stream priority (make learning enjoyable FIRST)
    → Stage 3: CONTENT volume can increase IF value stream approach
    → = Sequencing = VALUE stream first, CONTENT stream second
```

---

### Session 6: Minor Alignment — Terminology + Cross-refs (~8-10 files)

**Batch session: nhỏ, nhanh, chủ yếu find-replace + cross-ref updates**

```
FILES:
  Mother-Optimization.md  v2.1 → v2.2
    → ~10 replacements: "4+1 kênh/channel compile" → "compile architecture"
    → Cross-ref update: + CT v3.0, CS v1.0

  Domain-Knowledge-Map.md  v2.0 → v2.1
    → Terminology alignment: "4+1 compile" → architecture ref
    → Cross-ref update

  Connection-Education.md  v1.0 — VERIFY ONLY
    → Đã ref CT v3.0 ✅ — verify consistency

  Expansion-Saturation-Crisis.md  v1.2 — VERIFY + cross-ref
    → Đã dùng Trust/Experience — verify aligned

  Education-Arms-Race.md  v1.3 — cross-ref update

  Money-Education.md — cross-ref update

  00_Overview.md  v2.1 → v2.2
    → Add CT v3.0 + CS v1.0 vào dependency section

  Era-Analysis-2025.md  v2.1 — cross-ref update

  Hardware-Calibration.md  v1.1 — cross-ref update

  VN-Education-Status.md  v2.1 — cross-ref update
  VN-Recommendations.md  v2.1 — cross-ref update
  VN-Cultural-Factors.md  v2.1 — cross-ref update
```

---

## Tổng kết scope

```
┌─────────┬──────────────────────────────────────┬────────────┬──────────┐
│ Session │ Files                                │ Lines thêm │ Priority │
├─────────┼──────────────────────────────────────┼────────────┼──────────┤
│ S1      │ Child-Dev-Mechanism v2.0 → v2.2     │ +300L      │ ★★★★★   │
│ S2      │ Education-Mechanism v2.0 → v2.1     │ +200L      │ ★★★★★   │
│ S3      │ Natural-Dev v2.1→v2.2 + Skill v2.2  │ +200L      │ ★★★★    │
│ S4      │ Compile-Type-Learning v1.2 → v1.3   │ +120L      │ ★★★★    │
│ S5      │ Education-System v3.1 + Curriculum   │ +120L      │ ★★★     │
│ S6      │ ~10 files minor alignment            │ +50L       │ ★★      │
├─────────┼──────────────────────────────────────┼────────────┼──────────┤
│ TOTAL   │ ~16 files                            │ +990L      │          │
└─────────┴──────────────────────────────────────┴────────────┴──────────┘

So sánh:
  Post-drill v2.1 refine (2026-05-25): ~19 phases, ~200 repl, ~55 files
  Plan này: 6 sessions, ~990L additions, ~16 files
  = MODERATE scope — lớn hơn terminology fix, nhỏ hơn rewrite
```

---

## Checklist per-session

```
TRƯỚC mỗi session:
  □ Compact session trước
  □ Đọc lại CT v3.0 + CS v1.0 relevant sections
  □ Đọc file target TOÀN BỘ
  □ Verify dependencies đã done

SAU mỗi session:
  □ File backup (old version → backup/)
  □ Version bump trong frontmatter
  □ Cross-references updated
  □ Dependencies updated
  □ Verify: ví dụ cụ thể VẪN chính xác
  □ Verify: kết luận thực tế KHÔNG thay đổi
  □ Memory file update
```

---

## Open Questions

```
Q1: Compile-Type-Learning.md v1.2 có nên đổi tên thành Compile-Education.md?
    → v1.2 scope rộng hơn "type learning" — cover compile × education analysis
    → Nhưng rename = cascade cross-ref changes → cost cao
    → DEFER: giữ tên, note trong file

Q2: Education-System.md §2.8 sleep section có nên deep hơn?
    → Hiện tại 1 paragraph + ref
    → CS v1.0 có 1,318L detail
    → Education-System = APPLICATION layer → KHÔNG cần duplicate
    → KEEP: short summary + cross-ref CS v1.0

Q3: Child-Dev files cần thêm "3 Compile Types" per-age mapping không?
    → Trẻ 0-6: chủ yếu Experience Compile (body trải nghiệm)
    → Trust Compile emerge từ ~12m+ (social referencing, label)
    → Expertise Compile = KHÔNG có ở 0-6 (cần years)
    → KEEP in Compile-Type-Learning → reference from Child-Dev

Q4: Propagation tới Core-Deep-Dive/ files cần không?
    → Chunk.md v2.3 — đã reference CT v3.0
    → Body-Base.md — may need terminology alignment
    → DEFER: separate plan if needed
```
