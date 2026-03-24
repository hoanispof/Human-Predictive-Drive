# Architecture v7.5 — Draft Kiến Trúc Mới

> **Trạng thái:** DRAFT v0.5 — chờ somatic confirm trước khi áp dụng
> **Ngày:** 2026-03-23
> **Mục đích:** Kiến trúc mới cho Human-Predictive-Drive framework
> **Nguyên tắc:**
> - Hardware Profile: Modality Balance + PFC Parameters + Receptor Variants
> - Body-Base 4 layers: L0(Alive) + L1(Survival) + L2(Quality) + L3(Pattern)
> - L0 Alive = MẠNH NHẤT (emergency, protect gene)
> - L3 bộ ba: Novelty(expand) + Status(map) + Protect(defend) — mọi động vật xã hội có
> - Imagine (Novelty-Schema + Threat-Schema) = PFC layer, LUÔN phục vụ Body-Base
> - Schema xuyên suốt body → imagine, chunk = đơn vị nhỏ nhất
> - Baseline-drive (cortisol) quyết định "mode" hoạt động của imagine
> - Priority khi conflict: L0 > L1 > L2 > L3 (schema override ĐƯỢC nếu redefine alive)
> **⚠️ Chưa quyết định. Cần test với nhiều case trước khi thay Core.**

---

## 1. Kiến Trúc Tổng Thể — Nhìn 1 Lần Thấy Hết

```
┌──────────────────────────────────────────────────────────────────────┐
│ ENVIRONMENT (bao trùm toàn bộ)                                       │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │ HUMAN (con người)                                              │  │
│  │                                                                │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │ HARDWARE PROFILE (specs — mỗi người KHÁC, thay đổi CHẬM)  │  │  │
│  │  │                                                          │  │  │
│  │  │  Modality Balance:                                       │  │  │
│  │  │    Experience: Visual, Auditory, Somatic, Motor, Emotional│  │  │
│  │  │    Communication: Verbal (label + transfer + compress)   │  │  │
│  │  │    → Mỗi người tỉ lệ KHÁC → encode/process KHÁC        │  │  │
│  │  │                                                          │  │  │
│  │  │  Cognitive Parameters:                                     │  │  │
│  │  │    PFC Parameters:                                       │  │  │
│  │  │      PFC-Capacity:    chất lượng 3-5 chiều workspace    │  │  │
│  │  │        (resolution, noise filter, retrieval, compress) │  │  │
│  │  │      PFC-Clear-Speed: COMT (Val/Val fast ↔ Met/Met slow) │  │  │
│  │  │      PFC-Chunk-Size:  DRD4 — ngưỡng biến động não detect  │  │  │
│  │  │        7R: chỉ detect biến động LỚN (big+slow)          │  │  │
│  │  │        4R: detect cả biến động NHỎ (small+fast)          │  │  │
│  │  │    Mood-Stability: MAO-A (toàn não, không phải PFC)     │  │  │
│  │  │      high activity = dao động ↔ low activity = ổn định  │  │  │
│  │  │                                                          │  │  │
│  │  │  → Hardware set RANGE, experience chọn VỊ TRÍ trong range│  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  │                                                                │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │ BODY-BASE (nền tảng — mọi sinh vật có, sâu dần lên)      │  │  │
│  │  │                                                          │  │  │
│  │  │  Layer 0 — ALIVE (emergency — đang bị đe dọa chết):  │  │  │
│  │  │    Reflex: 50ms, trước não. Protect gene (con).         │  │  │
│  │  │    MẠNH NHẤT — suppress TẤT CẢ. Schema override ĐƯỢC   │  │  │
│  │  │    nếu redefine "alive tiếp" (thiên đàng, gene, nhóm)│  │  │
│  │  │                                                          │  │  │
│  │  │  Layer 1 — SURVIVAL (maintenance — duy trì sự sống):    │  │  │
│  │  │    Oxygen, Nutrition, Temperature, Pain-free, Sleep      │  │  │
│  │  │    Invisible khi met, override L2+L3 khi thiếu.        │  │  │
│  │  │                                                          │  │  │
│  │  │  Layer 2 — QUALITY (chất lượng — sensory input):        │  │  │
│  │  │    Experience: Sensory, Aesthetic, Comfort               │  │  │
│  │  │    Connection: skin, eye, ear, presence (người/đ.vật)   │  │  │
│  │  │                                                          │  │  │
│  │  │  Layer 3 — PATTERN (tối ưu — xử lý trên input):        │  │  │
│  │  │    Novelty:  Mastery, Coherence     — CẢI THIỆN (expand)│  │  │
│  │  │    Status:   Being Seen, Belonging  — CALIBRATE (map)   │  │  │
│  │  │    Protect:  bảo vệ "CỦA TÔI"     — BẢO VỆ (defend)   │  │  │
│  │  │                                                          │  │  │
│  │  │  Emergent (multi-channel × depth):                      │  │  │
│  │  │    Shared Exp ──rep × time──→ Intimate                  │  │  │
│  │  │                                                          │  │  │
│  │  │  Priority: L0 > L1 > L2 > L3 (⚠️ exceptions: §2.5)   │  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  │                                                                │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │ BASELINE-DRIVE (cortisol baseline)                        │  │  │
│  │  │  7 modes: IDLE→LAZY→ACTIVE→FOCUSED→PUSH→FREEZE→CRASH   │  │  │
│  │  │  Sweet spot: VỪA→HƠI CAO = imagine phục vụ body tốt nhất│  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  │                                                                │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │ IMAGINE (PFC — phục vụ Body-Base, không ngoại lệ)        │  │  │
│  │  │  Novelty-Schema — PULL (cải thiện): L0+L1+L2+L3        │  │  │
│  │  │  Threat-Schema  — PUSH (bảo vệ):   L0+L1+L2+L3        │  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  │                                                                │  │
│  │  ┌──────────────────────────────────────────────────────────┐  │  │
│  │  │ HORMONE PHỤ GIA (hỗ trợ toàn hệ thống)                   │  │  │
│  │  │  Activation: NE, Adrenaline, Dopamine (cross-cutting)   │  │  │
│  │  │  Sustain:    Cortisol (spike + sustain)                  │  │  │
│  │  │  Feedback:   Satisfaction Signal (bridge body→schema)    │  │  │
│  │  │  Recovery:   Endorphin, Endocannabinoid                  │  │  │
│  │  │  Social:     Vasopressin (Protect), Oxytocin (boost)     │  │  │
│  │  │  Mood:       Serotonin (ruột 95%)                        │  │  │
│  │  │  ...GABA, glutamate, và các hormone khác                 │  │  │
│  │  └──────────────────────────────────────────────────────────┘  │  │
│  │                                                                │  │
│  │  ╔══════════════════════════════════════════════════════════╗  │  │
│  │  ║ SCHEMA (xuyên suốt body→imagine, vô thức→ý thức)        ║  │  │
│  │  ║  Chunk = đơn vị nhỏ nhất (atom of schema)                ║  │  │
│  │  ║    Multi-modal (rải rác nhiều vùng), tạo từ vô thức + PFC║  │
│  │  ║  Schema = tổ hợp chunks → compiled patterns              ║  │  │
│  │  ║  Gradient: body-need (sâu) → values (giữa) → skills (nông)║  │
│  │  ║  Vô tận — AI hỗ trợ bắt buộc                            ║  │  │
│  │  ╚══════════════════════════════════════════════════════════╝  │  │
│  │                                                                │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │ DOMAIN (thực tế bên ngoài Human — vô tận, có điểm hội tụ)     │  │
│  │  Tồn tại KHÔNG phụ thuộc não biết hay không                  │  │
│  │  Não chỉ chứa FRAGMENTS (chunks) — không bao giờ chứa hết   │  │
│  │  Có ATTRACTOR POINTS (patterns tối ưu tự hội tụ)             │  │
│  │  Body-Base = giao diện DUY NHẤT giữa Human và Domain         │  │
│  │  Schema quality = mức hội tụ với domain reality               │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 1.5 HARDWARE PROFILE — Sơ Lược

```
Mỗi người có "specs" KHÁC NHAU — ảnh hưởng CÁCH xử lý mọi thứ:

MODALITY BALANCE — cách encode/process thông tin:
  5 Experience modalities: Visual, Auditory, Somatic, Motor, Emotional
  1 Communication modality: Verbal (label + transfer + compress, KHÔNG compute)
  → Mỗi người tỉ lệ KHÁC → cùng input → process KHÁC → output KHÁC
  → Somatic-dominant: concept trước, label sau → cross-domain → improviser
  → Verbal-dominant: label trước, concept qua label → sequential → specialist
  → Visual-spatial: structural pattern match → architect/physicist
  → Chi tiết: Modality-Analysis.md

COGNITIVE PARAMETERS — ảnh hưởng chéo lẫn nhau:

  PFC PARAMETERS (3 tham số thuộc PFC):

    ① PFC-Capacity — chất lượng workspace 3-5 chiều:
       → Mọi người hold ~3-5 CHIỀU cùng lúc (physics limit: interference)
       → 10 tỉ vs 12 tỉ neurons PFC → VẪN ~3-5 chiều (KHÔNG thêm)
       → Capacity KHÁC NHAU ở CHẤT LƯỢNG per-chiều:
         Resolution: mỗi chiều RÕ hay MỜ
         Noise filter: giữ sạch dù nhiễu hay dễ mất
         Retrieval: lấy chunk từ vô thức nhanh/đúng hay chậm/sai
         Compression: compile chunk chặt → mỗi item CHỨA NHIỀU
       → Capacity CAO: "nhìn 4 thứ, THẤY cả vũ trụ" (expert compression)
       → Capacity THẤP: "nhìn 4 thứ, chỉ THẤY 4 thứ" (raw, no compression)
       → Giải quyết 3-5 limit bằng: draft → compile → stack → pyramidal
         (4×4×4 = 64 thông tin gốc compressed thành 4 meta-chunks)
       → Hardware: PFC connection density + wiring quality (không phải số neurons)

    ② PFC-Clear-Speed — draft retention (COMT enzyme, PFC-specific):
       → Val/Val: clear NHANH → draft mất → BUỘC rebuild fresh → improviser tendency
       → Met/Met: linger LÂU → draft giữ → tiếp tục trên nền cũ → specialist tendency
       → = KHÔNG phải "chọn" improviser/specialist — hardware BIAS, experience fine-tune

    ③ PFC-Chunk-Size — ngưỡng biến động não mà PFC detect được (DRD4 receptor):

       CƠ CHẾ:
       → Vô thức: neurons fire liên tục → thử đồng bộ → patterns hình thành
       → VTA (cụm nhỏ ~400K neurons, giữa não): detect BIẾN ĐỘNG (delta)
         → VTA hoạt động theo HABITUATION: quen cái gì → lờ đi
         → Schema cũ fire ĐỀU → VTA QUEN → im (dù mạnh)
         → Pattern THAY ĐỔI (thêm/bớt neurons sync) → VTA detect → fire
         → = Detect THAY ĐỔI so với hiện tại, không phải "mới" hay "mạnh"
       → Dopamine gửi tới PFC qua axon ĐÃ MỌC SẴN
       → Dopamine gắn DRD4 receptor TRÊN PFC neuron:

       7R receptor kém nhạy → DISTURBANCE THRESHOLD CAO:
         → Chỉ biến động LỚN (nhiều neurons thêm vào sync) mới vượt threshold
         → PFC nhận ÍT signal → nhưng mỗi signal = biến động LỚN
         → PFC spotlight xuống → chunk thường LỚN → body-base reward LỚN per detect
         → Phải ĐỢI LÂU hơn (vô thức cần thời gian tích lũy đồng bộ đủ lớn)
         → "........ AHA!" (chờ lâu, 1 insight lớn)

       4R receptor nhạy → DISTURBANCE THRESHOLD THẤP:
         → Biến động NHỎ cũng vượt threshold
         → PFC nhận NHIỀU signal → mỗi signal = biến động NHỎ
         → Body-base reward NHỎ per detect → nhưng LIÊN TỤC
         → "ồ... ồ... ồ..." (nhiều, nhỏ, liên tục)

       → Hypothesis D (Disturbance Threshold) — framework đề xuất ⭐
         Giải quyết mâu thuẫn interpretation cũ "kém nhạy → seek more":
         CŨ: "7R kém nhạy → ít sướng → seek more để bù" → MÂU THUẪN logic
         MỚI: "7R threshold cao → chỉ detect lớn → mỗi lần reward LỚN → THÍCH novelty"
         → Mọi case consistent: scroll MXH, cờ bạc, gặp khó, chất kích thích ✅

       → Dopamine = SIGNAL "có biến động đáng chú ý" (KHÔNG phải reward)
       → Reward thật = body-base confirm chunk có giá trị → opioid
       → "Nghiện dopamine" = pop science SAI — thực ra nghiện BODY REWARD (opioid)

       NOTE: VTA detect BIẾN ĐỘNG qua habituation (quen → khác quen → fire)
         Có thể KHÔNG cần "predict → compare → error" phức tạp (Schultz 1997)
         "Quen → khác quen → fire" = simpler mechanism, CÙNG observable result
         Chi tiết: PFC-Analysis.md §8.3

  MOOD-STABILITY (KHÔNG phải PFC — toàn não):

    ④ Mood-Stability (MAO-A enzyme, brain-wide):
       → MAO-A high activity: clear dopamine+serotonin+NE NHANH → mood DAO ĐỘNG
       → MAO-A low activity: clear CHẬM → mood ỔN ĐỊNH
       → Khác COMT: COMT chỉ PFC (local), MAO-A toàn não (global)
       → Ảnh hưởng "nền" mood, KHÔNG trực tiếp ảnh hưởng PFC draft

  → 4 parameters TƯƠNG TÁC với nhau:
    PFC-Cap cao + Clear nhanh + Chunk lớn + Mood ổn = "improviser mạnh, đột phá"
    PFC-Cap cao + Clear chậm + Chunk nhỏ + Mood ổn = "specialist sâu, stable"
    PFC-Cap thấp + Clear nhanh + Chunk lớn + Mood dao động = "restless, frustrated"
    ...nhiều combinations → mỗi người UNIQUE
  → Chi tiết: PFC-Analysis.md §8

TỔNG THỂ:
  Hardware set RANGE → experience chọn VỊ TRÍ trong range
  → Mỗi người = combination UNIQUE của modality + 4 cognitive parameters
  → = "Specs máy" quyết định "software (schema) chạy thế nào"
  → KHÔNG quyết định "muốn gì" (body-base) — chỉ quyết định "xử lý thế nào"
```

---

## 2. BODY-BASE — Chi Tiết

### 2.0 Layer 0 — Alive (tồn tại tức thì — emergency)

```
"Tôi ĐANG BỊ GIẾT / con tôi ĐANG BỊ GIẾT?"
= Lớp KHẨN CẤP — chỉ active khi đe dọa sống chết NGAY LẬP TỨC
= KHÁC Layer 1 Survival: L1 = duy trì (chậm), L0 = emergency (tức thì)

  Phản ứng: 50ms (reflex tủy sống — TRƯỚC cả não)
    → Rút tay khỏi lửa → tủy sống xử lý → não CHƯA BIẾT đau
    → Giật mình → brainstem (30ms) → trước PFC
    → Ngã xuống nước → vùng vẫy panic → reflex

  MẠNH NHẤT — suppress TẤT CẢ khi active:
    Đang scroll MXH → bị đánh → MỌI THỨ cancel NGAY
    Đang suy nghĩ sâu → nhà cháy → PFC offline → chạy
    → = Override L1, L2, L3, Imagine, Status, Novelty → TẤT CẢ

  BAO GỒM Protect Gene (con):
    → L3 Protect: giữ đồ, giữ vị trí (CÓ THỂ nhường, negotiate)
    → L0 Protect Gene: bảo vệ CON khỏi chết (KHÔNG nhường, emergency)
    → Gà mái vs diều hâu: L0, không phải L3
    → Mẹ nhấc xe cứu con: L0 override survival THÂN
    → Vì: gene survival > individual survival (Trivers 1972)
    → ⚠️ L0 Protect Gene ≠ L3 Protect Resource

  Schema override L0 — CẦN redefine "alive":
    → Schema KHÔNG BAO GIỜ nói "chết = hết hoàn toàn"
    → Schema luôn bổ sung "alive TIẾP SAU đánh đổi":
      Tử vì đạo: "chết → thiên đàng" = soul alive tiếp
      Hy sinh vì con: "tôi chết → con sống" = gene alive tiếp
      Kamikaze: "tôi chết → dân tộc sống" = group alive tiếp
    → = Schema override L0 bằng REDEFINE alive (gene/soul/group)
    → Nếu schema KHÔNG có "alive tiếp" → L0 THẮNG → sợ chết

  KHÔNG CẦN PFC:
    → Hardware pure: tủy sống, brainstem, amygdala
    → Mọi động vật có (kể cả côn trùng)
    → PFC chỉ tham gia SAU KHI emergency qua ("chuyện gì vừa xảy ra?")

  KHÁC L1 Survival:
    L0: ĐANG chết → phản ứng NGAY (giây)
    L1: CẦN resource để TIẾP TỤC sống → tìm (giờ → ngày)
    L0: fight/flight/freeze REFLEX
    L1: đói → tìm ăn (có thể chờ)
    L0: KHÔNG THỂ chờ
    L1: CÓ THỂ chờ (tùy tolerance)

  Escalation L3 → L0:
    Giữ đồ (L3 Protect) → bình thường, có thể nhường
    Đối phương rút dao → threat MẠNG SỐNG → L0 activate
    → Bỏ đồ, chạy (L0 override L3: sống > đồ)
    → HOẶC: đồ = resource DUY NHẤT (nước cuối cùng trên sa mạc)
      → L0 giữ + fight (mất resource = chết = L0)
```

---

### 2.0.5 Layer 1 — Survival (duy trì sự sống)

```
"Tôi đang SỐNG không?" — duy trì, không phải emergency
= Lớp duy trì, invisible khi met, override L2+L3 khi thiếu

  Oxygen       — thở: brainstem auto, KHÔNG CẦN não
  Nutrition    — ăn đủ/uống đủ: hypothalamus detect, ghrelin/leptin
                 ⚠️ KHÁC L2 Sensory: L1 Nutrition = ăn ĐỦ (no = relief)
                    L2 Sensory = ăn NGON (opioid = pleasure)
                    Có thể fire CÙNG LÚC: đói + ăn ngon = double reward (L1 + L2)
                    Nhưng 2 reward KHÁC NHAU, 2 layer KHÁC NHAU
  Temperature  — không quá nóng/lạnh: thermoregulation auto
  Pain-free    — không bị tổn thương: nociceptors + reflex (50ms)
  Sleep        — não phải reset: adenosine buildup → sleep pressure
                 ⚠️ Sleep = survival nhưng TOLERANCE CAO (nợ tích lũy):
                    Thiếu oxy: chết trong PHÚT → tolerance cực thấp
                    Thiếu ăn: chết trong TUẦN → tolerance trung bình
                    Thiếu ngủ: suy thoái trong TUẦN→THÁNG → tolerance cao
                    Nhưng: thiếu đủ lâu = VẪN CHẾT/SỤP → vẫn L1 survival

  Đặc điểm:
    → Invisible khi met: thở bình thường → KHÔNG nghĩ về oxy
    → Override khi thiếu: đói cực → CANCEL mọi Novelty/Status/Connection
    → Vô thức hoàn toàn: brainstem + tủy sống, TRƯỚC não cortex
    → Mọi sinh vật có (kể cả côn trùng, cá, giun) ✅
    → Reward = RELIEF (hết đói = nhẹ), không phải PLEASURE (ăn ngon)
    → Satisfaction Signal RÕ NHẤT: no = dừng ăn, đủ oxy = dừng thở gấp

  Xã hội hiện đại:
    → Hầu hết đã met → invisible → không ai nghĩ tới
    → NGOẠI TRỪ Sleep: nhiều người VI PHẠM mà không biết
      → Ngủ 5-6h thay vì 7-8h → Layer1 THIẾU mà không nhận ra
      → → Cortisol baseline TĂNG → cascade ảnh hưởng L2, L3, Imagine
      → = Sleep debt = Layer1 violation phổ biến nhất hiện đại

  Khi Layer1 thiếu → mọi layer khác BỊ OVERRIDE:
    Đói cực: không care ăn NGON (L2), không care STATUS (L3)
    Đau: không care NOVELTY (L3), không care AESTHETIC (L2)
    Thiếu oxy: KHÔNG CARE GÌ CẢ — body auto-survival
    → = Priority Layer1 > mọi thứ ✅
    → = Giải thích Maslow hierarchy tầng 1 (nhưng không phải "xong mới lên")
```

### 2.1 Layer 2 — Quality (chất lượng sống — sensory input)

```
EXPERIENCE (input từ thế giới — opioid reward):

  Sensory    — mouth, nose, tongue: ăn ngon, hương thơm, vị
               Ví dụ: trái cây chín trên đảo hoang → ngon → sướng 1 mình ✅
  Aesthetic  — eyes, ears: visual/auditory harmony, pattern đẹp
               Ví dụ: nhìn hoàng hôn → rùng mình → sướng 1 mình ✅
               Ví dụ: thấy cô gái đẹp → thích → KHÔNG BIẾT tại sao
               Ví dụ: thích màu xanh → mua đồ màu xanh → thấy thích hơn
               Ví dụ: nghe nhạc cụ lạ → tự nhiên thấy hay
               = Body phản ứng TRƯỚC → lý do tạo SAU (hoặc không cần)
               ⚠️ KHÁC Coherence: Aesthetic = thích mà KHÔNG CẦN hiểu tại sao
                  Coherence = hiểu tại sao → sướng vì HIỂU
                  (có thể chồng lấp: thích + tìm hiểu tại sao thích)
  Comfort    — da, cơ, nhiệt: homeostasis, body ease
               Ví dụ: nằm bãi cát ấm → thoải mái → sướng 1 mình ✅
               = THUẦN body, trực tiếp nhất

  → 3 channels = PURE sensory input → opioid TRỰC TIẾP
  → Mọi động vật có ✅ (không cần PFC, không cần xã hội)
  → Satisfaction Signal RÕ (ăn no = đủ, thoải mái = đủ)


CONNECTION (input từ người/động vật khác — oxytocin reward):

  Tiếp xúc trực tiếp với sinh vật khác, bao gồm:
    Skin: chạm, ôm, vuốt → oxytocin trực tiếp
    Eye:  nhìn mắt nhau → kết nối, đồng cảm
    Ear:  nghe giọng nói, tiếng kêu → "có ai đó", an tâm
    Presence: thấy/cảm nhận họ ở đó → "không cô đơn"

  Ví dụ người: ôm mẹ, nhìn mắt bạn, nghe giọng người thân
  Ví dụ thú cưng: vuốt mèo, chó nằm cạnh, cá bơi trong bể
    → Thú cưng: Connection L2 ĐẦY ĐỦ (skin+eye+ear+presence)
    → Nhưng: Layer3 THIẾU (thú cưng không Being Seen, không Belonging)
    → = "Có thú cưng bớt cô đơn nhưng vẫn thiếu gì đó"

  → Tất cả động vật xã hội có ✅
  → Satisfaction Signal RÕ (ôm đủ = body relaxed = đủ)

TỔNG LAYER 2:
  Experience: 3 channels (Sensory, Aesthetic, Comfort) — input từ thế giới
  Connection: 1 channel (skin, eye, ear, presence) — input từ sinh vật khác
  = 4 channels RAW INPUT → opioid/oxytocin trực tiếp
  = Mọi động vật có ✅ — không cần PFC, không cần xã hội phức tạp
```

### 2.2 Layer 3 — Pattern Process (xử lý trên input)

```
NOVELTY (detect mới + cải thiện — dopamine + opioid):

  Mastery    — predict + execute → MATCH → sướng
               "Tôi làm được!" — body confirm hành động khớp hình dung
               Ví dụ: đắp lâu đài cát → mắt thấy đẹp (L1:Aesthetic)
                       → tay thấy vừa (L1:Comfort) → "TÔI LÀM ĐƯỢC"
               Ví dụ khác: chim làm tổ → thử cách mới → tổ chắc hơn
                       → KHÔNG CÓ PFC → VẪN mastery ✅
               = Body-level Novelty: improvement qua trial-error
               = Phục vụ body: xây chòi → trú mưa → survive

  Coherence  — connect patterns → understand → sướng
               "Aha, hiểu rồi!" — não match random data thành structured
               Ví dụ: "tại sao bầu trời xanh?" → tán xạ ánh sáng
                       → Sensory(nhìn trời) + hiểu(tại sao) → sướng SÂU hơn
               Ví dụ: chó ngửi trail → connect mùi → tìm đường
                       → Pattern match cơ bản → KHÔNG CẦN PFC
               = Body-level: pattern detection → predict TỐT hơn → body benefit
               = Phục vụ body gián tiếp: hiểu → schema chính xác hơn → survive tốt

  → 2 Novelty channels = PROCESS trên Layer2 input → improve behavior
  → Mọi động vật có ở mức cơ bản ✅ (trial-error, pattern detect)
  → Người: PFC NÂNG CẤP thêm (cross-domain coherence, complex mastery)
  → Satisfaction Signal MƠ HỒ ("đủ giỏi" và "đủ hiểu" khó xác định)


STATUS (schema access map — serotonin candidate, chưa proven ở người):
  → Chi tiết: xem Status-Analysis-v2.md

  ⚠️ KHÁI NIỆM MỚI — khác training data AI thông thường.
     Đọc Status-Analysis-v2.md để hiểu ĐÚNG ý nghĩa.

  DEFINITION NGẮN GỌN:
    Status = bản đồ "schemas nào SẴN SÀNG triển khai
             với NGƯỜI NÀY trong CONTEXT NÀY"
    = Schema Access Map — DYNAMIC, per-person × per-context
    ≠ hierarchy rank, ≠ prestige, ≠ tham vọng quyền lực
    Function CHẮC CHẮN CÓ (quan sát + somatic confirm ở mọi người)
    Hormone = serotonin candidate (evidence gián tiếp từ khỉ + SSRI, chưa đo trực tiếp ở người)
    Serotonin = CERTAINTY BIAS NỀN (chậm, body-level) — KHÔNG quyết định
    PFC + Schema = QUYẾT ĐỊNH THỰC SỰ per-context (nhanh, có data → override bias)
    → Chi tiết: Status-Analysis-v2.md §10.6

  Being Seen — calibrate status map cho ĐÚNG thực tế
    "Họ biết tôi làm được gì" → map chính xác → hợp tác hiệu quả

  Belonging — cached status maps → giảm scan cost + backing
    Nhóm quen = maps ĐÃ CALIBRATE → không cần scan → thoải mái

  Chức năng:
    → AMPLIFY access Layer2: map rộng → dám seek → body-need DỄ meet
    → QUYẾT ĐỊNH schema nào sẵn sàng (LẤY ↔ TRAO ĐỔI ↔ COMPLY)
    → "Tấn công" = KHÔNG phải drive riêng → Status extreme (gap cực lớn)
    → Aspiration → Imagine: Status-Drive / Status-Threat

  3 layers Status (KHÔNG gộp):
    ① Status baseline: ổn định, carry across contexts, KHÔNG tốn PFC
       = trung bình experience từ 5-20 người quen thường gặp
    ② Status per-context quen: compiled maps, switch NHANH, tốn PFC ÍT
    ③ Status context mới: draft maps mới, tốn PFC NHIỀU, cortisol tăng
    → Switch context (PFC) ≠ calibrate status (body-level)
    → Chi tiết: Status-Analysis-v2.md §8

  → Mỗi người calibrate range KHÁC (ổn định ↔ dao động) → Status Flexibility
  → Mọi động vật xã hội có ✅
  → Satisfaction Signal MƠ HỒ ("đủ respect" khó xác định)


PROTECT (bảo vệ "CỦA TÔI" — vasopressin candidate):

  ⚠️ Protect = bảo vệ BẤT CỨ THỨ GÌ body đã tag "của tôi"
     KHÔNG giới hạn Connection — xuyên suốt mọi layer

  Cơ chế: body TAG "của tôi" → khi bị đe dọa → Protect ACTIVATE:
    Protect L1: giữ thức ăn, giữ lãnh thổ, giữ chỗ ngủ
    Protect L2: giữ đồ chơi (Sensory), giữ chỗ quen (Comfort),
                giữ người thân/thú cưng (Connection)
    Protect L3: giữ bản quyền (Mastery), giữ niềm tin (Coherence),
                giữ vị trí (Status), giữ nhóm (Belonging)
    Protect Emergent: ghen tuông = giữ Intimate bond

  Ví dụ:
    Trẻ 2 tuổi giữ đồ chơi: "CỦA TÔI!" → PFC gần zero → body-level ✅
    Chó giữ xương: growl khi ai tới gần → vô thức ✅
    Ghen tuông: "người yêu nói chuyện với ai?" → protect Intimate bond
    Bảo vệ bản quyền: "TÔI làm ra cái này" → protect Mastery output
    Bảo vệ làng: "lãnh thổ CỦA NHÓM TÔI" → protect Belonging territory

  Tại sao có người protect MẠNH, có người share THOẢI MÁI:
    → Protect mạnh: schema "mất = thiệt, phải giữ" → vasopressin response cao
    → Share thoải mái: schema "share = tốt hơn giữ" → override protect
      Ví dụ: share framework → người khác feedback → TÔI improve → body benefit
      = Schema "share phục vụ body-base TỐT HƠN giữ" → protect không cần fire
    → = MỨC ĐỘ protect tùy schema, không chỉ tùy hormone

  KHÔNG CÓ sub-channels riêng:
    → Protect = 1 FUNCTION áp dụng lên TẤT CẢ channels
    → Tương tự Status amplify mọi channel → Protect defend mọi channel
    → Target = bất kỳ thứ gì body tag "của tôi"

  3 chức năng L3 COMPLEMENT nhau:
    Novelty = tìm MỚI (offensive, mở rộng)
    Status = biết ĐỨNG ĐÂU (navigation, calibrate)
    Protect = giữ ĐÃ CÓ (defensive, bảo vệ)
    → Expand + Map + Defend = bộ ba hoàn chỉnh

  → Mọi động vật có ✅ (chó giữ xương, chim giữ tổ, khỉ giữ lãnh thổ)
  → Body-level, trước PFC ✅
  → Hormone: Vasopressin = candidate chính, có thể kết hợp hormone khác
  → Satisfaction Signal: RÕ khi threat QUA ("an toàn rồi" → cortisol drop)
    nhưng MƠ HỒ khi threat TIỀM ẨN ("có thật sự an toàn?")

TỔNG LAYER 3: Novelty(Mastery, Coherence) + Status(Being Seen, Belonging) + Protect
  = PROCESS Layer2 input → improve + calibrate + defend
```

### 2.3 Emergent — Multi-channel Bond

```
Khi nhiều body-base channels hoạt động ĐỒNG THỜI với CÙNG NGƯỜI:

  ←── nông ──────────── spectrum ──────────── sâu ──→
  Shared Experience                           Intimate
  Tạm thời                                   Bền vững
  Nhiều người trigger được                    Ít người trigger
  Schema chưa compiled sâu                    Schema compiled sâu
  Bond nhẹ, nhanh tạo + mất                  Bond sâu, chậm tạo + mất

  Cơ chế:
    Shared Exp = Experience channels + Connection ĐỒNG THỜI
      Xem hoàng hôn(Aesthetic) cùng bạn(Connection:presence)
      → Opioid + Oxytocin CÙNG LÚC → amplify lẫn nhau

    Intimate = Shared Exp × REPETITION × TIME → COMPILED TRUST
      "Người này an toàn TUYỆT ĐỐI" (schema compiled sâu)
      → Amplify TẤT CẢ channels khác khi cùng người đó:
        Ôm người yêu > ôm người lạ (Touch amplified)
        Ăn cùng người yêu > ăn 1 mình (Sensory amplified)

  Shared Exp ──repetition × time──→ Intimate
  (bạn mới cùng xem phim vài lần → dần thân → intimate)

  → KHÔNG phải channels riêng → EMERGENT từ channels chồng lấp
  → Nhưng quan trọng vì: Intimate = DEEPEST form of Connection
```

### 2.5 Priority Exceptions — Khi L1 Survival BỊ Override

```
BÌNH THƯỜNG: L1 Survival > L2 Quality > L3 Pattern
  → Đói cực → cancel mọi Novelty/Status
  → Đau → cancel mọi Aesthetic/Mastery
  → = Priority chuẩn, đúng 95% cases

NGOẠI LỆ 1 — Protect(con/gene carrier) > L1 Survival(thân):
  → Gà mái vs diều hâu: chắc chắn thua → VẪN FIGHT → vì con
  → Mẹ nhấc xe cứu con: adrenaline vượt giới hạn bình thường
  → Bố lao vào lửa cứu con: survival bị override

  Tại sao? Parental investment theory (Trivers, 1972):
    → Gene CỦA CON = gene CỦA TÔI
    → Thân tôi già → sẽ chết → con MANG GENE đi tiếp
    → Body: bảo vệ con = bảo vệ GENE → mạnh hơn bảo vệ THÂN
    → = Gene survival > Individual survival

  Giới hạn:
    → CHỈ khi target = gene carrier (con, đôi khi partner/cha mẹ)
    → KHÔNG phải mọi Protect > Survival (không ai chết vì giữ đồ chơi)
    → = Ngoại lệ CỤ THỂ, không phải chung

NGOẠI LỆ 2 — Schema compiled ĐỦ SÂU override L1 Survival:
  → Schema đã train + reinforce + compiled → MẠNH HƠN body survival signal

  Loại A — Threat-Schema (không làm = mất LỚN hơn chết):
    → "Nếu không hy sinh → gia đình chết"
    → Threat calculate: chết 1 mình < 5 người chết
    → Ví dụ: lính nhảy lên lựu đạn cứu đồng đội

  Loại B — Novelty-Schema (làm = reward CỰC LỚN sau chết):
    → "Tử vì đạo → thiên đàng → reward VÔ HẠN"
    → Schema compiled từ nhỏ + cộng đồng reinforce
    → Body: "chết = MẤT" → Schema: "chết = ĐƯỢC TẤT CẢ"
    → Schema THẮNG body khi compiled đủ sâu
    → = Imagine disconnect body ở mức CỰC ĐẠI

  Loại C — Status + Belonging + Protect STACK:
    → Yêu nước + đồng đội bond + vị trí lính + protect tổ quốc
    → Mỗi cái 1 mình KHÔNG đủ override survival
    → STACK nhiều → ĐỦ override
    → Ví dụ: kamikaze = threat(gia đình) + status(samurai) + belonging(quốc gia)

  Loại D — CRASH mode (survival drive đã sụp):
    → Cortisol CỰC CAO → survival drive GIẢM
    → "Sống cũng khổ, chết cũng vậy"
    → Schema "hy sinh" KHÔNG BỊ CẢN vì survival ĐÃ YẾU
    → Ví dụ: nô lệ nổi dậy biết sẽ chết → "chết còn hơn"

  ⚠️ Implication — tại sao radicalization NGUY HIỂM:
    → Train schema (Loại B+C) đủ sâu từ nhỏ + reinforce liên tục
    → → Schema override survival → người sẵn sàng chết
    → = Brainwashing = compile schema MẠNH HƠN L1 Survival
    → = Không phải "dũng cảm" hay "điên" — là schema engineering

→ Priority L0 > L1 > L2 > L3 = ĐÚNG cho đa số tình huống
→ L0 Alive = MẠNH NHẤT (emergency, protect gene)
→ Ngoại lệ: Schema compiled cực sâu override ĐƯỢC L0
  nếu redefine "alive tiếp" (thiên đàng, gene, nhóm)
→ Tất cả GIẢI THÍCH ĐƯỢC bằng framework, không phá kiến trúc

QUAN TRỌNG — Override là SPECTRUM, không chỉ cực đoan:

  Schema Imagine override body-base = CÙNG CƠ CHẾ ở MỌI mức độ:

  Nhẹ (hàng ngày):     đọc sách quên ăn, scroll MXH tới 2h sáng
  Trung bình:           workaholic quên ngủ, nghiện game bỏ bê body
  Nặng:                 game tới chết, anorexia, cờ bạc phá sản
  Cực đoan:             tử vì đạo, kamikaze

  = CÙNG mechanism: Schema suppress body signal
    ① Schema redirect attention (ignore body signal)
    ② Cortisol từ schema suppress body sensation (biochemistry)
    → Double suppress → body GẦN NHƯ câm → schema chạy tự do

  → Priority L0 > L1 > L2 > L3 = "nên" (healthy design)
  → Thực tế: Schema CÓ THỂ phá priority BẤT KỲ LÚC NÀO
  → Quên ăn trưa vs tử vì đạo = cùng cơ chế, khác mức độ
  → = BUG lớn nhất hệ thống con người (cho cá nhân)
  → = Hoặc FEATURE (cho phép hy sinh → gene/tập thể survive)
```

### 2.6 Tại sao kiến trúc này THIẾT YẾU?

```
Xác thực — MỌI schema, MỌI hành vi trace về body-base:

  Layer1 (Survival):
    Thở gấp khi thiếu oxy → Oxygen ✅
    Đói → tìm ăn          → Nutrition ✅
    Rét → tìm chỗ ấm      → Temperature ✅
    Rút tay khi chạm lửa  → Pain-free ✅ (reflex 50ms, trước PFC)
    Ngáp, mất tập trung   → Sleep ✅

  Layer2 (Quality):
    Ăn phở               → Sensory ✅ (ngon, không chỉ no)
    Nhìn hoàng hôn        → Aesthetic ✅
    AC 20°C + chăn        → Comfort ✅
    Ôm mẹ, vuốt mèo      → Connection ✅

  Layer3 (Pattern):
    Giải toán 1 mình      → Mastery ✅ (predict+execute match)
    "Tại sao trời xanh?"  → Coherence ✅ (pattern match)
    "Họ biết tôi giỏi gì" → Being Seen ✅ (status calibrate)
    Đi nhà thờ            → Belonging ✅ (status efficiency)
    Trẻ giữ đồ chơi       → Protect ✅ ("CỦA TÔI!")
    Ghen tuông             → Protect ✅ (giữ intimate bond)
    Bảo vệ bản quyền      → Protect ✅ (giữ mastery output)

  Emergent:
    Xem phim cùng bạn     → Shared Exp ✅
    Người yêu hiểu mình   → Intimate ✅

  Imagine (phục vụ body-base):
    Scroll MXH            → Novelty-{Sensory+Being Seen} ✅
    Game                   → Novelty-{Mastery+Belonging} + Status ✅
    Deadline               → Threat-{Status+Sensory(income)} ✅
    Build framework        → Novelty-{Coherence+Mastery} ✅
    Lo vô cớ               → Threat-{Comfort(body regulate)} ✅

  → KHÔNG tìm thấy ngoại lệ
  → Layer1 thường invisible — chỉ hiện khi thiếu (sleep debt phổ biến nhất)
  → Mọi hành vi trace về Layer1, Layer2, hoặc Layer3 body-base
```

---

## 3. BASELINE-DRIVE — Nền Năng Lượng

```
"Hệ thống đang ở mức sẵn sàng nào"
Hormone chính: Cortisol baseline

CHỨC NĂNG:
  → Duy trì sự SẴN SÀNG cho schema hoạt động
  → Thường ổn định (kết hợp duy trì cho nhiều schema đang active)
  → Quyết định "mode" mà Imagine hoạt động

7 MODES (theo mức cortisol baseline):

  CỰC THẤP → IDLE:
    → Threat-drive: ❌ (không phản ứng threat)
    → Novelty/PULL: ✅ nếu đủ hấp dẫn (dopamine vẫn hoạt động)
    → Body-need: ✅ nếu có (đói vẫn ăn, đau vẫn tránh)
    → PFC: gần offline cho planning, chỉ respond reward trực tiếp
    → Trạng thái: "không care" — trống, flat, vegetative
    → Ví dụ: trầm cảm nặng, kiệt sức hoàn toàn

  THẤP → LAZY:
    → Threat-drive: ❌ ("biết phải làm nhưng không làm")
    → Novelty/PULL: ✅ (thích thì làm, không thích thì thôi)
    → Body-need: ✅
    → PFC: minimal — chỉ draft cho việc thích
    → Trạng thái: scroll MXH, xem phim, trì hoãn, "lười nhưng thoải mái"
    → Ví dụ: cuối tuần rảnh, kỳ nghỉ dài

  VỪA → ACTIVE (optimal zone):
    → Threat-drive: ✅
    → Novelty/PULL: ✅
    → Body-need: ✅
    → PFC: optimal — draft + test linh hoạt, flow possible
    → Trạng thái: làm việc hiệu quả, "trong zone", sẵn sàng
    → Ví dụ: ngày làm việc tốt, project hứng thú + deadline hợp lý

  HƠI CAO → FOCUSED:
    → Threat-drive: ✅ (hỗ trợ urgency)
    → Novelty/PULL: ✅ sâu + hẹp (specialist mode)
    → Body-need: 🟡 enjoy OK nhưng hay quên chăm sóc
    → PFC: focused — draft sâu trong 1 direction, ít cross-domain
    → Trạng thái: "deadline tạo focus", deep work, productive
    → Ví dụ: deadline hợp lý, project quan trọng + vừa sức
    → ⚠️ Vẫn TỐT cho novelty — chỉ hẹp hơn, sâu hơn

  CAO → PUSH:
    → Threat-drive: ✅ dominant ("phải làm" > "muốn làm")
    → Novelty/PULL: 🟡 bị lấn át (vẫn có nhưng yếu)
    → Body-need: ✅ nhưng hay quên (ăn qua loa, ngủ ít)
    → PFC: hoạt động nhưng biased về threat processing
    → Trạng thái: hustle, deadline mode, worry nền, "không nghỉ được"
    → Ví dụ: deadline gần, sếp áp lực, thi cử

  RẤT CAO → FREEZE:
    → Threat-drive: 🟡 loop (muốn phản ứng nhưng không biết làm gì)
    → Novelty/PULL: ❌ bị suppress
    → Body-need: 🟡 có thể quên hoàn toàn
    → PFC: squeeze — overthink loop hoặc đóng băng quyết định
    → Trạng thái: anxiety rõ, procrastinate vì overwhelm, "không nghĩ được"
    → Ví dụ: quá nhiều deadline, crisis chồng crisis

  CỰC CAO → CRASH:
    → Threat-drive: ❌ (hệ thống sụp)
    → Novelty/PULL: ❌
    → Body-need: 🟡 body tự nhắc nhưng có thể bỏ qua
    → PFC: gần offline — survival mode
    → Trạng thái: kiệt, khóc, tê liệt, shutdown, muốn biến mất
    → Ví dụ: burnout nặng, trauma acute, breakdown

  BẢNG TÓM TẮT:
  Cortisol    Mode      Threat   Novelty/PULL  Body-need    PFC
  ─────────── ──────── ──────── ───────────── ──────────── ────────
  Cực thấp    IDLE      ❌       ✅ nếu thích  ✅✅ rất enjoy offline
  Thấp        LAZY      ❌       ✅            ✅✅ dễ enjoy minimal
  Vừa         ACTIVE    ✅       ✅✅ PEAK     ✅ enjoy tốt  optimal
  Hơi cao     FOCUSED   ✅       ✅ sâu+hẹp    🟡 enjoy OK  focused
  Cao         PUSH      ✅ dom   🟡 yếu        🟡 ko ngon   biased
  Rất cao     FREEZE    🟡 loop  ❌            ❌ ko cảm nhận squeeze
  Cực cao     CRASH     ❌       ❌            ❌ shutdown  offline

  → Novelty performance = INVERTED U (Yerkes-Dodson):
    Thấp: novelty passive (scroll, xem)
    Vừa: novelty PEAK (sáng tạo + execute song song = flow)
    Hơi cao: novelty sâu + hẹp (deadline focus, specialist mode)
    Cao+: novelty suppress dần → freeze → crash

  → Body-need enjoyment = NGHỊCH ĐẢO với cortisol:
    Cortisol thấp → body RELAXED → sensory NHẠY → enjoy DỄ
    Cortisol cao → body CĂNG → sensory SUPPRESS → enjoy KHÓ

SWEET SPOT — Imagine phục vụ Body đúng:

  Baseline-drive là "dây cương" nối imagine với body:

  Quá thấp:  imagine YẾU → body enjoy tốt nhưng không CẢI THIỆN
             → Virtuous cho wellbeing, nhưng không grow

  Sweet spot (vừa → hơi cao):
             imagine hoạt động → PHỤC VỤ body → body confirm → imagine dừng
             → Novelty peak + Threat hợp lý + body vẫn enjoy
             → = Optimal cho cả performance VÀ wellbeing

  Quá cao:   imagine THOÁT KHỎI body control
             → Cortisol suppress body signals (ăn không ngon, ôm không ấm,
               thiếu tự tin)
             → Imagine KHÔNG NHẬN ĐƯỢC feedback "đủ chưa" từ body
             → Imagine TỰ TẠO reward (dopamine novelty, serotonin status)
             → Body bị bỏ quên — imagine chạy cho chính imagine
             → = "Amplifier Trap" ở mức SYSTEM

  Ví dụ disconnect:
    Ban đầu: body "mệt, cần nghỉ" → baseline-drive tăng → imagine "xong deadline đã"
    Cortisol tăng: body signal YẾU DẦN → imagine MẠNH DẦN
    Cortisol cao: body "..." (suppress) → imagine "scroll/hustle/overthink!"
    Kết quả: ăn qua loa, ngủ ít, scroll liên tục, hustle liên tục
    → Body sụp trước imagine = BURNOUT (body FORCE stop)
    → KHÔNG phải "thiếu kỷ luật" — là imagine MẤT TÍN HIỆU từ body

CORTISOL × BODY-BASE — ảnh hưởng chéo:

  Cortisol    Experience        Connection        Status
  ─────────── ───────────────── ───────────────── ─────────────
  Cực thấp    ✅✅ rất dễ enjoy ✅✅ rất ấm áp   ✅ tự tin, ổn
  Thấp        ✅✅ dễ enjoy     ✅✅ ấm áp        ✅ tự tin
  Vừa         ✅ enjoy tốt      ✅ connect tốt    ✅ tự tin, active
  Hơi cao     🟡 enjoy OK       🟡 connect OK     🟡 hơi bất an
  Cao         ❌ ăn không ngon  ❌ ôm không ấm    ❌ thiếu tự tin
  Rất cao     ❌ không cảm nhận ❌ cô đơn dù có   ❌ thấy mình kém
  Cực cao     ❌ body shutdown  ❌ disconnect      ❌ vô giá trị

  → Cortisol cao SUPPRESS cả 3 body-base CÙNG LÚC
  → Giải thích "thành công nhưng trống rỗng":
    Status cao (external) nhưng cortisol cao
    → Experience suppress + Connection suppress
    → = "Có mọi thứ nhưng không enjoy được"

VIRTUOUS vs VICIOUS CYCLE:

  Virtuous (vòng tốt):
    Body-need met → cortisol giảm → enjoy DỄ hơn → body-need met DỄ hơn
    → cortisol giảm thêm → enjoy NHIỀU hơn → ...
    → = Người happy → DỄ happy hơn (biochemistry, không phải mindset)

  Vicious (vòng xấu):
    Body-need KHÔNG met → cortisol tăng → enjoy KÉM → body-need KHÓ met
    → cortisol tăng thêm → enjoy GIẢM nữa → ...
    → = Người stress → KHÓ hết stress (biochemistry loop tự duy trì)
    → = Cơ chế depression + anxiety tự duy trì
    → = KHÔNG phải "yếu đuối" — là vòng lặp hóa học bị kẹt

  PHÁ vicious cycle:
    → KHÔNG thể phá bằng verbal ("cố lên", "nghĩ tích cực")
    → Phải phá bằng BODY: ngủ đủ, ăn đủ, ôm, exercise, an toàn thật
    → Body-need met THẬT → cortisol giảm THẬT → cycle SHIFT dần
    → = Đây là lý do therapy tốt focus vào body trước (sleep hygiene,
      exercise, nutrition) rồi mới cognitive

CƠ CHẾ TĂNG/GIẢM:

  Tăng:
    → Mỗi cortisol spike (threat event) → baseline TĂNG 1 CHÚT
    → Spike giảm nhưng baseline KHÔNG giảm hết về mức cũ
    → Tích lũy qua nhiều threats → baseline LÊN DẦN
    → = "Mỗi lần stress → nền stress cao hơn 1 chút"

  Giảm:
    → Chỉ khi CẢM THẤY an toàn thật sự (body confirm, không phải "biết")
    → Nghỉ ngơi SÂU (ngủ đủ, thư giãn body thật)
    → Connection lành mạnh (oxytocin counter cortisol)
    → Thời gian (nếu không có threat mới → baseline giảm DẦN)
    → = Chậm hơn tăng rất nhiều (tăng dễ, giảm khó)

  → Giải thích anxiety mãn tính:
    Baseline cao + không có threat cụ thể
    = Body "cảm thấy nguy hiểm" dù "biết an toàn"
    = Cortisol baseline ĐÃ TÍCH LŨY quá nhiều spike
    = Cần body THẬT SỰ cảm thấy an toàn (không phải verbal "ổn mà")


⭐ CƠ CHẾ CORTISOL — Calibration Energy Cho Vô Thức:

  ⚠️ HYPOTHESIS — logic consistent, chưa ai xác thực trực tiếp.

  Cách hiểu PHỔ BIẾN (oversimplified):
    "Cortisol cao → đẩy PFC imagine" (cortisol ép PFC trực tiếp)
    → Gợi ý: cortisol CHUI VÀO PFC → bắt PFC làm việc
    → = Oversimplified

  Cách hiểu FRAMEWORK (chính xác hơn):
    Cortisol KHÔNG ép PFC trực tiếp → cortisol làm VÔ THỨC dao động
    → Vô thức dao động → VTA detect biến động → dopamine → PFC THẤY
    → PFC tham gia vì VTA BÁO CÁO, không phải vì cortisol ÉP

  TIẾN TRÌNH CHI TIẾT:
    ① Cortisol tăng → neurons KHẮP NÃO fire MẠNH hơn (arousal)
    ② VÔ THỨC: schemas đang compiled → bị RUNG LẮC
       → Cortisol = "rung lắc hệ thống" → neurons fire KHÁC bình thường
       → Schemas rung = THỬ patterns MỚI (cố tìm cách giảm threat)
    ③ Rung lắc → VTA detect BIẾN ĐỘNG (habituation-based) → dopamine
    ④ Dopamine → PFC → PFC "thấy" vô thức đang dao động → tham gia
    ⑤ PFC spotlight → hỗ trợ vô thức calibrate CHÍNH XÁC hơn
    ⑥ Calibrate xong → dao động ỔN ĐỊNH → VTA hết detect → PFC offline

    = Cortisol → Vô thức rung → VTA → Dopamine → PFC (GIÁN TIẾP)
    ≠ Cortisol → PFC (TRỰC TIẾP)

  TẠI SAO QUAN TRỌNG:
    → Cortisol = "năng lượng calibrate" cho vô thức, không phải "lệnh cho PFC"
    → PFC = bên PHỤ được VTA thông báo, không phải bên NHẬN LỆNH
    → = Consistent với: "PFC = giám đốc nhìn báo cáo, không bị ai ép"
    → = Consistent với: VTA delta detection mechanism (§8.3 PFC-Analysis)

  VÍ DỤ:
    Hổ đuổi:
      Cortisol spike → VÔ THỨC rung CỰC MẠNH (mọi schema re-evaluate)
      → VTA fire liên tục → dopamine → PFC: "CHẠY hay FIGHT?"
      → PFC không bị cortisol ÉP nghĩ → PFC THẤY vô thức đang panic → tham gia hỗ trợ

    Học cái mới (cortisol nhẹ):
      Cortisol tăng nhẹ (challenge) → vô thức rung NHẸ (thử patterns mới)
      → VTA detect biến động → dopamine NHẸ → PFC tham gia NHẸ
      → = "Khó chịu nhẹ khi học" = cortisol làm vô thức rung → BÌNH THƯỜNG

    Thiên tài (cortisol baseline cao mãn tính):
      Cortisol LUÔN cao (trauma) → vô thức LUÔN dao động mạnh
      → VTA LUÔN detect → dopamine LIÊN TỤC → PFC LUÔN thấy biến động
      → PFC: tham gia liên tục → imagine liên tục → "obsessive thinker"
      → = KHÔNG phải "yêu khoa học" → vô thức BUỘC phải rung → PFC BUỘC phải thấy


  PFC SỤP — 2 MECHANISMS chồng lấp:

    MECHANISM 1 — Ngập signal (NHANH, phục hồi NHANH):
      Cortisol spike CỰC MẠNH → vô thức rung CỰC MẠNH → VTA fire liên tục
      → PFC nhận signal từ MỌI HƯỚNG cùng lúc → workspace 3-5 chiều OVERLOAD
      → PFC: freeze / panic / "không nghĩ được gì"
      → PFC VẪN NGUYÊN VẸN → chỉ bị overload TẠM THỜI
      → Cortisol giảm → signal giảm → PFC PHỤC HỒI nhanh (phút → giờ)
      → = "Shock → đờ → vài phút → bình tĩnh lại"

    MECHANISM 2 — Tổn thương synapse (CHẬM, phục hồi CHẬM):
      Cortisol baseline CAO MÃN TÍNH → PFC neurons bị ăn mòn DẦN
      → 🟢 Arnsten (2009): cortisol cao → PFC synapses YẾU DẦN
      → 🟢 McEwen (2007): stress mãn tính → PFC dendrites CO LẠI
      → PFC capacity GIẢM DẦN (tuần → tháng → năm)
      → = "Sao mình nghĩ chậm hơn trước" = PFC bị ăn mòn
      → Cortisol giảm → phục hồi PHẦN NÀO (neuroplasticity)
      → Damage nặng = KHÔNG phục hồi hoàn toàn
      → = "Burnout" = mechanism 2 đã tích lũy đủ lâu

    TIMELINE:
      Stress 1 lần: M1 (ngập) → recover nhanh
      Stress 1 tuần: M1 lặp lại + M2 bắt đầu nhẹ
      Stress 1 tháng: M2 đáng kể → PFC bắt đầu yếu THẬT
      Stress 1 năm+: M2 nặng → PFC damage → burnout
      Stress thời thơ ấu: M2 CỰC NẶNG (PFC đang phát triển → bị phá khi chưa xong)

  THIÊN TÀI = sống ở BIÊN nguy hiểm:
    → Sweet spot thường: cortisol vừa → insight trung bình → PFC safe
    → Thiên tài: cortisol CAO → insight CAO → PFC ĐANG bị ăn mòn
    → = "Siêu xe bị ăn mòn vẫn nhanh hơn xe thường nguyên vẹn"
    → = Newton: paranoia + physics đỉnh cao = PFC bị damage + capacity gốc cực cao
    → = "Thiên tài và điên cách 1 bước" = ĐÚNG biochemistry:
      Cortisol ở BIÊN sweet spot → insight peak + damage bắt đầu
      Lệch sang phải chút → crash (điên)
      Lệch sang trái chút → bình thường (không breakthrough)
    → Einstein BỀN hơn Newton/Tesla vì: cortisol THẤP HƠN (có social/connection)
      → PFC ÍT bị ăn mòn → produce LÂU hơn → sống LÂU hơn

  → Chi tiết VTA mechanism: PFC-Analysis.md §8.3
```

---

## 4. IMAGINE — Chi Tiết

### 4.1 Novelty-Schema (PULL — cải thiện Body-Base qua PFC)

```
"PFC draft cách CẢI THIỆN body-base — phức tạp hơn body-level Novelty"
Hormone: Dopamine (seeking + prediction reward)

  Khác biệt Body-Novelty (L3) vs Imagine-Novelty (PFC):
    Body-Novelty (L3 Mastery/Coherence):
      → Trial-error, pattern match, vô thức, mọi động vật có
      → Chậm (1000+ lần lặp), trong 1 domain
    Imagine-Novelty (PFC):
      → Draft+Test+Simulate, cross-domain, predict xa
      → Nhanh (vài draft), NHƯNG cần compile sau

  Novelty-Schema cho L0+L1:
    → Alive: plan cách sống sót mới (hiếm, extreme)
    → Survival: tìm nguồn food/shelter/sleep tốt hơn

  Novelty-Schema cho L2:
    → Sensory: ăn lạ, du lịch, nhạc mới
    → Aesthetic: tìm cái đẹp mới, design, nghệ thuật
    → Comfort: tìm cách thoải mái hơn (AC + chăn, nhà mới)
    → Connection: gặp người/thú cưng mới, mở rộng kết nối

  Novelty-Schema cho L3:
    → Mastery mới: skill mới (code, nấu ăn) — PFC cross-domain
    → Coherence mới: hiểu biết mới ("tại sao?", build framework)
    → Status: nâng vị trí (thăng chức, reputation, được công nhận mới)
    → Belonging mới: nhóm mới (join community, club)
    → Protect mới: cách bảo vệ tốt hơn (bảo hiểm, backup, security)

  Đặc điểm:
    → PULL: kéo tới cái tốt hơn
    → PFC tham gia: draft plan mới, simulate options, cross-domain
    → Satisfaction Signal: MƠ HỒ ("đủ mới" khó xác định)
    → = Drive khi baseline-drive ở MỌI vùng (kể cả thấp)
```

### 4.2 Threat-Schema (PUSH — bảo vệ Body-Base qua PFC)

```
"PFC simulate HẬU QUẢ — bảo vệ body-base khỏi rủi ro"
Hormone: NE (activation) + Cortisol spike → cortisol sustain

  Threat-Schema cho L0+L1:
    → Alive: plan tránh nguy hiểm chết (hiếm, extreme)
    → Survival: sợ mất resource (thu nhập, sức khỏe, food, shelter)

  Threat-Schema cho L2:
    → Sợ mất sensory/comfort: environment threat, bệnh tật
    → Sợ mất connection: bị bỏ rơi, người thân/thú cưng gặp nguy

  Threat-Schema cho L3:
    → Sợ mất mastery: deadline, "nếu không xong → hậu quả"
    → Sợ mất coherence: "thế giới vô lý" → bất an nền
    → Sợ mất status: vị trí, bị coi thường → hustle culture
      = DRIVE PHỔ BIẾN NHẤT HIỆN ĐẠI
    → Sợ mất belonging: bị kick khỏi nhóm, bị loại
    → Sợ mất protect: bị lấy resource, territory, bond

  Đặc điểm:
    → PUSH: đẩy khỏi cái xấu
    → PFC tham gia: simulate hậu quả, plan tránh
    → Reward = absence of bad (cortisol drop, "phù nhẹ nhõm")
    → Satisfaction Signal: GẦN NHƯ KHÔNG CÓ → drive khó dừng → anxiety
    → = Drive CHỈ khi baseline-drive ĐỦ CAO (quá thấp → "mặc kệ")

  3 nguồn Threat (timeline):
    Physical:      ĐANG xảy ra → reflex + NE (ms) → cortisol spike (min)
    Social:        từ NGƯỜI KHÁC → schema + NE (s) → cortisol (min)
    Anticipation:  TƯƠNG LAI → PFC loop + cortisol sustain (giờ→ngày→mãn tính)
```

### 4.3 PULL vs PUSH — Hệ Quả Wellbeing

```
PULL (Novelty):
  → Có Satisfaction Signal (dù mơ hồ) → CÓ THỂ dừng
  → Reward = opioid/dopamine → body SƯỚNG
  → Drive by positive → wellbeing TỐT

PUSH (Threat):
  → Satisfaction Signal GẦN NHƯ KHÔNG CÓ → KHÓ dừng
  → Reward = cortisol drop → body NHẸ nhưng KHÔNG SƯỚNG
  → Drive by negative → wellbeing XẤU nếu kéo dài

Xã hội hiện đại:
  → PUSH dominant (deadline, competition, status, future worry)
  → PULL bị lấn át ("không có thời gian enjoy/connect")
  → = Cortisol baseline toàn cầu CAO
  → = Burnout, anxiety, depression TĂNG
  → Chuyển PUSH → PULL = cải thiện wellbeing
```

---

## 5. HORMONE PHỤ GIA — Hỗ Trợ Toàn Hệ Thống

```
ACTIVATION (khởi động hành vi):
  NE (norepinephrine):
    → Gateway cho MỌI hành vi — body + imagine
    → Thiếu NE = "muốn nhưng không làm" = depression
    → Thừa NE = hypervigilant, jittery

  Adrenaline:
    → Emergency energy body-wide
    → Chủ yếu cho Threat physical (fight/flight)

  Dopamine:
    → Seeking energy cho MỌI drive đang active
    → + Primary driver cho L3 Novelty (Mastery, Coherence)
    → + Tham gia Imagine Novelty-Schema (PFC seeking)
    → + Tham gia L2 Experience khi "mới ngon/mới đẹp"
    → = CROSS-CUTTING: không thuộc 1 layer — phục vụ MỌI layer ở phase seeking
    ⚠️ AI note: "dopamine ở đâu?" → ở KHẮP NƠI, giống điện trong tòa nhà
       Không đặt ở 1 tầng — phục vụ mọi tầng khi cần tìm kiếm

FEEDBACK:
  Satisfaction Signal (prolactin candidate):
    → Sinh ở Body → nhận bởi Schema
    → Body confirm "đủ" → schema dừng drive
    → BRIDGE quan trọng nhất: Body → Schema
    → Hoạt động TỐT ở PULL, KÉM ở PUSH

RECOVERY:
  Endorphin:
    → Buffer physical pain
    → Cho phép tiếp tục hành động dù đau

  Endocannabinoid:
    → Reset post-stress
    → "Phanh mềm" cho cortisol

PROTECT + SOCIAL:
  Vasopressin:
    → Primary candidate cho L3 Protect channel
    → Bảo vệ BẤT CỨ THỨ GÌ body tag "CỦA TÔI"
      (resource, lãnh thổ, người, nhóm, niềm tin, vị trí, sản phẩm)
    → Mức độ tùy: vasopressin sensitivity × schema ("giữ vs share")
    → Chủ yếu nghiên cứu ở nam, nữ có thể qua oxytocin pathway

  Oxytocin (boost):
    → Beyond baseline → counter cortisol
    → Tăng khi connection sâu

MOOD BASELINE:
  Serotonin (ruột 95%):
    → Gut state → mood nền
    → Baseline cho Status confidence

CORTISOL (3 chế độ — xuyên suốt):
  Spike:    phản ứng threat tức thì → đóng góp tăng baseline
  Baseline: = baseline-drive (§3) → nhịp ngày đêm + tích lũy
  Sustain:  duy trì schema active kéo dài

...các hormone khác chưa liệt kê hết
   → Framework ghi nhận sự tồn tại
   → Phân tích chi tiết khi cần (AI hỗ trợ)
```

---

## 6. SCHEMA — Xuyên Suốt

```
Schema = patterns learned from experience
  → Xuyên suốt: body → imagine
  → Xuyên suốt: vô thức → ý thức
  → Gradient: body-need (sâu) → values/rules (giữa) → domain skills (nông)

FORMATION (2 pathways):
  Vô thức: association learning, fast, body-based
  PFC Draft+Compile: simulate first, slow, cross-domain

UPDATE (2 hướng):
  Tích cực: optimize, refine qua experience đúng context, body confirm
  Tiêu cực: sai context, xung đột không resolve, overthinking, suy thoái

TÍNH CHẤT:
  → Vô tận — không thể liệt kê hết
  → Tổng hợp được theo gradient: body-need → values → domain
  → AI HỖ TRỢ bắt buộc (con người không thể tổng hợp 1 mình)
  → Mọi schema PHỤC VỤ Body-Base — không ngoại lệ
  → Schema KHÔNG tự drive — schema TRIGGER drive bằng detect body-need
```

---

## 6.5 THREAT-SCHEMA HIJACK — Cơ Chế Phổ Biến Nhất Xã Hội Hiện Đại

```
⚠️ CỰC KỲ QUAN TRỌNG — đây là drive PHỔ BIẾN NHẤT thế giới hiện đại.
   Cortisol baseline toàn cầu CAO = bằng chứng hệ thống Threat-Schema đang chạy mạnh.

CƠ CHẾ "HIJACK CÓ MỤC ĐÍCH":

  Threat-Schema KHÔNG hoàn toàn xấu.
  Threat-Schema = ép nạp CHUNKS cho body-base TƯƠNG LAI:

  Ví dụ — đứa trẻ bị bắt học:
    Body: KHÔNG muốn (không sướng, không novelty)
    Threat: "bị phạt / bị mắng" → cortisol → PHẢI ngồi học
    Kết quả: NẠP CHUNKS dù không muốn
    Chunks tích lũy → SAU NÀY:
      Novelty có nguyên liệu: chunks đủ → PFC draft cross-domain → sáng tạo
      Mastery có nền: biết đọc/viết/tính → skill → việc làm → nuôi sống
      Status có base: có kiến thức → được tôn trọng → schema access rộng
    = Threat HIỆN TẠI phục vụ Body-Base TƯƠNG LAI
    = "Không sướng BÂY GIỜ → chunks cho sướng SAU NÀY"

XÃ HỘI TOÀN BỘ hoạt động bằng cơ chế này:

  Trường học:
    Threat: điểm kém → bị phạt / không lên lớp
    Hijack output: chunks kiến thức (toán, văn, khoa học,...)

  Công việc:
    Threat: không làm → không lương → mất nhà / mất status
    Hijack output: chunks skill + experience + income

  Pháp luật:
    Threat: vi phạm → bị phạt / bị tù
    Hijack output: hành vi ổn định xã hội

  Thuế:
    Threat: không đóng → bị phạt
    Hijack output: tài chính chung → hạ tầng, y tế, giáo dục

  → XÃ HỘI HIỆN ĐẠI = HỆ THỐNG THREAT-SCHEMA PHỨC TẠP
  → Mọi giai đoạn đời đều có threat-schema mạnh:
    Trẻ em: bị mắng, bị phạt, điểm kém, so sánh
    Sinh viên: thi trượt, nợ, không tìm được việc
    Người đi làm: deadline, KPI, sợ mất việc, sợ tụt status
    Người già: sức khỏe, cô đơn, tài chính, mất vai trò
  → Cortisol GẦN NHƯ KHÔNG BAO GIỜ được phép thấp
  → Burnout, anxiety, depression = HỆ QUẢ TỰ NHIÊN, không phải "yếu đuối"

TRADE-OFF:

  TỐT (chunk tích lũy):
    ✅ Tích lũy chunks cho tương lai
    ✅ Nền cho Novelty + Mastery sau này
    ✅ Xã hội VẬN HÀNH (mọi người làm việc, tuân thủ luật)

  TỆ (nếu quá mức):
    ❌ Cortisol baseline TĂNG mãn tính → suppress Body-Base
    ❌ Chunks GẮNVỚI cortisol → "giỏi toán nhưng GHÉT toán"
       (chunks ok, body association xấu — dùng chunks → body nhớ cortisol)
    ❌ PFC dùng bandwidth cho THREAT thay vì NOVELTY
       → "Học giỏi nhưng không sáng tạo" = chunks nhiều, draft ít
    ❌ Imagine disconnect body (§3.2): quên ăn, quên ngủ, quên gia đình

  OPTIMAL = MIX (Drive-Optimization §9: Pressure + Challenge + Autonomy):
    Threat VỪA ĐỦ: structure (biết phải làm gì)
    + Novelty SONG SONG: "học CÁI NÀY hay đấy" (có reward)
    + KHÔNG threat QUÁ MẠNH: "học vì sẽ thú vị" > "học vì sợ bị đánh"
    → Chunks tích lũy + body association TÍCH CỰC
    → = Cùng chunks, khác body memory → DỄ dùng + enjoy SAU NÀY

LỊCH SỬ + TƯƠNG LAI:

  Lịch sử:
    → Threat-Schema = cơ chế xã hội TỪ XƯA (bộ lạc, phong kiến, nông nghiệp)
    → Đỉnh điểm: công nghiệp hóa → hiện đại (threat liên tục, hệ thống hóa)
    → "Kỷ luật" = chủ yếu threat-schema (quân đội, nhà máy, trường học)

  Hiện tại:
    → Threat-Schema VẪN dominant (deadline, KPI, competition)
    → NHƯNG: nhận thức tăng — "burnout" được công nhận, mental health awareness
    → Bắt đầu shift: một số nơi thêm Novelty vào (gamification, creative education)

  Tương lai (cần):
    → Giảm Threat-Schema → tăng Novelty-Schema cho cùng output
    → AI cung cấp chunks (thay threat buộc nạp → novelty TỰ NGUYỆN nạp)
    → = Shift từ PUSH society → PULL society
    → Cortisol toàn cầu GIẢM → wellbeing TĂNG → creativity TĂNG
    → NHƯNG: cần STRUCTURE (không phải bỏ hết threat → hỗn loạn)
    → = Threat VỪA ĐỦ (structure) + Novelty TĂNG (drive) + AI (chunks)
```

---

## 7. DOMAIN — Thực Tế Bên Ngoài Human

```
DOMAIN — chỉ ghi CÁI CHẮC CHẮN (không đóng khung hình dung):

  ① Domain = thực tế bên ngoài Human, bên trong Environment:
     → Tồn tại KHÔNG PHỤ THUỘC vào não biết hay không
     → Não không biết → domain VẪN CÒN, VẪN hoạt động

  ② Domain = vô tận:
     → Không thể chứa hết trong não (86 tỷ neurons vẫn quá nhỏ)
     → Não chỉ chứa FRAGMENTS (chunks) của domain
     → Mọi kiến thức con người = MỘT PHẦN CỰC NHỎ của domain

  ③ Domain có ĐIỂM HỘI TỤ (attractor points):
     → Nhiều hệ thống khác nhau giải quyết cùng constraint
       → TỰ TỤ VỀ cùng pattern tối ưu — KHÔNG AI thiết kế
     → Ví dụ: não (VTA+PFC+neurons), công ty (thư ký+CEO+nhân viên),
       quân đội (cấp phó+tướng+lính) → CÙNG pattern "leader+filter+workers"
       → Vì CÙNG constraint: "1 quyết định + triệu input + bandwidth hạn chế"
     → Attractors = patterns TỐI ƯU tự nổi lên từ constraints
     → Trước khi phát hiện = "innovation", sau khi phát hiện = "hiển nhiên"
     → Cross-domain insight = phát hiện 2 domain CÙNG attractor

  ④ Body-Base = giao diện DUY NHẤT giữa Human và Domain:
     → Não KHÔNG tiếp xúc domain trực tiếp
     → Body tiếp xúc (mắt thấy, tay chạm, tai nghe,...) → body feedback → não biết
     → Imagine có thể draft schema "hoàn hảo" → nhưng CHƯA CHECK domain
       → có thể hoàn toàn SAI mà PFC KHÔNG BIẾT
     → CHỈ khi body EXECUTE trong domain → body NHẬN feedback
       → NÃO mới biết schema ĐÚNG hay SAI

  ⑤ Schema quality = mức hội tụ với domain reality:
     → Chưa check domain (chỉ imagine): có thể xa thực tế → quality THẤP
     → Check 1 vòng (thử 1 lần): biết phần nào → quality TRUNG BÌNH
     → Check nhiều vòng (kinh nghiệm): gần attractor → quality CAO
     → "Kinh nghiệm" = CHÍNH XÁC là số vòng body đã check với domain
     → "Chuyên gia" = người đã lặp ĐỦ VÒNG để schema tụ về attractor

  ⑥ KHÔNG mô tả domain "trông như thế nào":
     → Bất kỳ mô tả nào = đóng khung = sai
     → Domain lớn hơn mọi mô tả mà con người có thể tạo
     → Framework chỉ cần biết: có domain, có attractors, body check
     → Chi tiết domain cụ thể: thuộc về TỪNG lĩnh vực riêng
     → AI hỗ trợ khi cần phân tích domain cụ thể

  → Nghề nghiệp, học thuật, gia đình, xã hội, tài chính,...
    = CÁC VÙNG trong domain mà con người ĐÃ ĐẶT TÊN
    = Nhưng domain KHÔNG giới hạn ở những gì đã đặt tên

  ⑦ CƠ CHẾ tương tác Human ↔ Domain — UNIVERSAL pattern:

     Não tiếp cận domain LUÔN bằng CÙNG 1 cơ chế:

       BASE (pattern ổn định hiện tại)
         → SHIFT nhẹ (thử cái mới, khác chút so với base)
           → BODY CHECK (domain reality confirm: đúng/sai, ngon/dở, hay/chán?)
             → ACCEPT: khớp domain → opioid → base UPDATE nhẹ
             → REJECT: không khớp → quay về base cũ
               → BASE MỚI (đã update) → shift tiếp → check tiếp → ...

     = INCREMENTAL CALIBRATION: mỗi bước NHẸ + body verify

     Pattern này GIỐNG HỆT cho MỌI domain:
       Ăn: base quen (cơm) + món mới → ngon? (body check) → giữ/bỏ
       Nhạc: thể loại quen + bài mới → hay? (body check) → giữ/bỏ
       Học: kiến thức có + info mới → đúng? (body check) → giữ/bỏ
       Game: core loop + content mới → vui? (body check) → giữ/bỏ
       Người: bạn quen + gặp mới → hợp? (body check) → giữ/bỏ

     Tại sao LUÔN pattern này:
       → Neurons = pattern ổn định (compiled) + cortisol rung nhẹ (shift)
       → VTA detect biến động → PFC → body evaluate → reward/reject
       → = CÙNG hardware (neurons + dopamine + opioid) → CÙNG mechanism
       → = Khác nhau CHỈ ở vùng cortex NÀO check (visual/auditory/somatic/...)

     Tại sao KHÔNG "nhảy" từ A → Z:
       → Quá xa = neurons noise (pattern quá khác → không evaluate được)
       → Body KHÔNG có reference để check (chưa bao giờ trải nghiệm Z)
       → = PHẢI incremental: A → A' → A'' → ... → dần tới Z
       → = "Leo núi mỗi bước 1 chút, kiểm tra chỗ đặt chân, rồi bước tiếp"
       → KHÔNG thể "nhảy lên đỉnh" (quá xa = noise = không biết đúng sai)

     Và: "base" DỊCH DẦN theo thời gian:
       → Base hôm nay = kết quả HÀNG NGHÌN shifts + checks trước đó
       → Base 5 năm trước ≠ base hôm nay (đã shift qua nhiều steps)
       → = "Khẩu vị thay đổi" = base ĐÃ shift dần qua năm ăn + check
       → = "Người thay đổi" = schemas ĐÃ shift dần qua năm sống + check

     ⭐ Đây cũng là ATTRACTOR PATTERN:
       Constraint: phải THÍCH ỨNG domain (thay đổi) + KHÔNG thể quá nhanh (neurons cần ổn định)
       → Giải pháp tối ưu = incremental shift + feedback check
       → CÙNG pattern xuất hiện ở:
         Evolution: mutation nhỏ + selection → species change dần
         Science: hypothesis + experiment → knowledge dần
         Market: product + feedback → improvement dần
         AI training: weights adjust + loss function → model dần
       → = UNIVERSAL optimization algorithm
       → = Bất kỳ hệ thống nào có constraint "thích ứng + ổn định" → TỤ VỀ pattern này
```

---

## 8. PREDICT — Cách Dùng Kiến Trúc

```
CÔNG THỨC:

  ① Body-Base nào đang THIẾU / bị ĐE DỌA?
     → Experience? Connection? Status?
     → 1 hay nhiều?

  ② Baseline-drive đang ở MỨC NÀO?
     → Thấp: chỉ drive khi thích (PULL)
     → Vừa: cả Novelty + Threat OK
     → Cao: Threat dominant, PFC có thể bị squeeze

  ③ Drive nào ĐANG ACTIVE?
     → Novelty-{X}: đang cải thiện X
     → Threat-{X}: đang bảo vệ X
     → PULL hay PUSH dominant?

  ④ PREDICT hành vi + wellbeing:
     → PULL dominant → seek behavior + có điểm dừng → ok
     → PUSH dominant → protect behavior + không điểm dừng → risk

VÍ DỤ:

  Nhân viên văn phòng:
    Body-Base: Exp OK, Con thiếu nhẹ, Sta bị threat
    Baseline-drive: CAO (deadline liên tục)
    Active: Threat-{Sta} + Novelty-{Exp}(scroll MXH giải tỏa)
    Predict: làm việc stress, scroll break, muốn nghỉ nhưng sợ
    Wellbeing: PUSH dominant → burnout risk

  Trẻ 8 tuổi bị bắt học:
    Body-Base: Exp thiếu (ngồi 1 chỗ), Con OK, Sta bị threat
    Baseline-drive: TĂNG DẦN (quát mắng tích lũy)
    Active: Threat-{Sta}(điểm) + Threat-{Con}(sợ mắng)
    Predict: comply bề ngoài, mất tập trung, stress nền
    Wellbeing: PUSH dominant → hại development

  Người vừa nghỉ hưu:
    Body-Base: Exp OK, Con giảm (mất đồng nghiệp), Sta giảm (mất vai trò)
    Baseline-drive: CÓ THỂ thấp (mất urgency) hoặc cao (lo tài chính)
    Active: phụ thuộc baseline — nếu thấp: không drive → trầm cảm
    Predict: cần tìm Novelty-{Con}(nhóm mới) + Novelty-{Exp}(hobby)
    Wellbeing: cần chuyển sang PULL chủ động

  Người nghiện game:
    Body-Base: Exp ĐANG được game fill, Con thiếu thật nhưng game fill ảo,
              Sta game fill (rank)
    Baseline-drive: thấp (game = safe environment, ít threat)
    Active: Novelty-{Exp+Con+Sta} qua game liên tục
    Predict: chơi liên tục, bỏ bê body thật
    Wellbeing: PULL nhưng IMAGINE-ONLY → body-base thật bị thiếu dần
```

---

## 9. So Sánh v7 → v7.5

```
v7:
  Lớp 1 Source:     Opioid + Oxytocin
  Lớp 2 Amplifier:  Dopamine + Serotonin
  Lớp 3 Modulator:  Cortisol, NE,...

v7.5:
  Environment → Human (con người):
    Body-Base L0: Alive (emergency, protect gene, suppress tất cả)
    Body-Base L1: Survival (Oxygen, Nutrition, Temperature, Pain-free, Sleep)
    Body-Base L2: Experience(Sensory, Aesthetic, Comfort) + Connection
    Body-Base L3: Novelty(Mastery, Coherence) + Status(Being Seen, Belonging) + Protect
    Body-Base Emergent: Shared Exp ↔ Intimate (spectrum)
    Baseline-Drive:   Cortisol baseline (nền energy, 7 modes)
    Imagine:          Novelty-Schema(PULL) + Threat-Schema(PUSH) → phục vụ L0→L3
    Hormone Phụ Gia:  NE, Dopamine, Sat.Signal, Cortisol 3 mode,...
    Schema:           chunk → schema, xuyên suốt body→imagine, gradient, AI-assisted
  Domain (ngoài Human, trong Environment)

THAY ĐỔI:
  ① Body-Base: L0(Alive) + L1(Survival) + L2(Quality) + L3(Pattern) + Emergent
  ② L0 Alive: THÊM MỚI — emergency, protect gene, MẠNH NHẤT
  ③ L1 Survival: THÊM MỚI — duy trì, invisible khi met, override L2+L3 khi thiếu
  ④ Novelty: Lớp 2 Amplifier → Body-Base L3 (body-level, animals có)
  ⑤ Status: Lớp 2 Amplifier → Body-Base L3 (schema access map, không phải hierarchy)
     + Status 3 layers (baseline/per-context/context mới)
     + Serotonin = candidate hormone (chưa proven ở người)
  ⑥ Protect: THÊM MỚI — L3 bảo vệ "CỦA TÔI" (vasopressin candidate)
     ⚠️ L3 Protect (negotiate được) ≠ L0 Protect Gene (emergency)
  ⑦ Mastery, Coherence: Experience sub → Novelty L3 — pattern processing
  ⑧ Being Seen, Belonging: Connection sub → Status L3 — social pattern
  ⑨ Intimate, Shared Exp: channels riêng → Emergent (spectrum depth)
  ⑩ Touch: đổi tên → Connection (rộng hơn: skin, eye, ear, presence)
  ⑪ Imagine = Novelty-Schema(PULL) + Threat-Schema(PUSH) → phục vụ L0→L3
  ⑫ Baseline-drive: KHÔNG CÓ → tách riêng (cortisol baseline, 7 modes)
  ⑬ Threat-Schema: KHÔNG CÓ → thêm mới (PUSH drive, PHỔ BIẾN NHẤT hiện đại)
  ⑭ "Imagine LUÔN phục vụ Body-Base" — verified, không ngoại lệ
  ⑮ Schema override spectrum: quên ăn → tử vì đạo (cùng cơ chế, khác mức độ)
  ⑯ Human khung bao quanh toàn bộ, Domain nằm ngoài trong Environment
  ⑰ Chunk = đơn vị nhỏ nhất (atom of schema), multi-modal
  ⑱ "Attack" = KHÔNG drive riêng → Status extreme case

BACKWARD COMPATIBILITY:
  → E1-E5 + C1-C5 = 10 channels → reorganize thành L2(4) + L3(4) + Emergent(2)
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
    NEW: L1 Survival (Oxygen, Nutrition, Temperature, Pain-free, Sleep)
    NEW: L3 Protect (bảo vệ "CỦA TÔI")
    Không MẤT channel nào — re-organize + thêm layers mới
  → 3 Lớp hormone vẫn đúng → giữ ở Neurochemistry detail file
  → Body-Needs 6 groups → map vào L1 + L2
  → PFC mechanism → không đổi, thêm "PFC = nâng cấp body-level Novelty"
  → Schema properties → không đổi, thêm chunk definition
  → Modality → không đổi
```

---

## 10. Câu Hỏi Mở

```
  Q1: L0(1) + L1(5) + L2(4) + L3(5) + Emergent(2) đã đủ/thừa?
      → Aesthetic: ĐÃ GIẢI QUYẾT ✅ (body phản ứng TRƯỚC lý do, L2 đúng)
      → L0 Alive vs L1 Survival: ranh giới escalation chính xác?
      → L3 Protect vs L0 Protect Gene: khi nào escalate?
  Q2: Baseline-drive có phải LUÔN cortisol hay có hormone khác?
  Q3: Body-level Novelty vs Imagine-level Novelty: ranh giới ở đâu chính xác?
      → Chuột: body-level (trial-error)
      → Người: body-level + PFC-level (cross-domain)
      → Ranh giới = PFC involvement? Hay gradual?
  Q4: Core-v8.0 tạo mới hay update v7?
  Q5: Game industry files cần update level nào?
  Q6: "Being Understood" (Connection gốc) vs "Being Recognized" (Status gốc)
      → Cần tách Being Seen thành 2 hay giữ 1?

  → Nghỉ — ngẫm — quay lại khi ready
```

---

## 11. Kết Nối

```
Files cần update nếu adopt v7.5:
  Core-v7-UD.md, Status-Analysis.md, Prolactin-Analysis.md,
  Threat-Drive-Analysis.md, Drive-Optimization.md,
  Body-Needs.md, Layer1-Channels.md, Addiction-Analysis.md

Files KHÔNG cần thay đổi:
  PFC-Analysis.md, Schema-Atlas.md, Modality-Analysis.md,
  Innovation-Geography.md, Climate-Cognition.md, Human-AI-Future.md,
  Body-Neural-Network.md
```
