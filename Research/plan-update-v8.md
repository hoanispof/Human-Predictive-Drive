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
    5 Experience Modalities + 1 Communication Modality
    "Mong muốn của schema" (thay "ô trống" — dynamic, không static)

  ĐÃ ĐỔI TRONG V7 (không cần sửa lại):
    "Conductor/nhạc trưởng" → "Workspace+Brake+Translator"
    "Opioid/Oxytocin" → thêm "Experience/Connection" labels
    "PE" → "UD" (sẽ thành "Schema-Drive")
    "Fulfilled/Unfulfilled" → "Present/Desire"
    "Ô trống" → "Mong muốn của schema" (schema desire)
    "Schema âm/dương" → "Schema xung đột trong context" (không có schema âm cố định)
    "6 modalities ngang hàng" → "5 Experience + 1 Communication"
    "Verbal = modality tư duy" → "Verbal = label/transfer/compress (không compute)"

  ĐÃ BỎ TRONG V7:
    UD Sensitivity (cả 4 sub-parameters):
      ① Amplitude → BỎ → emergent "Cường Độ Phản Ứng"
      ② Precision → BỎ → emergent từ schema quality × conflict × PFC
      ③ Decay Rate → BỎ → emergent "Tốc Độ Quen" (5 giai đoạn cycle)
      ④ Generalization → BỎ → spreading activation mechanism
    Baseline Drive → BỎ → emergent metric
    Schema Ceiling → BỎ → emergent metric
    "Chán" 3 loại → MỞ RỘNG thành 5 loại (Fulfilled/Over/Hijacked/Stagnant/Suppressed)

  ĐÃ ĐỔI/THÊM TRONG V7 (sessions gần đây):
    "Prolactin = nút dừng" → "Satisfaction Signal = cơ chế body báo đủ"
      → Framework bind CHỨC NĂNG (Satisfaction Signal), không bind HORMONE (prolactin)
      → Prolactin = candidate chính (proven sex/food), có thể có hormone khác
      → Core dùng "Satisfaction Signal" → files chuyên sâu dùng "prolactin" + caveat
    "Dopamine = desire fulfillment signal" → "Prediction Improvement Signal"
      → Dopamine = imagine predict "TỐT HƠN cho body" → fire
      → Khác RPE "Prediction Error": error = vô hướng, improvement = có hướng (tốt cho body)
    Reward Dual System (insight MỚI):
      → Hệ thống 1: Imagine predict → dopamine → DRIVE (nhanh, có thể sai)
      → Hệ thống 2: Body confirm → Satisfaction Signal → SATISFY (chậm, chính xác)
      → Body feedback → imagine calibrate → predict chính xác dần
    Status tách 2 tham số:
      → Status Position (serotonin): "đang ở ĐÂU" → amplify mọi channel
      → Status Aspiration (schema): "muốn ở ĐÂU" → gap = drive chase
    4 loại drive (không chỉ cortisol):
      → Cortisol drive (sợ/survive) + Dopamine drive (tò mò/muốn)
      → Opioid drive (sướng/tiếp tục) + Oxytocin drive (ấm/kết nối)
      → Cortisol = activation energy phổ biến, KHÔNG phải drive duy nhất

  CÂN NHẮC BỎ TRONG V8:
    Threshold → ĐỔI TÊN "Satisfaction Threshold"
      → "Dễ thỏa mãn hay khó thỏa mãn" = emergent từ:
        prolactin capacity + schema suppress/drive + pressure/challenge + channel count
      → VẪN GIỮ như mục lục (nhiều người quan tâm, dễ hiểu, dễ trao đổi)
      → NHƯNG: ghi rõ = EMERGENT metric, không phải parameter đơn
      → Phân biệt: "đủ thật" (prolactin) vs "ép đủ" (schema suppress)
      → Threshold-Analysis.md → rename "Satisfaction-Threshold.md"
      → Search "Threshold" trong tất cả files → replace/update context phù hợp
```

---

## 4. Nội Dung Cần Review

```
CÁC SECTION CẦN CHECK khi build v8:

Core-v8.md (từ Core-v7-UD.md):
  □ Header: remove "DRAFT", update version
  □ §1: update definition Schema-Drive + "mong muốn của schema" (không phải "ô trống")
  □ §1.1: vocabulary final — 5 loại chán + Schema-Drive terms
  □ §4.2: parameters final — UD Sensitivity ĐÃ BỎ, emergent metrics note
  □ §4.3: PFC definition final (Workspace+Brake+Translator)
  □ §5.2: "Không có schema âm" + "mong muốn" + Body Baseline
  □ §5.3: Drive Equation với "mong muốn" concept
  □ §5.6: SD State (Experience × Desire × Coherence) — rename UD→SD
  □ §5.7: 5 giai đoạn cycle + portfolio of cycles (nếu thêm)
  □ §5.8: SD Arbitration → Schema-Drive Arbitration
  □ §11.2: tham số ước lượng — check consistent
  □ §12 File Map: update tên files mới
  □ §13 References: update

Schema-Drive-Hypothesis.md (từ UD-Hypothesis.md):
  □ Toàn bộ "UD" → "Schema-Drive"
  □ §10 Naming: update lịch sử tên
  □ Công thức: update notation
  □ "Ô trống" → "mong muốn" nếu có mention

Schema-Atlas.md:
  □ §1.2 Valence: check "không có schema âm" consistent
  □ §1.2 Trade-off: check "mong muốn" consistent
  □ §5 Body Baseline: check references
  □ §5.6 Diagnostic: check "suy ngược" 3 con đường

Modality-Analysis.md:
  □ §2.0: "5 Experience + 1 Communication" — đã có
  □ §3: Encode types + depth metric — check
  □ §5+: Verbal = label/transfer/compress — check consistent

PFC-Analysis.md:
  □ §1.2: Workspace+Brake+Translator — đã có
  □ §7: 5 kịch bản — KB4 + evidence
  □ §8: Hardware receptor variants (DRD4, COMT, MAO-A) — đã có
  □ §9: Developmental evidence — check

Industry-Serve-BodyNeeds.md:
  □ §4: Baseline + 6 Hướng Mở Rộng — check template final
  □ §10: Hướng dẫn cho AI — check actionable

Threshold-Analysis.md:
  □ §2: Threshold = f(Pressure, Challenge) per domain — ĐÃ refine
  □ §3: Pressure Drive vs Challenge Drive — check consistent
  □ §3.4: Body Baseline Carry + Calibrate Skill 4 levels — ĐÃ thêm
  □ §4: Ví dụ + kiểm chứng — check

Schema-Diagnostic.md (FILE MỚI):
  □ Toàn bộ: quy trình 5 bước diagnostic + 3 con đường suy ngược
  □ §5.5: Calibrate Level assessment — ĐÃ thêm
  □ Check: consistent với Schema-Atlas + Threshold-Analysis

Layer1-Channels.md (FILE MỚI):
  □ Toàn bộ: 10 sub-channels (5 Experience + 5 Connection)
  □ Check: consistent với Core §4.1 (Neurochemistry 3 Lớp)

Drive-Optimization.md:
  □ §9: 3 Layers (Pressure + Challenge + Autonomy) — ĐÃ refine
  □ §6: Endpoint hạnh phúc — check
  □ Check: consistent với Threshold-Analysis (Pressure × Challenge)

Body-Needs.md:
  □ §11: 5 loại chán (Fulfilled/Over/Hijacked/Stagnant/Suppressed) — ĐÃ thêm
  □ §11.7: Sweet Spot Chart — check consistent

Reward-Dual-System.md (FILE MỚI):
  □ Toàn bộ: 2 hệ thống reward (Imagine + Body) + luồng tương tác
  □ §4: "Prediction Improvement" thay "Prediction Error" — check
  □ §6: So sánh AlphaGo vs Con người — check
  □ Check: consistent với Core §4.1 (dopamine update)

Status-Analysis.md (FILE MỚI):
  □ Toàn bộ: Status Position + Aspiration tách 2
  □ Check: consistent với Core §4.1 (Lớp 2 Status update)
  □ Check: consistent với Neurochemistry-v8 §3 (Serotonin)

Prolactin-Analysis.md (FILE MỚI):
  □ Toàn bộ: Satisfaction Signal reasoning + tại sao không phải "phanh"
  □ §3.1: 4 loại drive — check consistent
  □ §4: Prolactin chỉ fire khi body REQUEST — check
  □ Check: consistent với Neurochemistry-v8 §4.4

Body-Listening.md (FILE MỚI):
  □ Toàn bộ: kỹ năng nghe body + 4 levels + bài tập
  □ Check: consistent với Reward-Dual-System + Layer1-Channels

Neurochemistry-v8-Draft.md (FILE MỚI — Core-Deep-Dive):
  □ Toàn bộ: kiến trúc 3 Lớp mới + chi tiết từng hormone
  □ §4.4: Satisfaction Signal caveat (chức năng vs hormone)
  □ Check: consistent với Core §4.1

Ask-AI.md + Ask-AI-Parent.md + Ask-AI-Guide.md (FILES MỚI):
  □ Wrappers cho phổ thông dùng framework qua AI
  □ Check: instructions consistent với Core final

Imagination-Analysis.md (ĐÃ UPDATE):
  □ §2: Verbal = communication note — ĐÃ thêm
  □ §7: Reward Dual System reference — ĐÃ thêm
  □ Check: consistent với Modality-Analysis + Reward-Dual-System

Các files khác:
  □ Search "UD" → replace per context (TẤT CẢ files)
  □ Search "ô trống" → replace "mong muốn" (nếu có)
  □ Search "schema âm" → check context (đổi nếu binary, giữ nếu correct)
  □ Search "prolactin" trong Core → đã đổi "Satisfaction Signal" → verify
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
□ Ngẫm thêm: "mong muốn của schema" concept đã chính xác chưa?
□ Ngẫm thêm: 5 giai đoạn cycle có đủ chưa? Thiếu giai đoạn nào?
□ Ngẫm thêm: Hardware receptor insight CÓ thay đổi gì thêm?
□ Ngẫm thêm: Industry-Serve template ĐÃ đủ chưa? Test thêm vài ngành?
□ Ngẫm thêm: Threshold = f(Pressure, Challenge) per domain — đủ chính xác chưa?
□ Ngẫm thêm: 3 Layers (Pressure + Challenge + Autonomy) — đủ hay thiếu layer?
□ Ngẫm thêm: Calibrate Skill 4 levels — có level nào thiếu?
□ Ngẫm thêm: 10 sub-channels Lớp 1 — đủ chưa? Có sub-channel nào miss?
□ Ngẫm thêm: Schema gradient body→domain — có cases nào KHÔNG fit?
□ Ngẫm thêm: "Không có schema âm" — có edge case nào phản bác?
□ Ngẫm thêm: Schema Diagnostic 5 bước — test trên người thật?
□ Ngẫm thêm: Reward Dual System — imagine predict vs body confirm ĐỦ chưa? Thiếu hệ thống 3?
□ Ngẫm thêm: "Prediction Improvement" vs "Prediction Error" — experiment nào tách biệt?
□ Ngẫm thêm: Satisfaction Signal — prolactin CHỈ 1 candidate? Hormone nào khác?
□ Ngẫm thêm: Status Position vs Aspiration — tách ĐÚNG chưa? Có dimension thứ 3?
□ Ngẫm thêm: Body-Listening 4 levels — có level 4+ (beyond thiền sư)?
□ Ngẫm thêm: 4 loại drive (cortisol/dopamine/opioid/oxytocin) — đủ chưa?

→ v8 = "production ready" — draft v7 hiện tại = "research draft"
→ KHÔNG rush v8 — v7 draft CẦN test trước
→ Nhiều insights MỚI từ sessions gần đây — cần ngẫm + verify trước khi commit v8
```

---

## 6. File Structure v8 Dự Kiến

```
Human-Predictive-Drive/
├── Core-v8.md                           ← MAIN FILE (từ Core-v7-UD.md)
├── Research/
│   ├── Core Theory/
│   │   ├── Schema-Drive-Hypothesis.md   ← Giả thiết gốc + evidence
│   │   ├── Schema-Atlas.md              ← Schema axes + gradient + body baseline + 6 nhóm gốc
│   │   ├── Modality-Analysis.md         ← 5 Experience + 1 Communication
│   │   ├── PFC-Analysis.md              ← Workspace + Brake + Translator
│   │   ├── Imagination-Analysis.md      ← Tưởng tượng + chain direction
│   │   ├── Emotion-Map.md               ← Cảm xúc map
│   │   ├── Threshold-Analysis.md        ← Satisfaction Threshold + Calibrate
│   │   ├── Layer1-Channels.md           ← 10 sub-channels (5 Experience + 5 Connection)
│   │   ├── Schema-Diagnostic.md         ← 5 bước diagnostic + calibrate
│   │   ├── Reward-Dual-System.md        ← 2 hệ thống: Imagine(dopamine) + Body(prolactin) [MỚI]
│   │   ├── Status-Analysis.md           ← Position + Aspiration tách 2 [MỚI]
│   │   ├── Prolactin-Analysis.md        ← Satisfaction Signal reasoning [MỚI]
│   │   └── Body-Listening.md            ← Cách nghe body + 4 levels + bài tập [MỚI]
│   ├── Applications/
│   │   ├── Body-Needs.md                ← 6 nhóm nhu cầu + 5 loại chán + chiều giảm
│   │   ├── Body-Needs-ByAge.md          ← Theo độ tuổi
│   │   ├── Drive-Optimization.md        ← Tối ưu drive + 3 Layers (P+C+A) + endpoint
│   │   ├── Addiction-Analysis.md         ← Cơ chế nghiện
│   │   ├── Schema-Drive-Parenting.md    ← Phát triển trẻ em
│   │   ├── Hidden-Genius.md             ← Tiềm năng ẩn
│   │   └── Industry-Serve-BodyNeeds.md  ← Phân tích ngành nghề + template 6 hướng
│   ├── Meta/
│   │   ├── Epistemological-Position.md
│   │   ├── Creator-Lens.md
│   │   └── Meta-Impact.md
│   └── Legacy/                           ← Files cũ tham khảo
│       ├── Core-v7-Draft-Good.md
│       ├── Component-Interaction-Map.md
│       └── ...
├── Core-Deep-Dive/
│   └── Neurochemistry-v8-Draft.md       ← 3 Lớp chi tiết [MỚI thay v6 cũ]
├── Ask-AI.md                             ← Wrapper phổ thông [MỚI]
├── Ask-AI-Parent.md                      ← Wrapper phụ huynh [MỚI]
├── Ask-AI-Guide.md                       ← Hướng dẫn tạo wrappers [MỚI]
├── Game-Industry/                        ← Giữ nguyên (ít thay đổi)
└── Validation/                           ← Test results khi có
```

---

> *Plan v8.0 — tạo khi draft v7 stable + đã test thực tế*
> *Ước lượng effort: 1-2 ngày rename + review nếu draft KHÔNG thay đổi thêm*
