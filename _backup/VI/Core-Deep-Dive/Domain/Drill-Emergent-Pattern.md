---
title: Emergent Patterns — Khi Domain Interaction Lặp Lại
version: 2.0
created: 2026-04-12
rewritten: 2026-05-24 (v2.0 — THU GỌN: ~60% superseded → cross-ref. Enemy + Nurturing + "Cho đi" + Violation KEPT + v7.8 aligned)
previous_versions:
  - v1.2 (2026-05-23, ~1,302L) → backup/Emergent-Patterns-v1.2-backup.md
status: v2.0 REFERENCE FILE
scope: |
  EMERGENT PATTERNS từ domain interaction LẶP LẠI:
  Enemy/Threat, Nurturing, "Cho đi", Violation & Recovery.
  v2.0 THU GỌN: ~60% content v1.2 superseded bởi file chuyên sâu:
    Dependency → Entity-Access v1.2 + Entity-Access-Excess v1.0
    Mixed Valence → Valence-Propagation v3.0
    Group Dynamics → Collective/ folder (5 files) + By-Product-Scale v1.0
  v2.0 CÒN LẠI = unique content KHÔNG CÓ ở file nào khác:
    ① Enemy pattern + dehumanization + schema inheritance
    ② Nurturing 4-factor model + baby schema
    ③ "Cho đi" 3 violation tests + 4 reward sources
    ④ Violation Impact formula + 3 responses + schema-level hierarchy
  Connection đã tách: Connection.md v5.0 (từ v1.1).
  v7.8 aligned: Self-Pattern-Modeling, Entity-Compiled, signal strength.
parent: Core-Deep-Dive/Domain/
dependencies:
  core:
    - Valence-Propagation.md v3.0 — per-entity valence, Hardware-Subsidy, mixed valence
    - Self-Pattern-Modeling.md v3.1 — Compiled/Fresh, agent prediction mechanism
    - Bond-Architecture.md v2.0 — 1 mechanism × 4 bond types, Resonance Decline
    - Entity-Compiled.md v1.0 — hub-and-spoke, grief, decay
  observation:
    - Connection.md v5.0 — 3 Generative Primitives, 4-Layer Sustainability
    - Protect.md v1.2 — loss aversion, giving balance
    - Obligation.md v1.2 — compiled prediction, reciprocity
  domain:
    - Domain.md v2.0 — 3 Domain Types, Dual Check
    - Conflict-Dynamics.md v2.0 — Overlap × Scarcity × Commitment
  collective:
    - Collective.md v1.0 — integration hub, 5 con đường
    - By-Product-Scale.md v1.0 — Pair/Hub/Institutional
    - Resonance-Sustainability.md v1.0 — 4-Layer model
  schema:
    - Anchor-Schema.md v1.2 — anchor amplify, violation cascade
    - Anchor-Schema-Extreme-Example.md v1.0 — anchor quá mức
  entity:
    - Entity-Access.md v1.2 — gradient Mức 0-5
    - Entity-Access-Excess.md v1.0 — Mức 5 territory, dependency mechanism
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Emergent Patterns — Khi Domain Interaction Lặp Lại

> **Bạn gặp 1 người → classify, evaluate, tương tác 1 lần → quên.**
> **Bạn gặp người đó 100 lần → valence tích lũy, schema compiled →**
> **→ Không còn "1 lần" nữa. Đã thành PATTERN.**
>
> Enemy. Nurturing. "Cho đi." Violation.
> Những thứ này KHÔNG được thiết kế sẵn.
> Chúng EMERGE — từ domain interaction lặp đi lặp lại,
> valence tích lũy, schema compiled qua thời gian.

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — EMERGENT PATTERNS LÀ GÌ
- §2 — [MOVED → Connection.md v5.0]
- §3 — ENEMY / THREAT PATTERN
- §4 — NURTURING PATTERN
- §5 — "CHO ĐI" PATTERN
- §6 — SUPERSEDED PATTERNS → Cross-Reference
- §7 — VIOLATION & RECOVERY
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 FILE NÀY QUAN SÁT PATTERNS EMERGE TỪ DOMAIN INTERACTION LẶP LẠI:

  Domain Interaction Flow:
    Body-need → Classify → Process → Evaluate (Valence) → Drive → Action → Feedback
    Feedback → LẶP LẠI → valence TÍCH LŨY → patterns EMERGE

  VỊ TRÍ:
  ┌──────────────────────────────────────────────────────────────┐
  │ Valence-Propagation.md v3.0                                  │
  │   = HOW body đánh giá 1 entity tại 1 thời điểm              │
  ├──────────────────────────────────────────────────────────────┤
  │ Drill-Emergent-Pattern.md (FILE NÀY)                          │
  │   = WHAT xảy ra khi valence TÍCH LŨY qua thời gian          │
  │   = Patterns EMERGE từ repeated interaction                   │
  ├──────────────────────────────────────────────────────────────┤
  │ Bond-Architecture.md v2.0                                     │
  │   = HOW patterns FORMALIZE thành 4 bond types                │
  │   Entity-Compiled = 1 mechanism × nhiều configurations       │
  ├──────────────────────────────────────────────────────────────┤
  │ Resonance-Sustainability.md v1.0                              │
  │   = WHY 1 số patterns PERSIST, 1 số DECAY                   │
  │   4-Layer: conditions → modality → amplification → trajectory│
  └──────────────────────────────────────────────────────────────┘

  FILE NÀY COVER:
    ✅ Enemy/Threat — chưa có file riêng
    ✅ Nurturing — 4-factor model unique
    ✅ "Cho đi" — 3 violation tests unique
    ✅ Violation & Recovery — schema-level analysis unique

  SUPERSEDED (cross-ref only — §6):
    → Dependency: Entity-Access v1.2 + Entity-Access-Excess v1.0
    → Mixed Valence: Valence-Propagation v3.0 §mixed
    → Group Dynamics: Collective/ folder (5 files) + By-Product-Scale v1.0
```

---

## §1 — EMERGENT PATTERNS LÀ GÌ

```
🟡 ĐỊNH NGHĨA:

  Emergent Pattern = mối quan hệ ổn định giữa body và domain entity,
  được COMPILED từ repeated domain interaction.

  KHÔNG phải module pre-designed:
    → Không có vùng não riêng cho "enemy" hay "nurturing"
    → Cùng 1 bộ cơ chế (Classify × Process × Valence × Body-base)
    → KHÁC input → KHÁC output → patterns KHÁC emerge

  KHÔNG phải quyết định có ý thức:
    → Body TỰ TÍCH LŨY valence qua mỗi interaction
    → Patterns COMPILED vào Entity-Compiled chunks vô thức
    → PFC chỉ NHẬN RA pattern đã hình thành ("ừ, nó là bạn tôi")
    → PFC KHÔNG TẠO pattern ("tôi quyết định nó là bạn")


  TẠI SAO GỌI "EMERGENT":

    ① Không ai thiết kế trước:
       → Interaction LẶP LẠI + valence TÍCH LŨY = pattern TỰ xuất hiện

    ② Emerge từ tương tác, không từ cá nhân:
       → 1 người KHÔNG THỂ có connection pattern (cần 2+)
       → Pattern nằm GIỮA body và entity, không thuộc bên nào

    ③ Không thể predict chính xác:
       → Phụ thuộc: valence tích lũy + context + body-state + cả 2 bên


  CẤU TRÚC MỖI PATTERN:

    ┌──────────────────────────────────────────────────────────────┐
    │ TRIGGER: điều kiện domain interaction nào dẫn tới pattern    │
    │ MECHANISM: body xử lý thế nào (Self-Pattern-Modeling + Valence)│
    │ COMPILED STATE: pattern đã hình thành = gì                   │
    │ INFLUENCE: pattern ảnh hưởng interaction tiếp theo            │
    │ BREAK CONDITION: khi nào pattern bị phá / thay đổi           │
    └──────────────────────────────────────────────────────────────┘

    → MỌI patterns trong file này đều follow cấu trúc này
    → Bond-Architecture.md v2.0 FORMALIZE patterns thành 4 bond types
    → Resonance-Sustainability.md v1.0 PREDICT patterns nào persist
```

---

## §2 — [MOVED] CONNECTION PATTERN → Connection.md v5.0

> Connection đã tách thành file riêng từ v1.1 (2026-04-24).
> → **Connection.md v5.0** — 3 Generative Primitives, 4-Layer Sustainability,
>   Resonance Decline, Hardware-Subsidy spectrum, Entity-Access gradient
> → **Empathy.md v4.0** — Connection ⊃ Empathy, PFC Budget, Compiled Quality

---

## §3 — ENEMY / THREAT PATTERN

```
🟡 ENEMY = MẶT ĐỐI DIỆN CỦA CONNECTION:

  Connection: sustained mutual POSITIVE valence → bond compile
  Enemy:      sustained NEGATIVE valence → avoidance / fight pattern compile

  NHƯNG enemy pattern CÓ ĐẶC ĐIỂM RIÊNG — KHÔNG phải "connection ngược":


  DEFINE:

    Enemy Pattern = compiled negative valence relationship
    giữa body và domain entity (agent HOẶC object),
    khi entity LIÊN TỤC ảnh hưởng NEGATIVE tới body channels.


  ⭐ BẤT ĐỐI XỨNG — Enemy hình thành NHANH hơn Connection:

    🟢 Negativity bias (Baumeister 2001, Rozin & Royzman 2001):
      → Negative events ảnh hưởng MẠNH hơn positive events cùng magnitude
      → 1 lần bị phản bội > 10 lần giúp đỡ (về valence impact)
      → Evolutionary: miss 1 threat = CHẾT. Miss 1 friend = chỉ thiếu

    Connection: cần NHIỀU lần positive → dần dần emerge
    Enemy: có thể chỉ 1 lần negative MẠNH → NGAY LẬP TỨC compile

    Connection: mất NHANH khi 1 lần violation lớn (§7)
    Enemy: mất CHẬM — cần NHIỀU positive để override (nếu có thể)

    → Asymmetric cost: false negative enemy = chết. False positive = chỉ tốn energy.


  3 DẠNG ENEMY PATTERN:

    ① AGENT ENEMY — sustained negative valence từ agent:
       → Kẻ bắt nạt, sếp toxic, kẻ thù chiến trường
       Đặc biệt agent enemy:
         → Agent CÓ mục tiêu riêng → unpredictable → adaptive
         → Agent BIẾT mình đang tránh → adjust strategy → arms race
         → = Agent enemy NGUY HIỂM HƠN object enemy

    ② OBJECT ENEMY — compiled negative valence từ object:
       → Chất độc, lửa, độ cao: body-base threat compiled từ experience/schema
       → Object = deterministic, không adaptive → DỄ TRÁNH hơn agent
       → NHƯNG: schema CÓ THỂ khuếch đại quá mức (phobia)

    ③ OBJECT-AS-PROXY — object reclassify vì agent schema:
       → Bụi cây chiến trường: object → "agent có thể ẩn bên trong" → threat
       → Bẫy, mìn: object MANG Ý ĐỒ agent → valence từ agent, dạng object
       → = Self-Pattern-Modeling Compiled fire "có agent" dù chỉ có object


  ⭐ DEHUMANIZATION — reclassify agent → object:

    🟡 Vấn đề: agent enemy → Self-Pattern-Modeling VẪN fire
      → Simulation tạo internal model of agent's state
      → Gây dissonance khi hành động gây hại
      → = RÀO CẢN tự nhiên chống bạo lực

    Giải pháp (evolutionary): RECLASSIFY agent → object
      → Object classification → Self-Pattern-Modeling KHÔNG fire
      → = Có thể tiêu diệt MÀ KHÔNG bị simulation dissonance

    Cases:
      "Gooks", "cockroaches" (Rwanda) = ngôn ngữ dehumanize
        → Relabel agent → vermin/object → bypass Self-Pattern-Modeling
      Bác sĩ phẫu thuật: patient → "ca mổ" → Object mode
        → TẠM THỜI, mục đích GIÚP = functional override

    → Cùng mechanism, KHÁC context:
      Bác sĩ: override TẠM THỜI, GIÚP = healthy
      Chiến tranh: override TOÀN DIỆN, DIỆT = dangerous


  ENEMY × SCHEMA INHERITANCE:

    🟡 Enemy pattern CÓ THỂ TRUYỀN qua schema KHÔNG cần trải nghiệm:
      → "Rắn = nguy hiểm" → compile enemy TRƯỚC KHI thấy rắn
      → "Nhóm X = kẻ thù" → compile TRƯỚC KHI gặp ai thuộc nhóm X
      → = Schema inheritance (Valence-Propagation v3.0): nhanh nhưng ÍT chính xác

    Risk: overgeneralize
      → "1 người nhóm X hại tôi" → compile "TOÀN BỘ nhóm X = enemy"
      → = Prejudice, racism = enemy pattern inherited + overgeneralized
      → Cùng mechanism §7 Violation response ② (overgeneralize sau violation)
```

---

## §4 — NURTURING PATTERN

```
🟡 NURTURING = EMERGENT PATTERN, KHÔNG PHẢI MODULE RIÊNG:

  DEFINE:
    Nurturing = drive chăm sóc entity có vulnerability cao,
    emerge từ: Self-Pattern-Modeling Compiled × vulnerability cues
    × perceived ability × existing body-base channels.


  4 YẾU TỐ QUYẾT ĐỊNH NURTURING INTENSITY (NHÂN, không cộng):

    ① LIVING — phải có sự sống (hoặc perceived):
       → Living → Self-Pattern-Modeling CÓ fire
       → Non-living → Self-Pattern-Modeling KHÔNG (trừ nhân cách hóa)

    ② VULNERABILITY — càng yếu ớt → signal CÀNG MẠNH:
       → 🟢 Baby Schema (Lorenz 1943, Glocker 2009):
         Mắt to, mặt tròn → nucleus accumbens fire kể cả ở non-parents
       → Hardware trigger: vulnerability = potential death → auto-prioritize

    ③ EXPRESSIVENESS — càng biểu hiện rõ state → signal CÀNG MẠNH:
       → Mặt người: CỰC expressive → Self-Pattern-Modeling input phong phú
       → Cá: gần zero biểu cảm → Self-Pattern-Modeling input nghèo nàn
       → 🟢 Facial EMG mimicry (Dimberg 2000): automatic, 300ms

    ④ SIMILARITY / FAMILIARITY — càng giống/quen → signal CÀNG MẠNH:
       → Compiled chunks nhiều → simulate CHÍNH XÁC → signal MẠNH
       → 🟢 In-group empathy bias (Xu 2009): ACC mạnh hơn cho in-group

    4 yếu tố NHÂN nhau:
      Baby ruột = Living ✅ × Vulnerability MAX × Expressiveness CAO × Familiarity MAX
        → = Nurturing MẠNH NHẤT
      Cá cảnh = Living ✅ × Vulnerability THẤP × Expressiveness ≈ 0 × Familiarity THẤP
        → = Nurturing gần ZERO → chủ yếu Aesthetic


  ⭐ REWARD ĐẶC BIỆT — gắn vào state NGƯỜI KHÁC:

    Mọi pattern khác: reward từ body-state CỦA MÌNH cải thiện
    Nurturing:         reward từ body-state CỦA NGƯỜI KHÁC cải thiện

    → "Nhìn con ăn ngon mà sướng" = Self-Pattern-Modeling detect target improve
      → prediction-delta POSITIVE → body-feedback PLEASANT
    → Unique: reward VIA simulation of other's state improvement

    → Bond-Architecture.md v2.0: parent→child bond = Entity-Compiled
      reuse mechanism, oxytocin-vasopressin dominant ratio


  CASES KIỂM CHỨNG:

    Mẹ chăm con ruột: 4 yếu tố MAX + hardware-subsidy (oxytocin)
    Người lớn thấy baby LẠ → muốn bế:
      → Baby schema hardware trigger, KHÔNG cần Entity-Compiled bond
      → = BẰNG CHỨNG nurturing ≠ connection (không cần bond)
    Nuôi pet sâu sắc: Vulnerability CAO + ability CỰC CAO (100% phụ thuộc)
    Con vật bị thương trên đường:
      → Ability CAO → dừng giúp → nhẹ nhõm
      → Ability THẤP → quay mặt → CẮT INPUT (defense)
      → = Perceived ability modulation RÕ NHẤT
```

---

## §5 — "CHO ĐI" PATTERN

```
🟡 "CHO ĐI" = CƠ CHẾ PHÂN PHỐI TÀI NGUYÊN TỰ NHIÊN:

  DEFINE:
    "Cho đi" = drive chia sẻ resource (vật chất, kiến thức, hành động)
    emerge khi: body-base CỦA MÌNH đủ + Self-Pattern-Modeling detect NGƯỜI KHÁC thiếu
    + reward từ sharing > reward từ giữ.


  CƠ CHẾ CỐT LÕI:

    Body-base MÌNH đã ĐỦ → thêm cho MÌNH: reward ≈ 0 (satiation)
    NGƯỜI KHÁC đang THIẾU → share → họ improve →
      Self-Pattern-Modeling detect improvement → prediction-delta → body PLEASANT

    → CÙNG 1 quả xoài:
      Tôi ăn thêm (đã no): reward ≈ 0 (Cyclic satiation — Gap-Body-Need v1.0)
      Cho người đói: reward cho TÔI (via Self-Pattern-Modeling) + reward cho HỌ
    → = Item tạo TỔNG REWARD LỚN HƠN khi được phân phối


  ⭐ "CHO ĐI" KHÔNG BAO GIỜ VÔ TƯ TUYỆT ĐỐI — 4 nguồn reward:

    ① SELF-PATTERN-MODELING REWARD — thấy người nhận improve → body mình pleasant
    ② STATUS REWARD — "tôi là người cho" → Costly Signal (Obligation.md v1.2)
    ③ CONNECTION REWARD — share → bond tăng → future access (reciprocal)
    ④ SCHEMA REWARD — "người tốt" identity confirm → satisfaction

    → = "Cho đi vô tư" thực ra = nhiều reward sources CÙNG fire
    → = Không phải xấu — là THIẾT KẾ TỐI ƯU (evolution)
    → Protect.md v1.2 §7: giving dynamic = ĐỐI TRỌNG tự nhiên cho protect


  ⭐ 3 VIOLATION TESTS — CHỨNG MINH "cho đi" driven by reward system:

    🟡 Nếu cho đi thật sự vô tư → 3 tests này sẽ KHÔNG ẢNH HƯỞNG.
    Nhưng thực tế: MỌI case đều dừng khi 1 trong 3 bị vi phạm:

    ① BODY-BASE CỦA MÌNH THIẾU:
       → Cho khi thừa = vui. Cho khi thiếu = ĐAU.
       → Trừ override justified: mẹ nhịn con ăn — hardware-subsidy L0

    ② SCHEMA GỐC BỊ VI PHẠM:
       → Từ thiện → phát hiện lừa đảo → DỪNG NGAY
       → Cúng chùa → sư phạm giới → DỪNG NGAY
       → = Schema drive bị phá → drive MẤT

    ③ RECIPROCITY = 0 KÉO DÀI:
       → Cho nhiều lần → không nhận lại gì → body compile: "no reciprocate"
       → Connection reward GIẢM → total reward < cost → DỪNG
       → 🟢 Reciprocal altruism (Trivers 1971): non-reciprocator bị loại


  SPECTRUM — LÀNH MẠNH tới PATHOLOGICAL:

    LÀNH MẠNH: body đủ + share dư → reward > 0, cost ≈ 0
    OVERRIDE A (justified): mẹ nhịn con ăn → hardware priority → CÓ ceiling tự nhiên
    OVERRIDE B (schema hijack): cúng tới khánh kiệt → "được phước"
      → KHÔNG có ceiling → CÓ HẠI
      → = Bug: mechanism tốt cho nhóm, hại cá nhân

    → Ranh giới: A có hardware ceiling, B không → B = territory nguy hiểm
```

---

## §6 — SUPERSEDED PATTERNS → Cross-Reference

> v1.2 có 3 sections đã được file chuyên sâu cover SÂU HƠN nhiều.
> v2.0 thu gọn → cross-ref. Content gốc: backup/Emergent-Patterns-v1.2-backup.md

### §6.1 — Dependency Pattern

> **→ Entity-Access.md v1.2** — gradient Mức 0-5, 3-Factor Model
> **→ Entity-Access-Excess.md v1.0** — Mức 5 territory, excess spectrum, 3 origins
> **→ Entity-Compiled.md v1.0** — hub-and-spoke, grief A+B+C, decay 3-layer
>
> v1.2 §6 core insight: Dependency = positive valence CAO + replaceability THẤP.
> Entity-Access v1.2 FORMALIZE: gradient Mức 0-5 thay cho binary dependency.
> Entity-Access-Excess v1.0: Mức 5 = dependency territory, cùng neural circuits drug addiction.

### §6.2 — Mixed Valence

> **→ Valence-Propagation.md v3.0** — ⑧ Mixed valence = PARALLEL per-channel
>
> v1.2 §7 core insight: Mixed valence = bình thường cho agent phức tạp.
> Valence-Propagation v3.0 FORMALIZE: Structural vs Current valence, per-entity dynamics,
> mixed = MOST COMMON state, 3 Firing Modes.

### §6.3 — Group Dynamics

> **→ Collective.md v1.0** — integration hub, 5 con đường ảnh hưởng cá nhân
> **→ Collective/ folder** (5 files: Collective-Body, Coordination-Node,
>   Collective-Arc-Dynamics, Collective-Purpose, Compliance-Floor)
> **→ By-Product-Scale.md v1.0** — Pair/Hub/Institutional topology
>
> v1.2 §8 core insight: group amplify reward × N agents, virtual chunks pooling.
> Collective/ folder cover SÂU HƠN: 3 cấp model, coordination node,
> arc dynamics, compliance floor. By-Product-Scale: 3 scales.

---

## §7 — VIOLATION & RECOVERY

```
🟡 KHI PATTERN BỊ PHÁ — domain thực tế XUNG ĐỘT MẠNH với schema compiled:

  DEFINE:
    Violation = domain event PHẢN lại pattern đã compiled,
    với magnitude đủ lớn để schema PHẢI update.

    → Bạn thân nói xấu sau lưng (connection pattern violated)
    → Sư phạm giới (schema "sư = thánh thiện" violated)
    → Mẹ bỏ rơi con (schema "mẹ = an toàn" violated)


  ⭐ IMPACT = INVESTMENT × VIOLATION SEVERITY:

    🟡 Không phải mọi violation đều ảnh hưởng BẰNG NHAU:

    Investment CAO × Violation NẶNG = ⭐ CRISIS
    Investment THẤP × Violation NẶNG = cắt, move on
    Investment CAO × Violation NHẸ = dung nạp, adjust
    Investment THẤP × Violation NHẸ = bỏ qua

    ┌────────────────────┬──────────────────┬─────────────────────┐
    │                    │ Violation NHẸ    │ Violation NẶNG      │
    ├────────────────────┼──────────────────┼─────────────────────┤
    │ Investment THẤP    │ Bỏ qua           │ Cắt, move on        │
    ├────────────────────┼──────────────────┼─────────────────────┤
    │ Investment CAO     │ Dung nạp          │ ⭐ CRISIS           │
    └────────────────────┴──────────────────┴─────────────────────┘


  ⭐ 3 RESPONSES KHI CRISIS (investment cao × violation nặng):

    ① RECALIBRATE — update schema cho entity CỤ THỂ:
       → "Bạn A phản bội → A KHÔNG đáng tin, nhưng BẠN BÈ nói chung vẫn OK"
       → = Adjust Entity-Compiled cho entity, giữ pattern tổng
       → HEALTHY nhưng KHÓ: cần PFC budget + cortisol manageable + time
       → = "Trưởng thành" = khả năng recalibrate sau violation

    ② OVERGENERALIZE — mở rộng violation ra TOÀN BỘ category:
       → "Bạn A phản bội → ĐÀN ÔNG/PHỤ NỮ đều thế → KHÔNG TIN AI NỮA"
       → Violation từ 1 entity → generalize thành pattern CHO CẢ LOẠI
       → Evolutionary safe: false positive (không tin ai) = chỉ mất cơ hội
       → = Prejudice, trust issues = overgeneralize
       → 🟢 Negativity bias (Baumeister 2001): negative generalize nhanh hơn positive
       → Cùng mechanism §3 Enemy schema inheritance

    ③ COLLAPSE — schema LEVEL CAO bị phá → worldview lung lay:
       → "Sư phạm giới → TÔN GIÁO là lừa → không tin gì nữa"
       → "Mẹ bỏ rơi → GIA ĐÌNH không an toàn → thế giới nguy hiểm"
       → = Violation đánh vào ANCHOR SCHEMA (Anchor-Schema.md) → cascade
       → NGUY HIỂM NHẤT nhưng HIẾM (cần violation ở schema rất cao)
       → Anchor-Schema-Extreme-Example.md: anchor quá mức + skip domain check


  SCHEMA LEVEL QUYẾT ĐỊNH IMPACT:

    ┌──────────────────────┬────────────────────────────────────────────┐
    │ Schema Level         │ Violation impact                           │
    ├──────────────────────┼────────────────────────────────────────────┤
    │ Agent CỤ THỂ         │ Chỉ ảnh hưởng relation với A               │
    │ (thấp nhất)          │ Recover: tương đối nhanh                   │
    ├──────────────────────┼────────────────────────────────────────────┤
    │ Category              │ Ảnh hưởng MỌI relation với category        │
    │                       │ Recover: lâu, cần positive counter-evidence│
    ├──────────────────────┼────────────────────────────────────────────┤
    │ Tổ chức / Domain      │ Ảnh hưởng toàn bộ domain trust            │
    │                       │ Recover: rất lâu, có thể KHÔNG            │
    ├──────────────────────┼────────────────────────────────────────────┤
    │ Worldview             │ Ảnh hưởng MỌI domain interaction           │
    │ (cao nhất)            │ Recover: cực kỳ khó, cần anchor MỚI      │
    └──────────────────────┴────────────────────────────────────────────┘

    → Schema level × Domain Types (Domain.md v2.0):
      Reality Domain violation: immediate feedback → recalibrate DỄ hơn
      Abstract-Dynamic Domain violation: delayed/ambiguous feedback
        → overgeneralize DỄ HƠN, recovery KHÓ HƠN
      → = Domain type ảnh hưởng recovery difficulty


  CASES:

    Tình yêu phản bội:
      Investment CAO + Violation NẶNG
      → Phổ biến: overgeneralize ("không dám yêu lại")
      → Healthy: recalibrate ("người NÀY không ổn, tình yêu vẫn có thể")
      → Entity-Compiled: grief Type A (active missing) + Type B (identity vacuum)

    Sư phạm giới:
      Anchor schema "sư = thánh thiện" bị phá → cascade risk CAO
      "Phước" KHÔNG verify được (Abstract-Dynamic Domain) → stuck
      Dual Check (Domain.md v2.0): body smoothing active, domain KHÔNG confirm

    Công đức + sư phạm giới (STACK):
      "Cho đi" pattern BỊ PHÁ (§5) + faith schema BỊ PHÁ = DOUBLE violation
      → Recovery cực khó vì 2 patterns bị phá ĐỒNG THỜI


  RECOVERY PATHS:

    ① Rebuild CÙNG entity (recalibrate):
       → Entity-Compiled chunks update, không xóa
       → Rebuild CHẬM HƠN build lần đầu (trust sẹo)
       → "Vết nứt đã sửa" — functional nhưng sẹo trong schema

    ② Rebuild VỚI entity MỚI:
       → Overgeneralize schema CÓ THỂ BLOCK ("không dám yêu lại")
       → Cần: domain exposure mới + time + positive counter-evidence

    ③ Rebuild SCHEMA level cao (sau collapse):
       → Cần ANCHOR MỚI (Anchor-Schema.md) — entity/experience đủ mạnh
       → "1 anchor person đủ" = 1 người đáng tin →
         rebuild "thế giới có người tốt" từ collapsed worldview
       → CỰC CHẬM + cần consistency lâu dài
```

---

## §8 — HONEST ASSESSMENT

```
  ESTABLISHED (🟢):

    🟢 Negativity bias (Baumeister 2001, Rozin & Royzman 2001):
       negative events impact mạnh hơn — enemy formation asymmetry
    🟢 Baby Schema (Lorenz 1943, Glocker 2009):
       nucleus accumbens fires cho infant faces, kể cả non-parents
    🟢 Facial EMG mimicry (Dimberg 2000):
       automatic, pre-conscious, 300ms
    🟢 In-group empathy bias (Xu 2009):
       ACC response mạnh hơn cho in-group
    🟢 Reciprocal altruism (Trivers 1971):
       cooperation = optimal long-term strategy
    🟢 Kin selection (Hamilton 1964):
       helping gene-carriers = giúp gene mình survive
    🟢 Attachment theory (Bowlby 1969):
       connection = innate drive, proximity seeking
    🟢 Social pain = physical pain (Eisenberger 2003):
       rejection activates same neural pathways


  FRAMEWORK SUY LUẬN (🟡):

    🟡 "Emergent patterns = compiled valence relationships"
       — Logical + consistent với attachment theory, schema therapy
    🟡 "Enemy hình thành NHANH hơn connection"
       — Supported by negativity bias research (🟢)
    🟡 "Dehumanization = agent→object reclassify → Self-Pattern-Modeling OFF"
       — Consistent với Haslam 2006, Leyens 2000
    🟡 "Nurturing = 4 factors nhân nhau"
       — Each factor documented; multiplication model = synthesis
    🟡 "'Cho đi' không vô tư — 4 reward sources"
       — Consistent với warm glow (Andreoni 1990), costly signaling
    🟡 "3 violation tests" — if truly selfless, tests wouldn't affect. They do.
    🟡 "Violation impact = investment × severity"
       — Well-established in relationship science
    🟡 "3 responses (recalibrate / overgeneralize / collapse)"
       — Consistent với schema therapy, Janoff-Bulman 1992
    🟡 "Schema level → violation impact (4-level)"
       — Logical: higher schema = more dependent schemas below


  HYPOTHESIS (🔴):

    🔴 "Object-as-proxy enemy" (bụi cây → agent container)
       — Logical but specific mechanism chưa mapped
    🔴 "Schema inheritance → enemy → prejudice" (full causal chain)
       — Each step has evidence, full chain = hypothesis
    🔴 "4 factors NHÂN (không cộng)" — could be additive or complex
    🔴 "Collapse → cần anchor MỚI" — consistent với therapy; "1 person đủ" = not verified
    🔴 "Domain type ảnh hưởng recovery difficulty" — logical but untested


  ⚠️ TỔNG THỂ:
    v2.0 THU GỌN v1.2 (~1,302L → ~560L). ~60% superseded → cross-ref.
    CÒN LẠI = unique content: Enemy + Nurturing + "Cho đi" + Violation.
    v7.8 aligned: Self-Pattern-Modeling, Entity-Compiled, signal strength.
    NEW: Domain Types × violation recovery (§7).
    Mạnh nhất: Enemy (negativity bias 🟢), Violation (relationship science 🟢).
    Yếu nhất: nurturing multiplication model, collapse recovery hypothesis.
```

---

## §9 — CROSS-REFERENCES

```
  DOMAIN FOLDER:
  → Domain.md v2.0 — 3 Domain Types, Dual Check, 3-nguồn constraint
  → Conflict-Dynamics.md v2.0 — scarcity engine, "cho đi" counter-mechanism
  → Domain-Mapping-Drive.md v2.0 — WHY map domain

  CORE MECHANISM:
  → Self-Pattern-Modeling.md v3.1 — Compiled/Fresh, agent prediction mechanism
  → Bond-Architecture.md v2.0 — 4 bond types, Resonance Decline decline, gap clone impossible
  → Entity-Compiled.md v1.0 — hub-and-spoke, formation 40→200h, grief
  → Valence-Propagation.md v3.0 — per-entity valence, Hardware-Subsidy, mixed
  → By-Product-Scale.md v1.0 — Pair/Hub/Institutional topology
  → Resonance-Sustainability.md v1.0 — 4-Layer model, persistence prediction

  OBSERVATION FILES:
  → Connection.md v5.0 — CONNECTION pattern (§2 MOVED)
  → Empathy.md v4.0 — Connection ⊃ Empathy, PFC Budget
  → Protect.md v1.2 — loss aversion, §7 giving balance
  → Obligation.md v1.2 — compiled prediction, reciprocity
  → Status.md v2.1 — Resource Access Map

  ENTITY SYSTEM:
  → Entity-Access.md v1.2 — gradient Mức 0-5 (§6.1 SUPERSEDED)
  → Entity-Access-Excess.md v1.0 — Mức 5 territory (§6.1 SUPERSEDED)

  SCHEMA:
  → Anchor-Schema.md v1.2 — anchor concept, violation cascade
  → Anchor-Schema-Extreme-Example.md v1.0 — anchor quá mức

  COLLECTIVE:
  → Collective.md v1.0 — integration hub (§6.3 SUPERSEDED)
  → Collective/ folder (5 files) — deep-dive collective dynamics

  BODY-BASE:
  → Gap-Body-Need.md v1.0 — satiation types (§5 reference)
  → Cortisol-Baseline.md v2.0 — sustained stress (violation context)

  BACKUP:
  → backup/Emergent-Patterns-v1.2-backup.md — full v1.2 content
```

---

> *"Bạn không QUYẾT ĐỊNH yêu ai hay ghét ai.
> Body gặp họ, đánh giá, lặp lại nhiều lần,
> và 1 ngày nhận ra: pattern ĐÃ HÌNH THÀNH.
> Enemy, nurturing, cho đi — tất cả EMERGE
> từ cùng 1 bộ cơ chế, chạy vô thức.
> Bạn chỉ NHẬN RA khi pattern đã quá mạnh để bỏ qua."*
