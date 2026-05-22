---
title: OCD Analysis — Qua Lens Framework v7.8
version: 2.2
created: 2026-03-27
refined: 2026-05-15
status: RESEARCH FILE v2.2 — tổng hợp suy luận từ framework v7.8 + established research
scope: |
  RESEARCH FILE: Phân tích OCD (Obsessive-Compulsive Disorder) qua mô hình
  3 tuyến phòng thủ "done" pipeline. Kết nối OCD ↔ Love ↔ Serotonin.
  v2.0 KEY CHANGES vs v1.0 (v7.5 era):
    ① Chunk dynamics mapping: OCD qua BFM (Shift/Miss/Gap)
    ② Spreading activation: serotonin ↓ = uninhibited cascade → obsessive loop
    ③ Cortisol 5 Roles applied (Holding/Threat-sustained/Silent)
    ④ PFC-Function mapping: tuyến 3 = HOLD + PROCESS, override fail mechanism
    ⑤ Love-Romantic v2.2 cross-reference updated
    ⑥ All terminology v7.5 → v7.8
  v2.1 KEY ADDITIONS (2026-04-26):
    ⑦ §4.5 Serotonin ↓ = AMPLIFIER, NOT ROOT CAUSE (feedback loop model)
    ⑧ §4.5b SPM childhood bias × OCD-like in love (anxious attachment mechanism)
    ⑨ §4.6 Cross-species evidence (deer mice, SAPAP3, Hoxb8, dogs, primates)
    ⑩ Updated Honest Assessment + Open Questions with new predictions
  v2.2 KEY ADDITIONS (2026-05-15 — post Health Conditions Drill):
    ⑪ §4.7 Basal ganglia × Parkinson architectural bridge (gate LOCKED vs gate NOISY)
    ⑫ §7.1 PTSD intrusions vs OCD obsessions — mechanism distinction (context-free vs done-pipeline)
    ⑬ §7.2 Autism × OCD co-occurrence (17.4%, cascade not comorbidity, RRBs vs compulsions)
    ⑭ Cross-refs updated: 6 drill files + dependency versions refreshed
  ⚠️ Framework KHÔNG thay thế chẩn đoán/điều trị y khoa.
  Phân tích cung cấp GÓC NHÌN bổ sung — nếu đúng, có thể giúp
  hiểu tại sao OCD xảy ra và tại sao các treatment hiện tại hoạt động.
purpose: |
  Research-level analysis: apply framework v7.8 vào failure mode.
  OCD = test case cho "done" detection mechanism:
  khi cơ chế DỪNG HÀNH VI bị lỗi → loop vô hạn.
  Love dùng CÙNG circuit nhưng CÓ exit condition (bond compile).
position: |
  Research/Health-Conditions/ — analysis file.
  Cùng folder: Hijack/ + Neurodegeneration/ + Neurodiversity/ + PTSD-Analysis.md.
dependencies:
  - Body-Feedback-Mechanism.md v2.0 — Chunk-Shift/Miss/Gap, §4 Compound, §5 Baseline Shift
  - Chunk-Activation-Dynamics.md — spreading activation, probability, trigger surface
  - Chunk.md v2.1 — substrate, compilation, hierarchy
  - Cortisol-Baseline.md v2.1 — 5 Cortisol Roles §7.7, cascade, recovery asymmetry
  - PFC-Function.md v1.2 — 24 functions, HOLD + PROCESS, reactive model
  - Status.md v2.1 — §9.2 Serotonin Ratchet, certainty bias
  - Love-Romantic.md v2.4 — §2.1 serotonin ↓40%, §3 3 primitives, §4 2-luồng
  - Feeling.md v2.1 — PFC observation interface
  - Threat.md v1.0 — 3 origin sources, threat priority
  - Connection.md v4.0 — social buffering, co-regulation
  - Protect.md v1.0 — loss aversion (OCD fear of loss)
  - Clarification/Dopamine-Is-Not-Reward.md v1.1 — dopamine = salience, not reward
  - Autism-Observation.md v1.0 — §8.4 Special Interests vs OCD, §13.1 co-occurrence 17.4%
  - PTSD-Analysis.md v1.0 — §14 context-tag model, §4 body-first temporal
  - Parkinson-Analysis.md v1.1 — §2 basal ganglia gate mechanism
sources_backup: |
  v1.0 (2026-03-27, 896L, v7.5 era) → backup/OCD-Analysis-v75-era.md
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# OCD Analysis — Qua Lens Framework v7.8

> **Bạn rửa tay. Xong. Body nhẹ. Chuyện khác.**
> **30 giây. Toàn bộ process: VÔ THỨC.**
>
> **Người OCD rửa tay. Xong... nhưng body KHÔNG nhẹ.**
> **"Done" signal fire → nhưng NOISY → body: "CHƯA CHẮC sạch."**
> **Rửa lại. Vẫn CHƯA CHẮC. Rửa lại. 50 lần. Tay rát.**
> **PFC: "TÔI BIẾT tay sạch." Body: "KHÔNG TIN."**
>
> **OCD = "done" pipeline FAILURE.**
> **3 tuyến phòng thủ dừng hành vi → 1 hoặc nhiều tuyến LỖI → loop vô hạn.**
> **PANDAS chứng minh: phá hardware tuyến 1 → OCD xuất hiện NGAY → sửa → hết.**
> **Love dùng CÙNG circuit (serotonin ↓40%) nhưng CÓ exit: bond compile → done.**
> **OCD KHÔNG CÓ exit: target không bao giờ "đủ" → cần treatment.**
>
> **⚠️ Framework cung cấp GÓC NHÌN — không thay thế chẩn đoán/điều trị y khoa.**

---

## Mục lục

- §1 — OCD LÀ GÌ
- §2 — CƠ CHẾ BÌNH THƯỜNG: "DONE" PIPELINE
- §3 — OCD = MULTI-POINT FAILURE
- §4 — V7.8 MAPPING: CHUNK DYNAMICS + SPREADING ACTIVATION + BASAL GANGLIA
- §5 — LOVE ↔ OCD: CÙNG CIRCUIT, KHÁC MỤC ĐÍCH
- §6 — SEROTONIN = "CERTAINTY BIAS"
- §7 — SPECTRUM: KHÔNG CHỈ OCD + PTSD DISTINCTION + AUTISM CO-OCCURRENCE
- §8 — TREATMENT MAP VÀO 3 TUYẾN
- §9 — TESLA CASE STUDY
- §10 — HARDWARE VS ENVIRONMENT
- §11 — HONEST ASSESSMENT
- §12 — CÂU HỎI MỞ
- §13 — CROSS-REFERENCES + STATUS

---

## §1 — OCD LÀ GÌ

```
DEFINE:
  OCD = Obsessive-Compulsive Disorder
  Obsession = suy nghĩ XÂM NHẬP lặp lại, KHÔNG MUỐN nhưng KHÔNG DỪNG được
  Compulsion = hành vi LẶP LẠI để giảm anxiety từ obsession

  Ví dụ phổ biến:
    "Tay bẩn" (obsession) → rửa tay 50 lần/ngày (compulsion)
    "Cửa chưa khóa" (obsession) → kiểm tra 10 lần trước khi ra (compulsion)
    "Số lẻ = xui" (obsession) → làm mọi thứ theo số chẵn (compulsion)

  ĐẶC ĐIỂM QUAN TRỌNG:
    → Người OCD BIẾT hành vi vô lý (PFC nhận ra — A zone)
    → NHƯNG không dừng được (chunks fire ở C+D zones KHÔNG nghe PFC)
    → = "Ego-dystonic" — PFC observe "sai" nhưng body fire "phải làm"
    → ≠ thói quen (ego-syntonic — PFC đồng ý → làm vì MUỐN)

    Qua v7.8: ego-dystonic = PFC OBSERVE (Feeling.md v2.0)
    body-chunk interaction → PFC thấy "vô lý" → nhưng PFC chỉ là OBSERVER,
    KHÔNG điều khiển trực tiếp C+D zones processing.

  🟢 Prevalence: ~2-3% dân số toàn cầu (WHO)
  🟢 Heritability: ~47-58% (Pauls 2010) → CÓ yếu tố hardware MẠNH
  🟢 Onset: BIMODAL — 2 peak:
     Peak 1: Childhood (~8-12 tuổi) — ~25-50% cases
       → Predominantly MALE
       → Genetic/hardware component MẠNH → tuyến 1 primary failure
       → Thường nặng hơn, dai dẳng hơn
     Peak 2: Late adolescence / early adult (~18-25)
       → Gender gần bằng nhau
       → Environmental triggers rõ hơn (stress, life transitions)
       → Tuyến 2+3 primary failure (PFC chưa mature + serotonin shift)
     → 2 peak MAP vào 2 failure mode KHÁC NHAU trong 3-tuyến model
```

---

## §2 — CƠ CHẾ BÌNH THƯỜNG: "DONE" PIPELINE

### §2.1 — Ví dụ: rửa tay bình thường

```
VÍ DỤ — RỬA TAY BÌNH THƯỜNG:

  ① Chunks "tay bẩn" FIRE (C+D zones, vô thức):
     → Body detect: "tay có gì đó" → compiled chunks trigger → rửa tay

  ② Hành động rửa:
     → Nước + xà phòng → giác quan báo: "tay trơn, sạch, hết dính"

  ③ "Done" detector CHECK (OFC-caudate circuit):
     → OFC nhận sensory input: "sạch"
     → Caudate nucleus: compare "hiện tại" vs "chuẩn done" (compiled baseline)
     → MATCH → fire "DONE" signal

  ④ Body-feedback propagate:
     → "Done" signal → chunks "tay bẩn" DEACTIVATE
     → Cortisol nhẹ (từ "bẩn") → DROP
     → Opioid nhẹ: body-need met → reward
     → Body relax → xong

  ⑤ PFC nhận kết quả:
     → PFC KHÔNG biết "done detector" vừa fire
     → PFC chỉ observe: "tự nhiên hết muốn rửa" → chuyện khác
     → = Toàn bộ process: C+D zones. PFC chỉ thấy OUTPUT.

TIMELINE: 30 giây → xong → quên luôn. Bình thường.
```

### §2.2 — 3 Tuyến phòng thủ

```
⭐ NÃO CÓ 3 TUYẾN đảm bảo hành vi DỪNG đúng lúc:

┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  TUYẾN 1 — "DONE" DETECTOR (automatic, C+D zones)               │
│  Hardware: OFC (orbitofrontal cortex) + caudate nucleus          │
│  Function: compare trạng thái hiện tại vs compiled "chuẩn done" │
│  Output: "DONE" signal → chunks deactivate                      │
│  Speed: nhanh nhất (milliseconds)                                │
│  🟢 Evidence: Saxena et al., Schwartz et al. — fMRI confirmed   │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TUYẾN 2 — SATISFACTION THRESHOLD (neurochemistry)               │
│  Hardware: serotonin system (toàn não)                           │
│  Function: xác định signal "done" cần MẠNH BAO NHIÊU            │
│            để được CHẤP NHẬN                                      │
│  Serotonin cao → threshold THẤP → dễ chấp nhận "done"           │
│  Serotonin thấp → threshold CAO → khó chấp nhận "done"          │
│  = Serotonin = certainty bias (Status.md v2.1 §9.2)             │
│  🟢 Evidence: SSRIs effective cho OCD (Bloch 2008)               │
│                                                                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  TUYẾN 3 — PFC OVERRIDE (conscious, chậm nhất)                  │
│  Hardware: dlPFC (dorsolateral prefrontal cortex)                │
│  Function: PFC HOLD "tôi BIẾT xong" → bias chunks → DỪNG       │
│  = Last resort khi tuyến 1+2 fail                               │
│  Depends on: PFC capacity (PFC-Function.md), cortisol level     │
│  PFC-Function.md: PFC = ~5% operator, HOLD → bias activation    │
│  🟢 Evidence: CBT/ERP effective cho OCD (Schwartz 1996)          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

BÌNH THƯỜNG: Tuyến 1 fire → tuyến 2 accept → done. PFC không cần.
STRESS NHẸ: Tuyến 1 hơi yếu → tuyến 2 compensate → done. PFC không cần.
STRESS NẶNG: Tuyến 1+2 hơi yếu → PFC override → done. Hơi mệt nhưng ok.
```

---

## §3 — OCD = MULTI-POINT FAILURE

### §3.1 — Failure ở từng tuyến

```
OCD = FAILURE ở 1 hoặc NHIỀU tuyến cùng lúc:

TUYẾN 1 LỖI — "Done" detector dysfunctional:
  🟢 OFC-caudate HYPERACTIVE nhưng signal KHÔNG SẠCH
  → Circuit fire LIÊN TỤC (hyperactive) nhưng output = NOISE
  → Giống: đèn báo "done" nhấp nháy loạn → body không biết "xong chưa?"
  → ≠ Signal THIẾU → signal BẨN (noisy, unreliable)
  → = Hardware problem: wiring lỗi, không phải thiếu nỗ lực

TUYẾN 2 LỖI — Threshold quá CAO:
  → Serotonin thấp → certainty bias giảm (Status.md v2.1 §9.2)
  → = "Có CHẮC CHẮN xong chưa?" → KHÔNG TIN
  → Signal "done" có fire → nhưng KHÔNG VƯỢT threshold
  → = Giống: ai đó nói "xong rồi" nhưng bạn KHÔNG TIN

TUYẾN 3 LỖI — PFC override thất bại:
  → PFC HOLD "tôi BIẾT tay sạch" → gửi bias "DỪNG"
    (PFC-Function.md: PFC HOLD → bias spreading activation → body tự respond)
  → NHƯNG: chunks đang fire ở THREAT DIRECTION
    (Cortisol §7.7 Role ① Compile Direction: compiled AVOIDANCE)
  → Threat-direction chunks > PFC bias authority
  → PFC mệt (cortisol cao, thiếu ngủ) → override YẾU HƠN NỮA
  → = PFC chỉ là ~5% operator — 95% chunks fire vô thức
```

### §3.2 — Tại sao "BIẾT" nhưng không dừng

```
🟡 "BIẾT" VÀ "DỪNG" Ở 2 SYSTEMS KHÁC NHAU:

  "BIẾT" = PFC OBSERVE (A zone — Feeling.md v2.0):
    PFC observe body-chunk interaction → nhận ra "vô lý"
    = Tuyến 3, conscious, CHẬM

  "DỪNG" = chunks DEACTIVATE (C+D zones):
    Cần tuyến 1 (done detector) hoặc tuyến 2 (threshold accept)
    = Vô thức, automatic, NHANH

  → PFC nói "dừng" = PFC HOLD → bias spreading activation
  → NHƯNG: chunks fire ở threat direction = PRIORITY CAO
    (Threat.md: threat priority > PFC authority — evolutionary design)
  → PFC bias KHÔNG ĐỦ MẠNH override threat-compiled chunks
  → = "Cố dừng 1 lần → thành công → nhưng 5 phút sau loop QUAY LẠI"
    (PFC override = temporary HOLD, chunks fire LẠI khi PFC release)
  → = Ý chí KHÔNG PHẢI giải pháp — vì vấn đề ở TUYẾN 1+2 (C+D zones)
```

### §3.3 — Spectrum: nhẹ → nặng

```
┌──────────────┬──────────┬───────────┬───────────┬──────────────────┐
│              │ Tuyến 1  │ Tuyến 2   │ Tuyến 3   │ Biểu hiện        │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Bình thường  │ OK       │ OK        │ OK        │ Rửa tay → xong   │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Personality  │ Hơi yếu  │ OK        │ OK        │ "Hơi kỹ" nhưng   │
│ trait        │          │           │           │ dừng được         │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ OCD nhẹ      │ Yếu      │ Hơi cao   │ OK        │ Rituals nhưng     │
│              │          │           │           │ PFC override ĐƯỢC │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ OCD trung    │ Yếu      │ Cao       │ Mệt dần  │ Rituals TĂNG,     │
│ bình         │          │           │           │ PFC override khó  │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ OCD nặng     │ Lỗi      │ Rất cao   │ Fail      │ Compulsive, không │
│              │          │           │           │ dừng được, kiệt   │
├──────────────┼──────────┼───────────┼───────────┼──────────────────┤
│ Treatment    │ DBS      │ SSRIs     │ CBT/ERP   │ Mỗi treatment     │
│ resistant    │ (last    │ (không    │ (không    │ target 1 tuyến    │
│              │ resort)  │ đủ)       │ đủ)       │ → cần COMBO       │
└──────────────┴──────────┴───────────┴───────────┴──────────────────┘
```

### §3.4 — PANDAS/PANS: bằng chứng nhân quả cho tuyến 1

```
⭐ PANDAS/PANS = VALIDATION CỰC MẠNH CHO MÔ HÌNH 3 TUYẾN

PANDAS (Pediatric Autoimmune Neuropsychiatric Disorders
        Associated with Streptococcal infections):

  MECHANISM:
    ① Trẻ bị nhiễm streptococcus (viêm họng liên cầu khuẩn)
    ② Hệ miễn dịch tạo kháng thể chống strep
    ③ Kháng thể NHẦM tấn công basal ganglia (bao gồm CAUDATE NUCLEUS)
    ④ Caudate bị viêm → "done" detector (OFC-caudate) BỊ PHÁ
    ⑤ OCD XUẤT HIỆN ĐỘT NGỘT — trong NGÀY, không phải tháng

  🟢 Evidence: Swedo et al. (1998), NIMH; multiple replications
  🟢 PANS = phiên bản mở rộng (không chỉ strep)

  TIMELINE:
    Tuần 0: trẻ BÌNH THƯỜNG hoàn toàn
    Tuần 1: nhiễm strep → sốt, viêm họng
    Tuần 2-4: kháng thể tấn công caudate
    Tuần 3-6: OCD XUẤT HIỆN ĐỘT NGỘT + tics + anxiety BÙNG NỔ

  TREATMENT:
    → Kháng sinh (diệt strep) → kháng thể GIẢM → caudate phục hồi
    → OCD GIẢM hoặc BIẾN MẤT khi hết viêm
    → Nặng: IVIG hoặc plasmapheresis (lọc kháng thể)

  QUA FRAMEWORK — TẠI SAO QUAN TRỌNG:
    → Phá tuyến 1 → OCD → sửa tuyến 1 → OCD giảm
    → = BẰNG CHỨNG NHÂN QUẢ (không chỉ correlation)
    → = "Natural experiment" — phá 1 tuyến → xem kết quả
    → = Validation MẠNH NHẤT cho mô hình 3 tuyến
```

---

## §4 — V7.8 MAPPING: CHUNK DYNAMICS + SPREADING ACTIVATION

> **Section MỚI v2.0**: Map OCD vào v7.8 chunk-centric architecture.

### §4.1 — OCD qua chunk dynamics (BFM)

```
🟡 OCD MAP VÀO BODY-FEEDBACK-MECHANISM.MD:

  OCD OBSESSION = PATTERN-DRIVEN trigger (BFM §2.3):
    → Chunks fire NỘI BỘ (không cần external stimulus thật)
    → "Tay bẩn" = chunks fire MÀ KHÔNG CẦN thực sự chạm bẩn
    → = Pattern-Driven ⓐ REPLAY + ⓔ SPREADING ACTIVATION
    → Khác với sensory-driven: không có stimulus MỚI → chỉ internal loop

  OCD COMPULSION = attempt tạo SENSORY-DRIVEN confirmation:
    → Rửa tay = tạo sensory input "sạch" (nước, xà phòng, trơn)
    → Mục đích: sensory input → "done" detector → DỪNG
    → NHƯNG tuyến 1 noisy → sensory confirmation KHÔNG accepted
    → = Compulsion = ĐÚNG strategy (tạo confirmation)
      nhưng FAIL vì hardware (done detector lỗi)


  OCD = CHUNK-MISS KHÔNG BAO GIỜ RESOLVE:

    ┌────────────────────────────────────────────────────────────┐
    │                                                            │
    │  BÌNH THƯỜNG:                                               │
    │    Body compiled baseline "tay SẠCH" → tay bẩn →            │
    │    Chunk-Miss (actual < baseline) → rửa →                   │
    │    done detector: MATCH → Chunk-Miss RESOLVE → opioid nhẹ  │
    │                                                            │
    │  OCD:                                                       │
    │    Body compiled baseline "tay SẠCH" → tay bẩn →            │
    │    Chunk-Miss (actual < baseline) → rửa →                   │
    │    done detector: NOISY → Chunk-Miss KHÔNG RESOLVE →        │
    │    VTA vẫn fire negative delta → rửa LẠI → LOOP            │
    │                                                            │
    │  = Cùng mechanism. Khác: done detector output quality.     │
    └────────────────────────────────────────────────────────────┘

    BFM §5 Quality Baseline Shift cũng áp dụng:
    → Mỗi lần rửa thêm = baseline "sạch" TĂNG thêm
    → = Threshold "đủ sạch" DẦN CAO HƠN qua mỗi compulsion
    → = OCD ESCALATE theo thời gian vì baseline SHIFT LÊN
    → = Crespi SNC 🟢: body compile baseline MỚI → cái cũ "không đủ"
```

### §4.2 — Spreading activation loop

```
🟡 OCD OBSESSIVE THINKING = UNINHIBITED SPREADING ACTIVATION:

  (Chunk-Activation-Dynamics.md §2)

  BÌNH THƯỜNG:
    Chunk X fire → spreading activation → liên quan A, B, C fire nhẹ
    → Serotonin = INHIBITOR: spreading activation bị GIỚI HẠN
    → Chỉ chunks STRONG links fire → phần còn lại KHÔNG fire
    → = "Nghĩ tới X → liên tưởng A → dừng"

  OCD (serotonin ↓):
    Chunk X fire → spreading activation → LESS INHIBITED
    → A, B, C, D, E... fire → cascade RỘNG hơn bình thường
    → Mỗi chunk fire → trigger thêm spreading → LOOP
    → = "Nghĩ tới vi khuẩn → tay → cửa → bàn → mọi thứ → KHÔNG DỪNG"

  ⭐ CÙNG CƠ CHẾ VỚI LIMERENCE (Love-Analysis.md v2.1 §2.1):

    ┌──────────────────┬──────────────────────┬──────────────────────┐
    │                  │ LIMERENCE            │ OCD                   │
    ├──────────────────┼──────────────────────┼──────────────────────┤
    │ Serotonin        │ ↓ ~40%               │ ↓ (tương đương)       │
    │ Spreading activ. │ UNINHIBITED          │ UNINHIBITED           │
    │ Target           │ Partner chunks       │ Threat chunks         │
    │ Cascade          │ "Nghĩ tới em 24/7"  │ "Nghĩ tới vi khuẩn   │
    │                  │                      │  24/7"                │
    │ Exit condition   │ CÓ (bond compile)    │ KHÔNG (target ≠ bond) │
    │ Self-resolves?   │ CÓ (12-18 tháng)    │ KHÔNG (cần treatment) │
    │ Cortisol role    │ ① Compile APPROACH   │ ③ Threat-sustained    │
    │ PFC đồng ý?     │ CÓ (ego-syntonic)    │ KHÔNG (ego-dystonic)  │
    └──────────────────┴──────────────────────┴──────────────────────┘

    = CÙNG mechanism (uninhibited spreading activation)
    = CÙNG neurochemistry (serotonin ↓)
    = KHÁC target (partner vs threat) → KHÁC outcome
    = KHÁC direction (approach vs avoidance)
```

### §4.3 — Cortisol 5 Roles trong OCD

```
🟡 CORTISOL-BASELINE.MD §7.7 — 5 ROLES APPLIED TO OCD:

  ┌─────────────────┬──────────────────────────────────────────────┐
  │ Cortisol Role    │ Trong OCD                                    │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ① Compile       │ Chunks "vi khuẩn nguy hiểm" compiled ở      │
  │   Direction     │ AVOIDANCE direction → threat-tagged →        │
  │                 │ fire priority CAO → PFC khó override         │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ② Holding       │ "Chưa kiểm tra cửa" = gap chưa close →     │
  │                 │ mild cortisol holding → PFC buộc quay lại    │
  │                 │ check → "đã xong chưa?" → CHƯA (tuyến 1 lỗi)│
  │                 │ → holding KHÔNG resolve → ESCALATE thành ③  │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ③ Threat-       │ OCD anxiety = cortisol sustained vì threat   │
  │   sustained     │ CHƯA HẾT (body: "vi khuẩn VẪN CÓ THỂ").   │
  │                 │ CÓ yếu tố SỢ → self-amplifying loop.       │
  │                 │ = CHÍNH role SUSTAIN OCD suffering thành     │
│                 │   chronic (amplifier, not root cause).       │
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ④ Inertia       │ Sau compulsion: cortisol CHƯA về baseline    │
  │                 │ dù vừa rửa xong. Body vẫn "chênh vênh"     │
  │                 │ → NHẦM thành "chưa sạch" → trigger lại loop│
  ├─────────────────┼──────────────────────────────────────────────┤
  │ ⑤ Silent        │ OCD chronic → cortisol CAO LIÊN TỤC nhưng   │
  │                 │ self-signal atrophy → PFC KHÔNG biết stress  │
  │                 │ → damage tích lũy không awareness            │
  │                 │ → PFC dendrite atrophy (Cortisol §9) →      │
  │                 │ tuyến 3 SUY YẾU THÊM → OCD NẶNG THÊM      │
  └─────────────────┴──────────────────────────────────────────────┘

  ⭐ ESCALATION PATH:
    ② Holding ("chưa xong") → ③ Threat-sustained ("SỢ")
    → ⑤ Silent (chronic, atrophy) → tuyến 3 WEAKER → OCD WORSE
    → = Vicious cycle: OCD → cortisol → PFC damage → OCD tăng
```

### §4.4 — PFC override failure qua PFC-Function.md

```
🟡 TUYẾN 3 MAP VÀO PFC-FUNCTION.MD:

  PFC 24 functions × 5 categories. Tuyến 3 OCD override dùng:

  HOLD: PFC hold "tôi biết tay sạch" = giữ chunk "sạch" active
  PROCESS: PFC evaluate evidence "tay trơn, sạch, không mùi"
  ORCHESTRATE: PFC bias spreading activation → "DỪNG rửa"

  TẠI SAO FAIL:
    → PFC = ~5% operator (PFC-Function.md)
    → 95% = chunks fire vô thức ở C+D zones
    → OCD chunks compiled ở THREAT DIRECTION (Role ①)
    → Threat-direction = PRIORITY CAO (evolutionary: threat > logic)
    → PFC 5% bias KHÔNG override 95% threat-priority chunks
    → PFC consume energy CỰC LỚN → Cortisol §6: glucose depletion
    → Override ngắn hạn OK → long-term = PFC kiệt → loop quay lại

  = Tại sao CBT/ERP cần NHIỀU sessions:
    → Mỗi session: PFC hold + body sit with anxiety + NOT compulse
    → Body TỰ HỌC: "anxiety TỰ GIẢM dù không check"
    → = RE-COMPILE chunks: "không check → VẪN OK" (new chunk)
    → Chunks mới compile COMPETITIVE với chunks cũ
      (Chunk-Activation-Dynamics.md §3: competitive re-linking)
    → Nhiều sessions = chunks mới DẦN MẠNH HƠN chunks cũ
    → = CBT không "xóa" OCD chunks → BUILD chunks mới competitive
```

### §4.5 — SEROTONIN ↓ = AMPLIFIER, NOT ROOT CAUSE

```
⭐ CÂU HỎI CỐT LÕI: Serotonin ↓ là CAUSE hay CONSEQUENCE?

  MAINSTREAM ĐƠN GIẢN: serotonin ↓ → OCD/limerence
    = 1 chiều. Serotonin = root cause.

  FRAMEWORK: serotonin ↓ = CONSEQUENCE of uncertainty + AMPLIFIER of loop
    = Feedback loop. Serotonin = amplifier, giống cortisol.


  ⭐ MÔ HÌNH FEEDBACK LOOP:

    [INITIAL TRIGGER] ← KHÁC NHAU tùy context
         ↓
    [UNCERTAINTY STATE] — body ở trạng thái "CHƯA CHẮC"
         ↓
    [SEROTONIN ↓] — certainty bias GIẢM (= CONSEQUENCE)
         ↓
    [SPREADING ACTIVATION UNINHIBITED] — cascade chunks
         ↓
    [OBSESSIVE THINKING] — monitor target liên tục
         ↓
    [VẪN CHƯA RESOLVE] — done detector fail HOẶC bond chưa compile
         ↓
    [UNCERTAINTY TIẾP TỤC] → quay lại ↑ → LOOP
         ↓
    [SEROTONIN CÒN THẤP HƠN] → amplify thêm → VICIOUS CYCLE


  INITIAL TRIGGERS KHÁC NHAU:

    OCD childhood onset:
      → Tuyến 1 hardware LỖI BẨM SINH → done signal NOISY
      → Body CHRONIC uncertainty ("chưa xong?")
      → Serotonin ↓ = CONSEQUENCE of hardware failure
      → → amplify loop thêm

    OCD adult onset:
      → Stress chronic → cortisol ↑ → serotonin ↓ (environment pathway)
      → NHƯNG root cause = STRESS, không phải serotonin tự giảm

    Love (limerence):
      → SPM library incomplete (mới gặp) → prediction-deltas CAO
      → Body GENUINE uncertainty about partner
      → Serotonin ↓ = ADAPTIVE RESPONSE (monitor cần thiết)
      → + Obligation unknown ("tôi phải trả GÌ để giữ?")
      → + Có thể childhood SPM bias (§4.5b)
      → = Serotonin ↓ = CONSEQUENCE of real uncertainty


  PARALLEL VỚI CORTISOL (Cortisol-Baseline.md):

    Cortisol = "amplifier, NOT cause.
    Đau đến từ 3 nguồn KHÁC. Cortisol chỉ đồng hành."

    Serotonin = "amplifier of uncertainty loop.
    Uncertainty đến từ nguồn KHÁC. Serotonin khuếch đại."

    CẢ HAI là FEEDBACK AMPLIFIERS, không phải ROOT CAUSES.


  🟢 EVIDENCE ỦNG HỘ "AMPLIFIER" MODEL:

    ① PANDAS: sửa tuyến 1 (caudate) → OCD HẾT
       → NẾU serotonin = root cause → sửa caudate KHÔNG nên fix
       → NẾU serotonin = consequence → sửa ROOT → uncertainty hết
         → serotonin TỰ PHỤC HỒI → OCD hết ✓

    ② SSRIs → bỏ → relapse ~80%:
       → NẾU serotonin = root cause đã fix → bỏ KHÔNG nên relapse
       → NẾU serotonin = amplifier → bỏ amplifier fix → root cause
         VẪN CÒN → loop quay lại ✓

    ③ CBT → bỏ → relapse chỉ ~20-30%:
       → CBT sửa CHUNKS (root level, C+D zones)
       → Root changed → loop KHÔNG quay lại (dù serotonin fluctuate)
       → = Root-level fix > amplifier-level fix ✓

    ④ Love tự resolve 12-18 tháng:
       → Bond compile → uncertainty ↓ → serotonin TỰ PHỤC HỒI
       → Serotonin phục hồi vì ROOT CAUSE resolved (not because meds)
       → = Serotonin follows uncertainty state ✓


  🟡 FRAMEWORK CLAIM:
    Serotonin ↓ = CONSEQUENCE + AMPLIFIER, NOT ROOT CAUSE
    Giống cortisol: participates, amplifies, but doesn't initiate
    Root cause = tuyến 1 hardware / stress / genuine uncertainty
```

### §4.5b — SPM bias từ tuổi thơ × OCD-like trong Love

```
🟡 TẠI SAO MỘT SỐ NGƯỜI "YÊU" INTENSE HƠN → OCD-LIKE HƠN:

  SPM LIBRARY BUILD TỪ CAREGIVER (Connection §3.2, §7):
    → Bé học SPM TRƯỚC TIÊN trên bố mẹ
    → Bố mẹ strict / unpredictable:
      → SPM library build DEEP nhưng THREAT-BIASED
        (Cortisol Role ① Compile Direction: AVOIDANCE)
      → Chunks = "close agent → phải CANH CHỪNG"

  ADULT → MEET PARTNER → SPM FIRE CÙNG LIBRARY:
    → SPM retrieve: "close agent → monitor liên tục"
    → "Partner buồn → TÔI CÓ LÀM GÌ SAI KHÔNG?"
      (thay vì: "partner buồn vì lý do riêng")
    → = HYPER-MONITORING — không phải vì partner xấu
      mà vì SPM library compiled TỪ MÔI TRƯỜNG PHẢI monitor

  HYPER-MONITORING → COMPOUND UNCERTAINTY:
    → Mỗi expression partner → SPM fire → interpret qua THREAT lens
    → "Họ yên lặng" → "giận? chán? sắp bỏ?" (predict sai thường xuyên)
    → Prediction-deltas NHIỀU HƠN → uncertainty CAO HƠN
    → + Obligation overthinking: "xứng đáng không? giữ sao? trả GÌ?"
      (Obligation.md: obligation = compiled prediction "cost phải trả"
       → relationship mới = obligation CHƯA COMPILE → Chunk-Gap)
    → = 2 nguồn uncertainty COMPOUND:
      ① SPM: "họ thật sự cảm thấy gì?"
      ② Obligation: "tôi phải trả GÌ để giữ?"
    → → Serotonin ↓ MẠNH HƠN → limerence INTENSE hơn + KÉO DÀI hơn

  MAP VÀO ATTACHMENT THEORY (🟢 Bowlby 1969):
    → "Anxious attachment" = SPM library compiled THREAT-BIASED
    → Adult: monitoring OVER-ACTIVE → uncertainty CHRONIC
    → Serotonin ↓ CHRONIC → limerence = OCD-like STATE
    → = Framework giải thích MECHANISM đằng sau anxious attachment label

  ⚠️ KHÔNG CHỈ CHILDHOOD — PARTNER CÓ THỂ LÀ NGUỒN:
    → Partner genuinely unpredictable → SPM errors CAO vì PARTNER
    → = SAME mechanism, DIFFERENT source
    → = Childhood bias + partner unpredictable = COMPOUND → worst case
```

### §4.6 — Cross-species evidence: OCD = bug circuit CỔ

```
⭐ OCD-LIKE BEHAVIORS Ở NHIỀU LOÀI → CIRCUIT CỔ:

  🟢 KHỈ RHESUS CAPTIVE (Novak et al. 2006):
    → Repetitive behaviors (rocking, pacing, self-harm)
    → Đặc biệt ở khỉ bị tách mẹ sớm (social deprivation)
    → Serotonergic involvement (Lutz, Well & Novak research program —
      fluoxetine giảm SIB, lower CSF serotonin trong SIB macaques)
    → Basal ganglia circuits compromised (Mason & Latham 2004)
    → = CÙNG vùng với OCD người (OFC-caudate)

  🟢 DEER MICE (Korff, Stein & Harvey 2008):
    → Tự phát triển compulsive jumping/somersaulting
    → Respond to fluoxetine (SSRI) ✓ — nhưng KHÔNG respond desipramine
      (= CHỈ serotonin path, giống OCD người)
    → Frontal cortex involvement (Korff et al. 2008-2009 research program)
    → = Ở loài KHÔNG CÓ PFC phức tạp

  🟢 SAPAP3 KNOCKOUT MICE (Welch et al. 2007, Nature):
    → Grooming compulsive đến rụng lông (facial lesions)
    → Respond to fluoxetine ✓
    → Cortico-striatal synaptic defects demonstrated
    → = Genetic manipulation → OCD-like → support hardware cause
    → = Landmark paper — strongest genetic model

  🟢 HOXB8 MUTANT MICE (Greer & Capecchi 2002, Neuron;
    bone marrow rescue: Chen et al. 2010, Cell):
    → Excessive grooming → sửa bằng bone marrow transplant
    → Mechanism: microglia replacement → neuroimmune
    → = GỢI NHỚ PANDAS mechanism (autoimmune → basal ganglia)!

  🟢 CHÓ — Canine Compulsive Disorder:
    → Tail-chasing, flank-sucking, shadow-chasing
    → Respond to fluoxetine (🟢 Irimajiri et al. 2009: RCT, 8.7× improvement)
    → CDH2 gene chromosome 7 (Dodman et al. 2010, Molecular Psychiatry)
    → Bull Terrier compulsive tail chasing (Moon-Fanelli et al. 2011)
    → = Genetic component confirmed ở loài khác


  ⭐ HỆ QUẢ CHO FRAMEWORK:

    ┌───────────────────────────────────────────────────────────────┐
    │                                                               │
    │  NẾU OCD CHỈ Ở NGƯỜI → bug riêng PFC phức tạp               │
    │  NẾU OCD Ở NHIỀU LOÀI → bug của CIRCUIT CỔ hơn PFC          │
    │                                                               │
    │  Evidence: chuột + chó + khỉ → CIRCUIT = BASAL GANGLIA       │
    │  (OFC-caudate = tuyến 1) — circuit CỔ, CROSS-SPECIES         │
    │                                                               │
    │  → SUPPORT mạnh cho 3-tuyến model:                            │
    │    Tuyến 1 (OFC-caudate) = HARDWARE CỔ, cross-species        │
    │      → Chuột CÓ tuyến 1 → chuột CÓ THỂ OCD-like            │
    │    Tuyến 2 (serotonin) = HARDWARE CỔ, cross-species          │
    │      → SSRIs giúp chuột + chó + người → CÙNG mechanism       │
    │    Tuyến 3 (PFC override) = CHỈ MẠNH Ở NGƯỜI                 │
    │      → Người CÓ tuyến 3 → CBT possible                       │
    │      → Chuột/chó KHÔNG CÓ tuyến 3 → CHỈ SSRIs/DBS           │
    │                                                               │
    │  → OCD = BUG CỦA CIRCUIT CỔ (tuyến 1+2)                     │
    │    PFC (tuyến 3) = GIẢI PHÁP BỔ SUNG CHỈ NGƯỜI CÓ           │
    └───────────────────────────────────────────────────────────────┘


  ⭐ LIÊN KẾT VỚI "SEROTONIN = AMPLIFIER" (§4.5):

    Deer mice: KHÔNG CÓ PFC phức tạp, KHÔNG "overthinking"
      → VẪN OCD-like + serotonin thay đổi ở OFC
      → = Ở chuột: serotonin ↓ gần HARDWARE CAUSE (gen, wiring)

    Khỉ captive: social deprivation → compulsive
      → = Ở khỉ: ENVIRONMENT trigger → serotonin ↓ = CONSEQUENCE

    Người: CẢ HAI + THÊM PFC complexity
      → Hardware (gen) → tuyến 1 lỗi → uncertainty → serotonin ↓
      → Environment (stress/childhood SPM bias) → uncertainty → serotonin ↓
      → Obligation overthinking → uncertainty → serotonin ↓
      → = Người có NHIỀU ĐƯỜNG DẪN đến serotonin ↓ hơn chuột/chó

    → Serotonin role = SPECTRUM tùy species complexity:
      Chuột: serotonin gần HARDWARE CAUSE (ít nguồn uncertainty)
      Khỉ: serotonin = MIX cause + consequence (có social component)
      Người: serotonin gần CONSEQUENCE + AMPLIFIER (NHIỀU nguồn uncertainty)
```

### §4.7 — Basal ganglia × Parkinson: architectural bridge

```
⭐ OCD × PARKINSON: CÙNG BASAL GANGLIA, KHÁC FAILURE MODE

  (Cross-ref: Parkinson-Analysis.md v1.1 §2)

  PARKINSON:
    → Basal ganglia = GATE (default ĐÓNG, dopamine = CHÌA KHÓA)
    → SNc neurons CHẾT → dopamine MẤT → gate BỊ KHÓA
    → Motor command TỪ PFC CÒN → signal KHÔNG ĐI QUA ĐƯỢC
    → = BIẾT phải làm gì nhưng KHÔNG LÀM ĐƯỢC

  OCD:
    → OFC-caudate circuit = DONE DETECTOR (basal ganglia component)
    → Done detector output = NOISY (signal bẩn, không sạch)
    → "Done" signal fire → nhưng unreliable → body KHÔNG TIN
    → = ĐÃ LÀM XONG nhưng KHÔNG DỪNG ĐƯỢC

  ┌────────────────┬──────────────────────┬──────────────────────┐
  │                │ PARKINSON            │ OCD                   │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ Failure mode   │ Gate LOCKED          │ Gate signal NOISY    │
  │                │ (key destroyed)      │ (detector unreliable) │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ Circuit        │ SNc → Striatum       │ OFC → Caudate        │
  │                │ (nigrostriatal)      │ (orbitofrontal)      │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ Kết quả        │ CAN'T START/EXECUTE  │ CAN'T STOP           │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ DBS target     │ STN (subthalamic)    │ VC/VS (ventral       │
  │                │                      │ capsule/striatum)    │
  ├────────────────┼──────────────────────┼──────────────────────┤
  │ DBS mechanism  │ JAM pathological     │ MODULATE done-signal │
  │                │ beta oscillations    │ processing           │
  └────────────────┴──────────────────────┴──────────────────────┘

  ⭐ HỆ QUẢ CHO "CIRCUIT CỔ" ARGUMENT (§4.6):
    → CẢ HAI = basal ganglia failure
    → Basal ganglia = GATE cho NHIỀU chức năng (motor + completion + reward)
    → CÙNG architectural principle, KHÁC failure output:
      Parkinson: motor gate locked → CAN'T EXECUTE
      OCD: completion gate noisy → CAN'T STOP
    → DBS cho CẢ HAI: cùng nguyên lý bypass (electrical override)
      nhưng KHÁC target (vì khác sub-circuit)
    → = Basal ganglia = infrastructure CỔ, nhiều failure modes possible
```

---

## §5 — LOVE ↔ OCD: CÙNG CIRCUIT, KHÁC MỤC ĐÍCH

> 🟢 Marazziti et al. (1999): Người đang yêu say đắm có
> serotonin transporter GIẢM ~40% — BẰNG MỨC người OCD.

### §5.1 — Cùng triệu chứng, khác label

```
NGƯỜI ĐANG YÊU (limerence, 0-18 tháng):
  → Nghĩ tới partner LIÊN TỤC (intrusive thoughts ✓)
  → Không dừng được dù MUỐN tập trung (compulsive ✓)
  → Kiểm tra điện thoại liên tục (checking ✓)
  → Phân tích mọi tin nhắn, cử chỉ (rumination ✓)
  → Serotonin giảm ~40% (🟢 Marazziti 1999)
  → Spreading activation uninhibited → cascade partner chunks

NGƯỜI OCD (contamination type):
  → Nghĩ tới vi khuẩn LIÊN TỤC (intrusive thoughts ✓)
  → Không dừng được dù BIẾT vô lý (compulsive ✓)
  → Kiểm tra tay liên tục (checking ✓)
  → Phân tích mọi bề mặt đã chạm (rumination ✓)
  → Serotonin thấp (🟢 established)
  → Spreading activation uninhibited → cascade threat chunks

→ = CÙNG mechanism. CÙNG neurochemistry. CÙNG behavior pattern.
→ Bỏ label → triệu chứng GIỐNG NHAU.
```

### §5.2 — Tại sao cùng circuit (evolutionary logic)

```
🟡 EVOLUTION ĐÃ BUILD 1 CIRCUIT:

  "Khi gặp thứ QUAN TRỌNG + CHƯA CHẮC CHẮN
   → giảm serotonin → giảm certainty bias
   → OBSESS → monitor liên tục
   → cho tới khi ĐỦ CHẮC CHẮN → serotonin phục hồi → dừng"

  Circuit ĐÚNG THIẾT KẾ khi:
    → Target = potential mate (QUAN TRỌNG + CHƯA CHẮC)
    → Serotonin ↓ → obsess → monitor mọi signal
    → Bond compile → "đủ biết" → serotonin phục hồi → obsession giảm
    → = "Yêu" = circuit obsessive-monitoring HOẠT ĐỘNG ĐÚNG MỤC ĐÍCH

  Circuit LỖI khi:
    → Target = thứ KHÔNG CẦN monitoring (tay sạch, cửa khóa, số chẵn)
    → Serotonin ↓ → obsess → NHƯNG target KHÔNG BAO GIỜ "đủ chắc"
    → "Tay sạch" KHÔNG THỂ confirm bằng bond (khác "người này đáng yêu")
    → = Circuit chạy ĐÚNG CÁCH nhưng NHẦM TARGET

  TƯƠNG TỰ Y HỌC:
    Sốt = FEATURE (chống nhiễm trùng) → sốt mãn tính = BUG (autoimmune)
    Obsession yêu = FEATURE (monitor mate) → obsession OCD = BUG (monitor sai target)
```

### §5.3 — 3 khác biệt quan trọng

```
┌─────────────────┬───────────────────────┬───────────────────────┐
│                 │ YÊU (limerence)       │ OCD                   │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Target          │ Partner — CÓ GIÁ TRỊ │ Thứ không cần monitor │
│                 │ bond, exit condition  │ (vi khuẩn, ổ khóa)   │
├─────────────────┼───────────────────────┼───────────────────────┤
│ PFC đồng ý?    │ CÓ — ego-syntonic     │ KHÔNG — ego-dystonic  │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Tự dừng?       │ CÓ — bond compile →   │ KHÔNG — cần treatment │
│                 │ done detector: DONE   │ done detector: LỖI    │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Reward          │ CÓ — opioid, oxytocin│ KHÔNG — chỉ giảm      │
│                 │ (body-need met THẬT)  │ anxiety TẠM            │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Cortisol role   │ ① APPROACH compile   │ ③ Threat-sustained    │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Body-Base Ext   │ Partner → extension   │ KHÔNG (target = object)│
│ (VP §2)        │ (L2 structural)       │                       │
├─────────────────┼───────────────────────┼───────────────────────┤
│ Adaptive?       │ CÓ — monitor mate    │ KHÔNG — waste energy   │
└─────────────────┴───────────────────────┴───────────────────────┘
```

### §5.4 — Timeline: yêu DỪNG thế nào (mà OCD không dừng)

```
YÊU — Timeline serotonin:

  Tháng 1-3: LIMERENCE
    → Serotonin ↓40% → spreading activation uninhibited → obsess CỰC MẠNH
    → "Done" detector: ĐANG check → chưa done (bond chưa compile)
    → = ĐÚNG — bond mới CẦN monitoring

  Tháng 3-12: BONDING
    → Gặp nhiều → SPM library build (Love §3.2) → uncertainty GIẢM
    → Chunks về partner compile DẦN → C+D zones "biết" dần
    → Serotonin PHỤC HỒI DẦN → spreading activation BỊ INHIBIT lại
    → = Bond đang compile → done detector dần nhận "đủ biết"

  Tháng 12-18: ATTACHMENT
    → Chunks về partner ĐÃ compile (SPM library DEEP)
    → Serotonin BÌNH THƯỜNG → certainty cao → hết obsess
    → L2 body-base extension compiled → structural reward thay thế L1
    → = "Tình yêu ban đầu phai" = OBSESSION hết, ATTACHMENT còn
    → = Circuit TỰ TẮT khi mục đích hoàn thành (bond compiled)

OCD — KHÔNG có timeline tương tự:
  → Target (vi khuẩn, ổ khóa) KHÔNG compile thành "bond"
  → "Done" detector KHÔNG BAO GIỜ nhận "đủ"
  → Serotonin KHÔNG TỰ phục hồi
  → = Loop VÔ HẠN — cần external intervention
```

### §5.5 — Khi yêu KHÔNG dừng: limerence kéo dài

```
🟡 LIMERENCE KÉO DÀI = "YÊU" STUCK TRONG OCD-LIKE STATE:

  Limerence kéo dài quá 18 tháng → bond KHÔNG compile:
    → Relationship bất ổn, unrequited, on-off
    → "Done" detector: KHÔNG BAO GIỜ nhận "done" (bond chưa ổn)
    → Serotonin VẪN THẤP → spreading activation VẪN uninhibited
    → = OCD-like state với target = NGƯỜI

  Hậu quả:
    → Stalking = compulsive checking (OCD checking pattern)
    → Jealousy extreme = uncertainty monitoring overload
    → "Không thể buông" = done detector CHƯA fire (bond chưa compile + chưa fail)
    → = CÙNG mechanism OCD, target = NGƯỜI thay vì VẬT

  Qua v7.8:
    → Limerence kéo dài = L2 body-base extension ĐANG compile
      nhưng relationship bất ổn → compile KHÔNG hoàn thành
    → Cortisol Role ② Holding → escalate ③ Threat-sustained
    → = Nếu relationship ổn → bond compile → done → dừng
    → = Nếu relationship MÃI bất ổn → chronic → giống OCD
```

---

## §6 — SEROTONIN = "CERTAINTY BIAS"

```
⭐ FRAMEWORK: SEROTONIN = CERTAINTY BIAS (Status.md v2.1 §9.2)

  POP SCIENCE:     "Serotonin = hạnh phúc. Thiếu = buồn."
  FRAMEWORK:       Serotonin = certainty/stability. Thiếu = uncertainty/checking.

  NẾU "hạnh phúc":
    → Người yêu (serotonin ↓) = BUỒN? ← SAI. Cực kỳ intense.
    → Người OCD (serotonin ↓) = BUỒN? ← Không hẳn. ANXIOUS.
    → SSRIs chữa OCD vì "vui hơn"? ← SAI. Vì BỚT CHECK.

  NẾU "certainty bias":
    → Người yêu (serotonin ↓) = KHÔNG CHẮC về partner → obsess ← ĐÚNG
    → Người OCD (serotonin ↓) = KHÔNG CHẮC "done" → check lại ← ĐÚNG
    → SSRIs = tăng certainty → dễ accept "done" → giảm checking ← ĐÚNG
    → Tryptophan depletion = giảm certainty → indecision ← ĐÚNG

  → "Certainty bias" giải thích NHIỀU HƠN "hạnh phúc"
  → Status.md v2.1 §9.2: serotonin = Ratchet (dễ lên, khó xuống)
    → OCD = ratchet STUCK ở mức thấp → certainty CỰC THẤP → check mãi


  SEROTONIN TRONG 3 TUYẾN:

    Tuyến 1 — "Done" detector:
      → Serotonin KHÔNG sửa hardware wiring
      → = Tại sao SSRIs GIÚP nhưng KHÔNG CHỮA DỨT OCD

    Tuyến 2 — Satisfaction threshold:
      → Serotonin TRỰC TIẾP ảnh hưởng:
        Serotonin cao → threshold THẤP → "done" yếu VẪN ACCEPT
        Serotonin thấp → threshold CAO → "done" phải CỰC MẠNH
      → = SSRIs target ĐÚNG tuyến này

    Tuyến 3 — PFC override:
      → Serotonin gián tiếp: mood ổn → PFC bớt cortisol → override mạnh hơn


  🟢 VALIDATION MẠNH:
    → OCD cần SSRI liều 3-4× depression (fluoxetine 60-80mg vs 20mg)
    → = OCD threshold CAO hơn → cần NHIỀU serotonin → "certainty bias" model
    → Noradrenergic antidepressants (desipramine) → KHÔNG effective cho OCD
    → = CHỈ serotonin path hoạt động → certainty bias, KHÔNG phải general mood
```

---

## §7 — SPECTRUM: KHÔNG CHỈ OCD

```
🟡 CÙNG CIRCUIT, KHÁC TARGET:

  ┌──────────────────┬───────────────────────┬────────────┬──────────┐
  │ Hiện tượng       │ Target monitoring     │ Adaptive?  │ Tự dừng? │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Yêu (limerence)  │ Potential mate        │ CÓ         │ CÓ       │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Limerence kéo dài│ Người yêu bất ổn     │ Partially  │ KHÓ      │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Health anxiety    │ Body symptoms        │ KHÔNG      │ KHÔNG    │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ OCD contamination│ Vi khuẩn, bẩn        │ KHÔNG      │ KHÔNG    │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ OCD checking     │ Ổ khóa, bếp, cửa    │ KHÔNG      │ KHÔNG    │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ Jealousy extreme │ Partner + rivals      │ Partially  │ TÙY      │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ BDD              │ Khuyết điểm ngoại    │ KHÔNG      │ KHÔNG    │
  │ 🟢 DSM-5: OCD   │ hình (phóng đại)     │            │          │
  │ spectrum         │                       │            │          │
  ├──────────────────┼───────────────────────┼────────────┼──────────┤
  │ PTSD intrusions  │ Traumatic event       │ Partially  │ KHÓ      │
  └──────────────────┴───────────────────────┴────────────┴──────────┘

  PATTERN CHUNG:
    → Serotonin ↓ → certainty ↓ → spreading activation uninhibited → obsessive monitor
    → Target CÓ exit condition + TỰ resolve → TỰ DỪNG (yêu)
    → Target KHÔNG exit condition → KHÔNG DỪNG (OCD, anxiety)
    → = Bệnh lý = circuit ĐÚNG chạy trên target SAI hoặc không có exit
```

### §7.1 — PTSD intrusions vs OCD obsessions: cùng "suy nghĩ xâm nhập", khác cơ chế

```
⭐ PTSD VÀ OCD ĐỀU CÓ "INTRUSIVE THOUGHTS" — NHƯNG CƠ CHẾ KHÁC HOÀN TOÀN:

  (Cross-ref: PTSD-Analysis.md v1.0 §2, §4, §14)

  PTSD INTRUSION:
    → Trauma chunk encoded VIA AMYGDALA (bypassed hippocampus)
    → Chunk có BODY STATE nhưng THIẾU 3 metadata: temporal, spatial, causal
    → Trigger (sensory match) → context-free chunk fire → body "SỐNG LẠI" trauma
    → Body-first temporal: amygdala 12ms → body 50ms → PFC 200ms+
    → PFC arrives LATE — body ĐÃ đáp ứng trước khi PFC kịp "biết"
    → = CONTEXT-FREE chunk fire sai context

  OCD OBSESSION:
    → Chunk compiled BÌNH THƯỜNG (CÓ context metadata đầy đủ 4/4)
    → "Done" detector output NOISY → completion signal unreliable
    → Chunk-Miss KHÔNG resolve → hành vi lặp lại
    → PFC biết "xong" nhưng body KHÔNG TIN done signal
    → = CONTEXT-INTACT chunk, "DONE" SIGNAL fail

  ┌────────────────┬──────────────────────────┬────────────────────────┐
  │                │ PTSD INTRUSION           │ OCD OBSESSION          │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Chunk type     │ Context-FREE (amygdala)  │ Context-INTACT (normal)│
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Metadata       │ THIẾU 3/4 (chỉ state)   │ ĐẦY ĐỦ 4/4            │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Failure point  │ ENCODING bị phá          │ COMPLETION detector    │
  │                │ (hippocampus suppressed)  │ bị noisy (OFC-caudate) │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Body response  │ FULL threat RE-EXPERIENCE│ UNCERTAINTY "chưa xong"│
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ PFC experience │ "Đây là memory" (late)   │ "Tôi BIẾT xong" (late) │
  ├────────────────┼──────────────────────────┼────────────────────────┤
  │ Treatment      │ ADD context metadata     │ LOWER threshold +      │
  │ principle      │ (re-contextualize)       │ RE-COMPILE chunks      │
  └────────────────┴──────────────────────────┴────────────────────────┘

  CÙNG "PFC biết nhưng body không nghe" — KHÁC lý do:
    PTSD: body ACTS 200ms trước PFC (temporal sequence problem)
    OCD: body IGNORES done signal (signal quality problem)
    → PTSD = chunk fire → body respond → PFC arrives TOO LATE
    → OCD = chunk fire → done signal fire → body DOESN'T TRUST signal

  ⚠️ CO-OCCURRENCE: PTSD + OCD compound
    → Trauma → cortisol chronic → tuyến 2+3 suy yếu
    → Pre-existing OCD vulnerability + PTSD = OCD ESCALATE
    → Ngược lại: OCD hypervigilance + trauma = PTSD risk ↑
    → (PTSD §12 cross-ref)
```

### §7.2 — Autism × OCD: cascade, không phải comorbidity

```
⭐ OCD TRONG AUTISM: 17.4% — CAO HƠN DÂN SỐ CHUNG (~2-3%)

  🟢 van Steensel, Bögels & Perrin 2011: 17.4% autistic children
    meet OCD criteria (meta-analysis)
  (Cross-ref: Autism-Observation.md v1.0 §13.1)


  TẠI SAO CAO HƠN — 3 ĐƯỜNG DẪN:

    ① Sensory gain → prediction-deltas LỚN HƠN → uncertainty ↑
       → Serotonin ↓ → tuyến 2 threshold CAO → khó chấp nhận "done"
       → Thế giới cảm giác INTENSE hơn → "chưa đủ sạch/đủ đúng"
         cảm giác MẠNH HƠN ở người autistic

    ② Masking (chronic mismatch) → cortisol ↑ (Autism §6)
       → Tuyến 2 (serotonin ↓) + tuyến 3 (PFC impaired) CÙNG SUY YẾU
       → = Giống Tesla trajectory (§9) nhưng TỪ MÔI TRƯỜNG, không phải aging

    ③ Predictive coding differences (Autism §4)
       → Prediction-delta LARGER by architecture (không phải stress)
       → Done detector cần STRONGER signal để match "chuẩn done"
       → = Tuyến 1 hardware BÌNH THƯỜNG nhưng THRESHOLD tự cao hơn


  ⭐ PHÂN BIỆT: RRBs (Autism) vs OCD Compulsions

    (Cross-ref: Autism-Observation.md v1.0 §8.4)

    ┌──────────────────┬─────────────────────┬──────────────────────┐
    │                  │ RRBs (Autism)       │ OCD Compulsions      │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Core mechanism   │ Regulation / reward │ "Done" detector fail │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Feeling          │ Calming, engaging   │ Anxiety, "phải" làm  │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Completion       │ Feels done per-step │ NEVER feels done     │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Ego              │ Syntonic (WANTED)   │ Dystonic (UNWANTED)  │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Function         │ BUILDS + REGULATES  │ REDUCES anxiety      │
    ├──────────────────┼─────────────────────┼──────────────────────┤
    │ Intervention     │ SUPPORT             │ ERP + medication     │
    └──────────────────┴─────────────────────┴──────────────────────┘

    EGO-SYNTONIC vs EGO-DYSTONIC = test phân biệt chính:
      → "Bạn MUỐN làm điều này?" → CÓ = RRB (regulation, reward)
      → "Bạn KHÔNG MUỐN nhưng không dừng được?" → OCD (done fail)

  ⚠️ CLINICAL: PHẢI PHÂN BIỆT PER-BEHAVIOR
    → Autistic person CÓ THỂ có CẢ RRBs (functional) + OCD (pathological)
    → Suppress RRBs like treating OCD = remove REWARD + COPING + IDENTITY
      (triple loss — Autism §8.5)
    → OCD treatment (ERP + SSRI) CHỈ cho behaviors ego-dystonic

  🟡 FRAMEWORK: "CASCADE NOT COMORBIDITY" (Autism §13.4):
    → OCD trong autism = SAME architecture under MORE load
    → Configuration khác → prediction-delta lớn hơn → uncertainty cascade
    → Giảm sensory load + giảm masking demand
      → giảm cascade → giảm OCD symptoms
    → = ROOT khác standalone OCD: giải quyết ENVIRONMENT + LOAD
      bên cạnh (hoặc trước) treatment OCD trực tiếp
```

---

## §8 — TREATMENT MAP VÀO 3 TUYẾN

```
MỖI TREATMENT TARGET 1 TUYẾN CỤ THỂ:

┌──────────────────┬───────────┬──────────────────────────────────────┐
│ Treatment        │ Tuyến     │ Cách hoạt động qua framework        │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ SSRIs            │ Tuyến 2   │ Tăng serotonin → hạ threshold →     │
│ (fluoxetine,     │           │ signal bẩn VẪN được accept →         │
│ fluvoxamine)     │           │ "done" loop dừng.                    │
│                  │           │ ⚠️ OCD: 60-80mg (3-4× depression)   │
│                  │           │ 🟢 First-line, effective ~60%        │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ CBT / ERP        │ Tuyến 3   │ Train PFC HOLD + sit with anxiety   │
│                  │           │ + NOT compulse → body TỰ HỌC        │
│                  │           │ "anxiety tự giảm dù không check"    │
│                  │           │ = RE-COMPILE chunks (competitive     │
│                  │           │ re-linking — Chunk-Activation §3)    │
│                  │           │ 🟢 Effective, especially + SSRIs     │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ SSRIs + CBT      │ 2 + 3    │ SSRIs hạ threshold → PFC override    │
│ (COMBO)          │           │ DỄ HƠN → ERP thành công HƠN →       │
│                  │           │ chunks re-compile NHANH hơn.         │
│                  │           │ 🟢 GOLD STANDARD                     │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ Clomipramine     │ Tuyến 2   │ Serotonergic MẠNH hơn SSRIs.        │
│                  │ (mạnh hơn)│ Side effects nhiều → second-line.    │
│                  │           │ ⭐ Noradrenergic (desipramine) →     │
│                  │           │ KHÔNG effective → CHỈ serotonin path │
│                  │           │ 🟢 Clomipramine Collaborative 1991   │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ Augmentation:    │ Tuyến 3   │ Antipsychotic liều thấp → giảm      │
│ Antipsychotics   │ (support) │ dopamine → giảm SALIENCE            │
│                  │           │ (Dopamine-Is-Not-Reward.md) →     │
│                  │           │ threat priority GIẢM →               │
│                  │           │ PFC override DỄ hơn                  │
│                  │           │ 🟢 ~30% treatment-resistant respond  │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ DBS              │ Tuyến 1   │ Kích thích OFC-caudate TRỰC TIẾP →  │
│                  │           │ sửa "done" detector ở hardware      │
│                  │           │ 🟢 Last resort, invasive but works   │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ PANDAS treatment │ Tuyến 1   │ Kháng sinh → caudate phục hồi →     │
│                  │ (direct)  │ "done" detector sửa ở hardware      │
│                  │           │ 🟢 Swedo 1998; chỉ PANDAS/PANS      │
├──────────────────┼───────────┼──────────────────────────────────────┤
│ Mindfulness      │ Tuyến 3   │ "Tôi THẤY obsession → nó chỉ là    │
│                  │ (support) │ thought → không cần ACT"            │
│                  │           │ = PFC OBSERVE (Feeling.md v2.0)      │
│                  │           │ 🟡 Adjunct, không đủ đơn lẻ         │
└──────────────────┴───────────┴──────────────────────────────────────┘

⭐ TẠI SAO COMBO TỐT NHẤT:
  → SSRIs = cầu tạm (hạ threshold tuyến 2)
  → CBT = sửa đường (re-compile chunks tuyến 3)
  → SSRIs TẠO ĐIỀU KIỆN cho CBT:
    anxiety ↓ → PFC override DỄ → ERP thành công → chunks re-compile
  → = Có thể GIẢM SSRIs sau khi CBT đã re-compile đủ

⚠️ SSRIs ĐƠN LẺ CHƯA ĐỦ:
  → Sửa tuyến 2 → nhưng tuyến 1 VẪN lỗi + chunks VẪN compiled threat
  → Bỏ SSRIs → threshold TĂNG LẠI → loop QUAY LẠI
  → 🟢 Relapse: SSRIs alone ~80%, SSRIs+CBT ~30-50%, CBT alone ~20-30%
  → = CBT thay đổi CẤU TRÚC (chunks) → long-term tốt nhất
```

---

## §9 — TESLA CASE STUDY

```
🟡 TESLA = KHÔNG PHẢI OCD BẨM SINH. LÀ TRAJECTORY:

GIAI ĐOẠN 1 — Functional (trẻ → trung niên):
  → Visual-dominant CỰC MẠNH (eidetic imagery)
  → Rituals nhỏ: sắp xếp gọn gàng, patterns = functional
  → "Done" detector: INTACT → dừng đúng lúc
  → PFC: MẠNH → override khi cần
  → = "Kỹ tính" → giúp work quality → PRODUCTIVE

GIAI ĐOẠN 2 — Escalation (50s-60s):
  → Cortisol chronic: cô đơn, nghèo, bị exploit
    (Cortisol §7.7 Role ③ → ⑤ Silent: damage tích lũy)
  → Aging: OFC-caudate SUY YẾU DẦN → tuyến 1 giảm
  → PFC aging: dlPFC giảm → tuyến 3 giảm
  → Serotonin giảm (cortisol chronic → disrupt serotonin) → tuyến 2 giảm
  → = 3 tuyến CÙNG suy yếu dần

GIAI ĐOẠN 3 — OCD-like (cuối đời, 1930s-1943):
  → Số CỐ ĐỊNH (chia hết cho 3) = "done" detector LỖI
  → Rituals CỨNG NHẮC → không flexibility
  → Chunk library CỰC SÂU CỰC HẸP → cross-domain flexibility THẤP
  → = TRƯỢT từ functional → OCD-like theo trajectory

QUA FRAMEWORK:
  → Tesla KHÔNG "bị" OCD → Tesla TRƯỢT VÀO OCD-like
  → 3 tuyến suy yếu ĐỒNG THỜI + isolation + cortisol chronic
  → Nếu cuộc sống ổn → CÓ THỂ giữ functional
  → = OCD-like cuối đời = TRAJECTORY, không phải số phận
```

---

## §10 — HARDWARE VS ENVIRONMENT

```
⭐ MỖI TUYẾN CÓ TỶ LỆ HARDWARE/ENVIRONMENT KHÁC NHAU:

TUYẾN 1 — "Done" detector (OFC-caudate):
  Hardware:  ████████░░ ~80%
  Environment: ██░░░░░░░░ ~20%
  → Chủ yếu gen + wiring bẩm sinh
  → PANDAS: phá hardware → OCD → sửa → hết = NHÂN QUẢ
  → = KHÓA cứng nhất trong 3 tuyến

TUYẾN 2 — Satisfaction threshold (serotonin):
  Hardware:  █████░░░░░ ~50%
  Environment: █████░░░░░ ~50%
  → Baseline serotonin = gen
  → NHƯNG: stress → cortisol → suppress serotonin (environment)
  → Thiếu ngủ → serotonin synthesis giảm
  → Dinh dưỡng (tryptophan) → environment
  → = Tuyến LINH HOẠT nhất

TUYẾN 3 — PFC override:
  Hardware:  ███░░░░░░░ ~30%
  Environment: ███████░░░ ~70%
  → PFC capacity baseline = gen
  → NHƯNG: stress → cortisol → PFC impaired (🟢 Arnsten 2009)
  → Training (CBT) → PFC override MẠNH hơn
  → = Tuyến DỄ THAY ĐỔI nhất


⭐ WAXING-WANING COURSE (🟢 Skoog & Skoog 1999):

  OCD severity dao động theo environment:

  ↑ TĂNG khi: stress (cortisol ↑ → tuyến 2+3 ↓), thiếu ngủ (PFC ↓),
    life transitions (uncertainty ↑ → serotonin ↓), viêm (PANDAS → tuyến 1)

  ↓ GIẢM khi: cuộc sống ổn (cortisol ↓ → tuyến 2+3 phục hồi),
    ngủ đủ + tập thể dục (serotonin ↑ + PFC ↑), CBT thành công,
    SSRIs đúng liều

  → = OCD = hardware vulnerability + environment TRIGGER/MODULATE
  → = Giống diabetes: gen = vulnerability, lifestyle = trigger + severity


⭐ "CHỮA KHỎI HẲN":

  🟢 Longitudinal data:
  ┌───────────────────────┬──────────┬───────────────────────────────┐
  │ Outcome               │ Tỷ lệ   │ Qua framework                 │
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Full remission        │ ~25-30%  │ Tuyến 1 nhẹ + tuyến 2+3 sửa │
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Significant improve   │ ~40-50%  │ Tuyến 2+3 improve, tuyến 1   │
  │                       │          │ vẫn yếu → residual khi stress │
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Partial response      │ ~15-20%  │ Chỉ 1 tuyến respond           │
  ├───────────────────────┼──────────┼───────────────────────────────┤
  │ Treatment-resistant   │ ~10-15%  │ Tuyến 1 lỗi nặng → cần DBS   │
  └───────────────────────┴──────────┴───────────────────────────────┘

  Relapse (🟢):
    SSRIs đơn lẻ → dừng → ~80% relapse (threshold TĂNG LẠI)
    SSRIs + CBT  → dừng → ~30-50% relapse
    CBT đơn lẻ   → after → ~20-30% relapse (chunks re-compiled = structural)

  → CBT = thay đổi CẤU TRÚC (re-compile chunks) → long-term tốt nhất
  → COMBO: SSRIs tạo điều kiện → CBT re-compile → giảm SSRIs → giữ gains
  → OCD KHÔNG PHẢI "yếu ý chí" — là condition y khoa cần treatment
```

---

## §11 — HONEST ASSESSMENT

### §11.1 — Established (🟢)

```
🟢 ESTABLISHED:
  → OFC-caudate hyperactive trong OCD — fMRI replicated
  → SSRIs effective, cần liều 3-4× depression — APA guidelines
  → CBT/ERP effective — randomized controlled trials
  → SSRIs+CBT > đơn lẻ — gold standard, multiple RCTs
  → Relapse: SSRIs alone ~80%, CBT alone ~20-30%
  → Serotonin ↓40% khi yêu ≈ OCD — Marazziti 1999
  → Heritability ~47-58% — twin studies (Pauls 2010)
  → Bimodal onset: childhood + late adolescence
  → PANDAS/PANS: kháng thể → caudate → OCD — Swedo 1998
  → Noradrenergic antidepressants KHÔNG effective cho OCD
  → Clomipramine (serotonergic) > noradrenergic
  → Waxing-waning course — Skoog & Skoog 1999
  → ~25-30% full remission
  → Spreading activation — Collins & Loftus 1975
  → Reward prediction error — Schultz 1997
  → SNC effect — Crespi 1942, Flaherty 1996
  → Cross-species OCD-like: deer mice (Korff, Stein & Harvey 2008),
    SAPAP3 mice (Welch et al. 2007, Nature), Hoxb8 mice (Greer & Capecchi 2002;
    Chen et al. 2010 bone marrow rescue), CCD dogs (Dodman et al. 2010;
    Irimajiri et al. 2009 fluoxetine RCT)
  → Captive primate stereotypies — basal ganglia (Mason & Latham 2004)
  → Primate SIB + serotonergic (Novak et al. 2006; Lutz research program)
  → Anxious attachment (Bowlby 1969, Ainsworth 1978)
  → OCD in autism ~17.4% — van Steensel, Bögels & Perrin 2011 (meta-analysis)
```

### §11.2 — Framework synthesis (🟡)

```
🟡 FRAMEWORK SYNTHESIS:
  → 3-tuyến "done" pipeline: mỗi tuyến CÓ independent evidence
    (PANDAS = tuyến 1, SSRIs = tuyến 2, CBT = tuyến 3)
  → Serotonin = "certainty bias": consistent, giải thích nhiều hơn "happiness"
    (Status.md v2.1 §9.2 Serotonin Ratchet)
  → ⭐ Serotonin ↓ = AMPLIFIER, NOT ROOT CAUSE (§4.5):
    parallel với cortisol (amplifier, not cause). 4 evidence points:
    PANDAS (sửa root → hết), relapse pattern (SSRI vs CBT),
    love self-resolve (bond compile → serotonin phục hồi tự nhiên),
    cross-species variation (chuột=hardware, khỉ=mix, người=consequence)
  → ⭐ Cross-species OCD (§4.6): deer mice + SAPAP3 mice + dogs + primates
    → circuit CỔ (basal ganglia), NOT PFC-specific bug.
    Tuyến 1+2 = cross-species. Tuyến 3 = CHỈ NGƯỜI.
  → ⭐ SPM bias từ tuổi thơ × OCD-like trong Love (§4.5b):
    anxious attachment = SPM library threat-biased → hyper-monitoring →
    compound uncertainty (SPM + obligation) → serotonin ↓ amplified
  → Love ↔ OCD cùng circuit: supported bởi Marazziti, logic mạnh
  → Spreading activation uninhibited: serotonin ↓ = less inhibition → cascade
    (Chunk-Activation-Dynamics.md §2 + Collins & Loftus 1975 🟢)
  → Chunk-Miss không resolve: OCD qua BFM (§4.1) — consistent
  → Baseline Shift escalation: BFM §5 applied — consistent với OCD worsening
  → 5 Cortisol Roles in OCD: Role ②→③→⑤ escalation path
  → PFC 5% operator override failure: consistent với CBT evidence
  → Competitive re-linking (CBT): chunks mới vs chunks cũ
  → Hardware/environment tỷ lệ per tuyến: model, chưa đo trực tiếp
  → Spectrum (BDD, health anxiety, jealousy): BDD confirmed DSM-5
  → Tesla trajectory: functional → OCD-like via 3-tuyến degradation
  → Limerence kéo dài = OCD-like: consistent, chưa formal test
  → ⭐ Basal ganglia × Parkinson bridge (§4.7): Parkinson = gate LOCKED,
    OCD = gate signal NOISY — cùng architectural principle, khác failure mode.
    DBS cho cả hai: cùng nguyên lý bypass, khác target. Strengthens "circuit cổ."
  → ⭐ PTSD intrusions vs OCD obsessions (§7.1): PTSD = context-FREE chunk
    (amygdala-encoded, thiếu 3/4 metadata). OCD = context-INTACT chunk
    (done signal noisy). Cùng "PFC biết" nhưng khác: PTSD = body TRƯỚC PFC
    (temporal), OCD = body KHÔNG TIN done signal (quality).
  → ⭐ Autism × OCD cascade (§7.2): 17.4% prevalence. 3 đường dẫn
    (sensory gain → uncertainty, masking → cortisol, predictive coding → threshold).
    RRBs ≠ OCD (ego-syntonic vs dystonic). "Cascade not comorbidity."
```

### §11.3 — Hypothesis (🔴)

```
🔴 TESTABLE PREDICTIONS:

  ⭐ SEROTONIN = AMPLIFIER TEST (§4.5):
    → PANDAS: đo serotonin transporter TRƯỚC và SAU caudate treatment
      NẾU phục hồi → serotonin = consequence (root fixed → serotonin follows)
      NẾU không phục hồi → serotonin có independent component
    → Anxious vs secure attachment: đo serotonin khi yêu
      NẾU anxious ↓ MẠNH hơn → SPM bias → compound uncertainty → support

  ⭐ CROSS-SPECIES PREDICTIONS (§4.6):
    → Deer mice OCD-like: test với environmental enrichment
      NẾU enrichment giảm OCD-like → environment component confirmed
      NẾU không → pure hardware → consistent với tuyến 1 ~80% hardware
    → Hoxb8 mice neuroimmune: extend to adult human inflammatory conditions?

  ⭐ BASAL GANGLIA COMPARISON (§4.7):
    → Parkinson DBS (STN) vs OCD DBS (VC/VS): khác target, cùng principle
      NẾU mechanism overlap → DBS parameter optimization cross-inform?
    → Parkinson + OCD co-occurrence: dopamine medication → OCD symptoms?

  ⭐ AUTISM CASCADE (§7.2):
    → Sensory accommodation → giảm OCD symptoms trong autistic people?
      NẾU giảm → support "cascade" model (root = load, not independent OCD)
      NẾU không → OCD = independent co-occurring condition
    → RRBs vs OCD: ego-syntonic/dystonic test reliable cross-culturally?

  EXISTING PREDICTIONS (vẫn giữ):
    → Tryptophan depletion → tăng CHECKING behavior (not just mood)?
    → "Done" detector trainable? PANDAS: caudate phục hồi = partially plastic?
    → Love → OCD risk? Relationship bất ổn nhiều lần → serotonin chronic ↓?
    → Viêm mãn tính nhẹ adult → subclinical OCD? (extend PANDAS)
    → Lifestyle → đo tuyến: Sleep → tuyến 3, Exercise → tuyến 2
    → OCD target selection: hardware or compiled chunks?
    → AI as external "done" validator: giúp hay compulsion mới?
```

---

## §12 — CÂU HỎI MỞ

```
OCD-Q1: "Done" detector CÓ THỂ TRAIN?
  → Tuyến 1 = hardware → nếu fixed → KHÔNG
  → NHƯNG PANDAS: caudate phục hồi sau viêm → partially plastic?
  → CBT target tuyến 3 hay cũng sửa tuyến 1? → chưa rõ

OCD-Q2: Bimodal onset = 2 failure modes?
  → Peak 1 (~8-12): tuyến 1 hardware primary
  → Peak 2 (~18-25): tuyến 2+3 environment primary
  → Testable: childhood onset RESPONDS DIFFERENTLY to treatment?

OCD-Q3: Love circuit overlap → clinical implications?
  → OCD patients yêu KHÁC BIỆT không? (serotonin ĐÃ thấp sẵn)
  → Nhiều relationship bất ổn → serotonin chronic ↓ → OCD risk?

OCD-Q4: Viêm mãn tính nhẹ → subclinical OCD adult?
  → Extend PANDAS: gut inflammation, autoimmune nhẹ
  → → caudate ảnh hưởng nhẹ → "kỹ tính tăng dần"?

OCD-Q5: Aging × OCD prevention?
  → Tesla trajectory: biết mechanism → prevent?
  → Maintain serotonin + PFC training + cortisol management?

OCD-Q6: AI trong OCD treatment?
  → AI = external done validator? (giúp hay compulsion mới?)
  → AI + CBT = guided ERP at home?

OCD-Q7: Serotonin causal direction — species gradient?
  → Chuột: serotonin gần hardware cause (gen, wiring, ít cognitive)
  → Khỉ: mix cause + consequence (social deprivation component)
  → Người: gần consequence + amplifier (nhiều nguồn uncertainty)
  → = Serotonin ROLE thay đổi theo species complexity?
  → Testable: interventions target ROOT vs SEROTONIN → compare outcome

OCD-Q8: SPM childhood bias → adult OCD-like in love?
  → Strict parenting → SPM threat-biased → adult hyper-monitor partner
  → + Obligation overthinking compound
  → = Anxious attachment mechanism EXPLAINED qua framework
  → Testable: attachment style × serotonin levels × relationship stability

OCD-Q9: Hoxb8 mice neuroimmune × PANDAS × adult chronic inflammation?
  → Mice: bone marrow transplant fix OCD-like (neuroimmune)
  → Children: PANDAS = autoimmune attack caudate
  → Adults: chronic low-grade inflammation (gut, autoimmune)
    → subclinical caudate impact? → "kỹ tính tăng dần"?
  → = CÙNG principle ở 3 tầng: mice / children / adults

OCD-Q10: Autism × OCD — cascade model testable? (§7.2)
  → 17.4% autistic children có OCD — cao hơn ~2-3% dân số chung
  → NẾU sensory accommodation + reduce masking → OCD symptoms ↓
    → = CASCADE confirmed (root = architecture + load)
  → NẾU OCD persists dù load giảm → independent OCD co-occurring
  → Testable: compare OCD response to SSRIs+CBT trong autistic vs NT

OCD-Q11: PTSD + OCD compound — bidirectional risk? (§7.1)
  → PTSD cortisol chronic → tuyến 2+3 suy yếu → OCD ESCALATE?
  → OCD hypervigilance pre-existing → trauma = PTSD risk ↑?
  → Treatment order: PTSD first (stabilize cortisol) → then OCD?
  → Testable: PTSD veterans with pre-existing OCD traits → outcome comparison
```

---

## §13 — CROSS-REFERENCES + STATUS

### §13.1 — Cross-references v7.8

```
MECHANISM FILES:
  → Body-Feedback-Mechanism.md v2.0 — Chunk-Shift/Miss/Gap, §4 Compound, §5 Baseline Shift
  → Chunk-Activation-Dynamics.md — spreading activation, probability, trigger surface
  → Chunk.md v2.1 — substrate, compilation, competitive re-linking
  → Cortisol-Baseline.md v2.1 — 5 Cortisol Roles §7.7, cascade, PFC damage §9
  → PFC-Function.md v1.2 — 24 functions, HOLD + PROCESS, ~5% operator
  → Status.md v2.1 — §9.2 Serotonin Ratchet, certainty bias

OBSERVATION PARAMETERS:
  → Threat.md v1.0 — threat priority > PFC, 3 origin sources
  → Connection.md v4.0 — social buffering (co-regulation giảm cortisol)
  → Feeling.md v2.1 — PFC observation interface (ego-dystonic = PFC observe "sai")

RESEARCH FILES:
  → Love-Romantic.md v2.4 — §2.1 serotonin mechanism, §4.2 spreading activation
  → Hijack/Addiction-Analysis.md v3.0 — OCD loop vs addiction loop
  → Autism-Observation.md v1.0 — §8.4 Special Interests vs OCD, §13.1 OCD 17.4% (v2.2 §7.2)
  → PTSD-Analysis.md v1.0 — §14 context-tag model, §4 body-first temporal (v2.2 §7.1)
  → Parkinson-Analysis.md v1.1 — §2 basal ganglia gate mechanism (v2.2 §4.7)

CLARIFICATION:
  → Dopamine-Is-Not-Reward.md v1.1 — dopamine = salience (augmentation rationale)
  → Cortisol-Amplifier-Not-Cause.md — cortisol ≠ stress hormone
```

### §13.2 — File status

```
⭐ STATUS:

  Version: v2.2 (enriched post Health Conditions Drill)
  Date: 2026-05-15
  Lines: ~1,450+
  Backup: backup/OCD-Analysis-v75-era.md (896L, 2026-03-27)

  v2.0 CHANGES:
    ① ADDED §4: Chunk dynamics + spreading activation mapping
    ② UPDATED: All terminology v7.5 → v7.8
    ③ ADDED: 5 Cortisol Roles applied to OCD (§4.3)
    ④ ADDED: PFC-Function mapping for tuyến 3 (§4.4)
    ⑤ UPDATED: Love ↔ OCD reference Love-Romantic v2.2
    ⑥ ADDED: Competitive re-linking for CBT mechanism
    ⑦ UPDATED: All cross-references → v7.8 files
    ⑧ KEPT: Core 3-tuyến model, PANDAS, treatment map, spectrum, Tesla

  v2.1 ADDITIONS (2026-04-26):
    ⑨ §4.5: Serotonin = AMPLIFIER, NOT ROOT CAUSE (key insight)
    ⑩ §4.5b: SPM childhood bias × love OCD-like (anxious attachment mechanism)
    ⑪ §4.6: Cross-species evidence (mice, dogs, primates)
    ⑫ Updated §11 Honest Assessment + §12 Open Questions

  v2.2 ADDITIONS (2026-05-15 — post Health Conditions Drill):
    ⑬ §4.7: Basal ganglia × Parkinson bridge (gate LOCKED vs NOISY)
    ⑭ §7.1: PTSD intrusions vs OCD obsessions mechanism distinction
    ⑮ §7.2: Autism × OCD co-occurrence (17.4%, RRBs vs compulsions, cascade)
    ⑯ Cross-refs: 6 drill files added, dependency versions refreshed
    ⑰ §11-§12: New synthesis items, predictions, open questions (Q10-Q11)
```

---

> *OCD = "done" pipeline failure ở 1 hoặc nhiều tuyến.
> PANDAS/PANS = bằng chứng nhân quả: phá caudate (tuyến 1) → OCD → sửa → hết.
> Love dùng CÙNG circuit (serotonin ↓40% → uninhibited spreading activation)
> nhưng TỰ DỪNG khi bond compile → done detector: DONE.
> OCD KHÔNG TỰ DỪNG vì target không có exit condition.
> Serotonin ↓ = AMPLIFIER, NOT ROOT CAUSE — giống cortisol.
> Root cause = tuyến 1 hardware / stress / genuine uncertainty.
> Cross-species evidence (chuột, chó, khỉ): circuit CỔ (basal ganglia), NOT PFC bug.
> Tuyến 1+2 = cross-species. Tuyến 3 (PFC override) = CHỈ NGƯỜI.
> v2.2: Parkinson = gate LOCKED, OCD = gate NOISY — cùng basal ganglia, khác failure.
> PTSD intrusions = context-FREE chunks. OCD obsessions = context-INTACT, done-signal fail.
> Autism × OCD 17.4%: cascade not comorbidity. RRBs ≠ OCD (ego-syntonic vs dystonic).
> Treatment: SSRIs = phá amplifier loop (tuyến 2), CBT = sửa root chunks (tuyến 3).
> ⚠️ Framework cung cấp GÓC NHÌN — không thay thế chẩn đoán/điều trị y khoa.*
>
> *v2.2 — 2026-05-15 — enriched post Health Conditions Drill (6 files)*
