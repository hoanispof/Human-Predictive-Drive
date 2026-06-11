---
title: Domain — Thực Tế Bên Ngoài Human
version: 2.0
created: 2026-03-30 (v1.0 DRAFT)
rewritten: 2026-05-24 (v2.0 — FULL REWRITE: +3 Domain Types, +Dual Check, +Gap System, +Compiled/Fresh, +Satiation, +Simulation-Engine, +Entity-Access. Tích hợp hữu cơ)
previous: v1.0 → backup/Domain-v1.0-backup.md
status: v2.0 REFERENCE FILE
scope: |
  Domain = thực tế bên ngoài human. File này KHÔNG mô tả domain trực tiếp —
  mô tả những gì CHẮC CHẮN BIẾT qua phản chiếu từ human interaction.
  3 Domain Types: Reality / Abstract / Abstract-Dynamic.
  3 Nguồn Constraint: Physics / Hardware / Collective → shelf-life khác nhau.
  Dual Check: body = quality controller, domain = final arbiter.
  Lean epistemological stance: infer domain through reflection.
parent: Core-Deep-Dive/Domain/
dependencies:
  core:
    - Conflict-Dynamics.md v2.0 — OVERLAP x SCARCITY x COMMITMENT
    - Domain-Mapping-Drive.md v2.0 — WHY humans drive to map domain
    - Knowledge-Flow.md v1.0 — knowledge flow between mapped regions
    - Discovery-vs-Expansion.md v1.0 — Sense-Verify-Scale pipeline
  pfc:
    - Imagine-Final.md v3.0 — constructive simulation, bridge body x domain
    - Simulation-Engine.md v1.0 — 1 engine, 3 components, domain simulation
    - PFC-Operations.md v1.0 — Compiled/Fresh spectrum, PFC Budget
  body-base:
    - Body-Feedback-Mechanism.md v2.0 — body check = domain feedback mechanism
    - Gap-Direction.md v2.0 — gap direction, "chưa biết = không có gap"
    - Gap-Body-Need.md v1.0 — 3 Satiation types (Cyclic/Tonic/Generative)
    - Gap-Distribution-Profile.md v1.1 — PFC Budget limits domain mapping
  agent:
    - Entity-Access.md v1.2 — per-entity domain access gradient Mức 0-5
  collective:
    - Collective-Arc-Dynamics.md v1.2 — shelf-life × 3 nguồn constraint
    - Collective-Purpose.md v1.2 — cosmic loop, vertical knowledge mapping
  application:
    - Ask-AI.md v3.1 — Dual Check protocol (body + domain reality)
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Domain — Thực Tế Bên Ngoài Human

> **Bạn KHÔNG THỂ nhìn thấy gió.**
> Nhưng bạn thấy lá bay, cây lay, sóng gợn → bạn BIẾT có gió.
>
> Domain cũng vậy.
> Chúng ta KHÔNG THỂ mô tả domain trực tiếp — nó vô tận, lớn hơn mọi mô tả.
> Nhưng chúng ta thấy BÓNG CỦA NÓ phản chiếu qua cách human tương tác:
> feedback thật, knowledge convergence, combination khả thi.
>
> 3 loại domain. 8 đặc điểm chắc chắn. 3 nguồn constraint.
> Và 1 nguyên tắc kiểm chứng: body check + domain reality.

---

## Mục lục

- §0 — VỊ TRÍ + SCOPE
- §1 — EPISTEMOLOGY: PHẢN CHIẾU, KHÔNG NHÌN TRỰC TIẾP
- §2 — 3 DOMAIN TYPES (Reality / Abstract / Abstract-Dynamic)
- §3 — 8 ĐẶC ĐIỂM CHẮC CHẮN — PHẢN CHIẾU TỪ FRAMEWORK
- §4 — 3 NGUỒN CONSTRAINT × DOMAIN TYPES
- §5 — DUAL CHECK: Body = Quality Controller, Domain = Final Arbiter
- §6 — DOMAIN × FRAMEWORK CONCEPTS
- §7 — HONEST ASSESSMENT
- §8 — CÂU HỎI MỞ
- §9 — KẾT NỐI

---

## §0 — VỊ TRÍ + SCOPE

```
⭐ FILE NÀY TRONG FRAMEWORK:

  Core-Deep-Dive/Domain/ — DEFINITION FILE.

  PHÂN BIỆT VỚI CÁC FILE GẦN:

    ┌───────────────────────────────┬────────────────────────────────────────┐
    │ File                          │ Trả lời                                │
    ├───────────────────────────────┼────────────────────────────────────────┤
    │ Domain.md (FILE NÀY)          │ WHAT = domain là gì, 3 types, 8 đặc   │
    │                               │ điểm, 3 nguồn constraint, Dual Check   │
    ├───────────────────────────────┼────────────────────────────────────────┤
    │ Domain-Mapping-Drive.md v2.0  │ WHY = tại sao human drive to map       │
    │                               │ "Có sẵn mà không pleasant" = modern    │
    │                               │ paradox → mapping drive mechanism       │
    ├───────────────────────────────┼────────────────────────────────────────┤
    │ Conflict-Dynamics.md v2.0     │ WHEN = xung đột khi OVERLAP ×          │
    │                               │ SCARCITY × COMMITMENT                  │
    ├───────────────────────────────┼────────────────────────────────────────┤
    │ Knowledge-Flow.md v1.0        │ HOW = knowledge chảy giữa mapped       │
    │                               │ regions (internal → output → external) │
    ├───────────────────────────────┼────────────────────────────────────────┤
    │ Discovery-vs-Expansion v1.0   │ HOW = Sense → Verify → Scale pipeline  │
    ├───────────────────────────────┼────────────────────────────────────────┤
    │ Collective-Arc-Dynamics v1.2  │ WHY = patterns expire differently      │
    │                               │ (shelf-life × constraint source)       │
    └───────────────────────────────┴────────────────────────────────────────┘

  FILE NÀY:
    → ĐỊNH NGHĨA domain = gì
    → PHÂN LOẠI 3 domain types
    → GOM 8 đặc điểm BIẾT CHẮC qua phản chiếu
    → TÍCH HỢP 3-nguồn constraint × domain types
    → THIẾT LẬP Dual Check principle
    → KẾT NỐI domain × framework concepts

  FILE NÀY KHÔNG:
    → Giải thích TẠI SAO map domain (→ Domain-Mapping-Drive.md)
    → Phân tích cơ chế xung đột (→ Conflict-Dynamics.md)
    → Mô tả domain mapping pipeline (→ Discovery-vs-Expansion.md)
```

---

## §1 — EPISTEMOLOGY: Phản Chiếu, Không Nhìn Trực Tiếp

```
⭐ CON NGƯỜI KHÔNG TIẾP XÚC DOMAIN TRỰC TIẾP:

  Não KHÔNG chạm domain → Body chạm (mắt, tai, tay, da,...) → Body feedback → Não biết
  → Body = GIAO DIỆN DUY NHẤT giữa human và domain
  → Mọi thứ não "biết" về domain = FRAGMENTS qua body


  VẬY LÀM SAO BIẾT DOMAIN CÓ ĐẶC ĐIỂM GÌ?

  CÁCH 1 — Feedback thật:
    → Nhảy xuống → ngã → ĐAU → gravity CÓ THẬT
    → Chạm lửa → bỏng → nhiệt CÓ THẬT
    → Domain TRẢ LỜI khi body interact → feedback = "bóng" của domain

  CÁCH 2 — Knowledge convergence (nhiều systems map cùng pattern):
    → Não (PFC + VTA + unconscious), công ty (giám đốc + thư ký + nhân viên),
      quân đội (tổng tư lệnh + phó tướng + quân lính)
      → 3 hệ thống KHÁC NHAU → CÙNG pattern "leader + filter + workers"
    → Nhiều hệ thống KHÁC NHAU tụ về CÙNG pattern qua shared constraints
    → Framework lean epistemological: "knowledge convergence"
      (observation level — KHÔNG claim "attractor IN domain")

  CÁCH 3 — Combination hoạt động:
    → Hydrocarbon cháy được (chemistry) + khí nở đẩy piston (physics)
      → 2 tính chất này đã TỒN TẠI trước khi ai nghĩ tới "động cơ"
      → Con người TÌM RA 2 tính chất → NỐI lại → động cơ đốt trong
    → Con người TÌM RA combination, không TẠO RA tính chất → domain ĐÃ cho phép từ trước
    → Combination thành công = "bóng" của domain structure


  → Chúng ta KHÔNG nhìn domain → nhìn BÓNG CỦA domain qua human
  → Mỗi đặc điểm dưới đây = 1 "bóng" chắc chắn thấy

  🟢 Epistemological framing: consistent với Kant (phenomena, not noumena)
  🟡 "3 cách biết" = framework synthesis from research consensus
```

---

## §2 — 3 DOMAIN TYPES

```
⭐ DOMAIN KHÔNG ĐỒNG NHẤT — 3 loại domain, 3 cơ chế feedback:


  ① REALITY DOMAIN — vật lý, sinh học, hóa học, địa chất:

    Đặc điểm:
      → Tồn tại TRƯỚC con người, VẪN TỒN TẠI sau con người tuyệt chủng
      → Feedback tức thì, objective, KHÔNG PHỤ THUỘC observer
      → Con người PHÁT HIỆN, không TẠO RA (gravity đã có trước Newton)
      → KHÔNG thay đổi theo participants

    Feedback mechanism:
      → Body chạm trực tiếp → nhận feedback thật
      → Rơi → đau. Chạm lửa → bỏng. Uống nước → hết khát.
      → Domain TRẢ LỜI unconditionally

    Shelf-life: patterns map Reality Domain → ≈ ∞
    VD: gravity, entropy, thermodynamics, biology, chemistry


  ② ABSTRACT DOMAIN — toán, logic, formal systems:

    Đặc điểm:
      → KHÔNG CÓ physical substrate trực tiếp
      → Con người PHÁT HIỆN, không TẠO RA (mathematical truths exist independently)
        → 🟡 Platonism vs Formalism debate — framework lean "discovered"
            nhưng không commit mạnh (câu hỏi mở DM-6)
      → Internal consistency = verification mechanism
      → KHÔNG thay đổi theo participants

    Feedback mechanism:
      → KHÔNG có body feedback trực tiếp (không "đau" khi sai toán)
      → Verify qua LOGICAL CONSISTENCY — proof, derivation, peer review
      → Body feedback GIÁN TIẾP: coherence (smooth → pleasant,
        inconsistency → dissonance)

    Shelf-life: patterns map Abstract Domain → ≈ ∞
    VD: mathematics, formal logic, set theory, number theory


  ③ ABSTRACT-DYNAMIC DOMAIN — xã hội, thị trường, văn hóa, ngôn ngữ:

    Đặc điểm:
      → Abstract (không có physical substrate cố định)
      → DYNAMIC — THAY ĐỔI theo participants (collective arc shift)
      → Con người VỪA phát hiện VỪA tạo ra (market rules = human construct)
      → ⚠️ "Behaves like domain" cho cá nhân — vi phạm → bị phạt THẬT

    Feedback mechanism:
      → Body feedback THẬT cho individual — bị sa thải = ĐAU THẬT
      → NHƯNG: feedback CÓ THỂ SHIFT (rules thay đổi → feedback thay đổi)
      → Bị kết án oan → hậu quả ĐAU THẬT (collective = real constraint)
      → Scale >> individual → cá nhân KHÔNG THỂ đơn phương thay đổi

    Shelf-life: LIMITED = f(tốc độ collective shift)
      → "Bằng ĐH → việc tốt" = ĐANG expire
      → Chi tiết: Collective-Arc-Dynamics.md v1.2
    VD: markets, law, culture, social norms, trends, language


  ⭐ TẠI SAO PHÂN LOẠI NÀY QUAN TRỌNG:

    ┌──────────────────┬────────────┬────────────┬────────────────┐
    │                  │ Reality    │ Abstract   │ Abstract-      │
    │                  │            │            │ Dynamic        │
    ├──────────────────┼────────────┼────────────┼────────────────┤
    │ Feedback         │ Body trực  │ Logic      │ Body THẬT      │
    │                  │ tiếp       │ consistency│ nhưng CAN SHIFT│
    ├──────────────────┼────────────┼────────────┼────────────────┤
    │ Thay đổi theo    │ Không      │ Không      │ Có             │
    │ participants?    │            │            │                │
    ├──────────────────┼────────────┼────────────┼────────────────┤
    │ Shelf-life       │ ∞          │ ∞          │ LIMITED        │
    ├──────────────────┼────────────┼────────────┼────────────────┤
    │ Con người        │ Phát hiện  │ Phát hiện  │ Phát hiện +    │
    │                  │            │            │ Tạo ra         │
    ├──────────────────┼────────────┼────────────┼────────────────┤
    │ Nguồn constraint │ Physics    │ Internal   │ Collective     │
    │ chính            │            │ logic (*)  │                │
    └──────────────────┴────────────┴────────────┴────────────────┘
    (*) Abstract Domain constraint source: debated (DM-6)

    → Cá nhân bên TRONG cả 3 domain types → body register GIỐNG NHAU
    → Phân biệt = META-LEVEL observation, không phải individual experience
    → Chi tiết tại sao individual không phân biệt: §4

  🟢 Reality vs Abstract distinction: philosophy of science
  🟡 Abstract-Dynamic = framework classification (original contribution)
  🟡 "Con người phát hiện" Abstract Domain: Platonism — debated (DM-6)
```

---

## §3 — 8 Đặc Điểm Chắc Chắn — Phản Chiếu Từ Framework

```
⭐ 8 ĐẶC ĐIỂM — mỗi cái BIẾT CHẮC qua phản chiếu:


  ① TỒN TẠI + KHÔNG PHỤ THUỘC HUMAN:
    → Gravity kéo dù ai biết hay không. Virus lây dù ai tin hay không.
    → Trước con người → domain ĐÃ CÓ. Sau tuyệt chủng → VẪN CÒN.
    → Áp dụng chủ yếu Reality + Abstract Domain.
    → Abstract-Dynamic: tồn tại CHỈ KHI có participants → khác.
    🟢 Physical reality independent of observation (physics consensus)


  ② VÔ TẬN TỔNG THỂ:
    → 86 tỷ neurons chỉ chứa FRAGMENTS. Mọi kiến thức = PHẦN CỰC NHỎ.
    → Mỗi thế kỷ phát hiện thêm → VẪN CHƯA HẾT.
    → "Chưa biết = không có gap" (Gap-Direction.md v2.0) →
      phần chưa map = INVISIBLE cho individual (§6.1)
    🟡 Inference from ongoing discovery (consistent with history of science)


  ③ FINITE TẠI MỖI ĐIỂM:
    → 1 miếng đất: chỉ 1 người dùng. 1 vị trí: chỉ 1 người ngồi.
    → = GỐC xung đột VÀ engine mở rộng:
      Finite + overlap → conflict (Conflict-Dynamics.md v2.0 §1)
      Finite + scarcity → exploration → expansion (Conflict-Dynamics.md v2.0 §7)
    🟢 Resource scarcity → conflict + innovation (economics consensus)


  ④ KNOWLEDGE CONVERGENCE:
    → Nhiều hệ thống KHÁC NHAU map về CÙNG pattern qua shared constraints
    → Não, công ty, quân đội → "leader + filter + workers"
    → 2 interpretations (operationally tương đương):
      A — Strong (ontological): "Domain CÓ attractor" → claim vượt observation
      B — Weak (epistemological): "Knowledge converge qua shared constraints"
    → Framework lean B — consistent §1: không nhìn domain trực tiếp
    → Vẫn dùng "attractor" như shorthand — hiểu là convergence pattern
    → Cross-domain insight = phát hiện 2 knowledge mappings CÙNG converge
    🟢 Convergent evolution supports pattern (Conway Morris 2003)
    🟡 "Lean B" = framework epistemological position


  ⑤ CHO PHÉP COMBINATION:
    → 2 vùng map NỐI → emerge vùng mới
    → Dầu + Máy = Công nghiệp. Silicon + Logic = Computing.
    → C LUÔN khả thi trong domain → cần map A + B trước mới THẤY C
    → "Domain mới" = KHÔNG xuất hiện từ hư không → luôn ở đó, mới TÌM RA
    → PFC simulate combination TRƯỚC khi thử (Simulation-Engine — §6.4)
    🟢 Combinatorial innovation (Arthur 2009 "The Nature of Technology")


  ⑥ FEEDBACK THẬT (domain không nói dối):
    → Body check → kết quả KHÔNG PHỤ THUỘC ý muốn
    → Domain = NGUỒN SỰ THẬT duy nhất → không thể bẻ cong
    → ⚠️ NHƯNG: body interpret feedback CÓ THỂ SAI
      → Domain feedback thật → body nhận → PFC giải thích → CÓ THỂ sai
      → "Sai" nằm ở HUMAN interpretation, không nằm ở domain
    → Dual Check: body check coherence, domain check truth (§5)
    🟢 Domain feedback independent of human desire (physics consensus)


  ⑦ CHỈ MAP ĐƯỢC DẦN (incremental, không nhảy):
    → Base → shift nhẹ → body check → accept/reject → base mới → tiếp
    → KHÔNG THỂ nhảy A → Z (quá xa = body không evaluate được)
    → Universal: evolution, science, market, AI training → CÙNG cơ chế
    → Compiled domain knowledge = base cho Fresh exploration tiếp (§6.2)
    🟢 Incremental learning: gradient descent, evolution, scientific method


  ⑧ EXPANSION TĂNG TỐC:
    → 1 vùng → 0 combination. 10 vùng → 45. 100 vùng → 4,950.
    → Tốc độ = n(n-1)/2 → tăng theo hàm mũ
    → 10,000 năm đầu = chậm → 100 năm gần = CỰC NHANH
    → Không phải human "giỏi hơn" → CÓ NHIỀU VÙNG ĐÃ MAP hơn
    🟢 Accelerating returns (Kurzweil 2005) — simplified model, data-consistent
```

---

## §4 — 3 Nguồn Constraint × Domain Types

```
⭐ 3 NGUỒN CONSTRAINT — phân biệt TẠI SAO patterns có shelf-life KHÁC NHAU:


  ① PHYSICS (vĩnh viễn, không phụ thuộc human):
    → Gravity, entropy, thermodynamics, chemistry, mathematical structure
    → Trước loài người = có. Sau tuyệt chủng = VẪN CÓ.
    → Feedback: absolute, unconditional
    → UNDERLIES: Reality Domain + Abstract Domain
    → Compiled patterns khớp physics: shelf-life ≈ ∞


  ② BODY HARDWARE (~100K year evolution, stable within lifetime):
    → PFC bandwidth 4±1, opioid/dopamine reward, sensory systems, needs
    → = HỆ ĐIỀU HÀNH cho patterns hoạt động + tương tác domain
    → CONSTRAINT CHUNG mọi domain type — body hardware GIỚI HẠN:
      HOW MUCH domain map được (PFC Budget — PFC-Operations.md v1.0)
      HOW FAST domain map được (incremental only — §3 ⑦)
      WHAT COUNTS as reward (Gap-Body-Need.md v1.0 — Satiation types)
    → Chết → trở về physics. Hackable by chemicals.
    → Compiled patterns khớp hardware: shelf-life ≈ ∞ trong 1 đời


  ③ COLLECTIVE (emergent từ nhiều body tương tác):
    → Market, law, culture, norms, trends, language, technology
    → Real constraints: vi phạm → bị phạt/loại THẬT
    → NHƯNG: CAN SHIFT (participants thay đổi → rules thay đổi)
    → Scale >> individual → cá nhân KHÔNG THỂ đơn phương thay đổi
    → TẠO RA: Abstract-Dynamic Domain (§2 ③)
    → Compiled patterns khớp collective: shelf-life = LIMITED
      = f(tốc độ collective shift — Collective-Arc-Dynamics.md v1.2)


  ⭐ TẠI SAO CÁ NHÂN KHÔNG PHÂN BIỆT:

    Body CHỈ CÓ 1 feedback system: hành động → kết quả → reward/pain.
    KHÔNG CÓ sensor riêng cho "đây là physics" vs "đây là collective."

    Rơi từ cao = đau (physics)
    Bị sa thải = đau (collective)
    Bị bỏ tù oan = đau (collective, SAI nhưng VẪN ĐAU THẬT)

    → Body register TẤT CẢ giống nhau → compile patterns giống nhau
    → Mỗi body ĐÃ nằm trong collective → collective = "domain" cho body
    → Phân biệt = META-LEVEL (framework, science) — KHÔNG phải cá nhân
    → Chi tiết deep analysis: Collective-Arc-Dynamics.md v1.2 §1-§3


  ⭐ SHELF-LIFE TABLE:

    ┌────────────────┬──────────────┬───────────────────────────────────┐
    │ Nguồn          │ Shelf-life   │ Ví dụ                             │
    ├────────────────┼──────────────┼───────────────────────────────────┤
    │ Physics        │ ≈ ∞          │ 2+2=4, gravity, entropy           │
    ├────────────────┼──────────────┼───────────────────────────────────┤
    │ Body hardware  │ ≈ ∞ / 1 đời │ PFC bandwidth, opioid reward      │
    ├────────────────┼──────────────┼───────────────────────────────────┤
    │ Collective     │ LIMITED      │ "Bằng ĐH → việc tốt" (expiring)  │
    │                │ = f(shift)   │ "SEO strategy" (expires nhanh)    │
    └────────────────┴──────────────┴───────────────────────────────────┘

  🟡 3 nguồn distinction = framework precision
     (consistent Logic-Feeling.md v4.0 §3.2 + Collective-Arc-Dynamics v1.2)
  🟡 "Individual không phân biệt" = body architecture observation
```

---

## §5 — DUAL CHECK: Body = Quality Controller, Domain = Final Arbiter

```
⭐ NGUYÊN TẮC KIỂM CHỨNG — 2 BƯỚC, KHÔNG CHỈ 1:


  BƯỚC 1 — BODY CHECK (quality controller):

    → Body cảm giác thế nào? Schema smooth hay resistance?
    → Coherence check: "thông tin này fit với chunks đã compiled?"
    → Nhanh, tự động, ~90% reliable (Body-Base.md v3.2 §7)
    → NHƯNG: đánh giá COHERENCE, không phải TRUTH
    → 3 failure modes:
      ① Evolution lag — hardware chưa cập nhật reality mới
      ② Chunks nền sai — compiled patterns chứa sai lệch
      ③ Schema override — schema ép body accept qua PFC


  BƯỚC 2 — DOMAIN CHECK (final arbiter):

    → Dữ liệu thực tế, kết quả THẬT, evidence
    → Domain feedback LUÔN ĐẾN — chỉ là sớm hay muộn
    → KHÔNG bị amplify, smooth, hay schema override
    → Domain feedback ≠ body interpretation (§3 ⑥)


  ⭐ 4 TRƯỜNG HỢP:

    Body YES + Domain YES → ✅ HIGH confidence (cả 2 align)
    Body NO  + Domain YES → 🔍 Investigate (body resist incoherent-but-true?)
    Body YES + Domain NO  → ⚠️ NGUY HIỂM — likely smoothing / amplification
    Body NO  + Domain NO  → ❌ Clear rejection

    Body YES + Domain NO = NGUY HIỂM NHẤT:
      → Body feel coherent → confident → NHƯNG domain VẪN NO
      → Delay crash → crash LỚN HƠN
      → AI có thể amplify risk này (Ask-AI.md v3.1 §6.1):
        AI confirm → body coherence TĂNG → body YES mạnh hơn
        → domain reality KHÔNG thay đổi → gap coherence↔truth LỚN HƠN


  ⭐ DOMAIN TYPES × DUAL CHECK:

    Reality Domain: domain check = TRỰC TIẾP (thử → thấy → biết)
    Abstract Domain: domain check = LOGICAL (proof, derivation, peer review)
    Abstract-Dynamic: domain check = PHỨC TẠP
      → Rules CAN shift → cần time + exposure + cross-validation
      → Chi tiết: Collective-Arc-Dynamics.md v1.2

  🟡 Dual Check = framework principle (chi tiết Ask-AI.md v3.1 §6.1)
  🟢 Body coherence ≠ truth: cognitive bias research (Kahneman 2011)
```

---

## §6 — DOMAIN × FRAMEWORK CONCEPTS

### §6.1 — Gap System × Domain

```
⭐ "CHƯA BIẾT = KHÔNG CÓ GAP" (Gap-Direction.md v2.0):

  Gap = hole trong chunk network. Gap có HƯỚNG = f(surrounding chunks).
  Không có chunks xung quanh = không có bờ = không có hole = KHÔNG CÓ GAP.

  Domain implications:
    → Phần domain CHƯA MAP = INVISIBLE cho individual
    → Bạn KHÔNG THỂ thiếu thứ bạn không biết tồn tại
    → Exposure = PREREQUISITE cho domain mapping
      (tạo chunks bờ → gap xuất hiện → drive to fill)
    → "Chưa biết" KHÁC "biết mà chưa hiểu":
      "Chưa biết" = no gap, no drive
      "Biết mà chưa hiểu" = gap exists, drive active

  → §3 ② (vô tận tổng thể): phần vô tận chưa map = NO GAP = no drive
  → Chi tiết: Gap-Direction.md v2.0 §1-§3

  🟡 Framework principle (consistent Schultz 1997 prediction-delta)
```

### §6.2 — Compiled/Fresh × Domain

```
⭐ DOMAIN KNOWLEDGE CÓ 2 CHẾ ĐỘ XỬ LÝ (PFC-Operations.md v1.0):

  COMPILED domain knowledge (Hardware-Stream):
    → Expert: compiled maps → nhận diện patterns nhanh, tự động
    → Ưu: fast, energy-efficient, reliable trong stable domain
    → Nhược: có thể miss novel patterns (compiled = nhìn qua lens cũ)
    → Phù hợp: Reality + Abstract Domain (stable → compiled quality cao)

  FRESH domain exploration (Modeling-Stream):
    → Beginner hoặc expert ở domain mới: chậm, tốn PFC Budget
    → Ưu: thấy patterns MỚI mà compiled eyes bỏ qua
    → Nhược: slow, tốn energy, sai nhiều
    → Phù hợp: Abstract-Dynamic Domain (shifting → cần fresh thường xuyên)

  Compiled Quality Dimension:
    → Genuine-compiled: body confirmed qua domain feedback → reliable
    → Schema-compiled: PFC-driven, chưa domain verify → risky
    → Threat-compiled: bị ép (collective/authority) → shelf-life uncertain

  → §3 ⑦ = Compiled base → Fresh exploration → Compiled mới
  → Expert blind spot: compiled TOO deep → resist fresh patterns ở domain shift
  → Chi tiết: PFC-Operations.md v1.0 §1-§5

  🟡 Framework application of Compiled/Fresh to domain mapping
```

### §6.3 — Satiation × Domain

```
⭐ 3 LOẠI SATIATION × DOMAIN (Gap-Body-Need.md v1.0):

  CYCLIC satiation (ăn → no → đói → ăn):
    → Domain resources: food, water, sleep, temperature
    → Reality Domain feedback tức thì, cycle predictable
    → Technology fill: agriculture, water system → GIẢI QUYẾT phần lớn

  TONIC satiation (baseline cần duy trì liên tục):
    → Domain stability: safety, shelter, predictability
    → Reality + Abstract-Dynamic → mixed feedback
    → Technology fill: partial (housing yes, social stability harder)

  GENERATIVE satiation (mapping → more mapping → never fully satiates):
    → Domain knowledge: mastery, discovery, understanding
    → ACROSS all domain types → mỗi map MỚI open MORE combinations (§3 ⑧)
    → Technology fill: accelerates (AI × domain mapping — DM-4)
    → = Domain-Mapping-Drive mechanism (Domain-Mapping-Drive.md v2.0)

  → Cyclic + Tonic: phần lớn Reality Domain, technology CAN fill
  → Generative: spans ALL domains, NEVER fully fill → engine vĩnh cửu

  🟡 3 Satiation types × domain = framework application
```

### §6.4 — Simulation-Engine × Domain

```
⭐ PFC SIMULATE DOMAIN QUA 1 ENGINE (Simulation-Engine.md v1.0):

  Simulation-Engine = MACHINERY cho domain access qua PFC:
    → PFC simulate "nếu tôi làm X → domain trả lời Y" → body evaluate
    → = Human's primary domain EXPLORATION tool (vượt direct body check)
    → Cho phép map domain TRƯỚC KHI body chạm (preview, planning)

  Domain simulation quality = f(compiled chunk quality × PFC Budget):
    → Expert: compiled chunks → simulate CHÍNH XÁC hơn
    → Beginner: ít chunks → simulate THÔ hơn
    → PFC Budget finite → phải CHỌN domain nào simulate
      (Gap-Distribution-Profile.md v1.1)

  → §3 ⑤ (combination) × Simulation-Engine:
    PFC simulate "NẾU nối A + B → C?" → body preview → thử → domain confirm
    → Tại sao con người map domain NHANH hơn mọi loài (PFC size)

  🟡 Simulation-Engine × domain = framework formalization
```

### §6.5 — Entity-Access × Domain

```
⭐ MỖI ENTITY = 1 "CỬA SỔ" VÀO DOMAIN (Entity-Access.md v1.2):

  Domain access = per-entity phenomenon:
    → Mỗi entity = 1 agent qua đó individual tiếp cận domain KHÁC NHAU
    → Entity-Access gradient: Mức 0 (stranger) → Mức 5 (excess)
    → Mức cao (self, close) → deep domain access (know body-state)
    → Mức thấp (stranger) → shallow (guess via compiled patterns)

  → §3 ④ (knowledge convergence):
    Nhiều entities access CÙNG domain region → report consistent patterns
    → Cross-validation → domain REAL

  → Entity-Access KHÁC per domain type:
    Reality Domain → entity-access ít relevant (gravity applies to everyone)
    Abstract-Dynamic → entity-access CỰC relevant
    (mỗi entity = 1 "cửa sổ" vào social landscape, market, culture)

  🟡 Entity-Access × domain = framework application
```

---

## §7 — HONEST ASSESSMENT

```
ESTABLISHED (🟢):
  🟢 Physical reality exists independently of observation
     (physics consensus — dù quantum interpretation debated)
  🟢 Convergent evolution: same constraints → same solutions
     across unrelated species (Conway Morris 2003)
  🟢 Combinatorial innovation: recombination of existing ideas
     (Arthur 2009 "The Nature of Technology")
  🟢 Accelerating returns: innovation rate increases over time
     (Kurzweil 2005 — simplified model, data-consistent)
  🟢 Resource scarcity drives innovation (economic history consensus)
  🟢 Body coherence ≠ truth (Kahneman 2011 — cognitive bias research)
  🟢 Incremental learning: gradient descent, evolution, scientific method


FRAMEWORK SYNTHESIS (🟡):
  🟡 "Nhìn domain qua phản chiếu": consistent Kant (phenomena, not noumena)
  🟡 3 Domain Types (Reality/Abstract/Abstract-Dynamic):
     Reality vs Abstract = philosophy of science.
     Abstract-Dynamic = original framework classification.
  🟡 3 nguồn constraint × shelf-life: framework precision.
     Consistent Logic-Feeling v2.1 §1.3b + Collective-Arc-Dynamics v1.2.
  🟡 Dual Check principle: framework application.
     Body = quality controller. Domain = final arbiter.
  🟡 Gap system × domain ("chưa biết = không có gap"): framework principle.
  🟡 Compiled/Fresh × domain: framework application of learning theory.
  🟡 3 Satiation types × domain: framework classification.
  🟡 Simulation-Engine × domain: framework formalization.
  🟡 Entity-Access × domain: framework application.
  🟡 "Individual không phân biệt 3 nguồn": body architecture observation.
  🟡 Knowledge convergence (refined): lean epistemological (Kant-consistent).


HYPOTHESIS (🔴):
  🔴 "Domain không thay đổi, chỉ human map thêm" — strong claim.
     Quantum mechanics gợi ý observer CÓ THỂ ảnh hưởng domain (DM-1).
  🔴 "8 đặc điểm = đầy đủ" — chắc chắn CHƯA đầy đủ.
     Domain vô tận → luôn có đặc điểm chưa phát hiện (DM-7).
  🔴 "Abstract Domain = discovered, not created" — Platonism debate (DM-6).
  🔴 "Scarcity = engine" — chỉ đúng khi agent CÓ KHẢ NĂNG expand
     (PFC, exposure, freedom — Conflict-Dynamics.md v2.0 §7).
```

---

## §8 — CÂU HỎI MỞ

```
DM-1: Domain có THAY ĐỔI không? Hay chỉ human map thêm?
      → Quantum: observer affect? Universe expand? Laws change?

DM-2: Knowledge convergence — finite hay infinite patterns?
      → Epistemological: bao nhiêu shared constraints khả thi?

DM-3: Combination potential n(n-1)/2 — chính xác hay simplified?
      → Có combinations domain constraint block?

DM-4: AI × domain: AI map domain NHANH HƠN human → implications?
      → AI tìm combination human KHÔNG THỂ thấy (quá xa cho PFC)?
      → AI × Generative satiation: accelerate hay replace human mapping?

DM-5: Digital domain: "domain mới" hay "extension"?
      → Internet, virtual worlds = domain thật hay human construct?

DM-6: Abstract Domain = "discovered" (Platonism) hay "created" (Formalism)?
      → Framework lean "discovered" nhưng chưa commit mạnh.
      → Impact: nếu "created" → Abstract ≈ Abstract-Dynamic?

DM-7: 8 đặc điểm hiện tại = đầy đủ?
      → Chắc chắn chưa. Đặc điểm nào TIẾP THEO cần formalize?
```

---

## §9 — KẾT NỐI

```
DOMAIN/ FOLDER:
  → Domain-Mapping-Drive.md v2.0 — WHY humans drive to map domain
  → Conflict-Dynamics.md v2.0 — WHEN domain causes conflict (OVERLAP x SCARCITY x COMMITMENT)
  → Knowledge-Flow.md v1.0 — HOW knowledge flows between mapped regions
  → Discovery-vs-Expansion.md v1.0 — HOW domain knowledge spreads (Sense-Verify-Scale)
  → Drill-Emergent-Pattern.md v2.0 — WHERE patterns emerge in domain

CORE MECHANISM:
  → Body-Feedback-Mechanism.md v2.0 — body check = domain feedback mechanism
  → Simulation-Engine.md v1.0 — domain simulation via 1 engine, 3 components
  → PFC-Operations.md v1.0 — Compiled/Fresh spectrum, PFC Budget, Hold/Suppress
  → Entity-Access.md v1.2 — per-entity domain access gradient Mức 0-5

BODY-BASE:
  → Gap-Direction.md v2.0 — "chưa biết = không có gap", gap direction
  → Gap-Body-Need.md v1.0 — 3 Satiation types (Cyclic/Tonic/Generative) × domain
  → Gap-Distribution-Profile.md v1.1 — PFC Budget limits domain mapping
  → Valence-Propagation.md v3.0 — body evaluation, structural/current valence

COLLECTIVE:
  → Collective-Arc-Dynamics.md v1.2 — shelf-life × 3 nguồn constraint (DEEP)
  → Collective-Purpose.md v1.2 — cosmic loop, vertical knowledge mapping
  → Collective-Body.md v2.1 — Model 3 cấp, trust bridge, coupling proxy

APPLICATION:
  → Ask-AI.md v3.1 — Dual Check protocol (body + domain reality)
  → Imagine-Final.md v3.0 — bridge body × domain (constructive simulation)
  → Self-Pattern-Modeling.md v3.1 — per-agent domain access quality

RESEARCH:
  → Conway Morris 2003 — convergent evolution
  → Arthur 2009 — The Nature of Technology (combinatorial innovation)
  → Kurzweil 2005 — accelerating returns
  → Kahneman 2011 — cognitive biases (body coherence ≠ truth)
  → Kant 1781 — Critique of Pure Reason (phenomena, not noumena)
  → Schultz 1997 — prediction-delta (VTA dopamine)
  → Seligman 2013 — prospection theory
```

---

> *Domain — "Chúng ta không thể nhìn gió. Nhưng thấy lá bay → biết có gió.
> Domain cũng vậy — vô tận, không mô tả được trực tiếp.
> 3 loại: vật lý (vĩnh viễn), trừu tượng (vĩnh viễn), xã hội (thay đổi).
> Body check = quality controller, domain = final arbiter.
> 'Chưa biết = không có gap' — phần chưa map = invisible.
> 8 tỉ melody × domain vô tận = map mãi không hết. Và đó là điều ĐẸP."*
