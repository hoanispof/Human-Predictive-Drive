# Valence — Cách Body Đánh Giá Mọi Thứ Trong Domain

> **Cái dao từng cắt tay bạn. Bạn SỢ nó.**
> **Cùng cái dao đó, bạn học cách dùng. Bạn THÍCH nó.**
> **Cùng cái dao đó, trong tay kẻ thù. Bạn SỢ nó LẠI.**
>
> Cùng 1 entity — valence THAY ĐỔI tùy experience và context.
>
> **Mẹ cho ăn. Bạn YÊU mẹ.**
> **Mẹ ép học. Bạn GHÉT mẹ.**
> **Cùng lúc.** Không mâu thuẫn — vì mẹ ảnh hưởng NHIỀU channels,
> mỗi channel 1 valence KHÁC NHAU.
>
> Valence = cách body ĐÁI GIÁ: entity này ảnh hưởng
> body channels CỦA TÔI thế nào? Positive? Negative? Mixed?
>
> File này: valence LÀ GÌ, cấu trúc, Object vs Agent,
> cách hình thành, cách update, và cases phân tích.

---

> **Trạng thái:** DRAFT v0.5 — concept MỚI trong framework
> **Ngày:** 2026-04-12
> **Mục đích:** Define Valence — cách body đánh giá MỌI entity trong domain
> dựa trên ảnh hưởng tới body channels. Multi-channel, dynamic, stored in schema.
> **Vị trí:** Core-Deep-Dive/Domain/ (file chi tiết, thuộc Domain Interaction)
> **Flow đọc:**
>   Domain-Interaction.md §5 (overview) → **Valence.md** (file NÀY — chi tiết)
> **PHÂN BIỆT VỚI DRIVE.MD:**
>   Valence = HOW body ĐÁNH GIÁ 1 entity (entity → body channels → positive/negative)
>   Drive.md = HOW NHIỀU drives COMBINE → action (multiple drives → tổng hợp → hành vi)
>   = 2 bước KHÁC NHAU: ③ evaluate (Valence) → ④ combine drives → action (Drive.md)
> **Tiền đề:**
>   Domain-Interaction.md (overview flow)
>   Object-Agent.md (classification ảnh hưởng valence complexity)
>   Core-v7.5-Draft.md §2 (Body-Base L0-L3 — channels mà valence đánh giá)
>   Body-Dissonance.md (dissonance signals — 1 trong 3 body signals)
>   Drive.md (drive integration — bước SAU valence)
> **⚠️ 🟡 Concept MỚI — logic consistent, cần test thêm**
> **Quy ước:** 🟢 Research support | 🟡 Suy luận từ framework | 🔴 Hypothesis

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — VALENCE LÀ GÌ
- §2 — VALENCE PROFILE: Cấu Trúc
- §3 — OBJECT VALENCE vs AGENT VALENCE
- §4 — CÁCH VALENCE HÌNH THÀNH
- §5 — VALENCE UPDATE: Feedback Loop
- §6 — CASES PHÂN TÍCH
- §7 — VALENCE DYNAMICS: Mixed, Conflict, Flip, Violation
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 VALENCE TRONG DOMAIN INTERACTION FLOW:

  Domain Interaction flow (Domain-Interaction.md §2):
    Body-need → ① Classify → ② Process → ③ EVALUATE → ④ Drive → ⑤ Feedback
                                            ↑
                                        FILE NÀY

  Bước ③ EVALUATE:
    → Entity đã được classify (Object/Agent) và process (Logic/Modeling)
    → Bây giờ body đánh giá: entity này ẢNH HƯỞNG body channels THẾ NÀO?
    → Kết quả = VALENCE PROFILE — stored in schema
    → Valence profile → feed vào Drive calculation (bước ④)


  PHÂN BIỆT 3 CONCEPTS GẦN NHAU:

    VALENCE (file này):
      "Entity X ảnh hưởng body channels CỦA TÔI thế nào?"
      = ĐÁNH GIÁ 1 entity → multi-channel profile
      Input: entity + body-base state + context + compiled schema
      Output: valence profile (positive/negative PER CHANNEL)

    DRIVE (Drive.md):
      "NHIỀU drives đang active → não CHỌN hành động NÀO?"
      = TỔNG HỢP nhiều drives → action emerge
      Input: tất cả valences + body-needs + context
      Output: action cụ thể

    BODY SIGNALS (Body-Dissonance.md):
      "Body PHẢN HỒI: đủ chưa? Hay chưa? Tiếp không?"
      = FEEDBACK sau action
      3 signals: Satisfaction, Reward, Dissonance

    Flow: Valence → Drive → Action → Body Signals → Update Valence → Loop
```

---

## §1 — VALENCE LÀ GÌ

```
🟡 ĐỊNH NGHĨA:

  Valence = ĐÁNH GIÁ CỦA BODY về cách 1 entity ảnh hưởng body channels.

  ⭐ MULTI-CHANNEL — KHÔNG PHẢI 1 TRỤC TỐT/XẤU:

    SAI: "Mẹ = tốt" hoặc "Mẹ = xấu" (1 trục)
    ĐÚNG: Mẹ = {
      L1 nutrition: ++ (cho ăn)
      L2 comfort: ++ (ôm, vỗ về)
      L2 autonomy: -- (ép học, cấm chơi)
      L3 mastery: + (dạy bài)
      L3 novelty: - (bắt lặp lại bài khó)
    }
    = Valence KHÁC NHAU trên TỪNG CHANNEL
    = YÊU VÀ GHÉT CÙNG LÚC — không mâu thuẫn

  ⭐ DYNAMIC — THAY ĐỔI THEO THỜI GIAN:

    Dao lần đầu: { L0 safety: -- }
    Dao sau khi học: { L1 utility: ++, L0 safety: neutral }
    = CÙNG entity, KHÁC valence — vì experience thay đổi

  ⭐ CONTEXT-DEPENDENT:

    Quả bom trong tay tôi: { L0: ++, L1: ++ } (vũ khí, bảo vệ)
    Quả bom trong tay kẻ thù: { L0: --, L1: -- } (threat)
    = CÙNG entity, CÙNG thời điểm, KHÁC CONTEXT → khác valence

  ⭐ STORED IN SCHEMA:

    Valence profile được compiled vào schema qua experience
    → Gặp lại entity → schema load valence → body respond NGAY
    → Không cần re-evaluate từ đầu mỗi lần
    → = Tại sao thấy con chó từng cắn → SỢ NGAY (compiled valence)
```

---

## §2 — VALENCE PROFILE: Cấu Trúc

```
🟡 CẤU TRÚC VALENCE PROFILE CHO MỖI ENTITY:

  Mỗi entity trong domain có 1 VALENCE PROFILE lưu trong schema:

  ┌─────────────────────────────────────────────────────────────┐
  │ VALENCE PROFILE: Entity X                                    │
  │                                                              │
  │ BODY-BASE CHANNELS:                                          │
  │   L0 Alive:     safe ←───────→ dangerous                    │
  │   L1 Survival:  useful ←──────→ harmful                     │
  │   L2 Quality:                                                │
  │     Comfort:    pleasant ←────→ unpleasant                   │
  │     Experience: rich ←────────→ poor                         │
  │     Agent input: calibrating ←→ draining                     │
  │   L3 Pattern:                                                │
  │     Novelty:    interesting ←─→ boring                       │
  │     Mastery:    enabling ←────→ blocking                     │
  │     Status:     elevating ←───→ diminishing                  │
  │     Protect:    safe ←────────→ threatening (my resources)   │
  │                                                              │
  │ META-DIMENSIONS:                                             │
  │   Trust:           high ←─────→ low                          │
  │   Predictability:  high ←─────→ low                          │
  │   Replaceability:  easy ←─────→ hard                         │
  │   Dependency:      none ←─────→ critical                     │
  │                                                              │
  │ NET: tổng hợp across channels → approach / avoid / mixed     │
  └─────────────────────────────────────────────────────────────┘


  ĐẶC ĐIỂM:

    ① Mỗi channel có valence RIÊNG — không average
      Mẹ: L1++ L2++ autonomy-- = KHÔNG phải "hơi positive"
      = Positive ở channels này, Negative ở channels kia, CÙNG LÚC

    ② Không phải mọi channel đều có valence cho mọi entity
      Dao: L0, L1 rõ ràng. L3 status? Gần zero. Novelty? Chỉ lần đầu.
      = Valence profile SPARSE cho objects, DENSE cho agents

    ③ Intensity KHÁC NHAU
      Dao cắt tay: L0 safety -2 (nhẹ)
      Hổ đuổi: L0 safety -10 (cực mạnh)
      = Cùng channel, cùng hướng, khác CƯỜNG ĐỘ

    ④ Meta-dimensions MODULATE body-base channels
      Trust cao → valence AMPLIFIED (tin người bạn thân → valence mạnh hơn)
      Trust thấp → valence DAMPENED (không tin người lạ → valence yếu)
      Replaceability dễ → mất entity ÍT impact
      Replaceability khó → mất entity IMPACT LỚN (grief)
```

---

## §3 — OBJECT VALENCE vs AGENT VALENCE

```
🟡 CLASSIFICATION (Object-Agent.md) QUYẾT ĐỊNH VALENCE COMPLEXITY:

  ┌─────────────────────┬──────────────────────────────────────────┐
  │ OBJECT VALENCE      │ AGENT VALENCE                             │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ Ít channels active   │ NHIỀU channels active                    │
  │ Dao: L0, L1          │ Mẹ: L0, L1, L2, L3, trust, dependency  │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ Tương đối ỔN ĐỊNH   │ DYNAMIC — thay đổi liên tục              │
  │ Dao vẫn là dao       │ Mẹ vui sáng, cáu chiều                  │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ ONE-WAY              │ BIDIRECTIONAL                             │
  │ Tôi đánh giá dao     │ Tôi đánh giá mẹ VÀ mẹ đánh giá tôi    │
  │ Dao không đánh giá   │ = 2 valence profiles TƯƠNG TÁC           │
  │ ngược                │                                          │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ NO CONFLICT          │ CÓ THỂ CONFLICT                          │
  │ Dao không có mục tiêu│ Mẹ muốn con học ≠ con muốn chơi        │
  │ xung đột với tôi    │ = Agent có mục tiêu RIÊNG → xung đột    │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ DỄ thay thế          │ KHÓ thay thế                             │
  │ Dao khác cũng cắt    │ Mẹ khác KHÔNG phải mẹ mình              │
  │ được                 │ = Mỗi agent unique                       │
  ├─────────────────────┼──────────────────────────────────────────┤
  │ PREDICTABLE          │ UNPREDICTABLE                             │
  │ Valence ít bất ngờ   │ Valence có thể FLIP bất ngờ              │
  │                      │ Bạn thân → phản bội = flip toàn diện    │
  └─────────────────────┴──────────────────────────────────────────┘


  → Agent valence PHỨC TẠP HƠN NHIỀU vì:
    Agent có state riêng (vui/buồn → ảnh hưởng hành vi → ảnh hưởng valence)
    Agent có mục tiêu riêng (có thể align hoặc conflict với mục tiêu tôi)
    Agent reciprocate (agent CŨNG đánh giá tôi → ảnh hưởng hành vi agent → ảnh hưởng valence)
    Agent unpredictable (valence có thể thay đổi bất ngờ)

  → = Tại sao "mối quan hệ" PHỨC TẠP hơn "dùng đồ vật"
  → = Cùng 1 cơ chế (valence), khác COMPLEXITY vì Object vs Agent
```

---

## §4 — CÁCH VALENCE HÌNH THÀNH

```
🟡 VALENCE ĐƯỢC BUILD TỪ 4 NGUỒN:

  ① DIRECT EXPERIENCE — trải nghiệm trực tiếp:
    → Cầm dao → cắt tay → ĐAU → valence: { L0 safety: -- }
    → Mẹ cho ăn → HẾT ĐÓI → valence: { L1 nutrition: ++ }
    → Chơi bóng cùng bạn → VUI → valence: { L3 novelty: ++, L2 experience: ++ }
    → = Nguồn CHÍNH XÁC NHẤT — body verify trực tiếp
    → = NHƯNGchậm (phải trải nghiệm mới biết)

  ② OBSERVED EXPERIENCE — quan sát người khác:
    → Thấy bạn bị chó cắn → valence chó: { L0 safety: - }
    → Thấy mẹ nấu ăn ngon → valence bếp: { L1: + }
    → = Mirror mechanism (agent processing) đọc state người khác
    → = NHANH hơn direct experience (không cần bị cắn để biết chó nguy hiểm)
    → = NHƯNG kém chính xác (mirror ≈ 10-30% intensity, có thể bias)

  ③ SCHEMA INHERITANCE — thừa kế từ cộng đồng:
    → Mẹ nói "dao nguy hiểm" → valence: { L0 safety: - } (chưa cần bị cắt)
    → Cộng đồng nói "bộ đội tốt" → valence: { trust: +, L0 safety: + }
    → Tôn giáo: "Thiên Chúa yêu thương" → valence God: { ALL: ++ }
    → = NHANH NHẤT (không cần trải nghiệm hay quan sát)
    → = NHƯNG có thể SAI (schema inherit ≠ reality)
    → = TẠI SAO tuyên truyền WORK: install valence TRƯỚC khi verify

  ④ CONTEXT INFERENCE — suy luận từ context:
    → Quả bom trong tay đồng đội: { positive }
    → Quả bom trong tay kẻ thù: { extreme negative }
    → Bụi cây trong công viên: { neutral }
    → Bụi cây trong chiến trường: { threat }
    → = Cùng entity, khác context → khác valence
    → = Modeling mode tính toán: "trong context NÀY, entity NÀY có ý nghĩa gì?"


  ĐỘ TIN CẬY:
    Direct experience > Observed experience > Context inference > Schema inheritance
    NHƯNG: tốc độ ngược lại:
    Schema inheritance > Context inference > Observed > Direct
    → = Trade-off: nhanh → ít chính xác. Chậm → chính xác hơn.
    → = Evolutionary: inherit "rắn nguy hiểm" NHANH > tự bị cắn rồi mới biết
```

---

## §5 — VALENCE UPDATE: Feedback Loop

```
🟡 VALENCE KHÔNG CỐ ĐỊNH — update liên tục qua feedback:

  LOOP:
    Valence hiện tại → Drive → Action → Domain feedback → Body signals → Update valence

  3 LOẠI UPDATE:

  ① REINFORCEMENT — valence MẠNH thêm:
    → Mẹ cho ăn 1000 lần → valence { L1: ++ } compiled CỰC SÂU
    → Bạn thân giúp đỡ nhiều năm → valence { trust: ++++ }
    → = Lặp lại consistent → valence COMPILE thành schema sâu
    → = Khó thay đổi vì đã anchored

  ② REVISION — valence THAY ĐỔI DẦN:
    → Dao: lần đầu cắt tay → { L0: -- }
    → Dao: học cách dùng → { L1: ++ } dần OVERRIDE { L0: -- }
    → Bạn B: cho bút { + } → phá tập trung { - } → net dần shift negative
    → = Domain feedback KHÁC valence hiện tại → body adjust DẦN
    → = Tốc độ: tùy intensity + frequency + recency

  ③ VIOLENT FLIP — valence BỊ ĐẢO NGƯỢC:
    → Bạn thân phản bội: trust++++ → trust---- (FLIP violent)
    → Phát hiện sư thầy tham nhũng: valence chùa flip
    → Cố tình ăn cơm với kẻ thù → kẻ thù hóa bạn (Stockholm)
    → = CỰC HIẾM nhưng CỰC MẠNH — vì phá compiled schema
    → = Chi tiết: Emergent-Patterns.md (Violation & Recovery)


  TỐC ĐỘ UPDATE — 3 yếu tố:

    INTENSITY: feedback mạnh → update nhanh
      Bị chó cắn (đau mạnh) → valence update NGAY
      Bạn hơi chậm trả lời tin nhắn → update RẤT CHẬM

    FREQUENCY: feedback lặp lại → update tích lũy
      Mẹ cho ăn MỖI NGÀY → valence compile RẤT SÂU
      Gặp người lạ 1 LẦN → valence RẤT NÔNG

    RECENCY: feedback GẦN ĐÂY ảnh hưởng nhiều hơn
      Bạn giúp hôm qua → valence tươi
      Bạn giúp 5 năm trước → valence MỜ DẦN (trừ khi đã compile)

  ⚠️ BIAS trong update:
    → Negative bias: negative feedback → update NHANH hơn positive
      (evolutionary: bỏ qua threat = chết > bỏ qua reward = mất cơ hội)
    → Confirmation bias: valence hiện tại → filter feedback cho match
      (ghét ai → chú ý hành vi xấu → ghét thêm → loop)
    → 🟢 Consistent: negativity bias trong psychology research
```

---

## §6 — CASES PHÂN TÍCH

```
🟡 CASES TỪ SESSION — verify Valence framework:

  ① CÁI DAO — Object valence đơn giản, thay đổi theo experience:

    Lần đầu cắt tay:
      Profile: { L0 safety: -3, L1 utility: 0 }
      → Sợ dao

    Sau khi học cách dùng:
      Profile: { L0 safety: -1 (biết cẩn thận), L1 utility: +4 }
      → Thấy dao có ích. Sợ giảm, utility tăng.

    = Object valence: ít channels, thay đổi qua learning, ổn định sau compile


  ② MẸ — Agent valence phức tạp, multi-channel, mixed:

    Trẻ nhỏ:
      Profile: { L1 nutrition: ++, L2 comfort: ++, L0 protection: ++,
                trust: high, dependency: critical, replaceability: impossible }
      → Yêu mẹ tuyệt đối

    Lớn hơn (mẹ ép học):
      Profile: thêm { L2 autonomy: --, L3 novelty: - (không được chơi),
                L1 energy: -- (thiếu ngủ) }
      → YÊU VÀ GHÉT CÙNG LÚC — channels cũ vẫn positive, channels mới negative

    Đọc bài văn về tình mẹ:
      → Modeling shift: thấy mẹ nỗ lực → valence { L3 coherence: + }
      → Logic confirm: mẹ ép vì tốt cho mình → rational valence +
      → NHƯNG body channels (mệt, thiếu ngủ) VẪN negative
      → = PFC valence ≠ body valence — có thể conflict

    = Agent valence: nhiều channels, mixed, dynamic, KHÔNG average


  ③ BẠN B — Agent valence shift dẫn tới CẮT:

    Cho bút: { L3 utility: +1 }
    Nói chuyện vui lần đầu: { L2 experience: +1 }
    Hay nói chuyện ồn khi mình đang làm việc: { L3 focus: -2, -3, -4... } (tích lũy)
    Nói thẳng → conflict: { trust: drop }
    Net valence shift NEGATIVE → CẮT → "thoải mái trở lại"

    So sánh với mẹ: BẠN B CẮT ĐƯỢC vì:
      Dependency: THẤP (không phải B cho ăn)
      Replaceability: DỄ (bạn khác cũng cho mượn bút)
      Channels positive: ÍT (chỉ 1-2)
      → Net negative + low dependency + easy replace = CẮT là optimal


  ④ THIÊN CHÚA — Abstract agent, valence HOÀN HẢO:

    Profile: { ALL channels: ++, trust: absolute,
              predictability: absolute (vì abstract, không hành động thực),
              replaceability: impossible }

    TẠI SAO valence hoàn hảo:
      → Abstract agent: KHÔNG BAO GIỜ hành động thực → KHÔNG BAO GIỜ tạo negative
      → Cộng đồng reinforce LIÊN TỤC → valence compile CỰC SÂU
      → Schema unfalsifiable → không có domain feedback nào phá được
      → = "Thiết kế" valence hoàn hảo nhất có thể cho sustained positive

    = Agent valence: khi agent KHÔNG CÓ THẬT → valence KHÔNG BAO GIỜ bị negative feedback


  ⑤ NGƯỜI ĂN XIN — Valence trigger MIRROR mechanism:

    Thấy người bò lê lết:
      → Agent processing: vulnerability cues CỰC CAO
      → Mirror fire: body dissonance CỦA MÌNH (dù không phải mình đau)
      → Valence người ăn xin: { vulnerability: extreme, ability_to_help: có }
      → Drive: cho tiền (resolve mirror dissonance)
      → Cho xong: RELIEF (not euphoria) — dissonance giảm, body signal "ổn"
      → Không cho: áy náy = mirror dissonance TREO + ability mà không action

    Người biết ăn xin GIẢ (schema override):
      → Schema "nhiều người giả" → SUPPRESS mirror
      → Valence: { trust: rất thấp } → mirror KHÔNG fire mạnh
      → Lắc đầu → không dissonance → đi tiếp
      → = CÙNG input, KHÁC schema → KHÁC valence → KHÁC response


  ⑥ QUẢ BOM — Cùng object, valence ĐẢO NGƯỢC theo context:

    Bom trong tay tôi: { L0: ++, L1: ++ } (vũ khí bảo vệ)
    Bom trong tay kẻ thù: { L0: --, L1: -- } (threat)
    Bom nằm dưới đất: { L0: --- } (mìn, threat trực tiếp)

    = Context QUYẾT ĐỊNH valence
    = Object valence CÓ THỂ phức tạp khi context thay đổi mạnh


  ⑦ THÚ CƯNG — Agent valence GẦN HOÀN HẢO:

    Profile: { L2 comfort: ++, L3 novelty: + (hành vi unpredictable nhẹ),
              L2 agent input: ++ (calibration), trust: high }
    Chi phí: { L1 resource: - (thức ăn, lông), time: - }
    NET: positive vượt trội

    TẠI SAO gần hoàn hảo:
      → Agent (sống, có hành vi) → agent processing fire
      → Mục tiêu GẦN NHƯ ALIGN hoàn toàn với chủ (ăn, chơi, gần người)
      → ÍT xung đột mục tiêu (thú cưng KHÔNG ép bạn học)
      → Vulnerability cao → mirror amplify → nurturing reward
      → = Agent có positive valence cao + ZERO mục tiêu xung đột
```

---

## §7 — VALENCE DYNAMICS: Mixed, Conflict, Flip, Violation

```
🟡 VALENCE KHÔNG TĨNH — có các dynamics phức tạp:

  ① MIXED VALENCE — positive VÀ negative CÙNG LÚC:
    → Mẹ: L1++ nhưng autonomy--
    → Công việc: L1++ (lương) nhưng L2-- (stress)
    → = Nhiều channels, mỗi cái valence riêng → body experience = MIXED
    → = Yêu-ghét, thích-chán, cần-ngại = TẤT CẢ là mixed valence
    → = Không phải bất thường — là BÌNH THƯỜNG khi agent phức tạp

  ② VALENCE CONFLICT — khi 2 entity xung đột:
    → Muốn chơi game (entity: game, valence ++) nhưng phải học (entity: bài, valence mixed)
    → Mẹ muốn con học (valence mẹ mixed vì ép) vs bạn rủ đi chơi (valence bạn ++)
    → = NHIỀU entities với valence KHÁC NHAU cạnh tranh cho CÙNG resource (time, attention)
    → = Drive.md xử lý conflict này (tổng hợp → action emerge)

  ③ VALENCE FLIP — khi entity THAY ĐỔI TOÀN DIỆN:
    → Bạn thân phản bội: trust++++ → trust----
    → Phát hiện tổ chức từ thiện gian lận tiền quyên góp: valence org flip
    → Kẻ thù cứu mạng: valence flip positive
    → = HIẾM nhưng MẠNH — phá compiled schema → cần rebuild

    Flip NHANH hay CHẬM:
    → Phụ thuộc DEPTH of compiled schema:
      Schema nông (quen 1 tuần) → flip nhanh, ít đau
      Schema sâu (quen 10 năm) → flip CHẬM, RẤT ĐAU, có thể deny

  ④ VIOLATION & OVERGENERALIZE — khi valence bị phá:

    Investment thấp → violation → update 1 entity, move on:
      → Tổ chức từ thiện X phốt → dừng cho X → tìm Y → ok

    Investment CAO → violation → NHIỀU kịch bản:

      a) Recalibrate chính xác (healthy, KHÓ):
         "Người NÀY phản bội. Không phải TẤT CẢ."
         → Update valence 1 entity. Vẫn open.

      b) Overgeneralize (phổ biến, evolutionary safe):
         "Người NÀY phản bội → LOẠI NGƯỜI NÀY đều xấu → TẤT CẢ đều xấu"
         → Schema extend valence negative ra CATEGORY
         → "Bị lừa 1 lần → không tin AI nữa" = overgeneralize

      c) Sụp đổ (khi violation phá ANCHOR):
         Schema "tình yêu = tốt đẹp" = ANCHOR cho nhiều behaviors
         Phản bội phá anchor → cascade collapse → "tôi là ai nếu không..."
         → = Anchor-Schema.md: anchor mất → mọi thứ build trên đó collapse

    TẠI SAO overgeneralize PHỔ BIẾN:
      → Violation → threat signal → body default Logic mode + conservative
      → "Tốt hơn tránh HẾT còn hơn bị LẠI" = false positive > false negative
      → = Cùng cơ chế bụi cây Việt Cộng: tránh hết bụi cây > bỏ qua 1 cái có VC
      → = Evolutionary safe, nhưng socially suboptimal

  ⑤ VALENCE DECAY — valence MỜ DẦN nếu không reinforce:
    → Bạn cũ không gặp 10 năm: valence vẫn có nhưng MỜ
    → Gặp lại → trigger compiled schema → valence SÁNG lại
    → NHƯNG: nếu entity ĐÃ thay đổi → compiled valence KHÔNG match reality
    → = "Gặp bạn cũ → thấy khác" = compiled valence vs current reality
```

---

## §8 — HONEST ASSESSMENT

```
VERIFIED (🟢):
  → Negativity bias: robust finding trong psychology
  → Multi-channel emotional processing: không ai tranh cãi cảm xúc phức tạp
  → Mixed feelings (ambivalence): well-documented phenomenon
  → Overgeneralization after trauma: established pattern

FRAMEWORK REASONING (🟡):
  → Valence as explicit multi-channel assessment framework: new formalization
    (concept "valence" tồn tại trong psychology, nhưng multi-channel profile = framework framing)
  → 4 nguồn hình thành (direct, observed, inherited, context): logic chain
  → Valence update dynamics (reinforce, revision, flip): consistent với learning theory
  → Meta-dimensions (trust, predictability, replaceability): framework addition

HYPOTHESIS (🔴):
  → Valence profile structure chính xác như mô tả: chưa test
    (multi-channel đúng, nhưng CỤ THỂ channels nào là debate)
  → Body "tính toán" valence vô thức: mechanism CỤ THỂ chưa rõ
    (neuroscience biết emotional valuation xảy ra, nhưng chi tiết process chưa rõ)
  → PFC valence vs body valence conflict: logical nhưng chưa formalize rõ

CÂU HỎI MỞ:
  → Valence lưu ở ĐÂU trong não? Amygdala? Distributed?
  → Cơ chế "tính" valence: weighted sum? Priority? Context-dependent switching?
  → Valence decay rate: có phải exponential? Hay step function?
  → "Vô thức đánh giá" = cụ thể circuit nào?
  → Valence inheritance (từ cộng đồng): mechanism CỤ THỂ? (mirror? verbal? ritual?)
```

---

## §9 — CROSS-REFERENCES

```
DOMAIN INTERACTION:
  → Domain-Interaction.md §5 — overview Valence trong flow
  → Object-Agent.md §3 — classification quyết định valence complexity
  → Logic-Modeling.md — processing mode ảnh hưởng cách tính valence
  → Emergent-Patterns.md — patterns emerge từ sustained valence
  → Domain-Mechanisms.md — mirror mechanism phục vụ valence assessment

FRAMEWORK:
  → Core-v7.5-Draft.md §2 — Body-Base L0-L3 (channels mà valence đánh giá)
  → Drive.md — bước SAU valence (tổng hợp → action)
  → Body-Dissonance.md — 14+ dạng dissonance signal
  → Anchor-Schema.md — anchor collapse khi valence flip phá anchor
  → Imagine-Final.md — preview valence TRƯỚC khi hành động

CASES REFERENCE:
  → Empathy-Mirror.md (backup) §5 — perceived ability modulate drive
  → Empathy-Mirror.md (backup) §6.5 — phân phối tài nguyên (surplus valence)
  → Connection.md (backup) §7 — 1 drive × N contexts
  → Conflict-Dynamics.md — conflict patterns (valence dynamics)
```
