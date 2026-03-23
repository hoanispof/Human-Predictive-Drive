# Plan Update v8.0 — Human Predictive Drive

> **Mục đích:** Roadmap build v8.0 từ v7.5 draft
> **Khi nào:** Khi Architecture-v7.5-Draft.md đã somatic confirm + test đủ case
> **Core mới:** Architecture-v7.5-Draft.md → Core-v8.md
> **Nguyên tắc:** Incremental update (giữ insights cũ, sửa kiến trúc), không burn and rebuild

---

## 1. Lịch Sử Framework

```
v1.0:  PE (Prediction Error) — 1 concept từ Schultz 1997
v2-3:  UD (Unconscious Desire) → UDM → Underlying Drive — đổi tên, mở rộng
v4-5:  3 lớp hormone (Source/Amplifier/Modulator), 10 channels — phức tạp dần
v6.0:  PE-centric, hormone layers chi tiết
v7.0:  Schema-Drive, PFC 5 functions, Satisfaction Signal, Dual Reward System
       "Mọi drive từ schema" — rename PE → Schema-Drive

v7.5 DRAFT (hiện tại — chưa chính thức):
  THAY ĐỔI KIẾN TRÚC LỚN:
    ① Body-Base 4 layers: L0(Alive) + L1(Survival) + L2(Quality) + L3(Pattern)
    ② L0 Alive = MẠNH NHẤT: emergency, protect gene, suppress tất cả
    ③ Novelty + Status + Protect chuyển vào Body-Base L3 (body-level, animals có)
    ④ L3 bộ ba: Novelty(expand) + Status(calibrate) + Protect(defend)
    ⑤ Imagine = PFC layer: Novelty-Schema(PULL) + Threat-Schema(PUSH)
    ⑥ Baseline-drive: cortisol baseline tách riêng, 7 modes
    ⑦ Status redefined: "schema access map" (không phải hierarchy rank)
       + Status 3 layers (baseline / per-context quen / context mới)
       + Switch context ≠ calibrate status
       + Serotonin = candidate hormone (chưa proven ở người)
    ⑧ Emergent: Shared Exp ↔ Intimate (spectrum, không phải channels riêng)
    ⑨ "Imagine LUÔN phục vụ Body-Base" — verified, không ngoại lệ
    ⑩ Schema trigger → Hormone sustain (không phải hormone drive)
    ⑪ PULL vs PUSH: Novelty(PULL có điểm dừng) vs Threat(PUSH không điểm dừng)
    ⑫ Cortisol × Body-Base: suppress cả 3 khi cao → disconnect mechanism
    ⑬ Schema override spectrum: quên ăn trưa → tử vì đạo (cùng cơ chế, khác mức độ)
    ⑭ Schema override L0 Alive: CHỈ khi redefine "alive tiếp" (gene/soul/group)
    ⑮ Human khung bao quanh toàn bộ (body+imagine+schema), Domain nằm ngoài trong Environment
    ⑯ Protect = L3 channel mới (vasopressin candidate): bảo vệ "CỦA TÔI"
       ⚠️ L3 Protect (negotiate được) ≠ L0 Protect Gene (không negotiate)
    ⑰ DRD4: data đúng, interpretation "kém nhạy → seek more" có lỗ hổng logic
       COMT = primary mechanism cho PFC clear speed
    ⑱ "Attack" = KHÔNG phải drive riêng → Status extreme case (gap cực lớn)

v8.0 DỰ KIẾN:
  = v7.5 draft CHÍNH THỨC HÓA + toàn bộ files update theo kiến trúc mới
```

---

## 2. Thay Đổi Kiến Trúc Chính: v7 → v8

```
KIẾN TRÚC CŨ (v7):
  Lớp 1 Source:     Opioid (Experience) + Oxytocin (Connection)
  Lớp 2 Amplifier:  Dopamine (Novelty) + Serotonin (Status)
  Lớp 3 Modulator:  Cortisol, NE, Vasopressin,...

KIẾN TRÚC MỚI (v8):
  Environment (bao trùm)
    Human (con người):
     Body-Base:
      Layer 0 — Alive: emergency, reflex 50ms, protect gene
      Layer 1 — Survival: Oxygen, Nutrition, Temperature, Pain-free, Sleep
      Layer 2 — Quality: Experience(Sensory, Aesthetic, Comfort) + Connection
      Layer 3 — Pattern: Novelty(Mastery, Coherence) + Status(Being Seen, Belonging) + Protect
      Emergent: Shared Exp ↔ Intimate (spectrum depth)
    Baseline-drive: cortisol baseline, 7 modes (IDLE→CRASH)
    Imagine: Novelty-Schema(PULL) + Threat-Schema(PUSH) → phục vụ Body-Base
    Hormone phụ gia: NE, Dopamine, Cortisol 3 mode, Sat.Signal, Endorphin,...
    Schema: xuyên suốt body→imagine, gradient, AI-assisted
    Domain: ghi nhận sự tồn tại, AI hỗ trợ khi cần

CHANNEL MAPPING (cũ → mới):
  E1 Sensory    → L2 Experience:Sensory
  E2 Mastery    → L3 Novelty:Mastery
  E3 Coherence  → L3 Novelty:Coherence
  E4 Aesthetic  → L2 Experience:Aesthetic
  E5 Comfort    → L2 Experience:Comfort
  C1 Intimate   → Emergent (deep end of spectrum)
  C2 Belonging  → L3 Status:Belonging
  C3 Being Seen → L3 Status:Being Seen
  C4 Touch      → L2 Connection (expanded: skin+eye+ear+presence)
  C5 Shared Exp → Emergent (shallow end of spectrum)
  NEW: L0 Alive (emergency, protect gene)
  NEW: L1 Survival (5 channels: oxygen, nutrition, temp, pain-free, sleep)
  NEW: L3 Protect (bảo vệ "CỦA TÔI", vasopressin candidate)
  NEW: Baseline-drive (cortisol, 7 modes)
  NEW: Threat-Schema (PUSH drive)
  NEW: Human khung (bao quanh body+imagine+schema)
  NEW: Schema override spectrum (quên ăn → tử vì đạo)
```

---

## 3. Thuật Ngữ v8

```
ĐÃ ỔN ĐỊNH (giữ nguyên):
  Schema-Drive = tên framework chính
  Satisfaction Signal = body báo "đủ" (prolactin = candidate)
  PFC = Draft + Test + Route + Brake + Translator (5 functions)
  "Mong muốn của schema" (không phải "ô trống")
  "Không có schema âm" → chỉ có schema conflict trong context
  5 Experience Modalities + 1 Communication Modality
  Body Baseline State = deepest schema

MỚI TRONG v7.5 (cần đồng bộ vào v8):
  Body-Base = Layer1 + Layer2 + Layer3 (thay "3 Lớp hormone")
  Baseline-drive = cortisol baseline (tách riêng khỏi "Lớp 3 modulator")
  Novelty-Schema = PULL drive qua PFC (thay "Dopamine Amplifier")
  Threat-Schema = PUSH drive qua PFC (HOÀN TOÀN MỚI)
  Status = "schema access map" (KHÔNG phải hierarchy rank)
  Status Flexibility = calibrate range rộng/hẹp theo người
  Emergent = multi-channel × depth (Shared Exp ↔ Intimate spectrum)
  Connection = skin+eye+ear+presence (expanded từ "Touch")
  7 modes = IDLE→LAZY→ACTIVE→FOCUSED→PUSH→FREEZE→CRASH
  PULL vs PUSH = Novelty(có Sat.Signal) vs Threat(không có Sat.Signal)
  Disconnect mechanism = cortisol cao → imagine thoát body control
  Virtuous/Vicious cycle = cortisol × body-need feedback loops

BỎ / THAY ĐỔI TRONG v8:
  "3 Lớp Source/Amplifier/Modulator" → giữ ở Neurochemistry detail,
    Core dùng "Body-Base 3 layers + Imagine + Hormone phụ gia"
  "4 loại drive (cortisol/dopamine/opioid/oxytocin)" → thay bằng
    "Schema trigger → Hormone sustain" + "Novelty-Schema PULL + Threat-Schema PUSH"
  "Novelty = Amplifier" → Novelty = Body-Base L3 + Imagine drive
  "Status = Amplifier" → Status = Body-Base L3 (amplifier + calibrate + access map)
  DRD4 "kém nhạy → seek more" → note "data đúng, interpretation có lỗ hổng logic"
    COMT = primary mechanism cho PFC clear speed (improviser/specialist)
```

---

## 4. File-by-File Update Plan

### 4.1 Files cần VIẾT MỚI

```
□ Core-v8.md
    → Từ Architecture-v7.5-Draft.md → chính thức hóa
    → Bao gồm: kiến trúc tổng thể, Body-Base 3L, Baseline-drive,
      Imagine, Hormone phụ gia, Schema, Domain, Predict formula
    → = FILE QUAN TRỌNG NHẤT

□ Neurochemistry-v8.md
    → Merge: Neurochemistry-v8-Draft.md + Drive-Architecture-Draft.md
    → Bảng hormone đầy đủ (nguồn phát, trigger, chức năng)
    → 3 Lớp cũ giữ lại ở đây (hormone detail, không phải Core)
    → Cortisol 3 modes, Dopamine cross-cutting, Sat.Signal bridge
```

### 4.2 Files cần UPDATE ĐÁNG KỂ (kiến trúc thay đổi)

```
□ Status-Analysis-v2.md — ĐÃ VIẾT MỚI ✅
    → Status = schema access map (không phải hierarchy)
    → Scan mechanism, per-person × per-context
    → Status Flexibility (ổn định vs dao động)
    → Belonging = cached status maps
    → Switch context ≠ calibrate status (3 layers Status)
    → Serotonin ratchet (dễ lên, kháng xuống)
    → Quân đội = status optimization system
    → Status thực tế = 5-20 người quen
    → Evidence limitations (function confirmed, hormone = candidate)
    → "Attack" = Status extreme case
    → CÒN CẦN khi v8 final: check consistency với Core-v8.md chính thức

□ Layer1-Channels.md
    → RESTRUCTURE: E1-E5 + C1-C5 → L1(5) + L2(4) + L3(4) + Emergent(2)
    → Hoặc: đổi tên thành "Body-Base-Channels.md"

□ Body-Needs.md
    → UPDATE: 6 groups map vào L1+L2+L3 mới
    → Check: 5 loại chán vẫn consistent

□ Drive-Optimization.md
    → UPDATE: 3 Layers (Pressure+Challenge+Autonomy) → map vào Baseline-drive
    → Thêm: PULL vs PUSH implication cho wellbeing
    → Thêm: Disconnect mechanism khi cortisol quá cao

□ Prolactin-Analysis.md
    → UPDATE: Satisfaction Signal hoạt động KHÁC nhau theo PULL/PUSH
    → PULL channels: Sat.Signal RÕ → có điểm dừng
    → PUSH channels: Sat.Signal MƠ HỒ/KHÔNG → anxiety

□ Threshold-Analysis.md
    → UPDATE: Satisfaction Threshold → link tới Baseline-drive modes
    → Sweet spot concept consistent với 7 modes

□ Addiction-Analysis.md
    → UPDATE: addiction = hijack CHANNEL CỤ THỂ nào (L2/L3)
    → Thêm: PULL addiction (novelty loop) vs PUSH addiction (threat loop)

□ UD-Parenting.md → rename Schema-Drive-Parenting.md
    → UPDATE: L1/L2/L3 per age
    → Thêm: Baseline-drive mode per child (calibrate)
    → Thêm: PUSH vs PULL parenting style impact

□ Reward-Dual-System.md
    → UPDATE: "Schema trigger → Hormone sustain" concept
    → Check: Imagine System = Novelty-Schema + Threat-Schema

□ PFC-Analysis.md
    → UPDATE §8: DRD4 note "data đúng, interpretation lỗ hổng"
    → UPDATE §8: COMT = primary cho clear speed
    → UPDATE §8: 3 thuộc tính PFC (Capacity, Clear Speed, Sensitivity)
    → Thêm: PFC draft pipeline (lấy từ vô thức → remix → test → compile)
    → Thêm: Compiled schema decay + reactivation (Schema lifecycle)
```

### 4.3 Files cần UPDATE NHẸ (thay tên + check consistency)

```
□ Schema-Atlas.md
    → KHÔNG cần viết lại — schema properties independent với layer changes
    → Sửa nhẹ: vài dòng terminology cũ (Lớp 1 Source → Body-Base L2, etc.)
    → Thêm: schema lifecycle (form → compile → decay → reactivate)
    → Thêm: link "schema override spectrum → xem Architecture §2.5"
    → Thêm: "schema override L0 Alive → xem Architecture §2.0"
    → §6 Body-Needs mapping: thêm note "xem Architecture cho L0-L3 mới"
    → "UD" → "Schema-Drive" nếu còn

□ Modality-Analysis.md
    → §11 Concept-first vs Label-first: ĐÃ có, check consistent
    → Broca sequence processing: ĐÃ có, check

□ Imagination-Analysis.md
    → Check references đúng v8 terms

□ Body-Needs-ByAge.md
    → Check: age stages vẫn consistent với L1/L2/L3

□ Hidden-Genius.md
    → Check: consistent, thay terms nếu cần

□ Industry-Serve-BodyNeeds.md
    → Check template: 6 hướng mở rộng vẫn OK

□ Body-Listening.md
    → Check: 4 levels consistent với Baseline-drive modes

□ Chemical-Enhancement-Notes.md
    → Thêm: "chất kích thích = amplifier execution, không phải source"
    → Thêm: "chất + chunks = output, chất - chunks = rác"

□ Emotion-Map.md, Conflict-Dynamics.md, Mismatch-Patterns.md,
  Depression-Predictive-Model.md, Social-Pressure-Tradeoff.md
    → Check consistency, update terms nếu cần

□ UD-Hypothesis.md → rename Schema-Drive-Hypothesis.md
    → "UD" → "Schema-Drive" toàn bộ
```

### 4.4 Files KHÔNG CẦN thay đổi

```
✅ Innovation-Geography.md — independent analysis
✅ Climate-Cognition.md — independent analysis
✅ Human-AI-Future.md — independent analysis
✅ Body-Neural-Network.md — independent analysis
✅ Psychometrics-Mapping.md — mapping tool
✅ Religion.md — application
✅ Macro-Civilization.md — application
✅ Meta-Impact/ files — meta analysis
✅ plan-web-visualization.md — plan file
```

### 4.5 Files MỚI cần tạo cho v8

```
□ Threat-Drive-Analysis.md — ĐÃ CÓ draft, cần finalize
□ Status-Analysis-v2.md — ĐÃ VIẾT ✅ (thay thế Status-Analysis.md cũ)
□ Body-Neural-Network.md — ĐÃ VIẾT ✅ (neurons ngoài não, ENS, distributed)
□ Innovation-Geography.md — ĐÃ VIẾT ✅ (trade hub, Áo-Hung, AI era)
□ Climate-Cognition.md — ĐÃ VIẾT ✅ (double calibration, AC analysis)
□ Human-AI-Future.md — ĐÃ VIẾT ✅ (Prisoner's Dilemma, Neanderthal, collective)
□ Có thể: Baseline-Drive-Analysis.md — 7 modes chi tiết
□ Có thể: Alive-Analysis.md — L0 emergency chi tiết (nếu cần)
```

### 4.6 Draft files (workspace — archive hoặc delete sau v8)

```
→ Architecture-v7.5-Draft.md → thành Core-v8.md
→ Drive-Architecture-Draft.md → merge vào Neurochemistry-v8.md
→ Reward-Channels-Draft.md → insights đã absorb vào Architecture
→ Layer-Architecture-Draft.md → legacy
→ Core-v7-UD.md → move to Legacy/
→ Neurochemistry-v8-Draft.md (cũ) → merge vào Neurochemistry-v8.md
→ Parameters-Review.md → legacy (parameters đã resolved)
→ Component-Interaction-Map.md → legacy
```

---

## 5. Cần Làm TRƯỚC Khi Build v8

```
SOMATIC CONFIRM:
  □ Đọc lại Architecture-v7.5-Draft.md — body nói "khớp" chưa?
  □ Test: map 10+ hành vi thực tế vào kiến trúc mới → đều trace được?
  □ Test: map bản thân (IsPof) vào → đúng ko?
  □ Test: map 2-3 người quen vào → predict đúng ko?

EDGE CASES:
  □ Người trầm cảm nặng → L1 Sleep thiếu + Baseline-drive cực thấp → predict?
  □ Người nghiện nặng → channel hijack + disconnect → predict?
  □ Trẻ sơ sinh → chỉ L1 + L2, L3 chưa có → predict?
  □ Thiền sư → L1+L2 optimal, Baseline-drive thấp, Imagine minimal → predict?
  □ Chiến tranh → L1 override tất cả → predict?

CÂU HỎI MỞ (cần ngẫm):
  □ Aesthetic: ĐÃ GIẢI QUYẾT ✅ — body phản ứng TRƯỚC lý do, L2 đúng vị trí
  □ Body-level Novelty vs PFC Novelty: ranh giới chính xác?
  □ Baseline-drive có phải LUÔN cortisol? Hay hormone khác contribute?
  □ Being Seen: ĐÃ GIẢI QUYẾT ✅ — thuần Status (calibrate đúng thực tế)
  □ Game industry files: update 8 channels → reorganize theo L0/L1/L2/L3?
  □ L0 Alive vs L1 Survival: ranh giới escalation chính xác?
  □ L3 Protect vs L0 Protect Gene: khi nào escalate?
  □ Serotonin: chưa proven ở người — framework bind function, not hormone
  □ Vasopressin: candidate cho Protect — có thể nhiều hormone kết hợp

VALIDATION (khi có):
  □ Cho 1-2 người đọc Core-v8 draft → họ hiểu không?
  □ Dùng framework predict hành vi → test accuracy
  □ Code game với framework → player behavior match?
```

---

## 6. File Structure v8 Dự Kiến

```
Human-Predictive-Drive/
├── Core-v8.md                            ← MAIN (từ Architecture-v7.5-Draft)
├── Research/
│   ├── Core Theory/
│   │   ├── Schema-Drive-Hypothesis.md
│   │   ├── Schema-Atlas.md
│   │   ├── Body-Base-Channels.md         ← (từ Layer1-Channels, restructured)
│   │   ├── Modality-Analysis.md
│   │   ├── PFC-Analysis.md
│   │   ├── Imagination-Analysis.md
│   │   ├── Reward-Dual-System.md
│   │   ├── Status-Analysis.md            ← REWRITE (schema access map)
│   │   ├── Prolactin-Analysis.md
│   │   ├── Threat-Drive-Analysis.md      ← NEW
│   │   ├── Threshold-Analysis.md
│   │   ├── Body-Listening.md
│   │   ├── Body-Neural-Network.md
│   │   └── Schema-Diagnostic.md
│   ├── Applications/
│   │   ├── Body-Needs.md
│   │   ├── Body-Needs-ByAge.md
│   │   ├── Drive-Optimization.md
│   │   ├── Addiction-Analysis.md
│   │   ├── Schema-Drive-Parenting.md
│   │   ├── Hidden-Genius.md
│   │   ├── Industry-Serve-BodyNeeds.md
│   │   ├── Emotion-Map.md
│   │   ├── Depression-Predictive-Model.md
│   │   ├── Chemical-Enhancement-Notes.md
│   │   ├── Innovation-Geography.md
│   │   ├── Climate-Cognition.md
│   │   └── Human-AI-Future.md
│   ├── Meta/
│   │   ├── Epistemological-Position.md
│   │   └── Meta-Impact.md
│   └── Legacy/                            ← v7 files tham khảo
│       ├── Core-v7-UD.md
│       ├── Drive-Architecture-Draft.md
│       ├── Reward-Channels-Draft.md
│       ├── Parameters-Review.md
│       └── Component-Interaction-Map.md
├── Neurochemistry/
│   └── Neurochemistry-v8.md              ← Hormone detail (3 Lớp giữ ở đây)
├── Ask-AI/
│   ├── Ask-AI.md
│   ├── Ask-AI-Parent.md
│   └── Ask-AI-Guide.md
├── Game-Industry/                         ← Update nhẹ theo v8 terms
│   ├── Core-Principles.md
│   ├── Player-Psychology.md
│   ├── Gameplay-Design.md
│   ├── Team-Workflow.md
│   ├── Visual-Audio.md
│   ├── Analytics-Guide.md
│   └── Monetization-Ethics.md
└── Validation/                            ← Test results khi có
```

---

## 7. Thứ Tự Thực Hiện

```
PHASE 1 — Chính thức hóa Core:
  □ Somatic confirm Architecture-v7.5-Draft
  □ Test edge cases (§5)
  □ Architecture-v7.5-Draft.md → Core-v8.md
  □ Resolve câu hỏi mở (§5)

PHASE 2 — Update Core Theory files:
  □ Status-Analysis.md (REWRITE — quan trọng nhất)
  □ Body-Base-Channels.md (RESTRUCTURE L1/L2/L3)
  □ PFC-Analysis.md (DRD4 note + COMT primary + pipeline)
  □ Prolactin-Analysis.md (PULL vs PUSH Sat.Signal)
  □ Reward-Dual-System.md (schema trigger concept)
  □ Threat-Drive-Analysis.md (finalize)
  □ Neurochemistry-v8.md (merge drafts)

PHASE 3 — Update Application files:
  □ Body-Needs.md, Drive-Optimization.md, Addiction, Parenting
  □ Threshold, Schema-Diagnostic, Body-Listening
  □ Chemical-Enhancement-Notes

PHASE 4 — Update peripheral + rename:
  □ Schema-Atlas, Modality, Imagination, Hidden-Genius,...
  □ Rename: UD-*.md → Schema-Drive-*.md
  □ Search-replace "UD" → "Schema-Drive" toàn bộ
  □ Move legacy files

PHASE 5 — Game Industry + Ask-AI:
  □ Game files update terms
  □ Ask-AI wrappers update theo v8

→ Không rush — incremental, test mỗi phase
→ Mỗi file update → check với Core-v8 → consistent?
→ AI hỗ trợ: đọc Core-v8 + file cũ → generate update
```

---

> *Plan v8.0 — updated 2026-03-23*
> *Core: Architecture-v7.5-Draft.md (chờ somatic confirm)*
> *Ước lượng: Phase 1-2 quan trọng nhất, Phase 3-5 có thể dần dần*
