# Domain Interaction — Cách Con Người Tương Tác Với Thế Giới

> **Bạn đói → tìm thức ăn → ăn → hết đói.**
> **Bạn sợ → nhận diện mối nguy → tránh → an toàn.**
> **Bạn cô đơn → tìm người → nói chuyện → dễ chịu hơn.**
>
> Nhu cầu khác. Target khác. Nhưng CÙNG 1 FLOW:
> **Body-need → tìm entity trong domain → tương tác → feedback → loop.**
>
> Giữa "body cần gì" và "hành động cụ thể" có 1 hệ thống
> phân loại, xử lý, đánh giá, và quyết định —
> phần lớn VÔ THỨC, chạy liên tục, không bao giờ tắt.
>
> File này: hệ thống đó LÀ GÌ và hoạt động THẾ NÀO.

---

> **Trạng thái:** DRAFT v0.5 — synthesis từ 2 sessions phân tích sâu
> **Ngày:** 2026-04-12
> **Mục đích:** Overview toàn bộ hệ thống Domain Interaction —
> cách con người phân loại, xử lý, đánh giá, và tương tác với
> MỌI entity trong domain (đồ vật, con người, động vật, ý tưởng,...).
> File này = BẢN ĐỒ TỔNG. Muốn sâu → đọc file chi tiết.
> **Vị trí:** Core-Deep-Dive/Domain/ (file overview, phía TRÊN các file chi tiết)
> **Flow đọc:**
>   **Domain-Interaction.md** (file NÀY — overview)
>   ├── Object-Agent.md (classification)
>   ├── Logic-Modeling.md (processing — ở Core-Deep-Dive/)
>   ├── Valence.md (evaluation)
>   ├── Emergent-Patterns.md (patterns: connection, enemy, nurturing,...)
>   └── Domain-Mechanisms.md (mirror, imagine-final, feedback)
> **Tiền đề:**
>   Core-v7.5-Draft.md §2 (Body-Base L0-L3)
>   Core-v7.5-Draft.md §6 (Schema detect body-need → trigger drive)
>   Drive.md (HOW drives combine → action)
>   Body-Dissonance.md (14+ signals)
>   Logic-Modeling.md (2 processing modes)
>   Mirror-Neuron-Analysis.md (Object-Agent discovery + mirror analysis)
> **Liên quan mainstream:**
>   🟢 Spelke Core Knowledge Systems (2007) — object vs agent
>   🟢 VTC neuroimaging (eLife 2019) — animate/inanimate binary
>   🟢 Social Baseline Theory (Coan & Beckes 2015) — brain defaults to social
>   🟢 Mere Presence Effect (2024-2025) — passive social recalibration
>   🟢 Bucharest Early Intervention Project (Nelson et al.) — agent deprivation damage
>   🟢 Dual Process Theory (Kahneman 2011) — basis for Logic-Modeling
> **⚠️ 🟡 Framework synthesis — components established, integration mới**
> **Quy ước:** 🟢 Research support | 🟡 Suy luận từ framework | 🔴 Hypothesis

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — DOMAIN INTERACTION LÀ GÌ
- §2 — FLOW TỔNG THỂ
- §3 — CLASSIFICATION: Object ↔ Agent
- §4 — PROCESSING: Logic ↔ Modeling
- §5 — VALENCE: Body Đánh Giá Entities
- §6 — AGENT INPUT = BODY-BASE NEED
- §7 — EMERGENT PATTERNS
- §8 — MECHANISMS
- §9 — KEY INSIGHTS: Empathy và Connection Redefine
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 DOMAIN INTERACTION TRONG KIẾN TRÚC:

  Framework trước Domain Interaction:
    Body-Base (needs) → Drive → Action → Feedback
    = ĐÃ TỐT: mô tả TẠI SAO con người hành động

  CÒN THIẾU: HOW con người xử lý domain entities?
    → Cái bàn vs con chó → não xử lý KHÁC NHAU, vì sao?
    → Mẹ cho ăn nhưng cũng ép học → yêu và ghét CÙNG LÚC, vì sao?
    → Người ăn xin → cho tiền → nhẹ nhõm. Không cho → áy náy. Vì sao?
    → Bụi cây bình thường vs bụi cây chiến trường → sợ hãi hoàn toàn khác, vì sao?

  Domain Interaction = TẦNG GIỮA: giữa "body cần gì" và "làm gì"

  ┌──────────────────────────────────────────────────────────────┐
  │ BODY-BASE (L0-L3) — NEEDS                                    │
  │   Body có needs → tạo dissonance khi thiếu, reward khi đủ   │
  └──────────────────────┬───────────────────────────────────────┘
                         ↓ body-need signal
  ┌──────────────────────────────────────────────────────────────┐
  │ DOMAIN INTERACTION (file NÀY)                                │
  │                                                              │
  │   ① CLASSIFY: Entity này là Object hay Agent?                │
  │   ② PROCESS:  Dùng Logic hay Modeling?                       │
  │   ③ EVALUATE: Entity này ảnh hưởng body channels thế nào?   │
  │      (= VALENCE)                                             │
  │   ④ PATTERNS: Relationship nào đã hình thành?                │
  │      (connection, enemy, dependency,...)                      │
  │   ⑤ MECHANISMS: Mirror đọc state, Imagine preview outcome   │
  │                                                              │
  │   → Tổng hợp → DRIVE hành động cụ thể                       │
  └──────────────────────┬───────────────────────────────────────┘
                         ↓ drive + direction
  ┌──────────────────────────────────────────────────────────────┐
  │ DRIVE INTEGRATION (Drive.md)                                  │
  │   Nhiều drives đồng thời → tổng hợp → ACTION emerge          │
  └──────────────────────┬───────────────────────────────────────┘
                         ↓ action
  ┌──────────────────────────────────────────────────────────────┐
  │ DOMAIN FEEDBACK                                               │
  │   Domain phản hồi → body signals (Satisfaction/Reward/Diss.) │
  │   → Update valence → update schema → LOOP lại                │
  └──────────────────────────────────────────────────────────────┘


  PHÂN BIỆT DOMAIN INTERACTION vs DRIVE.MD:
    Drive.md = HOW nhiều drives COMBINE → action emerge
    Domain Interaction = HOW não PROCESS domain entities → tạo drive cụ thể
    = 2 file BỔ SUNG, không trùng:
      Domain Interaction: "tôi đánh giá con chó này nguy hiểm" (valence)
      Drive.md: "drive tránh con chó + drive đi chợ → action: đi đường vòng" (combine)
```

---

## §1 — DOMAIN INTERACTION LÀ GÌ

```
🟡 ĐỊNH NGHĨA:

  Domain = MỌI THỨ bên ngoài body mà body tương tác hoặc CÓ THỂ tương tác.
    → Đồ vật: dao, bàn, bom, mẫu ảnh
    → Sinh vật: mẹ, bạn, con chó, con gián
    → Tập thể: nhóm bạn, quân đội, cộng đồng
    → Trừu tượng: Thiên Chúa, ý tưởng, giấc mơ
    → Môi trường: thời tiết, địa hình, bụi cây

  Domain Interaction = TOÀN BỘ quá trình não xử lý domain entities:
    Phân loại chúng → Xử lý thông tin → Đánh giá ảnh hưởng →
    Hình thành patterns → Quyết định tương tác

  ĐẶC ĐIỂM:
    ○ LIÊN TỤC — không bao giờ tắt (kể cả khi ngủ: process trong mơ)
    ○ PHẦN LỚN VÔ THỨC — PFC chỉ tham gia khi cần (~5-15% quyết định)
    ○ PHỤC VỤ BODY-BASE — MỌI tương tác ultimately = body-need fulfillment
    ○ EMERGENT — patterns (connection, enemy,...) emerge từ tương tác lặp lại
    ○ BIDIRECTIONAL — body ảnh hưởng domain, domain feedback lại body


  MỤC TIÊU CỦA DOMAIN INTERACTION:

    ⭐ MAP DOMAIN CHÍNH XÁC — không phải smooth melody

    Smooth melody = BYPRODUCT khi domain mapping tốt
    Smooth melody MÀ KHÔNG map domain = dead end

    Bằng chứng (gương):
      → Trẻ nhìn gương: prediction accuracy 100%, novelty 0
      → Melody smooth — nhưng ZERO domain expansion
      → Trẻ BỎ sau 1 lúc — body detect "không có gì mới trong domain"

    Bằng chứng (trẻ được chăm quá kỹ):
      → Mọi dissonance được bố mẹ fix hết
      → Melody smooth — nhưng chỉ map domain "có bố mẹ fix"
      → Ra domain real KHÔNG có bố mẹ → melody KHÔNG work → nguy hiểm

    → Domain Interaction MỤC TIÊU = map domain ngày càng chính xác
    → Chấp nhận dissonance tạm thời → map domain → reward tổng CAO hơn
```

---

## §2 — FLOW TỔNG THỂ

```
🟡 FLOW CỐT LÕI — loop liên tục:

  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  BODY-BASE (L0-L3)                                                  │
  │  Body detect: cái gì đó cần / thiếu / dư / bị đe dọa              │
  │                                                                     │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  ↓
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  ① CLASSIFY: Entity này là GÌ?                                     │
  │                                                                     │
  │     VTC (ventral temporal cortex) auto-classify:                    │
  │       → Object (bàn, dao, bom,...) = deterministic, physics-based  │
  │       → Agent (mẹ, bạn, chó,...) = goal-directed, unpredictable    │
  │                                                                     │
  │     Hardware binary — nhưng schema CAN override:                    │
  │       → Tượng Phật (object → perceived agent)                      │
  │       → "Beef" (agent [con bò] → relabeled object [thịt])         │
  │       → Bụi cây chiến trường (object → potential agent container)  │
  │                                                                     │
  │     → Chi tiết: Object-Agent.md                                     │
  │                                                                     │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  ↓
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  ② PROCESS: Tính toán THẾ NÀO?                                     │
  │                                                                     │
  │     Logic mode: rules-based, deterministic                          │
  │       → "2+3=5", "lửa = nóng = tránh", "dao cắt = đau"           │
  │       → MAP — chính xác TRONG scope đã biết                        │
  │                                                                     │
  │     Modeling mode: simulation-based, probabilistic                  │
  │       → "Mẹ đang cáu VÌ...", "Nếu tôi nói thế NÀY thì..."       │
  │       → LA BÀN — hướng kể cả vùng CHƯA biết                       │
  │                                                                     │
  │     Object default Logic, Agent default Modeling                    │
  │     Nhưng CẢ 4 combinations xảy ra (§4)                            │
  │                                                                     │
  │     → Chi tiết: Logic-Modeling.md                                   │
  │                                                                     │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  ↓
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  ③ EVALUATE: Entity này ẢNH HƯỞNG body channels thế nào?          │
  │                                                                     │
  │     = VALENCE PROFILE — multi-channel assessment:                   │
  │                                                                     │
  │       Entity X → body đánh giá:                                     │
  │         L0: safe / dangerous?                                       │
  │         L1: useful / harmful cho survival?                          │
  │         L2: pleasant / unpleasant?                                  │
  │         L3: interesting / boring? status+/-? mine / not-mine?       │
  │         + Trust: high / low?                                        │
  │         + Predictability: high / low?                               │
  │         + Replaceability: easy / hard?                              │
  │                                                                     │
  │     Object valence: ĐƠN GIẢN, ít thay đổi                         │
  │       Dao: dangerous → useful (sau khi học cách dùng)               │
  │                                                                     │
  │     Agent valence: PHỨC TẠP, đa kênh, thay đổi liên tục           │
  │       Mẹ: L1++ (cho ăn) + L2++ (comfort) + autonomy-- (ép học)    │
  │       = YÊU VÀ GHÉT cùng lúc — multi-channel reality              │
  │                                                                     │
  │     → Chi tiết: Valence.md                                          │
  │                                                                     │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  ↓
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  ④ DRIVE → ACTION                                                   │
  │                                                                     │
  │     Valence + Body-need + Context → Drive cụ thể:                   │
  │       → Positive valence + body-need match → APPROACH               │
  │       → Negative valence + threat → AVOID / FIGHT                   │
  │       → Mixed valence → CONFLICT (yêu-ghét, dependency)             │
  │       → Surplus + agent deficit detected → SHARE (cho đi)           │
  │                                                                     │
  │     Nhiều drives ĐỒNG THỜI → tổng hợp → action EMERGE              │
  │     → Chi tiết: Drive.md                                            │
  │                                                                     │
  └───────────────────────────────┬─────────────────────────────────────┘
                                  ↓
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │  ⑤ FEEDBACK → UPDATE → LOOP                                        │
  │                                                                     │
  │     Action → Domain phản hồi:                                       │
  │       → Body-Satisfaction: "đủ rồi" → drive GIẢM                   │
  │       → Body-Reward: "hay, tiếp" → drive GIỮ/TĂNG                  │
  │       → Body-Dissonance: "chưa ổn" → drive SHIFT/TĂNG              │
  │                                                                     │
  │     Feedback → UPDATE:                                              │
  │       → Valence profile entity X CẬP NHẬT                          │
  │       → Schema COMPILE nếu pattern lặp lại                         │
  │       → Trust TĂNG/GIẢM                                             │
  │       → Classification CÓ THỂ shift (Object↔Agent)                 │
  │                                                                     │
  │     → LOOP lại ① — liên tục, không bao giờ dừng                    │
  │                                                                     │
  └─────────────────────────────────────────────────────────────────────┘


  VÍ DỤ FLOW HOÀN CHỈNH — Bạn B cho mượn bút:

    Body-need: đang cần bút viết (L3 Learning → dissonance nhẹ)
    ① Classify: Bạn B = Agent (người, ngồi cạnh)
    ② Process: Modeling — "bạn B có vẻ có 2 bút, có thể cho mượn"
    ③ Evaluate: Valence hiện tại [B] = neutral (chưa biết nhiều)
    ④ Drive: approach + hỏi mượn → B cho → bút có
    ⑤ Feedback: Body-Satisfaction "có bút" + Valence update [B] = positive nhẹ
    → Schema update: "B = người tốt, có thể nhờ"

  VÍ DỤ FLOW HOÀN CHỈNH — Bụi cây chiến trường:

    Body-need: L0 Alive (đang trong vùng chiến sự)
    ① Classify: Bụi cây = Object... nhưng schema "VC ẩn trong bụi" →
       RECLASSIFY: bụi cây = potential Agent container
    ② Process: SWITCH từ Logic (bụi cây = thực vật) sang Modeling
       ("có ai ẩn trong đó không? nếu có thì sẽ bắn từ hướng nào?")
    ③ Evaluate: Valence = L0 THREAT cực cao (false negative = chết)
    ④ Drive: freeze + scan + ready to fire
    ⑤ Feedback: không có gì xảy ra → giảm nhẹ, nhưng schema VẪN active
       (vì asymmetric cost: bỏ qua agent thật = chết > phản ứng thừa = mất energy)
```

---

## §3 — CLASSIFICATION: Object ↔ Agent

```
🟢 2 CLASSIFICATION MODES CƠ BẢN:

  Não phân loại MỌI entity trong domain thành 1 trong 2:

  ┌─────────────────────┬─────────────────────────────────┐
  │ OBJECT              │ AGENT                            │
  ├─────────────────────┼─────────────────────────────────┤
  │ Deterministic        │ Non-deterministic                │
  │ Physics-based rules  │ Goal-directed behavior           │
  │ Cohesion, contact    │ Self-propelled, contingent       │
  │ Predictable          │ Unpredictable (có mục tiêu riêng)│
  │ Không có state riêng │ CÓ state riêng (vui/buồn/đói)  │
  │ Không reciprocate    │ CÓ reciprocate (phản hồi lại)   │
  └─────────────────────┴─────────────────────────────────┘

  🟢 Evidence:
    → Spelke Core Knowledge (2007): trẻ SƠ SINH đã phân biệt
    → VTC neuroimaging (eLife 2019): vùng não KHÁC xử lý animate vs inanimate
    → = Hardware-level binary — không phải learned

  🔴 Schema CAN override (framework hypothesis, evidence rõ):
    → Object → Agent: tượng Phật, mẫu ảnh Đức Mẹ, gấu bông "biết buồn"
    → Agent → Object: "beef" (con bò → thịt), kẻ thù bị dehumanize
    → Conflict ở ranh giới: chân ếch co giật (đã chết nhưng cử động), uncanny valley

  → Chi tiết: Object-Agent.md
```

---

## §4 — PROCESSING: Logic ↔ Modeling

```
🟡 2 PROCESSING MODES — file ĐÃ CÓ (Logic-Modeling.md):

  ┌──────────────────────┬──────────────────────────────┐
  │ LOGIC                │ MODELING                      │
  ├──────────────────────┼──────────────────────────────┤
  │ Rules-based           │ Simulation-based              │
  │ Deterministic         │ Probabilistic                 │
  │ MAP — chính xác      │ LA BÀN — hướng               │
  │   trong scope đã biết│   kể cả vùng chưa biết       │
  │ ANCHOR               │ EXPLORE                       │
  │ "Biết rồi → apply"  │ "Chưa biết → imagine → test" │
  └──────────────────────┴──────────────────────────────┘

  2×2 MATRIX — Object-Agent × Logic-Modeling:

  ┌──────────────┬──────────────────────┬─────────────────────────┐
  │              │ LOGIC                │ MODELING                 │
  ├──────────────┼──────────────────────┼─────────────────────────┤
  │ OBJECT       │ ⭐ DEFAULT           │ Insight hack             │
  │              │ Vật lý, toán, kỹ    │ (Einstein: model light   │
  │              │ thuật đã biết        │  như agent → insight)     │
  ├──────────────┼──────────────────────┼─────────────────────────┤
  │ AGENT        │ ⚠️ Dehumanize zone  │ ⭐ DEFAULT               │
  │              │ Hệ thống hóa người  │ Empathy, social,         │
  │              │ (agent → quy tắc)   │ predict behavior          │
  └──────────────┴──────────────────────┴─────────────────────────┘

  Loop: Modeling explore → Logic verify → Modeling refine → Logic anchor mới
  = Map mở rộng liên tục

  → Chi tiết: Logic-Modeling.md (Core-Deep-Dive/)
```

---

## §5 — VALENCE: Body Đánh Giá Entities

```
🟡 MỌI entity trong domain đều có VALENCE PROFILE:

  VALENCE = "entity này ảnh hưởng body channels CỦA TÔI thế nào?"

  Multi-channel — KHÔNG phải 1 trục tốt/xấu:
    Mẹ: L1++ (cho ăn) + L2++ (comfort) + autonomy-- (ép học)
    = YÊU VÀ GHÉT cùng lúc — multi-channel reality
    = KHÔNG mâu thuẫn — chỉ là NHIỀU channels, MỖI cái 1 valence

  Dynamic — thay đổi theo experience:
    Dao: L0-- (cắt tay lần đầu) → L1++ (học cách dùng → hữu ích)
    Bạn B: neutral → L3+ (cho bút) → L3-- (phá tập trung) → cắt

  Object valence = ĐƠN GIẢN:
    Ít channels, tương đối ổn định, không reciprocate

  Agent valence = PHỨC TẠP:
    Nhiều channels, thay đổi liên tục, agent CÓ mục tiêu riêng
    Agent CÓ THỂ xung đột (mẹ muốn con học ≠ con muốn chơi)
    Agent model NGƯỢC lại mình (bạn cũng đang đánh giá mình)
    Agent KHÓ thay thế (mỗi agent unique)

  → Chi tiết: Valence.md
```

---

## §6 — AGENT INPUT = BODY-BASE NEED

```
⭐ PHÁT HIỆN QUAN TRỌNG — agent input không chỉ "tốt khi có" mà là BODY CẦN:

  🟢 Social Baseline Theory (Coan & Beckes 2015):
    → Não người DEFAULT ở trạng thái CÓ agent gần
    → Ở 1 mình = DEVIATION từ default = não phải LÀM THÊM VIỆC
    → Não "at rest" hơn khi social resources available
    → Có partner tin cậy → GIẢM amygdala response to threat
    → = Não THIẾT KẾ giả định có agent — ở 1 mình = chế độ "thiếu tài nguyên"

  🟢 Mere Presence Effect (nghiên cứu 2024-2025):
    → CHỈ CẦN có người gần (không cần tương tác):
      Tăng effective connectivity trong attentional brain networks
      Modulate fronto-parietal areas, default mode regions
      Pupil size thay đổi (arousal level shift)
    → = AUTOMATIC recalibration — không cần conscious evaluation
    → = Ngồi trong quán cà phê 1 mình DỄ CHỊU HƠN ở nhà 1 mình

  🟢 Bucharest Early Intervention Project (Nelson et al.):
    → Trẻ mồ côi Romania: CÓ food, shelter → THIẾU sustained agent interaction
    → Kết quả: IQ giảm 20+ điểm, giảm brain volume, attachment disorders
    → Vùng não bị ảnh hưởng NẶNG NHẤT = social + cognitive areas
    → Foster care TRƯỚC 24 tháng → recover đáng kể
    → = Agent input CẦN cho neural development — thiếu = DAMAGE

  🟢 Solitary confinement (Grassian 2006):
    → Food, shelter, safety ĐỦ — agent input GẦN ZERO
    → Hallucinations, anxiety, cognitive deterioration trong VÀI NGÀY
    → = Body CRASH nhanh dù L1 met → agent input ≠ "tiện" mà = NEED

  🟢 Harlow's Monkeys (1958):
    → Khỉ con chọn cloth "mother" (no food, có touch)
      OVER wire "mother" (có food, no touch)
    → = Agent presence/touch = SEPARATE need, không thay thế bằng food


  AGENT INPUT SPECTRUM — phổ từ cơ bản đến sâu:

  ┌──────────┬───────────────────────────────────────────────────────┐
  │ Level    │ Mô tả                                                │
  ├──────────┼───────────────────────────────────────────────────────┤
  │ Level 0  │ MERE PRESENCE — chỉ biết có agent gần                │
  │          │ Brain auto-recalibrate attention networks             │
  │          │ Ngồi quán cà phê 1 mình, thấy dễ chịu hơn ở nhà   │
  ├──────────┼───────────────────────────────────────────────────────┤
  │ Level 1  │ PASSIVE OBSERVATION — quan sát agents hoạt động      │
  │          │ Nhặt patterns vô thức: cách người khác đi, nói      │
  │          │ Ra đường thấy mọi người → calibrate nhẹ nhàng        │
  ├──────────┼───────────────────────────────────────────────────────┤
  │ Level 2  │ LIGHT INTERACTION — chào hỏi, mua hàng, xã giao     │
  │          │ Mirror fire nhẹ → agent PHẢN HỒI lại → verify mình  │
  │          │ Dunbar ~150 acquaintances                             │
  ├──────────┼───────────────────────────────────────────────────────┤
  │ Level 3  │ REGULAR INTERACTION — bạn bè, đồng nghiệp           │
  │          │ Chunks exchange, shared novelty, co-regulation nhẹ   │
  │          │ Virtual chunks accessible                             │
  │          │ Dunbar ~50 friends, ~15 close                         │
  ├──────────┼───────────────────────────────────────────────────────┤
  │ Level 4  │ DEEP SUSTAINED — bạn thân, gia đình                  │
  │          │ Melody calibration SÂU, co-regulation MẠNH           │
  │          │ Virtual chunks RELIABLE, error correction             │
  │          │ Schema convergence qua năm                            │
  │          │ Dunbar ~5 intimate                                    │
  └──────────┴───────────────────────────────────────────────────────┘

  = Level 0-1: BODY-BASE NEED THẬT (brain cần agent input để function)
  = Level 2-4: COMPILED META-DRIVE (cụ thể ai, bao nhiêu, kiểu gì = learned)

  TƯƠNG TỰ HUNGER:
    "Đói" = body-base (cells cần glucose) — hardware need
    "Thèm phở" = compiled preference — learned, specific
    "Cần agent input" = body-base (brain cần calibration) — hardware need
    "Muốn gặp mẹ / bạn thân" = compiled preference — learned, specific


  TẠI SAO AGENT INPUT HIỆU QUẢ HƠN MỌI INPUT KHÁC:

    Agent = công cụ map domain HIỆU QUẢ NHẤT vì:
      ① Independent sensor — body KHÁC verify cùng domain → dual check
      ② Có chunks tôi không có → domain data MIỄN PHÍ
      ③ Unpredictable → TỰ ĐỘNG tạo prediction error → novelty → learning
      ④ Mirror mechanism → tự động calibrate schema TÔI (không cần PFC effort)
      ⑤ Phản hồi hành vi tôi → biết tôi map domain đúng/sai

    Gương KHÔNG cho được bất kỳ thứ nào trong 5 cái trên
    Object cho được 1 phần nhưng cạn novelty nhanh (deterministic)
    → Body PREFER agent input vì agent = RICHEST domain mapping source
```

---

## §7 — EMERGENT PATTERNS

```
🟡 Khi domain interaction LẶP LẠI → patterns EMERGE:

  ┌──────────────────────┬─────────────────────────────────────────────┐
  │ Pattern              │ Emerge từ                                    │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ CONNECTION           │ Sustained mutual POSITIVE valence (agent)   │
  │                      │ + body-base agent input need                │
  │                      │ Virtual chunks, calibration, co-regulation  │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ ENEMY / THREAT       │ Sustained NEGATIVE valence (agent/object)   │
  │                      │ Drive: avoid, fight, destroy                │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ NURTURING            │ Giving + vulnerability amplification        │
  │                      │ Mirror × vulnerability cues × ability       │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ "CHO ĐI"            │ Surplus + mirror reward > keep reward       │
  │                      │ Phân phối tài nguyên tự nhiên               │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ DEPENDENCY           │ High positive valence + irreplaceable       │
  │                      │ Không cắt được dù có channels negative     │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ YÊU + GHÉT          │ Mixed valence multi-channel (cùng 1 agent)  │
  │                      │ Mẹ: positive L1 + negative autonomy        │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ GROUP DYNAMICS       │ Multi-agent amplification                    │
  │                      │ Virtual chunks pooling, Dunbar limits       │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ VIOLATION & RECOVERY │ Khi pattern bị phá (phản bội, phốt)        │
  │                      │ Schema collapse → recalibrate / overgeneralize│
  └──────────────────────┴─────────────────────────────────────────────┘

  MỌI patterns đều EMERGE — không phải pre-designed:
    → Không có module "connection" hay "enemy" riêng
    → Patterns = KẾT QUẢ của domain interaction lặp lại
    → Compiled thành schema → ảnh hưởng tương tác tiếp theo

  → Chi tiết: Emergent-Patterns.md
```

---

## §8 — MECHANISMS

```
🟡 CÁC MECHANISMS PHỤC VỤ DOMAIN INTERACTION:

  ① MIRROR — đọc state agent:
    = CÁCH agent processing hoạt động, KHÔNG phải module riêng
    3 layers:
      Pattern Matching (vô thức, body-level) — thấy mặt buồn → body fire tương tự
      Agent Modeling (PFC, Theory of Mind) — model TẠI SAO agent ở state đó
      Schema Simulation (compiled, không cần input thật) — cầu nguyện với tượng
    → Phục vụ: đánh giá valence agent CHÍNH XÁC hơn
    → Mainstream gọi "empathy" = tập hợp 3 layers này

  ② IMAGINE-FINAL trong domain interaction:
    = Preview outcome TRƯỚC khi hành động
    "Nếu tôi cho bạn kẹo → bạn vui → mirror reward"
    "Nếu tôi đi đường này → bụi cây → nguy hiểm"
    → Phục vụ: chọn action tối ưu cho body-base

  ③ SCHEMA trong domain interaction:
    = Compiled patterns từ tương tác trước
    Valence profiles, trust levels, behavioral predictions
    → Phục vụ: không cần re-evaluate từ đầu mỗi lần gặp lại

  ④ FEEDBACK LOOP:
    = Body receives Satisfaction/Reward/Dissonance → update valence → loop
    → Phục vụ: continuous refinement of domain mapping

  → Chi tiết: Domain-Mechanisms.md
```

---

## §9 — KEY INSIGHTS: Empathy và Connection Redefine

```
⭐ SAU PHÂN TÍCH, 2 CONCEPTS CẦN REDEFINE:

  ① "EMPATHY" — từ system riêng → thành CÁCH agent processing hoạt động:

    CŨ (Empathy-Mirror.md):
      → Empathy-Mirror = cross-cutting mechanism RIÊNG BIỆT
      → Tạo bản sao body-state sinh vật khác trong body mình
      → Hệ thống tách biệt, feed vào mọi channels

    MỚI (Domain Interaction):
      → "Empathy" = TÊN mainstream đặt cho CÁCH agent processing đọc + phản hồi state
      → Mirror = mechanism agent processing DÙNG (không phải system riêng)
      → Khi não classify entity = Agent → TỰ ĐỘNG: detect state, model intent, mirror
      → Đó chính là "empathy" — không cần module tách biệt

    VẪN ĐÚNG:
      → Mirror tạo bản sao body-state (đúng, đây là cách mechanism hoạt động)
      → Feed vào mọi channels (đúng, vì agent ảnh hưởng mọi channels)
      → 2 tầng: vô thức + PFC (đúng, consistent)
      → 4 yếu tố mirror strength (đúng, consistent với agent processing)

    THAY ĐỔI:
      → Từ "system riêng cross-cutting" → "cách agent processing tự nhiên hoạt động"
      → Không cần file RIÊNG cho empathy — nằm trong Domain Mechanisms
      → Empathy-Mirror.md → backup (content absorbed)


  ② "CONNECTION" — từ channel/layer riêng → thành emergent pattern + body-base need:

    CŨ (Connection.md + Core-v7.5):
      → Connection = drive ở L2 + emergent property giữa melodies
      → Tension: vừa là body-need, vừa là emergent, chưa resolve

    MỚI (Domain Interaction):
      → AGENT INPUT = body-base need THẬT (Level 0-1):
        Não cần agent input cho calibration, development, regulation
        Thiếu hoàn toàn = crash (solitary confinement) / damage (orphans)
        = Body-base need ngang hàng other needs
      → CONNECTION (Level 2-4) = emergent PATTERN:
        Sustained mutual positive valence với specific agents
        Virtual chunks, melody calibration, co-regulation
        = COMPILED trên nền body-base need
      → RESOLVE tension: body-base need (agent input) ≠ connection (specific bonds)
        Cần agent input = hardware need
        Muốn GẦN MẸ = compiled preference build trên hardware need

    VẪN ĐÚNG:
      → Virtual chunks (đúng — key function of agent interaction)
      → Melody calibration (đúng — core mechanism)
      → Dunbar limits (đúng — hardware capacity)
      → Co-regulation (đúng — body-level function)
      → Amplify mọi layer (đúng — agent interaction enhances ALL L0-L3)

    THAY ĐỔI:
      → Từ "L2 drive riêng" → "body-base agent input need + compiled patterns"
      → Từ "emergent ở đâu?" → "emergent PATTERN trong Domain Interaction"
      → Connection.md → backup (content absorbed vào Emergent-Patterns.md)
```

---

## §10 — HONEST ASSESSMENT

```
VERIFIED (🟢 evidence rõ ràng):
  → Object-Agent classification: Spelke + VTC imaging
  → Agent input = body-base need: SBT + Mere Presence + BEIP + Solitary confinement
  → Mirror mechanism tồn tại: neuroimaging evidence
  → Empathy = multi-component: mainstream consensus

FRAMEWORK REASONING (🟡 logic consistent, chưa test trực tiếp):
  → Domain Interaction as unified flow (new integration)
  → Valence as multi-channel assessment
  → Empathy = cách agent processing hoạt động (reframe)
  → Connection = emergent pattern (reframe)
  → Agent input spectrum 5 levels
  → "Cho đi" = always has body-base reward

HYPOTHESIS (🔴 cần verify thêm):
  → Domain mapping = mục tiêu (vs smooth melody) — logic argument, chưa có direct evidence
  → Schema CAN override Object-Agent classification — evidence gián tiếp (meat paradox, etc.)
  → Logic-Modeling as independent pair — reframe của dual process, chưa phân biệt rõ với mainstream

CÂU HỎI MỞ:
  → Agent input need: nằm Ở ĐÂU trong L0-L3? L2? Hay cross-cutting?
  → Valence: cơ chế CỤ THỂ nào tính toán và lưu trữ valence?
  → Connection drive: body-base component CHÍNH XÁC ở level nào? (molecular/circuit/system)
  → Thiền sư: schema override agent input need hay reduce need?
  → Abstract agents (Thiên Chúa): đáp ứng agent input need ở level nào? (0? 1? simulate?)
```

---

## §11 — CROSS-REFERENCES

```
FILES TRONG BỘ DOMAIN INTERACTION:
  → Object-Agent.md — §3 classification chi tiết
  → Logic-Modeling.md — §4 processing chi tiết (Core-Deep-Dive/)
  → Valence.md — §5 evaluation chi tiết
  → Emergent-Patterns.md — §7 patterns chi tiết
  → Domain-Mechanisms.md — §8 mechanisms chi tiết

FILES FRAMEWORK LIÊN QUAN:
  → Core-v7.5-Draft.md — §2 Body-Base, §6 Schema-Drive
  → Drive.md — HOW drives combine → action
  → Body-Dissonance.md — 14+ dissonance signals
  → Imagine-Final.md — preview mechanism
  → Cortisol-Baseline.md — processing modes
  → Schema.md — compiled patterns
  → Chunk.md — đơn vị nhỏ nhất

FILES BACKUP (content absorbed):
  → backup/Empathy-Mirror.md — empathy mechanism chi tiết (absorbed → Domain-Mechanisms.md)
  → backup/Connection.md — connection patterns chi tiết (absorbed → Emergent-Patterns.md)

FILES RESEARCH/ANALYSIS:
  → Mirror-Neuron-Analysis.md — mirror research + Object-Agent discovery
  → Mirror-Empathy-Connection-Other/Analysis-Draft.md — session notes
  → Mirror-Empathy-Connection-Other/plan.md — restructure plan
```
