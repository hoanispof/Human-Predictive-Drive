# Plan Refine: Tạo Lại Files Mở Rộng Theo Chuẩn v5.5

> **Mục tiêu:** Tạo lại TOÀN BỘ files trong Research/, Applications/, Validation/
> theo chuẩn v5.5 (Square Model — Source × Depth Restructure).
> **Phương pháp:** Đọc file cũ → lọc insight giữ lại → phân tích qua lăng kính v5.5 →
> nếu có insight mới tốt hơn thì dùng mới → tạo file mới hoàn toàn.
> KHÔNG phải refactor từ file cũ. Chấp nhận tái cấu trúc đáng kể nếu cần.
> **Bản cũ:** Giữ trong *-v5.0/ làm reference. Không xóa.

---

## Thay Đổi Cốt Lõi v5.0 → v5.5 (Áp Dụng Cho MỌI File)

```
1. MÔ HÌNH VUÔNG (Square Model):
   v5.0: 2×2 grid (Source × Sync) → 4 ô = 4 nhãn
   v5.5: Square (Source × Depth) → 4 cạnh = 4 nhãn, phổ liên tục bên trong
   → MỌI phân tích per-pattern cần rewrite theo vị trí trên phổ, không phải ô cố định.

2. SYNC = EMERGE TỪ DEPTH:
   v5.0: Sync = trục riêng (trục Y)
   v5.5: Sync = hệ quả của Depth đủ cao (sub-parameter connectivity)
   → Mọi chỗ nói "sync cao/thấp" cần reframe thành "depth cao → sync emerge"

3. DEPTH = COMPOSITE (4 sub-parameters):
   ① Chunk quality  ② Connectivity (sync)  ③ Cluster formation  ④ Cluster maturity
   → Phân tích sâu cần tách sub-parameters, phân tích nhanh dùng Depth gộp.

4. COMPLIANCE = CHỈ SỐ PHÁI SINH:
   v5.0: Compliance = trục/thuộc tính (Internal/External)
   v5.5: Compliance = chunk_overlap(person.chunks, group.chunks) — hàm 2 biến
   → Cùng người, khác reference group → khác compliance score

5. SOLDIER GRAVITY → EXTERNAL CHUNK PRESSURE:
   v5.0: "Soldier Gravity" — tên gợi ý kéo "thành Soldier"
   v5.5: "External Chunk Pressure" — kéo MỌI vị trí về phía external source

6. NHÃN = MÔ TẢ, KHÔNG PHẢI CƠ CHẾ:
   v5.0: 4 pattern đôi khi dùng như category
   v5.5: 4 nhãn = 4 cạnh extreme, bên trong = phổ liên tục per domain

7. CONCEPTS MỚI v5.5:
   - Chunk Topology (§8.9): convergence, abstraction level, cross-domain sync
   - Dopamine inverted-U (§6.6): depth vs breadth — song song cortisol inverted-U
   - Habituation Blindness (§6.7): PE=0 ≠ Value=0
   - Compliance.md (Core-Deep-Dive): 4 pathways, diagnostic, dynamics
```

---

## Quy Ước Chung Cho Mọi File Mới

```
- Header: "Framework v5.5" + prerequisite sections trong Core.md
- Quy ước đọc v5.5 (compliance = phái sinh, 4 nhãn = mô tả, cơ chế = chunk config)
- Confidence markers: 🟢 Nghiên cứu | 🟡 Suy luận | 🔴 Giả thuyết
- Cross-references: dùng section numbers v5.5 (Core.md §8 = Mô Hình Vuông, §9 = ECP)
- Per domain analysis: luôn specify "person × domain", không gán nhãn cho toàn bộ person
- Kết nối cuối file: bảng cross-reference đến các file liên quan
```

---

## PHASE 1: RESEARCH/ (5 files — gần Core nhất)

### R1. Mismatch-Patterns.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 516 |
| **Khối lượng** | NHẸ — chủ yếu neurochemistry, ít dùng thuật ngữ pattern |
| **Insight giữ lại** | 6 pattern hoàn chỉnh (Stress Addiction, Self-Harm, Trauma Bonding, Love Addiction 3 types, Emotional Eating, Outrage Loop). Template 6-chiều phân tích. Triple mechanism Self-Harm. |
| **Cần thay đổi v5.5** | Header/disclaimer. Cross-refs (Core.md §numbers). Thêm Mô Hình Vuông lens cho "ai dễ mắc nhất" per pattern. |
| **Insight mới tiềm năng** | 5 pattern pending (People-Pleasing, Imposter Syndrome, Doom Scrolling, Revenge, Hoarding) — phân tích mới qua v5.5. Habituation Blindness (§6.7) có thể là pattern mới. Dopamine inverted-U lens cho addiction patterns. |
| **Tái cấu trúc?** | Nhẹ. Giữ template 6-chiều, thêm cột "vị trí trên Mô Hình Vuông" |
| **Ưu tiên** | 1 (nhẹ nhất, hoàn thành patterns pending) |

### R2. Education.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 527 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | 4 lý do Soldier-optimized. Architect-Dormant qua giáo dục. ADHD vs Improviser distinction. Teacher Projection. Framework Distribution bottleneck. Per-pattern pathway design. |
| **Cần thay đổi v5.5** | "Soldier Gravity" → "External Chunk Pressure". Per-pattern → per-vị-trí trên Mô Hình Vuông. Compliance = phái sinh reframe. Depth composite lens cho "prediction depth per domain" trong giáo dục. |
| **Insight mới tiềm năng** | Chunk Topology (§8.9) cho cross-domain learning. Dopamine inverted-U cho ADHD reframe. Soldier-Deep (professor) vs Soldier-Shallow distinction. Convergence concept cho "first principles education". |
| **Tái cấu trúc?** | Trung bình. Cấu trúc cũ ổn, nhưng per-pattern sections cần rewrite thành phổ liên tục |
| **Ưu tiên** | 2 |

### R3. Religion.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 781 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | 7 Functions framework (F1-F7). Per-pattern × tôn giáo analysis. Marx reframe. Secularization = PE deficit + opioid crisis correlation. Faith = structural requirement. Identity Fusion. |
| **Cần thay đổi v5.5** | "Soldier Gravity" → ECP (§5 "Tôn giáo như Soldier Gravity"). Per-pattern → vị trí trên Mô Hình Vuông. Compliance reframe. |
| **Insight mới tiềm năng** | Tôn giáo install CONTENT vào 4 schema CẤU TRÚC (Core.md §6.1 đã note). Chunk Topology: tôn giáo = shared foundation chunks (convergence CAO) → cross-domain sync. Habituation Blindness: ritual chống habituation = F7 qua PE lens mới. |
| **Tái cấu trúc?** | Trung bình. 7 Functions giữ, per-pattern rewrite, thêm Chunk Topology lens |
| **Ưu tiên** | 3 |

### R4. Macro-Civilization.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 766 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | PEM (Prediction Environment Mismatch) unifying 7 crises. Cortisol-dopamine coupling. Historical lessons (Rome, USSR, China). 4 kịch bản tương lai. 8 nguyên tắc giải pháp. |
| **Cần thay đổi v5.5** | Depth composite cho phân tích macro (collective chunk depth giảm). ECP thay Soldier Gravity. Mô Hình Vuông cho population shift per era. Compliance = phái sinh ở cấp xã hội. |
| **Insight mới tiềm năng** | Convergence (§8.9) cho "tại sao specialist society mất cross-domain sync". Dopamine inverted-U ở cấp xã hội (quá nhiều explore = Improviser society?). AI Era qua Chunk Topology lens. |
| **Tái cấu trúc?** | Trung bình. 7 crises structure giữ, PEM giữ, reframe qua v5.5 |
| **Ưu tiên** | 4 |

### R5. Psychometrics-Mapping.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 941 |
| **Khối lượng** | NẶNG — Sync trục riêng → emerge từ Depth thay đổi toàn bộ mapping logic |
| **Insight giữ lại** | 18 test mapping. Coverage matrix. 5 GAPs. Optimal battery. Profile template. |
| **Cần thay đổi v5.5** | TOÀN BỘ mapping logic: Sync không còn là dimension đo riêng → merge vào Depth composite. Coverage matrix cần redraw. GAPs cần re-evaluate (GAP "sync measurement" → "depth sub-parameter measurement"). Profile template cần redesign theo Mô Hình Vuông. |
| **Insight mới tiềm năng** | Depth composite 4 sub-parameters → 4 measurement dimensions mới. Compliance = phái sinh → compliance measurement = cần biết reference group. Chunk Topology → test convergence (cross-domain transfer ability). |
| **Tái cấu trúc?** | ĐÁNG KỂ. Mapping logic thay đổi fundamental |
| **Ưu tiên** | 5 (nặng nhất, cần Research khác xong trước) |

---

## PHASE 2: APPLICATIONS/ (4 files — protocol thực tế)

### A1. Relationships.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 1114 |
| **Khối lượng** | NẶNG — file dài nhất, nhiều per-pattern analysis |
| **Insight giữ lại** | 6 yếu tố tương thích. Weighting matrix per loại quan hệ. 10 cặp compliance mode. Attraction vs Sustainability. Habituation Blindness (đã update v5.5). Conflict cortisol cascade. Red/green flags. Repair framework. |
| **Cần thay đổi v5.5** | Per-pattern → phổ liên tục (vị trí trên Mô Hình Vuông). Compliance = phái sinh (tương thích = chunk overlap, không phải "mode match"). 10 cặp compliance → reframe thành vùng trên Mô Hình Vuông tương tác. |
| **Insight mới tiềm năng** | Depth composite cho "domain chung sâu" (chunk quality + connectivity + cluster). Convergence cho "tại sao polymath khó tìm partner hiểu mình". Habituation Blindness đã có — expand. |
| **Tái cấu trúc?** | ĐÁNG KỂ — 10 cặp compliance cần rethink thành phổ |
| **Ưu tiên** | 2 (quan trọng, nhiều người đọc) |

### A2. HR-Management.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 719 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | 6-Tệp model. Ma trận nhu cầu/task. Retention per tệp. Team composition. Manager projection bias. 7 sai lầm phổ biến. Mode Card. |
| **Cần thay đổi v5.5** | 6-Tệp → reframe qua Mô Hình Vuông (vị trí per domain công việc). "Soldier Gravity" → ECP trong tổ chức. Compliance = phái sinh (cùng người, khác team/role → khác "tệp"). |
| **Insight mới tiềm năng** | Depth composite cho đánh giá "senior vs junior" (chunk quality + cluster maturity). Convergence cho "cross-functional team". Dopamine inverted-U cho "tại sao senior burned out" (quá sâu 1 domain). |
| **Tái cấu trúc?** | Trung bình. 6-Tệp có thể giữ như practical shortcut + thêm Mô Hình Vuông lens |
| **Ưu tiên** | 3 |

### A3. HR-Assessment-Gamedev.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 697 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | 3-Tệp assessment (A: Mode, B: Domain, C: Skill). Hidden data reading. Role-specific archetypes (Programmer/Designer/Artist/Producer/Sound). Somatic-primary hiring. Ongoing assessment via observation. |
| **Cần thay đổi v5.5** | Assessment questions → đo vị trí trên Mô Hình Vuông per domain. Somatic:Verbal axis cần integrate hoặc note là domain-specific observation. Mode Card → Chunk Config Card. |
| **Insight mới tiềm năng** | Depth composite cho "senior assessment" (cluster maturity). Convergence cho "cross-role potential" (game designer → producer transition). |
| **Tái cấu trúc?** | Trung bình. Câu hỏi assessment có thể giữ phần lớn, reframe output |
| **Ưu tiên** | 4 (niche, phụ thuộc HR-Management) |

### A4. Reward-Economics.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 589 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | 3-Tier reward spectrum. 6 paths "rich still chasing". Money = prediction chunk. Cortisol Path vs Dopamine Path. Distribution chain (Creator → Intermediary → User). Reward Bootstrapping + Goldilocks + fading. "Nợ Thưởng" concept. |
| **Cần thay đổi v5.5** | Cortisol/Dopamine paths → link rõ với inverted-U (§6.4, §6.6). Bootstrapping → link với Depth composite (external reward → chunk formation → depth tăng). |
| **Insight mới tiềm năng** | Habituation Blindness cho economics (habituate → không thấy giá trị → mất → tiếc). Convergence cho "tại sao platform economy thắng" (shared foundation chunks). Dopamine inverted-U cho addiction economics. |
| **Tái cấu trúc?** | Nhẹ-Trung bình. Cấu trúc cũ ổn, thêm v5.5 lens |
| **Ưu tiên** | 5 |

---

## PHASE 3: VALIDATION/ (7 files — kiểm chứng)

### V1. Examples.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 761 |
| **Khối lượng** | TRUNG BÌNH-NẶNG — 35+ examples cần rewrite qua v5.5 lens |
| **Insight giữ lại** | 35 ví dụ across 9 categories (A-I). Drive equation applied consistently. Domain-specific chunk config. Schema determines interpretation. |
| **Cần thay đổi v5.5** | Mỗi ví dụ: thêm vị trí trên Mô Hình Vuông. Compliance reframe. "Sync" → "Depth + connectivity emerge". Có thể thêm ví dụ mới cho concepts v5.5 (Chunk Topology, Habituation Blindness, Dopamine inverted-U). |
| **Tái cấu trúc?** | Trung bình. Giữ categories, rewrite per example |
| **Ưu tiên** | 2 (cần sớm — examples = cách dễ nhất verify v5.5 consistency) |

### V2. Classic-Questions.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 662 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | 15 classical questions dissolved. Projection meta-insight. False dichotomy pattern. Buddhism convergence. Philosopher → mode mapping. Therapy → mode mapping. |
| **Cần thay đổi v5.5** | "Mode" → vị trí trên Mô Hình Vuông. Philosopher mapping → vị trí trên phổ. Compliance reframe. Thêm Depth composite lens cho "meaning" questions. |
| **Tái cấu trúc?** | Nhẹ-Trung bình. 15 questions giữ, reframe answers qua v5.5 |
| **Ưu tiên** | 3 |

### V3. Characters-Historical.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | ~1096 |
| **Khối lượng** | TRUNG BÌNH |
| **Insight giữ lại** | 4 figures (Einstein, Jobs, Van Gogh, Tesla). Domain-specific chunk config analysis. Contradiction → domain-specific explanation. 5-step validation methodology. |
| **Cần thay đổi v5.5** | Mỗi figure: vị trí trên Mô Hình Vuông per domain. Chunk Topology analysis (convergence). "Soldier Gravity creator" (Jobs) → ECP creator. |
| **Tái cấu trúc?** | Trung bình. Methodology giữ, per-figure rewrite |
| **Ưu tiên** | 4 |

### V4. Characters-Modern.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | ~1380 |
| **Khối lượng** | NẶNG — file dài, 3 living figures |
| **Insight giữ lại** | Musk (multi-domain architect + species survival schema), Trump (unfalsifiable schema + serotonin hierarchy), Swift (strategic architect hidden). Cross-comparison. Real-time prediction testing. |
| **Cần thay đổi v5.5** | Mô Hình Vuông per domain per figure. Chunk Topology (Musk convergence, Trump cluster isolation, Swift cluster growth). Compliance = phái sinh. Unfalsifiable Schema → formalize. |
| **Tái cấu trúc?** | Trung bình. Per-figure rewrite, add v5.5 analysis layers |
| **Ưu tiên** | 5 |

### V5. Characters-Questions.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | 335 |
| **Khối lượng** | NHẸ |
| **Insight giữ lại** | 10 question×figure pairings. 10/10 prediction accuracy. PE conversion mechanism. Same outcome different mechanism pattern. |
| **Cần thay đổi v5.5** | Reframe predictions qua Mô Hình Vuông. Nhẹ — phần lớn logic giữ nguyên. |
| **Tái cấu trúc?** | Nhẹ |
| **Ưu tiên** | 6 (phụ thuộc V3+V4) |

### V6. Deep-Dive-Musk.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | ~1465 |
| **Khối lượng** | NẶNG — case study chuyên sâu nhất |
| **Insight giữ lại** | Developmental analysis. Hardware/Software mapping. Domain-by-domain. Event timeline predictions. Convergence concept (shared foundation across SpaceX/Tesla/Boring). |
| **Cần thay đổi v5.5** | Chunk Topology = PERFECT fit cho Musk (convergence CAO = cross-domain architect). Mô Hình Vuông per domain. Depth composite analysis. |
| **Tái cấu trúc?** | Trung bình-Nặng. Thêm Chunk Topology layer (concept đã có trong v5.0 nhưng chưa formalize) |
| **Ưu tiên** | 7 |

### V7. Deep-Dive-Trump.md

| Mục | Chi tiết |
|-----|----------|
| **Dòng cũ** | ~1104 |
| **Khối lượng** | TRUNG BÌNH-NẶNG |
| **Insight giữ lại** | Unfalsifiable schema analysis. Serotonin hierarchy. Supporter psychology. Schema robustness. Event timeline. |
| **Cần thay đổi v5.5** | Mô Hình Vuông per domain. Compliance = phái sinh (Trump × different reference groups). Depth composite (Trump: deep in deal-making, shallow in policy). |
| **Tái cấu trúc?** | Trung bình |
| **Ưu tiên** | 8 |

---

## Thứ Tự Triển Khai Tổng Thể

```
PHASE 1 — RESEARCH (gần Core nhất, nền tảng cho Applications + Validation)
  R1. Mismatch-Patterns.md        ← NHẸ, ít phụ thuộc
  R2. Education.md                ← TB, nền cho nhiều file
  R3. Religion.md                 ← TB, tương đối độc lập
  R4. Macro-Civilization.md       ← TB, reference nhiều file
  R5. Psychometrics-Mapping.md    ← NẶNG, cần R1-R4 xong

PHASE 2 — APPLICATIONS (protocol thực tế, cần Research làm nền)
  A1. Relationships.md            ← NẶNG, nhiều người đọc
  A2. HR-Management.md            ← TB
  A3. HR-Assessment-Gamedev.md    ← TB, niche
  A4. Reward-Economics.md         ← TB

PHASE 3 — VALIDATION (kiểm chứng, cần Research + Applications làm nền)
  V1. Examples.md                 ← TB-NẶNG, verify v5.5 consistency
  V2. Classic-Questions.md        ← TB
  V3. Characters-Historical.md    ← TB
  V4. Characters-Modern.md        ← NẶNG
  V5. Characters-Questions.md     ← NHẸ, phụ thuộc V3+V4
  V6. Deep-Dive-Musk.md           ← NẶNG
  V7. Deep-Dive-Trump.md          ← TB-NẶNG
```

---

## Quy Trình Per File

```
Bước 1: ĐỌC FILE CŨ
  → Đọc kỹ toàn bộ file v5.0
  → Liệt kê insights đáng giữ (concepts, data, examples)
  → Liệt kê những gì outdated hoặc sai theo v5.5

Bước 2: PHÂN TÍCH QUA LĂNG KÍNH v5.5
  → Đọc lại Core.md + Core-Deep-Dive relevant sections
  → Với mỗi insight cũ: v5.5 giải thích TỐT HƠN hay GIỐNG?
  → Tìm insight MỚI mà v5.5 cho phép (Chunk Topology, Dopamine inverted-U,
    Habituation Blindness, Compliance phái sinh, Mô Hình Vuông)

Bước 3: THIẾT KẾ CẤU TRÚC MỚI
  → Outline sections cho file mới
  → Quyết định: giữ cấu trúc cũ (nếu tốt) hay tái cấu trúc (nếu cần)
  → Verify cross-references với Core.md v5.5 section numbers

Bước 4: VIẾT FILE MỚI
  → Viết từ đầu theo outline
  → Dùng insight cũ (đã filter) + insight mới (từ v5.5)
  → Confidence markers (🟢🟡🔴)
  → Cross-references chính xác

Bước 5: REVIEW
  → Check consistency với Core.md v5.5
  → Check cross-references với các file đã tạo
  → Check không còn thuật ngữ v5.0 (Soldier Gravity, Sync trục riêng, compliance trait)
```

---

## Tracking

| File | Bước 1 | Bước 2 | Bước 3 | Bước 4 | Bước 5 | Status |
|------|--------|--------|--------|--------|--------|--------|
| R1. Mismatch-Patterns | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| R2. Education | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| R3. Religion | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| R4. Macro-Civilization | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| R5. Psychometrics-Mapping | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| A1. Relationships | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| A2. HR-Management | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| A3. HR-Assessment-Gamedev | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| A4. Reward-Economics | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| V1. Examples | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| V2. Classic-Questions | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| V3. Characters (merged V3+V4+V5) | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| V4. Deep-Dive-Musk | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |
| V5. Deep-Dive-Trump | ☑ | ☑ | ☑ | ☑ | ☑ | ✅ Hoàn thành |

---

> *Plan Refine v1.0 — 16 files across 3 phases*
> *Phương pháp: Đọc → Lọc → Phân tích v5.5 → Tạo mới*
> *Chậm mà chắc.*
