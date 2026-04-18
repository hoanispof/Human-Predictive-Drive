# Chunk & PFC — Não Không Tính Toán, Não Tìm Kiếm

> **Bạn nghĩ 2+3 thì não "tính" ra 5?**
> Không. Não TÌM trong database: "có pattern nào match [2+3] không?"
> → Tìm thấy chunk [2+3=5] đã compiled → output "5."
> Nếu KHÔNG tìm thấy → tách nhỏ → tìm lại → sequential.
>
> Não = DATABASE + 2 OPERATORS.
> Vô thức = operator CHÍNH (~95%): compile, run, evaluate, process nền.
> PFC = operator PHỤ (~5%): search, hold, direct — nhưng quyết định HƯỚNG.
>
> File này = CORE mechanism. Chi tiết search: Chunk-Search-Advanced.md.
> Ứng dụng + failure modes: Chunk-Practical.md.

---

> **Trạng thái:** DRAFT — hypothesis từ framework + neuroscience foundations
> **Ngày:** 2026-03-28
> **Reference:** Schema-Operations.md, PFC-Analysis.md, Core-v7.5-Draft.md §5
> **Quy ước:** 🟢 Research support | 🟡 Suy luận từ framework | 🔴 Hypothesis

---

## 1. Chunk Là Gì — Ở Level Neuron

```
🟢 CHUNK = nhóm neurons đã WIRE TOGETHER → fire thành 1 ĐƠN VỊ:

  🟢 Hebb (1949): "Neurons that fire together, wire together"

  CHƯA compiled (neurons rời):
    Thấy số "3" lần đầu:
      → Nhóm A: hình dạng "3" (visual cortex)
      → Nhóm B: âm "ba" (auditory cortex)
      → Nhóm C: ý nghĩa "số lượng 3" (association cortex)
      → = 3 nhóm RIÊNG LẺ → PFC phải hold CẢ 3 → tốn 3 dimensions

  ĐÃ compiled (neurons wired):
    Thấy số "3" lần thứ 1000:
      → Nhóm A+B+C đã WIRE thành 1 UNIT
      → Fire 1 = biết hết (hình + âm + nghĩa) → tốn 1 dimension
      → = "Chunk" = compressed package

  CHUNK vs SCHEMA:
    → Chunk = ATOM (1 đơn vị, không có purpose riêng)
    → Schema = MOLECULE (nhiều chunks linked → có PURPOSE/FUNCTION)
    → VD: chunk [đạp phanh]. Schema [lái xe] = mạng chunks → PURPOSE: di chuyển
    → Schema chi tiết: Schema.md §1.1

  CHUNK MULTI-MODAL — span NHIỀU cortex:
    → VD: chunk "mẹ" = mặt (visual) + giọng (auditory) + ôm (somatic) + ấm (emotional)
    → Fire 1 phần (nghe giọng mẹ) → KÉO cả chunk fire (nhớ mặt, nhớ ôm,...)
    → 🟢 Distributed representations (Rumelhart & McClelland 1986)
```

---

## 2. Chunk Lifecycle — Tạo, Sửa, Yếu (Không Xóa)

```
🟡 4 CÁCH COMPILE (tạo chunk mới):

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
    → ⭐ BINDING MECHANISM (Neural-Processing-Flow.md §4): multi-modal compile
      cần BINDING giữa cortical areas — 5 cơ chế đồng thời:
      gamma sync ~40Hz (Singer 1995), multisensory neurons (Stein 1993),
      convergence zones (Parietal/STS/Insula), amygdala tagging, DMN scaffolding.
      Binding = emergent, không có single binder.

  ④ SLEEP CONSOLIDATION — ngủ compile offline:
    → Hippocampus REPLAY → strengthen hoặc prune
    → 🟢 Sleep consolidation (Walker 2017)


  CHUNK HIERARCHY — chunk CHỨA sub-chunks:
    Beginner lái xe: [lái]+[phanh]+[mirror]+[signal] = 4 chunks RIÊNG → PFC quá tải
    Expert lái xe: [LÁI XE] = 1 meta-chunk → fire 1 = tất cả auto → PFC freed
    → = Expert: 1 PFC slot = 1 meta-chunk = CỰC NHIỀU operations

  RECONSOLIDATION — sửa chunk đã compiled:
    → Khi chunk được RECALL → TẠM THỜI unstable (~vài giờ)
    → Trong window đó → CÓ THỂ modify → re-compile
    → = Therapy: recall trauma → reframe → re-compile = bớt đau
    → ⚠️ Recall MÀ KHÔNG modify → chunk STRENGTHEN → TỆ HƠN
    → 🟢 Memory reconsolidation (Nader 2000)

  DECAY — không dùng yếu dần:
    → "Quên" ≠ mất → "quên" = retrieval path YẾU
    → Re-exposure → "ồ NHỚ RỒI!" = path reactivate
    → Chunk compiled SÂU (childhood, emotional) = gần như không decay
    → 🟢 Savings in relearning (Ebbinghaus 1885)

  ⚠️ KHÔNG AI XÓA ĐƯỢC CHUNK:
    → Không có cơ chế "unwire" chủ động
    → Chunk chỉ: STRENGTHEN / WEAKEN / MODIFY — KHÔNG delete
    → = "Bỏ thói cũ" ≠ xóa → = chunk MỚI compile ĐỦ MẠNH → ĐÈ chunk cũ
    → = Stress → PFC yếu → chunk cũ CÓ THỂ fire lại ("tái phát khi mệt")
```

---

## 3. Hai Operator — Vô Thức Chính, PFC Phụ

```
🟡 CHUNK = DATA. Hai operator làm việc với CÙNG database:


  ⭐ VÔ THỨC = OPERATOR CHÍNH (~95% processing):

    COMPILE tự động: experience → neurons fire cùng → wire → chunk hình thành
      → KHÔNG CẦN PFC → body TỰ wire
      → = Đa số chunks = vô thức compile (không phải PFC tạo)

    RUN compiled schemas tự động: trigger match → schema fire → hành vi tự động
      → VD: thấy chó → chạy. Cầm đũa → ăn. PFC KHÔNG tham gia.

    EVALUATE qua body signals:
      → Body-Reward: "hay!" / Body-Dissonance: "kỳ kỳ" / Body-Satisfaction: "đủ"
      → Vô thức evaluate TRƯỚC PFC biết (body feel trước PFC label)

    PROCESS NỀN: đi bộ → sắp xếp chunks. Ngủ → hippocampus replay → consolidate.
      → = "Sáng mai rõ hơn" = vô thức ĐÃ xử lý trong đêm

    STRENGTHEN/WEAKEN tự động: dùng nhiều → mạnh. Không dùng → yếu (Hebbian).


  ⭐ PFC = OPERATOR PHỤ (~5% — nhưng quyết định HƯỚNG):

    SEARCH: hold 4 search terms → tìm chunks match
    HOLD: giữ chunks active (4 modes — xem §4)
    CREATE: imagine chunk MỚI → body check → compile
    MODIFY: recall → window unstable → thay đổi → re-compile
    DIRECT: chọn attention → quyết định chunks NÀO fire

    → = Vô thức xây nhà (95%), PFC chọn XÂY Ở ĐÂU (5%)
    → = CEO quyết định direction → team execute


  PHỐI HỢP 3 VAI:
    PFC chỉ hướng: "TÌM CÁI NÀY" (hold search terms)
    Vô thức tìm: spreading activation → match → "đây này!"
    Body duyệt: evaluate kết quả → "đúng!" hoặc "kỳ kỳ"
    PFC chọn: dựa trên body → giữ hoặc tìm tiếp

    VTA = alert system: vô thức detect mismatch → alert PFC → "ồ, cái gì?"
      → = Nhân viên thấy vấn đề → gọi sếp → sếp xử lý


  ⭐ GIỚI HẠN CƠ BẢN — mỗi operator CÓ THỂ và KHÔNG THỂ gì:

    VÔ THỨC CÓ THỂ:
      → Detect: body-base smooth hay không (current state)
      → Compile: patterns từ experience (match/mismatch)
      → Run: compiled schemas tự động
      → Tạo Imagine-Final: expectation patterns ở MỌI scale
        (micro: "vài giây tới" → long: "hướng đời" — Imagine-Final.md §1)
      → Check Imagine-Final BODY-BASE: "reality có match expectation không?"
      → Trả thưởng/phạt: opioid khi match, cortisol khi mismatch
      → = Giỏi: "BÂY GIỜ body thấy thế nào?" + "CÓ ĐÚNG HƯỚNG không?"
        → Trả lời NGAY, CHÍNH XÁC — ở mức BODY-BASE

    VÔ THỨC KHÔNG THỂ:
      → Check: "smooth NÀY có đúng với domain không?"
      → Simulate: "5 năm sau có sao không?"
      → Compare: "body thích nhưng THẬT SỰ hợp không?"
      → = Vô thức CHỈ ĐO body-base → KHÔNG ĐO domain accuracy
      → = Nếu body sướng → vô thức nói "OK" → DÙ domain có thể SAI
      → VD: nghiện = body sướng → vô thức "OK" → domain PHẠT
      → VD: limerence = body cực sướng → vô thức "hoàn hảo" → chưa test domain

    PFC CÓ THỂ (mà vô thức KHÔNG):
      → Simulate tương lai: "nếu tiếp tục → kết quả gì?"
      → So sánh ký ức: "lần trước pattern này → kết quả tệ"
      → Check domain: "body thích NHƯNG thực tế có bền không?"
      → Check Imagine-Final DOMAIN: "body muốn hướng này → domain có cho phép?"
        → = Vô thức CÓ Imagine-Final nhưng KHÔNG check domain accuracy
        → = PFC là HỆ THỐNG DUY NHẤT verify: Imagine-Final có khả thi không
      → Chọn giữa competing Imagine-Finals: ngắn hạn vs dài hạn
      → Tạo chunks evaluative MỚI → NẠP VÀO vô thức → UPDATE database
      → = PFC "DẠY" vô thức cái mà vô thức tự KHÔNG THỂ biết

    PFC KHÔNG THỂ (mà vô thức CÓ):
      → Feel trực tiếp: PFC KHÔNG cảm nhận → phải NHẬN từ body
      → Process 95% nền: PFC bandwidth quá nhỏ cho toàn bộ
      → Compile tự động: PFC chỉ draft → vô thức mới compile thật

    → = VÔ THỨC: giỏi "bây giờ body thế nào" (state detection)
    → = PFC: giỏi "bây giờ có ĐÚNG với thực tế không" (domain check)
    → = CẦN CẢ HAI: vô thức feel + PFC verify = "melody hay" (Personal-Melody §5)
    → = TẮT PFC = mất bộ CHECK DOMAIN DUY NHẤT → body-base unchecked
      (VD: limerence, nghiện, comfort zone — chi tiết: Love-Analysis.md)

    → Ở ĐỘNG VẬT: vô thức ĐỦ DÙNG (domain đơn giản, body-base calibrate tốt qua evolution)
    → Ở CON NGƯỜI: domain PHỨC TẠP hơn body-base calibrate được (~10% lệch)
      → PFC tiến hóa ĐỂ BÙ 10% đó → PFC = bộ check domain mà vô thức THIẾU
```

---

## 4. PFC Search — 4 Modes + Cortisol Amplify

```
🟡 PFC search = hold chunks → spreading activation = sóng CÓ HƯỚNG.

  PFC hold 4 chunks → sóng lan database → giao nhau ở đâu = hit
  → 🟢 Spreading activation (Collins & Loftus 1975)
  → 🟢 Working memory ~4 items (Cowan 2001)


  ⭐ 4 MODES — cách PFC hold KHÁC → output KHÁC:

    QUICK SEARCH (giây — recall xong quên):
      PFC hold [2+3] → hit [5] → RELEASE → quên
      Cortisol: không tăng (quá nhanh)
      VD: nhớ tên, tính nhẩm, lookup thông tin
      → "Tính" = CHUỖI quick searches: (1+2)+4 → [1+2=3] recall → [3+4=7] recall

    BODY NOVELTY (vô thức thuần — PFC KHÔNG tham gia):
      External input → body fire TỰ ĐỘNG → dopamine → "thú vị!"
      PFC KHÔNG hold → body TỰ absorb → không cần "nghĩ"
      VD: trẻ vào cửa hàng đồ chơi, cặp đôi ở CÙNG nhau calibrate melody
      = INPUT-DRIVEN: cơ chế CỔ NHẤT (mọi động vật có)

    LOOSE HOLD (phút-giờ — vừa đi vừa nghĩ):
      PFC hold NHẸ [vấn đề] → body RELAX (đi bộ, tắm)
      Sóng GENTLE, lan RỘNG nhưng NHẸ → insight BẤT NGỜ
      CÓ THỂ thả bất kỳ lúc nào → KHÔNG có threat
      VD: Archimedes bồn tắm, Einstein đi bộ, cặp đôi xa nhau nhớ nhau
      = CREATIVE mode → Novelty-dominant THƯỜNG ở mode này
      → Phát sinh TRỰC TIẾP từ curiosity, HOẶC từ active lock NỚI

    ACTIVE LOCK (giờ-ngày — ép body thực thi):
      = LOOSE HOLD + THREAT gắn vào → biến loose thành LOCK
      → "Sợ quên idea" / "Deadline mai" / "Để lâu càng lười" = threat
      → THREAT khiến PFC KHÔNG THỂ thả → phải HOÀN THÀNH
      → Body BỊ ÉP align → LÀM hoặc double dissonance
      = EXECUTION mode — "vừa chơi vừa lo" = PFC lock + body chơi = WORST
      → Fix: LÀM (alignment) hoặc GHI RA GIẤY (remove "sợ quên" → release)
      → 🟢 Zeigarnik Effect (1927)

  ⭐ THREAT = CÔNG TẮC loose ↔ lock:
    LOOSE + threat = LOCK. LOCK − threat = LOOSE.
    CEO giỏi = TOGGLE đúng lúc + đúng mức:
      BẬT khi execute / TẮT khi creative / TINH CHỈNH: vừa = productive, quá = freeze
    → (Novelty-Loop.md §3.2, Threat-Drive-Analysis.md §12)


  ⭐ CORTISOL = VOLUME LOA (amplifier, KHÔNG phải driver):

    PFC = người gõ search (TÌM GÌ). Cortisol = volume (tìm MẠNH cỡ nào).
    → KHÔNG phải "cortisol TẠO dao động" → mà "cortisol AMPLIFY search"

    Cortisol THẤP: sóng yếu → hit ít → "biết nhưng lười nghĩ"
    Cortisol VỪA: sóng vừa → hit rõ + noise thấp → SWEET SPOT (flow)
    Cortisol CAO + NHIỀU chunks: sóng mạnh + hits nhiều → INSIGHT cross-domain
      VD: Einstein → physics+toán+triết → hit chéo → E=mc²
    Cortisol CAO + ÍT chunks: sóng mạnh + không gì match → NOISE, RỐI
      VD: sinh viên năm nhất → stress → "rối, đau đầu"

    → = CÙNG căng thẳng → GIỎI ra insight, MỚI ra rối
    → = Không "căng thẳng tốt/xấu" → mà "căng thẳng + CHUNKS cỡ nào"


  ⭐ KẾT QUẢ — chunks SÁNG hay không:

    Sóng tới chunk KHỚP → chunk SÁNG → "ồ, cái này!"
    Sóng tới chunk KHÔNG khớp → lướt qua

    VD hit: [game+combat+nhạc+2 bên] → [rhythm game] SÁNG + [side-scroll] SÁNG
      → "Rhythm combat side-scroll!" = INSIGHT

    VD miss: [kiếm tiền+nhanh+ít vốn] → KHÔNG gì sáng
      → "Nghĩ mãi không ra" = database THIẾU

  → = "Sáng tạo" = PFC hold ĐÚNG + cortisol ĐỦ + chunks MATCH
  → (Chi tiết: Chunk-Search-Advanced.md)
```

---

## 5. Body Evaluate — PFC Tìm, Body Duyệt

```
🟡 PFC search → output emerge → body DUYỆT:

  → Body-Reward: "HAY!" → PFC giữ
  → Body-Dissonance: "KỲ KỲ" → PFC search lại
  → Body neutral: "hmm" → PFC hold → tìm thêm data
  → = "Trực giác" = body evaluate TRƯỚC PFC articulate

  ⚠️⚠️⚠️ "FEEL MƯỢT" ≠ "ĐÚNG":

    Body evaluate bằng chunks ĐÃ CÓ → chunks sai → evaluate SAI

    3 cấp: cá nhân bias → nhóm bias → toàn cầu bias
      VD toàn cầu: "cortisol = stress" → ngàn papers → "hiển nhiên" → thật ra giản lược

    MƯỢT GIẢ: mâu thuẫn → DISMISS → mãi mâu thuẫn ngầm
    MƯỢT THẬT: mâu thuẫn → FIX → mượt HƠN → thấy mâu thuẫn MỚI sâu hơn → fix tiếp

    Fix: real-check, đa dạng input, challenge, honest assessment 🟡🔴
    → (Chi tiết: Chunk-Practical.md)
```

---

## 6. Attention = Query Design

```
🟡 PFC hold 4 terms — nhưng CHỌN 4 terms NÀO?

  ATTENTION = thiết kế CÂU HỎI:
    Expert: terms CỤ THỂ → hit NHANH
    Beginner: terms MƠ HỒ → miss
    → = "Hỏi đúng câu hỏi = NỬA đáp án"
    → = "Biết cách tìm" = META-CHUNK compiled qua kinh nghiệm

  ⚠️ EMOTIONAL TAGS = search term NGẦM:
    Chunks có TAG từ amygdala → emotional state BIAS search:
    Đang sợ → chunks [threat] fire MẠNH → thấy nguy hiểm KHẮP NƠI
    Đang vui → chunks [reward] fire MẠNH → thấy cơ hội KHẮP NƠI
    → = PFC TƯỞNG neutral → emotional tag ĐÃ filter SẴN
    → (Chi tiết: Chunk-Search-Advanced.md)
```

---

## 7. Expert vs Beginner — Cùng PFC, Khác Database

```
🟡 "Thông minh" = database GIÀU + query TỐT:

  BEGINNER: database NHỎ + query MƠ HỒ → CHẬM, HẸP
  EXPERT:   database LỚN + query CỤ THỂ → NHANH, CHÍNH XÁC
  THIÊN TÀI: database CROSS-DOMAIN + query MỚI → hit CHƯA AI THỬ

  → CÙNG PFC (~4 slots):
    Beginner: slot = chunk NHỎ → ít info
    Expert: slot = meta-chunk → CỰC NHIỀU info
    → = "Cùng 4 slots — khác SIZE mỗi slot"

  → = "Thông minh" = database + compiled depth + query skill
  → = TẤT CẢ TRAINABLE (không phải talent cố định)
```

---

## 8. Honest Assessment

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
    🟢 Zeigarnik Effect (1927)

  FRAMEWORK SUY LUẬN (🟡):
    🟡 "Não = search engine" — consistent với connectionist models
    🟡 "Tính = chuỗi recall" — consistent với ACT-R (Anderson 1993)
    🟡 "4 modes hold" — consistent với working memory + incubation research
    🟡 "Vô thức chính (~95%), PFC phụ (~5%)" — consistent với
        unconscious processing literature (Dijksterhuis 2004)
    🟡 "Threat = công tắc loose↔lock" — consistent với Zeigarnik + motivation
    🟡 "Cortisol = amplifier" — consistent với arousal × performance
    🟡 "Không xóa chunk" — consistent với memory persistence research
    🟡 "Attention = query design" — consistent với biased competition
    🟡 "Emotional tags = hidden search" — consistent với affect-as-information
    🟡 "Feel mượt ≠ đúng" — consistent với confirmation bias literature
    🟡 "Vô thức chỉ đo body-base, PFC đo domain" — consistent với
        somatic marker hypothesis (Damasio): body = heuristic, not perfect (~90%)
        + dual process theory (Kahneman): System 1 fast/heuristic, System 2 slow/analytical
    🟡 "PFC dạy vô thức qua chunks evaluative" — consistent với
        deliberate practice → compiled expertise (Ericsson)
    🟡 "Động vật đủ vô thức, con người cần PFC thêm" — consistent với
        PFC expansion across species + domain complexity increase

  HYPOTHESIS (🔴):
    🔴 "KHÔNG CÓ true computation ở level chunk" — debate ongoing
    🔴 "~95%/5% split" — ước lượng, chưa đo chính xác
    🔴 "Cortisol AMPLIFY search" — logical nhưng chưa directly measured
```

---

## 9. Kết Nối

```
→ Chunk-Search-Advanced.md: resonance, aha, incubation, priming, emotional tags
→ Chunk-Practical.md: tools, transfer, interference, failure modes, ứng dụng
→ Schema.md §1.1: schema = mạng chunks có purpose (3 trạng thái)
→ Schema-Operations.md §8: PFC simulate = search + body evaluate
→ Schema-Operations.md §4: VTA detect biến động
→ PFC-Analysis.md §2: PFC sub-regions
→ Core-v7.5-Draft.md §3: Cortisol-Baseline (7 modes, amplifier)
→ Personal-Melody.md §5: "melody hay" = body-base smooth + domain accurate (cần CẢ HAI operator)
→ Personal-Melody.md §6.1: investment cost = build database
→ Love-Analysis.md §3: limerence = PFC suppress → mất domain check → body-base unchecked
→ Why-Body-Knows.md: body ~90% đúng → 10% sai = chỗ PFC CẦN bù
→ Melody-Arc.md §4: anchor first, mini-arc
→ Education-Bridge.md §5.5: arc design cho learning
→ Imagine-Final.md §4: nạp chunks THẬT
→ Body-Dissonance.md: dissonance = body signal khi mismatch
→ Connection.md §3: virtual chunks = access database NGƯỜI KHÁC
→ Novelty-Loop.md §3.2: threat = sàn giữ loop (threat toggle)
→ Threat-Drive-Analysis.md §12: threat-drive tốt khi nào
```

---

> *Chunk & PFC — "Não = database + 2 operators.
> Vô thức xây 95% (compile, run, evaluate). PFC chỉ 5% (search, hold, direct).
> Nhưng 5% đó quyết định HƯỚNG. 'Thông minh' = database lớn + query giỏi.
> 'Sáng tạo' = search terms MỚI → hit ở chỗ chưa ai thử.
> Threat = công tắc: bật → ép làm, tắt → creative. Toggle đúng lúc = CEO giỏi."*
