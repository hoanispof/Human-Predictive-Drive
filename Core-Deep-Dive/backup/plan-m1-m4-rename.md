# Plan: M1-M4 Rename — M1-M4 → Compiled-Suppress / Habituation / Prediction-Completion / Entity-Saturation

```
Status:    📁 SUPERSEDED → xem Plan-rename-m1-Mn/ (4 sub-plans)
           Plan cũ giữ làm THAM KHẢO (audit log, collision analysis).
Created:   2026-05-23
Audited:   2026-05-29 (full grep \bM[1-5]\b, 7-system disambiguation)
Split:     2026-05-29 → Plan-rename-m1-Mn/ folder:
             Plan-L-Love-Quality.md       (⑦ 1 file, ~6 occ)
             Plan-E-Entity-Profile.md     (② 1-2 files, ~80 occ)
             Plan-F-Firing-Modes.md       (③④ 3-4 files, ~30 occ)
             Plan-R-Resonance-Decline.md  (① ~46 files, ~545 occ)
           Thứ tự: L → E → F → R
Scope:     ~50 active files, ~580 replacements (Resonance Decline system)
           — LỚN HƠN ước lượng ban đầu (~34 file/455). Plan cũ undercount.
           + Collision FIX: Firing Modes (3 file), Entity Profile (1 file)
           + ⭐ PHÁT HIỆN MỚI: Love Quality Dims M1-M4 (hệ ⑦, plan cũ bỏ sót)
Approach:  CLUSTER-BY-CLUSTER (Source → Consumers → Education/Melody → Mixed/Collision)
Depends:   KHÔNG. Chạy ĐỘC LẬP.
Verify:    grep "\bM[1-4]\b" = 0 trong Resonance Decline context files
           (KHÔNG đếm các hệ M-label khác — xem §3.3 SKIP list)

⭐ QUYẾT ĐỊNH ĐÃ CHỐT (2026-05-29):
  D1. Scope = FULL (gồm Education/Child-Dev/Melody/Core-Software; loại false-positives)
  D2. Firing Modes → TÊN MÔ TẢ + align về Valence-Propagation + reconcile 3-vs-4
  D3. Entity Profile M1-M5 → BỎ SỐ, dùng tên mô tả (① Hardware subsidy...)
```

---

## §0 — TẠI SAO ĐỔI TÊN

### 3 lý do chính

**① M1-M4 KHÔNG MANG NGHĨA**

```
  "M1 ACCELERATE M2+M3+M4" — ai biết M1 là gì?
  → Phải tra Bond-Architecture.md §4 mỗi lần gặp

  "Compiled-Suppress ACCELERATE Habituation+Prediction-Completion+Entity-Saturation"
  → Ngay lập tức hiểu: suppress drive riêng → 3 cơ chế kia tăng tốc
```

**② TRÙNG KÝ HIỆU VỚI 5 HỆ THỐNG KHÁC (KHÔNG phải 4 — audit phát hiện hệ ⑥)**

```
  Framework hiện tại có 6 hệ thống M-labels:

  ① RESONANCE DECLINE (Bond-Architecture §4 / By-Product-Gap-Resonance §10 /
     Connection v5.0 §4.5 / Boredom v2.0):
     M1 = Compiled suppress gap riêng
     M2 = Habituation (Weber-Fechner)
     M3 = Prediction completion
     M4 = Entity-Compiled saturation
     → ~50 files, ~580 occ — PLAN NÀY RENAME

  ② ENTITY PROFILE PARAMETERS (Resonance-Per-Entity §3):
     M1. Hardware subsidy | M2. Compilation path | M3. Cost profile
     M4. 2-tầng proportion | M5. 2-luồng proportion
     → 1 file, ~30 occ — COLLISION FIX (D3: bỏ số → tên mô tả)

  ③ PFC FIRING MODES (Body-Base §5.3, Domain-Mapping, Discovery-vs-Expansion):
     ⚠️ 3 TAXONOMY KHÁC NHAU mang cùng tên "firing modes":
       Body-Base + Discovery:  M1 Tonic / M2 Phasic / M3 Compound / M4 Cascade
       Domain-Mapping:         M1 Structural / M2 Current-Shift / M3 Peak / M4 Compound
       Valence-Propagation v3.0 (canonical?): Maintenance / Chunk-Miss / Context-Trigger (3 modes!)
     → 3 files, ~25 occ — ⚠️ ERROR: cross-ref Bond-Architecture §M1-M4 SAI
       + mâu thuẫn 3-vs-4 modes — COLLISION FIX (D2)

  ④ MOTOR DEVELOPMENT EVENTS (Child-Chunk-Development arcs):
     M1 = Palmar grasp, M2 = Rooting, M3 = Moro, M4 = Stepping, M5 = Hand-to-mouth
     → MODALITY ARC CODE (V1/A1/M1/B1/I1) — SKIP

  ⑤ PFC DAMAGE MECHANISMS (Drill-Body-Feedback 01/02/03/04):
     M1 = Temporary recovery, M2 = Neural wear/damage
     → SEPARATE SCOPE — SKIP

  ⑥ MICRO EXAMPLE CODES (Anchor-Schema-Example.md) ⭐ AUDIT PHÁT HIỆN:
     M1. ĐƯA TAY LẤY LY NƯỚC | M2. GÕ PHÍM | M3. BƯỚC XUỐNG CẦU THANG...
     Spectrum: Micro(M1-M5) → Short(S1-S5) → Daily(D1-D5) → Long(L1-L5) → eXtreme(X1-X5)
     → "M" = "Micro" example code — SKIP (plan CŨ xếp NHẦM vào rename!)

  + Bonus collision (không phải M nhưng cùng dạng): Quote-Analysis "M1: Meta-insight"
     → SKIP (plan CŨ xếp NHẦM vào rename!)
```

**③ TÊN THAY THẾ ĐÃ ĐƯỢC DÙNG INLINE**

```
  Framework ĐÃ LUÔN viết kèm inline label:
  → "M1 compiled suppress" → chỉ cần bỏ "M1"
  → "M2 habituation" → chỉ cần bỏ "M2"
  → "M3 prediction completion" → chỉ cần bỏ "M3"
  → "M4 Entity-Compiled saturation" → chỉ cần bỏ "M4"
```

---

## §1 — ĐỊNH NGHĨA TÊN MỚI

### §1.1 — Tên chính thức (Resonance Decline)

```
  ┌──────────┬─────────────────────────┬──────────────────────────────────┐
  │ Hiện tại │ Tên mới                 │ Lý do                            │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M1       │ Compiled-Suppress       │ Suppress drive riêng → mất       │
  │          │                         │ nguồn by-products. STRONGEST.   │
  │          │                         │ Accelerator cho 3 cơ chế kia.   │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M2       │ Habituation             │ Weber-Fechner. Cùng stimulus    │
  │          │                         │ → VTA giảm fire → reward giảm.  │
  │          │                         │ Hardware tự nhiên. ĐỘC LẬP.     │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M3       │ Prediction-Completion   │ Self-Pattern-Modeling quá        │
  │          │                         │ accurate → delta = 0 → hết     │
  │          │                         │ novelty. Gap vẫn CÓ nhưng      │
  │          │                         │ không fill MỚI.                 │
  ├──────────┼─────────────────────────┼──────────────────────────────────┤
  │ M4       │ Entity-Saturation       │ Entity-Compiled formation       │
  │          │                         │ 40→200h diminishing returns.    │
  │          │                         │ Ít chunks MỚI về partner.       │
  └──────────┴─────────────────────────┴──────────────────────────────────┘

  Grouped label:
  → "M1-M4" → "4 Decline mechanisms"
  → "M1-M4 Resonance Decline" → "4 Resonance-Decline mechanisms"
  → Short context: "Compiled-Suppress through Entity-Saturation"
```

### §1.2 — Viết hoa / viết thường

```
  ⭐ QUY TẮC:

  Compiled-Suppress / Habituation / Prediction-Completion / Entity-Saturation
  = CAPITALIZED + HYPHENATED (concept names)

  Short forms khi context ĐÃ RÕ (trong formulas, tables):
  → "Suppress" / "Habituation" / "Completion" / "Saturation"
  → KHÔNG viết tắt thành CS/H/PC/ES

  Formulas:
  → "Compiled-Suppress ACCELERATE Habituation+Prediction-Completion+Entity-Saturation"
  → Hoặc ngắn: "Suppress ACCELERATE Habituation+Completion+Saturation"
```

### §1.3 — Compound terms

```
  ┌────────────────────────────────────┬──────────────────────────────────────┐
  │ Hiện tại                           │ Sau rename                           │
  ├────────────────────────────────────┼──────────────────────────────────────┤
  │ M1-M4                              │ 4 Decline mechanisms                 │
  │ M1-M4 Resonance Decline            │ 4 Resonance-Decline mechanisms       │
  │ M1 ACCELERATE M2+M3+M4            │ Compiled-Suppress ACCELERATE         │
  │                                    │ Habituation+Prediction-Completion    │
  │                                    │ +Entity-Saturation                   │
  │ M1 NHÂN M2+M3+M4                  │ Compiled-Suppress NHÂN ...           │
  │ M1 compiled suppress               │ Compiled-Suppress (bỏ M1)            │
  │ M1+M2+M3+M4 COMPOUND              │ All 4 Decline mechanisms COMPOUND    │
  │ Fix M1 / counter M1                │ Fix/counter Compiled-Suppress        │
  │ counter M2+M3 / counter M2-M4     │ counter Habituation+Completion (...) │
  │ which M1-M4 attack?                │ which Decline mechanisms attack?     │
  │ M1 + M2                            │ Compiled-Suppress + Habituation      │
  │ §4 — M1-M4                         │ §4 — 4 RESONANCE-DECLINE MECHANISMS │
  └────────────────────────────────────┴──────────────────────────────────────┘
```

---

## §2 — QUY TẮC THAY THẾ

### §2.1 — Replace passes (per SAFE file)

```
  ⭐ THỨ TỰ:

  PHASE A — GROUPED LABELS (trước standalone):
  Pass 1: "M1-M4"           → "4 Decline mechanisms" (hoặc context-specific, xem §1.3)
  Pass 2: "M1+M2+M3+M4"    → "Compiled-Suppress+Habituation+Prediction-Completion+Entity-Saturation"
  Pass 2b: "M2+M3+M4" / "M2-M4" → "Habituation+Prediction-Completion+Entity-Saturation"

  PHASE B — LABELED PATTERNS (tránh redundancy):
  Pass 3: "M1 compiled suppress"  → "Compiled-Suppress"
  Pass 4: "M1 Compiled suppress"  → "Compiled-Suppress"
  Pass 5: "M2 habituation"        → "Habituation"
  Pass 6: "M2 Habituation"        → "Habituation"
  Pass 7: "M3 prediction completion" → "Prediction-Completion"
  Pass 8: "M3 Prediction completion" → "Prediction-Completion"
  Pass 9: "M4 Entity-Compiled saturation" → "Entity-Saturation"
  Pass 9b: "M4 Entity-Saturation" / "M4 entity-compiled saturation" → "Entity-Saturation"

  PHASE C — STANDALONE (catch remaining):
  Pass 10: "M1" → "Compiled-Suppress"
  Pass 11: "M2" → "Habituation"
  Pass 12: "M3" → "Prediction-Completion"
  Pass 13: "M4" → "Entity-Saturation"

  ⚠️ PHASE C CHỈ DÙNG CHO FILES "SAFE" (pure Resonance Decline context — §3.2 nhóm RENAME).
  → Files MIXED/COLLISION (§3.4) phải MANUAL từng occurrence.
  → TUYỆT ĐỐI KHÔNG Phase C trên files SKIP (§3.3).
```

### §2.2 — ⚠️ AN TOÀN BẮT BUỘC (bài học từ audit)

```
  ① TRƯỚC mỗi file: Read full context, xác nhận file thuộc nhóm RENAME (§3.2).
  ② Phase C (standalone M1→...) chỉ chạy khi file 100% pure Resonance Decline.
  ③ Files có dạng "M1." (dấu chấm + tên khác) → nghi MIXED/SKIP, kiểm tra trước.
  ④ Sau mỗi file: grep "\bM[1-4]\b" còn sót → verify từng dòng còn lại là intentional.
  ⑤ KHÔNG replace_all "M1" toàn repo — destroy hệ ④⑤⑥.
```

---

## §3 — FILE INVENTORY (ĐÃ HIỆU CHỈNH SAU AUDIT 2026-05-29)

### §3.1 — Tổng quan 3 nhóm

```
  NHÓM A — RENAME (Resonance Decline thật):     ~46 files, ~545 occ
  NHÓM B — MIXED/COLLISION (manual):             ~4 files, ~95 occ
  NHÓM C — SKIP TUYỆT ĐỐI (false-positive + khác hệ): ~12+ files
  + backup/_backup/VI/ → SKIP toàn bộ
```

### §3.2 — NHÓM A: RENAME (pure Resonance Decline) — chạy Phase A→C

```
  ── Cluster S1: SOURCE + Agent-Mechanism (7 file, ~138 occ) ──
  │ Bond-Architecture.md                      ~42  SOURCE (§4 = định nghĩa gốc)
  │ By-Product-Gap-Resonance.md               ~43  §10 = bản tóm tắt
  │ Agent-Mechanism.md                        ~21
  │ Resonance-Sustainability.md               ~18
  │ Self-Pattern-Modeling.md                  ~8
  │ By-Product-Scale.md                       ~5
  │ Entity-Access.md                          ~1
  │ (Entity-Access-Calibration.md             ~2   verify-at-exec)

  ── Cluster S2: OBSERVATION (5 file, ~140 occ) ──
  │ Observation/Boredom.md                    ~50  HEAVY
  │ Observation/Connection.md                 ~42  HEAVY (= source thứ 2, §4.5/§5)
  │ Observation/Empathy.md                    ~28
  │ Observation/Status.md                     ~12
  │ Observation/Protect.md                    ~8

  ── Cluster S3: BODY-BASE + CORE (clean decline, ~12 file, ~61 occ) ──
  │ Body-Base/Body-Coupling.md                ~22  (✓ confirmed decline + entanglement)
  │ Core-Software.md (root)                   ~16  ⭐ MISSED BY OLD PLAN
  │ Body-Base/Inter-Body-Mechanism.md         ~5
  │ Body-Base/Chunk/Background-Pattern.md     ~4
  │ Body-Base/Chunk/Chunk.md                  ~3
  │ Body-Base/Valence-Propagation.md          ~3   ⚠️ verify (cross-ref label tới decline, KHÔNG phải firing-mode)
  │ Body-Base/.../Gap-Distribution-Profile.md ~2
  │ Body-Base/.../Gap-Body-Need.md            ~1
  │ Core-Hardware.md (root)                    ~1
  │ Neural-Processing-Flow.md                 ~1
  │ 00-Parameter-Overview.md (root)            ~1   verify-at-exec
  │ (Collective/Collective-Body.md            ~2)
  │ (Collective/Coordination-Node.md          ~2)

  ── Cluster S4: LOVE + INDEX + MISC (~7 file, ~82 occ) ──
  │ Research/Love-Unified.md                  ~35
  │ Research/Love-Romantic.md                 ~29
  │ Core-Deep-Dive/01-File-Index.md           ~9
  │ Domain/Drill-Emergent-Pattern.md          ~3
  │ Research/01-File-Index.md                 ~2
  │ Plan-Translate/00-Glossary.md             ~1   verify-at-exec
  │ Public-Plan/plan-tech-post.md             ~1
  │ (plan-1a-1b-rename.md                      ~1)

  ── Cluster S5: EDUCATION-SYSTEM (Applications) ⭐ NEW (6 file, ~29 occ) ──
  │ Applications/Education-System/Education-System.md          ~20
  │ Applications/Education-System/Hardware-Calibration.md      ~3
  │ Applications/Education-System/Curriculum-Framework.md      ~2
  │ Applications/Education-System/00_Overview.md               ~1
  │ Applications/Education-System/Country/VN/VN-Recommendations.md  ~2
  │ Applications/Education-System/Country/VN/VN-Education-Status.md ~1

  ── Cluster S6: EDUCATION-MECHANISM + CHILD-DEV (Research/Human-Learning) ⭐ NEW (9 file, ~98 occ) ──
  │ .../Education-Mechanism/Connection-Education.md            ~30  HEAVY
  │ .../Education-Mechanism/Education-Mechanism.md             ~18
  │ .../Education-Mechanism/Observation/Education-Arms-Race.md ~13
  │ .../Education-Mechanism/Domain-Knowledge-Map.md            ~9
  │ .../Education-Mechanism/Expansion-Saturation-Crisis.md     ~2
  │ .../Education-Mechanism/Observation/Money-Education.md      ~1
  │ .../Child-Development/Skill-Introduction.md                ~9
  │ .../Child-Development/Natural-Development.md                ~8
  │ .../Child-Development/Child-Development-Mechanism.md        ~8

  ── Cluster S7: MELODY-TECHNOLOGY (Research) ⭐ NEW (3 file, ~33 occ) ──
  │ Research/Melody-Technology/Religion.md                     ~17
  │ Research/Melody-Technology/Idol-Phenomenon.md              ~10
  │ Research/Melody-Technology/Melody-Technology-Overview.md   ~6
```

### §3.3 — NHÓM C: SKIP TUYỆT ĐỐI (false-positive + hệ khác)

```
  ⛔ KHÔNG ĐỘNG VÀO — nếu rename sẽ PHÁ HỎNG nội dung:

  ── False-positive (plan CŨ xếp nhầm vào rename) ──
  │ Schema/Anchor-Schema-Example.md           ~11  Hệ ⑥ Micro examples (M/S/D/L/X)
  │ Research/Quote-Analysis/ (×3 file)        ~12  Nhãn Meta-insight
  │   - Work-Journey-Destination-Cluster.md
  │   - Work-Comparison-Thief-Of-Joy.md
  │   - Work-Chunk-Dependent-Visibility-Cluster.md
  │ Neural-Architecture.md                    ~5   Motor cortex (M1 = primary motor cortex)

  ── Hệ ⑤ PFC Damage ──
  │ Drill-Body-Feedback/01-Foundation.md      ~2   "PFC M2 damage"
  │ Drill-Body-Feedback/02-Dissonance.md      ~13  M1=temp recovery, M2=neural wear
  │ Drill-Body-Feedback/03-Reward.md          ~1
  │ Drill-Body-Feedback/04-Integration.md     ~1

  ── Hệ ④ Motor Arc ──
  │ .../Child-Chunk-Development/Modality-Arcs/05-Motor-Output-Arc.md  ~5
  │ .../Child-Chunk-Development/09-Event-Chunks-Inference-Matrix.md   ~20
  │ + mọi VI/ version

  ── Backup ──
  │ Mọi file trong backup/ _backup/ VI/ → SKIP
```

### §3.4 — NHÓM B: MIXED + COLLISION (MANUAL từng occurrence)

```
  ⚠️ Session đặc biệt — đọc full file, phân biệt context từng dòng.

  │ Agent-Mechanism/Resonance-Per-Entity.md   ~58  ⚠️ MIXED:
  │   - ~28 occ Resonance Decline → RENAME (Phase A/B manual)
  │   - ~30 occ Entity Profile M1-M5 → D3: bỏ số, tên mô tả
  │     (M1.Hardware subsidy → ① Hardware subsidy, v.v.)
  │
  │ Body-Base/Body-Base.md                    ~14  ⚠️ FIRING MODES (collision):
  │   - §5.3 line 777-782 "M1-M4 firing modes" (Tonic/Phasic/Compound/Cascade)
  │     → D2: tên mô tả + fix cross-ref (đang trỏ SAI Bond-Architecture)
  │   - Dep-list labels "Bond-Architecture — M1-M4" = decline cross-ref → giữ/đổi nhãn
  │   - (plan CŨ xếp file này vào rename Cluster 3 — SAI)
  │
  │ Domain/Domain-Mapping-Drive.md            ~11  ⚠️ MIXED firing + decline:
  │   - line 944-951 firing modes (Structural/Current-Shift/Peak/Compound) → D2
  │   - line 951 cross-ref SAI "→ Xem Bond-Architecture §M1-M4" → fix
  │   - các dep-list "Bond-Architecture, M1-M4" = decline cross-ref → đổi nhãn
  │
  │ Domain/Discovery-vs-Expansion.md          ~11  ⚠️ MIXED firing + decline:
  │   - line 1036-1043 firing modes (Tonic/Phasic/Compound/Cascade) → D2
  │   - cross-ref SAI → fix
```

---

## §4 — SESSION PLAN (HIỆU CHỈNH)

```
  ┌─────┬─────────────────────────────────┬───────┬───────┬──────────────────┐
  │ Ses │ Cluster                         │ Files │ ~Occ  │ Note             │
  ├─────┼─────────────────────────────────┼───────┼───────┼──────────────────┤
  │ S1  │ Source + Agent-Mechanism        │   7   │ ~138  │ SOURCE DEFINITION│
  │ S2  │ Observation                     │   5   │ ~140  │ Boredom/Conn HEAVY│
  │ S3  │ Body-Base + Core                │  ~12  │  ~61  │ +Core-Software    │
  │ S4  │ Love + Index + Misc             │   7   │  ~82  │                  │
  │ S5  │ Education-System (Applications)  │   6   │  ~29  │ ⭐ NEW            │
  │ S6  │ Education-Mech + Child-Dev       │   9   │  ~98  │ ⭐ NEW            │
  │ S7  │ Melody-Technology               │   3   │  ~33  │ ⭐ NEW            │
  │ S8  │ MIXED + Collision Fixes         │   4   │  ~95  │ ⚠️ ALL MANUAL    │
  ├─────┼─────────────────────────────────┼───────┼───────┼──────────────────┤
  │     │ TOTAL                           │ ~53   │ ~676  │ 8 sessions       │
  └─────┴─────────────────────────────────┴───────┴───────┴──────────────────┘

  THỨ TỰ: S1 (source) trước → các consumer S2-S7 → S8 (collision) cuối.
  Lý do: định nghĩa tên chuẩn ở source xong mới propagate; collision/mixed
  cần thận trọng nhất → để cuối khi đã quen pattern.
```

---

## §5 — COLLISION FIXES (Session S8) — QUYẾT ĐỊNH ĐÃ CHỐT

### §5.1 — Entity Profile Parameters M1-M5 (Resonance-Per-Entity.md) — D3 CHỐT

```
  HIỆN TẠI (5 parameters, dạng "M1." có dấu chấm):
  → M1. Hardware subsidy level
  → M2. Compilation path
  → M3. Cost profile
  → M4. 2-tầng proportion
  → M5. 2-luồng proportion

  ✅ GIẢI PHÁP CHỐT (D3): BỎ M-PREFIX, dùng tên mô tả / số khoanh tròn:
  → "M1. Hardware subsidy" → "① Hardware subsidy" (hoặc giữ tên, bỏ "M1.")
  → "M2. Compilation path" → "② Compilation path"
  → ... M3→③, M4→④, M5→⑤
  → Sửa MỌI tham chiếu nội bộ: "which M1-M4 mechanisms attack" trong block
    này phải phân biệt: nếu nói về DECLINE → rename decline; nếu nói param → đổi số.
  ⚠️ Đọc kỹ §3 Resonance-Per-Entity: param M1-M5 và decline M1-M4 ĐAN XEN.
```

### §5.2 — PFC "Firing Modes" M1-M4 (3 file) — D2 CHỐT

```
  ⚠️ LỖI TỪ CONCEPT CASCADE REFINE (2026-05-23 v2.0) + MÂU THUẪN TAXONOMY:

  3 file define "firing modes" bằng 3 taxonomy KHÁC NHAU, tất cả cross-ref SAI
  về Bond-Architecture §M1-M4 (= Resonance DECLINE, không phải firing modes):
    Body-Base §5.3:        Tonic / Phasic / Compound / Cascade        (4)
    Discovery-vs-Expansion: Tonic / Phasic / Compound / Cascade        (4)
    Domain-Mapping-Drive:   Structural / Current-Shift / Peak / Compound (4)
  Trong khi Valence-Propagation v3.0 (§5) = canonical: 
    Maintenance / Chunk-Miss / Context-Trigger                         (3!)

  ✅ GIẢI PHÁP CHỐT (D2): TÊN MÔ TẢ + ALIGN VỀ VALENCE-PROPAGATION:
  ① Xóa cross-ref SAI: "→ Xem Bond-Architecture.md v1.0 §M1-M4"
  ② Bỏ M1-M4 labels, dùng tên mô tả trực tiếp (KHÔNG dùng M-prefix).
  ③ ⚠️ RECONCILE 3-vs-4 (cần đọc sâu khi tới S8):
     - Đọc Valence-Propagation §5-§13 (3 Firing Modes thật) + 3 file collision.
     - Quyết định: (a) merge 4-mode taxonomy về 3-mode Valence-Propagation, HOẶC
       (b) giữ taxonomy 4-mode như khái niệm riêng (intensity/timing patterns)
       nhưng đặt tên mô tả + trỏ cross-ref tới nơi định nghĩa đúng.
     - ĐÂY LÀ RECONCILIATION KHÁI NIỆM, không phải find-replace. 
       → Có thể cần hỏi user khi tới S8.
  ④ Sửa cross-ref đúng: trỏ Valence-Propagation (firing modes thật sống ở đó).
```

### §5.3 — Motor Arc + PFC Damage + Micro + Meta — SKIP

```
  ④ Motor Arc (V1/A1/M1/B1/I1): SKIP — arc labeling convention riêng.
  ⑤ PFC Damage (M1 recovery, M2 wear): SKIP — separate scope.
  ⑥ Micro examples (Anchor-Schema-Example, M/S/D/L/X): SKIP — example codes.
  + Quote-Analysis Meta-insight (M1-M4): SKIP — local enumeration.
  → Nếu muốn chuẩn hóa các hệ này → plan RIÊNG.
```

---

## §6 — AUDIT LOG (2026-05-29)

```
  PHƯƠNG PHÁP: grep "\bM[1-5]\b" toàn Human-Predictive-Drive (loại backup),
  phân loại từng cụm theo 6 hệ thống M-label.

  KẾT QUẢ vs PLAN CŨ:
  ① Plan cũ undercount: ~34 file/455 → thực tế ~50 file/580 (Resonance Decline).
     MISSED: Core-Software (16), toàn bộ Education-System/, Education-Mechanism/,
     Child-Development/, Melody-Technology/ (~19 file, ~180 occ).
  ② Plan cũ FALSE-POSITIVE (sẽ phá hỏng nếu rename mù):
     - Anchor-Schema-Example.md (hệ ⑥ Micro, KHÔNG phải decline)
     - Quote-Analysis ×3 (Meta-insight labels)
     - Neural-Architecture.md (Motor cortex) — plan flag VERIFY, xác nhận SKIP
  ③ Phát hiện hệ ⑥ (Micro examples) — plan cũ chỉ biết 5 hệ.
  ④ Collision Firing Modes LỚN hơn: 3 file (không phải 2) + Body-Base.md
     (plan cũ xếp Body-Base vào RENAME — SAI, nó là firing modes).
  ⑤ Mâu thuẫn taxonomy: firing modes có 3-4 cách đặt tên + 3-vs-4 modes
     so với Valence-Propagation canonical.

  QUYẾT ĐỊNH USER (2026-05-29): D1 full scope, D2 firing→descriptive+align,
  D3 entity-profile→bỏ số tên mô tả.
```
