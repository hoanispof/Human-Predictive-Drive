# Domain Mechanisms — Công Cụ Phục Vụ Domain Interaction

> **Bạn THẤY mẹ cười → body bạn nhẹ nhõm.**
> **Bạn THẤY em bé khóc → body bạn khó chịu.**
> **Bạn NGHĨ tới bạn thân → body bạn muốn gặp.**
>
> Bạn KHÔNG cười, KHÔNG khóc, KHÔNG cô đơn.
> Nhưng body bạn fire NHƯ THỂ bạn đang trải qua — chỉ YẾU HƠN.
>
> Đó KHÔNG phải "empathy" — 1 hệ thống riêng biệt.
> Đó là CÁCH agent processing TỰ NHIÊN hoạt động:
> brain cần predict agent → dùng own-state mapping → mirror LÀ BYPRODUCT.
>
> File này: các MECHANISMS phục vụ domain interaction —
> Mirror, Imagine-Final, Schema, và Feedback Loop —
> chúng HOẠT ĐỘNG thế nào, và tại sao "empathy" không cần system riêng.

---

> **Trạng thái:** DRAFT v0.5 — synthesis từ 4 sessions phân tích sâu
> **Ngày:** 2026-04-12
> **Mục đích:** Mô tả các MECHANISMS phục vụ domain interaction:
> Mirror (cách agent processing đọc state), Imagine-Final (preview outcomes),
> Schema (compiled models), Feedback Loop (learning from interaction).
> Redefine "Empathy" — từ "system riêng" → cách agent processing tự nhiên hoạt động.
> **Absorb từ:** Mirror-Neuron-Analysis.md (PRIMARY) + Empathy-Mirror.md §1-§5, §8-§9
> **Vị trí:** Core-Deep-Dive/Domain/ (file cuối trong bộ 5 Domain files)
> **Flow đọc:**
>   Domain-Interaction.md (overview)
>   ├── Object-Agent.md (classification)
>   ├── Logic-Modeling.md (processing)
>   ├── Valence.md (evaluation)
>   ├── Emergent-Patterns.md (patterns emerge từ repeated interaction)
>   └── **Domain-Mechanisms.md** (file NÀY — mechanisms phục vụ toàn bộ flow)
> **Tiền đề:**
>   Domain-Interaction.md (flow: Classify → Process → Evaluate → Drive → Action → Feedback)
>   Object-Agent.md (2 classification modes → basis cho "tại sao mirror tồn tại")
>   Valence.md (multi-channel assessment → mirror feed vào channels đã có)
>   Emergent-Patterns.md (WHAT patterns emerge → file này giải thích HOW mechanisms work)
>   Imagine-Final.md (product file → file này chỉ reference trong DI context)
>   Schema/ files (compiled models → file này chỉ reference trong DI context)
> **Phân biệt quan trọng:**
>   Emergent-Patterns.md = WHAT patterns emerge (cases, dynamics, conditions)
>   Domain-Mechanisms.md = HOW mechanisms work (chi tiết mechanism, KHÔNG duplicate cases)
> **Liên quan mainstream:**
>   🟢 Heyes ASL Theory (2010+) — mirror = learned association
>   🟢 Spelke Core Knowledge (2007) — object vs agent systems
>   🟢 VTC animate/inanimate (eLife 2019) — hardware binary classification
>   🟢 Mirror neurons (Rizzolatti 1996) — motor mirror in macaques
>   🟢 Pain empathy circuits (Singer 2004, Lamm 2011) — shared circuits
>   🟢 Theory of Mind (Frith & Frith 2006, Saxe 2006) — mPFC + TPJ
>   🟢 Emotional contagion (Hatfield 1994) — automatic affect transfer
>   🟢 Social buffering (Kiyokawa 2004) — presence reduces stress
> **⚠️ 🟡 Framework synthesis — reframe existing concepts, thêm "3 mechanisms" hypothesis**
> **Quy ước:** 🟢 Research support | 🟡 Suy luận từ framework | 🔴 Hypothesis

---

## Mục lục

- §0 — VỊ TRÍ TRONG FRAMEWORK
- §1 — MIRROR: CÁCH AGENT PROCESSING HOẠT ĐỘNG
  - 1.1 Mirror ≠ Module — Là Byproduct Của Agent Processing
  - 1.2 Ba Mechanisms: Pattern Matching → Agent Modeling → Schema Simulation
  - 1.3 Developmental Timeline — Từ Sơ Sinh Tới Trưởng Thành
  - 1.4 Agency Spectrum — Từ "Mẹ Thật" Đến "Cục Đá"
  - 1.5 Mirror → Channel Conversion — Cách Bản Sao Thành Signal
  - 1.6 Hai Tầng — Vô Thức BASE + PFC EXTENSION
  - 1.7 Mirror Strength + Perceived Ability (tóm tắt → EP.md §4)
  - 1.8 Empathy Fatigue + Mirror Reward Override (tóm tắt → EP.md §5)
- §2 — IMAGINE-FINAL TRONG DOMAIN INTERACTION
- §3 — SCHEMA TRONG DOMAIN INTERACTION
- §4 — FEEDBACK LOOP
- §5 — "EMPATHY" REDEFINE
- §6 — HONEST ASSESSMENT
- §7 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ TRONG FRAMEWORK

```
🟡 MECHANISMS = CÔNG CỤ phục vụ domain interaction

  Domain Interaction flow:
    Body-need → CLASSIFY → PROCESS → EVALUATE → DRIVE → ACTION → FEEDBACK
                (Object-Agent)  (Logic-Modeling)  (Valence)

  Mechanisms NẰM NGANG — hỗ trợ ở MỌI bước, cross-cutting:

  ┌──────────────────────────────────────────────────────────────────┐
  │          Domain Interaction Flow                                  │
  │  Classify → Process → Evaluate → Drive → Action → Feedback       │
  │     ↑          ↑          ↑         ↑        ↑         ↑        │
  │  ┌──┴──────────┴──────────┴─────────┴────────┴─────────┴──┐     │
  │  │              MECHANISMS (cross-cutting)                  │     │
  │  │                                                          │     │
  │  │  MIRROR:         Đọc state agent → feed vào Evaluate    │     │
  │  │  IMAGINE-FINAL:  Preview outcomes → feed vào Drive       │     │
  │  │  SCHEMA:         Compiled models → feed vào MỌI bước    │     │
  │  │  FEEDBACK:       Update sau interaction → feed LOOP lại  │     │
  │  └──────────────────────────────────────────────────────────┘     │
  └──────────────────────────────────────────────────────────────────┘


  PHÂN BIỆT:
    Flow steps = CÁC BƯỚC trong domain interaction (tuần tự)
    Mechanisms = CÔNG CỤ hỗ trợ các bước (cross-cutting)

    Ví dụ:
    → Classify (step) DÙNG Schema (mechanism) để lấy compiled model
    → Evaluate (step) DÙNG Mirror (mechanism) để đọc agent state
    → Drive (step) DÙNG Imagine-Final (mechanism) để preview kết quả
    → Feedback (step) DÙNG Schema (mechanism) để update compiled data


  TẠI SAO NẰM Ở ĐÂY (file cuối trong bộ Domain):
    → Object-Agent.md: đã mô tả CÁCH classify → basis cho "tại sao cần mirror"
    → Valence.md: đã mô tả CÁCH evaluate → basis cho "mirror feed vào đâu"
    → Emergent-Patterns.md: đã mô tả WHAT patterns emerge → file này giải thích HOW
    → File này: MECHANISMS hoạt động thế nào — bao gồm insight LỚN:
       "Mirror = BYPRODUCT của agent processing, không phải system riêng"
       "Empathy = CÁCH agent processing tự nhiên hoạt động"
```

---

## §1 — MIRROR: CÁCH AGENT PROCESSING HOẠT ĐỘNG

### 1.1 Mirror ≠ Module — Là Byproduct Của Agent Processing

```
🟡 CÂU HỎI GỐC:
  "Mirror neuron" là gì? Tại sao brain có nó?

  MAINSTREAM — 2 phe (2025):
    Rizzolatti (innate): neurons CHUYÊN cho mirror, gene encode
    Heyes (learned): mirror = associative sequence learning (ASL)
    → Đang nghiêng về Heyes — nhưng Heyes chưa nói TẠI SAO brain learn mirror


  FRAMEWORK INSIGHT:
    Mirror KHÔNG phải module riêng biệt.
    Mirror = BYPRODUCT tự nhiên của brain cần predict AGENT.

    Logic:

    ① Brain CẦN predict MỌI entity trong domain (để survive):
       → Predict đồ vật: input → rules → output CỐ ĐỊNH
         Bút: cầm → viết. Lửa: chạm → bỏng. Đá: thả → rơi.
         = DETERMINISTIC → Logic processing ĐỦ
         = Object-Agent.md §1: Object processing

    ② Agent = VẬT THỂ PHI LOGIC — rules KHÔNG work:
       → Cùng input (vẫy tay) → mẹ cười LÚC NÀY, mẹ bỏ đi LÚC KHÁC
       → Cùng input (đưa đồ chơi) → bạn lấy LÚC NÀY, bạn từ chối LÚC KHÁC
       → Logic processing FAIL cho agent
       → = Brain PHẢI build prediction model KHÁC cho agent

    ③ Model KHÁC đó = OWN-STATE MAPPING:
       → Trẻ observe: "khi MÌNH vui → MÌNH muốn chơi"
       → Trẻ observe: "khi MẸ vui → MẸ chơi với mình"
       → Mapping: "MẸ có state RIÊNG → state đó GIỐNG cách MÌNH có state"
       → = Dùng experience CỦA MÌNH để predict state CỦA AGENT
       → = "Nếu MẸ cũng có state giống MÌNH → khi MẸ cười = MẸ vui
            = MẸ sẽ chơi" → PREDICT ĐƯỢC

    ④ Own-state mapping = MIRROR:
       → Bản chất: body fire cùng pattern (yếu hơn) khi observe agent
       → Lý do: brain DÙNG own circuitry để SIMULATE agent's state
       → Kết quả: "mirror" = OUTPUT của agent processing
       → = KHÔNG phải system riêng — là CÁCH brain predict agent

    → = MIRROR = BYPRODUCT, không phải mục đích
    → = Brain KHÔNG "muốn empathize" → brain muốn PREDICT
    → = Empathy là SIDE EFFECT của prediction model


  SO SÁNH 3 VỊ TRÍ:

  ┌──────────────┬──────────────────┬────────────────────┬──────────────────────────┐
  │              │ Rizzolatti        │ Heyes               │ Framework                │
  │              │ (innate module)   │ (learned assoc.)     │ (prediction byproduct)   │
  ├──────────────┼──────────────────┼────────────────────┼──────────────────────────┤
  │ Neuron       │ CÓ, gene encode  │ KHÔNG, ASL          │ KHÔNG, pattern matching   │
  │ chuyên biệt  │                  │                      │                          │
  ├──────────────┼──────────────────┼────────────────────┼──────────────────────────┤
  │ WHY          │ Gene endowment   │ Cultural learning    │ Body CẦN predict         │
  │ mirror tồn   │                  │                      │ agent PHI LOGIC           │
  │ tại          │                  │                      │                          │
  ├──────────────┼──────────────────┼────────────────────┼──────────────────────────┤
  │ Trẻ sơ sinh  │ Mirror từ sinh   │ Chưa mirror         │ Chưa mirror — chỉ có     │
  │              │                  │                      │ arousal contagion         │
  ├──────────────┼──────────────────┼────────────────────┼──────────────────────────┤
  │ Strength     │ Hardwired        │ Learning history     │ Modality overlap ×        │
  │ gradient     │                  │                      │ interaction history       │
  ├──────────────┼──────────────────┼────────────────────┼──────────────────────────┤
  │ Tượng/ảnh    │ Khó giải thích   │ Schema-based         │ Compiled prediction       │
  │ thiêng       │                  │                      │ model, zero real mirror   │
  ├──────────────┼──────────────────┼────────────────────┼──────────────────────────┤
  │ Chó mirror   │ Cross-species    │ Learned              │ Co-evolution 30K năm →    │
  │ người       │ innate (?)        │                      │ learned agent model       │
  ├──────────────┼──────────────────┼────────────────────┼──────────────────────────┤
  │ Training     │ Không thay đổi   │ Re-learnable         │ Schema CAN override       │
  │ override     │ (hardwired)      │                      │ (15% → 90% firing rate)   │
  └──────────────┴──────────────────┴────────────────────┴──────────────────────────┘

  Framework THÊM so với Heyes:
    Heyes nói "learned through association" — ĐÚNG nhưng chưa nói TẠI SAO.
    Framework nói: learned VÌ agent = PHI LOGIC.
    Brain BUỘC phải build model KHÁC cho agent.
    Model đó = dùng own-state mapping onto other → "mirror".
    → = Mirror là BYPRODUCT của brain cần predict unpredictable agents.


  🟢 EVIDENCE ỦNG HỘ:

    ① VTC animate/inanimate (eLife 2019): 🟢
       → Brain có tổ chức RIÊNG cho animate vs inanimate trong VTC
       → = Hardware PHÂN LOẠI trước → software MODEL sau
       → = Consistent: classify agent → THEN build agent model

    ② Spelke Core Knowledge (2007): 🟢
       → Trẻ sinh ra với core knowledge cho object vs agent
       → Object: vật lý (continuity, solidity)
       → Agent: intentional action (self-propelled, goal-directed)
       → = 2 systems BẨM SINH — nhưng MIRROR xây dựng DẦN (không bẩm sinh)

    ③ Training override (Grossman 1995): 🟢
       → WWII: ~15-20% lính thực sự bắn vào địch
       → Vietnam: >90% (sau đổi training method)
       → = Schema CAN override mirror → mirror KHÔNG phải hardwired module

    ④ Distance × trauma (Grossman): 🟢
       → Xa (ném bom): trauma THẤP → không thấy mặt → agent model không fire
       → Cận chiến: trauma CỰC → thấy mặt → agent model FULL → mirror FULL
       → = Cùng người, khác input → khác response → input-dependent, NOT hardwired

    ⑤ Cross-species empathy: 🟢
       → Người mirror chó, chó mirror người (30K năm co-evolution)
       → Hardware "chỉ cho người" → KHÔNG giải thích cross-species
       → Learned model → giải thích: ai tương tác đủ → build model được
```

---

### 1.2 Ba Mechanisms: Pattern Matching → Agent Modeling → Schema Simulation

```
🔴 GIẢI THUYẾT FRAMEWORK:
  KHÔNG CÓ 1 "mirror" duy nhất.
  CÓ 3 mechanisms KHÁC NHAU mà mainstream GỘP thành "mirror":

  ┌───────────────────────────────────────────────────────────────────┐
  │  ① PATTERN MATCHING   →   ② AGENT MODELING   →   ③ SCHEMA SIM  │
  │     (pre-mirror)            (mirror proper)        (post-mirror) │
  │     limbic, near-innate     learned, 6-24m+        compiled      │
  │     arousal contagion       own-state mapping      virtual agent │
  │     mọi động vật            động vật xã hội        chủ yếu người │
  └───────────────────────────────────────────────────────────────────┘

  → Mainstream gọi CẢ 3 là "mirror" → confusion.
  → Tách ra: ① pre-mirror  ② mirror proper  ③ post-mirror
  → Mỗi mechanism = KHÁC CƠ BẢN về cách hoạt động


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ① PATTERN MATCHING — Pre-Mirror (limbic, near-innate, từ sinh)

    CÁCH HOẠT ĐỘNG:
      → Detect acoustic/visual PATTERN giống experience CỦA MÌNH
      → KHÔNG cần hiểu "người kia đang cảm gì"
      → Chỉ cần: "pattern NÀY giống khi MÌNH ở state X"
      → Body react THEO pattern quen — vô thức, nhanh, limbic

    VÍ DỤ:
      Sơ sinh nghe tiếng khóc trẻ khác:
        → "Tiếng khóc → giống khi MÌNH khóc → body react → khóc theo"
        → NHƯNG nghe khóc CỦA CHÍNH MÌNH (recorded) → phản ứng YẾU hơn
          (Dondi, Simion & Caltran 1999) 🟢
        → Tại sao?: khóc mình = FAMILIAR → đã resolve ("mẹ tới → bú → ổn")
                     khóc người khác = UNFAMILIAR → "pattern distress CHƯA resolve"
        → = Self-other discrimination RẤT SƠ KHAI — chưa phải empathy

      3-6 tháng:
        → Social smile với gương (treat reflection như "em bé khác")
        → Emotional contagion: phòng có người lo → trẻ bất an
        → Phân biệt biểu cảm vui/buồn/sợ trên mặt

      Cross-cultural confirm:
        → Vreden 2025 (thermal imaging): trẻ dưới 1 tuổi respond
          với NỘI DUNG CẢM XÚC của khóc, không chỉ acoustic aversiveness 🟢
        → = Vẫn pattern matching — detect pattern từ experience CỦA MÌNH

    ĐẶC ĐIỂM:
      → Limbic level — TRƯỚC PFC
      → Nhanh (ms-level)
      → KHÔNG CẦN agent model — chỉ cần pattern recognition
      → MỌI ĐỘNG VẬT CÓ (kể cả non-social): startle response = pattern matching
      → = AROUSAL CONTAGION, không phải empathy
      → 🟢 Chuột freeze khi thấy chuột khác bị shock (Church 1959) 🟢
      → 🟢 Khỉ từ chối ăn nếu ăn = đồng loại bị shock (Masserman 1964) 🟢

    RANH GIỚI — tại sao đây CHƯA PHẢI mirror:
      → Không có "MẸ đang buồn" → chỉ có "pattern GIỐNG khi MÌNH buồn"
      → Không có agent model → không biết OTHER có state RIÊNG
      → Không có own-state mapping → chỉ có pattern detection
      → = TIỀN THÂN của mirror, không phải mirror


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ② AGENT MODELING — Mirror Proper (learned, build dần 6-24 tháng+)

    CÁCH HOẠT ĐỘNG:
      → Brain nhận ra: entity NÀY = PHI LOGIC (agent, Object-Agent.md §2)
      → Logic processing FAIL → brain build MODEL KHÁC
      → Model = OWN-STATE MAPPING:
        "Khi MÌNH vui → MÌNH muốn chơi"
        "Khi MẸ vui → MẸ chơi với mình"
        → "MẸ CÓ STATE RIÊNG → state đó GIỐNG cách MÌNH có state"
      → = Dùng experience CỦA MÌNH predict state CỦA AGENT
      → = TRUE mirror bắt đầu ở đây

    QUÁ TRÌNH BUILD:

      Bước 1 — Trẻ tương tác ĐỒ VẬT:
        → Input → action → output CỐ ĐỊNH (logic)
        → Bút: cầm → viết. Lửa: chạm → bỏng.
        → Schema compiled → predict tốt → xong

      Bước 2 — Trẻ tương tác MẸ (agent):
        → Input → action → output PHI LOGIC
        → Cùng hành động → mẹ phản ứng KHÁC tùy lúc
        → Schema đồ vật KHÔNG work → PHẢI build model mới

      Bước 3 — Build agent model:
        → Observe hàng nghìn lần: MẸ state X → MẸ behavior Y
        → Map: "state MẸ ≈ state MÌNH" (vì cùng modality: mặt, giọng, body)
        → = Agent model = prediction model dùng OWN circuitry

      Bước 4 — Compile + generalize:
        → Lặp hàng nghìn lần → compiled vô thức
        → Mẹ → bố → người khác → chó → bất kỳ agent nào
        → Threshold: modality overlap CAO → map DỄ → mirror MẠNH

    EVIDENCE:

      Helping behavior phức tạp:
        → Warneken & Tomasello (2006, 2007): 🟢
          14-18 tháng: helping PHỨC TẠP hơn
          Phân biệt "muốn nhưng không được" vs "không muốn"
        → Svetlova, Nichols & Brownell (2010): 🟢
          Empathic helping KHÓ HƠN instrumental helping ở 18 tháng
          = Instrumental = pattern completion ("đồ rơi → nhặt")
          = Empathic = cần agent model ("buồn GIỐNG khi mình buồn")

      Self-recognition = milestone:
        → Rouge test (Amsterdam 1972): 🟢
          18-24 tháng: 50-65% pass → NHẬN RA MÌNH trong gương
        → Nhận ra self/other → MỚI có thể MAP state mình → other
        → = Agent model HOÀN CHỈNH khi self-other distinction rõ ràng

      Transition point:
        → TRƯỚC 18 tháng: "mirror" ≈ pattern completion + social participation
        → SAU 18 tháng: true mirror → agent modeling (own-state → other-state)

    ĐẶC ĐIỂM:
      → LEARNED — cần interaction data × time
      → CẦN agent thật (real-time, interactive)
      → Chỉ ĐỘNG VẬT XÃ HỘI có (cần social interaction lịch sử)
      → Modality overlap × interaction history = mirror strength
      → = TRUE EMPATHY — "TÔI biết BẠN đang buồn VÌ khi TÔI buồn, TÔI feel GIỐNG VẬY"


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ③ SCHEMA SIMULATION — Post-Mirror (compiled, trưởng thành)

    CÁCH HOẠT ĐỘNG:
      → Agent model từ mechanism ② compiled SÂU → stored trong schema
      → Body CÓ THỂ respond KHÔNG CẦN agent thật ở trước mặt
      → PFC TẠO virtual agent → schema fire → body respond
      → = KHÔNG CÒN CẦN MIRROR — model đã compiled, chạy từ schema

    VÍ DỤ:

      Tượng/ảnh thiêng:
        → Input: visual (static) + somatic (chạm) + CONTEXT (ritual)
        → Response từ agent: KHÔNG BAO GIỜ (tượng không respond)
        → Nhưng body VẪN RESPOND → tại sao?
          ① Schema compiled sâu (lặp ritual hàng nghìn lần)
          ② Mirror NGƯỜI XUNG QUANH (không phải mirror tượng!)
             "Mẹ kính cẩn → mirror state MẸ → body tôi kính cẩn"
          ③ PFC simulate virtual agent: "Đức Mẹ nhìn tôi, thương tôi"
          ④ Body không phân biệt "mirror thật" vs "PFC simulate"
        → Mirror quality: ZERO real mirror — 100% schema simulation

      Người đã mất:
        → Không còn agent thật → nhưng schema VẪN fire
        → "Nghĩ tới bà → body feel ấm → compiled từ hàng nghìn lần tương tác"
        → = Schema simulation: model CỦA BÀ đã compiled → fire không cần bà

      "Giọng lương tâm":
        → PFC simulate "agent đánh giá" (cha, mẹ, thầy, xã hội)
        → "Nếu MẸ biết mình làm điều này → mẹ sẽ buồn"
        → = Agent model compiled → PFC run simulation → body respond
        → = Guilt = mirror preview VIRTUAL (schema simulation)

      Mẫu ảnh nhỏ ở cổ:
        → Input: somatic (chạm da) + visual rất nhỏ
        → Mechanism: SOMATIC TRIGGER cho compiled schema
        → "Chạm → schema 'Đức Mẹ bảo vệ' fire → cortisol giảm nhẹ"
        → = Giống chạm gối cũ → feel safe → pure schema trigger

    CỤC ĐÁ ĐƯỢC THỜ — extreme case:
      → Input: visual (static) + somatic (chạm) + CONTEXT (ritual cộng đồng)
      → KHÔNG có agent. KHÔNG có sự sống. KHÔNG có biểu cảm.
      → Tại sao vẫn work?
        ① Schema inject từ cộng đồng: "đá NÀY có linh hồn"
        ② Animism phase (Piaget 2-7y): trẻ TỰ NHIÊN attribute feelings cho đồ vật
           → Cộng đồng PREVENT refinement → animism GIỮLẠI ở người lớn
        ③ Social proof: MỌI NGƯỜI tin → mirror NGƯỜI (không mirror đá!)
        ④ Ritual reinforce → compile sâu → body TỰ ĐỘNG respond
      → Mirror quality: ZERO — "đá = anchor cho compiled schema"

    ⭐ OBSERVATION QUAN TRỌNG:
      Body respond CÙNG PATHWAY cho TẤT CẢ:
        Mẹ thật   → body feel safe → cortisol giảm
        Tượng thiêng → body feel safe → cortisol giảm
        Cục đá thiêng → body feel safe → cortisol giảm
      → = CÙNG OUTPUT, KHÁC SOURCE
      → Body KHÔNG phân biệt source — chỉ biết "có signal → respond"
      → = Tại sao tôn giáo WORK dù không có agent thật
      → = Tại sao placebo WORK
      → = Tại sao locket người yêu WORK khi xa nhau

    EVIDENCE:
      → 🟢 Piaget animism (2-7y): trẻ attribute feelings cho đồ vật 🟢
        → Brain development data: consistent với overgeneralization
        → 4-7y: refine boundary (agent vs non-agent)
        → Cộng đồng CAN prevent refinement → animism giữ lại ở người lớn
      → 🟢 Placebo research: compiled expectation → real biochemical response 🟢
      → 🟢 Religious neuroscience: prayer/ritual activate similar circuits
        as social interaction (Schjoedt 2009) 🟢
      → 🟡 "Schema simulation thay thế mirror" = framework inference

    ĐẶC ĐIỂM:
      → Compiled — KHÔNG cần input thật
      → PFC-driven (conscious hoặc semi-conscious)
      → Chủ yếu NGƯỜI (cần PFC phát triển + schema phức tạp)
      → CÓ THỂ bị INJECT từ cộng đồng (không cần personal experience)
      → = POST-MIRROR — mirror đã xong việc, schema tiếp quản


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⭐ TẠI SAO TÁCH 3 MECHANISMS QUAN TRỌNG:

    ① Giải thích PHÁT TRIỂN:
       0-6m: chỉ có Pattern Matching (khóc lây = arousal, chưa phải empathy)
       6-24m: Agent Modeling ĐANG build (helping sơ khai → empathic helping)
       2y+: Schema Simulation bắt đầu (animism → compile → virtual agents)
       → 3 stages = 3 mechanisms KHÁC NHAU, không phải 1 mechanism "trưởng thành dần"

    ② Giải thích SPECTRUM:
       Mẹ thật = ② Agent Modeling (real-time, full channels)
       Video call = ② Agent Modeling (truncated channels)
       Tượng thiêng = ③ Schema Simulation (zero real mirror)
       Cục đá = ③ Schema Simulation (zero everything, pure schema)
       Tiếng khóc = ① Pattern Matching (pre-mirror, limbic)
       → 1 "mirror" duy nhất → KHÔNG giải thích sao body respond với cục đá

    ③ Giải thích CONFUSION trong mainstream:
       "Mirror neurons" = gộp ① + ② + ③ → tranh cãi vô tận
       → Rizzolatti đúng VỀ ①: có hardware pattern matching gần innate
       → Heyes đúng VỀ ②: agent modeling IS learned
       → Framework tách rõ: 3 mechanisms KHÁC NHAU, không phải 1

    ④ Giải thích cross-species:
       Chó mirror người: ② Agent Modeling (30K năm co-evolution → learned)
       Cá KHÔNG mirror người: ② chưa build (không đủ interaction history)
       Chuột freeze: ① Pattern Matching (arousal contagion, pre-mirror)
       → 1 mechanism → không giải thích gradient. 3 mechanisms → clear.
```

---

### 1.3 Developmental Timeline — Từ Sơ Sinh Tới Trưởng Thành

```
🟡 3 mechanisms KHÔNG xuất hiện cùng lúc — emerge THEO THỨ TỰ:

  ┌────────────┬─────────────────────┬────────────────────────────────────────┐
  │ Giai đoạn  │ Mechanism hoạt động │ Biểu hiện observable                   │
  ├────────────┼─────────────────────┼────────────────────────────────────────┤
  │ 0-6 tháng  │ ① Pattern Matching  │ Contagious crying, social smile,       │
  │            │    ONLY             │ emotional contagion trong phòng         │
  ├────────────┼─────────────────────┼────────────────────────────────────────┤
  │ 6-12 tháng │ ① + transition →②  │ Social referencing, helping sơ khai,   │
  │            │                     │ dùng mặt mẹ làm prediction tool        │
  ├────────────┼─────────────────────┼────────────────────────────────────────┤
  │ 12-24 th   │ ② Agent Modeling    │ Self-recognition, empathic helping,    │
  │            │    comes online     │ an ủi người khác (không chỉ nhặt đồ)  │
  ├────────────┼─────────────────────┼────────────────────────────────────────┤
  │ 2-7 tuổi   │ ② compile +        │ Animism (gán cảm xúc cho đồ vật),     │
  │            │ ③ begins            │ refine agent/non-agent boundary dần    │
  ├────────────┼─────────────────────┼────────────────────────────────────────┤
  │ Trưởng     │ ① + ② + ③          │ Full spectrum: arousal + real-time     │
  │ thành      │    all active       │ agent model + virtual agents compiled  │
  └────────────┴─────────────────────┴────────────────────────────────────────┘


  GĐ 1 — PATTERN MATCHING ONLY (0-6 tháng):

    Sơ sinh (0-72 giờ):
      → Contagious crying: nghe khóc → khóc theo
      → Khóc người khác > khóc MÌNH (recorded) 🟢 (Dondi 1999)
      → = Pattern recognition limbic — chưa phải mirror

    3-6 tháng:
      → Social smile với gương → treat reflection như "em bé khác"
      → Phân biệt biểu cảm vui/buồn/sợ trên mặt (face discrimination)
      → Emotional contagion: phòng có người lo → trẻ bất an
      → = Vẫn PATTERN MATCHING — detect pattern quen, chưa có agent model

    Neonatal imitation (Meltzoff) — ĐANG BỊ CHALLENGE:
      → Oostenbroek 2016: replication failure 🟢
      → Nếu trẻ sơ sinh KHÔNG imitate → consistent với "chưa có mirror"
      → = Chưa có data → chưa build được model


  GĐ 2 — TRANSITION: Social Referencing → Prediction Tool (6-12 tháng):

    6-9 tháng — Social referencing xuất hiện:
      → Nhìn MẸ trước khi react với vật lạ
      → Mẹ sợ → trẻ tránh. Mẹ vui → trẻ approach.

      Cơ chế (framework lens):
        → Compiled hàng nghìn lần: "mặt mẹ thế này → outcome thế này"
        → Mẹ cười → sau đó = chơi, reward → "mặt cười = safe"
        → Mẹ sợ → sau đó = căng thẳng → "mặt sợ = unsafe"
        → = Dùng biểu cảm mẹ làm PREDICTION TOOL cho outcome CỦA MÌNH
        → = CHƯA PHẢI "mẹ đang sợ" → MÀ LÀ "cái mặt đó → nguy hiểm cho MÌNH"
        → = BẮT ĐẦU transition từ pattern matching → agent-aware

    9.5-12 tháng — Helping behavior sơ khai:
      → >80% trẻ 12 tháng nhặt đồ rơi cho experimenter 🟢
      → KHÔNG nhặt trong control condition (cố ý thả)
      → 3 khả năng tại sao (chưa settled):
        A. Goal understanding → cần Theory of Mind sơ khai
        B. Pattern completion → "người cầm đồ = bình thường" → đồ rơi = delta
        C. Social participation → "làm gì đó → người lớn phản ứng → vui"
      → Research hiện tại: blend of B + C, A bắt đầu emerge


  GĐ 3 — AGENT MODELING COMES ONLINE (12-24 tháng):

    14-18 tháng:
      → Warneken & Tomasello (2006, 2007): helping PHỨC TẠP hơn 🟢
      → Phân biệt "muốn nhưng không được" vs "không muốn"
      → NHƯNG: empathic helping (an ủi người buồn) VẪN KHÓ
        (Svetlova 2010: empathic > instrumental difficulty ở 18m) 🟢
      → = TRANSITION POINT:
        Instrumental helping = pattern completion (đồ rơi → nhặt) → ① đủ
        Empathic helping = cần agent model ("buồn GIỐNG khi mình buồn") → ② đang build

    18-24 tháng — Bước nhảy lớn:
      → Self-recognition: rouge test, 50-65% pass (Amsterdam 1972) 🟢
      → Empathic helping TĂNG đáng kể
      → Trẻ bắt đầu AN ỦI người khác (không chỉ nhặt đồ)

      Cơ chế bước nhảy:
        → Nhận ra MÌNH trong gương = phân biệt SELF / OTHER rõ ràng
        → Phân biệt → MỚI có thể MAP state mình lên other
        → "Bạn buồn GIỐNG khi mình buồn → khi mình buồn muốn ÔM → ÔM bạn"
        → = Agent Model hoàn chỉnh: own-state predict other-state
        → = TRUE MIRROR bắt đầu ở đây


  GĐ 4 — COMPILE + OVERGENERALIZE + REFINE (2 tuổi+):

    2-4 tuổi — Animism phase (Piaget) 🟢:
      → Trẻ gán feelings cho ĐỒ VẬT: "ghế bị đau", "búp bê buồn"
      → Piaget: "normal cognitive development" — không phải lỗi
      → Framework lens: agent model ĐÃ BUILD → apply RỘNG HƠN CẦN THIẾT
        → Giống trẻ học "chó" rồi gọi mọi 4 chân là "chó"
        → = OVERGENERALIZATION → refine dần

    4-7 tuổi — Refine boundaries:
      → Agent model selective hơn: người, chó = CÓ state. Ghế = KHÔNG.
      → NHƯNG: nếu CỘNG ĐỒNG nói "đá có linh hồn"
        → Schema cộng đồng COMPILED SÂU hơn personal refinement
        → → Animism GIỮLẠI thành belief người lớn
        → = Tôn giáo = cộng đồng PREVENT natural refinement (Object-Agent.md §4)

    Trưởng thành — 3 mechanisms cùng hoạt động:
      → ① Pattern Matching: vẫn active (startle, contagion)
      → ② Agent Modeling: compiled deep cho người quen, sơ khai cho lạ
      → ③ Schema Simulation: virtual agents (thần, người đã mất, lương tâm)
      → Body KHÔNG phân biệt source → cùng output, khác mechanism


  ⭐ INSIGHT TỪ TIMELINE:
    "Empathy" KHÔNG xuất hiện bẩm sinh — EMERGE từ interaction.
    Trẻ KHÔNG "có empathy" hay "không có empathy".
    Trẻ ĐI QUA 3 stages — mỗi stage = mechanism KHÁC:
      ① "Khóc lây" (pattern matching) ≠ ② "hiểu bạn buồn" (agent modeling)
    → Giải thích: tại sao trẻ 12 tháng nhặt đồ (①) nhưng CHƯA an ủi (②)
    → Giải thích: tại sao self-recognition (18-24m) = milestone cho empathy
```

---

### 1.4 Agency Spectrum — Từ "Mẹ Thật" Đến "Cục Đá"

```
🟡 3 mechanisms KHÔNG chỉ khác nhau theo TUỔI — còn khác theo TARGET.
   Cùng 1 người trưởng thành, mechanism NÀO fire PHỤ THUỘC entity:

  ┌──────────────────┬───────────┬───────────────────────────────────────────┐
  │ Entity           │ Mechanism │ Chi tiết                                   │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ MẸ THẬT          │ ②         │ Full agent: real-time, full channels       │
  │ (full agent)     │ Agent     │ Input: visual + auditory + somatic +       │
  │                  │ Modeling  │ olfactory + timing                         │
  │                  │           │ Response: phi logic, interactive           │
  │                  │           │ Mirror quality: MẠNH NHẤT                  │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ NGƯỜI LẠ         │ ②         │ Agent model sơ khai, dùng species overlap  │
  │                  │ Agent     │ (~70-90% shared modality)                  │
  │                  │ Modeling  │ Mirror quality: trung bình                 │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ CHÓ              │ ②         │ Cross-species learned (30K năm co-evol)    │
  │                  │ Agent     │ Input: visual + auditory + somatic +       │
  │                  │ Modeling  │ olfactory. Modality overlap thấp hơn người │
  │                  │           │ Mirror quality: có nhưng yếu hơn          │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ VIDEO CALL       │ ②         │ Dùng compiled model (nếu đã quen)         │
  │                  │ Agent     │ Input: visual + auditory ONLY              │
  │                  │ Modeling  │ Mirror quality: ~60-70% — truncated        │
  │                  │ (trunc.)  │ THIẾU: touch, smell, presence, timing      │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ ẢNH / VIDEO      │ ② → ③    │ One-way, scripted hoặc frozen              │
  │ KHÔNG tương tác  │ Schema    │ PFC SIMULATE dựa trên compiled schema     │
  │                  │ Sim.      │ Mirror quality: rất yếu — PFC imagine,    │
  │                  │           │ không real feedback                        │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ TƯỢNG / ẢNH      │ ③         │ ZERO real mirror — 100% schema simulation │
  │ THIÊNG           │ Schema    │ Tại sao work: schema compiled sâu +        │
  │                  │ Sim.      │ mirror NGƯỜI xung quanh + PFC virtual     │
  │                  │           │ Body không phân biệt source               │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ MẪU ẢNH NHỎ     │ ③         │ Somatic trigger → compiled schema         │
  │ Ở CỔ            │ Schema    │ "Chạm → Đức Mẹ bảo vệ → cortisol giảm"  │
  │                  │ Sim.      │ Giống chạm gối cũ → feel safe             │
  ├──────────────────┼───────────┼───────────────────────────────────────────┤
  │ CỤC ĐÁ          │ ③         │ ZERO agent, zero sự sống, zero biểu cảm  │
  │ ĐƯỢC THỜ         │ Schema    │ Pure anchor cho compiled schema            │
  │                  │ Sim.      │ "đá = anchor, body respond vì SCHEMA"     │
  └──────────────────┴───────────┴───────────────────────────────────────────┘


  ⭐ QUY LUẬT — mechanism nào fire PHỤ THUỘC:

    ① Input CHANNELS có bao nhiêu?
       Full channels (gặp trực tiếp) → ② Agent Modeling (real-time)
       Truncated (video/phone) → ② nhưng yếu hơn
       Zero (tượng, đá, trí nhớ) → ③ Schema Simulation

    ② Có REAL-TIME RESPONSE không?
       Có response → ② Agent Modeling (calibrate liên tục)
       Không response → ③ Schema Simulation (chạy từ compiled data)

    ③ Có COMPILED SCHEMA không?
       Có schema → ③ CÓ THỂ fire (dù zero input)
       Không schema → KHÔNG fire gì → entity = object thuần

    → = GRADIENT liên tục, không phải binary
    → = Body TỰ chọn mechanism tối ưu cho input available


  EINSTEIN PARALLEL — "Mirror" trong tư duy:
    🟡 Einstein KHÔNG tính thuần logic. Ông MAP own-state lên OBJECT:
      "Nếu TÔI cưỡi tia sáng thì TÔI sẽ thấy gì?"
    → = CÙNG CƠ CHẾ agent modeling: dùng experience MÌNH predict THỨ KHÁC
    → Khác: Einstein apply ② lên NON-AGENT (tia sáng) — ② thường chỉ cho agent
    → = Genius = khả năng apply agent modeling NGOÀI DOMAIN thông thường
    → Einstein somatic simulate → cần Grossmann verify bằng math
    → = Simulate → check domain → refine → cùng loop với trẻ mirror mẹ
```

---

### 1.5 Mirror → Channel Conversion — Cách Bản Sao Thành Signal Của Mình

```
🟡 Mirror tạo bản sao body-state NGƯỜI KHÁC trong body MÌNH.
   Nhưng bản sao đó → chạy qua CHANNELS ĐÃ CÓ → thành signal CỦA MÌNH.

  QUY TRÌNH 5 BƯỚC:

    ① DETECT sinh vật khác + state CỦA HỌ:
       → Input: visual (mặt, body language), auditory (giọng, tiếng khóc),
         somatic (nhiệt, rung), presence
       → KHÔNG cần PFC — brainstem + amygdala + mirror circuits ĐỦ

    ② MIRROR FIRE — tạo bản sao YẾU trong body MÌNH:
       → Anterior insula: tổng hợp → "body-state delta"
       → Bản sao = CÙNG pattern, THẤP hơn intensity
       → 🟢 Singer 2004: insula + ACC fire khi quan sát pain,
         YẾU hơn trải nghiệm trực tiếp (~10-30% intensity) 🟢

    ③ Bản sao FEED VÀO channels đã có CỦA MÌNH:
       → Mirror L0 threat CỦA HỌ  → Body-Dissonance CỦA MÌNH (nhẹ)
       → Mirror L1 deficit CỦA HỌ → Body-Dissonance CỦA MÌNH (nhẹ)
       → Mirror L2 reward CỦA HỌ  → Body-Reward CỦA MÌNH (nhẹ)
       → Mirror L3 threat CỦA HỌ  → Body-Dissonance CỦA MÌNH (nhẹ)
       → = CÙNG 3 body signals: Satisfaction / Reward / Dissonance
       → = CÙNG channels (L0→L3)
       → = CHỈ KHÁC: nguồn trigger — từ MIRROR thay vì từ body MÌNH trực tiếp

    ④ PFC observe (nếu signal ĐỦ MẠNH):
       → PFC: "body mình khó chịu VÌ THẤY người kia đau"
       → PFC interpret + simulate sâu (tầng 2, xem §1.6)
       → PFC chọn response

    ⑤ DRIVE hoặc KHÔNG:
       → Signal đủ mạnh + perceived ability → DRIVE hành động
       → Signal yếu hoặc không ability → cắt input (defense)


  ⭐ QUAN TRỌNG — Signal CỦA MÌNH, dù nguồn từ MIRROR:

    Khi mirror tạo dissonance CỦA MÌNH → đó LÀ dissonance CỦA MÌNH THẬT:
      → Cortisol CỦA MÌNH tăng
      → NE CỦA MÌNH fire
      → Body MÌNH căng
      → = KHÔNG phải "tưởng tượng" — là biochemistry THẬT trong body MÌNH

    Khác biệt DUY NHẤT: nguồn trigger
      Direct: body MÌNH đói  → dissonance
      Mirror: thấy HỌ đói   → mirror → dissonance CỦA MÌNH
      → Cùng dissonance, cùng pathway, khác trigger, khác intensity


  VÍ DỤ — Channel Conversion thực tế:

    Thấy người ĐÓI (mirror L1 Nutrition deficit CỦA HỌ):
      → Body MÌNH dissonance nhẹ (dù MÌNH không đói)
      → PFC: "tội người ta" → drive cho ăn (nếu có ability)

    Thấy người bị ĐÁNH (mirror L0 threat CỦA HỌ):
      → Body MÌNH giật mình (dù MÌNH không bị đánh)
      → = Arousal contagion (①) + agent model (②) CÙNG fire

    Thấy người THÀNH CÔNG (mirror Mastery reward CỦA HỌ):
      → Body MÌNH sướng nhẹ (dù MÌNH không thành công)
      → = "Vui lây" = mirror reward qua L3 Mastery channel

    Thấy người CÔ ĐƠN (mirror Connection deficit CỦA HỌ):
      → Body MÌNH trống nhẹ
      → = Mirror qua agent input need channel (DI.md §6)

    → = Mirror CROSS-CUTTING toàn bộ Body-Base — MỌI channel đều bị ảnh hưởng
    → = Empathy-Mirror.md §1 đã mô tả: mechanism, không phải channel mới
    → = File này reconfirm: mirror = CÁCH agent processing hoạt động
```

---

### 1.6 Hai Tầng — Vô Thức BASE + PFC EXTENSION

```
🟡 Mirror hoạt động ở 2 TẦNG — parallel cấu trúc Imagine-Final:

  ┌──────────────────────────────────────────────────────────────────┐
  │  Imagine-Final:  vô thức LUÔN có expectation                     │
  │                  → PFC chỉ conscious hóa + check domain          │
  │                                                                  │
  │  Mirror:         vô thức LUÔN mirror                             │
  │                  → PFC chỉ interpret + simulate sâu + chọn resp  │
  │                                                                  │
  │  = CÙNG KIẾN TRÚC: base vô thức + PFC extension                 │
  └──────────────────────────────────────────────────────────────────┘


  TẦNG 1 — VÔ THỨC BASE (Emotional Contagion — luôn chạy):

    Cơ chế:
      → 🟢 Mirror neurons fire khi THẤY agent hành động
        (Rizzolatti 1996: motor mirror neurons ở khỉ) 🟢
      → 🟢 Anterior insula fire khi THẤY người khác đau
        — cùng vùng với đau CỦA MÌNH (Singer 2004, Lamm 2011) 🟢
      → 🟢 Nucleus accumbens fire khi nhìn infant faces
        — kể cả non-parents (Glocker 2009) 🟢
      → 🟢 Emotional contagion: cảm xúc tự lan truyền giữa người
        (Hatfield 1994) 🟢

    Đặc điểm:
      → TỰ ĐỘNG — không cần PFC ra lệnh
      → NHANH — ms-level (nhanh hơn PFC process)
      → MỌI ĐỘNG VẬT XÃ HỘI CÓ — chó, khỉ, voi, chuột
      → KHÔNG cần hiểu TẠI SAO — chỉ fire PATTERN tương tự
      → = Body-level, pre-PFC, cross-species


  TẦNG 2 — PFC EXTENSION (Theory of Mind — khi body gọi):

    Cơ chế:
      → 🟢 mPFC + TPJ activate khi nghĩ về mental state NGƯỜI KHÁC
        (Frith & Frith 2006, Saxe 2006) 🟢
      → mPFC dùng schema CỦA MÌNH để simulate NGƯỜI KHÁC
      → = "Phiên bản TÔI đóng vai HỌ" — giới hạn bởi chunk overlap

    PFC làm 3 VIỆC (parallel Imagine-Final tầng 2):

      ① INTERPRET: gọi tên mirror signal vô thức
         → Body khó chịu khi thấy bạn buồn
         → PFC: "à, bạn đang ĐAU VÌ chia tay"
         → = PFC PHÁT HIỆN, không phải PFC TẠO mirror

      ② SIMULATE SÂU: model TẠI SAO agent ở state đó
         → "Bạn buồn VÌ chia tay VÌ invest 3 năm VÌ sợ cô đơn"
         → = Imagination-Analysis §③: simulate chuỗi nguyên nhân
         → Chỉ NGƯỜI CÓ: chó thấy buồn nhưng KHÔNG biết TẠI SAO

      ③ CHỌN RESPONSE: quyết định làm gì với mirror information
         → Giúp → body-reward (cooperation reward)
         → Ignore → body-neutral (hoặc guilt nhẹ)
         → Override empathy → dissonance nhưng strategic gain


  "EMPATHY CEILING" — giới hạn của tầng 2:

    → mPFC dùng chunks CỦA MÌNH → simulate "MÌNH đóng vai HỌ"
    → = APPROXIMATE, không bao giờ 100%
    → 3 loại blind spot:

      ① Hardware delta: DRD4, cortisol baseline, hormone profile
         → KHÔNG simulate được — hardware CỦA MÌNH ≠ hardware CỦA HỌ
         → "Tôi hiểu bạn buồn" nhưng KHÔNG thể feel CƯỜNG ĐỘ CHÍNH XÁC

      ② Compiled schema sâu CỦA HỌ: hộp đen
         → 30 năm experience compiled → tôi KHÔNG access được
         → "Tôi biết bạn sợ nước" nhưng KHÔNG thể feel SỢ GIỐNG HỌ

      ③ Context CỦA HỌ mà tôi không biết:
         → Internal state hiện tại, recent events, ongoing concerns
         → = Information gap, không phải mechanism failure

    → 3 LỚP OVERLAP quyết định accuracy (Personal-Melody.md §12):
      ① Species overlap (~70-90%): cùng loài → body-base gần giống
      ② Culture overlap (0-80%): shared domain → chunks chung
      ③ Personal overlap (0-90%): time × attention → simulate chi tiết

    → Overlap CAO → simulate CHÍNH XÁC → "hiểu nhau"
    → Overlap THẤP → simulate SAI → "không thể hiểu tôi"
    → = "Hiểu" = mức OVERLAP, không phải binary có/không


  ⭐ TẠI SAO 2 TẦNG QUAN TRỌNG:

    Tầng 1 = GỐC (mọi động vật xã hội có):
      → Bảo đảm RESPONSE NHANH cho social signals
      → Không cần "quyết định empathize" — body TỰ ĐỘNG

    Tầng 2 = MỞ RỘNG (chỉ người, cần PFC):
      → Cho phép HIỂU TẠI SAO + CHỌN phản ứng
      → Cho phép simulate KHÔNG CẦN input thật (virtual agents)
      → Trade-off: chậm hơn, tốn energy, nhưng SÂUHƠN

    Parallel Imagine-Final:
      Imagine-Final: body luôn có expect → PFC conscious hóa + check domain
      Mirror: body luôn mirror → PFC interpret + simulate sâu + chọn response
      → = 2 mechanisms, CÙNG kiến trúc, KHÁC chức năng
      → = Imagine-Final: predict OUTCOME. Mirror: predict AGENT STATE.
```

---

### 1.7 Mirror Strength + Perceived Ability (tóm tắt → EP.md §4)

```
🟡 Mirror strength KHÔNG đồng đều — có GRADIENT rõ.
   Chi tiết + cases: Emergent-Patterns.md §4 (Nurturing Pattern).
   Ở đây: tóm tắt MECHANISM.


  4 YẾU TỐ NHÂN VỚI NHAU (không cộng):

    ① LIVING BEING — prerequisite:
       → Phải là sinh vật (hoặc perceived có sự sống)
       → Living → mirror CÓ. Non-living → mirror KHÔNG CÓ.
       → = Gate: chưa pass ① → 3 yếu tố sau = irrelevant

    ② VULNERABILITY CUES — càng yếu → mirror CÀNG MẠNH:
       → 🟢 Baby Schema / Kindchenschema (Lorenz 1943): mắt to, mặt tròn,
         body nhỏ → trigger nurturing response ở người lớn 🟢
       → 🟢 Nucleus accumbens fire khi nhìn infant faces (Glocker 2009) 🟢
       → Tại sao: vulnerability = POTENTIAL DEFICIT LỚN
         → Body auto-prioritize: "sinh vật này CÓ THỂ chết nếu không ai giúp"

    ③ EXPRESSIVENESS — càng biểu hiện rõ state → mirror CÀNG MẠNH:
       → Mặt người: CỰC expressive → mirror MẠNH
       → Mặt chó: khá expressive → mirror tốt
       → Cá: gần zero biểu cảm → mirror rất yếu
       → 🟢 Facial mimicry = automatic, 300ms (Dimberg 2000) 🟢
       → = Mirror CẦN INPUT để fire — ít input = ít mirror

    ④ SIMILARITY / FAMILIARITY — càng giống/quen → CÀNG MẠNH:
       → Cùng loài > khác loài (species overlap)
       → Quen > lạ (compiled chunks → simulate CHÍNH XÁC)
       → 🟢 In-group empathy bias (Xu 2009): ACC response mạnh hơn
         cho in-group member 🟢

    → 4 yếu tố NHÂN: baby ruột = ①✅ × ②CỰC CAO × ③CAO × ④CỰC CAO
      = Mirror MẠNH NHẤT → drive chăm sóc MẠNH NHẤT
    → Cá cảnh = ①✅ × ②THẤP × ③≈0 × ④THẤP = mirror rất yếu


  PERCEIVED ABILITY — van điều khiển giữa mirror và drive:

    Mirror dissonance + Perceived Ability CAO → DRIVE mạnh:
      → "Thấy người đói + tôi CÓ đồ ăn" → drive cho ăn
      → PFC: Imagine-Final preview "nếu giúp → mirror dissonance GIẢM"

    Mirror dissonance + Perceived Ability THẤP → CẮT INPUT:
      → "Thấy chiến tranh trên TV + tôi KHÔNG LÀM ĐƯỢC GÌ"
      → Dissonance không resolve → tích lũy → defense: cắt input
      → "Tắt TV", "lướt qua", "không dám nhìn"

    → = Ability = VAN: cao → drive → action → resolve
    → = Ability = VAN: thấp → block → cắt input → defense
    → Chi tiết + cases: Emergent-Patterns.md §4 (nurturing) + §5 ("cho đi")
```

---

### 1.8 Empathy Fatigue + Mirror Reward Override (tóm tắt → EP.md §5)

```
🟡 2 MẶT CỦA CÙNG 1 ĐỒNG XU — cả hai liên quan mirror:
   Chi tiết + spectrum: Emergent-Patterns.md §4-§5.
   Ở đây: tóm tắt MECHANISM.


  MẶT 1 — EMPATHY FATIGUE (mirror dissonance quá tải):

    Cơ chế:
      → Mirror tạo dissonance CỦA MÌNH (biochemistry thật, §1.5)
      → Dissonance LIÊN TỤC + MẠNH + KHÔNG resolve = tích lũy
      → Cortisol baseline TĂNG (Cortisol-Baseline.md logic)
      → Body CẮT MIRROR (defense) → "mất empathy"

    3 defense mechanisms:
      ① Detachment: PFC suppress mirror input
         → "Nhìn bệnh nhân như case, không như người"
      ② Numbness: VTA habituate mirror signal
         → "Quen rồi, không feel nữa"
      ③ Avoidance: cắt input source hoàn toàn
         → "Không muốn nhìn tin tức"

    → KHÔNG PHẢI "người xấu" — là body SELF-PROTECT
    → Cùng cơ chế burnout: hoạt động > repair → wear
    → Ai chịu nhiều nhất: y tá, social worker, giáo viên môi trường khó


  MẶT 2 — MIRROR REWARD OVERRIDE (mirror reward quá mạnh):

    Cơ chế:
      → Giúp người khác → thấy họ improve → mirror reward (opioid, oxytocin)
      → Mirror reward = biochemistry THẬT → body MÌNH nhận reward
      → NHƯNG body-base C��A MÌNH VẪN THIẾU (chưa fix cho mình)
      → Mirror reward MASK deficit signal CỦA MÌNH
      → = "Sướng vì giúp người" che mất "mình đang thiếu"

    2 loại override — KHÁC CĂN BẢN:
      Loại A — L0 justified (gene carrier threat): có ceiling tự nhiên
        → Mẹ ăn ít cho con → L0 > L1 → designed, tạm thời
      Loại B — Schema hijack (không L0): KHÔNG có ceiling
        → Quyên góp tôn giáo dù gia đình khó → schema "phước" drive
        → = BUG — evolution không designed điều này

    → Cùng cơ chế Core §2.5: schema override body-base
    → Thêm pathway: mirror reward + schema reward CÓ THỂ STACK
    → Chi tiết + spectrum: Emergent-Patterns.md §5 ("cho đi" pattern)


  LIÊN KẾT 2 MẶT:
    §8 Fatigue: mirror dissonance QUÁ NHIỀU → body CẮT mirror → numbness
    §8.5 Override: mirror reward QUÁ MẠNH → body NGHIỆN mirror → ignore own needs
    → Fatigue = body TỰ BẢO VỆ (cắt input)
    → Override = body BỊ HIJACK (reward thay thế)
    → 2 failure modes CỦA CÙNG 1 mechanism
```

---

## §2 — IMAGINE-FINAL TRONG DOMAIN INTERACTION

```
🟡 Imagine-Final = mechanism preview KẾT QUẢ trước hành động.
   Chi tiết Imagine-Final: Imagine-Final.md (product file) + Imagination-Analysis.md (process file).
   Ở đây: Imagine-Final TRONG CONTEXT domain interaction — đặc biệt khi tương tác AGENT.


  IMAGINE-FINAL × DOMAIN INTERACTION:

    Với OBJECT — straightforward:
      → "Nếu tôi chạm lửa → bỏng" → LOGIC predict → Imagine-Final preview outcome
      → Simple: input → rules → output → preview → drive tránh/approach
      → = Logic processing + Imagine-Final = đủ

    Với AGENT — phức tạp hơn:
      → "Nếu tôi cho bạn kẹo → bạn sẽ...?"
      → KHÔNG dùng logic (agent = phi logic) → DÙNG MIRROR + IMAGINE-FINAL:
        ① Mirror: simulate state CỦA BẠN ("bạn đang muốn ăn")
        ② Imagine-Final: preview "nếu cho → bạn vui"
        ③ Mirror preview: "bạn vui → mirror reward CỦA MÌNH"
        ④ = Body MÌNH preview MIRROR REWARD trước khi hành động
      → = IMAGINE-FINAL × MIRROR = powerful combination


  TẠI SAO COMBINATION NÀY MẠNH:

    Imagine-Final MỘT MÌNH:
      → Preview outcome CỦA MÌNH → drive hành động cho MÌNH
      → "Nếu ăn → bớt đói" → drive ăn

    Imagine-Final × Mirror:
      → Preview outcome CỦA AGENT + preview MIRROR REWARD CỦA MÌNH
      → = DOUBLE preview: outcome cho HỌ + reward cho MÌNH qua mirror
      → "Nếu cho kẹo → BẠN vui → MÌNH mirror vui"
      → = Body preview CHUỖI: action → their-state → mirror → my-reward

    → = Tại sao nghĩ tới LÀM ĐIỀU TỐT cũng ĐÃ feel-good
    → = Imagine-Final preview mirror reward → opioid nhẹ → "muốn làm"


  CASES — Imagine-Final trong agent interaction:

    Preview GẶP bạn thân:
      → Imagine-Final: "gặp bạn → nói chuyện → vui"
      → Mirror preview: simulate bạn vui → mirror reward preview
      → Body: opioid nhẹ TRƯỚC KHI gặp → "muốn gặp" = drive
      → = "Nhớ bạn" = Imagine-Final × Mirror preview REWARD

    Preview CHO QUÀ:
      → Imagine-Final: "cho quà → bạn mở → bạn ngạc nhiên vui"
      → Mirror preview: simulate PHẢN ỨNG bạn → mirror reward preview
      → = "Sướng khi NGHĨ TỚI cho quà" = preview mirror reward
      → = Tại sao CHỌN QUÀ = exciting: optimize mirror reward preview

    Preview XUNG ĐỘT:
      → Imagine-Final: "nếu nói thẳng → bạn giận → mirror dissonance"
      → Mirror preview: simulate bạn GIẬN → mirror dissonance preview
      → Body: cortisol nhẹ TRƯỚC KHI nói → "ngại nói" = avoidance drive
      → = "Sợ confrontation" = Imagine-Final × Mirror preview DISSONANCE

    Preview MẤT NGƯỜI THÂN:
      → Imagine-Final: "nếu mẹ mất → cuộc sống không có mẹ"
      → Mirror preview: KHÔNG CÒN gì để mirror → void
      → Schema simulation: compiled model MẸ fire → body respond
      → = "Grief trước khi mất" = anticipatory grief = Imagine-Final × Mirror × Schema


  ⭐ CONNECTION × IMAGINE-FINAL (mỗi layer):

    Body-base need (mere presence): không cần Imagine-Final — body auto-detect
    Calibration (observation): Imagine-Final preview "gần người → calibrate → an hơn"
    Virtual chunks (light interaction): Imagine-Final preview "hỏi bạn → biết thêm"
    Deep bond (sustained): Imagine-Final preview TOÀN BỘ relationship trajectory
    → Từ L0 → L4 agent input: Imagine-Final TĂNG DẦN vai trò
    → L0 = hardware, không cần preview. L4 = compiled, Imagine-Final drive complex decisions
    → Chi tiết: Emergent-Patterns.md §2.2 (Connection per layer)
```

---

## §3 — SCHEMA TRONG DOMAIN INTERACTION

```
🟡 Schema = compiled models từ experience.
   Chi tiết Schema: Schema/ files (Anchor-Schema.md, v.v.).
   Ở đây: Schema TRONG CONTEXT domain interaction — 4 vai trò chính.


  VAI TRÒ 1 — COMPILED VALENCE PROFILES:

    Mỗi entity bạn từng tương tác → brain COMPILED valence profile:

      "Bạn A":
        L1 Nutrition: neutral (không ảnh hưởng)
        L2 Experience: positive (hay đi chơi cùng)
        L3 Mastery: positive nhẹ (đôi khi share kiến thức)
        Agent input: positive (vui khi ở gần)
        → Net valence: POSITIVE → approach drive

      "Đồng nghiệp B":
        L2 Experience: negative (hay gây stress)
        L3 Status: positive nhẹ (networking value)
        → Net valence: MIXED → cautious

    → = Valence profile = COMPILED từ hàng trăm interactions
    → = KHÔNG cần evaluate LẠI mỗi lần gặp → schema FIRE NGAY
    → = "Thấy bạn A → body vui TRƯỚC KHI PFC process" = compiled valence
    → Chi tiết: Valence.md §3 (valence profiles)


  VAI TRÒ 2 — COMPILED AGENT MODELS:

    Mỗi agent bạn tương tác ĐỦ → brain compiled agent model:

      "Mẹ":
        → Khi mẹ cau mày = mẹ lo (không phải giận)
        → Khi mẹ im lặng = mẹ mệt (không phải giận)
        → Khi mẹ nấu nhiều = mẹ vui (biểu hiện qua hành động)
        → = Agent model CHÍNH XÁC: predict state mẹ TỐT HƠN người lạ

      "Sếp":
        → Khi sếp gọi riêng = CÓ THỂ tốt HOẶC xấu
        → Chưa compiled đủ → model chưa chính xác → anxiety

    → Agent model compiled SÂU hơn → mirror CHÍNH XÁC hơn (§1.4)
    → = "Hiểu nhau" = compiled agent model CHÍNH XÁC
    → = "Không hi���u nhau" = model SƠ KHAI hoặc SAI


  VAI TRÒ 3 — SCHEMA INHERITANCE (từ cộng đồng):

    KHÔNG phải mọi schema đều từ personal experience.
    Cộng đồng INSTALL valence + agent model TRƯỚC KHI trẻ experience:

      "Rắn = nguy hiểm":
        → Trẻ CHƯA gặp rắn → nhưng body SỢ (mẹ sợ → mirror → compile)
        → = Schema inheritance: valence CỦA MẸ → compiled vào schema CỦA TRẺ
        → 🟢 Consistent: observational learning (Bandura 1977) 🟢

      "Ông bà = kính trọng":
        → Trẻ chưa hiểu TẠI SAO → nhưng body treat ông bà = positive agent
        → = Agent model INHERIT từ cha mẹ, cộng đồng

      "Đức Mẹ = bảo vệ":
        → Trẻ CHƯA BAO GIỜ gặp → nhưng schema compiled qua ritual
        → = Schema Simulation (§1.2 mechanism ③) = chạy trên INHERITED schema

    Trade-off:
      NHANH: cộng đồng install → trẻ có schema NGAY → survive nhanh hơn
      KÉM CHÍNH XÁC: schema CỦA CỘNG ĐỒNG ≠ reality CỦA TRẺ
      → = "Rắn = nguy hiểm" = tốt (rắn thật sự nguy hiểm phần lớn)
      → = "Người lạ = xấu" = oversimplified (phần lớn người lạ neutral)
      → Chi tiết: Valence.md §4 (valence dynamics — inheritance vs experience)


  VAI TRÒ 4 — SCHEMA OVERRIDE Object↔Agent:

    Schema CAN override hardware classification (Object-Agent.md §4):

      Agent → Object:
        → Dehumanization: "kẻ thù = con vật / mối mọt"
        → = Schema reclassify agent thành object → BYPASS mirror
        → = Cho phép tiêu diệt MÀ KHÔNG bị mirror dissonance
        → Evidence: combat training, propaganda (Grossman 1995) 🟢

      Object → Agent:
        → Nhân cách hóa: "xe hơi của tôi có tính cách"
        → Tôn giáo: "cục đá này có linh hồn"
        → = Schema reclassify object thành agent → TRIGGER mirror (yếu)
        → = Schema Simulation (§1.2 mechanism ③)

    → = Schema là LAYER mạnh nhất trong domain interaction
    → = CÓ THỂ override HARDWARE classification (VTC binary)
    → = Cộng đồng dùng schema override để shape behavior tập thể
    → Chi tiết: Object-Agent.md §4 (schema override classification)
```

---

## §4 — FEEDBACK LOOP

```
🟡 Domain interaction KHÔNG 1 chiều.
   Mỗi interaction → body nhận Satisfaction/Reward/Dissonance →
   → UPDATE valence + schema → LOOP LẠI domain interaction.
   Chi tiết valence update: Valence.md §5.


  CƠ CHẾ — 3 loại update:

    ① REINFORCEMENT (confirm → stronger):
       → Interact → outcome ĐÚNG như schema predict
       → Valence profile: MẠNH hơn (compile deeper)
       → "Bạn A vui mỗi lần gặp" → schema "bạn A = positive" → DEEPER

    ② REVISION (adjust → update):
       → Interact → outcome KHÁC schema predict (nhưng không shock)
       → Valence profile: ADJUST dần
       → "Bạn A hôm nay cáu" → schema "bạn A = positive BUT đôi khi cáu"
       → = Update INCREMENTAL — không phá schema cũ, chỉ refine

    ③ FLIP (dramatic — schema bị phá):
       → Interact → outcome HOÀN TOÀN NGƯỢC schema predict
       → Valence profile: FLIP hoặc CRASH
       → "Bạn A phản bội" → schema "bạn A = positive" → CRASH
       → = Violation (Emergent-Patterns.md §9): investment × severity = impact


  NESTED LOOPS — 3 tầng:

    MICRO (1 interaction):
      → Gặp bạn → nói chuyện → vui → reinforce "bạn = positive"
      → Gặp sếp → bị chê → dissonance → revise "sếp = mixed"
      → = Loop NHANH: minutes-hours

    MESO (relationship trajectory):
      → 100 interactions với bạn A → compiled pattern: "bạn A = reliable positive"
      → 50 interactions với đồng nghiệp B → compiled: "B = inconsistent"
      → = Loop TRUNG BÌNH: weeks-months-years
      → = Emergent patterns FORM ở tầng này (Connection, Enemy, Dependency...)

    MACRO (worldview):
      → 1000+ interactions across many agents → compiled: "con người = trustworthy"
      → HOẶC: 1000+ bad interactions → compiled: "con người = không đáng tin"
      → = Loop CHẬM: years-decades
      → = Schema level cao nhất: agent cụ thể < tổ chức < domain < worldview
      → = Violation ở macro = impact LỚN NHẤT (Emergent-Patterns.md §9)


  CASE — Bạn B (toàn bộ trajectory qua feedback loop):

    Giai đoạn 1 — Mới quen:
      → Vài interactions: vui, share kiến thức
      → Feedback: positive → reinforce → schema "B = positive nhẹ"
      → Loop: approach → interact → reward → approach thêm

    Giai đoạn 2 — Build up:
      → Nhiều interactions: deeper sharing, trust tăng
      → Feedback: consistent positive → deeper compile
      → Schema: "B = reliable positive, L3 positive, agent input positive"
      → = Connection pattern ĐANG FORM (EP.md §2)

    Giai đoạn 3 — Conflict:
      → B nói sau lưng → discovered → VIOLATION
      → Feedback: DRAMATIC negative → schema REVISION hoặc FLIP
      → Investment THẤP (vài tháng) × severity TRUNG BÌNH
        → Impact: moderate → REVISION (không collapse)

    Giai đoạn 4 — Decision:
      → Revised schema: "B = mixed, unreliable"
      → Replaceability: CAO (có bạn khác cùng chunks)
      → Dependency: THẤP (không phải critical agent)
      → → CẮT — cost-benefit: keep B < find alternative
      → = Valence.md §5: revised valence + low dependency → terminate

    Giai đoạn 5 — Post-cut:
      → Schema "B" VẪN tồn tại → nhưng drive = 0 (no approach)
      → Gặp lại → schema fire → body neutral hoặc slightly negative
      → = Compiled schema KHÔNG XÓA — chỉ valence THAY ĐỔI


  ⭐ FEEDBACK LOOP = CƠ CHẾ HỌC:

    Domain interaction KHÔNG static — là ADAPTIVE system:
      → Mỗi interaction = data point
      → Data → update schema → better predict next interaction
      → = LEARNING: body HỌC cách tương tác TỐT HƠN qua thời gian

    Loop mechanics:
      → Positive outcome → reinforce approach → MORE interaction → MORE data
      → Negative outcome → revise/avoid → LESS interaction → LESS data
      → = Positive bias: body INVEST nhiều hơn vào positive relationships
      → = Negative cut: body WITHDRAW từ negative relationships
      → = Adaptive: tối ưu hoá domain interaction qua feedback

    Connection với Imagine-Final:
      → Feedback loop DATA → compiled → Imagine-Final DÙng compiled data
        để preview FUTURE interactions chính xác hơn
      → = Past feedback → better future prediction
      → = Tại sao relationship kinh nghiệm → predict người MỚI tốt hơn
```

---

## §5 — "EMPATHY" REDEFINE

```
⭐ SECTION NÀY KẾT THÚC TOÀN BỘ RESTRUCTURE.

  Mục tiêu:
    Mainstream dùng "empathy" như 1 KHÁI NIỆM — mơ hồ, gộp nhiều thứ.
    Framework TÁCH RÕ: mỗi thứ mainstream gọi "empathy" = mechanism CỤ THỂ.
    Kết quả: KHÔNG CẦN system "empathy" riêng biệt.
    Empathy = CÁCH agent processing TỰ NHIÊN hoạt động.


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  MAINSTREAM "EMPATHY" — tập hợp không rõ ràng:

    Mainstream chia empathy thành:
      → Affective empathy (cảm thấy GIỐNG người khác)
      → Cognitive empathy (HIỂU người khác cảm gì)
      → Empathic concern (MUỐN GIÚP người khác)
    + Thêm:
      → Theory of Mind (hiểu người khác NGHĨ gì)
      → Emotional contagion (cảm xúc LÂY)
      → Compassion fatigue (mệt mỏi vì empathy)
      → Mirror neurons (cơ chế gốc?)

    VẤN ĐỀ:
      → 7+ thuật ngữ, CHỒNG CHÉO, boundary không rõ
      → "Affective empathy" vs "emotional contagion" = khác thế nào?
      → "Cognitive empathy" vs "Theory of Mind" = khác thế nào?
      → Mirror neurons = gốc của CÁI NÀO trong 7 cái trên?
      → = CONFUSION vì gộp nhiều MECHANISMS khác nhau thành 1 "empathy"


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  FRAMEWORK MAPPING — mỗi thuật ngữ = mechanism CỤ THỂ:

  ┌───────────────────────┬─────────────────────────────────────────────────┐
  │ Mainstream term        │ Framework mechanism                             │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Emotional contagion" │ ① PATTERN MATCHING (§1.2)                       │
  │ "cảm xúc lây"        │ Pre-mirror: limbic detect pattern giống          │
  │                       │ experience CỦA MÌNH → body react                │
  │                       │ = Arousal contagion, NOT empathy               │
  │                       │ Mọi động vật có. Trẻ sơ sinh có.              │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Affective empathy"   │ ② AGENT MODELING tầng 1 (§1.2 + §1.6)         │
  │ "cảm thấy giống"     │ Mirror proper: own-state mapping → bản sao      │
  │                       │ body-state AGENT trong body MÌNH               │
  │                       │ + Channel Conversion (§1.5): bản sao → signal  │
  │                       │ = Learned mechanism, 6-24m+ để build           │
  │                       │ Động vật xã hội có. Cần interaction history.   │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Cognitive empathy"   │ ② AGENT MODELING tầng 2 (§1.6)                 │
  │ "hiểu người khác"    │ PFC Extension: interpret mirror signal +        │
  │                       │ simulate SÂU tại sao agent ở state đó         │
  │                       │ = "Phiên bản TÔI đóng vai HỌ"                │
  │                       │ Chỉ người có (cần PFC phát triển).            │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Theory of Mind"      │ ② AGENT MODELING compiled + PFC (§1.2 + §1.6) │
  │                       │ Agent model (learned) + PFC simulate           │
  │                       │ = Đặc biệt: compile deep → ③ Schema Sim       │
  │                       │ = "Biết MẸ sẽ nói gì" = compiled agent model  │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Empathic concern"    │ NURTURING + "CHO ĐI" patterns (EP.md §4-§5)   │
  │ "muốn giúp"          │ Mirror dissonance → perceived ability →         │
  │                       │ Imagine-Final preview → drive hành động         │
  │                       │ = EMERGENT PATTERN từ mirror + valence         │
  │                       │ = KHÔNG phải mechanism riêng — là KẾT QUẢ      │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Compassion"          │ Mirror dissonance (§1.5) + Drive (§1.7)        │
  │                       │ Mirror → channel conversion → dissonance →     │
  │                       │ perceived ability CAO → drive giúp → action    │
  │                       │ = DRIVE sinh ra từ mirror, không phải emotion  │
  │                       │   riêng biệt                                   │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Compassion fatigue"  │ MIRROR OVERLOAD → defense (§1.8)               │
  │                       │ Mirror dissonance tích lũy → cortisol tăng →   │
  │                       │ body CẮT mirror (detach/numb/avoid)            │
  │                       │ = Body self-protect, KHÔNG phải "mất empathy" │
  ├───────────────────────┼─────────────────────────────────────────────────┤
  │ "Mirror neurons"      │ Gộp sai 3 MECHANISMS KHÁC NHAU (§1.2):        │
  │                       │ ① Pattern Matching (pre-mirror)                │
  │                       │ ② Agent Modeling (mirror proper)               │
  │                       │ ③ Schema Simulation (post-mirror)              │
  │                       │ = Tách ra → giải quyết 30 năm tranh cãi       │
  └───────────────────────┴─────────────────────────────────────────────────┘


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ⭐ INSIGHT GỐC — TẠI SAO KHÔNG CẦN "EMPATHY" RIÊNG:

    Empathy = CÁCH agent processing TỰ NHIÊN hoạt động.

    Logic:
      ① Brain cần predict agent (Object-Agent.md: agent = phi logic)
      ② Predict agent → build agent model bằng own-state mapping (§1.1)
      ③ Own-state mapping → mirror BYPRODUCT (§1.2)
      ④ Mirror → channel conversion → signal CỦA MÌNH (§1.5)
      ⑤ Signal → drive hành động (nếu có ability) (§1.7)
      ⑥ Hành động → feedback → update schema (§4)
      ⑦ Repeated → patterns emerge (EP.md: connection, nurturing, cho đi...)

    → TẤT CẢ = domain interaction flow BÌNH THƯỜNG
    → KHÔNG CẦN thêm system "empathy" vào framework
    → "Empathy" = TÊN mainstream ĐẶT cho OUTPUT tự nhiên của agent processing

    Parsimony:
      Mainstream: Body-Base + Schema + Mirror Module + Empathy System + ToM Module
      Framework: Body-Base + Schema + Agent Processing (mirror = byproduct)
      → Ít components hơn → giải thích NHIỀU hơn → parsimony


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  TẠI SAO REDEFINE QUAN TRỌNG:

    ① GIẢM CONFUSION:
       → Mainstream: 7+ terms chồng chéo → researcher tranh cãi definitions
       → Framework: mỗi term = mechanism CỤ THỂ → clear, testable

    ② THỐNG NHẤT CƠ CHẾ:
       → Mainstream: mỗi "empathy" aspect = silos riêng biệt
       → Framework: tất cả = PARTS OF SAME FLOW (domain interaction)
       → Connection, nurturing, "cho đi", fatigue = emergent từ CÙNG bộ cơ chế

    ③ GIẢI THÍCH NHIỀU HƠN:
       → Mainstream: "tại sao người ta mirror tượng đá?" = khó giải thích
       → Framework: §1.2 mechanism ③ Schema Simulation → clear
       → Mainstream: "tại sao trẻ 12m nhặt đồ nhưng chưa an ủi?" = khó
       → Framework: §1.3 → ① đủ cho helping, ② chưa ready cho empathic helping

    ④ PRACTICAL IMPLICATIONS:
       → "Dạy empathy" = KHÔNG DẠY được ① (near-innate) hay ② (needs interaction)
       → CÓ THỂ DẠY: tăng interaction quality → build ② tốt hơn
       → CÓ THỂ DẠY: PFC skills → tầng 2 mạnh hơn (interpret, simulate, chọn response)
       → = Empathy education = INTERACTION QUALITY + PFC TRAINING


  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  EMPATHY × AI — Con Người Có Gì AI Không Có:

    🟡 AI KHÔNG có body → KHÔNG có mirror THẬT:

      AI CÓ (excellent):
        → Tầng 2: PFC-equivalent → analyze, predict, suggest response
        → Pattern matching text/language → detect emotional cues
        → Simulate "nếu người này ở state X → nên response Y"
        → = "Cognitive empathy" in mainstream terms → AI GIỎI

      AI KHÔNG CÓ:
        → Tầng 1: body mirror → KHÔNG có neurons fire cùng pattern
        → Channel conversion → KHÔNG có biochemistry thật
        → Co-regulation → KHÔNG có body để sync với người
        → = "Affective empathy" → AI THIẾU HOÀN TOÀN

      Hệ quả:
        → AI NÓI đúng (tầng 2) nhưng KHÔNG FEEL (tầng 1)
        → Presence AI ≠ presence người (không có mirror loop)
        → AI = excellent TOOL hỗ trợ domain interaction
        → AI ≠ AGENT THẬT trong domain interaction sense
        → = Body mirror = thứ CON NGƯỜI CÓ mà AI KHÔNG CÓ

      Tương lai:
        → AI replace logic, analysis, prediction → OK
        → AI KHÔNG replace mirror, co-regulation, presence
        → Careers cần tầng 1 THẬT (therapy, nursing, teaching, parenting)
          → vẫn cần NGƯỜI — AI hỗ trợ, không thay thế
        → = Empathy (tầng 1) = one of very few irreplaceable human capacities
```

---

## §6 — HONEST ASSESSMENT

```
  ESTABLISHED (🟢) — evidence rõ, framework DỰA TRÊN:

    🟢 Mirror neurons ở khỉ (Rizzolatti 1996):
       single-neuron recording, fire khi thấy agent hành động
    🟢 Shared pain circuits (Singer 2004, Lamm 2011):
       anterior insula + ACC fire khi quan sát người khác đau
    🟢 Theory of Mind circuits (Frith & Frith 2006, Saxe 2006):
       mPFC + TPJ activate cho mental state reasoning
    🟢 Emotional contagion (Hatfield 1994):
       cảm xúc tự lan truyền giữa người — automatic, pre-conscious
    🟢 VTC animate/inanimate (eLife 2019):
       ventral temporal cortex có tổ chức riêng cho animate vs inanimate
    🟢 Spelke Core Knowledge (2007):
       trẻ sinh ra với core systems cho object vs agent
    🟢 Baby Schema response (Lorenz 1943, Glocker 2009):
       nucleus accumbens fire cho infant faces, kể cả non-parents
    🟢 Facial EMG mimicry (Dimberg 2000):
       automatic, 300ms, pre-conscious
    🟢 In-group empathy bias (Xu 2009):
       ACC response mạnh hơn cho in-group members
    🟢 Social buffering (Kiyokawa 2004):
       presence giảm stress response
    🟢 Infant helping (Warneken & Tomasello 2006, 2007):
       14-18 tháng: instrumental helping phức tạp
    🟢 Empathic vs instrumental helping (Svetlova 2010):
       empathic helping khó hơn instrumental ở 18 tháng
    🟢 Self-recognition (Amsterdam 1972):
       rouge test 18-24 tháng, self-other distinction
    🟢 Neonatal imitation debate (Oostenbroek 2016):
       replication failure → neonatal imitation không robust
    🟢 Newborn cry discrimination (Dondi, Simion & Caltran 1999):
       distinguish own vs other cry, differential response
    🟢 Cross-cultural infant emotion (Vreden 2025):
       thermal imaging confirm emotion content response
    🟢 Training override firing rates (Grossman 1995):
       WWII ~15-20% → Vietnam >90%
    🟢 Distance × trauma correlation (Grossman 1995):
       closer combat = more trauma, face → agent model fires
    🟢 Piaget animism (2-7 years):
       normal developmental stage, attribute feelings to objects
    🟢 Cross-species empathy (Church 1959, Masserman 1964):
       chuột freeze, khỉ từ chối ăn khi đồng loại bị shock
    🟢 Placebo effect (extensive literature):
       compiled expectation → real biochemical response
    🟢 Interpersonal synchrony (Feldman 2007):
       physiology syncs during social interaction


  FRAMEWORK SUY LUẬN (🟡) — logic consistent, chưa test trực tiếp:

    🟡 "Mirror = BYPRODUCT của agent processing, không phải module riêng"
       — Consistent: mirror circuits overlap với general prediction circuits
       — Consistent: Heyes ASL (learned), framework thêm WHY (agent = phi logic)
       — Chưa có test trực tiếp phân tách "mirror module" vs "agent processing byproduct"
       — Tuy nhiên: Rizzolatti "innate module" đang mất ground → hướng Heyes/framework

    🟡 "3 mechanisms: Pattern Matching → Agent Modeling → Schema Simulation"
       — Mỗi mechanism có evidence riêng (see 🟢 above)
       — Phân loại 3 mechanisms = framework-specific
       — Mainstream CHƯA tách rõ (gộp thành "mirror")
       — Prediction: nếu tách → giải quyết nhiều tranh cãi hiện tại

    🟡 "Developmental timeline maps 3 mechanisms to stages"
       — Evidence ở mỗi stage có (Dondi, Warneken, Amsterdam, Piaget)
       — Mapping mechanism → stage = framework inference
       — Testable: nếu ① là gốc → trẻ dưới 6m KHÔNG có ② behaviors → consistent

    🟡 "Agency spectrum — mechanism depends on target entity"
       — Evidence: video call < face-to-face (literature)
       — Tượng/ảnh thiêng = schema simulation (consistent với placebo, religious neuro)
       — Full spectrum mapping (mẹ thật → cục đá) = framework

    🟡 "Channel conversion: mirror → existing channels → signal CỦA MÌNH"
       — Consistent: shared neural pathways literature (Singer 2004)
       — "Conversion process" chưa đo trực tiếp
       — Prediction: nếu mirror → channels → nên thấy SAME channel activation

    🟡 "2-tier structure parallel Imagine-Final"
       — Tầng 1 (vô thức) + tầng 2 (PFC) = well-established components
       — Parallel với Imagine-Final = framework structural claim
       — Consistent: cả 2 mechanisms có vô thức + PFC elements

    🟡 "Feedback loop: 3 types (reinforce/revise/flip) × 3 levels (micro/meso/macro)"
       — Components individually supported (reinforcement learning, schema update)
       — Structured categorization = framework-specific
       — Nested loops concept = consistent với multi-level learning theory

    🟡 "Empathy redefine: mainstream terms → specific mechanisms"
       — Mapping IS the framework's primary contribution
       — Each mapping individually reasonable (supported above)
       — Complete mapping table chưa được test as unified model
       — Prediction: nếu mapping đúng → interventions target ĐÚNG mechanism → better outcomes

    🟡 "Imagine-Final × Mirror = double preview"
       — Logical: preview THEIR state + preview MY mirror reward
       — Consistent với anticipatory emotion research
       — "Double preview" formulation = framework-specific


  HYPOTHESIS (🔴) — reasonable nhưng cần thêm evidence:

    🔴 "Mirror intensity ~10-30% bản gốc"
       — Ước lượng từ fMRI activation comparison
       — Không phải direct measurement of subjective experience
       — Range có thể rộng hơn tùy context

    🔴 "Einstein parallel: apply agent modeling lên non-agent"
       — Interesting parallel, chưa có evidence Einstein dùng "mirror-like" processing
       — Historical claim, không testable
       — Useful as illustration, not as evidence

    🔴 "AI không có tầng 1 mirror → irreplaceable human advantage"
       — Depends on definition of "feel" and "consciousness"
       — Philosophical territory, not empirically settleable (yet)
       — Practical implication reasonable: AI behavior ≠ AI experience

    🔴 "Cộng đồng PREVENT animism refinement → religious mechanism"
       — Consistent với observed religious behavior
       — Causal claim (prevent refinement) chưa có direct test
       — Alternative: religious belief = separate mechanism entirely

    🔴 "Schema + Mirror + Threat STACK = triple override"
       — 3 independent sources → combined effect: logical
       — Direct test phân tách 3 pathways chưa có
       — Observable behavior consistent (mẹ hy sinh, nghiện quyên góp)


  TỔNG KẾT:
    🟢 ESTABLISHED: 22 evidence points
    🟡 FRAMEWORK: 9 claims (mỗi claim individually supported, integration = framework)
    🔴 HYPOTHESIS: 5 claims (reasonable, cần thêm evidence)
    → Framework = SYNTHESIS of established evidence
       + framework-specific integration (🟡)
       + some novel predictions (🔴)
    → Strongest claim: "mirror = byproduct of agent processing" (🟡 → potentially 🟢)
    → Most novel claim: "3 mechanisms tách rõ" (🔴 → testable)
```

---

## §7 — CROSS-REFERENCES

```
  DOMAIN INTERACTION FILES (bộ 5):
    → Domain-Interaction.md: overview flow — file NÀY giải thích mechanisms CHO flow đó
    → Object-Agent.md §1-§4: 2 classification modes — basis cho TẠI SAO mirror tồn tại (§1.1)
    → Valence.md §3-§5: multi-channel evaluation — mirror FEED VÀO channels đó (§1.5)
    → Emergent-Patterns.md §2: Connection pattern — mechanisms ở đây SERVE pattern formation
    → Emergent-Patterns.md §4: Nurturing — mirror strength CASES chi tiết (§1.7 ref)
    → Emergent-Patterns.md §5: "Cho đi" — mirror reward override SPECTRUM chi tiết (§1.8 ref)
    → Emergent-Patterns.md §9: Violation — feedback loop FAILURE cases (§4 ref)

  CORE FILES:
    → Core-v7.5-Draft.md §2: Body-Base L0-L3 — channels mà mirror FEED vào (§1.5)
    → Core-v7.5-Draft.md §2.5: Schema override spectrum — cùng mechanism với §1.8
    → Core-v7.5-Draft.md §6: Schema detect body-need → file này: schema trong DI (§3)

  MECHANISM FILES:
    → Imagine-Final.md: product file — file này chỉ reference trong DI context (§2)
    → Imagination-Analysis.md §③: simulate chuỗi nguyên nhân — PFC tầng 2 dùng (§1.6)
    → Logic-Modeling.md: 2 processing modes — Object=Logic, Agent=Modeling connection (§1.1)
    → Cortisol-Baseline.md: mirror dissonance → cortisol → baseline tăng (§1.8)

  SCHEMA FILES:
    → Schema/Anchor-Schema.md: compiled models — file này: schema trong DI (§3)
    → Imagine-Final-Evaluation.md: evaluation framework — mirror feed into evaluation

  DRIVE FILES:
    → Drive/Drive.md: HOW drives combine → action — mirror dissonance = drive source (§1.5)
    → Drive/Novelty.md: novel agent = novelty reward + mirror → double engagement
    → Drive/Threat.md: agent threat = threat drive + mirror suppress — combat cases (§1.1)

  BODY-BASE FILES:
    → Body-Base/Body-Dissonance.md: 14+ signals — mirror ADD dissonance signals (§1.5)
    → Body-Base/Body-Satisfaction.md: satisfaction state — prerequisite cho healthy "cho đi"

  MELODY / PERSONAL:
    → Personal-Melody.md §12: 3 overlap layers (species/culture/personal) — empathy ceiling (§1.6)
    → Global-Melody.md §1: melody sync giữa người — mirror = cơ chế gốc

  RESEARCH / EDUCATION:
    → Empathy-Education.md: dạy empathy — reframe: tăng interaction + PFC training (§5)
    → Domain-Mapping-Drive.md: WHY drive + transition — mirror trong meta-domain context

  BACKUP FILES (content absorbed):
    → backup/Empathy-Mirror.md: §1-§5 → absorbed vào §1.1-§1.6
    → backup/Empathy-Mirror.md: §8-§8.5 → absorbed vào §1.8
    → backup/Empathy-Mirror.md: §9 → absorbed vào §5 (AI section)
    → Mirror-Empathy-Connection-Other/Mirror-Neuron-Analysis.md:
       PRIMARY source → absorbed vào §1.1-§1.4
    → Mirror-Empathy-Connection-Other/plan.md: restructure plan

  SOURCE RESEARCH:
    → Mirror neurons: Rizzolatti 1996
    → Pain empathy: Singer 2004, Lamm 2011
    → Theory of Mind: Frith & Frith 2006, Saxe 2006
    → Emotional contagion: Hatfield 1994
    → VTC: eLife 2019
    → Core Knowledge: Spelke 2007
    → ASL theory: Heyes 2010+
    → Combat psychology: Grossman 1995
    → Infant helping: Warneken & Tomasello 2006, 2007
    → Self-recognition: Amsterdam 1972
    → Newborn cry: Dondi 1999
    → Cross-cultural: Vreden 2025
    → Baby schema: Lorenz 1943, Glocker 2009
    → Social buffering: Kiyokawa 2004
    → Facial mimicry: Dimberg 2000
    → In-group bias: Xu 2009
    → Animism: Piaget
    → Neonatal imitation: Oostenbroek 2016
    → Empathic helping: Svetlova 2010
    → Religious neuroscience: Schjoedt 2009
```

---

> **Bạn không CẦN "empathy" như 1 hệ thống riêng.**
>
> Bạn cần predict agent → brain build model bằng own-state →
> model fire → body bạn phản chiếu → signal chạy qua channels đã có →
> drive bạn hành động → feedback → loop.
>
> Đó là TOÀN BỘ. Không hơn, không kém.
>
> "Empathy" = TÊN mainstream đặt cho OUTPUT tự nhiên
> của agent processing. Cách con người TƯƠNG TÁC với agent
> TRONG domain — không phải system đặc biệt.
>
> Mirror = byproduct. Nurturing = emergent. "Cho đi" = emergent.
> Connection = emergent. Fatigue = overload defense.
>
> Tất cả = domain interaction hoạt động BÌNH THƯỜNG.
> Khi bạn hiểu mechanism, bạn hiểu TẤT CẢ.
