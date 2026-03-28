# Chunk & PFC — Não Không Tính Toán, Não Tìm Kiếm

> **Bạn nghĩ 2+3 thì não "tính" ra 5?**
> Không. Não TÌM trong database: "có pattern nào match [2+3] không?"
> → Tìm thấy chunk [2+3=5] đã compiled → output "5."
> Nếu KHÔNG tìm thấy → tách nhỏ → tìm lại → sequential.
>
> Não = DATABASE + SEARCH ENGINE.
> PFC = người gõ tìm kiếm (tối đa 4 từ khóa cùng lúc).
> "Thông minh" = database LỚN + chunks compiled SÂU → search HIT nhanh.
>
> File này = CORE mechanism. Chi tiết search: Chunk-Search-Advanced.md.
> Ứng dụng + failure modes: Chunk-Practical.md.

---

> **Trạng thái:** DRAFT — hypothesis từ framework + neuroscience foundations
> **Ngày:** 2026-03-28
> **Mục đích:** Giải thích chunk LÀ GÌ, PFC DÙNG chunk thế nào,
> và tại sao "tính toán" = "chuỗi tìm kiếm." CẦN VÀ ĐỦ — không thừa.
> **Reference:** Schema-Operations.md, PFC-Analysis.md, Core-v7.5-Draft.md §5
> **Quy ước:** 🟢 Research support | 🟡 Suy luận từ framework | 🔴 Hypothesis

---

## 1. Chunk Là Gì — Ở Level Neuron

```
🟢 CHUNK = nhóm neurons đã WIRE TOGETHER → fire thành 1 ĐƠN VỊ:

  🟢 Hebb (1949): "Neurons that fire together, wire together"

  CHƯA compiled (neurons rời):
    Thấy số "3" lần đầu:
      → Neuron nhóm A: hình dạng "3" (visual cortex)
      → Neuron nhóm B: âm "ba" (auditory cortex)
      → Neuron nhóm C: ý nghĩa "số lượng 3" (association cortex)
      → = 3 nhóm RIÊNG LẺ → PFC phải hold CẢ 3 → tốn 3 dimensions

  ĐÃ compiled (neurons wired):
    Thấy số "3" lần thứ 1000:
      → Nhóm A+B+C đã WIRE thành 1 UNIT
      → Fire 1 = biết hết (hình + âm + nghĩa) → tốn 1 dimension
      → = "Chunk" = compressed package

  CHUNK vs SCHEMA:
    → Chunk = ATOM (1 đơn vị nhỏ nhất, không có purpose riêng)
    → Schema = MOLECULE (nhiều chunks linked → có PURPOSE/FUNCTION)
    → VD: chunk [đạp phanh] = 1 unit. Schema [lái xe] = mạng chunks → PURPOSE: di chuyển
    → Schema có 3 trạng thái: compiled (auto-run), active (PFC dùng), monitor (nền)
    → = File này focus CHUNK + PFC search. Schema chi tiết: Schema.md §1.1

  CHUNK MULTI-MODAL — span NHIỀU cortex:
    → VD: chunk "mẹ" = mặt (visual) + giọng (auditory) + ôm (somatic) + ấm (emotional)
    → = 1 chunk DISTRIBUTED across toàn não
    → Fire 1 phần (nghe giọng mẹ) → KÉO cả chunk fire (nhớ mặt, nhớ ôm,...)
    → 🟢 Distributed representations (Rumelhart & McClelland 1986)
```

---

## 2. Chunk Compilation — CÁCH Neurons Wire

```
🟡 4 CÁCH COMPILE:

  ① REPETITION — lặp lại nhiều lần:
    → Fire pattern 50 lần → connections strengthen → auto
    → CHẬM nhưng BỀN
    → 🟢 Long-term potentiation (Bliss & Lømo 1973)

  ② EMOTIONAL PEAK — 1 lần cảm xúc cực mạnh:
    → Amygdala + NE → wire CỰC NHANH, 1 lần đủ
    → VD: bị chó cắn → chunk [chó=nguy hiểm] compiled NGAY
    → 🟢 Flashbulb memories (Brown & Kulik 1977)

  ③ MULTI-MODAL — nhiều kênh cùng lúc:
    → Visual + auditory + somatic + motor CÙNG fire → wire across NHIỀU cortex
    → = Experience THẬT compile MẠNH hơn imagine/đọc/nghe

  ④ SLEEP CONSOLIDATION — ngủ compile offline:
    → Hippocampus REPLAY → strengthen hoặc prune
    → 🟢 Sleep consolidation (Walker 2017)


  CHUNK HIERARCHY — chunk CHỨA sub-chunks:
    Beginner lái xe: [lái]+[phanh]+[mirror]+[signal] = 4 chunks RIÊNG → PFC quá tải
    Expert lái xe: [LÁI XE] = 1 meta-chunk → fire 1 = tất cả auto → PFC freed
    → = Expert: 1 PFC slot = 1 meta-chunk = CỰC NHIỀU operations

  CHUNK RECONSOLIDATION — sửa chunk đã compiled:
    → Khi chunk được RECALL → TẠM THỜI unstable (~vài giờ)
    → Trong window đó → CÓ THỂ modify → re-compile
    → = Therapy: recall trauma → reframe → re-compile = bớt đau
    → ⚠️ Recall MÀ KHÔNG modify → chunk STRENGTHEN → TỆ HƠN
    → 🟢 Memory reconsolidation (Nader 2000)

  CHUNK DECAY — không dùng yếu dần:
    → "Quên" ≠ mất → "quên" = retrieval path YẾU
    → Re-exposure → "ồ NHỚ RỒI!" = path reactivate
    → Chunk compiled SÂU (childhood, emotional) = gần như không decay
    → 🟢 Savings in relearning (Ebbinghaus 1885)
```

---

## 3. PFC = Search Engine, Không Phải Calculator

```
🟡 PFC KHÔNG "tính" — PFC ORCHESTRATE quá trình tìm kiếm:

  MÔ HÌNH:
    Não = DATABASE hàng tỉ chunks đã compiled
    PFC = NGƯỜI GÕ tìm kiếm (tối đa ~4 từ khóa cùng lúc)
    "Suy nghĩ" = gõ từ khóa → database search → output

  VTA = CHUÔNG BÁO cho PFC:
    → PFC KHÔNG tự biết khi nào cần search → VTA BÁO
    → VTA detect: "input KHÁC prediction" → fire dopamine → PFC ALERT
    → KHÔNG CÓ VTA alert → PFC KHÔNG BIẾT → compiled schemas tự chạy

  PFC 4 DIMENSIONS = 4 TỪ KHÓA TÌM KIẾM:
    → PFC hold tối đa ~4 chunks ACTIVE cùng lúc
    → 4 chunks active = 4 search terms gửi vào database
    → Database search pattern MATCH → output emerge
    → 🟢 Working memory ~4 items (Cowan 2001)

  VD:
    "2+3=?" → PFC hold [2]+[3]+[cộng] → search → HIT [2+3=5] → "5"
    "247+389=?" → search MISS → tách nhỏ → 3 searches sequential → "636"
    Game design: hold [stickman]+[combat]+[nhạc]+[2 bên] → search → HIT combo MỚI

  → Search xong → output emerge → CHƯA XONG
  → Body phải DUYỆT output (§6) → PFC chọn dựa trên body evaluation
```

---

## 4. "Tính" = Chuỗi Recall — Không Có Raw Computation

```
🟡 MỌI "tính toán" ở level chunk = RECALL:

  1 BƯỚC RECALL (compiled): "2+3=?" → [2+3=5] fire → "5" → INSTANT
  SEQUENTIAL RECALL (chưa compiled): "(1+2)+4=?" → [1+2=3] → [3+4=7] → 2 bước
  PROCEDURAL RECALL (dùng procedure): đếm ngón tay = recall [đếm] procedure

  → = "Tính" = CHUỖI pattern matching, mỗi step = 1 recall
  → = "Tính nhanh" = ÍT steps (chunks compiled lớn)
  → = "Tính chậm" = NHIỀU steps (chunks nhỏ, phải tách)

  SEQUENTIAL LIMIT:
    → Mỗi step: output hold 1 slot → ÍT slots cho search terms
    → Chuỗi 5+ steps → PFC HẾT slots → CẦN giấy / tools
    → = Tại sao toán phức tạp CẦN viết ra — PFC alone KHÔNG đủ

  VẬY "TÍNH" THẬT SỰ Ở ĐÂU:
    Level NEURON: CÓ (voltage threshold → fire/not) = PHYSICS
    Level CHUNK: KHÔNG (chunk fire hoặc không — pattern match)
    Level PFC: KHÔNG (PFC orchestrate, không compute)
    → = "Tính toán" conscious = ILLUSION — thật ra = chuỗi pattern matching
```

---

## 5. Dao Động — Search Mechanism Cơ Bản

```
🟡 PFC hold 4 chunks → tạo ACTIVATION PATTERN → "sóng" lan database:

  CƠ CHẾ:
    → 4 chunks FIRE cùng lúc → kích hoạt neurons CONNECTED
    → = "Sóng" lan từ 4 điểm → giao nhau ở đâu → ĐÓ là pattern match
    → Giống: ném 4 viên đá vào hồ → sóng giao nhau = hit
    → 🟢 Spreading activation (Collins & Loftus 1975)

  RESONANCE — tinh tế hơn "hit or miss":
    → Chunks ĐÚNG: HẤP THỤ dao động → fire RÕ NÉT → SIGNAL
    → Chunks SAI: dao động PHẢN LẠI → TẠO NHIỄU → NOISE
    → Output = signal-to-noise ratio đủ CAO → chunk rõ nhất = answer

  CORTISOL × CHUNKS:
    Cortisol CAO + ÍT chunks = noise >> signal → RỐI, đau đầu
    Cortisol CAO + NHIỀU chunks = signal >> noise → INSIGHT
    Cortisol THẤP + NHIỀU chunks = signal yếu → "biết nhưng lười nghĩ"
    Cortisol VỪA + NHIỀU chunks = SWEET SPOT → Flow

  → = "Sáng tạo" = chunks đủ + dao động đủ = signal/noise CAO
  → (Chi tiết: Chunk-Search-Advanced.md)
```

---

## 6. Body Evaluate — PFC Tìm, Body Duyệt

```
🟡 PFC search → output emerge → body DUYỆT:

  → PFC present output → body simulate → body check "feel ĐÚNG?"
  → Body-Reward: "HAY!" → PFC giữ output
  → Body-Dissonance: "KỲ KỲ" → PFC discard → search lại
  → Body neutral: "hmm" → PFC hold → tìm thêm data
  → = PFC TÌM, body DUYỆT, PFC CHỌN dựa trên body
  → = "Trực giác" = body evaluate TRƯỚC PFC articulate

  ⚠️ Body evaluate CÓ THỂ SAI (confirmation bias):
    → Body evaluate bằng chunks ĐÃ CÓ → chunks cũ SAI → evaluate SAI
    → Fix: real-check + đa dạng experience → build chunks mới
    → (Chi tiết: Chunk-Practical.md)
```

---

## 7. Attention = Query Design — Chọn TÌM CÁI GÌ

```
🟡 PFC hold 4 terms — nhưng CHỌN 4 terms NÀO?

  ATTENTION = PFC chọn 4 chunks NÀO để search = THIẾT KẾ CÂU HỎI:
    Expert: chọn terms CỤ THỂ → hit NHANH
    Beginner: chọn terms MƠ HỒ → miss hoặc noise
    → = "Hỏi đúng câu hỏi = NỬA đáp án"
    → = "Biết cách tìm" = META-CHUNK compiled qua kinh nghiệm

  ⚠️ EMOTIONAL TAGS = "search term NGẦM" mà PFC không biết:
    → Chunks có EMOTIONAL TAG từ amygdala (nguy hiểm / an toàn / vui / buồn)
    → Emotional state hiện tại BIAS search:
      Đang sợ → chunks tagged [threat] fire MẠNH → thấy nguy hiểm KHẮP NƠI
      Đang vui → chunks tagged [reward] fire MẠNH → thấy cơ hội KHẮP NƠI
    → = PFC TƯỞNG search neutral → emotional tag ĐÃ filter SẴN
    → (Chi tiết: Chunk-Search-Advanced.md)
```

---

## 8. Expert vs Beginner — Cùng PFC, Khác Database + Query

```
🟡 "Thông minh" = database GIÀU + query design TỐT:

  BEGINNER: database NHỎ + query MƠ HỒ → search CHẬM, HẸP
  EXPERT:   database LỚN + query CỤ THỂ → search NHANH, CHÍNH XÁC
  THIÊN TÀI: database CROSS-DOMAIN + query MỚI → hit ở chỗ CHƯA AI THỬ

  → CÙNG PFC (~4 slots) nhưng:
    Beginner: mỗi slot = chunk NHỎ → ít info per search
    Expert: mỗi slot = meta-chunk (§2 hierarchy) → CỰC NHIỀU info per search
    → = "Cùng 4 slots — khác KÍCH THƯỚC mỗi slot"

  → = "Thông minh" KHÔNG phải "PFC mạnh hơn"
  → = "Thông minh" = database lớn + compiled sâu + query design giỏi
  → = TẤT CẢ đều TRAINABLE (không phải talent cố định)
```

---

## 9. Honest Assessment

```
  ESTABLISHED (🟢):
    🟢 Hebbian learning (Hebb 1949)
    🟢 Long-term potentiation (Bliss & Lømo 1973)
    🟢 Flashbulb memories (Brown & Kulik 1977)
    🟢 Memory reconsolidation (Nader 2000)
    🟢 Chunking (Chase & Simon 1973, Miller 1956)
    🟢 Working memory ~4 items (Cowan 2001)
    🟢 Spreading activation (Collins & Loftus 1975)
    🟢 Expert intuition = pattern recognition (de Groot 1946, Klein 1998)
    🟢 Distributed representations (Rumelhart & McClelland 1986)
    🟢 Sleep consolidation (Walker 2017)
    🟢 Savings in relearning (Ebbinghaus 1885)

  FRAMEWORK SUY LUẬN (🟡):
    🟡 "Não = search engine" — consistent với connectionist models
    🟡 "Tính = chuỗi recall" — consistent với ACT-R (Anderson 1993)
    🟡 "4 dimensions = 4 search terms" — consistent với content-addressable retrieval
    🟡 "Resonance signal/noise" — consistent với signal detection theory
    🟡 "Attention = query design" — consistent với biased competition (Desimone 1995)
    🟡 "Emotional tags = hidden search term" — consistent với affect-as-information
    🟡 "Expert = database + query" — consistent với expertise research

  HYPOTHESIS (🔴):
    🔴 "KHÔNG CÓ true computation ở level chunk" — debate ongoing in cognitive science
    🔴 "Resonance" metaphor — neural dynamics phức tạp hơn
    🔴 "Cortisol → sóng rộng → insight" — logical, chưa directly measured
```

---

## 10. Kết Nối

```
→ Chunk-Search-Advanced.md: resonance chi tiết, aha mechanism, incubation, priming, emotional tags
→ Chunk-Practical.md: external tools, transfer, interference, failure modes, ứng dụng
→ Schema-Operations.md §8: PFC simulate (= search + body evaluate)
→ Schema-Operations.md §4: VTA detect biến động (= alert PFC search)
→ PFC-Analysis.md §2: PFC sub-regions (hardware for orchestration)
→ Core-v7.5-Draft.md §4.1.4: cortisol → neurons fire mạnh → cross-connection
→ Personal-Melody.md §6.1: investment cost = BUILD database
→ Melody-Arc.md §4 ①: anchor first = link chunk mới với database CŨ
→ Education-Bridge.md §5.5: mini-arcs = build chunks từ nhỏ → lớn
→ Imagine-Final-Gradient.md §4: nâng level = NẠP chunks THẬT
→ Body-Dissonance.md: dissonance = body signal khi search MISS hoặc CONFLICT
→ Connection.md §3: virtual chunks = access database NGƯỜI KHÁC
```

---

> *Chunk & PFC — "Não không phải máy tính. Não là Google.
> Mỗi lần 'suy nghĩ' = gõ tìm kiếm (4 từ khóa max).
> Kết quả = pattern match từ database chunks đã compiled.
> 'Thông minh' = database lớn + query giỏi.
> 'Sáng tạo' = search terms MỚI → hit ở chỗ chưa ai thử."*
