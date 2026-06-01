# Plan 1/3: Compile Architecture Refine — Child-Development/

> **Created:** 2026-06-01
> **Trigger:** Compile-Taxonomy.md v3.0 + Compile-Sleep.md v1.0 → 8 reframes chưa lan tới Child-Dev
> **Scope:** 4 files trong Child-Development/ → refine (KHÔNG rewrite toàn bộ)
> **Approach:** Rà soát + refine từng file. Chất lượng > tốc độ.
> **Dependency:** PLAN NÀY ĐI TRƯỚC. Plan 2 (Education-Mechanism/) + Plan 3 (Education-System/) đứng trên nền plan này.

---

## 8 Reframes cần lan (từ CT v3.0 + CS v1.0)

```
R1: "4+1 Channel Compile" → "1 Engine (Hebbian) + 3 Modulators + 3 Exposure Channels"
R2: Trust = Amplifier (gradient Mức 0-5), KHÔNG phải Gate (binary)
R3: Multi-Stream Compile: Content/Value/Entity/Behavior song song
R4: Critical Asymmetry: PFC→Entity-Valence CHẬM, Entity-Valence→PFC NHANH
R5: 3 Compile Types = Dominant Modulator Configurations (Experience/Trust/Expertise)
R6: Sleep = Offline Maintenance (6 mechanisms, ~1.5 exposure + ~4.5 optimization)
R7: Sleep × Architecture interactions (Engine, Entity-Valence, Exposure Channels, PFC)
R8: Waking Rest ≈ 30% only
```

---

## Nguyên tắc refine

```
① NỘI DUNG CỤ THỂ KHÔNG ĐỔI — chỉ reframe CƠ CHẾ MÔ TẢ
   VÍ DỤ: bò, chạm lửa, piano, bơi, toán → TẤT CẢ VẪN ĐÚNG
   Approach/avoidance tag → VẪN ĐÚNG — chỉ ENRICH thêm multi-stream

② KẾT LUẬN THỰC TẾ KHÔNG ĐỔI
   "Ngủ đủ" → chỉ giải thích CHÍNH XÁC hơn TẠI SAO (6 mechanisms)
   "Cách dạy quyết định tag" → thêm chiều VALUE vs CONTENT
   "Phòng >> Chữa" → giữ nguyên

③ THÊM, KHÔNG XÓA
   Thêm: 1E+3M architecture, Multi-Stream, Critical Asymmetry, 6-mechanism sleep
   Không xóa cấu trúc section hiện có — enrich bên trong

④ VERSION BUMP
   v2.0/v2.1 → v2.2 (refine, not rewrite)
```

---

## File 1: Child-Development-Mechanism.md v2.0 → v2.2 ★★★★★

**Current:** 2,641L | **Target:** ~2,940L (+300L) | **Priority:** HIGHEST

```
FRONTMATTER:
  scope: "4+1 Channel Compile" → "Compile Architecture (1E+3M)"
  + dependencies: Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0

§0.3 (FIX ~3 chỗ):
  "4+1 channel compile (§2)" → "Compile Architecture (§2)"

§2 HEADING:
  OLD: "§2 — 4+1 CHANNEL COMPILE: CHUNKS TÍCH LŨY THẾ NÀO"
  NEW: "§2 — COMPILE ARCHITECTURE: CHUNKS TÍCH LŨY THẾ NÀO"

§2.0 (NEW ~40L): Architecture Overview
  → 1 Engine (Hebbian) + 3 Modulators + 3 Exposure Channels + Sleep Maintenance
  → Diagram: architecture cho child-dev context
  → Cross-ref: Compile-Taxonomy.md v3.0 (chi tiết)
  → KEY: "4 cơ chế ở §2.1 = 4 DẠNG EXPOSURE cho CÙNG 1 ENGINE"
  → "External Install ở §2.2 = Trust Compile pathway"

§2.1 (REFRAME heading + context, giữ ví dụ):
  OLD heading: "4 Kênh Compile Nội Bộ"
  NEW heading: "Compile Engine + 4 Dạng Exposure"

  ① Repetition → thêm note: "= COMPILE ENGINE (Hebbian, bất biến)"
  ② Emotional Peak → thêm: "= Engine + Entity-Valence Bias dominant"
  ③ Multi-modal → thêm: "= Exposure richness (nhiều kênh → compile sâu hơn)"
  ④ Sleep → REFRAME:
    OLD: "Hippocampus replay → cortex transfer → 6+ cơ chế offline"
    (Đã mention 6 cơ chế nhưng chưa phân loại exposure/optimization)
    NEW: Thêm ~30L:
      → Sleep = Offline Maintenance (KHÔNG phải "kênh compile" ngang hàng)
      → 6 mechanisms: ~1.5 exposure + ~4.5 optimization
      → Table tóm tắt 6 mechanisms
      → "Trẻ sơ sinh ngủ 14-17h → ~4.5 optimization + ~1.5 replay"
      → Cross-ref: Compile-Sleep.md v1.0 (chi tiết)
      → KẾT LUẬN VẪN ĐÚNG: "ngủ đủ = non-negotiable"

  TẤT CẢ VÍ DỤ GIỮ NGUYÊN:
    bò 100 lần, nghe "mama" 1000 lần, chạm lửa, bị chó cắn,
    chơi cát, nấu ăn cùng mẹ, tập bò → đêm replay

§2.2 (ENRICH ~20L):
  OLD heading: "Kênh Thứ 5: External Install"
  NEW heading: "Trust Compile: External Install qua Entity-Valence"

  Thêm context:
  → 5 cơ chế external = Trust Compile pathway (Entity-Valence dominant)
  → Trust Compile = fast bootstrap, Experience Compile = slow verify
  → Map: Trust → Experience transition (trẻ nghe mẹ → tự verify)
  → Cross-ref: Compile-Type-Learning.md §3
  → GIỮ NGUYÊN 5 mechanisms + 4 failure modes

§2.6 (NEW ~100L): Multi-Stream Compile for Child Development
  → 4 streams: Content / Value / Entity / Behavior
  → VD trẻ: chạm lửa 1 lần →
      Content: "lửa = nóng" (compiled)
      Value: "lửa = nguy hiểm" (avoidance tag)
      Entity: "mẹ nói đúng" (trust +)
      Behavior: "rụt tay" (motor avoidance)
  → = 4 compilations KHÁC NHAU từ 1 event
  → VD trẻ bị ép học toán →
      Content: compile ✓ (exposure → knowledge)
      Value: compile avoidance ✗ (trust amplifier ≈ 0 cho [toán → tốt])
  → = "Giỏi nhưng ghét toán" = Content ✓ Value ✗
  → VD "biết nhưng vẫn chạm lại" = Content compiled, Behavior chưa compiled đủ
  → Cross-ref: Compile-Taxonomy.md v3.0 §5

§3.1 (ENRICH ~30L): Multi-Stream Tag Clarification
  Sau §3.1 hiện tại (Body-State-at-Compile), thêm subsection:
  → Tag approach/avoidance ÁP DỤNG chủ yếu cho VALUE + BEHAVIOR stream
  → CONTENT stream compile KHÔNG PHỤ THUỘC tag
  → = "Giỏi toán nhưng ghét toán" ở trẻ = Value avoidance, Content OK
  → Reframe chính xác hơn: "cùng exposure → content compile GIỐNG,
    value compile KHÁC tùy body state lúc compile"

§3.2 (ENRICH ~50L): Critical Asymmetry for Parenting — NEW SUBSECTION
  → PFC → Entity-Valence: mẹ GIẢI THÍCH "toán quan trọng" = CHẬM, tốn PFC
  → Entity-Valence → PFC: mẹ tạo TRẢI NGHIỆM vui với toán = NHANH, free
  → = "Làm mẫu + tạo hứng thú" > "giải thích + thuyết phục"
  → = Tại sao Hardware-Subsidy (mẹ bên cạnh) hiệu quả hơn lời nói
  → VD: "Piano quan trọng" (PFC path) vs chơi piano vui (Entity-Valence path)
  → Cross-ref: Compile-Taxonomy.md v3.0 §7

§10 (UPDATE ~5L):
  → §2 confidence note: update "4-channel" → "compile architecture"

§11 (UPDATE ~10L):
  → Thêm: Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  → Update Chunk.md ref: v2.0 → v2.3 (if applicable)

SUMMARY (END):
  → Update "4+1 Channel Compile" → "Compile Architecture (1E+3M)"

BACKUP: v2.0 → backup/
```

---

## File 2: Natural-Development.md v2.1 → v2.2 ★★★★

**Current:** 2,405L | **Target:** ~2,510L (+105L) | **Depends:** File 1 done

```
FRONTMATTER:
  + dependencies: Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  Update: Child-Development-Mechanism.md v2.0 → v2.2

§1 (TERMINOLOGY ~5 replacements):
  "4+1 kênh compile" → "Compile Architecture"
  "4+1 Channel Compile" → "Compile Architecture"
  "kênh compile" → "compile mechanisms"

§2 (~5 replacements):
  "kênh compile đang hoạt động" → "compile engine đang hoạt động"
  "Cơ chế compile: Mechanism §2 (4+1 Channel Compile)"
    → "Cơ chế compile: Mechanism §2 (Compile Architecture)"

§3 — GIẤC NGỦ (REFRAME ~80L):

  §3 intro quote:
    OLD: "Giấc ngủ = 4th compile channel (Sleep Consolidation) — Mechanism §2.1④"
    NEW: "Giấc ngủ = Offline Maintenance System — Mechanism §2.1④ + Compile-Sleep.md v1.0"

  §3.1 (REFRAME content):
    Hiện tại nói "3 chương trình chạy khi ngủ" (cũ, trước CS v1.0)
    → Reframe: "6 cơ chế offline maintenance"
    → Nhóm lại:
      Optimization (majority): SHY + Active Consolidation + Emotional Decoupling
      Exposure-related (minority): Hippocampal Replay + Creative Linking + Gist
    → "Ngủ = não ĐANG MAINTENANCE" (thay cho "não đang compile")
    → VẪN GIỮ: practical content (thời lượng ngủ, nap, REM)

  §3.2 (ADD note ~10L):
    → REM 50% ở sơ sinh → phần lớn = Circuit Testing + Creative Linking
    → Emotional Decoupling ở trẻ = calibrate initial emotional tags

  §3.4 (ADD note ~10L):
    → Nap = maintenance window → enrich:
      20min nap: SHY partial + light replay
      90min nap: full cycle → SHY + Replay + Creative Linking possible

§7 (ADD ~15L): Multi-Stream observation
  → Trẻ "biết" nhưng "không làm" = Content compiled, Behavior chưa compiled
  → = BÌNH THƯỜNG, không phải "hư"
  → Cross-ref: Mechanism §2.6 (Multi-Stream)

§10 CROSS-REFERENCES:
  + Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  Update: Mechanism.md v2.0 → v2.2

BACKUP: v2.1 → backup/
```

---

## File 3: Skill-Introduction.md v2.1 → v2.2 ★★★★

**Current:** 2,277L | **Target:** ~2,400L (+123L) | **Depends:** File 1 done

```
FRONTMATTER:
  + dependencies: Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  Update: Mechanism.md v2.0 → v2.2

INTRO QUOTE (line 76):
  OLD: "Cơ chế chunks: → Mechanism.md §2 (4+1 Channel Compile)."
  NEW: "Cơ chế chunks: → Mechanism.md §2 (Compile Architecture)."

§1 (ADD ~30L): Trust vs Experience Compile mapping cho 4-step
  Sau §1 nguyên tắc xuyên suốt, thêm:
  → Bước 1-3 ≈ Experience Compile pathway (trải nghiệm trực tiếp)
  → Bước 4 (External instruction) = Trust Compile install
  → OPTIMAL: Experience DẪN TRƯỚC Trust
  → 4 bước = đảm bảo Experience Compile build approach tags
    TRƯỚC KHI Trust Compile install content
  → Cross-ref: Compile-Type-Learning.md v1.2 §3

§2 (ADD ~40L): Multi-Stream × 4-step
  → Bước 1-2: chủ yếu VALUE stream compile (approach/neutral)
  → Bước 3: VALUE + CONTENT + BEHAVIOR stream bắt đầu
  → Bước 4: CONTENT stream dominant + VALUE đã positive
  → = Skip bước 1-3 → Value stream = avoidance → "biết nhưng ghét"

§2 Withdrawal (ADD ~20L): Multi-Stream lens
  → "Con muốn dừng" CÓ THỂ =
    a) Value stream avoidance (cách dạy sai) → đổi approach
    b) Content satiation (đã compile đủ) → move on
    c) Habituation (VTA) → thêm novelty
  → Phân biệt rõ hơn nhờ multi-stream

§2 (ADD ~30L): Critical Asymmetry × Skill — NEW SUBSECTION
  → "Piano quan trọng" = PFC path → CHẬM
  → Chơi piano vui trước mặt con = Entity-Valence path → NHANH
  → = "Sống mẫu" có cơ sở cơ chế rõ ràng
  → Hardware-Subsidy + Entity-Valence = compound approach tag

§2 reference updates (~3 chỗ):
  "Mechanism §2: 4+1 channel" → "Mechanism §2: Compile Architecture"
  "4+1 Channel Compile" → "Compile Architecture"

§11 CROSS-REFERENCES:
  + Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  Update: Mechanism.md v2.0 → v2.2

BACKUP: v2.1 → backup/
```

---

## File 4: Mother-Optimization.md v2.1 → v2.2 ★★

**Current:** 2,563L | **Target:** ~2,575L (+12L) | **Depends:** File 1 done

```
ĐẶC THÙ: File này MEDICAL-HEAVY — framework lens NHẸ.
→ Chỉ cần terminology alignment + cross-ref update.
→ KHÔNG cần thêm Multi-Stream hay Critical Asymmetry
  (prenatal context = trước khi compile types relevant).

FRONTMATTER:
  + dependencies: Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  Update: Mechanism.md v2.0 → v2.2

TERMINOLOGY (~10 replacements):
  "4+1 compile" → "Compile Architecture"
  "4+1 kênh compile" → "Compile Architecture"
  "4+1 channel compile" → "Compile Architecture"
  "kênh compile" → "compile mechanism" (context-dependent)
  "chunk compile channels" → "compile architecture"
  "Mechanism §2.1 kênh ④: sleep consolidation"
    → "Mechanism §2.1④: Sleep Maintenance (Compile-Sleep.md v1.0)"

CROSS-REFERENCES (§12):
  + Compile-Taxonomy.md v3.0, Compile-Sleep.md v1.0
  Update: Mechanism.md v2.0 → v2.2

BACKUP: v2.1 → backup/
```

---

## Thứ tự thực hiện

```
┌─────┬──────────────────────────────┬──────────┬──────────┐
│ #   │ File                         │ Lines +  │ Priority │
├─────┼──────────────────────────────┼──────────┼──────────┤
│  1  │ Child-Dev-Mechanism v2.2     │ +300L    │ ★★★★★   │
│  2  │ Natural-Development v2.2     │ +105L    │ ★★★★    │
│  3  │ Skill-Introduction v2.2      │ +123L    │ ★★★★    │
│  4  │ Mother-Optimization v2.2     │  +12L    │ ★★      │
├─────┼──────────────────────────────┼──────────┼──────────┤
│     │ TOTAL                        │ +540L    │          │
└─────┴──────────────────────────────┴──────────┴──────────┘

File 1 PHẢI xong trước — các file khác reference nó.
File 2+3 có thể cùng session (nếu compact sạch).
File 4 nhẹ — có thể gộp vào session File 2 hoặc 3.
```

---

## Checklist per-file

```
TRƯỚC mỗi file:
  □ Đọc file target TOÀN BỘ
  □ Đọc CT v3.0 + CS v1.0 relevant sections
  □ Verify dependencies đã done (File 1 xong trước)

SAU mỗi file:
  □ Version bump trong frontmatter
  □ Old version → backup/
  □ Cross-references updated
  □ Dependencies updated
  □ Verify: VÍ DỤ CỤ THỂ vẫn chính xác
  □ Verify: KẾT LUẬN THỰC TẾ không thay đổi
  □ Verify: new concepts (Multi-Stream, Critical Asymmetry) consistent với CT v3.0
```

---

## Sau Plan 1 hoàn thành

```
→ Compact session
→ Chuyển sang Plan 2: Education-Mechanism/ (7 files)
  Plan 2 reference Child-Dev files ĐÃ REFINE → consistent
→ Plan 2 xong → Plan 3: Education-System/ (8 files)
```
