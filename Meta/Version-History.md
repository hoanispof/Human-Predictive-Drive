# Lịch Sử Phiên Bản — Version History

> **Vai trò:** Theo dõi quá trình phát triển framework từ v1 → v6.0.
> Ghi nhận các insight quan trọng được thêm vào mỗi phiên bản,
> câu hỏi đã resolved, và hướng phát triển.

---

## Timeline

### v1.0 — Khái Niệm Ban Đầu

```
Thời gian: Phiên thảo luận đầu tiên
Nội dung:
  - Ý tưởng cốt lõi: con người = prediction machine
  - 3 kênh gốc: Novelty, Opioid, Oxytocin
  - Drive = Reward − Cost (sơ khai)
  - Chưa có compliance model
  - Chưa có PE sensitivity / threshold chi tiết
Files: 1 (draft duy nhất)
```

### v2.0 — Mở Rộng Cơ Chế

```
Thời gian: Phiên thảo luận thứ 2-3
Nội dung mới:
  - 5 phụ gia: Serotonin, Cortisol/GABA, NE, Vasopressin, Prolactin
  - 3 tham số nền: Capacity, Threshold, PE Sensitivity
  - Schema (4 nền + override)
  - Prediction depth per domain
  - Deepen vs Explore
  - Drive Equation chi tiết
  - Ví dụ đối chiếu đầu tiên
```

### v3.0 — Compliance Model

```
Thời gian: Phiên phát triển compliance
Nội dung mới:
  - 2 trục compliance: Internal ↔ External × High ↔ Low structure
  - 4 vùng: Soldier, Architect, Improviser, Drifter
  - Compliance per domain (KHÔNG phải kiểu người)
  - Emergence Phase
  - Ứng dụng HR, quan hệ
```

### v3.6 — Tổ Chức Hệ Thống

```
Thời gian: Tổng hợp + refine
Files: 12 files, ~10,081 dòng
Nội dung mới:
  - Core framework file (989 dòng)
  - Ví dụ đối chiếu (35+ ví dụ)
  - Phân tích macro văn minh
  - Tương thích quan hệ
  - Quản lý nhân sự + đánh giá gamedev
Hạn chế:
  - Tổ chức "lịch sử" (thêm dần), không phải "logic"
  - Core file vừa lý thuyết vừa ứng dụng → dày nhưng thiếu gọn
```

### v3.7 — Kiểm Chứng + Mở Rộng

```
Thời gian: Phiên kiểm chứng deep
Files: +6 files mới (tổng ~18 files)
Nội dung mới:
  - "Profile" → "Mode" (per domain, không phải kiểu người)
  - Tôn giáo: 5 functions + so sánh 7 tôn giáo + tương lai
  - 10 câu hỏi kinh điển nhân loại → framework dissolution
  - 7 nhân vật nổi tiếng: Einstein, Jobs, Van Gogh, Tesla, Musk, Trump, Swift
  - 10 cặp {câu hỏi × nhân vật} — 10/10 predictions đúng
  - Kiểm chứng thực tế: Iran-Israel, Musk-Trump-DOGE
Hạn chế:
  - Thiếu: profile variants, misidentification patterns, prolactin hypothesis
  - Soldier Gravity Bias chưa ghi nhận explicit
  - Giáo dục chưa có file riêng
```

### v4.0 — Tái Cấu Trúc "Human Predictive Drive" ★

```
Thời gian: 3/2026
Files: 17 files trong cấu trúc logic
Cấu trúc: Core + Deep-Dive/ + Applications/ + Validation/ + Meta/

NỘI DUNG MỚI (13 Tier 1 insights):
  1. Profile variants (Soldier-Cortisol, Architect-Dormant, etc.)
  2. 5 Misidentification patterns (+ top 3 tests)
  3. Prolactin hypothesis (healthy vs pathological)
  4. Bridge vs Trap mở rộng (3 tiêu chí)
  5. Soldier Gravity 4 forces + 3 anti-gravity
  6. Religion F6 (threshold calibration) + F7 (ritual PE schedule)
  7. ADHD vs Improviser test
  8. Education analysis (MỚI HOÀN TOÀN)
  9. Philosopher → Mode mapping
  10. Therapy → Mode mapping
  11. PEM (Prediction Environment Mismatch) — formal concept
  12. Soldier Bias trong dự đoán — explicit
  13. Compliance ratio per era — chi tiết 5 thời đại

THAY ĐỔI CẤU TRÚC:
  - Core.md: viết mới từ đầu (~700 dòng, đọc = hiểu)
  - Deep-Dive/: 5 files chuyên sâu (2 mới + 3 tách/gộp)
  - Applications/: 4 files ứng dụng (migrate + refine)
  - Validation/: 5 files kiểm chứng (migrate + thêm mapping)
  - Meta/: version history
  - Terminology nhất quán: "mode" (không "profile"), per domain
  - Cross-references chính xác giữa TẤT CẢ files

KIỂM CHỨNG THỰC TẾ (v4.0):
  - Musk-DOGE: Architect Misapplication → ✅ xác nhận (Tesla -71%, rời DOGE 5/2025)
  - Musk-Trump oscillation: predict → ✅ xung đột → hàn gắn tạm → xung đột lại
  - 7 khủng hoảng văn minh = PEM → framework mới
```

### v5.0 — Predictive-Chunk Configuration + Terminology Refine ★

```
Thời gian: 3/2026
Files: 19 files (thêm Deep-Dive/Psychometrics-Mapping.md, Deep-Dive/Mismatch-Patterns.md,
       Validation/Deep-Dive-Trump.md, Validation/Deep-Dive-Musk.md)
       Xóa: Plan.md (archive — vai trò hoàn tất)

NỘI DUNG MỚI — CORE CONCEPTUAL SHIFT:
  1. Predictive-Chunk Configuration (v5.0 core):
     3 thuộc tính per domain per person:
       Depth (xa ↔ ngắn) × Source (internal ↔ external) × Sync (rời rạc ↔ hệ thống)
     → Thay thế "mode" như cơ chế nền — mode trở thành nhãn mô tả
  2. Compliance = QUAN HỆ:
     Chunk alignment với nhóm tham chiếu, KHÔNG phải thuộc tính cá nhân
  3. 4 Patterns = NHÃN MÔ TẢ:
     Soldier/Architect/Improviser/Drifter = observable labels, not mechanisms
  4. 4 Schema nền (refinement):
     Bản thân, Thế giới, Người khác, Tương lai
     "schema nỗ lực = đền đáp" → biểu hiện phổ biến của schema tương lai
     "schema quan hệ" → domain-specific instance, không phải schema nền riêng
  5. QUY ƯỚC ĐỌC (v5.0) block:
     Thêm vào header MỌI file phụ — disclaimer chuẩn hóa thuật ngữ

THAY ĐỔI TERMINOLOGY (toàn bộ files):
  - "compliance mode" → giữ nguyên trong body text (quy ước đọc clarify)
  - "Mode = trạng thái" → "Pattern = nhãn mô tả"
  - "schema nỗ lực" → "schema tương lai" (khi đúng ngữ cảnh)
  - "4 mode" → "4 pattern" (header/footer/formal)
  - Prerequisite refs: "compliance mode" → "predictive-chunk config"
  - Footer: tất cả files v4.0 → v5.0

FILES MỚI:
  - Deep-Dive/Psychometrics-Mapping.md: 18 tests → chunk config mapping
  - Deep-Dive/Mismatch-Patterns.md: 6 patterns mismatch phổ biến
  - Validation/Deep-Dive-Trump.md: case study chuyên sâu (v1.0)
  - Validation/Deep-Dive-Musk.md: case study chuyên sâu (v1.0)

CORE.MD CHANGES (v5.0):
  - §4 Cortisol: fix bảng + trim MR/GR details
  - §5.3 PE Sensitivity: condense 3 sub-mechanisms
  - §6.1 Schema: thêm terminology note (schema nỗ lực / schema quan hệ)
  - §8.2: thêm sync disambiguation note
  - §13 File map: thêm Psychometrics-Mapping.md
  - Line 102: "Tự động" → "Automated" (language consistency)

DEEP-DIVE/ CHANGES:
  - Psychometrics-Mapping.md: full rewrite với Vietnamese diacritics
  - Tất cả Deep-Dive files đã là v5.0 từ prior session

APPLICATIONS/ CHANGES (4 files):
  - Relationships.md: header v5.0, §2.6 schema reframe, Kết Nối table
  - HR-Management.md: header v5.0, "4 mode"→"4 pattern", schema terminology
  - HR-Assessment-Gamedev.md: header v5.0, schema + AI prompt updates
  - Macro-Civilization.md: header v5.0, schema terminology

VALIDATION/ CHANGES (7 files):
  - Examples.md: header/footer v5.0, QUY ƯỚC ĐỌC, Kết Nối table
  - Classic-Questions.md: header/footer v5.0, QUY ƯỚC ĐỌC, Kết Nối table
  - Characters-Historical.md: header/footer v5.0, QUY ƯỚC ĐỌC, phương pháp
  - Characters-Modern.md: header/footer v5.0, QUY ƯỚC ĐỌC
  - Characters-Questions.md: header/footer v5.0, QUY ƯỚC ĐỌC
  - Deep-Dive-Trump.md: thêm QUY ƯỚC ĐỌC v5.0 (giữ footer v1.0)
  - Deep-Dive-Musk.md: thêm QUY ƯỚC ĐỌC v5.0 (giữ footer v1.0)
```

### v5.5 — Square Model: Source × Depth Restructure ★

```
Thời gian: 3/2026
Files: Core.md major restructure, Version-History.md update

NỘI DUNG MỚI — MÔ HÌNH VUÔNG (SQUARE MODEL):
  1. Mô Hình Vuông (v5.5 core):
     2 trục: Source Ratio (X: internal ↔ external) × Depth Composite (Y: shallow → deep)
     4 nhãn = 4 CẠNH (không phải 4 ô/góc):
       Drifter (cạnh dưới) | Architect (cạnh trên)
       Improviser (cạnh trái) | Soldier (cạnh phải)
     Mọi vị trí bên trong = 1 profile per domain trên phổ liên tục.

  2. Depth = THAM SỐ GỘP (composite):
     ① Chunk quality (prediction accuracy)
     ② Connectivity (sync giữa chunks)
     ③ Cluster formation (tổ chức thành cụm)
     ④ Cluster maturity (ổn định + convergence)
     → Sync KHÔNG còn là trục riêng — là sub-parameter (connectivity) của Depth.
     → Giải quyết: "Soldier sync" vs "Architect sync" = 2 dạng nhưng cùng trục Y.

  3. Compliance = CHỈ SỐ PHÁI SINH:
     Compliance(person, group) = chunk_overlap(person.chunks, group.chunks)
     → Hàm 2 biến, không phải thuộc tính 1 biến.
     → Demoted từ trục cơ bản (v5.0) sang chỉ số phái sinh (v5.5).

  4. Soldier Gravity → External Chunk Pressure:
     Reframe: áp lực kéo MỌI VỊ TRÍ về phía external (cạnh phải),
     không phải kéo "thành Soldier" (vì Soldier = cạnh, không phải loại).

  5. Compliance per era → Source Ratio Shift per era:
     Bảng biểu hiện reframe qua vị trí trên Mô Hình Vuông.

LÝ DO RESTRUCTURE:
  - v5.0 grid (Source × Sync) không giải quyết "Soldier-Deep" (professor 30 năm
    = external + deep). Trên grid cũ, vị trí này không có nhãn.
  - Sync thực ra TƯƠNG QUAN với depth — khi depth tăng, sync emerge tự nhiên.
    → Sync không phải trục độc lập → gộp vào depth composite.
  - Compliance là relationship, không phải axis — §8.3 v5.0 đã nói điều này,
    v5.5 chỉ THỰC HIỆN nhất quán.

CORE.MD CHANGES (v5.5):
  - Header: v5.0 → v5.5
  - §1: cập nhật "phổ liên tục" → "Mô Hình Vuông"
  - §2: TẦNG 2 thêm "Mô Hình Vuông: Source (X) × Depth (Y)"
  - §8 title: "Compliance Mode" → "Predictive-Chunk Patterns — Mô Hình Vuông"
  - §8.1: thêm compliance = chỉ số phụ thuộc bối cảnh
  - §8.2: VIẾT MỚI — Mô Hình Vuông thay 2×2 grid
  - §8.3: "quan hệ" → "chỉ số phái sinh" + công thức chunk_overlap
  - §8.4-8.8: cập nhật terminology (sync → depth, phổ 2D → Mô Hình Vuông)
  - §8.9: "Chunk Topology" → "Chi Tiết Depth Composite" (3 trục → 4 sub-parameters)
  - §9 title: "Soldier Gravity" → "External Chunk Pressure (Soldier Gravity)"
  - §9.1-9.5: reframe toàn bộ Soldier Gravity → External Chunk Pressure
  - §10 title: "Tỉ Lệ Compliance" → "Source Ratio Shift Per Thời Đại"
  - §12.4, §14: cập nhật terminology
  - §13: cập nhật file map description

FILE RENAME (v5.5):
  - Deep-Dive/Compliance-Model.md → Chunk-Patterns.md (file "phần mềm")
  - Deep-Dive/Compliance-Society.md → Society-Dynamics.md (External Pressure × xã hội)
  - Headers, QUY ƯỚC ĐỌC, section titles, Kết Nối tables cập nhật trong cả 2 file
  - Cross-references cập nhật trong TẤT CẢ 21 files

⚠️ CHƯA CẬP NHẬT ĐẦY ĐỦ (để phase sau):
  - Deep-Dive/ files: terminology consistency bên trong body text
  - Applications/ files: terminology consistency
  - Validation/ files: terminology consistency
```

### v6.0 — Novelty Reframe + PE Sensitivity ④ Generalization Scope ★

```
Thời gian: 3/2026
Files: ~25 files (thêm PE-Sensitivity.md, Depression-Predictive-Model.md,
       Social-Pressure-Tradeoff.md, Education/, Curriculum/)
       Validation/Characters-*.md → gộp thành Characters.md

NỘI DUNG MỚI — PE SENSITIVITY DEEP DIVE:
  1. PE Sensitivity ④ — Generalization Scope (v6.0 core):
     Sub-parameter thứ 4: phạm vi PE lan tỏa (hẹp ↔ rộng).
     ④ hẹp → deep expression (chuyên gia). ④ rộng → broad expression (đa lĩnh vực).
     Structural vs Creative = NHÃN downstream, KHÔNG PHẢI sub-type.
     → Giải quyết: "cùng Novelty cao + Threshold cao mà biểu hiện khác nhau"

  2. Novelty Reframe:
     Novelty ≠ "ý tưởng mới". Novelty = PE từ chunk MỚI (bất kỳ chunk chưa predicted).
     Bao gồm cả explore (domain mới) lẫn deepen (kết nối mới trong domain cũ).

  3. Encoding Modality — Mixing Board Model:
     4 kênh encoding: somatic, motor, spatial, verbal.
     Chạy SONG SONG (mixing board), không phải sub-type.
     Kênh cao nhất = dominant, nhưng kênh thấp vẫn chạy.
     → Giải quyết: "encoding modality: 1 chiều hay multi-dimensional?"

FILES MỚI:
  - Core-Deep-Dive/PE-Sensitivity.md: ★ PE Sensitivity deep-dive (4 sub + encoding modality)
  - Research/Depression-Predictive-Model.md: Trầm cảm = learned prediction suppression
    (4 cơ chế can thiệp A/B/C/D, 19 phương pháp mapping, 5 case studies, 13 predictions)
  - Research/Social-Pressure-Tradeoff.md: Trade-off áp lực xã hội (system-level)
  - Applications/Education.md: Giáo dục qua framework lens (moved from Research/)
  - Applications/Education/: Curriculum chi tiết + 00_Overview.md

FILE CHANGES:
  - Validation/Characters-Historical.md + Characters-Modern.md + Characters-Questions.md
    → gộp thành Characters.md
  - Core.md: header v6.0, §5.3 PE Sensitivity thêm ④, §14 resolved questions cập nhật

CORE.MD CHANGES (v6.0):
  - Header: v5.5 → v6.0 (Novelty Reframe + PE Sensitivity ④ Generalization Scope)
  - §5.3: PE Sensitivity thêm sub ④ generalization scope
  - §13: File map cập nhật (PE-Sensitivity.md, Depression, Social-Pressure, Education/)
  - §14.1: Thêm câu hỏi mở #13, #14 (generalization scope verification)
  - §14.2: 3 câu hỏi resolved mới (novelty, ④, encoding modality)
```

---

## Câu Hỏi Đã Resolved

| # | Câu hỏi | Phiên bản resolved | Đáp án |
|---|---------|-------------------|--------|
| 1 | Compliance là 1 trục hay 2 trục? | v3.0 | 2 trục: Internal↔External × High↔Low structure |
| 2 | Compliance là kiểu người hay per domain? | v3.6 → v3.7 | Per domain (mode, không phải type) |
| 3 | Prolactin vai trò gì? | v4.0 | Cùng kênh gốc: bình thường = healthy, thấp = pathological |
| 4 | Bridge vs Trap phân biệt thế nào? | v4.0 | 3 tiêu chí: channel match, reward dosage, "why" |
| 5 | Soldier Gravity có bao nhiêu lực? | v4.0 | 4 forces + 3 anti-gravity |
| 6 | Tôn giáo có bao nhiêu function? | v3.7 → v4.0 | 7 functions (thêm F6 threshold calibration, F7 ritual PE) |
| 7 | Framework có bias? | v4.0 | CÓ — Soldier Bias explicit (majority → predictions lean Soldier) |
| 8 | "Khủng hoảng hiện đại" có gốc chung? | v4.0 | PEM: Prediction Environment Mismatch |
| 9 | Compliance là thuộc tính cá nhân? | v5.0 | KHÔNG — là QUAN HỆ giữa chunk config với nhóm tham chiếu |
| 10 | 4 mode là cơ chế hay nhãn? | v5.0 | NHÃN MÔ TẢ — cơ chế thật = Predictive-Chunk Config (Depth × Source × Sync) |
| 11 | "Schema nỗ lực" là schema nền riêng? | v5.0 | KHÔNG — biểu hiện phổ biến của schema tương lai |
| 12 | Sync là trục độc lập? | v5.5 | KHÔNG — Sync = hệ quả của depth. Gộp vào Depth composite (sub-parameter: connectivity) |
| 13 | 4 nhãn = 4 ô / 4 góc? | v5.5 | KHÔNG — 4 nhãn = 4 CẠNH trên Mô Hình Vuông (phổ liên tục bên trong) |
| 14 | Compliance là trục cơ bản? | v5.5 | KHÔNG — Chỉ số PHÁI SINH = chunk_overlap(person, group). Hàm 2 biến |
| 15 | "Soldier-Deep" (external + deep) có vị trí hợp lệ? | v5.5 | CÓ — vị trí phải-trên trên Mô Hình Vuông. Grid cũ không biểu diễn được |
| 16 | Novelty = ý tưởng mới? | v5.5→v6.0 | KHÔNG — Novelty = PE từ chunk MỚI (bất kỳ). Bao gồm explore + deepen |
| 17 | Cùng Novelty + Threshold cao mà biểu hiện khác? | v6.0 | PE Sensitivity ④ generalization scope: hẹp → deep, rộng → broad. Structural vs Creative = nhãn downstream |
| 18 | Encoding modality: 1 chiều hay multi-dimensional? | v6.0 | Multi-dimensional. 4 kênh (somatic, motor, spatial, verbal) chạy SONG SONG (mixing board) |

---

## Câu Hỏi Mở (Top Priority)

| # | Câu hỏi | Status |
|---|---------|--------|
| 1 | PEM đo được không? Metric nào? | Open |
| 2 | Threshold tập thể: quốc gia nào cao/thấp nhất? | Open |
| 3 | Buddhism convergence: overlap + diverge chi tiết? | Open |
| 4 | Therapy × mode: RCT evidence? | Open |
| 5 | Compliance mode phân bố per quốc gia/văn hóa? | Open |
| 6 | Framework apply cho AI consciousness? | Open |
| 7 | ④ Generalization scope: encoding modality → ④ confirm? Mixing board cần verify thực nghiệm | Open |
| 8 | ④ generalization: tách biệt với ③ habituation rate chắc chắn? Cần counterexample | Open |

---

## Cấu Trúc Files v5.0

```
Human Predictive Drive/
│
├── Core.md                          ★ FILE CHÍNH (~1165 dòng)
│
├── Deep-Dive/
│   ├── Neurochemistry.md            ← Hóa chất thần kinh chi tiết
│   ├── Chunk-Patterns.md          ← 4 pattern + variants + diagnostics
│   ├── Society-Dynamics.md        ← Soldier gravity + per era + fairness
│   ├── Education.md                 ← Giáo dục qua framework lens
│   ├── Religion.md                  ← 7 functions + so sánh + tương lai
│   ├── Mismatch-Patterns.md         ← 6 patterns mismatch phổ biến
│   └── Psychometrics-Mapping.md     ← 18 tests → chunk config mapping
│
├── Applications/
│   ├── Relationships.md             ← Tương thích quan hệ
│   ├── HR-Management.md             ← Quản lý nhân sự (6 tệp)
│   ├── HR-Assessment-Gamedev.md     ← Đánh giá nhân sự gamedev
│   └── Macro-Civilization.md        ← 7 khủng hoảng + PEM
│
├── Validation/
│   ├── Examples.md                  ← 35+ ví dụ đối chiếu
│   ├── Classic-Questions.md         ← 15 câu hỏi kinh điển + mapping
│   ├── Characters-Historical.md     ← Einstein, Jobs, Van Gogh, Tesla
│   ├── Characters-Modern.md         ← Musk, Trump, Swift + verify
│   ├── Characters-Questions.md      ← 10 cặp {câu hỏi × nhân vật}
│   ├── Deep-Dive-Trump.md           ← Case study chuyên sâu Trump
│   └── Deep-Dive-Musk.md            ← Case study chuyên sâu Musk
│
└── Meta/
    └── Version-History.md           ← File này
```

---

## Cấu Trúc Files v5.5 (Restructure)

```
THAY ĐỔI TỪ v5.0 → v5.5:
  Deep-Dive/ → TÁCH thành 2 folders:
    Core-Deep-Dive/  = đào sâu từng tầng Core.md (hardware, software, xã hội)
    Research/         = nghiên cứu chuyên sâu per topic qua framework lens

  Applications/Macro-Civilization.md → Research/Macro-Civilization.md
    (tính chất research > application)

  Deep-Dive/Mismatch-Patterns.md → Research/Mismatch-Patterns.md
    (áp dụng nhiều tầng core để phân tích hiện tượng, không đào sâu 1 tầng)

Human Predictive Drive/
│
├── Core.md                          ★ FILE CHÍNH (v5.5)
│
├── Core-Deep-Dive/                  ← Đào sâu từng tầng Core.md
│   ├── Neurochemistry.md            ← Tầng 0 (hardware)
│   ├── Chunk-Patterns.md            ← Tầng 1A+2 (software)
│   ├── Society-Dynamics.md          ← External Pressure × xã hội
│   └── Compliance.md                ← Cross-layer: compliance v5.5 (4 pathways, diagnostic, dynamics)
│
├── Research/                        ← Nghiên cứu chuyên sâu per topic
│   ├── Education.md                 ← Giáo dục qua framework lens
│   ├── Religion.md                  ← 7 functions + so sánh + tương lai
│   ├── Psychometrics-Mapping.md     ← 18 tests → chunk config mapping
│   ├── Mismatch-Patterns.md         ← 6 patterns mismatch phổ biến
│   └── Macro-Civilization.md        ← 7 khủng hoảng + PEM
│
├── Applications/                    ← Ứng dụng thực tế (protocol cụ thể)
│   ├── Relationships.md
│   ├── HR-Management.md
│   ├── HR-Assessment-Gamedev.md
│   └── Reward-Economics.md
│
├── Validation/                      ← Kiểm chứng framework
│   ├── Examples.md
│   ├── Classic-Questions.md
│   ├── Characters-Historical.md
│   ├── Characters-Modern.md
│   ├── Characters-Questions.md
│   ├── Deep-Dive-Trump.md
│   └── Deep-Dive-Musk.md
│
└── Meta/
    └── Version-History.md
```

---

## Cấu Trúc Files v6.0

```
THAY ĐỔI TỪ v5.5 → v6.0:
  Core-Deep-Dive/ + PE-Sensitivity.md (MỚI — PE Sensitivity deep-dive)
  Research/ + Depression-Predictive-Model.md (MỚI — trầm cảm qua framework)
  Research/ + Social-Pressure-Tradeoff.md (MỚI — áp lực xã hội system-level)
  Research/Education.md → Applications/Education.md (tính chất application > research)
  Applications/Education/ (MỚI — curriculum chi tiết)
  Validation/ gộp 3 Characters files → Characters.md

Human Predictive Drive/
│
├── Core.md                         ★ FILE CHÍNH (v6.0)
│
├── Core-Deep-Dive/                 ← Đào sâu từng tầng Core.md
│   ├── Neurochemistry.md           ← Tầng 0 (hardware)
│   ├── PE-Sensitivity.md           ← ★ PE Sensitivity deep-dive: 4 sub + encoding modality (v6.0)
│   ├── Chunk-Patterns.md           ← Tầng 1A+2 (software)
│   ├── Society-Dynamics.md         ← External Pressure × xã hội
│   └── Compliance.md               ← Cross-layer: compliance v5.5 (4 pathways, diagnostic, dynamics)
│
├── Research/                       ← Nghiên cứu chuyên sâu per topic
│   ├── Religion.md                 ← 7 functions + so sánh + tương lai
│   ├── Psychometrics-Mapping.md    ← 18 tests → chunk config mapping
│   ├── Mismatch-Patterns.md        ← 6 patterns mismatch phổ biến
│   ├── Depression-Predictive-Model.md ← ★ Trầm cảm = learned prediction suppression (v0.3)
│   ├── Social-Pressure-Tradeoff.md ← ★ Trade-off áp lực xã hội
│   └── Macro-Civilization.md       ← 7 khủng hoảng + PEM
│
├── Applications/                   ← Ứng dụng thực tế (protocol cụ thể)
│   ├── Relationships.md
│   ├── HR-Management.md
│   ├── HR-Assessment-Gamedev.md
│   ├── Reward-Economics.md
│   ├── Education.md                ← Giáo dục qua framework lens
│   └── Education/                  ← Curriculum chi tiết
│       ├── 00_Overview.md
│       └── Curriculum/             ← Thiết kế chương trình
│
├── Validation/                     ← Kiểm chứng framework
│   ├── Examples.md
│   ├── Classic-Questions.md
│   ├── Characters.md               ← Gộp từ Historical + Modern + Questions
│   ├── Deep-Dive-Trump.md
│   └── Deep-Dive-Musk.md
│
└── Meta/
    └── Version-History.md
```

---

> *Version History — v6.0*
> *Lịch sử v1 → v6.0: từ khái niệm → hệ thống ~25 files.*
> *v6.0: Novelty Reframe, PE Sensitivity ④ Generalization Scope, Encoding Modality mixing board.*
> *18 câu hỏi resolved. 8 câu hỏi mở.*
