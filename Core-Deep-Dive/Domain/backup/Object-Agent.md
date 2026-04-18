# Object-Agent — 2 Classification Modes Của Não

> **Cái bàn KHÔNG thể muốn gì. Bạn BIẾT nó sẽ đứng yên.**
> **Con chó CÓ THỂ muốn gì đó. Bạn KHÔNG BIẾT nó sẽ làm gì.**
>
> Đó là sự khác biệt cơ bản nhất trong cách não xử lý thế giới:
> **Object** (vật thể) = deterministic, tuân theo vật lý.
> **Agent** (tác nhân) = non-deterministic, có mục tiêu riêng.
>
> Não classify MỌI THỨ trong domain vào 1 trong 2 loại này —
> hardware-level, binary, gần như instant — TRƯỚC khi xử lý thông tin.
>
> Nhưng schema CÓ THỂ flip classification:
> con bò → "beef", tượng Phật → "Ngài", bụi cây → "Việt Cộng".
>
> File này: 2 modes là gì, evidence, phát triển ở trẻ,
> khi nào classification bị flip, và tại sao điều này quan trọng.

---

> **Trạng thái:** DRAFT v0.5 — synthesis từ research + framework analysis
> **Ngày:** 2026-04-12
> **Mục đích:** Deep dive vào Object-Agent classification —
> cách não phân loại mọi entity trong domain, evidence cơ sở,
> phát triển theo tuổi, schema override, và implications.
> **Vị trí:** Core-Deep-Dive/Domain/ (file chi tiết, thuộc Domain Interaction)
> **Flow đọc:**
>   Domain-Interaction.md §3 (overview) → **Object-Agent.md** (file NÀY — chi tiết)
> **Tiền đề:**
>   Domain-Interaction.md (overview)
>   Logic-Modeling.md (2 processing modes — tương tác với Object-Agent)
>   Mirror-Neuron-Analysis.md (Object-Agent discovery + evidence gốc)
> **Liên quan mainstream:**
>   🟢 Spelke Core Knowledge Systems (2007) — object vs agent innate distinction
>   🟢 VTC neuroimaging (eLife 2019) — animate/inanimate brain organization
>   🟢 Infant animate detection research — 9-month motion discrimination
>   🟢 Piaget animism (1929) — agent overgeneralization in children
>   🟢 Meat Paradox (Loughnan, Bastian 2014) — Agent→Object reclassification
>   🟢 Grossman "On Killing" (1995) — combat dehumanization + distance × trauma
>   🟢 Uncanny Valley (Mori 1970) — classification boundary conflict
> **⚠️ Framework: 🟢 classification evidence rõ ràng; 🔴 schema override = hypothesis có evidence gián tiếp**
> **Quy ước:** 🟢 Research support | 🟡 Suy luận từ framework | 🔴 Hypothesis

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — 2 CLASSIFICATION MODES: Object và Agent
- §2 — EVIDENCE
- §3 — PHÁT TRIỂN Ở TRẺ
- §4 — SCHEMA OVERRIDE: Khi Classification Bị Flip
- §5 — AGENCY SPECTRUM
- §6 — TƯƠNG TÁC VỚI LOGIC-MODELING
- §7 — IMPLICATIONS CHO DOMAIN INTERACTION
- §8 — HONEST ASSESSMENT
- §9 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 OBJECT-AGENT TRONG DOMAIN INTERACTION:

  Domain Interaction flow (Domain-Interaction.md §2):
    Body-need → ① CLASSIFY → ② Process → ③ Evaluate → ④ Drive → ⑤ Feedback

  File NÀY = bước ① — CLASSIFY:
    → Entity này là Object hay Agent?
    → Quyết định CỰC SỚM trong flow, ảnh hưởng MỌI bước sau
    → Classification sai = processing sai = valence sai = hành động sai

  TẠI SAO BƯỚC NÀY QUAN TRỌNG:
    → Classify Object → não dùng Logic mode default (physics rules)
    → Classify Agent → não dùng Modeling mode default (predict goals)
    → Classify Object → valence ĐƠN GIẢN (ít channels)
    → Classify Agent → valence PHỨC TẠP (nhiều channels, reciprocal)
    → = Classification QUYẾT ĐỊNH cách não xử lý entity CÒN LẠI
```

---

## §1 — 2 CLASSIFICATION MODES: Object và Agent

```
🟢 ĐỊNH NGHĨA:

  ┌─────────────────────────────┬─────────────────────────────────────┐
  │ OBJECT                      │ AGENT                                │
  ├─────────────────────────────┼─────────────────────────────────────┤
  │ Deterministic                │ Non-deterministic                    │
  │ Tuân theo vật lý             │ Có MỤC TIÊU RIÊNG                   │
  │ Cohesion: không tự rời rạc  │ Self-propelled: tự di chuyển         │
  │ Contact: cần va chạm        │ Contingent: phản ứng tùy context     │
  │ Continuity: đường di chuyển │ Goal-directed: hành vi có đích       │
  │   liên tục, có thể predict  │   nhưng ĐƯỜNG đi unpredictable       │
  │                              │                                      │
  │ KHÔNG có state riêng         │ CÓ state riêng (vui/buồn/đói)      │
  │ KHÔNG reciprocate            │ CÓ reciprocate (phản hồi lại bạn)  │
  │ KHÔNG có mục tiêu xung đột  │ CÓ mục tiêu có thể XUNG ĐỘT       │
  │                              │                                      │
  │ Predictable                  │ Unpredictable                        │
  │ → Ít novelty dài hạn       │ → Novelty source LIÊN TỤC           │
  │ → Valence đơn giản          │ → Valence phức tạp                   │
  └─────────────────────────────┴─────────────────────────────────────┘


  VÍ DỤ PARADIGM:

    Object:
      Quả bóng: rơi xuống khi thả, nảy khi chạm sàn — LUÔN NHƯ VẬY
      Cái dao: cắt khi ấn, không tự cắt — tuân physics
      Quả bom: nổ khi kích hoạt — deterministic

    Agent:
      Con mèo: đôi khi muốn ôm, đôi khi cào — TÙY state
      Mẹ: đôi khi cho ăn, đôi khi mắng — TÙY context + mục tiêu
      Kẻ thù: có thể tấn công bất cứ lúc nào — unpredictable, goal-directed


  ⭐ BINARY — KHÔNG PHẢI SPECTRUM:

    Hardware level (VTC): Object HOẶC Agent. KHÔNG có "hơi agent".
    Giống bit: 0 hoặc 1.

    NHƯNG: schema layer CÓ THỂ tạo ra spectrum PERCEIVED:
      → Cây cối: object... nhưng "sống" → hơi agent?
      → Robot: object... nhưng cử động → hơi agent?
      → Người trong coma: agent... nhưng không respond → hơi object?
    
    = Hardware binary + Schema overlay = perceived spectrum
    = Không mâu thuẫn: VTC classify binary, PFC + schema tạo nuance
```

---

## §2 — EVIDENCE

```
🟢 SPELKE CORE KNOWLEDGE SYSTEMS (2007):

  Elizabeth Spelke: trẻ sơ sinh có CORE KNOWLEDGE innate về:
    ① Object representation: cohesion, continuity, contact
       → Trẻ SỚM hiểu: đồ vật liền, đường đi liên tục, cần tiếp xúc để di chuyển
    ② Agent representation: self-propelled, goal-directed, contingent
       → Trẻ SỚM hiểu: sinh vật tự di chuyển, có mục tiêu, phản ứng tùy context

  = 2 hệ thống KHÁC NHAU từ SƠ SINH:
    → Không phải learned — là CORE KNOWLEDGE
    → Trẻ NGẠC NHIÊN khi object vi phạm physics (vi phạm kỳ vọng test)
    → Trẻ NGẠC NHIÊN khi agent không goal-directed (vi phạm kỳ vọng test)
    → = Não ĐÃ CÓ 2 bộ kỳ vọng KHÁC NHAU cho 2 loại entities


🟢 VTC NEUROIMAGING (eLife 2019 + prior research):

  Ventral Temporal Cortex (VTC) có tổ chức:
    → Vùng RIÊNG cho animate (face, body, animal)
    → Vùng RIÊNG cho inanimate (tool, place, object)
    → = Hardware-level BINARY organization

  Quan sát:
    → Animate stimuli capture attention NHANH HƠN + GIỮ LÂU HƠN
    → 2 giai đoạn xử lý:
      ① Categorize by shape (temporoparietal) — nhanh, hardware
      ② Attention allocation animate (frontal) — agent gets MORE attention
    → = Não ĐẦU TƯ nhiều resource hơn cho agent processing

  PHÂN BIỆT QUAN TRỌNG:
    → VTC hardware: "CÓ agent hay không" = BINARY FILTER (rất sớm, gần innate)
    → Learned model: "agent đang ở STATE nào" = LEARNED MODEL (build từ interaction)
    → = 2 thứ KHÁC NHAU mà mainstream thường gộp
    → = VTC LỌC → Learned model PROCESS → Body RESPOND


🟢 INFANT ANIMATE DETECTION:

  Trẻ 9 tháng phân biệt animate/inanimate motion CHỈ từ chuyển động
  → Đốm sáng di chuyển: animate pattern → trẻ chú ý KHÁC
  → = Sớm, robust, cross-cultural

  Trẻ sơ sinh: prefer face-like patterns (innate bias)
  → 2 tháng: nhận visual mặt mẹ
  → 3 tháng: phân biệt mẹ vs người lạ
  → 6 tháng: subtle face differences
  → 6-9 tháng: stranger anxiety (= classify "agent quen" vs "agent lạ")
  → = Face processing = ưu tiên hardware cho agent detection
```

---

## §3 — PHÁT TRIỂN Ở TRẺ

```
🟢🟡 TIMELINE — từ sơ sinh tới trưởng thành:

  SƠ SINH (0-6 tháng): HARDWARE FILTER đã có
  ─────────────────────────────────────────────
    → Prefer face-like patterns (innate) 🟢
    → Distinguish animate vs inanimate motion
    → Contagious crying = pattern matching (limbic)
      — CHƯA phải "mirror" — là detect acoustic pattern quen
      — Dondi, Simion & Caltran (1999) 🟢
    → Social smile với gương (treat reflection như agent)
    → = VTC binary filter HOẠT ĐỘNG — nhưng chưa có agent MODEL

  6-12 THÁNG: BẮT ĐẦU BUILD agent model
  ─────────────────────────────────────────
    → Social referencing: nhìn mẹ trước khi react với vật lạ 🟢
      Mẹ sợ → trẻ tránh. Mẹ vui → trẻ approach.
      = Dùng biểu cảm mẹ làm PREDICTION TOOL cho outcome CỦA MÌNH
    → 9.5-12 tháng: helping behavior sơ khai 🟢
      >80% trẻ 12 tháng nhặt đồ rơi cho experimenter
      Nhưng KHÔNG nhặt khi cố ý thả (= phân biệt accident vs intention)
    → = TRANSITION: pattern matching → agent-aware processing

  14-24 THÁNG: AGENT MODEL hình thành
  ──────────────────────────────────────
    → 14-18 tháng: helping PHỨC TẠP hơn 🟢
      Phân biệt "muốn nhưng không được" vs "không muốn"
      (Warneken & Tomasello 2006, 2007)
    → 18-24 tháng: BƯỚC NHẢY LỚN 🟢
      Mirror self-recognition (rouge test, Amsterdam 1972)
      = Phân biệt SELF / OTHER rõ ràng
      → Empathic helping tăng đáng kể (an ủi, không chỉ nhặt đồ)
      → = AGENT MODEL hoàn chỉnh: dùng own-state predict other-state
    → = TRUE "mirror" / empathy BẮT ĐẦU ở đây

  2-7 TUỔI: OVERGENERALIZE rồi REFINE
  ─────────────────────────────────────
    → Animism phase (Piaget 1929) 🟢:
      Trẻ attribute feelings cho ĐỒ VẬT: "ghế bị đau", "búp bê buồn"
      = Agent model đã build → apply RỘNG HƠN CẦN THIẾT
      = OVERGENERALIZATION — giống trẻ học "chó" rồi gọi mọi 4 chân là "chó"
    → 4-7 tuổi: REFINE dần
      Agent model selective hơn: người, chó = CÓ state. Ghế = KHÔNG.
      = Brain learn boundary Object vs Agent chính xác hơn

    ⚠️ NHƯNG: nếu CỘNG ĐỒNG nói "đá có linh hồn":
      → Schema cộng đồng PREVENT refinement
      → Animism GIỮLẠI thành belief người lớn
      → = KHÔNG phải "ngây thơ" — mà vì schema cộng đồng > personal refinement

  TRƯỞNG THÀNH: COMPILED + CONTEXT-DEPENDENT
  ────────────────────────────────────────────
    → Classification gần như instant (VTC hardware)
    → NHƯNG schema overlay có thể FLIP classification (§4)
    → Context matters: cùng bụi cây → công viên vs chiến trường = classify KHÁC
    → = Hardware filter + compiled schemas + context → classification cuối cùng
```

---

## §4 — SCHEMA OVERRIDE: Khi Classification Bị Flip

```
🔴 HARDWARE = BINARY, nhưng SCHEMA CAN OVERRIDE:

  VTC classify: Object hoặc Agent (hardware, fast)
  Schema layer: CÓ THỂ override classification (compiled, slower)
  → Kết quả cuối: hardware + schema = perceived classification

  = Giống: mắt nhìn thấy ảo giác (hardware) → PFC biết là ảo (schema override)
    Nhưng body VẪN respond với classification cuối cùng


  ⭐ OBJECT → AGENT FLIP (gán "tính agent" cho vật thể):

  ┌──────────────────────┬─────────────────────────────────────────────┐
  │ Case                 │ Cơ chế                                       │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Tượng Phật           │ Schema cộng đồng: "Ngài = agent, có ý chí" │
  │                      │ Ritual reinforce × hàng nghìn lần           │
  │                      │ Mirror NGƯỜI xung quanh (không mirror tượng)│
  │                      │ PFC simulate virtual agent                   │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Mẫu ảnh Đức Mẹ      │ Object nhỏ → somatic trigger cho schema     │
  │                      │ Chạm → "Đức Mẹ bảo vệ" fire → cortisol ↓  │
  │                      │ = Pure schema trigger, zero mirror          │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Cục đá được thờ      │ Animism phase (Piaget) + cộng đồng prevent │
  │                      │ refinement + social proof + ritual compile  │
  │                      │ = Mechanism tôn giáo: inject + compile +    │
  │                      │   prevent-refinement                         │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Gấu bông "biết buồn"│ Trẻ (animism) hoặc người lớn project       │
  │                      │ Agent model apply lên object quen + đặt tên │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Bụi cây chiến trường │ Object → "potential agent CONTAINER"        │
  │ ("bụi cây Việt Cộng")│ Context threat → brain reclassify mọi object│
  │                      │ CÓ THỂ chứa agent → treat như agent         │
  │                      │ Asymmetric cost: bỏ qua agent thật = chết  │
  │                      │ Phản ứng thừa = chỉ mất energy              │
  └──────────────────────┴─────────────────────────────────────────────┘

  ⭐ OBSERVATION: Body respond CÙNG PATHWAY cho tất cả:
    Mẹ thật → body feel safe → cortisol giảm
    Cục đá thiêng → body feel safe → cortisol giảm
    Mẫu ảnh nhỏ → body feel safe → cortisol giảm
    = CÙNG OUTPUT, KHÁC SOURCE
    Body KHÔNG phân biệt source — chỉ biết "có signal → respond"
    → = Tại sao tôn giáo WORK dù không có agent thật
    → = Tại sao placebo WORK
    → = Tại sao locket người yêu WORK khi xa nhau


  ⭐ AGENT → OBJECT FLIP (tước "tính agent" khỏi sinh vật):

  ┌──────────────────────┬─────────────────────────────────────────────┐
  │ Case                 │ Cơ chế                                       │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Meat Paradox         │ 🟢 Loughnan, Bastian (2014):                │
  │ (con bò → "beef")   │ 4 strategies reclassify agent → object:     │
  │                      │   ① Linguistic camouflage: "beef" not "cow" │
  │                      │   ② Dementalization: "chúng không feel"     │
  │                      │   ③ Avoidance: không nghĩ tới nguồn gốc    │
  │                      │   ④ Dissociation: "thịt" ≠ "con vật"       │
  │                      │ = Schema PHẢI reclassify để ăn được          │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Dehumanization       │ Kẻ thù = "không phải người" → object-like   │
  │ (chiến tranh)        │ Training override: 15% → 90% firing rate    │
  │                      │ 🟢 Grossman "On Killing" (1995):            │
  │                      │ Xa (ném bom): agent model không fire         │
  │                      │ Gần (thấy mặt): agent model fire → trauma   │
  │                      │ = INPUT-DEPENDENT, not hardwired             │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Medical dissociation │ Bác sĩ phẫu thuật: treat body as "object"  │
  │                      │ = Suppress agent processing để operate      │
  │                      │ = Professional schema override               │
  ├──────────────────────┼─────────────────────────────────────────────┤
  │ Sacred object disposal│ 🟢 Catholic Canon Law:                     │
  │                      │ Vật được ban phước KHÔNG được vứt rác       │
  │                      │ PHẢI đốt hoặc chôn = agent→object RITUAL   │
  │                      │ = Transition CẦN nghi thức, không flip tức thì│
  └──────────────────────┴─────────────────────────────────────────────┘


  ⚠️ CONFLICT Ở RANH GIỚI — khi classification KHÔNG RÕ:

    → Uncanny Valley (Mori 1970) 🟢:
      Robot gần giống người → khó chịu
      = VTC classify object + schema detect "gần agent" → CONFLICT
      = Dissonance giữa hardware classification và schema overlay

    → Chân ếch co giật (đã chết nhưng cử động):
      Hardware: animate motion → agent?
      Knowledge: đã chết → object?
      = CONFLICT → disgust/discomfort

    → Ăn động vật sống (live food):
      Hardware: living agent → agent processing fire
      Schema: "đây là thức ăn" → object processing
      = CONFLICT → nhiều người KHÔNG chịu nổi

    → Người trong coma:
      Hardware: human body → agent
      Observation: không respond → object-like
      = CONFLICT → ethical dilemma

  → CONFLICT ở ranh giới = EVIDENCE cho hardware binary:
    Nếu classification là spectrum → không có ranh giới → không có conflict
    CÓ conflict → CÓ ranh giới → binary classification confirmed
```

---

## §5 — AGENCY SPECTRUM

```
🟡 PERCEIVED agency SPECTRUM (hardware binary + schema overlay):

  MẸ THẬT (full agent, real-time):
    Input: visual + auditory + somatic + olfactory + timing
    Response: phi logic, unpredictable, interactive
    Agent processing: FULL — real-time model, calibrate liên tục
    Domain mapping value: CỰC CAO

  NGƯỜI LẠ:
    Input: visual + auditory + (limited somatic)
    Agent model: sơ khai, dùng species overlap (~70-90%)
    Domain mapping value: trung bình (agent nhưng ít data)

  CHÓ (30.000 năm co-evolution):
    Input: visual + auditory + somatic + olfactory
    Agent model: cross-species, learned qua interaction
    Domain mapping value: có nhưng thấp hơn người (modality overlap kém hơn)

  VIDEO CALL / SCREEN:
    Input: visual + auditory only (truncated channels)
    Agent model: dùng compiled model (nếu đã quen)
    Domain mapping value: 60-70% so với trực tiếp

  ẢNH / VIDEO KHÔNG TƯƠNG TÁC:
    Input: visual only, one-way, scripted
    Agent model: PFC simulate dựa trên compiled schema
    Domain mapping value: rất thấp — không có real feedback

  TƯỢNG / ẢNH THẦN:
    Input: visual (static) + somatic (chạm) + CONTEXT (ritual)
    Response: KHÔNG BAO GIỜ
    Agent model: 100% COMPILED SCHEMA — inject từ cộng đồng
    Domain mapping value: ZERO real — nhưng body respond VÌ SCHEMA

  MẪU ẢNH NHỎ Ở CỔ:
    Input: somatic trigger (chạm da) + visual rất nhỏ
    Agent model: pure somatic trigger cho compiled schema
    Domain mapping value: ZERO — nhưng cortisol giảm vì schema

  CỤC ĐÁ ĐƯỢC THỜ:
    Input: visual + somatic + CONTEXT (ritual cộng đồng)
    Agent model: ZERO — đá = anchor cho compiled schema
    Domain mapping value: ZERO — body respond vì SCHEMA, không vì entity

  CỤC ĐÁ BÌNH THƯỜNG:
    Input: visual + somatic
    Agent model: KHÔNG CÓ
    Classification: pure object
    Domain mapping value: rất thấp (deterministic, cạn novelty nhanh)


  ⭐ PATTERN RÕ:
    → CÀNG XUỐNG → agent processing CÀI ÍT
    → CÀNG XUỐNG → compiled schema CÀI NHIỀU
    → Body respond CÙNG PATHWAY bất kể source
    → Mẹ thật: agent processing THẬT → body respond
    → Cục đá thiêng: agent processing ZERO → schema fire → body respond CÙ 
    → = "Empathy" ở tượng/đá = KHÔNG CÓ empathy — chỉ có schema simulation
```

---

## §6 — TƯƠNG TÁC VỚI LOGIC-MODELING

```
🟡 Object-Agent × Logic-Modeling = 2 cặp INDEPENDENT:

  Object-Agent: PHÂN LOẠI (entity này là gì?)
  Logic-Modeling: XỬ LÝ (tôi tính toán thế nào?)
  
  2 cặp independent nhưng CÓ DEFAULT pairing:

  ┌──────────────┬──────────────────────┬───────────────────────────┐
  │              │ LOGIC                │ MODELING                   │
  ├──────────────┼──────────────────────┼───────────────────────────┤
  │ OBJECT       │ ⭐ DEFAULT           │ Insight mode               │
  │              │ Physics, math,       │ "Nếu tôi là tia sáng..."  │
  │              │ kỹ thuật đã biết     │ (Einstein apply agent      │
  │              │                      │  processing lên object)    │
  ├──────────────┼──────────────────────┼───────────────────────────┤
  │ AGENT        │ ⚠️ Systematize       │ ⭐ DEFAULT                 │
  │              │ "Phân tích kiểu      │ Empathy, social predict,  │
  │              │  người lạnh lùng"    │ "mẹ đang cáu vì..."      │
  │              │ Dehumanization nguy  │                            │
  │              │ hiểm khi dùng sai   │                            │
  └──────────────┴──────────────────────┴───────────────────────────┘

  Agent + Logic = VÙNG NGUY HIỂM:
    → Hệ thống hóa con người theo quy tắc = treat agent like object
    → Có ích: tâm lý học, y khoa, quản lý hệ thống
    → Nguy hiểm: dehumanization, bóc lột hệ thống, genocide "logic"

  Object + Modeling = VÙNG INSIGHT:
    → Apply agent processing lên object = "nhìn vật thể như có ý chí"
    → Einstein: "nếu tôi cưỡi tia sáng..." = model light như agent
    → → Insight → rồi Logic (toán) verify → General Relativity

  → Chi tiết: Logic-Modeling.md (Core-Deep-Dive/)
```

---

## §7 — IMPLICATIONS CHO DOMAIN INTERACTION

```
🟡 CLASSIFICATION QUYẾT ĐỊNH TOÀN BỘ PIPELINE SAU:

  ① PROCESSING MODE:
    Object → Logic default → "apply rules đã biết"
    Agent → Modeling default → "simulate, predict, mirror"

  ② VALENCE COMPLEXITY:
    Object → ít channels, ổn định, đơn giản
    Agent → nhiều channels, dynamic, có thể mixed (yêu+ghét)

  ③ MECHANISMS USED:
    Object → KHÔNG mirror (không có state để đọc)
    Agent → Mirror mechanism fire (đọc state, model intent)

  ④ DOMAIN MAPPING VALUE:
    Object → cạn novelty nhanh (deterministic, predict được)
    Agent → novelty source LIÊN TỤC (unpredictable, mục tiêu riêng)

  ⑤ REPLACEABILITY:
    Object → thường dễ thay thế (dao khác, bàn khác)
    Agent → khó thay thế (mỗi agent unique, compiled schema riêng)


  ⭐ TẠI SAO AGENT = GIÁ TRỊ CAO HƠN OBJECT CHO DOMAIN MAPPING:

    Agent unpredictable → liên tục tạo prediction error → novelty → learning
    Agent có chunks tôi không có → domain data miễn phí
    Agent phản hồi hành vi tôi → verify tôi map domain đúng/sai
    Agent = independent sensor → dual check domain
    Mirror mechanism → auto-calibrate schema tôi KHÔNG CẦN PFC

    Object deterministic → cạn novelty → ít learning mới
    Object không phản hồi → không verify hành vi tôi
    Object = 1 sensor → single check

    → Brain ĐẦU TƯ nhiều resource hơn cho agent (VTC evidence) = HỢP LÝ
    → Agent input = body-base need (Domain-Interaction.md §6)
```

---

## §8 — HONEST ASSESSMENT

```
VERIFIED (🟢):
  → Object-Agent distinction ở trẻ: Spelke Core Knowledge
  → VTC animate/inanimate organization: neuroimaging
  → Infant development timeline: multiple studies
  → Meat Paradox strategies: Loughnan, Bastian 2014
  → Combat distance × trauma: Grossman (methodology bị challenge ở Marshall data,
    nhưng distance × mirror principle ít bị tranh cãi)
  → Uncanny Valley: robust finding

FRAMEWORK REASONING (🟡):
  → Classification quyết định processing mode → valence → drive: logic chain
  → Agency spectrum từ mẹ thật tới cục đá: consistent nhưng chưa test trực tiếp
  → Schema override mechanism: evidence gián tiếp (meat paradox, religion, etc.)
  → Body respond cùng pathway bất kể source: consistent với placebo research

HYPOTHESIS (🔴):
  → Hardware BINARY + Schema overlay = perceived spectrum: framework framing
  → Animism maintained = "community prevent refinement": logical nhưng chưa test
  → Bụi cây reclassify mechanism: framework application, chưa test trực tiếp

CÂU HỎI MỞ:
  → VTC binary: binary HOÀN TOÀN hay có gradient nào ở hardware level?
  → Schema override: latency bao lâu? Schema flip tức thì hay cần thời gian?
  → Abstract agents (Thiên Chúa): brain process ở VTC level NHƯ THẾ NÀO?
  → AI chatbot: classify Object hay Agent? (= ranh giới mới chưa có trong evolution)
```

---

## §9 — CROSS-REFERENCES

```
DOMAIN INTERACTION:
  → Domain-Interaction.md §3 — overview Object-Agent trong flow
  → Logic-Modeling.md §5 — 2×2 matrix chi tiết
  → Valence.md — Object valence vs Agent valence (chi tiết)
  → Emergent-Patterns.md — patterns emerge từ agent interaction
  → Domain-Mechanisms.md — mirror mechanism (agent processing tool)

FRAMEWORK:
  → Core-v7.5-Draft.md §2 — Body-Base L0-L3
  → Schema.md — compiled patterns, schema operations
  → Drive.md — how drives combine
  → Threat.md — threat processing (relevant: asymmetric cost)
  → Novelty.md — novelty from unpredictable agents

RESEARCH / ANALYSIS:
  → Mirror-Neuron-Analysis.md — evidence gốc, developmental timeline chi tiết
  → Mirror-Empathy-Connection-Other/Analysis-Draft.md — session notes

REFERENCES:
  → Spelke (2007): Core Knowledge Systems
  → VTC neuroimaging: animate/inanimate (eLife 2019)
  → Loughnan, Bastian (2014): Meat Paradox
  → Grossman (1995): On Killing — distance × trauma
  → Mori (1970): Uncanny Valley
  → Piaget (1929): animism in preoperational stage
  → Amsterdam (1972): mirror self-recognition rouge test
  → Warneken & Tomasello (2006, 2007): infant helping
  → Dondi, Simion & Caltran (1999): newborn cry discrimination
  → Harlow (1958): cloth vs wire mother
```
