---
title: 09 — Event-Chunks-Inference Matrix (tổng hợp cross-cutting)
parent: Child-Chunk-Development
session: N+4c2 → [translation session]
status: DRAFT TRANSLATION — Phase A
last_updated: 2026-04-16 (translation)
drill_phase: F1-P14
addresses_nut_that: ["cross-cutting — đóng góp cho cả 7 Nút Thắt verdict readiness"]
hypotheses: ["H1 cross-cutting evidence aggregation", "PFC-Inference Ladder empirical grip demonstration"]
scope: Aggregation — không có phân tích mới; tổng hợp events từ các arc 03-08 thành master matrix tables cho readers + synthesis
language: Tiếng Việt primary + English technical terms
depends_on:
  - 03-Visual-System-Arc.md
  - 04-Auditory-System-Arc.md
  - 05-Motor-Output-Arc.md
  - 06a-Interoceptive-Bladder-Keystone.md
  - 06b-Interoceptive-Other-States.md
  - 07-Social-Recognition-Arc.md
  - 08-Verbal-Production-Arc.md
---

# 09 — Event-Chunks-Inference Matrix

## §0 — Abstract + hướng dẫn đọc

File này là **aggregation file** cho F1 drill. Không chứa phân tích mới. Tổng hợp tất cả events đã phân tích trong các arcs [03](03-Visual-System-Arc.md)-[08](08-Verbal-Production-Arc.md) thành **master matrix tables** được tổ chức theo body-input system, plus **các phân tích cross-cutting** theo ladder level + nút thắt coverage + compile mechanism.

**Mục đích**:
1. **Reader reference** — cái nhìn tổng quan về tất cả F1 event-inference classifications
2. **Verdict readiness check** — tổng hợp bằng chứng cho từng Nút Thắt để đánh giá commitment readiness
3. **Distribution visualization** — ladder levels, compile mechanisms, body-input systems
4. **Open questions collection** — tổng hợp từ tất cả arc files cho 10-Synthesis closeout
5. **R-F1-* recommendations preliminary list** — hoàn thiện trong 10

**Cách đọc file**:
- §2 là deliverable trung tâm — 7 body-input arc tables
- §3-§6 là cross-cuts cung cấp các góc nhìn khác nhau về cùng một data
- §7-§8 tổng hợp open questions + framework recommendations
- §9 là cross-references

**Cách dùng**:
- Cần tra cứu một event cụ thể? → §2 tables theo arc, Ctrl+F tên event
- Cần xem tất cả L2 events? → §3.3 Ladder distribution
- Cần đánh giá bằng chứng cho một Nút Thắt? → §4 Nút Thắt coverage
- Cần hiểu compile mechanism distribution? → §5

**Scope boundary**: 09 không re-analyze events. Nếu cần mechanism analysis cho một event, hãy xem home arc file của nó (được chỉ định trong mỗi table row).

**Framework rule được duy trì**: Mọi entry đều theo [01 §6.3](01-PFC-Hardware-Reframe.md#§6) event-inference methodology. Mọi Ladder classification đều là **thuộc tính của event**, không phải thuộc tính của tuổi. Tất cả plausibility qualifiers 🟢🟡🔴 được bảo tồn từ home arc files.

---

## §1 — Phương pháp luận tóm tắt

### §1.1 — Quy tắc event-inference methodology

Per [01 §6.3](01-PFC-Hardware-Reframe.md#§6), mọi F1 event được phân tích theo template:

```
[Observable event, age range, research citation]
    ↓
[Chunks plausibly required]
    ↓
[PFC-Inference Ladder level (L0-L4)]
    ↓
[Plausibility qualifier 🟢🟡🔴]
```

**KHÔNG được phép**: "PFC trưởng thành ở tuổi X", "PFC phát triển khả năng Y ở tuổi X", các claims về hardware-maturation.

**ĐƯỢC PHÉP**: "Event Y có thể quan sát ở tuổi Z (citation); cần chunks A, B, C; ladder L2 🟡".

Quy tắc này được áp dụng đồng nhất qua tất cả events trong matrix.

### §1.2 — Các cấp độ PFC-Inference Ladder

Per plan §0.7:

| Cấp độ | Nhãn | Mô tả | Chunks điển hình |
|---|---|---|---|
| **L0** | Pure reflex | Phản ứng hardwired, không cần chunks | 0 |
| **L1** | Reflexive-differentiated | Phản xạ được điều chỉnh bởi state, proto-chunks tagging | 1-2 proto |
| **L2** | Pattern-match activation ⭐ | Chunk kích hoạt trên pattern recognition trước khi có hành động rõ ràng | 1-3 compiled |
| **L3** | Crude coordinated response | Pattern + crude action assembly | 3-5 compiled |
| **L4** | Coordinated execution | Full plan với prediction + sequence + integration | 5-8+ compiled |

**Các thuộc tính cần ghi nhớ** (per plan §0.7.3):
1. Ladder level là **thuộc tính của event**, không phải thuộc tính của tuổi
2. Non-uniform: các body-inputs khác nhau đạt các cấp độ khác nhau ở các tuổi khác nhau
3. Plausibility-qualified: mọi classification đều có 🟢🟡🔴
4. Graded within level: weak-L2 vs strong-L2, v.v.
5. Falsifiable: các alternative hypotheses có thể bị reject một cách tường minh

### §1.3 — Plausibility qualifiers

- 🟢 **Strong**: Bằng chứng empirical trực tiếp + mechanism-level plausibility + nhiều đường độc lập
- 🟡 **Moderate**: Framework plausibility + nhất quán với bằng chứng hiện có nhưng mechanism được inferred
- 🔴 **Weak**: Suy đoán với bằng chứng yếu; flagged cho testing trong tương lai (không có 🔴 events trong F1 drill output — các 🔴 events đã được reject hoặc defer)

### §1.4 — Cách đọc table rows

Định dạng mỗi row:

```
| ID | Tên event | Tuổi | Ladder | Chunks required | Compile mechanism | Research | Confidence | Home |
```

- **ID**: Internal reference identifier (V1, A1, M1, B1, H1, P1, T1, Em1, S1, Ve1). Chữ cái đầu = arc code.
- **Event**: Mô tả observable event
- **Tuổi**: Age range điển hình (individual variation per arc notes)
- **Ladder**: L0-L4 với transitional markers (ví dụ: "L2-L3" cho các transitional events)
- **Chunks required**: Chunks plausibly required để giải thích event
- **Compile mechanism**: Dominant compile mechanism từ plan §0.7 (Rep / Peak / Multi-mod / Sleep / Combined)
- **Research**: Primary citation (full cite trong home arc file)
- **Confidence**: 🟢🟡🔴 plausibility qualifier
- **Home**: Arc file nơi full analysis tồn tại

**Arc code legend**:
- **V** = Visual ([03](03-Visual-System-Arc.md))
- **A** = Auditory ([04](04-Auditory-System-Arc.md))
- **M** = Motor ([05](05-Motor-Output-Arc.md))
- **B** = Bladder interoceptive ([06a](06a-Interoceptive-Bladder-Keystone.md))
- **H/P/T/Em** = Hunger/Pain/Thermal/Emotional interoceptive ([06b](06b-Interoceptive-Other-States.md))
- **S** = Social recognition ([07](07-Social-Recognition-Arc.md))
- **Ve** = Verbal production ([08](08-Verbal-Production-Arc.md))

---

## §2 — ⭐ Master event matrix

### §2.1 — Visual arc events (từ [03-Visual-System-Arc.md](03-Visual-System-Arc.md))

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| V1 | Face preference (CONSPEC) | khi sinh | L0 | Hardwired template | — (hardware) | Morton & Johnson 1991 | 🟢 |
| V2 | Direct gaze preference ⭐ | 2-5 ngày | L2 | Gaze-template + direct-gaze bind | Rep + Multi-mod | Farroni 2002 | 🟢 |
| V3 | High-contrast pattern detection | newborn | L0-L1 | Edge detector substrate | — (hardware) | Slater et al. 1983 | 🟢 |
| V4 | Mother face recognition ⭐ | 5 tháng (E15) | L3 | Face individuation + identity bind + affective tag | Rep + Peak + Multi-mod | Bushnell 2001 | 🟢 |
| V5 | Feature integration | 4-6 tháng | L2 | Feature binding chunk | Rep + Multi-mod | Treisman 1980, devel. replications | 🟡 |
| V6 | Color discrimination | 2-4 tháng | L2 | Color category chunks | Rep | Bornstein 1976 | 🟢 |
| V7 | Object file chunks | 4-6 tháng | L2 | Object persistence proto | Rep + Multi-mod | Kahneman Treisman Gibbs 1992 | 🟡 |
| V8 | Object permanence ⭐ | 4-9 tháng | L2-L3 | Occlusion chunk + persistence | Rep + Multi-mod | Baillargeon 1987 VoE | 🟢 |
| V9 | Face categorization + individuation | 6-9 tháng | L2-L3 | Multiple face individuation chunks | Rep + Multi-mod | Quinn 2002 | 🟢 |
| V10 | Smooth pursuit eye movements | 6-8 tuần | L1 | Motor-visual tracking chunk | Rep + feedback loop | Aslin 1981 | 🟢 |
| V11 | Head turn toward visual target | 3-4 tháng | L2 | Target detection + head motor | Rep + Multi-mod | Bertenthal 1996 | 🟢 |
| V12 | Visually guided reaching | 4-5 tháng | L3 | Visuomotor transform + reach plan | Rep + Multi-mod | von Hofsten 1982 | 🟢 |
| V13 | Gaze following (E14) ⭐ | 6 tháng | L3 | Gaze direction chunk + inferred target | Multi-mod + social | Butterworth 1991 | 🟢 |
| V14 | Object tracking through occlusion | 8-9 tháng | L3 | Persistence + prediction | Rep + Multi-mod | Spelke 1990s | 🟢 |
| V15 | Joint attention triadic (E18) ⭐ | 9-12 tháng | L4 | Referent + social + self + triangulation | Multi-mod + social | Tomasello 1995 | 🟢 |
| V16 | Mirror self-recognition | 18-24 tháng | L4 | Self-visual-identity bind | Multi-mod + self chunks | Amsterdam 1972 | 🟢 |

**Home**: Tất cả rows → [03-Visual-System-Arc.md](03-Visual-System-Arc.md) để xem full analysis.

**Arc notes**:
- V1 (CONSPEC) là L0 baseline rõ ràng nhất trong F1 — hardwired template không có chunks
- V2 (Farroni direct gaze) là L2 marker rất sớm — L2 event sớm nhất có thể chứng minh trong F1 catalog
- V15 (joint attention E18) có thể là L4 visual event muộn nhất trong F1 — cần social + self + referent triangulation

### §2.2 — Auditory arc events (từ [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md))

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| A1 | Moro startle reflex | khi sinh | L0 | Hardwired startle | — (brainstem reflex) | Moro 1918 | 🟢 |
| A2 | Mother voice preference | khi sinh | L2 (prenatal) | Mother voice template (compiled prenatally) | Prenatal rep + amygdala tag | DeCasper & Fifer 1980 | 🟢 |
| A3 | Native language rhythm | khi sinh | L2 (prenatal) | Language rhythm template (prenatal) | Prenatal rep | Mehler 1988 | 🟢 |
| A4 | Phoneme discrimination universal | khi sinh | L2 | Universal phoneme categories | Rep (prenatal start) | Eimas 1971 | 🟢 |
| A5 | Phoneme narrowing ⭐ | 6-12 tháng | L2 | Native phoneme categories strengthened, non-native weakened | Rep + Multi-mod | Werker & Tees 1984 | 🟢 |
| A6 | Own name recognition ⭐ | 4.5 tháng | L2 | Phonological pattern + self-reference bind | Rep + Multi-mod + Peak | Mandel Jusczyk & Pisoni 1995 | 🟢 |
| A7 | Word segmentation ⭐ | 8 tháng | L2 | Statistical transitional-probability chunks | Rep (implicit statistical) | Saffran Aslin Newport 1996 | 🟢 |
| A8 | Common noun comprehension ⭐ | 6-9 tháng | L2-L3 | Word-referent binding (receptive) | Rep + Multi-mod + contingency | Bergelson & Swingley 2012 | 🟢 |
| A9 | Speech prosody-to-meaning | 8-12 tháng | L2 | Prosodic contour chunks + affect binding | Rep + Peak | Fernald 1985 | 🟢 |
| A10 | Head turn toward sound source | 3-4 tháng | L2 | Sound localization + motor chunk | Rep + feedback loop | Muir & Field 1979 | 🟢 |
| A11 | Attention orienting to familiar voices | ~0-3 tháng | L2 | Voice recognition + orient | Rep + Peak | DeCasper & Fifer 1980 | 🟢 |

**Home**: Tất cả rows → [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md).

**Arc notes**:
- A2/A3 (L2 events được compile prenatal) là các L2 events sớm nhất có thể chứng minh trong F1 catalog — compile bắt đầu trước t=0
- A5 (phoneme narrowing) là bằng chứng chính cho [04 §6.4](04-Auditory-System-Arc.md#§6.4) Nút Thắt 1 gradient verdict
- A6-A8 là 3 critical receptive-side events cung cấp H11 line 1 (13.5 tháng name gap)

### §2.3 — Motor arc events (từ [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md))

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| M1 | Palmar grasp reflex (E7) | khi sinh | L0 | Hardwired grasp | — (brainstem) | Prechtl 1977 | 🟢 |
| M2 | Rooting + sucking (E8) | khi sinh | L0 | Hardwired feeding reflex | — (brainstem) | Prechtl 1977 | 🟢 |
| M3 | Hand-to-mouth intentional | 2-3 tháng | L1 | Proto-chunk hand-to-mouth sequence | Rep + feedback | Rochat 1993 | 🟢 |
| M4 | Visually guided reaching ⭐ | 4-5 tháng | L3 | Visuomotor transform + reach plan (= V12) | Rep + Multi-mod | von Hofsten 1982 | 🟢 |
| M5 | Grasp with full hand | 5-6 tháng | L2 | Reach + grasp coordination | Rep + feedback | Halverson 1931 | 🟢 |
| M6 | Object exploration via hand | 5-9 tháng | L2-L3 | Reach + grasp + manipulate + visual integration | Rep + Multi-mod | Ruff 1984 | 🟢 |
| M7 | Pincer grasp (fine motor) | 9-10 tháng | L3 | Fine motor + visual targeting | Rep + Multi-mod | Fagard 2000 | 🟢 |
| M8 | Proto-imperative pointing | 9-10 tháng | L3 | Social + motor + communicative intent | Rep + Social + contingency | Bates 1979 | 🟢 |
| M9 | Proto-declarative pointing ⭐ | 12-14 tháng | L4 | Joint attention + social + showing intent | Rep + Social + Multi-mod | Liszkowski 2004 | 🟢 |
| M10 | Tool use + object manipulation | 12-18 tháng | L3-L4 | Tool + affordance + goal chunks | Rep + Multi-mod | Willatts 1999 | 🟢 |
| M11 | E25 intentional gesture ⭐ H11 | 14 tháng | L4 | Need detection + gestural handle + social | Rep + Social + contingency | Goodwyn Acredolo Brown 2000 | 🟢 |
| M12 | Delayed imitation | 14-18 tháng | L4 | Memory + motor planning + goal | Rep + Sleep consolidation | Meltzoff 1988 | 🟢 |
| M13 | Postural reflexes | khi sinh | L0 | Hardwired postural | — (brainstem) | Prechtl 1977 | 🟢 |
| M14 | Head control | 2-4 tháng | L1-L2 | Neck motor + head balance | Rep + feedback | Bayley norms | 🟢 |
| M15 | Rolling over | 4-6 tháng | L2 | Multi-segment motor coordination | Rep + feedback | Bayley norms | 🟢 |
| M16 | Sitting unsupported | 6-7 tháng | L2-L3 | Trunk balance + proprioception | Rep + feedback | Bayley norms | 🟢 |
| M17 | Crawling | 7-9 tháng | L3 | Limb coordination + locomotion goal | Rep + Sleep | Adolph 1995 | 🟢 |
| M18 | Pull to stand | 9-10 tháng | L3 | Leg motor + support + goal | Rep + feedback | Bayley norms | 🟢 |
| M19 | First independent steps | 10-14 tháng | L3-L4 | Balance + stride + fall recovery | Rep + Sleep consolidation | Adolph 2003 | 🟢 |
| M20 | Walking stable | 12-15 tháng | L4 | Gait + balance + navigation | Rep + Sleep + Multi-mod | Adolph 2003 | 🟢 |
| M21 | Running | 18-24 tháng | L4 | Advanced gait + speed control | Rep + Sleep | Adolph 2003 | 🟢 |

**Home**: Tất cả rows → [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md).

**Arc notes**:
- M4 và V12 là **cùng một event** (visuomotor reaching) được phân tích từ góc nhìn visual (03) và motor (05)
- M11 (E25 gesture) là bằng chứng within-child H11 chính cho line 2 của 7
- M8-M11 trace gestural communication arc song song với verbal arc với ~4-8 tháng lead

---

> *[Phase A hoàn thành — Header YAML + §0 Abstract + hướng dẫn đọc (5 mục đích, cách đọc, cách dùng, scope boundary, framework rule) + §1 Methodology (§1.1 event-inference rule template, §1.2 Ladder 5 levels table, §1.3 plausibility qualifiers, §1.4 table row format + arc code legend) + §2.1 Visual arc V1-V16 (16 events) + §2.2 Auditory arc A1-A11 (11 events + 3 arc notes) + §2.3 Motor arc M1-M21 (21 events + 3 arc notes).]*

### §2.4 — Bladder interoceptive arc events (từ [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md))

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| B1 | E3 newborn wet diaper cry | 3 tuần | L0-L1 | Discomfort signal only, không có anticipation | — (reflexive) | Wolff 1969 | 🟢 |
| B2 | Stage A unaware bladder | 0-6 tháng | L0 | Không có bladder signal chunks | — | Brazelton 1962 clinical | 🟢 |
| B3 | Repetition compile phase | 6-12 tháng | L0-L1 | Proto-chunks đang accumulate | Rep | — (inferred từ B4 onset) | 🟡 |
| B4 | Stage B đơ mặt L2 ⭐ | 12-18 tháng | **L2** ⭐ | Antecedent bladder signal chunk | Rep + contingency | Brazelton 1962, Bakker 2000 | 🟢 |
| B5 | Stage C crude response | 14-20 tháng | L3 | Signal + proto-motor response | Rep + Peak | Brazelton 1962 | 🟢 |
| B6 | Stage D "buồn đái" E23 ⭐ | 22 tháng | **L4** | Predictive + verbal + plan + motor | Rep + contingency + caregiver labeling | Feel-Example E23 + clinical | 🟢 |
| B7 | E24 "buồn ỉa" transfer | 24 tháng | L4 | Template transfer từ B6 | Template reuse | Feel-Example E24 | 🟢 |

**Home**: Tất cả rows → [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md).

**Arc notes**:
- B1-B7 là **traversal L0→L4 đầy đủ duy nhất trong một single body state** trong F1 catalog — bằng chứng single-state sạch nhất về non-uniform ladder progression
- B4 đơ mặt là ⭐ **L2 marker rõ ràng nhất** trong F1 (neutral valence, passive freeze, behavioral signature rõ ràng nhất)
- Full formalization trong [06a §5](06a-Interoceptive-Bladder-Keystone.md#§5) với 4 falsifiable predictions

### §2.5 — Other interoceptive arc events (từ [06b-Interoceptive-Other-States.md](06b-Interoceptive-Other-States.md))

#### §2.5.1 — Hunger sub-arc

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| H1 | E1 hunger cry newborn | 0-3 tháng | L0-L1 | Hunger signal → reflexive cry | — (brainstem + state) | Wolff 1969 | 🟢 |
| H2 | E11 differentiated hunger cry | 3-5 tháng | L1 | Hunger vs other distress distinct cry | Rep + parent response | Wasz-Höckert 1968 | 🟢 |
| H3 | Anticipatory feeding response ⭐ L2 | 3-4 tháng | **L2** | Bottle-sight → anticipatory quieting | Rep + Peak + contingency | Gewirtz 1977 | 🟢 |
| H4 | Crude reach for food | 8-12 tháng | L3 | Hunger + motor reach + food target | Rep + Multi-mod | Feeding observations | 🟢 |
| H5 | E21 "đói" verbal ⭐ | 18 tháng | **L4** | Hunger + verbal handle + plan + motor + social | Rep + contingency + labeling | Fenson CDI + Feel-Example | 🟢 |

#### §2.5.2 — Pain sub-arc

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| P1 | E2 pain cry newborn | 0-3 tháng | L0-L1 | Nociceptive → reflexive cry | — | Anand & Craig 1996 | 🟢 |
| P2 | Differentiated pain cry | 3-5 tháng | L1 | Pain vs hunger distinct cry | Rep | Wasz-Höckert 1968 | 🟢 |
| P3 | Vaccination pre-cry ⭐ L2 | 9-12 tháng | **L2** | Visit context → anticipatory distress | Rep + **Peak-negative valence** | Pierce & Rodrigues 1996 | 🟢 |
| P4 | E22 "đau chân" + body part ⭐ | 18-20 tháng | **L4** | Pain + body schema + verbal + gesture | Rep + Peak + labeling | Feel-Example E22 | 🟢 |

#### §2.5.3 — Thermal sub-arc (truncated)

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| T1 | E4 thermal distress newborn | 0-3 tháng | L0-L1 | Thermal signal → reflexive cry | — | Mitchell 1993 clinical | 🟢 |
| T2 | Differentiated thermal discomfort | 3-12 tháng | L1-L2 | Thermal signal differentiated | Rep (sparse) | Clinical + parent report | 🟡 |
| T3 | Wriggling / postural adjustment | 12-18 tháng | L3 partial | Proto-motor response to thermal | Rep + feedback | Parent observation | 🟡 |
| T4 | **Thermal L4 hiếm khi đạt trước 24 tháng** | — | ∅ (truncated) | Insufficient chunks compile by 24 tháng | Rep too sparse | Mitchell 1993 SIDS edge case | 🟢 |

**Arc note (T4)**: Thermal ladder traversal **bị truncated có hệ thống** trong 2 năm đầu tiên vì các compile mechanism modulators (exposure × saliency × contingency × valence) quá yếu cho thermal so với các interoceptive states khác. Sự truncation này được predicted bởi công thức và **có hậu quả nghiêm trọng** trong trường hợp SIDS edge case (xem [06b §4.3](06b-Interoceptive-Other-States.md#§4.3)).

#### §2.5.4 — Emotional sub-arc

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| Em1 | Emotional newborn states | 0-3 tháng | L0-L1 | Arousal + crude valence | — | Bridges 1932 | 🟢 |
| Em2 | E11 differentiated emotional | 3-5 tháng | L1 | Distinct emotional expressions | Rep + contingency | Izard 1978 | 🟢 |
| Em3 | E12 social smile (cross-ref S4) | 6-8 tuần | **L2** | Social + positive affect + face binding | Multi-mod + Peak + contingency | Wolff 1963 | 🟢 |
| Em4 | E26 egocentric empathy | 18 tháng | **L4** | Other-distress + Resonance + comfort handle | Multi-mod + Social + self chunks | Hoffman 2000, Feel-Example E26 | 🟢 |
| Em5 | Verbal emotional labels (post-F1) | 2-3 tuổi+ | L4 | Multi-layered: emotional + meta + vocabulary | Rep + contingency + abstract labeling | Bretherton & Beeghly 1982 | 🟡 |

**Arc notes**:
- Emotional H11 gap là lớn nhất (~24-30 tháng) vì productive bundle lớn nhất (bao gồm meta-emotional + abstract vocabulary + low-contingency caregiver labeling)
- Cross-refs: Em3 ↔ S4 (cùng event, interoceptive và social sides); Em4 ↔ S18

**Home**: Tất cả rows → [06b-Interoceptive-Other-States.md](06b-Interoceptive-Other-States.md).

### §2.6 — Social recognition arc events (từ [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md))

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| S1 | Hardware: multisensory + DMN + amygdala | — | (substrate) | — | — (hardware) | Meredith & Stein 1983, Doria 2010 | 🟢 |
| S2 | CONSPEC + Farroni direct gaze | 2-5 ngày | L2 | (= V2) | Rep + Multi-mod | Farroni 2002 | 🟢 |
| S3 | E9 cry contagion ⭐ | ngày 1 | L1 | Own-cry pattern + Resonance proto | Rep (hours) + Peak | Sagi & Hoffman 1976, Dondi 1999 | 🟢 |
| S4 | E12 social smile ⭐ keystone | 6-8 tuần | **L2** | Multi-modal face + voice + warmth + positive affect | Multi-mod (4-mech) + Peak | Wolff 1963 | 🟢 |
| S5 | E13 smile contagion | 4 tháng | L2 | Stable own-smile + other-smile recognition + bind | Multi-mod + Peak | Haviland & Lelwica 1987 | 🟢 |
| S6 | E15 mother recognition (= V4) | 5 tháng | L3 | Face individuation + identity + affective bind | Rep + Multi-mod + Peak | Bushnell 2001 | 🟢 |
| S7 | E14 gaze following (= V13) | 6 tháng | L3 | Gaze direction + inferred target | Multi-mod + social | Butterworth 1991 | 🟢 |
| S8 | E16 stranger anxiety ⭐ L2 | 7-9 tháng | **L2** | Familiar-face schema + novelty detection + peak-negative | Rep + Multi-mod + Peak-negative | Sroufe 1977 | 🟢 |
| S9 | E17 separation distress | 9 tháng | L3-L4 | Attachment figure + separation prediction + distress | Rep + Peak + Social | Bowlby 1969, Ainsworth 1978 | 🟢 |
| S10 | E19 social referencing | 9-12 tháng | L3-L4 | Face-emotion + inferred meaning + behavior mod | Multi-mod + Social + contingency | Sorce 1985 | 🟢 |
| S11 | E20 still-face Phase 2 puzzled ⭐ L2 | 6-9 tháng | **L2** | Dyadic interaction schema + violation detection | Rep + Multi-mod + Peak | Tronick 1978 | 🟢 |
| S12 | E18 joint attention triadic (= V15) | 9-12 tháng | L4 | Referent + social + self + triangulation | Multi-mod + Social | Tomasello 1995 | 🟢 |
| S13 | E30 peek-a-boo anticipation ⭐ L2 | 10-14 tháng | **L2** | Temporal prediction + social + peak-positive | Rep + Peak-positive | Parrott & Gleitman 1989 | 🟢 |
| S14 | Reciprocal smile production | 6-8 tuần+ | L2 | Smile motor + social contingency | Rep + contingency | Wolff 1963 | 🟢 |
| S15 | Proto-imperative pointing (= M8) | 9-10 tháng | L3 | Social + motor + imperative intent | Rep + Social | Bates 1979 | 🟢 |
| S16 | Proto-declarative pointing (= M9) | 12-14 tháng | L4 | Joint attention + showing intent | Multi-mod + Social | Liszkowski 2004 | 🟢 |
| S17 | E29 delayed imitation (= M12) | 14-16 tháng | L4 | Memory + social + motor planning | Sleep + Rep | Meltzoff 1988 | 🟢 |
| S18 | E26 egocentric empathy (= Em4) | 18 tháng | L4 | Other-distress + Resonance + own comfort template | Multi-mod + Self chunks | Hoffman 2000 | 🟢 |
| S19 | E31 "không" autonomy (= Ve13) | 18-24 tháng | L4 | Self-as-agent + negation + verbal assertion | Self chunks + Social + Rep | Erikson 1963, Feel-Example E31 | 🟢 |

**Home**: Tất cả rows → [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md).

**Arc notes**:
- Social events đạt L2 sớm nhất (S4 ở 6-8 tuần) vì multi-modal richness cao nhất — modulator thứ 5 implicit của compile
- S4 E12 là ⭐ keystone cho [07 §6](07-Social-Recognition-Arc.md#§6) Nút Thắt 3 multi-mechanism verdict
- S3 E9 cry contagion là bằng chứng decisively anti-hardware-mirror (asymmetric timing so với E12 và E13)
- 4 L2 markers từ social arc (S4 + S8 + S11 + S13) được thêm vào catalog trong N+4c1

### §2.7 — Verbal production arc events (từ [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md))

| ID | Event | Tuổi | Ladder | Chunks required | Compile | Research | Confidence |
|---|---|---|---|---|---|---|---|
| Ve1 | Cooing | 6-8 tuần | L1 | Laryngeal + vocal tract + positive affect | Rep + Social reinforcement | Oller 1980 | 🟢 |
| Ve2 | Reduplicated babbling ⭐ L2 mới | 4-6 tháng | **L2** | CV closure + rhythm + auditory feedback loop | Rep + feedback | Oller 1980, Stark 1980 | 🟡 |
| Ve3 | Variegated babbling | 8-10 tháng | L2-L3 | Multiple CV + sequence chunk | Rep + ambient matching | Oller 1980 | 🟢 |
| Ve4 | Canonical babbling | 8-10 tháng | L2-L3 | Native phonotactic templates + articulation | Rep + Statistical learning | Oller & Eilers 1988 | 🟢 |
| Ve5 | "Mama" pre-referential ⭐ L2 mới | 10-12 tháng | **L2** | Phonological pattern (không có semantic binding) | Rep + Social reinforcement | Jakobson 1941 | 🟡 |
| Ve6 | "Mama" referential | 12-14 tháng | L3 | Phonological + referent + word-referent binding | Multi-mod + contingency | Nelson 1973, Bloom 1973 | 🟢 |
| Ve7 | First 10 words | 12-18 tháng | L3 | ~10 word chunks + retrieval paths | Rep + Multi-mod + contingency | Fenson 1994 | 🟢 |
| Ve8 | E21 "đói" (= H5) | 18 tháng | L4 | (xem H5) | — | Fenson + Feel-Example | 🟢 |
| Ve9 | E22 "đau chân" (= P4) | 18-20 tháng | L4 | (xem P4) | — | Feel-Example E22 | 🟢 |
| Ve10 | E23 "buồn đái" (= B6) | 22 tháng | L4 | (xem B6) | — | Feel-Example E23 | 🟢 |
| Ve11 | Vocabulary spurt | 18-24 tháng | L3-L4 | Rapid word chunks accumulating + meta-chunk | Accumulated + parallel compile | Goldfield & Reznick 1990 | 🟢 |
| Ve12 | Two-word combinations | 18-24 tháng | L4 | Words + combinatorial + semantic relation | Usage-based + imitation | Brown 1973, Tomasello 2003 | 🟢 |
| Ve13 | E31 "không" (= S19) | 18-24 tháng | L4 | Self-as-agent + negation + verbal | Self + Social + Rep | Erikson 1963 | 🟢 |

**Home**: Tất cả rows → [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md).

**Arc notes**:
- Ve2 (reduplicated babbling) + Ve5 (pre-referential mama) là **2 L2 markers mới** được thêm vào catalog trong N+4c2 drill
- Ve8-Ve10 là body-state verbal labels (cross-referenced từ home arc files 06a/06b)
- Ve13 là cross-reference với S19 — cùng event, two-arc analysis

### §2.8 — Event count và cross-referencing summary

**Tổng số unique events được catalogued**: ~80 events qua 7 body-input arcs.

**Cross-referenced events** (cùng một observable event được phân tích từ nhiều arc angles):

| Event | Arc 1 | Arc 2 | Arc 3 |
|---|---|---|---|
| Visuomotor reaching | V12 visual | M4 motor | — |
| Mother face recognition | V4 visual | S6 social | — |
| Gaze following E14 | V13 visual | S7 social | — |
| Joint attention E18 | V15 visual | S12 social | — |
| Social smile E12 | Em3 interoceptive | S4 social | — |
| Proto-imperative pointing | M8 motor | S15 social | — |
| Proto-declarative pointing | M9 motor | S16 social | — |
| E25 gesture 14 tháng | M11 motor | (H11 line 2) | — |
| E21 "đói" 18 tháng | H5 interoceptive | Ve8 verbal | (H11 line 4) |
| E22 "đau" 20 tháng | P4 interoceptive | Ve9 verbal | (H11 line 5) |
| E23 "buồn đái" 22 tháng | B6 interoceptive | Ve10 verbal | (H11 line 3) |
| E26 egocentric empathy | Em4 interoceptive | S18 social | — |
| E29 delayed imitation | M12 motor | S17 social | — |
| E31 "không" | S19 social | Ve13 verbal | — |

**Quan sát**: ~14 events được cross-referenced qua 2-3 arc files. Các cross-references phản ánh thực tế là các body-input systems không thể phân tách sạch sẽ — hầu hết các developmental events đều liên quan đến multi-system coordination. Tổ chức theo arc là một **analytical tool**, không phải là claim về sự phân tách neural.

---

> *[Phase B hoàn thành — §2.4 Bladder B1-B7 (7 events + 3 arc notes: B4 cleanest L2 marker, single full L0→L4 traversal); §2.5 interoceptive other (§2.5.1 Hunger H1-H5, §2.5.2 Pain P1-P4, §2.5.3 Thermal T1-T4 truncated note, §2.5.4 Emotional Em1-Em5 + H11 gap note); §2.6 Social S1-S19 (19 events + 4 arc notes: L2 sớm nhất, E12 keystone, E9 anti-mirror, 4 L2 markers); §2.7 Verbal Ve1-Ve13 (13 events + 3 arc notes: Ve2+Ve5 new L2 markers, cross-refs); §2.8 Event count + 14 cross-referenced events table + observation về analytical tool.]*

## §3 — Phân tích Ladder distribution

### §3.1 — Ladder distribution counts

| Cấp độ | Events | Body-input systems |
|---|---|---|
| **L0** (pure reflex) | V1 V3 M1 M2 M13 A1 B2 (+ brainstem events qua các arcs) | Tất cả arcs trừ verbal |
| **L0-L1** transitional | V10 M3 M14 B1 H1 P1 T1 Em1 Ve1 | Motor + interoceptive + verbal early |
| **L1** (reflexive-differentiated) | Ve1 M3 H2 P2 Em2 | Motor + interoceptive + verbal |
| **L2** (pattern-match) | V2 V5 V6 V7 V11 A2 A3 A4 A5 A6 A7 A8 A9 A10 A11 M5 M15 B4 H3 P3 Em3 S2 S4 S8 S11 S13 S14 Ve2 Ve3 Ve4 Ve5 | **Cấp độ nhiều events nhất** — tất cả arcs, từ 2-5 ngày (V2) đến 14 tháng (S13) |
| **L2-L3** transitional | V8 V9 M6 M16 Ve3 Ve4 Ve11 | Visual + motor + verbal |
| **L3** (crude coordinated) | V4 V12 V13 V14 M4 M7 M8 M17 M18 B5 H4 T3 S6 S7 S9 S10 S15 Ve6 Ve7 | Tất cả arcs |
| **L3-L4** transitional | M10 M19 S9 S10 Ve11 | Motor + social + verbal |
| **L4** (coordinated execution) | V15 V16 M9 M11 M12 M20 M21 B6 B7 H5 P4 Em4 Em5 S12 S16 S17 S18 S19 Ve8 Ve9 Ve10 Ve12 Ve13 | Tất cả arcs, chủ yếu 12-24 tháng |

**Quan sát**:

- **L2 là cấp độ nhiều events nhất** — 31+ events qua tất cả arcs. Điều này nhất quán với L2 là cấp độ "pattern-match activation" quan trọng đánh dấu transition từ hành vi reflexive đến behavior driven by chunks. L2 là nơi hầu hết các "aha moments" phát triển xảy ra.
- **L0 phổ biến sớm rồi dần biến mất** — sau ~3 tháng, hầu hết các events là L1 trở lên. Pure reflex events tập trung ở khi sinh.
- **L4 events tập trung ở 12-24 tháng** — phản ánh bản chất tích lũy của chunks bundles; L4 cần nhiều compiled chunks + coordination.
- **Thermal arc là arc duy nhất với L4 bị truncated có hệ thống** — nhất quán với prediction của compile formula khi exposure × saliency × contingency × valence modulators quá yếu.

### §3.2 — L0 events — pure reflex catalog

| Event | Arc | Tuổi |
|---|---|---|
| Face preference CONSPEC | V1 | khi sinh |
| High-contrast pattern | V3 | khi sinh |
| Palmar grasp | M1 | khi sinh |
| Rooting + sucking | M2 | khi sinh |
| Postural reflexes | M13 | khi sinh |
| Moro startle | A1 | khi sinh |
| Stage A unaware bladder | B2 | 0-6 tháng |

**Pattern**: L0 events tập trung ở khi sinh và phản ánh circuitry brainstem/midbrain hardwired không có cortical chunks. Đến 3 tháng, hầu hết L0 events đã transition đến L1 (reflex + state modulation) hoặc cao hơn.

### §3.3 — L2 events — 10-marker catalog cho Nút Thắt 4

Per plan §0.8 L2 observable markers (được sử dụng như bằng chứng reframe cho PFC hardware × chunks missing reconciliation):

| # | Marker | Tuổi | Arc | Valence | Home |
|---|---|---|---|---|---|
| 1 | ⭐ Bladder đơ mặt | 12-18 tháng | B4 | Neutral-negative (passive freeze) | [06a §3.3](06a-Interoceptive-Bladder-Keystone.md#§3.3) |
| 2 | Vaccination pre-cry | 9-12 tháng | P3 | **Peak-negative** (active distress) | [06b §3.3](06b-Interoceptive-Other-States.md#§3.3) |
| 3 | Anticipatory feeding response | 3-4 tháng | H3 | **Peak-positive** (active quieting) | [06b §2.4](06b-Interoceptive-Other-States.md#§2.4) |
| 4 | Farroni direct gaze | 2-5 ngày | V2 | Neutral (attention orientation) | [03 §3.2](03-Visual-System-Arc.md#§3.2) |
| 5 | Stranger anxiety (E16) | 7-9 tháng | S8 | Negative (wariness → distress) | [07 §3.7](07-Social-Recognition-Arc.md#§3.7) |
| 6 | Still-face Phase 2 puzzled (E20) | 6-9 tháng | S11 | Neutral-negative (confusion) | [07 §3.10](07-Social-Recognition-Arc.md#§3.10) |
| 7 | Peek-a-boo anticipation (E30) | 10-14 tháng | S13 | **Peak-positive** (active excitement) | [07 §3.12](07-Social-Recognition-Arc.md#§3.12) |
| 8 | VoE looking time | 4-6 tháng | V8 (partial) | Neutral (cognitive surprise) | [03 §3.8](03-Visual-System-Arc.md#§3.8) |
| 9 | Reduplicated babbling | 4-6 tháng | Ve2 | Neutral (pattern exploration) | [08 §4.2](08-Verbal-Production-Arc.md#§4.2) |
| 10 | Pre-referential "mama" | 10-12 tháng | Ve5 | Neutral (phonological pattern) | [08 §4.5](08-Verbal-Production-Arc.md#§4.5) |

**L2 valence taxonomy** (từ [07 §3.12](07-Social-Recognition-Arc.md#§3.12) refinement): Ladder level L2 là **valence-independent về cấu trúc** nhưng **valence-dependent về body-level manifestation**:

- **Passive freeze** ở neutral/mild-negative valence (markers 1, 4, 8)
- **Active distress** ở peak-negative valence (markers 2, 5)
- **Active excitement** ở peak-positive valence (markers 3, 7)
- **Puzzled interruption** ở schema-violation (marker 6)
- **Pattern exploration** ở playful engagement (markers 9, 10)

Các L2 events khác nhau tạo ra các biểu hiện bodily observable khác nhau, nhưng cơ chế **pattern-match chunk firing trước khi có overt action** là cùng một mechanism.

**Implication cho Nút Thắt 4**: 10 L2 markers qua tất cả arcs, với diverse valence profiles và mechanisms, là **bằng chứng overwhelming** rằng em bé có functional pattern-match capability (L2 = chunks firing on pattern recognition) well before age timelines nhất quán với quan điểm cũ "PFC offline". Reframe (chunks-missing, không phải hardware-immature) được support mạnh mẽ.

### §3.4 — L3-L4 transitional events

| Event | Arc | Tuổi | Tại sao transitional |
|---|---|---|---|
| Object permanence (VoE → A-not-B) | V8 | 4-9 tháng | VoE evidence là L2-L3, A-not-B failure là L3 |
| Pincer grasp | M7 | 9-10 tháng | Crude + precision dependant on feedback |
| Tool use | M10 | 12-18 tháng | Simple L3, complex sequences L4 |
| First independent steps | M19 | 10-14 tháng | Crude at onset, L4 khi stable |
| Separation distress | S9 | 9 tháng | Coordinated distress L3, planful seeking L4 |
| Social referencing | S10 | 9-12 tháng | Face-emotion inference L3, behavior mod L4 |
| Vocabulary spurt | Ve11 | 18-24 tháng | Individual words L3-L4, productive generation L4 |

### §3.5 — L4 events — coordinated execution peaks

L4 events tập trung ở **12-24 tháng** với một số exceptions sớm hơn:

**L4 events sớm hơn (6-12 tháng)**: S12 joint attention (9-12 tháng), V15 joint attention (9-12 tháng). Các social-cognition L4 events này là sớm nhất vì chúng build on maximally-compiled multi-modal substrate.

**L4 events mainstream (12-18 tháng)**: M9 proto-declarative pointing, M11 E25 gesture, M12 delayed imitation, S16 pointing, S17 imitation. Motor-social L4 ở tầm giữa.

**L4 events muộn hơn (18-24 tháng)**: E21/E22/E23 body-state verbal, two-word combinations, self-agency autonomy, mirror self-recognition. Verbal + self-chunks L4 ở tầm cao nhất.

**Pattern**: L4 timing varies by 12+ months qua body-input systems. Motor-social L4 đến sớm hơn verbal hoặc self-chunk L4. Điều này nhất quán với **non-uniform ladder progression** — các arcs khác nhau climb ladder ở rates khác nhau vì compile mechanism modulators của chúng khác nhau.

### §3.6 — Non-uniform progression visualization

Tuổi xấp xỉ khi mỗi arc đạt mỗi ladder level:

| Arc | L0-L1 | L2 đầu tiên | L3 đầu tiên | L4 đầu tiên |
|---|---|---|---|---|
| Visual | khi sinh | 2-5 ngày (V2) | 4-5 tháng (V12) | 9-12 tháng (V15) |
| Auditory | khi sinh | khi sinh (A2-A3 prenatal) | 4.5-9 tháng (A6-A8 receptive/productive) | ~12-18 tháng (word-based via Ve) |
| Motor | khi sinh | 4-6 tháng (M5) | 4-5 tháng (M4) | 12-18 tháng (M9-M11) |
| Bladder | 0-6 tháng (B2) | 12-18 tháng (B4) | 14-20 tháng (B5) | 22 tháng (B6) |
| Hunger | 0-3 tháng | 3-4 tháng (H3) | 8-12 tháng (H4) | 18 tháng (H5) |
| Pain | 0-3 tháng | 9-12 tháng (P3) | — (đến verbal directly) | 18-20 tháng (P4) |
| Thermal | 0-3 tháng | — | 12-18 tháng partial (T3) | truncated (T4) |
| Emotional | 0-3 tháng | 6-8 tuần (Em3/S4) | 6-12 tháng (S9/S10) | 18 tháng (Em4) |
| Social | ngày 1 (S3) | 2-5 ngày (S2) | 5-6 tháng (S6/S7) | 9-12 tháng (S12) |
| Verbal | 6-8 tuần (Ve1) | 4-6 tháng (Ve2) | 12-14 tháng (Ve6) | 18-22 tháng (Ve8-Ve10) |

**Non-uniformity observations**:
- **Visual + social đạt L2 sớm nhất** (ngày 1-5 via V2/S2) — nhất quán với multi-modal richness + high salience
- **Bladder đạt L2 muộn nhất** (12-18 tháng) — nhất quán với tần suất lặp thấp + multi-modal richness thấp
- **Social đạt L4 sớm nhất** (9-12 tháng via S12/V15) — nhất quán với multi-modal richness + caregiver contingency
- **Thermal bị truncate** — L4 hiếm khi đạt trong window F1, nhất quán với weak modulators

**Framework implication**: Developmental sequence không phải là một hardware timeline. Nó là một **content-level compile trajectory** được driven bởi arc-specific modulators. Đây là central F1 thesis, được populate với 80+ events làm bằng chứng.

---

## §4 — Nút Thắt coverage table

### §4.1 — Tổng hợp bằng chứng per Nút Thắt

| Nút Thắt | Primary home | Supporting events | Verdict readiness |
|---|---|---|---|
| **1 Proto-chunk gradient** | [04 §6.4](04-Auditory-System-Arc.md#§6.4) | A5 phoneme narrowing (primary), V5-V9 visual gradient, M14-M21 motor gradient, B3-B4 bladder gradient, Ve2-Ve6 verbal gradient | ⭐ **PRIMARY VERDICT COMMITTED** N+4b |
| **2 P2 Chunks Base Adequacy** | [06a §6](06a-Interoceptive-Bladder-Keystone.md#§6) + [06b §6.2](06b-Interoceptive-Other-States.md#§6.2) | B1-B7 full ladder traversal (primary), H1-H5 hunger (validation), P1-P4 pain, T1-T4 thermal, Em1-Em5 emotional (5-for-5 ordinal ranking) | ⭐ **PRIMARY VERDICT COMMITTED** N+4c1 (4-channel compile × 4-parameter formula) |
| **3 Multi-modal binding** | [07 §6](07-Social-Recognition-Arc.md#§6) | S4 E12 social smile (keystone), S3 E9 cry contagion (anti-hardware-mirror), S5 E13 smile contagion (timing lag), V4/S6 mother recognition, Ve6 "mama" referential | ⭐ **PRIMARY VERDICT COMMITTED** N+4c1 (4-mechanism concurrent) |
| **4 PFC hardware × chunks missing** | [01](01-PFC-Hardware-Reframe.md) + all arcs | 10 L2 markers (xem §3.3) + non-uniform progression evidence (§3.6) + event-inference methodology application qua tất cả arc files | ⭐ **COMMITTED** trong 01; reinforced bởi tất cả arcs |
| **5 Receptive-Productive H11** | [08 §6](08-Verbal-Production-Arc.md#§6) | 7 converging lines (A6-A8 name gap + M11 gesture-verbal + B4-B6 bladder + H2-H5 hunger + P2-P4 pain + T-truncated + Em1-Em5 emotional) | ⭐ **PRIMARY VERDICT COMMITTED** N+4c2 (H11 formal statement + 7 predictions + 4 rejections) |
| **6 Alternative labeling handles** | [08 §5](08-Verbal-Production-Arc.md#§5) | Pre-verbal chunks evidence (9 chunk types), M11 E25 gesture (alternative handle), multi-channel output evidence (Feel-Example), Whorfian moderate (E22) | ⭐ **PRIMARY VERDICT COMMITTED** N+4c2 (Hybrid = retrieval + compression) |
| **7 Body state at compile (refined N+4c2-REV1, trước đây là "cortisol tagging")** | [06a §7](06a-Interoceptive-Bladder-Keystone.md#§7) + [06b §6.3](06b-Interoceptive-Other-States.md#§6.3) | B (bladder profile), H (hunger profile, feeding-connection entanglement), P (pain profile, endorphin-buffered), T (thermal edge case, chunks-absent failure), Em (emotional ⭐ imposed-parent dual-source primary case) | ⭐ **PRIMARY VERDICT COMMITTED** N+4c1 + **REFINED N+4c2-REV1** (novelty vs threat direction + 4-threshold gradient + 3 mechanism × 3 origin taxonomy + neural wear dimension) |

**Quan sát**: **Tất cả 7 Nút Thắt đều có primary verdicts committed** trước khi đến 10-Synthesis. File 10 sẽ tổng hợp + finalize cho 99-Master-Synthesis integration, không drill verdicts mới. **NT7 được refined substantial trong N+4c2-REV1** sau khi audit với upstream framework files ([Cortisol-Baseline.md](../../Cortisol-Baseline.md) + [Drive/Threat.md](../../Drive/Threat.md) + [Drive/Threat-Drive-Analysis.md](../../Drive/Threat-Drive-Analysis.md)) — framing "cortisol tagging" cũ không đầy đủ và dễ gây hiểu nhầm; refinement là architectural, không chỉ là scope expansion. Xem [06a §7.0](06a-Interoceptive-Bladder-Keystone.md#§7.0) cho upstream framework commitments được inherited, và [10 §1.7](10-F1-Synthesis.md#§1.7) cho refined final verdict.

### §4.2 — Cross-cutting evidence observations

Một số events đóng góp cho nhiều Nút Thắt đồng thời:

- **B4 Bladder đơ mặt L2** đóng góp cho Nút Thắt 1 (gradient evidence), 2 (P2 compile mechanism anchor), 4 (⭐ cleanest L2 marker), 7 (body-state-at-compile test case, 4-threshold gradient keystone), 5 (H11 line 3), củng cố nhiều verdicts với một event.
- **S4 E12 social smile L2** đóng góp cho Nút Thắt 1 (gradient), 2 (P2 compile mechanism via multi-mod richness), 3 (⭐ keystone), 4 (L2 marker via Em3/S4), cho thấy bản chất interconnected của các framework commitments.
- **A5 Phoneme narrowing** đóng góp cho Nút Thắt 1 (⭐ primary gradient evidence) + 4 (pattern-match L2 không cần PFC maturation).

Sự interconnection này không phải là design flaw — nó phản ánh thực tế là các developmental events có nhiều góc nhìn interpretive.

---

> *[Phase C hoàn thành — §3 Ladder Distribution (§3.1 counts table 8-row với Ladder levels, §3.2 L0 catalog 7 events + pattern, §3.3 L2 10-marker catalog với valence taxonomy 5-type + NT4 implication, §3.4 L3-L4 transitional 7 events, §3.5 L4 peaks: sớm/mainstream/muộn, §3.6 non-uniform progression 10-arc table + 4 observations + framework implication); §4 Nút Thắt coverage (§4.1 7-row NT table với primary home/supporting events/verdict readiness — tất cả committed, NT7 refined note, §4.2 cross-cutting observations: B4/S4/A5 multi-NT contributions).]*

## §5 — Compile mechanism distribution

### §5.1 — Compile mechanisms tóm tắt

Per plan §0.7 + [Body-Base/Schema/Chunk.md](../../Body-Base/Schema/Chunk.md) §2, bốn primary compile mechanisms:

1. **Rep (Repetition)** — LTP-based, dominant cho hầu hết chunks
2. **Peak (Emotional peak tagging)** — amygdala-driven accelerated compile
3. **Multi-mod (Multi-modal binding)** — temporal co-occurrence qua các modalities
4. **Sleep (Sleep consolidation)** — offline replay + late-LTP stabilization

Plus: **Contingency** (caregiver contingent response như modulator), **Feedback** (sensorimotor loop), **Statistical learning** (implicit transitional probability).

### §5.2 — Distribution theo dominant mechanism

**Rep-dominant events** (hầu hết F1 events): 60+ events. Repetition là universal compile mechanism. Ví dụ: V5, V6, V11, A4, A5, M5, M15-M21, Ve2-Ve7, v.v.

**Multi-mod-dominant events** (binding-critical): ~20 events. Ví dụ: V2 Farroni (face template + direct gaze), V4/S6 mother recognition, V12/M4 visuomotor, V15/S12 joint attention, S4 E12 social smile (keystone), Ve6 "mama" referential.

**Peak-dominant events** (affective tagging critical): ~10 events. Ví dụ: P3 vaccination pre-cry (peak-negative), H3 anticipatory feeding (peak-positive), S13 peek-a-boo (peak-positive), S8 stranger anxiety (peak-negative), Em3/S4 E12 social smile (peak-positive social).

**Sleep-dominant events** (consolidation-critical): M12 delayed imitation, M19-M21 motor milestones (locomotion cần sleep consolidation). Ít được highlight hơn nhưng load-bearing cho motor arc.

**Statistical-learning events**: A7 word segmentation, A5 phoneme narrowing, Ve4 canonical babbling (ambient phonotactic templates).

**Feedback-loop events**: Ve1-Ve4 babbling progression, M3 hand-to-mouth, M4/V12 visuomotor, M5 grasp, M14 head control.

### §5.3 — Quan sát: compile mechanisms là combinatorial

Hầu hết F1 events được driven bởi **nhiều mechanisms đồng thời**. "Dominant" mechanism chỉ là contributor mạnh nhất; các mechanisms khác thường cũng đóng góp. Ví dụ:

- **V2 Farroni direct gaze**: Rep (nhìn thấy khuôn mặt nhiều lần) + Multi-mod (face + gaze + affective context)
- **S4 E12 social smile**: Rep (caregiver lặp lại) + Peak (high-affect moments) + Multi-mod (4-mechanism per [07 §6](07-Social-Recognition-Arc.md#§6))
- **B4 bladder đơ mặt**: Rep (bladder cycles) + contingency (caregiver reactions) + Peak (discomfort valence)
- **Ve6 "mama" referential**: Rep (nghe "mama" nhiều lần) + Multi-mod (nghe trong khi nhìn thấy mẹ) + contingency (caregiver reinforcement) + Peak (affective moments với mẹ)

**Framework implication**: Compile formula nên được parametrize **combinatorial**, không phải single-mechanism. Per [06a §6.2](06a-Interoceptive-Bladder-Keystone.md#§6.2) 4-parameter rate formula:

```
compile_rate ≈ f(exposure × saliency × contingency × peak_valence)
```

Plus [07 §6.4](07-Social-Recognition-Arc.md#§6.4) 5th implicit modulator từ multi-modal richness. Điều này cho compile rate là một 5-parameter function, với các events khác nhau được weight khác nhau per parameter.

### §5.4 — Mechanism distribution per body-input arc

| Arc | Dominant mechanism | Secondary mechanism |
|---|---|---|
| Visual | Rep + Multi-mod | Peak (cho affective events) |
| Auditory | Rep + Statistical learning | Multi-mod (cho word-referent) |
| Motor | Rep + Feedback loop | Sleep consolidation |
| Bladder interoceptive | Rep + Contingency | Peak (moderate) |
| Hunger interoceptive | Rep + Contingency + Peak | Multi-mod (food context) |
| Pain interoceptive | Peak + Rep (sparser) | Contingency (caregiver response) |
| Thermal interoceptive | Rep (sparser) | (truncated) |
| Emotional interoceptive | Multi-mod + Peak | Rep + Contingency |
| Social | Multi-mod + Peak + Contingency | Rep |
| Verbal | Rep + Feedback + Multi-mod | Contingency (caregiver labeling) |

**Quan sát**: Social + verbal có combinations mechanisms phong phú nhất (tất cả 4-5 mechanisms active). Thermal có sparser nhất (Rep only, weak). Sự mechanism richness này dự đoán L2 onset timing — mechanisms phong phú hơn → L2 onset sớm hơn, nhất quán với §3.6 non-uniform progression table.

---

## §6 — Tổng hợp non-uniform ladder progression

### §6.1 — Framework claim

Các body-input systems khác nhau climb PFC-Inference Ladder ở các rates khác nhau, được driven bởi **arc-specific compile mechanism modulator profiles**. Non-uniform progression là **được predicted bởi framework** — không phải là một observation cần giải thích.

### §6.2 — Modulator profile per arc

Per §5.4 + [06a §6.2](06a-Interoceptive-Bladder-Keystone.md#§6.2) 4-parameter rate formula:

```
chunks_compile_rate ≈ f(exposure × saliency × contingency × peak_valence × multi_modal_richness)
```

Arcs với giá trị cao ở hầu hết parameters → compile nhanh → L2/L3/L4 onset sớm.
Arcs với giá trị thấp ở một số parameters → compile chậm → L4 muộn hoặc truncated.

| Arc | Exposure | Saliency | Contingency | Peak valence | Multi-modal | Tổng |
|---|---|---|---|---|---|---|
| Visual | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Rất Cao |
| Auditory | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | Rất Cao |
| Motor | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐⭐ | Cao |
| Social | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | **Tối đa** |
| Verbal (productive) | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | Cao (nhưng có H11 productive lag) |
| Bladder | ⭐⭐ | ⭐ | ⭐ | ⭐⭐ | ⭐ | Trung bình |
| Hunger | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | Cao |
| Pain | ⭐ | ⭐⭐⭐ | ⭐ | ⭐⭐⭐ | ⭐ | Trung bình (peak-dominated) |
| Thermal | ⭐ | ⭐ | ⭐ | ⭐ | ⭐ | **Thấp (truncated)** |
| Emotional | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | Cao nhưng productive lag tối đa |

### §6.3 — Prediction fit

Từ §3.6 non-uniform progression table + §6.2 modulator profiles, framework predict:

- **Social + Visual đạt L2 sớm nhất** (ngày 1-5) → ✅ match S2/V2 onset
- **Social đạt L4 sớm nhất** (9-12 tháng) → ✅ match S12/V15 joint attention
- **Thermal bị truncate ở L4** → ✅ match T4 observation
- **Bladder đạt L4 muộn nhất trong interoceptive** → ✅ match B6 22 tháng
- **Verbal productive đạt L4 ~18-22 tháng do H11 lag** → ✅ match Ve8-Ve10
- **Emotional productive đạt L4 muộn nhất** (24-30 tháng+) → ✅ match Em5 post-F1

**Framework confirmation**: Modulator-profile model **correctly predicts** non-uniform progression được quan sát qua tất cả arcs. Đây là bằng chứng cho 5-parameter compile formula xấp xỉ đúng.

### §6.4 — Clinical implication

**Single-modality developmental assessment là unreliable**. Một trẻ bị delay ở một body-input system có thể đang phát triển điển hình ở các hệ khác. F1 framework implies rằng:

1. Assessment nên multi-modal (cover nhiều body-input systems)
2. Delay ở một arc không predict delay ở các arcs khác
3. Intervention nên target các arc modulators cụ thể yếu nhất
4. "Developmental age" như một con số đơn lẻ là misleading; các arcs khác nhau có ages khác nhau

Đây là **practical implication** cho developmental psychology và pediatric assessment xuất hiện từ F1 framework mà không phải là focus của F1 drill.

---

## §7 — Open questions tổng hợp từ các arc files

Tổng hợp từ §12 sections của 03-08. Được sắp xếp theo chủ đề.

### §7.1 — Substrate + mechanism questions

1. **Fetal chunk formation extent**: Bao nhiêu chunks compile trước khi sinh? Fetal auditory learning (A2/A3) cho thấy một số chunks tồn tại prenatal. Visual, interoceptive, motor prenatal contributions không rõ ràng. ([04](04-Auditory-System-Arc.md) §12, [06a](06a-Interoceptive-Bladder-Keystone.md) §9)

2. **Có thể đo chunk strength trực tiếp không?**: Hiện tại được inferred từ behavior. Direct neural measurement ở infants chưa khả thi. Các paradigms fNIRS + MEG + habituation trong tương lai có thể enable. ([04 §6.6](04-Auditory-System-Arc.md#§6.6))

3. **Parallel vs serial compile trong bundles**: §6.3 giả định xấp xỉ linear gap scaling. Thực tế có parallelism + serialization. Models tinh vi hơn sẽ improve H11 predictions. ([08 §12](08-Verbal-Production-Arc.md#§12))

4. **Compile time t(age, chunk_type)**: Được giả định xấp xỉ constant. Likely varies với chunk complexity + substrate maturation + mechanism modulators. ([08 §12](08-Verbal-Production-Arc.md#§12))

### §7.2 — Individual variation questions

5. **Individual variation factors**: Gap 3 tháng đến 18+ tháng trong H11 milestones. Các factors genetic, epigenetic, caregiver-input, neural-substrate đều contribute. Dominant factor không rõ ràng. ([08 §12](08-Verbal-Production-Arc.md#§12))

6. **Crawling-skip babies**: Hậu quả cognitive của việc skip crawling (ngồi → pull to stand → đi)? Campos 2000 lập luận crawling có cognitive benefits. ([05 §9](05-Motor-Output-Arc.md#§9))

7. **Individual variation trong first steps 9-18 tháng**: Các factors genetic, physiological, environmental trong motor milestone timing. ([05 §9](05-Motor-Output-Arc.md#§9))

### §7.3 — Cross-cultural + environmental questions

8. **Cross-linguistic H11 testing**: Prediction 1 từ [08 §6.5](08-Verbal-Production-Arc.md#§6.5) yêu cầu cross-linguistic replication. Open empirical program. ([08 §12](08-Verbal-Production-Arc.md#§12))

9. **Cross-cultural variation trong motor milestones**: Super 1976 East African infants đi sớm hơn, Karasik 2010 review. Framework F1 predict caregiver-practice shifts như thế nào? ([05 §9](05-Motor-Output-Arc.md#§9))

10. **Cultural variation trong body-state vocabulary**: Vietnamese richer body parts → deeper body schema chunks? Framework implication của handle granularity. ([06b](06b-Interoceptive-Other-States.md) + [08 §5.6](08-Verbal-Production-Arc.md#§5.6))

11. **Tác động của institutional care**: Reduced caregiver contingency ảnh hưởng compile mechanism nào nhất? Framework predict combined effect của: (a) chunk-association damage via Level 3-like compile body state cho emotional + hunger (feeding-connection entangled) + (b) neural wear trên developing PFC từ chronic moderate threat cortisol + (c) amplified damage via imposed-adult origin khi caregiver-of-record là professional staff với rotation (không có secure-base continuity). Framework testable predictions per [06a §7](06a-Interoceptive-Bladder-Keystone.md#§7) + [06b §6.3](06b-Interoceptive-Other-States.md#§6.3) refined model.

### §7.4 — Specific mechanism questions

12. **Quantitative contribution của sleep consolidation**: Người lớn ~20-30% improvement. Infant likely similar hoặc lớn hơn. Direct comparison studies needed. ([05 §9](05-Motor-Output-Arc.md#§9))

13. **Delayed imitation (Meltzoff 1988) — mechanism**: 14-18 tháng imitate actions từ nhiều ngày trước. Visual memory, motor imagery, hoặc language-mediated? Framework question cho chunks persistence. ([05 §9](05-Motor-Output-Arc.md#§9))

14. **Tại sao hand motor đi trước articulation motor 4+ tháng?**: Nhiều hypotheses (visual feedback, cortical representation size, evolutionary age) — chưa được tested definitively. ([05 §9](05-Motor-Output-Arc.md#§9))

15. **Handle migration**: Gestural handle có dissolve khi verbal handle compile không? Hay handles accumulate như parallel access paths? ([08 §5.9](08-Verbal-Production-Arc.md#§5.9))

16. **Internal-only handles (felt sense)**: Handleless chunks hay chunks với internal-only handles? Framework distinction ảnh hưởng đến theories of pre-reflective cognition. ([08 §5.9](08-Verbal-Production-Arc.md#§5.9))

### §7.5 — Multi-mechanism binding questions

17. **Relative contributions của 4 binding mechanisms**: Nút Thắt 3 commits 4 concurrent mechanisms không có weighting. Selective disruption không ethically possible ở infants. Animal models? ([07 §6.6](07-Social-Recognition-Arc.md#§6.6))

18. **Dissociation evidence cho binding**: Có pathological cases nào nơi một binding mechanism intact nhưng mechanism khác disrupted không? Autism literature gợi ý multisensory integration differences. ([07 §6.6](07-Social-Recognition-Arc.md#§6.6))

19. **Chunks binding qua thời gian**: [06a §4.3](06a-Interoceptive-Bladder-Keystone.md#§4.3) E23→E24 template transfer. Transfer tương tự cho cross-modal binding qua các identities mới? ([07 §6.6](07-Social-Recognition-Arc.md#§6.6))

### §7.6 — Language + handles questions

20. **Vocabulary spurt mechanism specifics**: Tại sao ở ~18 tháng? Triggers cho rate change? ([08 §12](08-Verbal-Production-Arc.md#§12))

21. **Two-word boundary F1/F3**: F1 kết thúc và F3 bắt đầu ở đâu chính xác? Current boundary ở ~18-24 tháng là pragmatic. ([08 §12](08-Verbal-Production-Arc.md#§12))

22. **Adult L2 H11**: Prediction 7 từ [08 §6.5](08-Verbal-Production-Arc.md#§6.5). Partially tested; open systematic empirical program.

23. **Animal chunks không có language**: Non-human animals có gestural/action handles không? Hay chunks của chúng là purely content-level không có handle layer? ([08 §5.9](08-Verbal-Production-Arc.md#§5.9))

---

## §8 — Framework update recommendations (preliminary list)

Tổng hợp từ các arc files. Hoàn thiện trong [10-F1-Synthesis.md](10-F1-Synthesis.md) §5.

- **R-F1-1**: Rewrite [Imagination/PFC-Analysis.md](../../Imagination/PFC-Analysis.md) §4 timeline với reframe. **Partially completed** trong N+4 prep via §4.0 REFRAME block + §4.1 corrections. Final integration trong 10.

- **R-F1-2**: Propose "đơ mặt" như developmental marker với operational definition + 4 falsifiable predictions + 2 counter-hypothesis rejections. **Fully formalized** trong [06a §5](06a-Interoceptive-Bladder-Keystone.md#§5). Ready cho framework contribution.

- **R-F1-3**: Commit multi-mechanism cross-modal binding (4 concurrent mechanisms) architectural commitment trong [Body-Base/Schema/Chunk.md](../../Body-Base/Schema/Chunk.md) §2. **Fully formalized** trong [07 §6](07-Social-Recognition-Arc.md#§6). Ready cho Schema/Chunk update.

- **R-F1-4**: Update [Body-Feedback-Draft/01-Foundation.md](../Body-Feedback-Draft/01-Foundation.md) §5.5 P2 mechanism với F1 substrate evidence (cross-link với 4-channel compile × 4-parameter rate formula từ [06a §6](06a-Interoceptive-Bladder-Keystone.md#§6)).

- **R-F1-5**: Update [Body-Base/Feeling/Feel-Example-Draft.md](../../Body-Base/Feeling/Feel-Example-Draft.md) với cross-references đến F1 event analyses.

- **R-F1-6**: Propose H11 + PFC-Inference Ladder như framework contributions trong 99-Master-Synthesis. **H11 fully formalized** trong [08 §6](08-Verbal-Production-Arc.md#§6); **Ladder** applied qua tất cả arcs + 10-marker catalog.

- **R-F1-7** (expanded N+4c2-REV1): Update [Body-Base/Body-Parenting-Optimization.md](../../Body-Base/Body-Parenting-Optimization.md) với refined NT7 framework — novelty vs threat cortisol direction, 4-threshold gradient (nhẹ/vừa/nặng/cực đoan), 3 mechanism × 3 origin taxonomy, imposed-parent dual-source damage, neural wear dimension (ACE), 3 update paths cho chunks đã bị damage, "cortisol is not the enemy" public-health framing. Apply qua 5 body states (bladder, hunger, pain, thermal, emotional attachment). Scope substantially lớn hơn earlier draft. Xem [10 §5.7](10-F1-Synthesis.md#§5.7) cho full integration content.

- **R-F1-8**: Cross-reference [Agent/](../Agent/) sub-folder files (Resonance, Self-Pattern-Modeling) với F1 developmental evidence cho E9/E10/E12/E26/E31 cross-arc events. Particularly Resonance framework anchors trong E9+E10+E12 (từ [07 §7](07-Social-Recognition-Arc.md#§7)).

- **R-F1-9** (emerging): Update [Modality-Analysis.md](../../Modality-Analysis.md) với commitment rằng verbal KHÔNG PHẢI modality thứ 5 mà là distinct architectural layer (per [08 §5.4](08-Verbal-Production-Arc.md#§5.4) Nút Thắt 6 verdict).

- **R-F1-10** (emerging): Thêm non-uniform ladder progression table (§3.6 file này) vào Schema/Chunk.md như bằng chứng empirical cho body-input-specific compile trajectories.

**Tổng số recommendations**: 10 framework updates sẵn sàng cho 10-Synthesis + 99-Master-Synthesis integration.

---

## §9 — Cross-references

### §9.1 — Within F1 Child-Chunk-Development

- [00-Chunk-System-Sketch.md](00-Chunk-System-Sketch.md) — F1 sub-folder orientation
- [01-PFC-Hardware-Reframe.md](01-PFC-Hardware-Reframe.md) — §6.3 methodology rule + Nút Thắt 4 primary home
- [02-Womb-to-Birth-Baseline.md](02-Womb-to-Birth-Baseline.md) — §9.1 baseline state at t=0
- [03-Visual-System-Arc.md](03-Visual-System-Arc.md) — §2.1 source cho V1-V16
- [04-Auditory-System-Arc.md](04-Auditory-System-Arc.md) — §2.2 source cho A1-A11; Nút Thắt 1 ⭐ verdict
- [05-Motor-Output-Arc.md](05-Motor-Output-Arc.md) — §2.3 source cho M1-M21; Nút Thắt 5+6 preview
- [06a-Interoceptive-Bladder-Keystone.md](06a-Interoceptive-Bladder-Keystone.md) — §2.4 source cho B1-B7; Nút Thắt 2 ⭐ + 5 ⭐ + 7 ⭐ + 4 reinforcement
- [06b-Interoceptive-Other-States.md](06b-Interoceptive-Other-States.md) — §2.5 source cho H/P/T/Em events; Nút Thắt 2 cross-state validation
- [07-Social-Recognition-Arc.md](07-Social-Recognition-Arc.md) — §2.6 source cho S1-S19; Nút Thắt 3 ⭐ primary verdict
- [08-Verbal-Production-Arc.md](08-Verbal-Production-Arc.md) — §2.7 source cho Ve1-Ve13; Nút Thắt 5 ⭐ + 6 ⭐ primary verdicts + H11 full formalization
- [10-F1-Synthesis.md](10-F1-Synthesis.md) — final verdicts aggregation + R-F1-* finalization

### §9.2 — Upstream framework files

- [../../Body-Base/Schema/Chunk.md](../../Body-Base/Schema/Chunk.md) — substrate architecture (target cho R-F1-3 + R-F1-10 updates)
- [../../Body-Base/Body-Input-Enumeration.md](../../Body-Base/Body-Input-Enumeration.md) — body-input taxonomy (L0 + L1 + L3 drives)
- [../../Body-Base/Feeling/Feel-Example-Draft.md](../../Body-Base/Feeling/Feel-Example-Draft.md) — 50+ events verbatim, anchors cho F1
- [../../Body-Base/Body-Parenting-Optimization.md](../../Body-Base/Body-Parenting-Optimization.md) — R-F1-7 update target
- [../../Imagination/PFC-Analysis.md](../../Imagination/PFC-Analysis.md) — R-F1-1 update (partially completed)
- [../../Modality-Analysis.md](../../Modality-Analysis.md) — R-F1-9 update target

### §9.3 — Drilled sub-folders (cross-cut)

- [../Learning-Cycle/Learning-Cycle.md](../Learning-Cycle/Learning-Cycle.md) — H8 learning cycle (áp dụng cho tất cả L3-L4 events via error → correction → repetition)
- [../Agent/By-Product-Gap-Resonance.md](../Agent/By-Product-Gap-Resonance.md) — H9 Resonance (anchors E9/E10/E12/E26 social events)
- [../Agent/Self-Pattern-Modeling.md](../Agent/Self-Pattern-Modeling.md) — H9 Self-Pattern-Modeling (anchors E21-E31 self chunks)
- [../Body-Feedback-Draft/01-Foundation.md](../Body-Feedback-Draft/01-Foundation.md) — H10 P2 mechanism (cross-link với 06a §6)

---

## §10 — Status

✅ **DRILLED + TRANSLATED — N+4c2 → Vietnamese (2026-04-16)** — File 09/12 F1 Child-Chunk-Development.

**Deliverables**:
- ⭐ **Master event matrix**: ~80 events qua 7 body-input arcs được tổ chức thành 7 sub-tables (§2.1-§2.7)
- Cross-reference table (§2.8) — 14 events spanning 2-3 arc files
- Ladder distribution analysis (§3) — counts + 10-marker L2 catalog + L0/L4 catalogs + valence taxonomy refinement
- Nút Thắt coverage table (§4) — **tất cả 7 Nút Thắt đều có primary verdicts committed** trước 10
- Compile mechanism distribution (§5) — 4 mechanisms + 2 secondary + per-arc profiles
- Non-uniform ladder progression synthesis (§6) — 5-parameter modulator model + prediction fit
- 23 open questions tổng hợp (§7)
- 10 R-F1-* preliminary recommendations (§8)

**File tiếp theo**: [10-F1-Synthesis.md](10-F1-Synthesis.md) ⭐ — 7 Nút Thắt final verdicts + H1 + H11 + Ladder framework contribution + R-F1-1 through R-F1-10 recommendations + output contracts cho F3/F4/99-Master/Feeling L3.

**Không cần mandatory review stop** per NEXT-DIRECTIONS — 09 là aggregation, không phải new claims. Tiếp tục sang 10 drill.

---

**Kết thúc 09-Event-Chunks-Inference-Matrix-VI.md (N+4c2 drill → Vietnamese translation).**




