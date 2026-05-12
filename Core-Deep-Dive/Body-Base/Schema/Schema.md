---
title: Schema.md v2.0 — Schema as Observation Parameter
created: 2026-03-25 (v1.0 DRAFT)
updated: 2026-04-20 (v2.0 REWRITE — observation parameter reframe per v7.8)
status: v2.0 COMPLETE
scope: |
  Schema = observation parameter, NOT architectural component.
  Schema = named chunk-network pattern = cách QUAN SÁT, không phải cách NÃO HOẠT ĐỘNG.
  File này define: schema là gì, tại sao hữu ích, properties quan sát được,
  tương tác với body-feedback/PFC/domain, và giới hạn.
previous_version: Schema/backup/ (v1.1 content redistributed)
supersedes: |
  Schema-Operations.md (DRAFT 2026-03-26) → backup (content absorbed into Chunk.md v2.0, Feeling.md v2.0)
  Schema-Example.md (DRAFT 2026-03-24) → backup (data valid, framing outdated)
parent: Core-v7.8-Draft.md §8 (observation parameters table)
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, observation parameters
  - Chunk.md v2.0 — chunk substrate (sole substrate)
  - Body-Feedback.md v1.1 — dual-pull, H10, interface loop
  - Body-Feedback-Mechanism.md v1.0 — chunk dynamics (Shift/Miss/Gap)
  - Feeling.md v2.0 — PFC observation interface
  - Cortisol-Baseline.md v2.0 — amplifier, direction gate
  - Valence-Propagation.md v1.1 — valence per-entity + chain
  - Anchor-Schema.md v1.2 — sync point, trust binding
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Schema — Observation Parameter

> **Trong phần mềm: "hàm" = đơn vị tính toán thật. "Tính năng" = cách mô tả phần mềm từ bên ngoài.**
> **Trong não: chunks = đơn vị tính toán thật. Schema = cách mô tả chunk networks từ bên ngoài.**
>
> Schema KHÔNG phải component kiến trúc.
> Schema = named chunk-network pattern — observation label.
> Hữu ích để mô tả, predict, communicate.
> Nhưng body-base KHÔNG "chạy schemas" — body-base chạy CHUNKS.
>
> File này define schema trong v7.8 cycle-based architecture.

---

## Mục lục

- §0 — TẠI SAO REFRAME
- §1 — SCHEMA LÀ GÌ TRONG V7.8
- §2 — ANALOGY PHẦN MỀM
- §3 — GIÁ TRỊ CỦA SCHEMA NHƯ OBSERVATION PARAMETER
- §4 — PROPERTIES QUAN SÁT ĐƯỢC
- §5 — SCHEMA × BODY-FEEDBACK
- §6 — SCHEMA × PFC
- §7 — SCHEMA × DOMAIN
- §8 — BODY BASELINE STATE
- §9 — CÂU HỎI MỞ
- §10 — HONEST ASSESSMENT
- §11 — CROSS-REFERENCES

---

## §0 — TẠI SAO REFRAME

### §0.1 Schema trong v1.1

```
V1.1 (2026-03-25 → 2026-04-18):
  → Schema = "PATTERN dao động neuron đã ổn định (compiled)"
  → Schema = SOFTWARE chạy trên HARDWARE (neurons)
  → Schema System = component kiến trúc (cùng cấp Drive, Layer)
  → Chunks = "gạch", Schema = "ngôi nhà"

  Vấn đề:
  ① Schema TRÔNG GIỐNG component riêng biệt → nhưng thực chất = chunks + links
  ② "Schema compiled" → gợi ý schema LÀ thứ gì đó → thực chất chunks compiled
  ③ 3 trạng thái (compiled/active/monitor) → thực chất là chunk activation states
  ④ Tương tác schema-schema → thực chất là chunk spreading activation
  → = MỌI THỨ schema "làm" = chunks làm. Schema chỉ là TÊN GỌI.
```

### §0.2 Deep drill revealed

```
63,000+ dòng drill (44+ files, 2026-03 → 2026-04) cho kết quả nhất quán:

  Chunk.md v2.0: "Não = database + 2 operators" → chunks = sole substrate
  Body-Feedback.md: "6-step interface loop" → cycle, không components
  Agent.md: "Agent = function on chunk substrate" → không category riêng
  Feeling.md v2.0: "PFC observation of body-chunk interaction" → interface
  Drive.md v1.1: "Schema = DETECTOR, drive = emergent" → observation label
  Core-v7.8-Draft.md §0.2: 9/9 files compatible với reframe

  → Schema = observation label cho chunk network patterns
  → Giống "tính năng" trong phần mềm: mô tả từ bên ngoài, không phải cấu trúc bên trong
```

### §0.3 V2.0 = gì

```
V2.0 REFRAME:
  → Schema = OBSERVATION PARAMETER (cùng nhóm: Novelty, Status, Protect,...)
  → Body-base chạy HOÀN TOÀN trên chunks
  → Schema = cách CON NGƯỜI QUAN SÁT chunk network patterns
  → Vẫn HỮU ÍCH — nhưng phải biết đây là lens, không phải reality

  KHÔNG thay đổi:
  → Properties quan sát được (depth, activation, decay, override) vẫn VALID
  → Ví dụ vẫn đúng (tình yêu lifecycle, burnout, trauma cross-contamination)
  → Chỉ thay đổi STATUS: từ "component" → "observation parameter"
```

---

## §1 — SCHEMA LÀ GÌ TRONG V7.8

### §1.1 Định nghĩa

```
⭐ SCHEMA = NAMED CHUNK-NETWORK PATTERN:

  Schema = tập hợp chunks liên kết + mục đích chung + TÊN GỌI

  Chunks [đạp phanh] + [nhìn gương] + [đánh lái] + [quan sát] +...
    + links giữa chúng
    + purpose: "di chuyển an toàn"
    = Schema mà ta GỌI LÀ "lái xe"

  Schema KHÔNG TỒN TẠI như 1 entity riêng biệt trong não.
  Schema = CÁI TÊN mà PFC (hoặc observer bên ngoài) ĐẶT CHO
  chunk network pattern quan sát được.

  CHUNK = atom (đơn vị tính toán thật, fire trong não)
  SCHEMA = molecule (tên gọi cho nhóm atoms liên kết)
  ATOM TỒN TẠI VẬT LÝ → molecule = cách ta MÔ TẢ tổ hợp atoms

  🟡 Reframe key:
  → "Schema fire" = chunks trong network đó fire
  → "Schema compiled" = chunks trong network đó đã strengthened
  → "Schema conflict" = 2 nhóm chunks fire hướng ngược nhau
  → "Schema update" = chunk links trong network re-weight
  → MỌI "schema operation" = chunk operation + observation label
```

### §1.2 Schema vs Chunk — phân biệt rõ

```
┌───────────────┬──────────────────────────────────────┐
│               │ Chunk                                 │
├───────────────┼──────────────────────────────────────┤
│ Ontology      │ TỒN TẠI VẬT LÝ (neurons wired)     │
│ Level         │ Atom — đơn vị nhỏ nhất               │
│ Fire          │ Fire THẬT trong não (measurable)      │
│ Mechanism     │ LTP, spreading activation, compile    │
│ Phân loại     │ KHÔNG THỂ phân loại hết (vô hạn)     │
│ Ví dụ         │ [đỏ], [nóng], [mẹ-mặt], [phanh-chân]│
└───────────────┴──────────────────────────────────────┘

┌───────────────┬──────────────────────────────────────┐
│               │ Schema                                │
├───────────────┼──────────────────────────────────────┤
│ Ontology      │ OBSERVATION LABEL (tên gọi pattern)  │
│ Level         │ Molecule — tên cho tổ hợp atoms       │
│ Fire          │ "Fire" = chunks trong network fire     │
│ Mechanism     │ KHÔNG có mechanism riêng              │
│ Phân loại     │ CÓ THỂ đặt tên (nhưng tên ≠ reality)│
│ Ví dụ         │ "lái xe", "sợ chó", "tình yêu"       │
└───────────────┴──────────────────────────────────────┘

⭐ TEST:
  "Bỏ khái niệm schema → mất gì?"
  → Mất: shorthand tiện lợi, cách communicate nhanh
  → KHÔNG mất: mechanism (chunks vẫn fire, link, compile y nguyên)
  → = Schema = convenience, NOT necessity
```

---

## §2 — ANALOGY PHẦN MỀM

```
⭐ "TÍNH NĂNG" TRONG PHẦN MỀM = SCHEMA TRONG NÃO:

  PHẦN MỀM:
    → "Hàm" (function) = đơn vị tính toán thật
    → Mỗi hàm có code thật, chạy trên CPU thật
    → Có thể call, có thể link, có thể reuse
    → VÔ HẠN hàm có thể tồn tại (tùy nhu cầu)
    → KHÔNG THỂ phân loại hết các hàm

    → "Tính năng" (feature) = cách MÔ TẢ phần mềm từ bên ngoài
    → "Game có tính năng shop" → shop = NHIỀU hàm kết hợp
    → "Game có tính năng xếp hạng" → xếp hạng = NHIỀU hàm kết hợp
    → Shop và xếp hạng có thể DÙNG CHUNG 1 hàm cơ bản
    → Thêm/bớt/sửa tính năng = thay đổi cách gọi, KHÔNG thay đổi hàm

    → Tính năng = OBSERVATION PARAMETER:
      ✅ Hữu ích: user biết phần mềm "LÀM ĐƯỢC GÌ"
      ✅ Communicate: product manager nói "tính năng shop" → team hiểu
      ❌ Không phải technical: dev không code "tính năng" → dev code "hàm"
      ❌ Tính năng KHÔNG tồn tại riêng biệt → là tên gọi cho tổ hợp hàm

  NÃO:
    → "Chunk" = đơn vị tính toán thật
    → Mỗi chunk = neurons fire đồng bộ, synapses thật
    → VÔ HẠN chunks (tùy experience)
    → KHÔNG THỂ phân loại hết chunks

    → "Schema" = cách MÔ TẢ chunk networks từ bên ngoài
    → "Sợ chó" = NHIỀU chunks kết hợp ([chó]+[nguy hiểm]+[lùi]+[tim đập])
    → "Lái xe" = NHIỀU chunks kết hợp ([phanh]+[lái]+[gương]+[tốc độ])
    → "Sợ chó" và "sợ rắn" DÙNG CHUNG chunk [nguy hiểm]
    → Thêm/bớt/sửa schema = thay đổi tên gọi, chunks VẪN fire

    → Schema = OBSERVATION PARAMETER:
      ✅ Hữu ích: "anh ấy có schema tình yêu phức tạp" → nhanh hiểu
      ✅ Communicate: therapist nói "schema cũ fire" → client hiểu
      ❌ Không phải mechanism: não KHÔNG "chạy schema" → não fire chunks
      ❌ Schema KHÔNG tồn tại riêng biệt → là tên gọi cho chunk network

  MỞ RỘNG:
    → FlappyBird và CandyCrush: hàm KHÁC ĐÁ KỂ, overlap chút engine
    → Giáo sư toán và nhân viên tạp hóa: chunks toán OVERLAP, chunks khác KHÁC
    → Source Excel KHÔNG dùng viết FlappyBird: chunks MỘT domain ≠ chunks domain KHÁC
    → Dev game học web DỄ HƠN newbie: engine chunks overlap → transfer partial
    → = Giống chunks: overlap PARTIAL, transfer PARTIAL, không 100%
```

---

## §3 — GIÁ TRỊ CỦA SCHEMA NHƯ OBSERVATION PARAMETER

```
🟡 SCHEMA VẪN HỮU ÍCH — biết rõ giới hạn:

  ① MÔ TẢ (Descriptive):
     → "Schema tình yêu bị trauma contaminate" = shorthand cho:
       "chunks connection + chunks trust + chunks trauma chia sẻ
       shared chunks [hồi hộp] → fire trauma khi fire connection"
     → Schema = ngôn ngữ NGẮN cho pattern chunk PHỨC TẠP
     → KHÔNG cần nói 50 chunks → nói 1 tên schema

  ② DỰ ĐOÁN (Predictive):
     → "Người có schema sợ bị bỏ → predict ghen tuông khi partner bận"
     → = Người có chunk network [bỏ rơi + lo + kiểm soát] compiled mạnh
       → predict chunks fire khi partner absent → ghen tuông
     → Schema giúp PREDICT hành vi nhanh hơn liệt kê chunks

  ③ GIAO TIẾP (Communicative):
     → Therapist: "schema cũ đang fire" → client hiểu ngay
     → Nếu nói: "chunk network [childhood abandonment + cortisol association
       + amygdala pattern] đang spread activate" → KHÔNG AI hiểu
     → Schema = ngôn ngữ cho NON-EXPERTS

  ④ NAVIGATE (Navigation aid):
     → "Fix schema tình yêu" = practical instruction:
       nhận diện pattern → body-listen → phân biệt chunks
     → KHÔNG CẦN biết chính xác chunks nào → biết PATTERN = đủ navigate
     → Schema = compass, KHÔNG phải GPS

  ⚠️ GIỚI HẠN:
     → Schema KHÔNG phải mechanism → KHÔNG dùng để THIẾT KẾ can thiệp
     → Can thiệp phải ở chunk level:
       thay đổi body-input, compile chunks mới, re-associate existing chunks
     → "Fix schema" = actually "re-wire chunk links" + "compile new chunks"
     → Nói "fix schema" = tiện → nhưng phải BIẾT underneath = chunk work
```

---

## §4 — PROPERTIES QUAN SÁT ĐƯỢC

### §4.1 Gradient Depth (chunk compile depth)

```
🟡 Schema quan sát được có DEPTH GRADIENT:

  Thực chất: chunks compiled ở depths khác nhau.
  Observation label: "schema sâu" hay "schema nông".

  NÔNG (domain-specific, ít repetition, ít modality):
    → "Trời mưa mang ô" — chunks ít, links yếu
    → Thay đổi: NGÀY (đổi context = đổi ngay)
    → Ảnh hưởng: HẸP (1 context)

  GIỮA (cross-context, nhiều repetition):
    → "Phải luôn productive" — chunks nhiều, reinforced qua năm
    → Thay đổi: TUẦN → THÁNG (cần repeated experience mới)
    → Ảnh hưởng: TRUNG BÌNH (nhiều contexts)

  SÂU (body-embedded, emotional weight lớn):
    → "Tôi vô giá trị" — chunks embedded vào cortisol baseline, muscle tension
    → Thay đổi: THÁNG → NĂM (phải thay đổi BODY, không chỉ "nghĩ khác")
    → Ảnh hưởng: RỘNG (ảnh hưởng mọi context)

  DEPTH = f(số lần lặp × số modality × emotional weight)
  → Depth CAO = synapses MẠNH = chunk links dày = khó re-wire
  → Depth THẤP = synapses YẾU = chunk links mỏng = dễ re-wire

  ⚠️ DEPTH CHỈ LÀ 1 CHIỀU — 2D MODEL:
  → Chiều 2 = LINK DENSITY (pattern linked với bao nhiêu chunks khác qua thời gian)
  → High Depth + Low Density (bị chó cắn 1 lần): PFC thấy, therapy weeks
  → Low Depth + High Density (cultural pattern): PFC KHÔNG thấy, therapy YEARS
  → Chi tiết: Chunk/Background-Pattern.md (2D model Compile Depth × Link Density)

  🟢 Kiểm chứng "trúng số" (Brickman et al. 1978):
    Surface: "mai không đi làm" → ĐỔI NGAY ✅
    Mid: "tôi là người giàu" → vài tháng mới "tin" ⚠️
    Deep: "tôi vô giá trị" → VẪN CÒN dù giàu ❌
    Body: cortisol baseline VẪN CAO ❌
    → ~70% lottery winners quay về happiness baseline trong 1-2 năm
    → Vì: deep chunk networks KHÔNG đổi vì surface change
```

### §4.2 Activation States (chunk activation observation)

```
🟡 Schema quan sát được ở 3 trạng thái — thực chất = chunk activation:

  "COMPILED" (vô thức, auto-run):
    → Chunks fire TỰ ĐỘNG khi trigger match
    → PFC KHÔNG tham gia
    → Observation: "hành vi tự động", "biết mà không cần nghĩ"
    → Mechanism: chunk spreading activation probability-weighted
    → VD: thấy chó → chunks [threat-chó] fire → lùi. Không cần "nghĩ"
    → = PHẦN LỚN hành vi hàng ngày

  "ACTIVE" (PFC đang hold):
    → PFC hold anchor chunks → BIAS spreading activation hướng cụ thể
    → Observation: "đang nghĩ về", "đang tập trung vào"
    → Mechanism: PFC working memory hold + chunk bias (Chunk.md §8, §9)
    → VD: PFC hold [game design] → activation spread trong game-related chunks

  "MONITOR" (nền, luôn chạy nhẹ):
    → Chunks chạy BACKGROUND → alert PFC khi detect mismatch
    → Observation: "luôn để ý", "canh chừng"
    → Mechanism: low-level chunk activation + prediction-delta detection
    → VD: chunks [con tôi an toàn?] chạy nền → con khóc → VTA alert PFC
    → 🟢 Cocktail party effect (Cherry 1953): tên mình = always-on monitor

  → 3 states NÀY = observation labels cho CHUNK ACTIVATION LEVELS
  → Chunks KHÔNG "biết" mình thuộc schema nào → chỉ fire theo link strength
```

### §4.3 Decay + Reactivation (chunk decay observation)

```
🟡 Schema "mờ dần" = chunks decay theo gradient:

  Chunk yếu DẦN khi không reinforced:
    → Synapse yếu → fire ÍT → pattern MỜ
    → NÔNG (ít lặp, ít modality): mờ NHANH (tháng)
    → SÂU (nhiều lặp, nhiều modality, emotional): mờ CỰC CHẬM

  🟢 Alzheimer's: mất chunks MỚI trước, CŨ NHẤT mất SAU CÙNG
  → = Depth = durability

  Interference — chunks mới cạnh tranh chunks cũ:
    → Proactive: chunks cũ CẢN chunks mới ("quen số sàn → khó học tự động")
    → Retroactive: chunks mới cạnh tranh links của chunks cũ
    → 🟢 Competitive re-linking (Nader 2000): chunk links NEVER fully deleted,
      chỉ probability shift. Stress can reactivate old links.
    → = "Cai 10 năm vẫn có thể relapse" — old links STILL EXIST

  Reactivation:
    → Chunk links yếu nhưng VẪN CÒN → reactivate DỄ HƠN learn mới
    → 🟢 Savings effect (Ebbinghaus): "học lại" nhanh hơn "học lần đầu"
    → = Schema "mờ" = chunk links yếu, KHÔNG mất
```

### §4.4 Cross-Contamination (shared chunk activation)

```
🟡 Schemas "ảnh hưởng lẫn nhau" = chunks CHIA SẺ:

  Chunk [hồi hộp] thuộc NHIỀU networks:
    → Network "tình yêu": [crush] → [hồi hộp] → [gần] → ...
    → Network "sợ bị bỏ": [một mình] → [hồi hộp] → [lo] → ...
    → Shared chunk [hồi hộp] = BRIDGE

  Khi network "tình yêu" fire:
    → [crush] fire → [hồi hộp] fire → spreading activation
    → [hồi hộp] CŨNG activate network "sợ bị bỏ" (qua shared link)
    → = "Đang yêu vui vẻ → bỗng LO SỢ VÔ CỚ"
    → = KHÔNG vô cớ: shared chunk bridge

  Tại sao TRAUMA networks dễ contaminate:
    ① Compiled SÂU (emotional peak → strong synapses)
    ② Chunks RỘNG (sợ, hồi hộp, bất an = chunks PHỔ BIẾN → shared nhiều)
    ③ Amygdala reinforce (cortisol chronic → amygdala sensitive → fire dễ)
    → = Trauma = "ô nhiễm" DỄ NHẤT cho chunk networks khác

  🟢 Retrieval-induced forgetting (Anderson 1994)
  🟢 Stress relapse mechanism (Sinha 2001)

  Ví dụ "chọn nhầm người":
    → Chunks [yêu = hồi hộp + bất an + sợ mất] compiled từ childhood trauma
    → Gặp người mới → vô thức match: người cho cảm giác HỒI HỘP + BẤT AN
    → Body sensation GIỐNG "yêu" (dopamine + NE tương tự)
    → Vô thức KHÔNG phân biệt → ráp trauma chunks vào "tình yêu" mới
    → = "Luôn yêu người không phù hợp" = trauma chunk matching, KHÔNG phải "xui"
```

---

## §5 — SCHEMA × BODY-FEEDBACK

### §5.1 Không có "schema âm" — chỉ có xung đột

```
🟡 MỌI chunk network hình thành ĐỂ PHỤC VỤ body → luôn "dương" ban đầu:

  "Kiềm chế lời nói":
    = DƯƠNG khi ở nhà bố mẹ strict (BẢO VỆ body khỏi bị phạt)
    = "ÂM" khi ở công ty cần communicate (CẢN body kết nối)
    → CÙNG chunk network → KHÁC context → từ "dương" THÀNH "âm"
    → = Chunk network KHÔNG có valence cố định → CONTEXT quyết định

  3 loại xung đột:

    Loại 1 — 2 networks CÙNG context, KHÁC hướng:
      "Muốn ăn" + "muốn giảm cân" → cả 2 dương riêng → xung đột CÙNG LÚC

    Loại 2 — Network ĐÚNG context CŨ, SAI context MỚI (OUTDATED):
      "Tiết kiệm từng đồng" → ĐÚNG khi nghèo → OUTDATED khi lương ổn

    Loại 3 — NHIỀU networks ĐÚNG riêng, TỔNG THỂ xung đột:
      "Career" + "family" + "self-care" = TẤT CẢ dương → 24h KHÔNG đủ

  Cơ chế:
    → Network A push body hướng TRÁI, network B push hướng PHẢI
    → Body chỉ đi được 1 hướng → PFC phải chọn
    → Network bị chặn VẪN fire → tốn energy → dissonance
    → 🟡 ĐAU ∝ |force_A − force_B| khi NGƯỢC hướng
    → ĐAU CỰC ĐẠI khi 2 forces GẦN BẰNG (paralysis)
    → "Quyết định xong DÙ SAI cũng nhẹ hơn KHÔNG quyết định"
```

### §5.2 Override spectrum

```
🟡 Chunk networks CÓ THỂ override body-base signals:

  CƠ CHẾ — double suppress:
    ① Chunk network redirect attention (PFC ignore body signal)
    ② Cortisol từ chunk network suppress body sensation (biochemistry)
    → Body GẦN NHƯ câm → chunk network chạy tự do

  SPECTRUM từ nhẹ tới cực đoan:

    Nhẹ (hàng ngày):
      → Đọc sách hay quên ăn: novelty chunks override hunger signal
      → Scroll MXH tới 2h sáng: novelty chunks override sleep signal

    Trung bình:
      → Workaholic quên ngủ: threat-status chunks override L1 sleep
      → Diet cực đoan: status chunks override L1 nutrition

    Nặng:
      → Game tới chết: novelty chunk loop override survival signals
      → Anorexia: status chunks override L0 nutrition

    Cực đoan:
      → Tử vì đạo: belief chunk network override L0 Alive
      → Mẹ nhảy vào lửa cứu con: protect chunks override L0 Alive(thân)

  → V7.8: signal strength decides, KHÔNG PHẢI layer priority
  → Chunk network compiled MẠNH + cortisol sustained = CÓ THỂ override BẤT KỲ signal
  → "Bug" cho cá nhân (quên ăn → hại body)
  → "Feature" cho gene/tập thể (hy sinh → gene survive)
```

### §5.3 Chunk association — Novelty vs Threat

```
🟡 Cùng chunk, khác association → khác SUỐT ĐỜI:

  NOVELTY-DIRECTION compile (tò mò, thích thú):
    → Chunk gắn với: curiosity + relief + opioid
    → Body-base: "chunk này cho tôi SƯỚNG" → sẵn sàng dùng lại
    → VD: Newton đọc physics vì tò mò → chunk gắn opioid → THÍCH

  THREAT-DIRECTION compile (sợ, bị ép):
    → Chunk gắn với: sợ + cortisol + "phải làm"
    → Body-base: "chunk này gắn KHÓ CHỊU" → không muốn dùng lại
    → VD: học sinh bị ép học toán → chunk gắn cortisol → GHÉT

  → CÙNG kiến thức → KHÁC association → KHÁC khả năng dùng
  → Cortisol at compile time = determines chunk association tag (Chunk.md §2.4 NT7)
  → MỌI HÀNH VI = MIX threat + novelty (tỉ lệ KHÁC NHAU)

  Ngưỡng:
    Threat NHẸ (60:40): dễ update sau → chunk association CÓ THỂ shift
    Threat NẶNG (95:5): cortisol cực sâu → body PHẢN ĐỐI khi dùng → CỰC KHÓ update

  → Chi tiết: Cortisol-Baseline.md v2.0 §3.5
```

### §5.4 "Giọt nước tràn ly"

```
🟡 Chunk swap trong network mạnh:

  Network đang active MẠNH (compiled months, cortisol duy trì):
    → Chunk [tôi cố được] giữ network ở mode "chịu đựng"
    → Body: khó chịu nhưng CHƯA tới threshold ĐAU

  1 event NHỎ (sếp nhắc nhẹ):
    → Chunk swap: [tôi cố được] → [tôi có thể bị đuổi]
    → CÙNG network CÙNG cường độ → nhưng giờ mode "THREAT"
    → Toàn bộ energy → chạy threat → body-feedback CỰC LỚN

  Spectrum phản ứng CÙNG sự kiện:
    Người khỏe (ly trống): "ok, sửa" → nhẹ nhàng
    Người mệt 3 tháng (ly nửa): khó chịu 1 tiếng → ok
    Người burnout (ly đầy): KHÓC ngay tại chỗ
    → CÙNG giọt → KHÁC kết quả → vì accumulated dissonance KHÁC

  → Body-Feedback-Mechanism.md: compound dynamics = Miss + Shift + Gap
  → 02-Dissonance.md: 14 intensity levels
```

---

## §6 — SCHEMA × PFC

### §6.1 PFC observe chunk networks → gọi là "schema"

```
🟡 PFC KHÔNG "thấy" schema — PFC thấy CHUNK ACTIVATIONS → LABEL:

  Body compute FIRST → Feeling emerge → PFC observe LAST
  (🟢 Damasio 1994, 1999: somatic markers precede conscious decision)

  PFC observe:
    → Nhiều chunks fire ĐỒNG THỜI theo pattern → PFC nhận tổng hợp
    → PFC label: "à, đây là 'sợ chó'" (verbal label cho chunk pattern)
    → Label = Feeling.md v2.0 Layer 6 (40-80% fidelity) — LOSSY

  PFC KHÔNG thấy:
    → Chunks CỤ THỂ nào đang fire (too many, too fast)
    → Links CỤ THỂ nào mạnh/yếu
    → Shared chunks đang bridge tới network NÀO
    → = PFC thấy OUTPUT (feeling, behavior) → suy ngược PATTERN → gọi "schema"

  → = Schema = PFC's BEST GUESS about what chunk network is active
  → APPROXIMATE, not exact
  → Useful, not authoritative
```

### §6.2 PFC orchestrate chunk networks

```
🟡 PFC CAN bias chunk activation (indirect control):

  PFC hold chunks → BIAS spreading activation direction
  → Vô thức phản ứng dây chuyền theo bias
  → Chunks compiled cho tình huống → auto execute

  VD: PFC hold "viết con chó"
    → Vô thức đã compile [gõ c-o-n space c-h-ó]
    → Ngón tay tự gõ → PFC nhìn lại: đúng ✓
    → PFC KHÔNG nghĩ tới motor details

  VD: Chuyên gia xem tranh ở chợ đồ cũ
    → Lướt qua → vô thức match weak: "nét vẽ kỳ lạ"
    → PFC notice → cầm lên, dùng kính lúp (amplify input cho vô thức)
    → Vô thức match SÂU hơn → "bức tranh đặc biệt"
    → = PFC KHÔNG "thấy" tranh đẹp → PFC hold attention →
      vô thức match → body reward → PFC observe reward

  KHI PFC BẤT LỰC:
    → Chunks cho tình huống CHƯA COMPILED → PFC hold nhưng vô thức không có gì run
    → Body-base signal quá mạnh → PFC override thất bại
    → PFC effectiveness = f(chunks đã compiled cho tình huống đó)
```

### §6.3 Schema KHÔNG THỂ phân tích chính xác

```
🟡 TẠI SAO không thể "đọc" schema chính xác:

  ① 86 tỷ neurons × ~100 nghìn tỷ connections = quá phức tạp
  ② Chunk networks = MULTI-MODAL (verbal chỉ capture ~1/6)
  ③ Deep chunks = BODY EMBEDDED (cortisol baseline, muscle tension)
     → chính chủ nhân CŨNG không biết
  ④ Chunk links thay đổi LIÊN TỤC → "chụp" lúc này → lúc sau đã khác
  ⑤ Công cụ hiện đại CHƯA ĐỦ: fMRI thấy vùng, KHÔNG thấy chunk content

  VẬY FRAMEWORK LÀM GÌ?
    → KHÔNG phân tích chính xác (impossible)
    → CÓ THỂ: nhận diện PATTERN (hành vi lặp lại = chunk network biểu hiện)
    → CÓ THỂ: ước lượng depth (deep vs surface chunks)
    → CÓ THỂ: suggest hướng (body fix trước, chunk links tự adjust)
    → = COMPASS, không phải GPS
    → = "Công thức, không đáp án"

  ⭐ NGƯỜI KHÁC THẤY PATTERN MÀ CHỦ NHÂN KHÔNG THẤY:
    → Deep chunks = chạy vô thức → PFC KHÔNG observe
    → Observer BÊN NGOÀI: thấy PATTERN hành vi lặp lại → build chunks VỀ pattern
    → = "Bạn hay tự sabotage khi gần thành công" (bạn thân thấy, mình không)
    → 🟢 Blind spot bias (Pronin 2002)
    → = Therapist/mentor/bạn thân: giá trị CHÍNH = external observer
    → Cho chunks VỀ CHÍNH BẠN mà PFC bạn không tự build được
```

---

## §7 — SCHEMA × DOMAIN

### §7.1 Base → Shift → Check — Universal Pattern

```
🟡 MỌI chunk networks tương tác domain theo CÙNG 1 pattern:

  ① CÓ BASE ổn định (compiled chunks quen thuộc):
     → VTA: quen → KHÔNG fire (habituation) → PFC không chú ý

  ② SHIFT NHẸ từ base (thử cái mới, khác chút):
     → VTA: detect BIẾN ĐỘNG → dopamine → PFC biết

  ③ BODY CHECK (domain reality test):
     → Khớp: opioid → ACCEPT → chunk links UPDATE
     → Không khớp: REJECT → quay về cũ

  ④ NEW BASE → shift tiếp → check tiếp → ...

  Pattern NÀY chạy XUYÊN MỌI domain:
    Ăn: cơm quen (base) + món phụ mới (shift) + ngon không? (check)
    Nhạc: thể loại quen + bài mới + hay không?
    Code: architecture có + feature mới + work không?
    Người: bạn quen + người mới + hợp không?
    → CÙNG mechanism: prediction-delta + body evaluate + chunk update

  ⭐ DUAL-PULL TENSION (Body-Feedback.md §2):
    → Hardware pull: muốn giữ smooth → BẢO THỦ
    → Domain pull: đòi adapt → ĐÒI HỎI
    → = Chunk networks luôn bị KÉO giữa "ổn định" và "cập nhật"
    → = ATTRACTOR PATTERN: stable base + incremental shift + feedback check
```

### §7.2 Chunk network hình thành — 2 con đường

```
🟡 Chunk networks build qua 2 nguồn:

  CON ĐƯỜNG 1 — VÔ THỨC TỰ BUILD (không cần PFC):
    → Association learning: stimulus → body respond → chunks TỰ wire
    → NHANH (1 experience CÓ THỂ đủ, đặc biệt emotional peak)
    → KHÔNG TỐN PFC
    → NHƯNG: chỉ từ TRẢI NGHIỆM TRỰC TIẾP
    → 🟢 Trẻ 0-4 tuổi PFC gần zero → VẪN build networks phức tạp

  CON ĐƯỜNG 2 — PFC DRAFT + COMPILE (imagine):
    → PFC imagine scenario → body simulate → body check → compile nếu ok
    → CHẬM hơn, TỐN PFC
    → NHƯNG: từ IMAGINE — không cần trải nghiệm trực tiếp
    → PREDICT XA hơn, AN TOÀN hơn, CROSS-DOMAIN possible
    → VD: Einstein thought experiment → draft → insight

  CẢ HAI CẦN MẠNH:
    Vô thức mạnh + PFC yếu: nhiều chunks cơ bản + ÍT predict xa
    PFC mạnh + vô thức yếu: draft hay nhưng KHÔNG body-verify
    CẢ HAI: nền RỘNG + đỉnh CAO = expert

  ⚠️ VÔ THỨC RÁP BẰNG CHUNKS CÓ SẴN — KHÔNG PHÂN BIỆT:
    → Vô thức tìm chunks KHỚP NHẤT → RÁP
    → KHÔNG filter "tốt" hay "trauma"
    → Trauma chunks CÓ THỂ bị ráp vào network mới MÀ KHÔNG BIẾT
    → = "Mỗi người yêu KHÁC dù gặp CÙNG người"
```

---

## §8 — BODY BASELINE STATE

```
🟡 MỌI chunk networks build TRÊN 1 nền tảng: body baseline state
  = Ground truth — PFC, verbal, logic đều THAM CHIẾU về đây

  Body Baseline State = trạng thái TỔNG THỂ body khi NGHỈ:
    Cortisol baseline:  mức stress nền
    Opioid tone:        mức pleasure nền
    Oxytocin level:     mức connection nền
    Muscle tension:     vai gồng? thả lỏng?
    Gut state:          tiêu hóa bình thường?
    Sleep architecture: deep sleep đủ? REM đủ?
    HRV:                heart rate variability
    Immune baseline:    inflammation mãn tính?

  = "Khi không có gì xảy ra, cơ thể TÔI feel thế nào?"

  ⭐ TẠI SAO BODY BASELINE LÀ NHƯ VẬY — MECHANISM:
    → Body baseline = PHYSICAL REFLECTION của Background Patterns
    → Cortisol baseline CAO vì Background Pattern [threat] chạy nền → cortisol sustained
    → Opioid tone THẤP vì Background Pattern [not enough] suppress reward
    → Muscle tension CAO vì Background Pattern [alert] fire liên tục
    → = Body baseline KHÔNG random — là output của accumulated chunk patterns
    → Chi tiết mechanism: Chunk/Background-Pattern.md (chunk-level underneath)

  Fix body baseline → chunk networks tự adjust (ground truth thay đổi)
  Fix chunks MÀ KHÔNG fix body → relapse (body PULL quay lại)
  Fix CÙNG LÚC body + build competing Background Pattern → TRUE resolution

  → Thứ tự: Body → Chunks → Schema observation → ĐÚNG THỨ TỰ
  → = "Biết nhưng không thay đổi" = verbal chunks updated, Background Pattern CHƯA

  3 ĐƯỜNG reverse-engineer body baseline:
    ① Observe behavior: "tôi hay LÀM GÌ khi stress?" → chunk network biểu hiện
    ② Observe body: "vai tôi THƯỜNG gồng hay thả?" → body state hiện tại
    ③ Self-identify conflicts: "tôi MUỐN gì nhưng KHÔNG LÀM?" → chunk conflict
    → = Không cần biết CHÍNH XÁC chunks → biết PATTERN = đủ navigate
```

---

## §9 — CÂU HỎI MỞ

```
S1: Chunk network "negative" có THẬT SỰ không tồn tại?
    → Framework: chỉ có conflict → nhưng "tôi vô giá trị" LUÔN conflict MỌI context?
    → Có thể: always-on network compiled CỰC SÂU = pseudo-negative
    → Technically conflict → practically = negative everywhere
    → ⚠️ Chưa resolve hoàn toàn

S2: Chunk links có thể giảm tới ZERO hoàn toàn?
    → Likely: KHÔNG BAO GIỜ zero → chỉ probability CỰC THẤP
    → "Cai 10 năm vẫn relapse" = old links CÒN dù cực yếu
    → 🟢 Competitive re-linking (Nader 2000): links mới CẠNH TRANH cũ
    → 🟢 Stress relapse (Sinha 2001): stress reactivate old links

S3: AI detect chunk network patterns?
    → AI đọc TEXT = detect verbal chunks (~1/6 total)
    → CẦN: body data (HRV, cortisol, muscle) để detect SÂU
    → 3 tầng: AI detect → Chuyên gia verify → Client body-check
    → Chi tiết: AI-Schema-Detection.md (planned)

S4: Epigenetics × chunk networks?
    → Trauma → cortisol high → epigenetic changes → 1-2 thế hệ?
    → 🟢 Dias & Ressler 2014: fear conditioning → offspring fear response
    → = Chunk ASSOCIATION có thể "di truyền" qua epigenetics
```

---

## §10 — HONEST ASSESSMENT

```
ESTABLISHED (🟢):
  → Chunk = learned associative patterns (Hebb 1949, Bliss & Lømo 1973)
  → Spreading activation (Collins & Loftus 1975)
  → Competitive re-linking (Nader 2000)
  → Savings effect (Ebbinghaus)
  → Cocktail party effect (Cherry 1953)
  → Lottery winners baseline return (Brickman et al. 1978)
  → Blind spot bias (Pronin 2002)
  → Stress relapse (Sinha 2001)
  → Somatic markers precede decision (Damasio 1994)
  → Fear conditioning epigenetics (Dias & Ressler 2014)

FRAMEWORK SYNTHESIS (🟡):
  → Schema = observation parameter (consistent với 9/9 deep drill files)
  → "Không có schema âm" = chỉ có context-dependent conflict
  → Override spectrum = cùng cơ chế, khác mức độ
  → Chunk association tag (novelty vs threat direction)
  → PFC observe chunk activations → label = "schema"
  → Base → Shift → Check = universal pattern
  → Body baseline = ground truth → fix body trước
  → Dual-pull tension = evolutionary feature

METAPHOR (⚠️):
  → "Schema = tính năng phần mềm" = hình dung, không 1-1 chính xác
  → Não KHÔNG phải máy tính → analogy giúp hiểu, không phải mô hình
  → Depth gradient = observation, KHÔNG đo được chính xác per-%
```

---

## §11 — CROSS-REFERENCES

### §11.1 Core mechanism files

```
  Core-v7.8-Draft.md             — cycle architecture, §8 observation parameters
  Chunk.md v2.0                  — chunk substrate (sole substrate, 14 sections)
  Body-Feedback.md v1.1          — dual-pull, H10, interface loop
  Body-Feedback-Mechanism.md v1.0— chunk dynamics (Shift/Miss/Gap), compound
  Feeling.md v2.0                — PFC observation interface, 7-layer fidelity
  Cortisol-Baseline.md v2.0      — amplifier, direction gate, 7 modes
  Valence-Propagation.md v1.1    — valence per-entity + chain + PFC blindness
```

### §11.2 Schema-specific files

```
  Anchor-Schema.md v1.2          — sync point, trust binding, 4 nguồn fill
  Anchor-Schema-Example.md       — anchor cases
  Anchor-Schema-Extreme-Example.md — extreme anchor cases
  AI-Schema-Detection.md         — AI-assisted pattern detection
  Melody Lens/                   — Personal-Melody, Global-Melody, Melody-Arc
```

### §11.3 Related analysis

```
  Agent.md v1.0                  — agent = function on chunks, 4-layer
  Empathy.md v1.0                — SPM applied to others
  Drive.md v1.1                  — drive = emergent, 6 PFC Modes
  Imagination-Analysis-v2.md     — imagine = PFC engine
```

### §11.4 Application files

```
  Body-Personal-Optimization.md  — personal tuning
  Body-Parenting-Optimization.md — parenting application
  Research/Education/             — education applications
```

### §11.5 Superseded files (trong backup/)

```
  Schema-Operations-v1.md        — content → Chunk.md v2.0, Feeling.md v2.0
  Schema-Example-v1.md           — data valid, framing outdated
  Schema-Diagnostic.md           — diagnostic tools (framing outdated)
```

---

> *Schema v2.0 — "Schema = observation parameter, NOT component.
> Chunks = hàm (tính toán thật). Schema = tính năng (mô tả từ bên ngoài).
> Body-base chạy HOÀN TOÀN trên chunks.
> Schema vẫn hữu ích: mô tả, predict, communicate.
> Nhưng can thiệp phải ở chunk level: body-input, compile, re-associate.
> Fix body TRƯỚC → chunks adjust → schema observation thay đổi."*
