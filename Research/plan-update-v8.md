# Plan Update v8.0 — Schema-Drive

> **Mục đích:** Checklist cho khi build v8.0 từ v7 draft
> **Khi nào:** Khi draft v7 STABLE + đã test thực tế đủ
> **Nguyên tắc:** Sửa 1 lần duy nhất, chất lượng cao, không sửa đi sửa lại

---

## 1. Đổi Tên Chính

```
LỊCH SỬ ĐỔI TÊN:
  v6.0: PE (Prediction Error) — từ Schultz 1997
  v7.0 đầu: UD (Unconscious Desire) — reframe PE thành desire-based
  v7.0 giữa: UD (Unconscious Desire Match / UDM) — thêm "match" → thừa → bỏ
  v7.0 sau: UD (Underlying Drive) — bỏ "Unconscious" (quá binary, Freud-ish)
  v8.0: Schema-Drive — tên CHÍNH XÁC NHẤT, tự giải thích

  → TẤT CẢ tên trên (PE, UD, Unconscious Desire, UDM, Underlying Drive)
     đều CHỈ CÙNG 1 CONCEPT — chỉ khác tên qua quá trình refine
  → v8.0 thống nhất: Schema-Drive = tên cuối cùng
  → Ai đọc file CŨ thấy PE/UD/UDM → biết = Schema-Drive

Lý do chọn Schema-Drive:
  → Schema-Drive CHÍNH XÁC hơn: mọi drive ĐỀU từ schema
  → Không binary (conscious/unconscious) → gradient theo schema depth + modality
  → PFC chỉ brake/workspace/translate → KHÔNG drive → drive = từ SCHEMA
  → "Schema-Drive" = tên tự giải thích: drive CỦA schema, không cần viết tắt

Phạm vi sửa:
  → TẤT CẢ files trong Research/ + Game-Industry/
  → Search-replace: "PE"/"UD"/"Unconscious Desire"/"Underlying Drive" → "Schema-Drive"
  → ⚠️ CẨN THẬN: "UD" trong "UD-" prefix, "PE" trong "PE-Sensitivity" (v6 legacy)
  → Kiểm tra context mỗi chỗ (không replace blind)
```

---

## 2. Rename Files

```
CŨ                              → MỚI
Core-v7-UD.md                   → Core-v8.md
UD-Hypothesis.md                → Schema-Drive-Hypothesis.md
UD-Parenting.md                 → Schema-Drive-Parenting.md (hoặc giữ tên, chỉ sửa nội dung)

Cân nhắc:
  → Có nên rename TẤT CẢ files có "UD" hay chỉ core files?
  → Đề xuất: rename core files + giữ tên files phụ (tránh break references)
  → Update references TRONG files khi rename
```

---

## 3. Thuật Ngữ Cần Đồng Bộ

```
CHECK + UPDATE trong TẤT CẢ files:

  "UD" → "Schema-Drive" (hoặc "SD" nếu cần viết tắt — nhưng tránh viết tắt)
  "UD State" → "Schema-Drive State" (hoặc giữ "SD State")
  "UD Arbitration" → "Schema-Drive Arbitration"
  "UD Signal" → "Schema-Drive Signal"
  "UD-centric" → "Schema-Drive-centric"

  GIỮ NGUYÊN (đã đồng bộ):
    Experience / Connection (Lớp 1)
    Novelty / Status (Lớp 2)
    Workspace + Brake + Translator (PFC)
    Present / Desire / Coherence (SD State)
    Body Baseline State (schema sâu nhất)

  ĐÃ ĐỔI TRONG V7 (không cần sửa lại):
    "Conductor/nhạc trưởng" → đã đổi thành "Workspace+Brake+Translator"
    "Opioid/Oxytocin" → đã thêm "Experience/Connection" labels
    "PE" → đã đổi thành "UD" (sẽ thành "Schema-Drive")
    "Fulfilled/Unfulfilled" → đã đổi thành "Present/Desire"
```

---

## 4. Nội Dung Cần Review

```
CÁC SECTION CẦN CHECK khi build v8:

Core-v8.md (từ Core-v7-UD.md):
  □ Header: remove "DRAFT", update version
  □ §1: update definition Schema-Drive
  □ §4.3: PFC definition final (Workspace+Brake+Translator — check vẫn consistent)
  □ §5.2: Schema valence note → check consistent với Schema-Atlas.md
  □ §12 File Map: update tên files mới
  □ §13 References: update

Schema-Drive-Hypothesis.md (từ UD-Hypothesis.md):
  □ Toàn bộ "UD" → "Schema-Drive"
  □ §10 Naming: update lịch sử tên (thêm "Schema-Drive" là tên cuối)
  □ Công thức: update notation

Các files khác:
  □ Search "UD" → replace per context
  □ Check cross-references vẫn đúng sau rename
  □ Game-Industry/ files: ít mention "UD" → nhanh
```

---

## 5. Cần Làm TRƯỚC Khi Build v8

```
□ Test framework trên game thật (feel tuning, ABTest)
□ Predict 1-2 người thật (observable behavior → check accuracy)
□ Ít nhất 1 external review (ai đó có background đọc qua)
□ Ghi nhận: cases nào framework predict ĐÚNG, cases nào SAI
□ Fix issues từ testing → update draft v7 → RỒI mới build v8

→ v8 = "production ready" — draft v7 hiện tại = "research draft"
→ KHÔNG rush v8 — v7 draft CẦN test trước
```

---

## 6. File Structure v8 Dự Kiến

```
Human-Predictive-Drive/
├── Core-v8.md                           ← MAIN FILE (từ Core-v7-UD.md)
├── Research/
│   ├── Core Theory/
│   │   ├── Schema-Drive-Hypothesis.md   ← Giả thiết gốc + evidence
│   │   ├── Schema-Atlas.md              ← Schema axes + body baseline
│   │   ├── Modality-Analysis.md         ← 5 Experience + 1 Communication
│   │   ├── PFC-Analysis.md              ← Workspace + Brake + Translator
│   │   ├── Imagination-Analysis.md      ← Tưởng tượng + chain direction
│   │   ├── Emotion-Map.md               ← Cảm xúc map
│   │   └── Threshold-Analysis.md        ← Threshold decompose
│   ├── Applications/
│   │   ├── Body-Needs.md                ← 6 nhóm nhu cầu
│   │   ├── Body-Needs-ByAge.md          ← Theo độ tuổi
│   │   ├── Drive-Optimization.md        ← Tối ưu drive bền vững
│   │   ├── Addiction-Analysis.md         ← Cơ chế nghiện
│   │   ├── Schema-Drive-Parenting.md    ← Phát triển trẻ em
│   │   ├── Hidden-Genius.md             ← Tiềm năng ẩn
│   │   └── Industry-Serve-BodyNeeds.md  ← Phân tích ngành nghề
│   ├── Meta/
│   │   ├── Epistemological-Position.md
│   │   ├── Creator-Lens.md
│   │   └── Meta-Impact.md
│   └── Legacy/                           ← Files cũ tham khảo
│       ├── Core-v7-Draft-Good.md
│       ├── Component-Interaction-Map.md
│       └── ...
├── Game-Industry/                        ← Giữ nguyên (ít thay đổi)
└── Validation/                           ← Test results khi có
```

---

> *Plan v8.0 — tạo khi draft v7 stable + đã test thực tế*
> *Ước lượng effort: 1-2 ngày rename + review nếu draft KHÔNG thay đổi thêm*
