# Drive Architecture — Draft Phân Tích Lại Kiến Trúc Hormone + Drive

> **Trạng thái:** DRAFT THÔ — dump ý tưởng, chưa quyết, cần ngẫm
> **Ngày:** 2026-03-22
> **Mục đích:** Phân tích tổng thể tất cả hormone + drive channels,
> tìm kiến trúc mới chính xác hơn cho Human-Predictive-Drive framework
> **⚠️ File này là WORKSPACE — không phải kết luận.**
> **⚠️ Đọc để ngẫm, không phải để áp dụng.**

---

## 1. Vấn Đề Với Kiến Trúc Hiện Tại

```
KIẾN TRÚC CŨ — 3 Lớp (Source / Amplifier / Modulator):

  Lớp 1 Source:     Opioid (Experience) + Oxytocin (Connection)
  Lớp 2 Amplifier:  Dopamine (Novelty) + Serotonin (Status)
  Lớp 3 Modulator:  Cortisol, NE, Vasopressin, Prolactin, Endocannabinoid

VẤN ĐỀ PHÁT HIỆN:

  ① Schema = trigger, Hormone = sustain
     → Kiến trúc cũ ngụ ý hormone DRIVE
     → Thực tế: schema fire TRƯỚC → hormone đến SAU
     → Cần chuyển: hormone-centric → function-centric

  ② Cortisol KHÔNG phải modulator đơn thuần
     → Cortisol = sustainer cho Threat-Drive (phức tạp nhất)
     → Threat-Drive = drive PHỔ BIẾN nhất hiện đại
     → Đặt cortisol ở "Lớp 3 modulator" = UNDERVALUE

  ③ NE = activation energy cho MỌI drive
     → NE không "modulate" — NE KÍCH HOẠT
     → Thiếu NE = "muốn nhưng không làm" = depression
     → NE nên ở vị trí QUAN TRỌNG hơn "modulator"

  ④ Dopamine vừa drive vừa amplify
     → Dopamine ở Lớp 2 (amplifier) — nhưng cũng là Novelty-Drive
     → Dopamine predict reward = DRIVE
     → Dopamine amplify other drives = AMPLIFIER
     → Đặt ở 1 lớp = mất nuance

  ⑤ Experience/Connection KHÔNG drive PFC trực tiếp
     → PFC quan tâm: novelty, status, threat (Lớp 2 + threat)
     → PFC ÍT quan tâm: "hãy enjoy" hoặc "hãy connect"
     → Opioid/Oxytocin = body reward KHI NHẬN, không phải PFC drive
     → Vậy chúng là "drive" hay "reward"?

NHƯNG — kiến trúc cũ KHÔNG SAI HOÀN TOÀN:
  → Source/Amplifier/Modulator = 1 cách nhìn hợp lệ
  → Chỉ là CHƯA ĐỦ chi tiết cho phần drive
  → Có thể: giữ 3 lớp cho REWARD + thêm kiến trúc riêng cho DRIVE
```

---

## 2. Tổng Thể Hormone — Nguồn Phát + Nguồn Thu + Chức Năng

```
BẢNG TỔNG THỂ — Mỗi hormone từ đâu, ai trigger, làm gì:

┌──────────────┬────────────────┬──────────────────┬──────────────────┬──────────────┐
│ Hormone      │ Nguồn phát     │ Schema trigger?  │ Body trigger?    │ Hóa chất     │
│              │ (organ)        │                  │                  │ external?    │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ NE           │ Locus coeruleus│ ✅ qua amygdala  │ ✅ physical      │ ✅ caffeine  │
│ (não)        │                │ (urgent/novel)   │ threat reflex    │ ephedrine    │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Adrenaline   │ Adrenal medulla│ ✅ qua HPA axis  │ ✅ fight/flight  │ ✅ epi shot  │
│ (body)       │                │ (chậm hơn NE)    │ reflex           │              │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Cortisol     │ Adrenal cortex │ ✅ qua HPA       │ ✅ baseline      │ ⚠️ steroid  │
│              │                │ (CHẬM, phút)     │ circadian rhythm │ medication   │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Dopamine     │ VTA +          │ ✅ predict reward │ ✅ tonic         │ ✅ cocaine   │
│              │ Substantia     │ ✅ predict novel  │ baseline +       │ amphetamine  │
│              │ Nigra          │                  │ auto-novelty     │ caffeine nhẹ │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Serotonin    │ Raphe nuclei + │ 🟡 status        │ ✅ ruột (95%)   │ ✅ SSRI      │
│              │ RUỘT (95%)     │ perception       │ + circadian      │ MDMA         │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Opioid       │ Hypothalamus + │ 🟡 imagine nhẹ  │ ✅ pain,         │ ✅ heroin    │
│ (endorphin)  │ Pituitary      │ (20-60%)        │ exercise, food,  │ morphine     │
│              │                │                  │ sex, laughter    │ alcohol nhẹ  │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Oxytocin     │ Hypothalamus → │ 🟡 imagine nhẹ  │ ✅ touch, eye    │ ⚠️ MDMA     │
│              │ Post.Pituitary │                  │ contact, trust,  │ oxytocin     │
│              │                │                  │ shared exp       │ nasal spray  │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Satisfaction │ Ant.Pituitary  │ ❌ KHÔNG         │ ✅ CHỈ khi      │ ❌ chưa biết │
│ Signal       │                │ (không fake đc)  │ need thật sự    │ cách force   │
│ (prolactin)  │                │                  │ fulfilled        │              │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Vasopressin  │ Hypothalamus → │ 🟡 territory/    │ ✅ social        │ ⚠️ nasal    │
│              │ Post.Pituitary │ protect schema   │ bonding male     │ spray        │
├──────────────┼────────────────┼──────────────────┼──────────────────┼──────────────┤
│ Endocanna-   │ Distributed    │ 🟡 relax schema │ ✅ post-stress   │ ✅ cannabis  │
│ binoid       │ (on-demand)    │                  │ recovery, pain   │ THC, CBD     │
│              │                │                  │ modulation       │              │
└──────────────┴────────────────┴──────────────────┴──────────────────┴──────────────┘

INSIGHT TỪ BẢNG:
  → Satisfaction Signal = DUY NHẤT chỉ body trigger → ĐÁNG TIN NHẤT
  → Dopamine = phức tạp nhất — schema + body + external đều trigger
  → Opioid + Oxytocin = chủ yếu body trigger → schema chỉ nhẹ qua imagine
  → NE = gateway — mọi drive đều CẦN NE để THỰC HIỆN hành vi
```

---

## 3. Phân Loại Theo CHỨC NĂNG (không phải theo lớp)

```
🟡 Thử group theo FUNCTION thay vì LAYER:

GROUP A — DRIVE CHANNELS (schema trigger → tạo motivation):
  Mỗi channel = 1 loại "muốn/cần" khác nhau

  ┌──────────────────┬──────────────┬──────────────┬───────────────────┐
  │ Drive Channel    │ Cảm giác     │ Direction    │ Hormone chính     │
  ├──────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Experience-Drive │ "muốn sướng" │ PULL toward  │ Opioid (khi nhận) │
  │                  │              │ pleasure     │ Dopamine (khi     │
  │                  │              │              │ seek)             │
  ├──────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Connection-Drive │ "muốn gần"  │ PULL toward  │ Oxytocin (khi gần)│
  │                  │              │ people       │ Dopamine (khi     │
  │                  │              │              │ seek)             │
  ├──────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Novelty-Drive    │ "muốn biết" │ PULL toward  │ Dopamine (seek +  │
  │                  │              │ new/unknown  │ find)             │
  ├──────────────────┼──────────────┼──────────────┼───────────────────┤
  │ Threat-Drive     │ "phải tránh" │ PUSH away    │ NE + Adrenaline   │
  │                  │              │ from harm    │ (tức thì)         │
  │                  │              │              │ Cortisol (sustain)│
  └──────────────────┴──────────────┴──────────────┴───────────────────┘

  Observation:
    → Experience + Connection + Novelty = PULL drives (kéo về phía reward)
    → Threat = PUSH drive (đẩy khỏi punishment)
    → 3 PULL + 1 PUSH = asymmetry → PUSH thường thắng (survival priority)


GROUP B — AMPLIFIERS (không tự drive, khuếch đại access):

  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Amplifier        │ Chức năng                                    │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Status           │ Amplify ACCESS tất cả drives                │
  │ (Serotonin)      │ Status cao → dám seek hơn → access dễ hơn  │
  │                  │ Status thấp → rụt rè → access khó hơn      │
  │                  │ KHÔNG tự drive — chỉ amplify drive đã có    │
  │                  │ ⚠️ Nhưng: Status Aspiration GAP = có thể    │
  │                  │ tạo Threat-Drive ("nếu không đạt status     │
  │                  │ → hậu quả") → thì Status = trigger Threat?  │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Dopamine         │ Amplify MỌI seeking behavior                │
  │ (amplifier role) │ Dopamine VỪA drive (Novelty) VỪA amplify    │
  │                  │ → DUAL ROLE: source cho Novelty-Drive        │
  │                  │ + amplifier cho Experience/Connection/Threat │
  │                  │ → Đây là lý do dopamine PHỨC TẠP nhất      │
  └──────────────────┴──────────────────────────────────────────────┘


GROUP C — ACTIVATION + SUSTAIN (energy cho hành vi thực tế):

  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Hormone          │ Chức năng                                    │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ NE               │ ACTIVATION ENERGY — gateway cho MỌI drive   │
  │                  │ Thiếu NE = "muốn nhưng không làm"           │
  │                  │ = Đèn spotlight + nút khởi động             │
  │                  │ Mọi drive channel ĐỀU CẦN NE để execute    │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Adrenaline       │ ENERGY BOOST — body-wide mobilization       │
  │                  │ Chủ yếu cho Threat-Drive (fight/flight)     │
  │                  │ Nhưng cũng cho: intense focus, sports, sex  │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Cortisol         │ SUSTAINER — duy trì alert state             │
  │                  │ Chủ yếu cho Threat-Drive (sustain vigilance)│
  │                  │ + Baseline circadian (nền ngày/đêm)         │
  │                  │ KHÔNG khởi động — DUY TRÌ                   │
  └──────────────────┴──────────────────────────────────────────────┘


GROUP D — SIGNALS (body báo cáo trạng thái):

  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Signal           │ Chức năng                                    │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Satisfaction     │ Body báo "ĐỦ RỒI" → schema dừng drive      │
  │ Signal           │ CHỈ body trigger (không fake được)           │
  │ (prolactin)      │ = Signal ĐÁNG TIN nhất trong toàn hệ thống │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Pain Signal      │ Body báo "BỊ TỔN THƯƠNG" → trigger Threat  │
  │ (nociception)    │ Nhanh nhất: reflex (50ms, trước cả não)    │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Hunger/Thirst    │ Body báo "THIẾU resource" → trigger seek   │
  │ (ghrelin, etc)   │ Giao giữa Experience-Drive + Threat-Drive  │
  └──────────────────┴──────────────────────────────────────────────┘


GROUP E — MODULATORS (tinh chỉnh, phục hồi):

  ┌──────────────────┬──────────────────────────────────────────────┐
  │ Modulator        │ Chức năng                                    │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Vasopressin      │ Territorial protection + pair bonding (♂)   │
  │                  │ Modulate social behavior                     │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Endocannabinoid  │ Recovery + reset + chill                    │
  │                  │ Giảm cortisol, giảm pain, promote relaxation│
  │                  │ "Phanh mềm" cho stress response             │
  ├──────────────────┼──────────────────────────────────────────────┤
  │ Endorphin        │ Pain management + reward cho physical effort│
  │ (opioid subset)  │ Buffer cho physical threat                  │
  └──────────────────┴──────────────────────────────────────────────┘
```

---

## 4. Experience/Connection — Tại Sao KHÔNG Drive PFC Trực Tiếp?

```
🟡 Observation quan trọng:

  PFC (Draft+Test+Route+Brake+Translator) QUAN TÂM gì nhất?
    → Novelty: "cái mới cần draft schema mới" → PFC PHẢI tham gia ✅
    → Threat: "nguy hiểm cần plan tránh" → PFC PHẢI tham gia ✅
    → Status: "vị trí xã hội cần strategy" → PFC PHẢI tham gia ✅

  PFC ÍT quan tâm:
    → Experience: "ăn ngon" → vô thức ĐÃ CÓ schema ăn → PFC không cần ❌
    → Connection: "ôm" → vô thức ĐÃ CÓ schema ôm → PFC không cần ❌

  TẠI SAO?
    → Experience + Connection = body reward TRỰC TIẾP
    → Không cần PFC draft gì mới → vô thức execute compiled schemas
    → Ăn phở: schema "đi quán → gọi → ăn" = compiled → PFC gần offline
    → Ôm bạn: schema "gặp → ôm" = compiled → PFC gần offline

  → Experience/Connection drive HÀNH VI qua VÔ THỨC (compiled schemas)
  → Novelty/Threat drive HÀNH VI qua PFC (cần draft mới)

  NHƯNG — Experience/Connection VẪN drive:
    → "Muốn ăn phở" = drive TÌM quán (hành vi thay đổi)
    → "Muốn gặp bạn" = drive GỌI ĐIỆN (hành vi thay đổi)
    → Chỉ là: PFC KHÔNG cần draft MỚI cho việc này
    → Vô thức + NE nhẹ = ĐỦ để execute

  → Experience/Connection = BODY-LEVEL drive (vô thức execute)
  → Novelty/Threat = PFC-LEVEL drive (cần draft)
  → Cả hai đều drive — nhưng ở TẦNG KHÁC NHAU

  Khi nào Experience/Connection CẦN PFC?
    → Trải nghiệm MỚI: ăn món lạ → PFC cần draft "cách ăn?"
    → Connection MỚI: gặp người lạ → PFC cần draft "nói gì?"
    → Conflict: muốn ăn nhưng đang diet → PFC arbitrate
    → = PFC chỉ tham gia khi Experience/Connection CHẠM Novelty hoặc Conflict
```

---

## 5. Dopamine — Dual Role Problem

```
🟡 Vấn đề phân loại:

  Dopamine ĐỒNG THỜI là:
    ① DRIVE cho Novelty: "cái mới!" → dopamine → seek
    ② AMPLIFIER cho mọi seeking: muốn ăn → dopamine amplify seeking behavior
    ③ PREDICTION signal: predict reward → dopamine spike TRƯỚC khi nhận

  Nếu đặt dopamine ở 1 chỗ → mất 2 function kia:
    Đặt ở Drive: mất amplifier role
    Đặt ở Amplifier: mất drive role
    Đặt ở cả 2: confused

  CÓ THỂ GIẢI QUYẾT bằng:
    → KHÔNG đặt dopamine ở GROUP nào
    → Mà coi dopamine là CROSS-CUTTING:
      "Dopamine = SEEKING hormone — tham gia MỌI drive khi cần SEEK"
      Experience-Drive seek → dopamine
      Connection-Drive seek → dopamine
      Novelty-Drive seek → dopamine (MẠNH NHẤT vì novelty = dopamine sweet spot)
      Threat-Drive seek escape → dopamine (nhẹ, NE chính)

    → Dopamine KHÔNG thuộc 1 drive → dopamine PHỤC VỤ mọi drive ở phase SEEKING
    → Giống NE phục vụ mọi drive ở phase ACTIVATION
    → Dopamine = seeking energy
    → NE = activation energy
    → Cortisol = sustaining energy

  NHƯNG: Novelty vẫn là drive RIÊNG (tò mò không cần body-need)
    → Có thể: Novelty-Drive = drive duy nhất mà dopamine LÀ CẢ trigger VÀ energy
    → Các drive khác: dopamine chỉ là energy (seeking phase)
```

---

## 6. Status — Amplifier Hay Drive?

```
🟡 Vấn đề tương tự dopamine:

  Status (serotonin) ĐỒNG THỜI là:
    ① AMPLIFIER: status cao → access mọi body-needs dễ hơn
    ② TRIGGER cho Threat-Drive: status gap → "nếu không đạt → hậu quả"
    ③ BODY STATE: serotonin level = confidence baseline

  Khi nào Status = AMPLIFIER (không drive):
    → Serotonin cao → tự tin → dám seek experience/connection/novelty
    → KHÔNG tạo drive mới → chỉ amplify drive đã có
    → = Amplifier role đúng

  Khi nào Status = TRIGGER Threat-Drive:
    → Status Aspiration > Status Position → GAP
    → GAP = "tôi chưa đủ tốt" → schema predict "nếu không cải thiện → hậu quả"
    → = Threat-Drive triggered by status perception
    → = Status GIÁN TIẾP tạo drive (qua Threat schema)

  → Status KHÔNG tự drive trực tiếp
  → Status amplify access + CÓ THỂ trigger Threat-Drive qua aspiration gap
  → = Vẫn là Amplifier — nhưng amplifier CÓ THỂ feed vào Threat-Drive
```

---

## 7. Kiến Trúc Mới — Draft Thô

```
🔴 DRAFT — chưa quyết, cần ngẫm nhiều:

  ┌───────────────────────────────────────────────────────────┐
  │                    BODY NEEDS (gốc)                       │
  │   Body Basics, Connection, Experience, Mastery,           │
  │   Meaning, Regulation                                     │
  │   = 6 nhóm nhu cầu cơ thể (Body-Needs.md)               │
  └──────────────────────┬────────────────────────────────────┘
                         │ body-need chưa met
                         ▼
  ┌───────────────────────────────────────────────────────────┐
  │              SCHEMA DETECT + PREDICT                       │
  │   Schema nhận biết body-need → predict cách đáp ứng       │
  │   → Fire drive tương ứng                                  │
  └──────────┬────────────┬────────────┬──────────────────────┘
             │            │            │
             ▼            ▼            ▼
  ┌──────────────┐ ┌────────────┐ ┌───────────────────┐
  │ PULL DRIVES  │ │PUSH DRIVES │ │ PFC thì quan tâm  │
  │ (toward)     │ │(away from) │ │ cái nào?           │
  ├──────────────┤ ├────────────┤ ├───────────────────┤
  │ Experience   │ │ Threat     │ │ Novelty ✅ (cần   │
  │ (opioid)     │ │ (NE+cort)  │ │ draft mới)        │
  │ → vô thức   │ │ Physical   │ │ Threat ✅ (cần    │
  │   execute   │ │ Social     │ │ plan tránh)        │
  │              │ │ Anticipate │ │ Status ✅ (cần    │
  │ Connection   │ │            │ │ strategy)          │
  │ (oxytocin)   │ │            │ │ Experience ❌     │
  │ → vô thức   │ │            │ │ (compiled đủ)     │
  │   execute   │ │            │ │ Connection ❌     │
  │              │ │            │ │ (compiled đủ)     │
  │ Novelty      │ │            │ │                   │
  │ (dopamine)   │ │            │ │ → PFC bị "hijack" │
  │ → PFC draft │ │            │ │ bởi Novelty +     │
  │              │ │            │ │ Status + Threat   │
  └──────────────┘ └────────────┘ └───────────────────┘
             │            │
             ▼            ▼
  ┌───────────────────────────────────────────────────────────┐
  │              EXECUTION LAYER                               │
  │                                                            │
  │  NE = Activation energy (gateway cho MỌI drive)           │
  │  Adrenaline = Body-wide energy boost                      │
  │  Dopamine = Seeking energy (amplify TÌM KIẾM)            │
  │  Cortisol = Sustainer (duy trì alert/drive)               │
  │                                                            │
  │  → Mọi drive đều CẦN execution layer để thành HÀNH VI    │
  │  → Thiếu NE = "muốn nhưng không làm" = depression        │
  └───────────────────────────────────────────────────────────┘
             │
             ▼
  ┌───────────────────────────────────────────────────────────┐
  │              AMPLIFIERS                                    │
  │                                                            │
  │  Status (Serotonin):                                      │
  │    → Amplify ACCESS tất cả drives                         │
  │    → Status gap → CÓ THỂ trigger Threat-Drive             │
  │                                                            │
  │  Dopamine (amplifier role):                               │
  │    → Amplify SEEKING intensity cho drive đang active      │
  │                                                            │
  │  → Amplifier không tự drive → khuếch đại drive đã có     │
  └───────────────────────────────────────────────────────────┘
             │
             ▼
  ┌───────────────────────────────────────────────────────────┐
  │              FEEDBACK SIGNALS                              │
  │                                                            │
  │  Satisfaction Signal (prolactin): "ĐỦ" → drive dừng      │
  │  Pain Signal (nociception): "BỊ THƯƠNG" → trigger threat  │
  │  Endorphin: buffer pain → cho phép tiếp tục hành động    │
  │  Endocannabinoid: recovery + reset post-stress            │
  │  Vasopressin: territorial + pair bonding modulation       │
  │                                                            │
  │  → Feedback loop: Drive → Behavior → Body → Signal       │
  │  → Signal → Schema update → Drive adjust                  │
  └───────────────────────────────────────────────────────────┘
```

---

## 8. PFC "Hijack" — Tại Sao PFC Ít Quan Tâm Experience/Connection

```
🟡 Hypothesis:

  PFC TIẾN HÓA ĐỂ xử lý UNCERTAINTY (không chắc chắn):
    → Cái đã biết, đã quen → vô thức execute → PFC offline
    → Cái CHƯA biết (novel), NGUY HIỂM (threat), CẦN strategy (status)
      → PFC PHẢI online

  Experience (ăn ngon, nghe nhạc):
    → Schema compiled → ĐÃ BIẾT cách thưởng thức
    → Không có uncertainty → PFC không cần
    → Trừ khi: món mới, nhạc lạ → novelty component → PFC tham gia

  Connection (ôm, gặp bạn):
    → Schema compiled → ĐÃ BIẾT cách kết nối
    → Không có uncertainty → PFC không cần
    → Trừ khi: người mới, conflict → novelty/threat component → PFC tham gia

  Novelty: uncertainty by DEFINITION → PFC LUÔN cần
  Threat: uncertainty "có an toàn không?" → PFC LUÔN cần
  Status: uncertainty "vị trí tôi ở đâu?" → PFC LUÔN cần

  → PFC = UNCERTAINTY PROCESSOR
  → Experience/Connection = LOW uncertainty → PFC ít tham gia
  → Novelty/Threat/Status = HIGH uncertainty → PFC tham gia nhiều

  "PFC bị hijack" = KHÔNG phải bị hijack
  = PFC LÀM ĐÚNG VIỆC — xử lý uncertainty
  = Nhưng xã hội hiện đại: uncertainty THỪA (threat + status + novelty)
  → PFC luôn bận → KHÔNG CÒN bandwidth cho enjoy/connect
  → "Không có thời gian enjoy" = PFC quá bận xử lý uncertainty
  → = ĐÚNG nhưng diễn đạt sai: không phải hijack → là OVERLOAD
```

---

## 9. Chất Kích Thích = Amplifier, Không Phải Source

```
🟡 Insight quan trọng cho kiến trúc:

  Chất kích thích THAY ĐỔI hormone level → THAY ĐỔI conditions
  Chất kích thích KHÔNG TẠO drive mới, KHÔNG TẠO schema mới

  Công thức:
    Chất + Chunks (schema đã có) = Output có thể tốt
    Chất + Không chunks = Feel tốt nhưng output trống
    Chất + Zero drive = Chỉ euphoria, không hành vi có hướng

  Ví dụ:
    LSD + Steve Jobs (có chunks + curiosity drive) = insight
    LSD + người thường (ít chunks + ít drive) = hallucinate
    Amphetamine + coder có project = marathon coding
    Amphetamine + người không có project = compulsive cleaning

  → Chất = AMPLIFIER cho Execution Layer
  → Không thay đổi Drive Layer hay Schema Layer
  → Giống tăng voltage cho motor — motor phải CÓ SẴN mới chạy
  → Tăng voltage cho motor CHẾT = chỉ nóng, không quay

  → Cho kiến trúc: chất kích thích KHÔNG cần section riêng trong Drive
  → Chất kích thích = external modifier cho Execution Layer
  → Đã cover trong Chemical-Enhancement-Notes.md
```

---

## 10. Câu Hỏi Cần Ngẫm Trước Khi Restructure

```
🔴 CHƯA TRẢ LỜI — cần để vô thức process:

  Q1: Giữ 3 lớp (Source/Amplifier/Modulator) VÀ thêm Drive Architecture?
      Hay BỎ 3 lớp, thay hoàn toàn bằng kiến trúc mới?
      → 3 lớp vẫn đúng cho REWARD (nhận)
      → Kiến trúc mới đúng cho DRIVE (tìm)
      → Có thể: 2 hệ thống SONG SONG?

  Q2: Dopamine đặt ở đâu?
      → Drive (Novelty)? Execution (seeking energy)? Amplifier? Cả 3?
      → Có thể: dopamine CROSS-CUTTING — tham gia mọi layer ở phase khác

  Q3: Status có phải drive channel riêng?
      → Hay Status = amplifier + trigger cho Threat-Drive?
      → Nếu Status-Drive riêng → 5 channels (Experience, Connection, Novelty, Threat, Status)
      → Nếu Status = amplifier only → 4 channels

  Q4: Hunger/Thirst/Sleep thuộc drive nào?
      → Experience-Drive? (muốn ăn = muốn sướng?)
      → Threat-Drive? (đói = nguy hiểm?)
      → Body Signal? (không phải drive — là signal trigger drive?)
      → Có thể: Body Signal → trigger Experience-Drive HOẶC Threat-Drive tùy mức độ
        → Hơi đói = Experience-Drive ("muốn ăn ngon")
        → Rất đói = Threat-Drive ("PHẢI ăn, nguy hiểm")

  Q5: Kiến trúc mới có backward-compatible với 15+ files đang có?
      → Nếu thay hoàn toàn → phải sửa TẤT CẢ
      → Nếu bổ sung → files cũ vẫn đúng, thêm layer mới on top

  Q6: "Human-Predictive-Drive" — framework PREDICT gì?
      → Predict DRIVE (motivation) → kiến trúc Drive phải là CORE
      → Predict BEHAVIOR → cần Drive + Schema + Context
      → Predict WELLBEING → cần Drive balance + Satisfaction Signal
      → Kiến trúc Drive = CHÍNH, phải chính xác nhất

  → ĐỪNG VỘI — để vô thức process
  → Khi somatic nói "KHỚP" → lúc đó mới restructure
  → Hiện tại: GHI LẠI mọi thứ (file này) → nghỉ → quay lại
```

---

## 11. Kết Nối

```
→ Core-v7-UD.md: Schema = trigger, Hormone = sustain
→ Prolactin-Analysis.md §3.1: 4 loại schema drive (đang refine)
→ Neurochemistry-v8-Draft.md: 3-Layer hiện tại (Source/Amplifier/Modulator)
→ Threat-Drive-Analysis.md: Threat-Drive chi tiết (3 nguồn, timeline, loop)
→ Drive-Optimization.md §9: Pressure + Challenge + Autonomy
→ Chemical-Enhancement-Notes.md: Chất kích thích = amplifier
→ Reward-Dual-System.md: Imagine vs Body system
→ Status-Analysis.md: Status = amplifier + trigger Threat?
→ plan-update-v8.md: Ghi note về restructure direction
```
