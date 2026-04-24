---
title: Status — Observation Parameter
version: 1.0
created: 2026-04-20
status: OBSERVATION PARAMETER v1.0
scope: |
  OBSERVATION FILE: Status = named pattern khi quan sát self-assessment
  chunk networks + hormonal baseline trong social context.
  Status không phải component hay operator — là TÊN GỌI cho patterns
  emergent từ body-level social scan + compiled schema access maps.
  File này mô tả: Schema Access Map (core redefine), body scan mechanism,
  3 modes tương tác, position vs aspiration, serotonin = certainty bias,
  chunk dynamics mapping, cortisol interaction, honest assessment.
purpose: |
  Core v7.8 §8 define Status ngắn gọn ("Self-assessment chunk patterns
  + hormonal baseline"). File này DEEP-DIVE: tại sao status ≠ hierarchy,
  mechanism scan vô thức, 3 modes, 2 tham số tách biệt, serotonin
  = certainty bias nền (NOT decision maker), chunk dynamics khi status
  thay đổi, cortisol vicious cycle, quân đội case study.
  Đặc biệt: honest assessment về serotonin research limitations.
position: |
  Core-Deep-Dive/Observation/ — ngang hàng Novelty.md, Threat.md, Drive.md,
  Boredom.md, Empathy.md, Connection.md, Schema.md, AI-Schema-Detection.md,
  Liking-Wanting.md. Tất cả = observation parameter deep-dives.
dependencies:
  - Core-v7.8-Draft.md — cycle architecture, §8 observation parameters
  - Body-Feedback-Mechanism.md — Chunk-Shift/Miss/Gap, compound mechanism
  - Chunk.md v2.0 — chunk substrate, compilation, hierarchy
  - Agent.md — SPM mechanism, §12 body-need feeder
  - Connection.md v1.0 — overlap analysis (belonging ≠ connection)
  - Threat.md v1.0 — social threat, imposed threat
  - Cortisol-Baseline.md v2.0 — amplifier, vicious cycle
  - Feeling.md v2.0 — PFC observation interface
  - Valence-Propagation.md v1.1 — body evaluation, chain propagation
sources_backup: |
  Rewrite từ: Status-Analysis-v2.md (656L, 2026-03-23, v7.5-era)
  Backup: _backup/Status-Analysis-v2-v75-era.md
language: Tiếng Việt primary + English technical terms
confidence: 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
---

# Status — Observation Parameter

> Gặp sếp → tự động khúm núm. Gặp em mới → tự động thoải mái.
> Gặp bạn thân → dám nói thẳng. Gặp người lạ → dè dặt từng chữ.
>
> Mainstream gọi tất cả là "social hierarchy" — ai cao hơn ai.
> Nhưng hierarchy chỉ giải thích quân đội, công ty (rank rõ ràng).
> KHÔNG giải thích: gia đình, người yêu, bạn bè, hay tại sao CÙNG NGƯỜI
> mà ở chỗ này tự tin, chỗ kia rụt rè.
>
> Framework redefine: Status = Schema Access Map.
> "Với NGƯỜI NÀY, trong CONTEXT NÀY: schemas nào SẴN SÀNG, schemas nào BỊ BLOCK?"
>
> Không phải 1 con số. Là bản đồ DYNAMIC — thay đổi theo từng người × từng context.
> Body scan vô thức trong milliseconds: ai hơn gì, tôi hơn gì, trao đổi được gì.
> Kết quả scan = danh sách schemas sẵn sàng triển khai.
>
> Hierarchy = trường hợp ĐẶC BIỆT ĐƠN GIẢN NHẤT (1 chiều cao/thấp).
> Schema Access Map = trường hợp TỔNG QUÁT (nhiều chiều, per-person, per-context).
>
> File này phân tích: Status trông thế nào, mechanism bên dưới,
> 3 modes tương tác, 2 tham số tách biệt (position vs aspiration),
> serotonin = certainty bias (KHÔNG phải decision maker),
> chunk dynamics khi status thay đổi, và tại sao "giảm stress"
> thường không fix được vấn đề status thực sự.

---

## Mục lục

- §0 — VỊ TRÍ: OBSERVATION PARAMETER
- §1 — STATUS LÀ GÌ: SCHEMA ACCESS MAP
- §2 — CƠ CHẾ SCAN: BODY VÔ THỨC
- §3 — STATUS GAP → 3 MODES TƯƠNG TÁC
- §4 — POSITION VS ASPIRATION: 2 THAM SỐ
- §5 — BEING SEEN: STATUS CALIBRATION FUNCTION
- §6 — BELONGING: CACHED STATUS MAPS
- §7 — SEROTONIN: CERTAINTY BIAS NỀN
- §8 — FLEXIBILITY + CONTEXT SWITCH
- §9 — STATUS × CHUNK DYNAMICS
- §10 — STATUS × CORTISOL
- §11 — STATUS × OTHER OBSERVATION PARAMETERS
- §12 — QUÂN ĐỘI: STATUS OPTIMIZATION CASE STUDY
- §13 — STATUS TRONG TẬP THỂ
- §14 — HONEST ASSESSMENT + CÂU HỎI MỞ
- §15 — CROSS-REFERENCES

---

## §0 — VỊ TRÍ: OBSERVATION PARAMETER

```
⭐ REFRAME V7.8:

  Core v7.5 (cũ): Status = "L3 Drive" — 1 trong 3 drives xã hội
  Core v7.8 (mới): Status = observation parameter — tên gọi cho pattern

  Status KHÔNG PHẢI:
    ✗ Component kiến trúc (không có "Status module" trong não)
    ✗ Drive operator (không có "Status engine" bật/tắt)
    ✗ Layer riêng (không có "L3 Status" — layer-model đã bỏ)
    ✗ Personality trait "tự tin" (pop psychology — mô tả, không giải thích)

  Status LÀ:
    ○ Tên gọi cho pattern observable: self-assessment chunk networks
      + hormonal baseline → behavior per-person per-context
    ○ Emergent từ body-level social scan + compiled schema access maps
    ○ Có giá trị mô tả + predict + communicate
    ○ KHÔNG phải mechanism — mechanism nằm ở chunks + body-feedback

  CROSS-SPECIES:
    Ở động vật: hormone → status behavior trực tiếp (khỉ: serotonin ↔ rank)
    Ở con người: hormone → chunk processing → status behavior
    = Cùng function, nhưng chunk system phức tạp → OVERRIDE hormone đáng kể
    = Giải thích: người nghèo vẫn tự tin (PFC + chunks override serotonin thấp)

  VỊ TRÍ TRONG CYCLE (Core-v7.8-Draft.md §1):
    Domain (social context)
      → Body-Input (social scan signals: posture, voice, gaze)
        → Unconscious (status chunks activate, schema access maps load)
          → Feeling (tự tin / rụt rè / bất an)
            → PFC (evaluate: dám thử không?)
              → Body-Output (behavior: comply / trao đổi / lấy)
                → Domain (social outcome → update status chunks)

  → Status = observation parameter trên toàn cycle
  → Không nằm ở 1 step — observe ACROSS cycle
```

---

## §1 — STATUS LÀ GÌ: SCHEMA ACCESS MAP

```
⚠️ QUAN TRỌNG: "Status" trong framework ≠ "social hierarchy" thông thường.

NÓI GỌN NHẤT:
  Status = calibrate "schemas NÀO được phép chạy" khi gặp người cụ thể
  = Schema Access Map

  Hierarchy (hiểu biết phổ biến) = chỉ 1 CHIỀU: cao/thấp
    "Tôi rank 5, họ rank 8" → tôi thấp hơn → comply
    → Giải thích: quân đội, công ty (rank rõ ràng)
    → KHÔNG giải thích: gia đình, người yêu, bạn bè, context switch

  Framework Status = NHIỀU CHIỀU:
    "Với NGƯỜI NÀY: tôi ôm được, nhưng không ra lệnh được,
     có thể nhờ giúp nhưng phải hỏi lịch sự,
     nếu cần kỹ thuật thì tôi hơn nên có thể đề xuất"
    → NHIỀU schema calibrate ĐỒNG THỜI, không phải 1 số duy nhất
    → Giải thích: MỌI tương tác (quân đội + gia đình + người yêu + người lạ)

  → Hierarchy = trường hợp ĐẶC BIỆT ĐƠN GIẢN NHẤT của Status
    (khi context flatten thành 1 chiều: rank)

DEFINITION V7.8:
  Status = self-assessment chunk patterns + hormonal baseline
  (Core-v7.8-Draft.md §8)

  Cụ thể:
    ① Self-assessment chunk patterns:
       → Compiled maps: "với người A tôi dám gì / không dám gì"
       → Per-person × per-context (KHÔNG phải global)
       → Update qua experience: thắng/thua, được/mất công nhận
       → = Schema Access Map (maps nào MỞ, maps nào ĐÓNG)

    ② Hormonal baseline:
       → Serotonin nền = certainty bias (§7 chi tiết)
       → Carry across contexts (serotonin không đổi khi switch context)
       → Thay đổi chậm (tuần → tháng)
       → = "NHÌN CHUNG tôi tự tin thế nào" (bias, không phải quyết định)

  DYNAMIC, KHÔNG TĨNH:
    ✅ Thay đổi theo từng người gặp × từng context
    ✅ Mỗi người gặp = 1 bản đồ KHÁC
    ✅ Bidirectional: tôi→họ VÀ họ→tôi cùng lúc
    ✅ Body-level: vô thức scan, không cần PFC quyết định
    ✅ Mọi động vật xã hội có (baboon, gà, sói, cá)
```

### §1.1 — Tại sao "Schema Access Map" chứ không phải "Hierarchy"

```
🟡 SCHEMA ACCESS MAP GIẢI THÍCH ĐƯỢC NHỮNG GÌ HIERARCHY KHÔNG THỂ:

  ① Cùng người, khác context:
     Hierarchy: anh A rank 5 (cố định)
     Schema Access Map: anh A ở cty = map X | ở nhà = map Y | ở nhà thờ = map Z
     → 3 maps KHÁC NHAU cho CÙNG 1 người

  ② Nhiều chiều cùng lúc:
     Hierarchy: tôi > họ hoặc tôi < họ (1 chiều)
     Schema Access Map: kỹ thuật tôi > họ, gia đình họ > tôi,
       thể chất ngang nhau, tài chính tôi < họ
     → Nhiều schemas MỞ/ĐÓNG KHÁC NHAU đồng thời

  ③ Gia đình — hierarchy phá sản:
     Vợ rank cao hơn chồng? Chồng rank cao hơn vợ? → KỲ QUẶC
     Schema Access Map: vợ dám chê bếp chồng (map: cooking expertise),
       chồng dám đề xuất đi chơi (map: social initiative),
       cả hai dám ôm nhau (map: intimacy — MUTUAL)
     → Mỗi domain = 1 map riêng, không cần xếp rank

  ④ Context switch giải thích tự nhiên:
     Hierarchy: rank thay đổi → khó giải thích (rank "di chuyển"?)
     Schema Access Map: PFC load map khác (compiled sẵn) → tự nhiên
     → "Switch context" = switch maps, không phải "thay đổi rank"

  → Schema Access Map SUBSUME hierarchy (hierarchy = 1 trường hợp đặc biệt)
  → Chính xác hơn, linh hoạt hơn, giải thích nhiều hơn
```

---

## §2 — CƠ CHẾ SCAN: BODY VÔ THỨC

```
🟢 KHI GẶP 1 NGƯỜI, BODY VÔ THỨC SCAN (milliseconds → seconds):

  ① HỌ HƠN TÔI CÁI GÌ?
     → Sức mạnh? Skill? Kiến thức? Resource? Network?
     → = "Họ CÓ GÌ mà tôi cần/muốn"
     → Input: visual cues (posture, clothing, gaze direction),
       auditory (voice tone, confidence), context (setting, role)

  ② TÔI HƠN HỌ CÁI GÌ?
     → Sức mạnh? Skill? Kiến thức? Resource?
     → = "Tôi CÓ GÌ mà họ cần/muốn"
     → Input: compiled self-assessment chunks + domain chunks

  ③ TÔI CÓ THỂ NHẬN GÌ TỪ HỌ?
     → Không cần trả gì? (tôi >> họ)
     → Phải trao đổi? (ngang hàng)
     → Phải xin? (tôi << họ)

  ④ HỌ CÓ THỂ NHẬN GÌ TỪ TÔI?
     → Tôi có thể từ chối? (ngang/trên)
     → Tôi không thể từ chối? (dưới)

  ⑤ CÓ THỂ TRAO ĐỔI KHÔNG?
     → "Tôi muốn ôm, họ cũng muốn" → schema "ôm" SẴN SÀNG
     → "Tôi muốn ôm, họ không muốn" → schema "ôm" BỊ BLOCK

  KẾT QUẢ SCAN = Schema Access Map cho NGƯỜI NÀY:
    → Danh sách schemas SẴN SÀNG
    → Danh sách schemas BỊ BLOCK
    → = Status Position VỚI NGƯỜI NÀY (không phải chung chung)

  🟢 BODY-LEVEL, KHÔNG CẦN PFC:
    Scan này xảy ra VÔ THỨC — giống cách body biết "nóng" → rụt tay.
    PFC chỉ can thiệp KHI: kết quả scan mơ hồ hoặc cần override
    ("biết là sếp nhưng quyết định cãi vì đúng").
    Scan speed × accuracy tùy: compiled chunks (quen = nhanh + chính xác)
    vs chưa compiled (lạ = chậm + tốn PFC).
```

### §2.1 — Scan mechanism: chunk-based

```
🟡 SCAN KHÔNG PHẢI "TÍNH TOÁN" — LÀ CHUNK PATTERN MATCHING:

  Gặp người → visual/auditory/context inputs fire
    → Spreading activation qua compiled status chunks
      → Chunks match → map LOAD nhanh (quen: ms)
      → Chunks không match → PFC draft new map (lạ: seconds → minutes)

  Quen (compiled maps):
    Gặp vợ → map VỢ compiled → load → vô thức biết "ở đây tôi thế nào"
    → PFC cost ≈ zero (giống lái xe đường quen)

  Lạ (chưa compiled):
    Gặp sếp mới → không có map → PFC scan:
      Visual cues → estimate domain expertise
      Voice cues → estimate confidence
      Context → estimate authority
    → PFC DRAFT temporary map → cortisol tăng nhẹ (uncertainty)
    → Qua vài lần gặp → map COMPILE → lần sau = vô thức
    → = Giải thích "ngày đầu đi làm mệt" = PFC drafting maps liên tục

  Nhiều người cùng lúc:
    Party 20 người lạ → 20 maps cần draft → PFC OVERLOAD
    → Cortisol tăng → mệt → muốn về
    → = Giải thích introvert "sợ party" = PFC cost quá cao cho scan
    → Party bạn quen → maps compiled → PFC cost thấp → thoải mái
```

---

## §3 — STATUS GAP → 3 MODES TƯƠNG TÁC

```
🟡 STATUS QUYẾT ĐỊNH MỌI TƯƠNG TÁC — từ ôm tới chiến tranh:

  Schema Access Map scan xong → GAP giữa tôi và họ → 3 MODES:

  ┌──────────────────────────────────────────────────────────────┐
  │ Status gap            │ Mode         │ Schema sẵn sàng       │
  ├───────────────────────┼──────────────┼────────────────────────┤
  │ TÔI >> HỌ (gap lớn)  │ LẤY          │ Ra lệnh, kiểm soát,   │
  │                       │              │ lấy mà không trả       │
  ├───────────────────────┼──────────────┼────────────────────────┤
  │ TÔI ≈ HỌ (ngang)     │ TRAO ĐỔI     │ Negotiate, cùng cho   │
  │                       │              │ nhau, tương hỗ         │
  ├───────────────────────┼──────────────┼────────────────────────┤
  │ TÔI << HỌ (gap lớn)  │ COMPLY       │ Xin, tuân theo,       │
  │                       │              │ cho mà không đòi       │
  └───────────────────────┴──────────────┴────────────────────────┘

  CÁC MODE LÀ SPECTRUM, KHÔNG PHẢI 3 HỘP:
    → Lấy ←→ Trao đổi ←→ Comply = phổ liên tục
    → Mỗi domain có thể nằm KHÁC CHỖ trên phổ
    → Ví dụ: "kỹ thuật tôi >> họ (lấy/dẫn dắt) + xã hội họ >> tôi (comply/học)"

  "TẤN CÔNG" KHÔNG PHẢI DRIVE RIÊNG:
    → Hổ đuổi nai: không "tấn công" — hổ "ăn" (schema "lấy" sẵn sàng vì status >>)
    → 2 đội đánh nhau: cả 2 nghĩ mình >> → CALIBRATE status bằng conflict
    → Kẻ thắng: maps MỞ TOÀN BỘ | Kẻ thua: maps ĐÓNG TOÀN BỘ
    → Thế giới hiện đại: tranh giành bằng rules (kiện tụng, cạnh tranh thương mại)
    → "Tấn công" = extreme case: gap CỰC LỚN → schema "lấy" KHÔNG BỊ CẢN
    → KHÔNG cần "attack drive" riêng — Status COVER toàn bộ spectrum
```

### §3.1 — 3 Modes trong đời thường

```
🟡 ĐỜI THƯỜNG KHÔNG EXTREME — PHẦN LỚN Ở VÙNG TRAO ĐỔI:

  Vợ chồng (ngang):
    → Map: trao đổi sự quan tâm, chia sẻ trách nhiệm
    → Schema sẵn sàng: đề xuất, từ chối nhẹ, negotiate
    → Khi 1 người dominant → map SHIFT → không còn ngang → stress

  Sếp - nhân viên (gap vừa):
    → Map: comply đa số (nghe chỉ đạo), nhưng KHÔNG hoàn toàn
    → Schema sẵn sàng: đề xuất ý kiến (nếu culture cho phép),
      từ chối việc quá sức (tùy compiled map), xin support
    → Modern workplace: gap ĐANG flatten → gần trao đổi hơn comply

  Bạn bè (ngang + domain-specific gap):
    → Map: trao đổi đa chiều
    → Nhưng: domain X bạn A >> tôi (tech) → tôi comply/học
            domain Y tôi >> bạn A (music) → tôi dẫn dắt/cho
    → = Multi-domain maps CHỒNG LÊN → relationship phong phú

  Người lạ (chưa có map):
    → Default: thận trọng (body bias toward safety)
    → PFC draft temporary map dựa trên visual/context cues
    → Qua vài tương tác → maps compile → settle vào 1 trong 3 zones
```

---

## §4 — POSITION VS ASPIRATION: 2 THAM SỐ

```
🟡 STATUS CÓ 2 THAM SỐ ĐỘC LẬP (không phải 1):

  ① POSITION — "tôi ĐANG ở đâu" (cảm nhận hiện tại):
     → Serotonin baseline = chemical đánh dấu (candidate, §7)
     → Ổn định, thay đổi chậm (tuần → tháng)
     → Body-level (vô thức biết "nhìn chung tôi thế nào")
     → = Certainty bias nền cho toàn hệ thống
     → Carry across contexts (sếp hay nhà → CÙNG baseline)

  ② ASPIRATION — "tôi MUỐN ở đâu" (mong muốn):
     → Chunk patterns predict "nên ở vị trí X"
     → Có thể thay đổi NHANH (so sánh MXH → aspiration tăng vọt)
     → PFC-level (imagine + compare + social input)
     → = Imagine-Final preview cho status tương lai

  GAP = Aspiration - Position:
    Gap > 0: có thể → drive (tích cực) hoặc → threat (tiêu cực)
      → Drive: "tôi muốn lên và có plan" → productive cortisol
      → Threat: "tôi sợ không bao giờ được" → chronic cortisol
    Gap ≈ 0: content (thỏa mãn với vị trí hiện tại)
    Gap < 0: "quá nhiều" → có thể CHO BỚT (hiếm nhưng có thật)
```

### §4.1 — Verify bằng 6 cases

```
  ┌─────────────────────────────┬──────────────────────────────────┐
  │ Case                        │ Analysis                          │
  ├─────────────────────────────┼──────────────────────────────────┤
  │ CEO chase thêm              │ Pos CAO + Asp CAO HƠN → gap > 0 │
  │                             │ → drive tiếp tục ✅               │
  ├─────────────────────────────┼──────────────────────────────────┤
  │ Người nghèo thỏa mãn       │ Pos THẤP + Asp THẤP → gap ≈ 0   │
  │                             │ → content ✅                      │
  ├─────────────────────────────┼──────────────────────────────────┤
  │ Khoe MXH                    │ Pos VỪA + Asp CAO → gap > 0      │
  │                             │ → compensate bằng khoe ✅         │
  ├─────────────────────────────┼──────────────────────────────────┤
  │ Tỷ phú cho hết              │ Pos CAO + Asp THẤP → gap < 0     │
  │                             │ → cho bớt ✅                      │
  ├─────────────────────────────┼──────────────────────────────────┤
  │ Tự tin nội tại              │ Pos VỪA + Asp = Pos → gap = 0    │
  │                             │ → stable ✅                       │
  ├─────────────────────────────┼──────────────────────────────────┤
  │ Công nhân vui vẻ            │ Pos THẤP + Asp THẤP → gap ≈ 0   │
  │                             │ → content ✅                      │
  └─────────────────────────────┴──────────────────────────────────┘

  → Position = body-level (serotonin baseline + compiled chunks)
  → Aspiration = PFC-level (Imagine-Final preview + social comparison)
  → Gap = driver of behavior — nhưng DIRECTION phụ thuộc Imagine-Final quality
```

### §4.2 — MXH và Aspiration Inflation

```
🟡 MXH EXPLOIT cơ chế Aspiration một cách đặc biệt:

  Trước MXH: so sánh với 5-20 người quen → aspiration REALISTIC
  Sau MXH: so sánh với HÀNG NGHÌN curated highlights → aspiration INFLATE

  Cơ chế:
    MXH feed → visual success of others
      → Self-Pattern-Match fires: "họ có X, tôi muốn X"
        → Aspiration TĂNG (PFC imagine "nên ở vị trí đó")
          → Gap tăng → body-feedback dissonance
            → Cortisol tăng nhẹ (uncertainty cho gap)
              → Cortisol suppress serotonin baseline (§10)
                → Position CẢM NHẬN giảm
                  → Gap tăng THÊM → vicious cycle

  → MXH không hạ status TRỰC TIẾP
  → MXH hạ status GIÁN TIẾP qua chuỗi: inflate aspiration → gap → cortisol → suppress
  → = Một trong các sources của "trầm cảm MXH" (mechanism, not opinion)
```

---

## §5 — BEING SEEN: STATUS CALIBRATION FUNCTION

```
🟡 "BEING SEEN" = MUỐN SCHEMA ACCESS MAP CHÍNH XÁC:

  ĐỊNH NGHĨA:
    Being Seen = người khác có map ĐÚNG về tôi
    = "Họ biết tôi làm được gì, không làm được gì — CHÍNH XÁC"

  TẠI SAO CẦN (evolutionary function):
    Map chính xác → hợp tác HIỆU QUẢ
      → Biết ai cho gì, nhận gì → trao đổi tối ưu
    Map sai → frustrate hoặc exploit
      → Đánh giá thấp: "anh không biết gì" → schema bị block SAI → mất cơ hội
      → Đánh giá cao: "anh chắc biết" → bị giao việc quá sức → fail → stress

  VÍ DỤ:
    "Anh làm được, chỉ chưa phải bây giờ, em hiểu cho"
    = Muốn map ĐÚNG: "anh CÓ capacity, đang bận"
    = Nếu map sai: "anh không làm được" → schema bị block sai
    = Em rời đi → mất cơ hội trao đổi tương lai → thiệt CẢ HAI

  BEING SEEN ≠ CONNECTION:
    Being Seen = calibrate map ĐÚNG → chỉ cần "biết đúng" (đồng nghiệp đủ)
    Connection = body-level reward từ multi-input (Connection.md §0)
    → Sếp biết đúng năng lực tôi = Being Seen (không cần thân)
    → Bạn thân ôm = Connection (không liên quan đánh giá đúng/sai)
    → Có thể CẢ HAI (bạn thân + biết đúng) nhưng 2 functions KHÁC NHAU

  TRONG NHÓM:
    Mọi người BIẾT nhau → maps CHÍNH XÁC → hợp tác TỐT
    1 người bị hiểu sai → map sai → hợp tác KÉM + frustrate
    → Being Seen = social EFFICIENCY function (giảm friction)
```

---

## §6 — BELONGING: CACHED STATUS MAPS

```
🟡 BELONGING = "STATUS MAPS ĐÃ CALIBRATE SẴN CHO NHÓM":

  2 FUNCTIONS:

  ① CACHE — giảm scan cost:
     Gặp người trong nhóm: map CÓ SẴN → không scan → THOẢI MÁI
     Gặp người ngoài nhóm: phải scan → TỐN PFC → MỆT
     → Belonging = "tiết kiệm PFC cost cho status calibration"

     Hệ quả:
       Mất belonging = mất cache → phải scan MỌI NGƯỜI → kiệt sức
       Người mới chuyển trường/cty = MỆT (scan liên tục 2-4 tuần)
       Settle xong = cache compiled → "cảm thấy thuộc về" = maps ổn định

  ② BACKING — tăng confidence:
     Thuộc nhóm = có thế lực hỗ trợ → status maps MỞ RỘNG hơn
     → "Tôi có nhóm hỗ trợ" → dám mở schema → tự tin hơn
     → Mất nhóm → mất backing → schema thu hẹp → mất tự tin

     🟢 Social Baseline Theory (Coan 2015):
       Proximity to trusted others → metabolic cost GIẢM
       → Brain literally uses LESS energy khi "có đồng minh"
       → = Backing effect có neural basis thật

  BELONGING ≠ CONNECTION (phân biệt rõ):
    Belonging = cached maps + backing → efficiency + confidence
    Connection = body reward từ multi-input aggregate (Connection.md)
    → Có thể belong nhóm mà KHÔNG connection sâu (đồng nghiệp quen)
    → Có thể connection sâu mà KHÔNG belong nhóm (bạn ở xa)
    → CẢ HAI đều giá trị — nhưng satisfy KHÁC body-need

  VÍ DỤ — NHÀ THỜ:
    Cha Sứ > Ông Trùm > tín hữu ngang nhau
    → Status maps DEFINED SẴN → vào nhà thờ = không scan → thoải mái
    → Belonging = cache (biết ai ở đâu) + backing (cộng đồng hỗ trợ)
    → NGOÀI nhà thờ: maps KHÁC (context switch, §8)

  VÍ DỤ — ĐÀN KHỈ:
    → Mỗi con biết rank mọi con khác → maps SẴN → tiết kiệm
    → Con mới gia nhập → scan + fight → tốn energy → rồi settle
    → Sau settle → cache compiled → thoải mái = "belonging"
```

### §6.1 — Belonging × Agent.md SPM

```
🟡 BELONGING CÓ COMPONENT SPM (Agent.md §12):

  Khi thuộc nhóm:
    → Self-Pattern-Match fires liên tục lên members (background)
    → = "Tôi hiểu họ, họ hiểu tôi" = cached mutual SPM
    → Body nhận social presence signal liên tục (Agent.md §12.1)
    → = Baseline comfort từ nhóm (không cần tương tác active)

  Khi MẤT nhóm:
    → SPM firing lên absent members = Chunk-Miss (BFM §3.2)
    → Body expects social presence → absent → negative delta
    → = "Nhớ nhóm cũ" = SPM firing nhưng không có feedback
    → Duration: tùy compiled depth × alternative source availability

  → Belonging = STATUS function (cached maps + backing)
     + CONNECTION component (SPM-based social presence)
  → 2 functions overlap TRONG belonging — nhưng CÓ THỂ TÁCH
```

---

## §7 — SEROTONIN: CERTAINTY BIAS NỀN

```
⚠️ SECTION NÀY TÁCH RÕ: FUNCTION (chắc chắn) vs HORMONE (candidate).

  FUNCTION "certainty bias nền" = CHẮC CHẮN CÓ:
    ✅ Mọi người trải nghiệm "nhìn chung tự tin/không tự tin" (somatic confirm)
    ✅ Baseline này ỔN ĐỊNH, carry across contexts (verify: cùng bạn, khác place)
    ✅ Thay đổi CHẬM (tuần → tháng) theo tích lũy experience
    ✅ BIAS, không phải QUYẾT ĐỊNH (PFC có thể override — §7.2)

  HORMONE "serotonin = chemical carrier" = CHỈ LÀ CANDIDATE:
    → Evidence CÓ nhưng GIÁN TIẾP (§7.3 chi tiết)
    → Framework bind vào FUNCTION, không bind vào hormone
    → Nếu research chứng minh hormone khác → function KHÔNG ĐỔI
```

### §7.1 — 2 tầng: Bias nền + PFC quyết định

```
🟡 SEROTONIN KHÔNG "QUYẾT ĐỊNH" — PFC QUYẾT ĐỊNH:

  TẦNG 1 — Serotonin nền (body-level, chậm, vô thức):
    = MỨC CHẮC CHẮN NỀN cho toàn hệ thống
    → Cao: body CẢM THẤY "nhìn chung ok" → BIAS tự tin nhẹ
    → Thấp: body CẢM THẤY "nhìn chung không chắc" → BIAS rụt rè nhẹ
    → Thay đổi CHẬM (tuần → tháng) theo experience tích lũy
    → = BIAS nền — khung mặc định khi KHÔNG CÓ data cụ thể

  TẦNG 2 — PFC + Compiled chunks (imagine-level, nhanh, per-context):
    = QUYẾT ĐỊNH THỰC SỰ schema nào triển khai
    → PFC evaluate: "CỤ THỂ việc này, mình làm được không?"
    → Schema compiled: "đã làm 100 lần → chắc chắn" → auto execute
    → = OVERRIDE serotonin nền KHI CÓ data đủ mạnh

  TƯƠNG TÁC:
    Serotonin CAO + PFC chắc  → ✅✅ rất tự tin (bias + data align)
    Serotonin CAO + PFC ko chắc → 🟡 dám thử (bias push, data thiếu)
    Serotonin THẤP + PFC chắc → ✅ vẫn làm (data override bias)
    Serotonin THẤP + PFC ko chắc → ❌ rụt rè (bias + data đều block)

  → Serotonin = STARTING POINT (bias)
  → PFC + chunks = FINAL ANSWER (quyết định)
  → Quan trọng: khi data CỤ THỂ mạnh → serotonin baseline GẦN NHƯ KHÔNG MATTER
  → Chỉ khi KHÔNG CÓ data (mới, lạ, mơ hồ) → serotonin bias QUYẾT ĐỊNH

  VÍ DỤ — Người đang yêu (uncertainty phase):

    Tình huống: crush giai đoạn đầu — chưa biết họ có thích mình không.
    Serotonin nền: CÓ THỂ GIẢM (uncertainty loop, OCD-like — 🟡 Marazziti 1999).
    Lưu ý: "đang yêu" có NHIỀU phase, mỗi phase body state KHÁC.
    Ví dụ dưới = specifically uncertainty phase (crush chưa rõ).

    Context yêu (PFC KHÔNG CHẮC):
      PFC: "không biết họ có thích mình không" → KHÔNG CÓ data
      + Serotonin nền thấp → BIAS rụt rè
      → ❌ Rụt rè, không dám hành động với người đó

    Context công ty (PFC CHẮC CHẮN):
      PFC: "việc này rõ ràng, mình làm 3 năm rồi" → data DỒI DÀO
      + Serotonin nền thấp → bias rụt rè NHẸ
      + NHƯNG PFC override (compiled chunks quá mạnh)
      + THÊM: body đang hưng phấn (dopamine từ crush) → energy CAO
      → ✅ Vẫn tự tin ở cty — có thể HƠN bình thường (body energy boost)

    → = CÙNG người, CÙNG serotonin nền, KHÁC KẾT QUẢ per-context
    → Vì: PFC certainty per-context QUYẾT ĐỊNH, serotonin chỉ BIAS
    → Khi PFC có data mạnh → override bias hoàn toàn
    → Khi PFC không có data → bias THẮNG
```

### §7.2 — Serotonin Ratchet: dễ lên, khó xuống

```
🟡 SEROTONIN CÓ XU HƯỚNG HOMEOSTASIS ĐẶC BIỆT:

  ① ỔN ĐỊNH (mặc định):
     Serotonin baseline CỐ GIỮ mức hiện tại
     → Tránh dao động → tránh tốn PFC recalibrate toàn bộ maps
     → = "Tôi biết mình ở đâu, giữ nguyên" (energy efficient)

  ② SẴN SÀNG TĂNG (khi có cơ hội):
     Cơ hội → serotonin TĂNG nhanh:
       Được khen → tăng
       Đối thủ mất → "vị trí trống" → tăng
       Thắng competition → tăng
     → 🟢 Sapolsky: khỉ alpha chết → khỉ beta serotonin TĂNG NGAY
     → = Luôn sẵn sàng "lấp chỗ trống" phía trên (evolutionary advantage)

  ③ KHÁNG GIẢM (khi bị threat):
     Bị hạ status → body KHÁNG trước khi chấp nhận:
       Phase 1 — Denial: "không, tôi vẫn giỏi" (serotonin hold)
       Phase 2 — Rationalize: "họ không hiểu tôi" (PFC explain away)
       Phase 3 — Fight back: "tôi sẽ chứng minh" (behavioral resist)
       Phase 4 — Accept: serotonin DROP khi bằng chứng QUÁ NHIỀU
     → = Mất rank = body KHÁNG → rồi mới chấp nhận → rồi mới adjust

  → = RATCHET EFFECT: dễ lên, khó xuống
  → Evolutionary logic: giữ status cao = giữ schema access rộng = survival advantage
  → Giải thích:
    CEO bị sa thải: denial kéo dài (serotonin KHÁNG) → đau khổ dài
    Người mới giàu: adjust NHANH (serotonin sẵn sàng tăng)
    Người mới nghèo: adjust CHẬM (serotonin kháng giảm) → kéo dài khổ
```

### §7.3 — Evidence Limitations: thật thà về research

```
⚠️ TÁCH RÕ — framework HONEST về giới hạn evidence:

  EVIDENCE CÓ (nhưng gián tiếp):
    🟢 Khỉ: rank correlate serotonin MÁU (Raleigh 1991)
       → NHƯNG: serotonin máu ≠ serotonin não
       → 95% serotonin ở RUỘT → đo máu ≈ đo ruột chủ yếu
    🟢 Khỉ: rank change → cortisol change (Sapolsky 30+ năm)
       → NHƯNG: đàn khỉ = 20-50 con, 1 hierarchy ĐƠN GIẢN
       → Người = triệu, NHIỀU hierarchies → không tương đương trực tiếp
    🟢 Người: rank công việc → health change (Whitehall Studies)
       → NHƯNG: KHÔNG đo serotonin — chỉ đo cortisol + health outcomes
    🟢 Người: SSRI (tăng serotonin) → tự tin hơn, social behavior đổi
       → Support serotonin liên quan → nhưng SSRI affect NHIỀU system

  EVIDENCE THIẾU:
    ❌ Chưa có study đo serotonin NÃO trực tiếp ở người theo status
    ❌ Chưa có study so sánh serotonin: CEO vs nhân viên
    ❌ Serotonin máu ≈ serotonin não = chưa confirm
    ❌ Khỉ (20 con, 1 hierarchy) ≠ người (triệu, nhiều hierarchy)

  FRAMEWORK POSITION:
    "Status FUNCTION = chắc chắn có (quan sát + somatic confirm)
     Serotonin = CANDIDATE hormone (evidence gián tiếp từ khỉ + SSRI)
     Có thể serotonin + hormone khác kết hợp
     Hormone chính xác = CHƯA PROVEN ở người
     Framework bind FUNCTION 'certainty bias nền' — không assert hormone"

  → Giống: Satisfaction Signal (prolactin = candidate, function = chắc chắn)
  → Framework bind vào FUNCTION, không bind vào hormone
  → Nếu research chứng minh hormone khác → function KHÔNG ĐỔI
```

### §7.4 — Serotonin có nhiều function

```
🟡 SEROTONIN KHÔNG CHỈ LÀM 1 VIỆC:

  Function 1 — Certainty bias nền: mức chắc chắn NỀN (status-related)
  Function 2 — Mood regulation: mood chung (irritable, calm, patient)
  Function 3 — OCD link: uncertainty → compulsive check loop
  Function 4 — Sleep regulation: serotonin → melatonin pathway
  Function 5 — Gut signaling: 95% serotonin ở ruột → gut function

  → 1 hormone, 5+ functions → THÊM lý do chỉ là CANDIDATE
  → Framework bind "certainty bias" function, không bind toàn bộ serotonin
  → = Tránh overcommit vào hormone khi evidence chưa đủ
```

---

## §8 — FLEXIBILITY + CONTEXT SWITCH

```
🟡 MỖI NGƯỜI CALIBRATE STATUS KHÁC NHAU KHI SWITCH CONTEXT:

  ỔN ĐỊNH CAO (serotonin baseline ổn, compiled maps nhất quán):
    → Ở đâu cũng gần GIỐNG (tự tin hoặc rụt rè)
    → Switch context → status map thay đổi ÍT
    → Ưu: predictable, ít stress khi đổi context
    → Nhược: có thể không adapt đủ (tự tin ở chỗ nên khiêm nhường)
    → Ví dụ: "người này ở đâu cũng tự tin giống nhau"

  DAO ĐỘNG MẠNH (serotonin baseline dao động, maps context-specific):
    → Mỗi context → status map thay đổi ĐÁNG KỂ
    → Ưu: adapt tốt theo context (linh hoạt)
    → Nhược: energy tốn nhiều, stress khi switch nhanh
    → Ví dụ: ở cty rất tự tin (sếp) → ở nhà rụt rè (vợ dominant)

  PHỔ BIẾN: somewhere in between
    → Có baseline ổn định + calibrate VỪA cho từng context
    → Giống: thân nhiệt ổn 37°C nhưng DA adjust theo môi trường
```

### §8.1 — 3 thứ KHÁC NHAU dễ nhầm

```
⚠️ QUAN TRỌNG — DỄ NHẦM "SWITCH CONTEXT" = "CALIBRATE STATUS":

  ① SEROTONIN BASELINE (certainty bias nền):
     → Ổn định, carry across ALL contexts
     → KHÔNG tốn PFC
     → = "Nhìn chung tôi tự tin thế nào"
     → Thay đổi CHẬM (tuần → tháng)
     → Ví dụ: được khen ở cty → về nhà VẪN tự tin (carry)
              bị mắng ở nhà → lên lớp VẪN thiếu tự tin (carry)

  ② STATUS PER-CONTEXT (compiled maps cho context quen):
     → Mỗi context quen = 1 compiled map
     → Switch giữa maps quen = PFC load compiled → TỐN ÍT
     → Ở cty: map A | ở nhà: map B | ở nhà thờ: map C
     → = Giống lái xe đường quen — vô thức
     → Ví dụ: từ cty về nhà → PFC switch map nhanh (cả 2 đã compiled)

  ③ STATUS CONTEXT MỚI (chưa có map):
     → Gặp nhóm mới, job mới, nước mới
     → PFC phải DRAFT map mới → TỐN NHIỀU bandwidth
     → Cortisol tăng (uncertainty) cho tới khi map compiled
     → = "Mệt khi đi chỗ mới" = PFC drafting status maps liên tục
     → Ví dụ: ngày đầu đi làm = mệt (scan mọi người + draft maps)

  CHỒNG LÊN NHAU (worst case):
    Switch context (load map khác): nhanh nếu quen
    + Serotonin baseline: carry theo (có thể thấp)
    + Calibrate mới: nếu context mới → PFC heavy

    → Người chuyển trường: switch context (PFC)
      + calibrate TOÀN BỘ maps mới (PFC heavy)
      + serotonin baseline carry (có thể thấp nếu bị bully trước)
      = TRIPLE cost → cực mệt → giải thích "trầm cảm khi chuyển trường"
```

### §8.2 — Status thực tế: nhóm 5-20 người quen

```
🟡 TRONG THẾ GIỚI HIỆN ĐẠI — status baseline SHAPED BỞI NHÓM NHỎ:

  Thời cổ đại — gap CỰC LỚN:
    Lãnh chúa: kiểm soát mọi thứ → body state tự tin thật sự
    Nô lệ: không kiểm soát gì → body state sợ hãi thật sự
    → Status baseline KHÁC BIỆT lớn → biochemistry KHÁC thật

  Thế giới hiện đại — gap bị FLATTEN:
    ① Pháp luật: CEO không đánh nhân viên, tổng thống không lấy nhà bạn
    ② Ít tương tác trực tiếp cross-status: bạn KHÔNG GẶP tổng thống
    ③ Basic needs MET: không "comply vì đói"
    → Gap TRÊN GIẤY > gap CẢM NHẬN

  → Status THẬT SỰ CẢM NHẬN = từ NHÓM 5-20 NGƯỜI QUEN:
    Vợ/chồng, con, sếp trực tiếp, đồng nghiệp, bạn thân
    → ĐÂY mới là nơi status TÁC ĐỘNG hàng ngày
    → Bị vợ coi thường → status baseline GIẢM thật
    → Được sếp công nhận → status baseline TĂNG thật
    → = Status thực tế ≈ trung bình experience từ nhóm thân

  Hệ quả:
    "Giàu nhưng vợ coi thường" = status THẤP (within nhóm thân)
    "Nghèo nhưng gia đình tôn trọng" = status ỔN (within nhóm thân)
    → Thu nhập KHÔNG = status thực tế cảm nhận
    → = "Hạnh phúc không nằm ở tiền" có mechanism basis thật
```

---

## §9 — STATUS × CHUNK DYNAMICS

```
⭐ MỚI (v7.8): KHI STATUS THAY ĐỔI, CHUNK NETWORK XẢY RA GÌ?

  Body-Feedback-Mechanism.md define 3 chunk dynamics:
    ① Chunk-Shift: same chunks, DIFFERENT valence (đánh giá đổi)
    ② Chunk-Miss: compiled pattern ABSENT (negative prediction delta)
    ③ Chunk-Gap: pattern CHƯA CÓ nhưng network detect hole

  Status changes MAP TRỰC TIẾP vào 3 dynamics này:
```

### §9.1 — Chunk-Shift: status re-evaluate

```
🟡 CHUNK-SHIFT TRONG STATUS:

  ĐỊNH NGHĨA: Chunks về BẢN THÂN vẫn y nguyên — ĐÁNH GIÁ thay đổi.
  = Status Position shift mà không thay đổi reality khách quan.

  CASES:

  ① Bị phản bội (social):
     Chunks "bạn A tin tưởng tôi" → phản bội xảy ra
     → Valence SHIFT: từ "an toàn" → "bị lừa"
     → Status map VỚI NGƯỜI ĐÓ restructure toàn bộ
     → Body-feedback: dissonance mạnh (Chunk-Shift, BFM §3.1)

  ② Phát hiện sai (self-assessment):
     Tưởng mình giỏi domain X → feedback thật: kém
     → Chunks "tôi giỏi X" vẫn đó, valence SHIFT negative
     → Status Position GIẢM trong domain đó
     → Body-feedback: dissonance ("tôi không như tôi tưởng")

  ③ Được công nhận bất ngờ (positive shift):
     Không biết mình giỏi → sếp khen trước mọi người
     → Chunks "tôi làm X" vẫn đó, valence SHIFT positive
     → Status Position TĂNG
     → Body-feedback: reward (surprise + validation)

  ĐẶC ĐIỂM CHUNK-SHIFT TRONG STATUS:
    → Content unchanged (tôi VẪN LÀ tôi)
    → Evaluation changed (đánh giá VỀ TÔI khác)
    → Propagation: shift ở 1 domain → có thể lan sang domains liên quan
    → Speed: có thể rất nhanh (1 event đủ) — khác serotonin baseline (chậm)
    → = Chunk valence shift NHANH, serotonin adjust CHẬM → lag → stress
```

### §9.2 — Chunk-Miss: status absent

```
🟡 CHUNK-MISS TRONG STATUS:

  ĐỊNH NGHĨA: Compiled status maps KHÔNG ĐƯỢC FIRE (absent).
  = Từng có status position → MẤT (hoặc rời bỏ context).

  CASES:

  ① Rời nhóm quen:
     Compiled maps cho nhóm A → rời nhóm → maps ABSENT
     → VTA detect: actual (không fire) < baseline (fire daily)
     → Body-feedback: negative prediction delta (miss nhóm)
     → = "Nhớ nhóm cũ" = Chunk-Miss (maps compiled nhưng không fire)

  ② CEO bị sa thải:
     Compiled maps: "mọi người comply, tôi ra lệnh, maps MỞ TOÀN BỘ"
     → Sa thải → maps ABSENT (không ai comply nữa)
     → VTA: massive negative delta (hàng chục maps mất cùng lúc)
     → Body-feedback: dissonance rất mạnh (multi-map Chunk-Miss)
     → + Serotonin Ratchet KHÁNG (§7.2) → denial kéo dài

  ③ Chuyển trường:
     Compiled maps cho nhóm cũ → MẤT TOÀN BỘ (Chunk-Miss)
     + Context mới chưa có maps → phải draft (Chunk-Gap)
     → = COMPOUND: Miss (cũ absent) + Gap (mới chưa có)
     → Giải thích: cực mệt + cực stress (2 dynamics cùng lúc)

  ĐẶC ĐIỂM:
    → Duration tùy: compiled depth × thời gian có × alternative source
    → Deep compiled (10 năm ở nhóm) → Miss kéo dài (tháng → năm)
    → Shallow compiled (3 tháng) → Miss ngắn (tuần)
    → CAN fade: khi maps mới compile đủ → old maps deactivate dần
```

### §9.3 — Chunk-Gap: status chưa từng có

```
🟡 CHUNK-GAP TRONG STATUS:

  ĐỊNH NGHĨA: CHƯA TỪNG CÓ status position X, nhưng network DETECT thiếu.
  = Muốn status chưa từng trải nghiệm (aspiration without experience).

  CASES:

  ① Muốn được tôn trọng (chưa từng):
     Lớn lên bị coi thường → compiled maps toàn "comply"
     → Network detect hole: "người khác có maps MỞ, tôi không"
     → Chunk-Gap: muốn status chưa từng compile
     → Body-feedback: dissonance (gap detection, ACC mechanism)
     → = "Khao khát được tôn trọng" = Chunk-Gap cho status

  ② Aspiration từ MXH:
     Chưa từng là influencer → thấy người khác có
     → Network detect: "pattern đó tồn tại nhưng tôi chưa có"
     → Chunk-Gap: aspiration KHÔNG dựa trên experience
     → Body-feedback: dissonance (want without compiled basis)

  ③ Child muốn "lớn":
     Thấy người lớn có schema access rộng → muốn
     → Chunk-Gap: chưa compiled maps cho adult context
     → = "Muốn lớn nhanh" = Gap detection cho status maps

  ĐẶC ĐIỂM:
    → Chunk-Gap khác Chunk-Miss: Miss = TỪNG CÓ rồi mất, Gap = CHƯA BAO GIỜ CÓ
    → Gap → có thể transition thành Miss (BFM §3.3 Gap→Miss Transition)
      khi Imagine-Final preview ổn định + lặp → compile baseline → reality miss
    → Gap MORE durable than Miss (không fade tự nhiên vì không có gì replace)
    → Gap CAN resolve: khi compile maps mới (experience thật, không phải imagine)
```

### §9.4 — Compound: khi nhiều dynamics cùng lúc

```
🟡 STATUS CHANGES THƯỜNG LÀ COMPOUND (2-3 dynamics cùng lúc):

  ┌─────────────────────────┬────────────────────────────────────────────┐
  │ Tình huống              │ Compound dynamics                           │
  ├─────────────────────────┼────────────────────────────────────────────┤
  │ CEO bị sa thải          │ Shift (identity) + Miss (daily maps)       │
  │                         │ + Gap (what now? future uncertain)          │
  │                         │ = TRIPLE → giải thích severity              │
  ├─────────────────────────┼────────────────────────────────────────────┤
  │ Chuyển trường           │ Miss (old maps absent) + Gap (new maps     │
  │                         │ chưa compiled) = DOUBLE                     │
  ├─────────────────────────┼────────────────────────────────────────────┤
  │ Bị bạn thân phản bội   │ Shift (valence flip) + Miss (trust maps    │
  │                         │ absent) = DOUBLE                            │
  ├─────────────────────────┼────────────────────────────────────────────┤
  │ Thăng chức bất ngờ     │ Shift (positive) + Gap (new role maps      │
  │                         │ chưa compiled) = MIXED (reward + stress)   │
  ├─────────────────────────┼────────────────────────────────────────────┤
  │ Người nghèo bỗng giàu  │ Shift (self-assessment) + Gap (new context │
  │                         │ maps) = MIXED (serotonin sẵn sàng tăng    │
  │                         │ nhưng maps chưa compiled → anxiety + joy)  │
  └─────────────────────────┴────────────────────────────────────────────┘

  → Compound MẠNH hơn single (mỗi dynamic = 1 signal, chồng = amplify)
  → Giải thích tại sao major life transitions = CỰC stress
  → Giải thích tại sao recovery time tùy: bao nhiêu dynamics đồng thời
  → Cross-ref: BFM §4 Compound Mechanism, Connection.md §1.3 (4 Cases)
```

---

## §10 — STATUS × CORTISOL

```
🟡 CORTISOL × STATUS = VICIOUS CYCLE TIỀM ẨN:

  Cortisol = Change-Readiness Amplifier (Cortisol-Baseline.md §1).
  Status changes = uncertain → trigger cortisol.
  Cortisol cao + kéo dài → SUPPRESS status maps.

  SPECTRUM:
    Cortisol    Status effect
    ─────────── ──────────────────────────────────────────────
    Thấp        Status maps ỔN → body-need dễ meet
    Vừa         Status maps ỔN + ACTIVE calibrate tốt (optimal)
    Cao         Status maps THU HẸP → "tôi kém" → rụt rè
    Rất cao     Status maps GẦN ĐÓNG → "vô giá trị" → isolate

  VICIOUS CYCLE:
    Status threat (bị coi thường, mất nhóm, etc.)
      → Cortisol tăng (change-readiness cho threat)
        → Cortisol suppress status maps (thu hẹp)
          → Ít schema sẵn sàng → body-need KHÓ meet
            → Body-need unmet → cortisol tăng thêm
              → Maps thu hẹp thêm → isolate
                → SPIRAL (depression pathway)

  PHÁ VICIOUS CYCLE:
    → Cần EXTERNAL input (social contact, success experience)
    → Cortisol tự nó KHÔNG GIẢM chỉ vì "nghỉ ngơi" (inertia, §2.3 Cortisol-Baseline)
    → Cần: experience MỚI cho body compile maps mới → confidence restore
    → = Giải thích tại sao "ở nhà nghỉ" KHÔNG fix depression
    → = Cần HÀNH ĐỘNG (dù nhỏ) → success → map expand → cortisol giảm
```

### §10.1 — "Thành công nhưng trống rỗng"

```
🟡 STATUS POSITION CAO (BÊN NGOÀI) + CORTISOL CAO (BÊN TRONG):

  Paradox phổ biến: CEO/celebrity "có mọi thứ" nhưng "không enjoy"

  Mechanism:
    Status Position cao: compiled maps MỞ RỘNG (schema access đầy đủ)
    NHƯNG: cortisol cao (vì continuous threat: sợ mất, sợ fail, workload)
    → Cortisol suppress: maps THU HẸP (override position)
    → = Trên giấy maps mở, nhưng BODY CẢM NHẬN maps hẹp
    → = "Có quyền nhưng không dám dùng" / "có tiền nhưng không enjoy"

  → Status = self-assessment chunks + hormonal baseline (§1)
  → Khi chunks nói "cao" nhưng cortisol nói "nguy hiểm"
    → Body nghe CORTISOL (signal strength mạnh hơn, §0)
  → = "Thành công nhưng trống rỗng" có mechanism explanation
  → Fix: giảm cortisol source (threat sources) — KHÔNG phải "thêm thành công"
```

---

## §11 — STATUS × OTHER OBSERVATION PARAMETERS

```
🟡 STATUS AMPLIFY HOẶC SUPPRESS MỌI OBSERVATION PARAMETER KHÁC:

  Status = meta-parameter: nó GATE access cho toàn bộ parameters khác.
  (Không phải "layer cao hơn" — mà "maps rộng/hẹp affect mọi thứ")

  STATUS CAO (maps MỞ) — amplify:
    Novelty: dám thử mới (không sợ fail) → novelty accessible
    Connection: dám approach, eye contact, intimate → connection possible
    Mastery: dám thử skill khó → mastery development enabled
    Autonomy: "tôi quyết được" → prediction accuracy cao
    → = Maps MỞ → body-need DỄ meet → positive feedback loop

  STATUS THẤP (maps ĐÓNG) — suppress:
    Novelty: sợ fail → avoid new → novelty blocked
    Connection: rụt rè → avoid approach → connection limited
    Mastery: sợ fail → avoid challenge → mastery stagnant
    Autonomy: "tôi không dám" → prediction overridden → dissonance
    → = Maps ĐÓNG → body-need KHÓ meet → vicious cycle potential

  QUAN TRỌNG: per-person × per-context:
    → Cùng 1 người: status CAO với nhóm A (maps mở) → novelty + connection OK
                    status THẤP với nhóm B (maps đóng) → novelty + connection blocked
    → KHÔNG phải "status cao = mọi thứ tốt globally"
    → = Per-context amplification/suppression
```

### §11.1 — Status × Connection (overlap analysis)

```
🟡 STATUS VÀ CONNECTION: KHÁC NHAU NHƯNG INTERACT:

  Connection.md phân biệt rõ:
    Connection = body reward từ multi-input aggregate GIỮA 2+ agents
    Status = self-assessment chunks + maps per-person per-context

  OVERLAP:
    → Status CAO với người X → dám approach → connection POSSIBLE
    → Status THẤP với người X → rụt rè → connection BLOCKED
    → Connection SÂU với người X → maps CALIBRATE chính xác (Being Seen)
    → = Status GATES connection, Connection CALIBRATES status

  TÁCH BIỆT:
    → Có thể status cao mà KHÔNG connection (sếp: respected nhưng alone)
    → Có thể connection sâu mà status đối xứng (bạn thân: ngang hàng)
    → Belonging = status function (cached maps) + connection component (SPM)

  → 2 parameters KHÁC NHAU, INTERACT strong, KHÔNG reduce về nhau
```

### §11.2 — Status × Threat (social threat)

```
🟡 STATUS THREAT = THREAT OBSERVATION PARAMETER APPLIED TO STATUS:

  Threat.md §origin 2 (Peer-Threat):
    → Social comparison → "tôi kém hơn" → threat signal
    → = Status threat = Chunk-Shift (valence shift negative)

  Status threat KHÁC physical threat:
    Physical: bounded, có endorphin buffer, hết nhanh
    Status: anticipatory, unbounded, KHÔNG buffer, kéo dài
    → = Status threat CÓ THỂ chronic → cortisol sustained → vicious cycle (§10)

  MXH = chronic low-level status threat:
    → Liên tục so sánh → liên tục threat → liên tục cortisol
    → Không acute (không "bị đánh") → KHÔNG có endorphin buffer
    → = "Death by thousand cuts" — mỗi lần nhỏ, tích lũy lớn

  → Cross-ref: Threat.md §origin 2, Cortisol-Baseline.md §4 silent cortisol
```

---

## §12 — QUÂN ĐỘI: STATUS OPTIMIZATION CASE STUDY

```
🟡 QUÂN ĐỘI = THIẾT KẾ STATUS HIỆU QUẢ NHẤT LOÀI NGƯỜI TẠO RA:

  VẤN ĐỀ trong đời thường:
    → Gặp người mới → scan → calibrate → TỐN PFC
    → Status không rõ → xung đột → tốn thời gian + energy
    → 100 người lạ → 100 maps cần draft → PFC OVERLOAD

  QUÂN ĐỘI GIẢI QUYẾT BẰNG 4 NGUYÊN TẮC:

  ① PHÂN CẤP RÕ RÀNG (quân hàm = visual symbol):
     → NHÌN là biết status → PFC cost ≈ ZERO
     → Đời thường: gặp lạ → 5-30 giây scan
     → Quân đội: nhìn quân hàm → 0.5 giây → map LOADED ngay
     → = Pre-compiled maps for EVERY rank → no drafting needed

  ② TUÂN THỦ TUYỆT ĐỐI (schema FIXED per rank):
     → Cấp dưới: comply → luôn đúng → PFC không cần evaluate
     → Cấp trên: ra lệnh → luôn đúng → PFC không cần negotiate
     → = Schemas pre-assigned → vô thức execute

  ③ TÔN TRỌNG TUYỆT ĐỐI (không challenge):
     → Rank cao: serotonin stable → assured
     → Rank thấp: BIẾT RÕ vị trí → không bất an (certainty!)
     → "Biết rõ ở đâu" = THOẢI MÁI hơn "không biết"
     → = Uncertainty (tốn PFC + cortisol) → Certainty (tiết kiệm)

  ④ LÝ DO RÕ RÀNG (coherence satisfied):
     → Rank cao vì kinh nghiệm + training → hiểu được → chấp nhận dễ
     → = Coherence signal: "hệ thống này hợp lý" → less resistance

  KẾT QUẢ:
    Đời thường: ~significant PFC bandwidth cho social status calibration
    Quân đội: minimal PFC cho status (pre-defined) → PHẦN LỚN cho TASK
    → = PFC FREED UP cho chiến thuật, chiến lược, problem-solve
    → = Đây là lý do quân đội HIỆU QUẢ trong crisis (PFC available for action)
```

### §12.1 — Cùng principle ở nơi khác

```
🟡 QUÂN ĐỘI KHÔNG UNIQUE — CÙNG PRINCIPLE, KHÁC MỨC ĐỘ:

  Đồng phục trường học: giảm status noise (giàu/nghèo → visual flatten)
  Dress code công ty: giảm visual status competition
  Áo lễ nhà thờ: flatten status (ngang nhau trước Chúa)
  Hierarchy rõ ràng (CEO → VP → Manager → IC): pre-define maps
  Titles + business cards: visual cue cho nhanh scan

  → TẤT CẢ nhằm: GIẢM PFC cost cho status calibration
  → = Status system design principle: CLARITY reduces cognitive load
  → Ngược lại: flat organization = MORE PFC cost (ai report ai? ai quyết gì?)
    → Ưu: flexibility, creativity
    → Nhược: PFC overhead, potential conflict
    → = Trade-off: clarity vs flexibility
```

---

## §13 — STATUS TRONG TẬP THỂ

```
🟡 STATUS KHÔNG CHỈ CÁ NHÂN — CẤU TRÚC TẬP THỂ:

  BẦY ĐÀN ĐỘNG VẬT:
    → Status hierarchy = cấu trúc TỔ CHỨC tự nhiên
    → Mỗi con biết vị trí → behavior predictable → nhóm STABLE
    → Alpha bệnh/chết → hierarchy sụp → chaos → re-calibrate → stable lại
    → = Status = "phần mềm tổ chức" cho tập thể

  XÃ HỘI LOÀI NGƯỜI:
    → Multi-context, multi-dimension (phức tạp hơn đàn khỉ nhiều)
    → Nhưng CÙNG function: status maps → organize collective behavior
    → Pháp luật = FORMALIZE status maps ("ai được gì, phải gì")
    → Dân chủ = FLATTEN status gap (trao đổi > lấy/comply)
    → Độc tài = WIDEN gap (lãnh đạo >> dân → lấy mode dominant)

  SCALE EFFECT:
    Nhóm nhỏ (5-20): status maps = personal (tôi biết từng người)
    Nhóm vừa (20-150): status maps = role-based (vị trí/chức danh)
    Nhóm lớn (150+): status maps = symbolic (quân hàm, bằng cấp, title)
    → Càng lớn → càng cần SYMBOL → càng flatten thành hierarchy đơn giản
    → = Hierarchy là COMPRESSION ALGORITHM cho status ở scale lớn
    → Nhỏ: full Schema Access Map (nhiều chiều) | Lớn: hierarchy (1 chiều)
```

---

## §14 — HONEST ASSESSMENT + CÂU HỎI MỞ

```
⚠️ WHAT WE'RE CONFIDENT ABOUT:

  ✅ Status FUNCTION exists (quan sát được ở mọi người, mọi động vật xã hội)
  ✅ Schema Access Map model giải thích MORE cases than hierarchy model
  ✅ Per-person × per-context nature (ai cũng somatic confirm)
  ✅ 5-step scan mechanism (body-level, quan sát được)
  ✅ Position vs Aspiration distinction (6 cases verify)
  ✅ Being Seen = calibration function (functional, observable)
  ✅ Belonging = cached maps + backing (observable + Social Baseline Theory 🟢)
  ✅ Cortisol × Status interaction (Whitehall Studies 🟢, Sapolsky 🟢)
  ✅ Ratchet effect (khỉ: Sapolsky 🟢, người: observable patterns)

  🟡 WHAT WE'RE SYNTHESIZING (framework logic, not directly proven):

  🟡 Schema Access Map as COMPLETE model (framework synthesis, not tested)
  🟡 3 Modes (Lấy/Trao đổi/Comply) as exhaustive spectrum
  🟡 Chunk Dynamics mapping (§9) — logical extension from BFM, not direct study
  🟡 Status as meta-parameter gating other parameters (§11)
  🟡 MXH mechanism chain (aspiration → gap → cortisol → suppress)
  🟡 Military as "status optimization" framing

  ❌ WHAT WE DON'T KNOW:

  ❌ Serotonin = carrier hormone (candidate only, evidence gián tiếp)
  ❌ Exact neural mechanism cho body scan (amygdala? STS? FFA?)
  ❌ Status flexibility: hardware (receptor variants) vs training (experience)?
  ❌ Online status (MXH) = cùng mechanism hay weakened version?
  ❌ Quantitative: maps MỞ bao nhiêu % per context?
```

### §14.1 — Câu hỏi mở

```
  Q1: Status scan VÔ THỨC — neural circuit chính xác?
      → Candidate: amygdala, STS (Superior Temporal Sulcus), FFA
      → Research có nhưng chưa integrate đầy đủ

  Q2: Status Flexibility — hardware hay training?
      → Serotonin receptor variants (5-HT1A, 5-HT2A) → hardware range?
      → Childhood experience → training within range?
      → Likely cả 2: hardware set range, experience chọn vị trí (giống PFC)

  Q3: Online Status (MXH) — same or different mechanism?
      → Likes = status signal? Body respond tương tự face-to-face?
      → Hypothesis: WEAKER per-signal (no body presence)
        nhưng VOLUME compensation (nhiều signals tích lũy)
      → = Net effect có thể MẠNH hơn face-to-face (ironic)

  Q4: Status ở hermit (không gặp ai)?
      → Internalized status từ quá khứ → VẪN CÓ maps
      → Nhưng: không calibration mới → maps drift
      → = Status CẦN social contact để maintain accuracy
      → Hermit status = frozen at time of withdrawal

  Q5: Status × Imagine-Final → aspiration compile?
      → Aspiration lặp lại đủ lâu → compile thành baseline?
      → = Gap→Miss Transition (BFM §3.3) applied to status aspiration?
      → If yes: chronic high aspiration → eventual Miss (kỳ vọng thành standard)
      → Implication: "kỳ vọng cao → thất vọng lớn" = mechanism-level truth
```

---

## §15 — CROSS-REFERENCES

```
  CORE:
    → Core-v7.8-Draft.md §8 — Status observation parameter definition
    → Core-v7.8-Draft.md §9 — Development trajectory (status across life)

  MECHANISM FILES:
    → Body-Feedback-Mechanism.md §3 — Chunk-Shift/Miss/Gap (§9 mapping)
    → Body-Feedback-Mechanism.md §4 — Compound mechanism
    → Cortisol-Baseline.md v2.0 §3 — 10 touchpoints (status = touchpoint)
    → Cortisol-Baseline.md v2.0 §4 — Silent cortisol (MXH pathway)
    → Chunk.md v2.0 — Chunk substrate, compilation, hierarchy
    → Valence-Propagation.md v1.1 — Valence shift mechanism (§9.1)

  OBSERVATION PARAMETER FILES:
    → Observation/Connection.md — §1.3 (4 Cases), §3 (Calibration), §6 (×Imagine-Final)
    → Observation/Threat.md — Social threat origin, imposed threat
    → Observation/Novelty.md — Status gates novelty access (§11)
    → Observation/Empathy.md — SPM applied to status reading
    → Observation/Drive.md — Status as drive-like emergent pattern
    → Observation/Boredom.md — Low status + boredom = isolation risk

  OTHER DEEP-DIVE FILES:
    → Agent.md §12 — Body-need feeder, SPM as social comparison mechanism
    → Feeling.md v2.0 — PFC observation interface (status = felt sense)
    → Anchor-Schema.md — Trust binding (trust = status stability)
    → Imagine-Final.md — Aspiration as Imagine-Final preview

  APPLICATION FILES:
    → Research/Education/Domain-Mapping-Drive.md — Status in learning
    → Research/Education/Education-Principles.md — Status × classroom
    → Core-Deep-Dive/PFC/Feeling/Deep-Analysis-Draft/ — Status in giving

  BACKUP:
    → _backup/Status-Analysis-v2-v75-era.md — v7.5-era version (656L)
```

---

## Summary

```
Status = observation parameter: self-assessment chunk patterns + hormonal baseline.

Core insight: Status = Schema Access Map (NOT hierarchy rank).
  → Per-person × per-context: "schemas nào SẴN SÀNG với NGƯỜI NÀY"
  → Hierarchy = simplest special case (1 dimension only)

Mechanism: body vô thức scan (5 bước) → Schema Access Map → 3 modes (Lấy/Trao đổi/Comply)
2 parameters: Position (serotonin baseline, chậm) vs Aspiration (PFC-level, nhanh)
Serotonin = certainty BIAS nền (candidate hormone) — PFC QUYẾT ĐỊNH thực sự
Chunk dynamics: status changes = Shift (re-evaluate) / Miss (absent) / Gap (never had)
Cortisol vicious cycle: threat → cortisol → suppress maps → more unmet → more cortisol
Military = status optimization (pre-define maps → PFC freed for tasks)
Honest: function = proven, hormone = candidate, exact neural circuit = unknown.
```

---

> **Version:** 1.0
> **Lines:** ~1,301
> **Created:** 2026-04-20
> **Rewrite từ:** Status-Analysis-v2.md (656L, 2026-03-23)
> **v7.8 aligned:** ✅ observation parameter framing, cycle-based, chunk dynamics mapped
