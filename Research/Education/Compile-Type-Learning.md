# Compile-Type-Learning — Loại Compile Ảnh Hưởng Learning Thế Nào

> **Pythagoras tự đo vòng tròn → phát hiện pi → compile Type A/B (trực tiếp).**
> **Học sinh được dạy pi = 3.14 → trust thầy cô → compile Type C (install).**
>
> Cả hai "biết" pi. Cả hai tính đúng.
> Nhưng CHẤT LƯỢNG chunk khác nhau:
>   Pythagoras: multi-modal (đo, vẽ, tính, sai, sửa) → chunk SÂU, ROBUST
>   Học sinh: single-channel (nghe, ghi, áp dụng) → chunk NHANH, PHỤ THUỘC SOURCE
>
> File này phân tích: compile type MIX trong learning ảnh hưởng gì?
> Khi nào Type C đủ? Khi nào cần Type A verify?
> Cực đoan 2 hướng → hệ quả gì? Research nói gì?
>
> **Insight nền tảng:**
> Logic vẫn có thể chặt chẽ dù toàn Type C — vì chain chunk vẫn được,
> body feedback "chain này đúng." Nhưng "đúng" ở đâu?
> Đúng trên giấy? Hay đúng ngoài đời? Đó là câu hỏi.

---

> **Trạng thái:** v1.1
> **Ngày:** 2026-05-12 (v1.1 — §0.1 Evolutionary Context + §4.5 Screen/Digital)
> **Vị trí:** Research/Education/ (research analysis, observation-level)
> **Dependencies:**
>   Compile-Taxonomy.md v1.1 — 3 Loại A/B/C, 4 pathways, 6 trade-offs
>   Education-Mechanism.md v1.0 — arc design principles, bridge + motivation
>   Chunk.md v2.1 — compile mechanisms, trust gate
>   Collective-Body.md v1.1 — trust = only bridge, Model 3 cấp
> **Confidence:** 🟢 Research support | 🟡 Framework synthesis | 🔴 Hypothesis
> **Language:** Tiếng Việt primary + English technical terms

---

## Mục lục

- §0 — VẤN ĐỀ CỐT LÕI
- §0.1 — EVOLUTIONARY CONTEXT: TYPE A → TYPE C QUA 2 TRIỆU NĂM
- §1 — 3 COMPILE TYPES TRONG LEARNING CONTEXT
- §2 — RESEARCH EVIDENCE: 2 CỰC ĐOAN
- §3 — TYPE C → TYPE A TRANSITION: "TRUST THEN VERIFY"
- §4 — PER-DOMAIN ANALYSIS: TOÁN, NGÔN NGỮ, LẬP TRÌNH, THỂ THAO, SCREEN/DIGITAL
- §5 — LẶP CÓ BODY-CHECK VS LẶP MÁY MÓC
- §6 — HỆ QUẢ CHO THIẾT KẾ GIÁO DỤC
- §7 — HONEST ASSESSMENT
- §8 — CROSS-REFERENCES

---

## §0 — VẤN ĐỀ CỐT LÕI

```
⭐ CÂU HỎI NỀN TẢNG:

  Học sinh ngồi trong lớp, nghe giảng, làm bài, thi — 12+ năm.
  Phần lớn kiến thức = Type C: trust thầy cô, trust sách, trust hệ thống.
  Logic chain chặt chẽ trên giấy. Điểm cao. Graduation.

  Nhưng ra ngoài đời:
  → "Học giỏi mà không biết làm gì"
  → "Biết lý thuyết nhưng không áp dụng được"
  → "Giải bài toán nhanh nhưng không hiểu tại sao phải giải"

  TẠI SAO?

  Framework predict: vì COMPILE TYPE khác nhau tạo CHUNK QUALITY khác nhau.

  Type A (trực tiếp): body trải nghiệm → multi-modal → chunk SÂU, ROBUST
  Type C (trust install): nghe/đọc → single-channel → chunk NHANH, DỄ CONFABULATE

  Cả hai đều "biết." Nhưng chunk Type A LINK được với domain thật.
  Chunk Type C LINK được với context lớp học. Đổi context → fire yếu hoặc không fire.

  = TRANSFER FAILURE — hiện tượng phổ biến nhất trong education research.

⚠️ FILE NÀY KHÔNG NÓI Type C xấu:
  Type C = cơ chế mạnh nhất để access collective knowledge.
  Không ai đủ 1 đời để Type A compile toàn bộ kiến thức nhân loại.
  Vấn đề = TYPE C ALONE, không kết hợp Type A verify.
```

---

## §0.1 — EVOLUTIONARY CONTEXT: TYPE A → TYPE C QUA 2 TRIỆU NĂM

```
⭐ TIẾN TRÌNH LỊCH SỬ CỦA COMPILE TYPE:

  ~2M năm:     100% Type A
               Bộ lạc 30-150 người. Săn, hái, chế tạo, quan sát tự nhiên.
               Mọi thứ = trải nghiệm trực tiếp. Multi-modal. Domain feedback ngay.
               Trẻ HỌC bằng chơi, bắt chước, thử-sai. Không có "trường."

  ~100K năm:   Type A + ngôn ngữ → Type C sơ khai
               Ngôn ngữ nói = trust install đầu tiên ("hổ ở kia → tránh").
               NHƯNG: vẫn verify được ngay (đi xem → thấy hổ thật).
               Type C có anchor Type A gần như TỨC THÌ.

  ~5,000 năm:  Chữ viết → Type C MỞ RỘNG
               Kiến thức ghi lại → trust sách, trust kinh, trust luật.
               Type C bắt đầu TÁCH khỏi Type A: đọc về nơi chưa tới,
               chuyện chưa thấy, kiến thức chưa verify.

  ~500 năm:    In ấn (Gutenberg) → Type C PHỔ BIẾN
               Sách không còn hiếm. Collective knowledge accessible rộng.
               Type C scale tăng MẠNH. Type A vẫn là daily life.

  ~200 năm:    Trường học phổ cập → Type C DOMINANT
               Lần đầu tiên: trẻ NGỒI TRONG PHÒNG 6-8 giờ/ngày
               NGHE người lớn nói → ghi → làm bài → thi.
               = Body calibrate cho Type A (chạy, nhảy, nghịch, khám phá)
                 bị ép chạy Type C (ngồi, nghe, ghi, nhớ).
               = Cùng logic mismatch: processed food vs ancestral diet
                 (Core-Software.md §2 Ancestral Domain).

  ~50 năm:     TV → Type C THỤ ĐỘNG
               1 chiều. 2 kênh (visual + auditory). Không contingency.
               Trẻ NHẬN nhưng KHÔNG hành động. Brain wire 1 chiều.

  ~15 năm:     Smartphone + Social media → Type C TĂNG TỐC
               Thông tin vô tận. Quảng cáo vô tận. Nội dung vô tận.
               Type C install ở tốc độ CHƯA TỪNG CÓ trong lịch sử.

  ~5 năm:      Short-form video (TikTok) → Type C ở tốc độ CỰC ĐẠI
               ~15 giây/video × vô tận × algorithmic optimization
               VTA fire mỗi swipe → baseline novelty BỊ NÂNG
               → Domain thật (cát, nước, lego, sách) = "chậm, chán"

  ⭐ PATTERN:
    Type A giảm dần. Type C tăng dần. Tốc độ tăng = EXPONENTIAL.
    Body-brain system = hardware 2M năm tuổi.
    Input hiện đại = software ~5-200 năm tuổi.
    = MISMATCH TĂNG DẦN — không chỉ ở food/exercise,
      mà ở CÁCH COMPILE KNOWLEDGE.

  ⚠️ KHÔNG NÓI "ngày xưa tốt hơn":
    Type C = advancement CỰC LỚN (access collective knowledge).
    Không ai muốn quay lại 100% Type A (săn hổ để "learn by doing").
    Vấn đề = TYPE A BỊ LOẠI BỎ quá nhiều, quá nhanh.
    Optimal = BALANCE — không phải extreme nào.
```

---

## §1 — 3 COMPILE TYPES TRONG LEARNING CONTEXT

### §1.1 Type A trong learning: trải nghiệm trực tiếp

```
🟢🟡 TYPE A = BODY EXPERIENCE → BODY COMPILE:

  VÍ DỤ TRONG EDUCATION:
    → Học bơi: nhảy xuống nước → body compile motor patterns
    → Học nấu ăn: nếm → cắt → nấu → body compile taste + motor + timing
    → Thí nghiệm hóa: trộn chất → thấy đổi màu → body compile trực tiếp
    → Thực tập: làm thật ở công ty → body compile workflow + social

  ĐẶC ĐIỂM TRONG LEARNING:
    ✅ Multi-modal: thấy + nghe + chạm + ngửi + cảm xúc → chunk SÂU
    ✅ Domain feedback trực tiếp: bơi sai → chìm (reality feedback ngay)
    ✅ Transfer tốt: chunk link với DOMAIN THẬT, không chỉ context lớp
    ❌ Chậm: phải trải nghiệm từng thứ → tốn thời gian
    ❌ Hẹp: chỉ compile cái ĐÃ trải nghiệm
    ❌ Rủi ro: trải nghiệm sai có thể gây hại (bỏng, ngã, thất bại)
```

### §1.2 Type B trong learning: expertise qua practice

```
🟢🟡 TYPE B = PFC-DIRECTED BODY COMPILE QUA NHIỀU NĂM:

  VÍ DỤ TRONG EDUCATION:
    → Nghiên cứu sinh: years trong 1 domain → compiled meta-chunks
    → Nghệ sĩ: luyện hàng nghìn giờ → "ngón tay tự biết"
    → Bác sĩ lâm sàng: years khám bệnh → "nhìn là biết"

  ĐẶC ĐIỂM TRONG LEARNING:
    ✅ Chính xác nhất: domain-calibrated, body-verified
    ✅ Meta-chunks: compress → expert "thấy" nhiều hơn beginner
    ❌ Years required: không shortcut
    ❌ Domain-specific: Einstein expert vật lý + novice cooking

  → Type B hiếm khi xảy ra trong K-12 education.
  → Type B = product of sustained practice SAU graduation.
  → NHƯNG: nền tảng cho Type B = Type A + Type C hồi K-12.
```

### §1.3 Type C trong learning: trust install

```
🟡 TYPE C = TRUST SOURCE → COMPILE SHORT:

  VÍ DỤ TRONG EDUCATION:
    → "Pi = 3.14" → trust thầy cô → compile [pi → tính diện tích]
    → "Trái đất quay quanh mặt trời" → trust sách → compile
    → "Thuốc lá gây ung thư" → trust bác sĩ/PSA → compile
    → "Đạo hàm của x² = 2x" → trust công thức → compile

  ĐẶC ĐIỂM TRONG LEARNING:
    ✅ Nhanh: install trong vài lần tiếp xúc
    ✅ Rộng: access toàn bộ collective knowledge mà không cần trải nghiệm
    ✅ Scalable: 1 thầy → 30 học sinh → 30 chunk installs
    ❌ Phụ thuộc source: trust sai source → compile sai pattern
    ❌ Single-channel thường: chủ yếu nghe/đọc → chunk MỎNG
    ❌ Context-bound: chunk link với "lớp học", không link với domain thật
    ❌ Confabulation risk: PFC explain post-hoc tại sao biết,
       nhưng thực ra = installed, không understood
       (Compile-Taxonomy.md §2.3: Type C accuracy ~30-60% confabulation)

  ⭐ CRITICAL INSIGHT:
    Logic chain VẪN CHẶT CHẼ trong Type C — vì brain chain chunks được.
    Body feedback "chain này đúng" → nhưng "đúng" = đúng TRONG SYSTEM.
    [pi → công thức → đáp án → giáo viên confirm → điểm 10]
    = Chain hoạt động. Body feedback positive. NHƯNG:
    → "Đúng" = đúng trên giấy, đúng trong hệ thống điểm
    → Chưa chắc = đúng ngoài đời, hiểu tại sao đúng
    → Trust chain: sách → thầy cô → hệ thống → KHÔNG phải domain thật
```

### §1.4 Toán học: ví dụ phân tích

```
🟡 VÍ DỤ PI — PHÂN TÍCH QUA 3 LOẠI:

  ARCHIMEDES (Type A/B — người phát hiện):
    → Vẽ đa giác nội tiếp/ngoại tiếp vòng tròn
    → Tăng số cạnh: 6 → 12 → 24 → 48 → 96
    → Tính chu vi → thấy converge về giá trị ~3.14159
    → Body experience: đo, vẽ, tính, sai, sửa, lại tính
    → Domain feedback trực tiếp: geometry match reality
    → Chunk: MULTI-MODAL (visual + motor + logical + discovery emotion)
    → = Type A compile → deepened qua years → Type B

  HỌC SINH (Type C — người học):
    → Thầy cô nói: "pi = 3.14, dùng tính diện tích hình tròn"
    → Làm bài tập: S = pi × r² → ra đáp án → điểm 10
    → Body feedback: "chain này đúng" (đúng trên giấy)
    → Chunk: SINGLE-CHANNEL (nghe → ghi → áp dụng công thức)
    → Trust chain: thầy cô → sách → hệ thống
    → = Type C compile. Logic chặt chẽ. Nhưng chunk MỎNG.

  HỌC SINH TÒ MÒ (Type C → Type A transition):
    → Được dạy pi = 3.14 (Type C install)
    → TỰ đo: lấy dây đo vòng tròn, chia cho đường kính → ~3.14!
    → Body reaction: "Ồ! Đúng thật!" → emotional peak → Type A compile
    → Chunk: upgraded — logic + direct experience + surprise emotion
    → = Type C → verified by Type A = STRONGEST
```

---

## §2 — RESEARCH EVIDENCE: 2 CỰC ĐOAN

### §2.1 Cực đoan A: Pure Type C (chỉ học, không trải nghiệm)

```
⭐ HỌC SINH CHỈ CẮM ĐẦU VÀO HỌC:

  Profile:
    → Phần lớn thời gian = lớp học + sách vở + homework
    → Ít chơi tự do, ít trải nghiệm thực tế, ít giao tiếp ngoài
    → Body-feedback channel: HẸP — chủ yếu "điểm cao/thấp"
    → Chunk density: cao trong academic domain, thấp ở hầu hết domain khác

  Framework predict:
    ① Transfer failure cao — chunks link với "lớp học" context
    ② Body-feedback calibrate hẹp — chỉ biết "điểm cao = đúng"
    ③ Creativity thấp — ít Type A chunks = ít material cho Type 4 linking
    ④ Social skills yếu — ít practice = ít Type A social chunks
    ⑤ Anxiety cao khi gặp novel domain — không có anchor chunks
    ⑥ Confabulation cao — "biết" nhưng biết CÓ THỂ SAI mà không hay
```

### §2.2 Research: Transfer Failure

```
🟢 "INERT KNOWLEDGE" — WHITEHEAD 1929:

  Observation: kiến thức học được nhưng KHÔNG activate trong tình huống thực.
  → Học sinh giải được bài vật lý trên giấy
  → NHƯNG không giải thích được tại sao bóng rơi xuống đất

  Framework lens:
    Type C chunks compile trong context "bài tập vật lý"
    → Chỉ fire khi gặp context tương tự (bài tập, thi)
    → Không fire khi gặp domain thật (bóng rơi ngoài sân)
    → = Chunks link với CONTEXT, không link với DOMAIN

🟢 TRANSFER FAILURE — BARNETT & CECI 2002:

  Meta-analysis: students consistently FAIL to transfer
  classroom knowledge to new contexts.
  → "Near transfer" (bài tương tự) = OK
  → "Far transfer" (context khác hẳn) = rất yếu

  Framework lens:
    Near transfer = cùng context → cùng chunks fire → OK
    Far transfer = khác context → chunks KHÔNG fire → fail
    → Type C chunks = context-bound
    → Type A chunks = domain-bound → transfer TỐT HƠN vì link với domain thật

🟢 ROTE LEARNING VS DEEP LEARNING — MARTON & SÄLJÖ 1976:

  "Surface approach": memorize facts, reproduce on test
  "Deep approach": understand meaning, relate to existing knowledge

  Framework lens:
    Surface = Type C pure (install + reproduce)
    Deep = Type C install + PFC deliberate linking + body-check
    → Deep approach = Type C + Type 4 linking + body verification
    → = Moving TOWARD Type A quality nhưng qua PFC route
```

### §2.3 Research: Play Deprivation

```
🟢 PETER GRAY 2011 — "The Decline of Play and the Rise of
   Psychopathology in Children and Adolescents":

  Data: free play giảm liên tục từ 1955 → cùng thời gian:
    → Anxiety tăng
    → Depression tăng
    → Narcissism tăng
    → Empathy giảm
    → Sense of control giảm (external locus of control tăng)

  Framework lens:
    Free play = Type A compile cho:
      → Social: negotiate, cooperate, conflict resolution
      → Motor: run, climb, balance → body-input calibration
      → Creativity: improvise, imagine, create
      → Autonomy: self-directed → efference copy → agency
      → Risk assessment: fall, get up → body learn limits

    Bớt play = bớt Type A compile ở những domain CRITICAL.
    Thay bằng: thêm structured learning = thêm Type C install.
    → Academic chunks tăng. Life chunks giảm. Net effect = fragile.

🟢 STUART BROWN — "PLAY" (2009):

  Clinical observation: adults deprived of play as children
    → Difficulty with social relationships
    → Rigid thinking, difficulty adapting to change
    → Higher rates of depression

  Framework lens:
    Play deprivation = Type A chunk deficit ở social + creative domains
    → PFC có Type C schemas ("nên giao tiếp thế nào") nhưng body
      KHÔNG có compiled motor/social patterns → awkward, effortful
    → = "Biết lý thuyết giao tiếp" nhưng body chưa compile
```

### §2.4 Research: Finland vs East Asia

```
🟢🟡 FINLAND MODEL:
  → Ít homework (ít nhất OECD)
  → Nhiều giờ chơi tự do, nhiều recess
  → Ít thi chuẩn hóa (không thi quốc gia cho tới 16 tuổi)
  → PISA scores: consistently TOP
  → Student wellbeing: CAO

  Framework lens: BALANCED Type A + Type C
    → Type C: vẫn học, vẫn trust teacher
    → Type A: play + outdoor + practical activities
    → Body-feedback calibrate RỘNG: academic + social + physical
    → Transfer better: Type A chunks link với domain thật

🟢🟡 EAST ASIAN "CRAMMING" MODEL (Hàn, Nhật, Trung):
  → Rất nhiều homework + hagwon/juku (tutoring centers)
  → Ít chơi tự do
  → Nhiều thi chuẩn hóa
  → PISA scores: consistently TOP
  → Student wellbeing: THẤP NHẤT OECD
  → Youth suicide rates: among highest globally

  Framework lens: DOMINANT Type C
    → Chunk density academic RẤT CAO
    → Nhưng: body-feedback calibrate HẸP (chủ yếu "điểm")
    → Ít Type A chunks cho: social, physical, creative, autonomy
    → Kết quả: performance tốt + wellbeing tệ
    → = System tối ưu cho OUTPUT, không tối ưu cho HUMAN

  ⭐ SO SÁNH:
    Cả hai → PISA scores cao (academic chunks OK)
    Finland: + wellbeing cao (balanced Type A/C)
    East Asia: + wellbeing thấp (dominant Type C)
    → Compile TYPE MIX matters, không chỉ chunk density

🟢 OECD PISA Wellbeing reports 2015, 2018
🟢 Korean youth suicide rates: OECD Health Statistics
🟡 Framework analysis: synthesis
```

### §2.5 Research: Montessori vs Traditional

```
🟢 LILLARD & ELSE-QUEST 2006:

  Montessori (hands-on, experiential, mixed-age, self-paced)
  vs Traditional (lecture-based, same-age, teacher-paced)

  Results:
    → Montessori children: better social cognition
    → Better executive function
    → Better at applying knowledge to NEW PROBLEMS
    → Similar or better academic achievement

  Framework lens:
    Montessori = Type A + Type C mix (hands-on + guided)
    Traditional = Type C dominant (lecture + exercise)
    → Montessori: Type A chunks → link with domain → better transfer
    → Traditional: Type C chunks → link with context → worse transfer

🟢 LILLARD 2012 (follow-up review):

  Montessori benefits strongest when implemented with fidelity.
  Watered-down Montessori ≈ Traditional.
  → = It's not the LABEL, it's the actual Type A compile happening.
```

### §2.6 Research: Chinese Learner Paradox

```
🟢 "CHINESE LEARNER PARADOX" — WATKINS & BIGGS 1996:

  Paradox: Chinese students APPEAR to rote learn (Type C)
  nhưng vẫn perform well on tests requiring understanding.

  Resolution: nhiều học sinh Á châu thực hiện
  "repetition WITH understanding" — không chỉ Type C thuần túy.

  = Lặp đi lặp lại CHO TỚI KHI "body feel đúng"
  = Không chỉ memorize → mà lặp cho tới khi HIỂU

  Framework lens:
    → Ban đầu: Type C install ("đạo hàm x² = 2x")
    → Lặp lại: tính đi tính lại → body start recognize pattern
    → Khi body "feel đúng" = Type A verify đang xảy ra
    → Repetition + body-check = Type C → Type A transition
    → ≠ "rote learning" thuần → MÀ là repetition-as-verification

  ⭐ INSIGHT: "Chinese Learner Paradox" KHÔNG paradox nếu nhìn qua framework.
    Repetition CÓ THỂ = verification pathway.
    ĐIỀU KIỆN: repetition + body-check ("mình hiểu thật chưa?")
    Nếu repetition thuần mechanical = vẫn Type C, chỉ mạnh hơn.
```

---

## §3 — TYPE C → TYPE A TRANSITION: "TRUST THEN VERIFY"

### §3.1 Transition mechanism

```
🟡 TYPE C → TYPE A = KHÔNG XÓA TYPE C, MÀ THÊM TYPE A LÊN TRÊN:

  Bước 1: TYPE C INSTALL
    → Thầy cô nói: "pi = 3.14, dùng tính diện tích"
    → Trust gate pass → compile [pi → diện tích] = chunk mỏng
    → Đủ để giải bài tập → body feedback "đúng"

  Bước 2: DOMAIN ENCOUNTER (optional nhưng quan trọng)
    → Học sinh TỰ đo vòng tròn → ra ~3.14
    → HOẶC: làm việc cần tính thể tích bể nước → dùng pi → đúng thật
    → Body reaction: surprise + confirm → emotional peak
    → = Type A compile LẠI cùng concept nhưng multi-modal

  Bước 3: CHUNK UPGRADE
    → Chunk [pi → diện tích] giờ có THÊM:
      + Motor memory (đo)
      + Visual memory (vòng tròn thật)
      + Emotional memory (ồ! đúng thật!)
      + Domain link (thực tế, không chỉ giấy)
    → = Chunk SÂU hơn, RỘNG hơn, TRANSFER tốt hơn

  ⭐ NGUYÊN TẮC:
    Type C install = FAST BOOTSTRAP (nhanh, rộng, access collective)
    Type A verify = QUALITY UPGRADE (sâu, robust, domain-linked)
    OPTIMAL = Type C FIRST → Type A VERIFY → chunk chất lượng cao
    = "TRUST THEN VERIFY" — bằng BODY, không chỉ bằng logic
```

### §3.2 Khi nào Type C ĐỦ (không cần Type A verify)

```
🟡 TYPE C ĐỦ KHI:

  ① Domain abstract + collective verify MẠNH:
    → "Trái đất quay quanh mặt trời" — không thể Type A verify trực tiếp
    → Collective evidence (astronomy, space missions) = đủ trust
    → Type C install = hợp lý, không cần cá nhân tự verify

  ② Risk thấp + utility cao:
    → "Nước sôi ở 100°C" — Type C đủ cho daily use
    → Nếu sai (ở độ cao khác → sôi < 100°C) → hệ quả nhẹ
    → Không cần mọi người tự đo nhiệt kế

  ③ Foundation for next learning:
    → "Bảng cửu chương" → Type C install → dùng làm tool
    → Body verify gián tiếp qua sử dụng thành công liên tục
    → = Repetition verify (Chinese Learner mechanism)

  ⚠️ TYPE C KHÔNG ĐỦ KHI:
    → Domain đòi hỏi PHYSICAL skill (bơi, lái xe, phẫu thuật)
    → Decision-making under uncertainty (business, relationships)
    → Creative work (Type 4 linking cần diverse chunks)
    → Personal values (cần body-check, không chỉ sách nói)
```

### §3.3 Failure: Type C LOCKED (không bao giờ transition)

```
⚠️ TYPE C LOCKED = NGUY HIỂM TINH TẾ:

  Khi nào xảy ra:
    → Học sinh CẮM ĐẦU học 12+ năm
    → Không chơi, không nghịch, không trải nghiệm thực tế
    → Tất cả knowledge = Type C (sách, thầy cô, hệ thống)
    → Tốt nghiệp → gặp real domain → Type C chunks KHÔNG fire

  Biểu hiện:
    → "Học giỏi mà ra trường không biết làm gì"
    → "Biết lý thuyết quản lý nhưng quản lý thất bại"
    → "Điểm cao mà phỏng vấn trượt"
    → "Đọc sách self-help nhưng đời không đổi"

  Framework mechanism:
    → Type C chunks link với CONTEXT "lớp học + sách"
    → Real domain = KHÁC context → chunks không activate
    → PFC confabulate: "tôi biết mà!" — thực ra = confabulation
    → Body-feedback chưa bao giờ calibrate cho domain thật
    → = "BIẾT MÀ KHÔNG LÀM ĐƯỢC" (Compile-Taxonomy.md §7.2)
    → Nhưng ở mức TOÀN DIỆN: không chỉ 1 skill, mà HẦU HẾT life skills

  ⭐ KHÔNG PHẢI LỖI HỌC SINH:
    = Hệ thống ưu tiên Type C install (efficient, scalable)
    = Ít tạo cơ hội Type A verify (tốn thời gian, khó kiểm soát)
    = Body-feedback hệ thống: điểm = thước đo DUY NHẤT
    = Học sinh optimize cho thước đo → rational response to incentive
```

---

## §4 — PER-DOMAIN ANALYSIS

### §4.1 Toán học

```
🟡 TOÁN = DOMAIN ĐẶC BIỆT — TYPE C RẤT HIỆU QUẢ:

  Toán có ĐẶC TÍNH RIÊNG:
    → Internal consistency: axioms → theorems → proofs
    → Self-verifying: chain logic TỰ kiểm tra (sai = contradiction)
    → Abstract: không cần physical verification cho nhiều khái niệm

  TYPE C TRONG TOÁN:
    → Install axioms + rules → chain logic → derive results
    → Body-feedback: "chain smooth" = body confirm logic chain đúng
    → Lặp lại nhiều bài → body compile patterns (Chinese Learner)
    → = Type C CÓ THỂ transition sang Type A qua REPETITION
      (vì toán TỰ verify qua internal consistency)

  NHƯNG — GIỚI HẠN:
    → "Biết giải" ≠ "hiểu tại sao"
    → Học sinh solve x² + 5x + 6 = 0 → ra x = -2, -3
    → NHƯNG không biết: "x² + 5x + 6 TRÔNG như thế nào trên graph?"
    → = Algebraic chunk (Type C) ≠ Geometric understanding (Type A visual)
    → = Liên quan: "inert knowledge" — biết solve, không biết MEAN gì

  OPTIMAL: Type C install rules → Type A visualize → Type B expertise
```

### §4.2 Ngôn ngữ

```
🟡 NGÔN NGỮ = TYPE C + TYPE A TỰ NHIÊN:

  FIRST LANGUAGE (L1):
    → Type A dominant: body trải nghiệm ngôn ngữ trực tiếp
    → Nghe mẹ nói → bắt chước → body compile sound patterns
    → Multi-modal: nghe + thấy miệng + cảm xúc + context thật
    → = Đây là lý do L1 compile MẠNH (Type A natural)

  SECOND LANGUAGE (L2) Ở TRƯỜNG:
    → Type C dominant: học grammar rules, memorize vocabulary
    → "Present perfect = have/has + past participle" → rule install
    → Practice = bài tập trên giấy → Type C context
    → = Tại sao học 10 năm tiếng Anh mà nói không được

  L2 IMMERSION:
    → Type A: sống trong môi trường → body compile trực tiếp
    → Nghe native speakers → body compile natural patterns
    → Social pressure + emotional context → multi-modal
    → = Tại sao du học 1 năm > học trường 10 năm
    → = Type A verify cho Type C installed chunks

  ⭐ INSIGHT:
    Ngôn ngữ = ví dụ rõ nhất cho Type A vs Type C difference.
    Grammar rules (Type C) ≠ fluency (Type A).
    Cần CẢ HAI: Type C cho structure, Type A cho fluency.
```

### §4.3 Lập trình

```
🟡 LẬP TRÌNH = DOMAIN CÓ DOMAIN FEEDBACK TỨC THÌ:

  ĐẶC BIỆT:
    → Code chạy hoặc không chạy → domain feedback NGAY (compile/runtime error)
    → = Type C install rules → Type A verify NGAY khi code chạy
    → = Natural transition mechanism built into domain

  HỌC LẬP TRÌNH KIỂU TYPE C:
    → Đọc sách → học syntax → memorize patterns
    → Biết "for loop syntax" → nhưng chưa viết program thật
    → = Tutorial hell: đọc tutorial → hiểu → nhưng KHÔNG viết được

  HỌC LẬP TRÌNH KIỂU TYPE A:
    → Viết code → run → error → fix → run → works!
    → Body compile: error patterns, debugging flow, architecture feel
    → Multi-modal: visual (code), motor (type), logical (debug), emotional (eureka)
    → = Tại sao "learn by doing" = consensus trong CS education

  ⭐ Lập trình = CLOSEST TO OPTIMAL:
    → Type C install (syntax, concepts) → Type A verify (code runs) = natural
    → Domain feedback cycle = FAST (seconds, not years)
    → Error = NOT FAILURE, = INFORMATION (Type A compile opportunity)
    → = Giải thích tại sao self-taught programmers often outperform CS graduates
      (more Type A compile, less Type C only)
```

### §4.4 Thể thao / Kỹ năng vật lý

```
🟢 THỂ THAO = TYPE A DOMINANT — TYPE C KHÔNG THỂ THAY THẾ:

  Không ai học bơi bằng đọc sách bơi.
  Không ai lái xe bằng xem video lái xe.
  Không ai phẫu thuật bằng nghe giảng phẫu thuật.

  → Body PHẢI trải nghiệm trực tiếp → motor patterns compile
  → Type C có thể ACCELERATE ("giữ tay thẳng, đá chân từ hông")
  → Nhưng Type C KHÔNG THỂ THAY THẾ Type A cho motor skills

  HIERARCHY:
    Type C: biết lý thuyết ("gập đầu gối 90°") → useful as guide
    Type A: body compile motor pattern → bắt buộc, không bypass
    Type B: years practice → expert level (vận động viên chuyên nghiệp)

  ⭐ INSIGHT:
    Thể thao PROOF rằng Type C ≠ Type A.
    Ai cũng đồng ý: không thể học bơi bằng sách.
    Framework extend: CÙNG PRINCIPLE áp dụng cho MỌI domain —
    chỉ khác DEGREE.
    → Bơi: 99% Type A, 1% Type C
    → Toán: 60% Type C, 40% Type A (approximate)
    → Social skills: 70% Type A, 30% Type C
    → Mỗi domain = mix khác nhau. Không ai 100% Type C đủ.
```

### §4.5 Screen / Digital — Compile type YẾU NHẤT

```
🟢🟡 SCREEN = TYPE C THỤ ĐỘNG — YẾU HƠN CẢ TYPE C THƯỜNG:

  Type C thường (lớp học): trust thầy cô (AGENT) → compile
    → Thầy cô = agent mà trẻ có trust relationship
    → Có turn-taking: thầy hỏi → trò đáp → feedback
    → Có social context: bạn bè, tương tác, body-feedback xã hội
    → = Type C qua trust gate HOẠT ĐỘNG

  Type C screen (TV, YouTube, TikTok): trust MÀN HÌNH → compile?
    → Màn hình KHÔNG phải agent mà trẻ trust theo cách trust mẹ
    → Không có turn-taking: TV phát → trẻ nhận THỤ ĐỘNG
    → Không có contingency: hành động của trẻ KHÔNG ảnh hưởng nội dung
    → 2 kênh (visual + auditory) vs 6+ kênh khi chơi thật
    → = Type C KHÔNG ĐẦY ĐỦ — thiếu trust gate, thiếu multi-modal

  🟢 Child-Development-Mechanism.md §2 — 3 parameters screen THUA:

    ┌─────────────────┬─────────────────────────┬───────────────────────┐
    │ Parameter       │ Người thật              │ Màn hình              │
    ├─────────────────┼─────────────────────────┼───────────────────────┤
    │ Contingency     │ CAO — "tôi nói → mẹ đáp"│ THẤP — "TV phát →    │
    │                 │ = hành động TÔI gây ra   │ tôi không gây ra"    │
    ├─────────────────┼─────────────────────────┼───────────────────────┤
    │ Multi-modal     │ 6+ kênh (tactile, motor,│ 2 kênh (visual +     │
    │                 │ proprioceptive, social)  │ auditory) THỤ ĐỘNG   │
    ├─────────────────┼─────────────────────────┼───────────────────────┤
    │ Saliency        │ Mẹ nói "CON ƠI!" =     │ TV nói chung chung = │
    │                 │ relevant cho BODY-NEED   │ generic, không riêng │
    └─────────────────┴─────────────────────────┴───────────────────────┘

  🟢 Natural-Development.md §6.4:
    "Trẻ học ngôn ngữ từ NGƯỜI tốt hơn nhiều so với từ MÀN HÌNH
    (vì: thiếu turn-taking, thiếu social context, thiếu body feedback)"

  🟢 AAP (American Academy of Pediatrics):
    Trẻ <18 tháng: tránh screen (trừ video call)
    Video call = CÓ contingency (bà nói → trẻ đáp → bà cười)
    → = Phân biệt: interactive (Type A element) vs passive (pure receive)
```

### §4.5.1 Trẻ con xem TikTok vs Người lớn xem TikTok

```
🟡 2 NHÓM, CÙNG NỘI DUNG, KHÁC CHUNKS:

  NGƯỜI LỚN xem TikTok:
    → ĐÃ CÓ Type A chunks cho hầu hết nội dung trên screen
    → Thấy phụ nữ nhảy → đã có chunks về phụ nữ (gặp thật, nói thật)
    → Thấy đồ ăn → đã có chunks về vị (nếm thật, nấu thật)
    → Video = KÍCH HOẠT chunks ĐÃ CÓ → body respond dựa trên experience
    → = Stimulation cho existing chunk network
    → VẪN có vấn đề: VTA habituation, wanting without liking
      (Liking-Wanting.md §4.3: "empty scrolling")
      nhưng ÍT NHẤT có anchor chunks từ real life

  TRẺ CON xem TikTok:
    → CHƯA CÓ Type A chunks cho phần lớn nội dung
    → Thấy hình khối, quả nọ quả kia, màu sắc rực rỡ
      → CHƯA TỪNG thấy ngoài đời (so với trẻ)
    → Video install chunks KHÔNG CÓ ANCHOR trong domain thật
    → = Chunks "treo lơ lửng" — compile pattern mà body chưa verify
    → + VTA fire liên tục (~15 giây/video = novelty mới)
    → + Baseline novelty BỊ NÂNG → đồ chơi thật = "chậm, chán"
    → = DOUBLE DAMAGE:
      ① Compile chunks không link với reality
      ② Hijack VTA → làm giảm khả năng Type A compile
        (vì domain thật "không đủ hấp dẫn" nữa)

  ⭐ INSIGHT:
    Người lớn xem TikTok = stimulate existing chunks (vẫn có vấn đề)
    Trẻ con xem TikTok = compile chunks THAY THẾ Type A experience
    → Nguy hiểm hơn RẤT NHIỀU — vì trẻ đang ở giai đoạn
      CẦN Type A nhất (chunk foundation cho cả đời)
```

### §4.5.2 VTA Habituation: Screen → Domain thật = "chán"

```
🟡 CƠ CHẾ VTA HABITUATION (Natural-Development.md §6.4):

  Màn hình: novelty CAO + reward NHANH (mỗi giây = hình mới)
  → VTA quen với nhịp ĐÓ → dopamine baseline nâng
  → Quay lại domain thật (cát, nước, lego, sách):
    → Novelty THẤP hơn (cát vẫn là cát)
    → Reward CHẬM hơn (phải đào, xúc, xây → minutes, không seconds)
    → VTA: "không đủ delta" → KHÔNG fire → body signal "chán"

  = KHÔNG PHẢI đồ chơi thật kém hấp dẫn.
  = MÀ VTA ĐÃ BỊ CALIBRATE cho tốc độ screen.
  = Cùng cơ chế: processed food → thức ăn tự nhiên "nhạt"
    (Core-Software.md §3.3 baseline adaptation)

  HỆ QUẢ:
    → Trẻ "chán mọi thứ" trừ screen = VTA baseline distortion
    → Type A compile opportunity GIẢM (vì trẻ không MUỐN chơi thật)
    → Type C passive install TĂNG (vì screen = path of least resistance)
    → = Vòng lặp tự tăng cường: screen → chán thật → more screen → ...
    → Giống addiction mechanism (Addiction-Analysis.md §2: bypass H10)
```

### §4.5.3 "Học chữ qua TV" vs "Học chữ qua người"

```
🟢🟡 VÍ DỤ CỤ THỂ — HỌC NGÔN NGỮ / CHỮ CÁI / ĐẾM:

  HỌC QUA NGƯỜI (Type A + Type C):
    → Mẹ chỉ: "Đây là chữ A — giống mái nhà!"
    → Trẻ: nhìn (visual) + nghe (auditory) + chỉ tay (motor)
      + mẹ cười (social reward) + context thật (biển hiệu, sách)
    → Contingency: trẻ hỏi → mẹ đáp → trẻ hỏi tiếp
    → = Multi-modal + social + contingency = compile SÂU

  HỌC QUA TV / APP (Type C thụ động):
    → TV nói: "A! Apple! A-A-Apple!"
    → Trẻ: nhìn (visual) + nghe (auditory) = 2 kênh
    → Không contingency: TV nói BẤT KỂ trẻ có nghe không
    → Không social reward: không ai cười khi trẻ nhận ra chữ
    → = 2-channel passive → compile MỎNG

  RESEARCH SUPPORT:
    → 🟢 Trẻ học ngôn ngữ từ NGƯỜI > từ MÀN HÌNH
      (AAP recommendations, multiple studies)
    → 🟢 "Video transfer deficit" — trẻ nhỏ (<3) KHÓ transfer
      kiến thức từ video sang real world (Anderson & Pempek 2005)
    → Framework lens: video = Type C mà không có anchor,
      contingency, hoặc trust gate đầy đủ → compile yếu

  ĐÁNG CHÚ Ý:
    → Trẻ HỌC ĐƯỢC từ screen — nhưng CHẬM HƠN và MỎNG HƠN
    → Không phải screen = zero learning → mà = INFERIOR learning
    → Screen + BỐ MẸ XEM CÙNG + thảo luận = tốt hơn nhiều
      (vì thêm: contingency + social + trust agent)
    → = Natural-Development.md §6.4:
      "Screen = snack / Exploration thật = bữa ăn chính"
```

---

## §5 — LẶP CÓ BODY-CHECK VS LẶP MÁY MÓC

### §5.1 Phân biệt quan trọng nhất

```
⭐⭐ PHÂN BIỆT NÀY = KEY INSIGHT CỦA FILE:

  CÙNG "LẶP LẠI" — NHƯNG 2 CƠ CHẾ HOÀN TOÀN KHÁC:

  LẶP MÁY MÓC (Mechanical Repetition):
    → Lặp đi lặp lại KHÔNG có body-check
    → PFC off, body chạy tự động
    → VD: chép bài 100 lần, memorize flashcard, drill without thinking
    → Kết quả: Type C STRENGTHEN (chunk mạnh hơn, KHÔNG sâu hơn)
    → Pattern: [stimulus → response] NHANH hơn — nhưng CÙNG QUALITY

  LẶP CÓ BODY-CHECK (Verified Repetition):
    → Lặp đi lặp lại VỚI body-check ở mỗi lần
    → "Mình hiểu thật chưa? Cái này feel đúng chưa?"
    → PFC observe + body-vote ở mỗi iteration
    → VD: giải toán → check "tại sao bước này?", chơi nhạc → listen "âm này đúng chưa?"
    → Kết quả: Type C → Type A TRANSITION (chunk upgrade)
    → Pattern: [stimulus → response → body-check → adjust] = DEEPER

  ⭐ SỰ KHÁC BIỆT:

    Mechanical:    [lặp] → chunk MẠNH hơn (same type)
    Body-check:    [lặp + check] → chunk CHUYỂN LOẠI (Type C → Type A)

    Mechanical = chỉ ② Repetition (1 trong 4 compile mechanisms)
    Body-check = ② Repetition + ③ Multi-modal (thêm body-observation channel)
                 + có thể ④ Emotional peak (khi "aha!" xảy ra)
    → = NHIỀU compile mechanisms active hơn → compile SÂU hơn
```

### §5.2 Chinese Learner Paradox = Verified Repetition

```
🟡 GIẢI PARADOX:

  Western view: "Chinese students rote learn" = Mechanical Repetition
  Reality: nhiều Chinese students = Verified Repetition

  Watkins & Biggs 1996: "repetition for understanding"
  → Lặp cho tới khi "nắm" = body-check ở mỗi iteration
  → KHÁC "lặp cho tới khi nhớ" = mechanical

  Framework lens:
    "Nắm" = body feel smooth khi process
    "Nhớ" = retrieval success (có thể vẫn Type C)
    → "Nắm" > "nhớ" — vì "nắm" = Type A verify đã xảy ra

  ⚠️ NHƯNG: KHÔNG PHẢI TẤT CẢ:
    Một số học sinh THẬT SỰ lặp máy móc (mechanical)
    → Chỉ memorize → chưa bao giờ body-check
    → = Type C strengthen, KHÔNG transition
    → = Những học sinh này = TRUE rote learners → transfer failure

  → Paradox = vì Western researchers KHÔNG phân biệt 2 loại lặp.
  → Framework CÓ THỂ phân biệt: mechanical vs body-check repetition.
```

### §5.3 Làm sao biết mình đang lặp loại nào?

```
🟡 SELF-DIAGNOSTIC:

  LẶP MÁY MÓC — dấu hiệu:
    → "Tôi thuộc bài nhưng không giải thích được tại sao"
    → "Tôi làm nhanh nhưng không biết bước nào có thể bỏ"
    → "Đổi format bài → confused"
    → "Tôi biết công thức nhưng không biết khi nào dùng"
    → Body signal: NEUTRAL (không hứng thú, không khó chịu, chỉ... lặp)

  LẶP CÓ BODY-CHECK — dấu hiệu:
    → "À, bước này vì xyz — tôi thấy nó connect với cái kia"
    → "Nếu thay số khác → kết quả change thế nào? Let me check..."
    → "Bài này khác bài trước ở chỗ nào? Tại sao cách giải khác?"
    → Occasional "aha!" moments — body reaction khi connect mới
    → Body signal: ENGAGED (có thể khó, nhưng ALIVE — approach-tagged)

  ⭐ CHỈ CẦN 1 CÂU HỎI:
    "Mình có thể giải thích cho đứa em / bạn bè HIỂU không?"
    → Nếu CÓ = đã body-check, chunk có depth
    → Nếu KHÔNG = chỉ memorize, chunk mỏng
    → (Feynman Technique = essentially body-check via teaching)
```

---

## §6 — HỆ QUẢ CHO THIẾT KẾ GIÁO DỤC

### §6.1 Nguyên lý từ analysis

```
🟡 5 NGUYÊN LÝ RÚT RA:

  ① TYPE C = BOOTSTRAP, KHÔNG PHẢI DESTINATION
    → Type C install = nhanh, rộng, access collective knowledge
    → NHƯNG: Type C alone = fragile, context-bound, confabulation risk
    → Giáo dục NÊN dùng Type C để START, rồi tạo cơ hội Type A verify

  ② MỖI DOMAIN = MỘT MIX KHÁC NHAU
    → Toán: Type C có thể transition qua verified repetition
    → Ngôn ngữ: cần immersion (Type A) — Type C alone = insufficient
    → Thể thao: Type A bắt buộc — Type C chỉ guide
    → Social: Type A bắt buộc — Type C chỉ framework
    → Không có 1 công thức cho tất cả

  ③ PLAY = TYPE A COMPILE INFRASTRUCTURE
    → Play không "phí thời gian" — play = Type A compile
    → Bớt play = bớt Type A = bớt anchor chunks cho transfer
    → Gray 2011: play giảm → mental health issues tăng

  ④ LẶP ≠ LẶP — PHÂN BIỆT MECHANICAL VS BODY-CHECK
    → Mechanical repetition: strengthen Type C (faster, not deeper)
    → Body-check repetition: transition Type C → Type A (deeper)
    → Education system hiếm khi phân biệt 2 loại
    → = Missed opportunity

  ⑤ BODY-FEEDBACK CHANNEL PHẢI RỘNG HƠN "ĐIỂM"
    → Nếu body chỉ biết "điểm cao = đúng" → calibrate hẹp
    → Cần thêm: domain feedback, social feedback, physical feedback
    → = Diversify body-input → robust chunk network
```

### §6.2 Framework predict: OPTIMAL LEARNING FLOW

```
🟡 OPTIMAL FLOW = TYPE C → TYPE A → (TYPE B):

  ┌───────────────────────────────────────────────────┐
  │ Phase 1: TYPE C INSTALL (fast bootstrap)          │
  │  → Thầy cô/sách giới thiệu concept              │
  │  → Trust gate: "thầy cô nói → compile"           │
  │  → Chunk mỏng nhưng NHANH có                     │
  │  → Đủ để bắt đầu practice                        │
  └───────────────┬───────────────────────────────────┘
                  ↓
  ┌───────────────────────────────────────────────────┐
  │ Phase 2: TYPE A VERIFY (quality upgrade)          │
  │  → Thực hành: đo thật, code thật, chơi thật      │
  │  → Domain feedback: đúng thật / sai thật          │
  │  → Body compile multi-modal: xác nhận/bác bỏ     │
  │  → Chunk upgrade: thêm depth, thêm domain-link   │
  └───────────────┬───────────────────────────────────┘
                  ↓
  ┌───────────────────────────────────────────────────┐
  │ Phase 3: VERIFIED REPETITION (consolidate)        │
  │  → Lặp CÓ body-check: "hiểu thật chưa?"         │
  │  → Mỗi lần lặp = 1 verify cycle                  │
  │  → Sleep consolidation giữa sessions              │
  │  → Chunk solidify: robust, transferable           │
  └───────────────┬───────────────────────────────────┘
                  ↓ (years, optional)
  ┌───────────────────────────────────────────────────┐
  │ Phase 4: TYPE B EXPERTISE (deep mastery)          │
  │  → PFC-directed practice qua nhiều năm            │
  │  → Meta-chunks form: expert "thấy" nhiều hơn     │
  │  → = Domain chuyên môn                            │
  └───────────────────────────────────────────────────┘

  ⚠️ Hầu hết education systems CHỈ CÓ Phase 1 + ít Phase 3.
     Phase 2 (verify) = thường thiếu hoặc optional.
     = Tại sao transfer failure là vấn đề phổ biến nhất.
```

---

## §7 — HONEST ASSESSMENT

```
🟢 HIGH CONFIDENCE:
  → Transfer failure research (Barnett & Ceci 2002) — established
  → Inert knowledge (Whitehead 1929) — established concept
  → Play deprivation effects (Gray 2011, Brown 2009) — established correlation
  → Montessori vs Traditional (Lillard 2006) — peer-reviewed
  → Chinese Learner Paradox (Watkins & Biggs 1996) — established
  → Finland vs East Asia PISA + wellbeing data — OECD data
  → Screen < Person cho ngôn ngữ trẻ nhỏ — AAP + multiple studies
  → Video transfer deficit (Anderson & Pempek 2005) — established
  → VTA habituation mechanism — established neuroscience
  → Contingency, multi-modal, saliency parameters — established

🟡 MEDIUM CONFIDENCE (Framework Synthesis):
  ⚠ Type C → Type A transition as unified mechanism
    (each component established, unifying integration = novel)
  ⚠ "Verified repetition" vs "Mechanical repetition" distinction
    (consistent with evidence, framework terminology)
  ⚠ Per-domain compile type mix ratios
    (directional, not measured — e.g., "toán 60% Type C")
  ⚠ Play = Type A compile infrastructure
    (consistent with Gray/Brown, framework framing = novel)
  ⚠ Optimal learning flow 4-phase model
    (each phase established, sequence = framework contribution)
  ⚠ Evolutionary timeline Type A → Type C as mismatch frame
    (each data point established, mismatch framing = novel)
  ⚠ Trẻ con vs người lớn TikTok: "chunks treo lơ lửng" concept
    (consistent with video transfer deficit, framework terminology)
  ⚠ Screen Type C < classroom Type C (trust gate + contingency difference)
    (components established, hierarchy = framework contribution)

🔴 LOW CONFIDENCE:
  ⚠ Specific % estimates (e.g., "60% Type C" cho toán)
    → Calibration anchor, không phải đo lường
  ⚠ Self-taught programmers outperform CS graduates claim
    → Anecdotal + selection bias, not controlled
  ⚠ Feynman Technique = "body-check via teaching"
    → Plausible but not formally tested as body-check mechanism
  ⚠ "Double damage" TikTok trẻ em (compile + VTA hijack)
    → Logical from mechanism, not directly measured as combined effect
```

---

## §8 — CROSS-REFERENCES

```
CORE MECHANISM:
  Compile-Taxonomy.md v1.1  — 3 Loại A/B/C, 4 pathways, 6 trade-offs
  Chunk.md v2.1             — 4 compile mechanisms, trust gate
  Collective-Body.md v1.1   — trust = only bridge, Model 3 cấp
  Body-Base.md v2.0         — "body evaluates patterns, not reality"
  Body-Feedback.md          — Dual-Pull, H10, 3 nguồn feedback

EDUCATION:
  Education-Mechanism.md    — arc design principles (HOW thiết kế bài học)
  Domain-Knowledge-Map.md   — nhóm kiến thức per era (WHAT dạy)
  Education-Arms-Race.md    — observation: competition spiral
  Expansion-Saturation-Crisis.md — grad unemployment, domain shift

CHILD DEVELOPMENT:
  Natural-Development.md    — §6.4 screen time, VTA habituation, snack vs bữa chính
  Child-Development-Mechanism.md — §2 compile parameters (contingency, multi-modal, saliency)
  Skill-Introduction.md     — person vs screen learning examples

RELATED ANALYSIS:
  Blackbox-Map.md           — 5 gaps (file này = application of Gap 3 insight)
  Liking-Wanting.md §4.3    — TikTok scroll: wanting without liking
  Addiction-Analysis.md     — hijack mechanism, bypass H10
  Feeling-Accuracy.md       — 6 error modes (body-check limitations)
  Logic-Feeling-Balance.md  — meta-principle: mỗi người tự cân bằng
  Core-Software.md §2       — Ancestral Domain, modern mismatch
  Core-Software.md §3.3     — Baseline adaptation mechanism (delta rule)

KEY RESEARCH CITATIONS:
  Whitehead 1929            — Inert knowledge
  Barnett & Ceci 2002       — Transfer failure meta-analysis
  Marton & Säljö 1976       — Surface vs deep approach
  Gray 2011                 — Play deprivation + psychopathology
  Brown 2009                — Play clinical observation
  Lillard & Else-Quest 2006 — Montessori vs Traditional
  Lillard 2012              — Montessori fidelity review
  Watkins & Biggs 1996      — Chinese Learner Paradox
  Anderson & Pempek 2005    — Video transfer deficit in young children
  AAP 2016                  — Screen time recommendations
  OECD PISA 2015, 2018      — Wellbeing data Finland vs East Asia
```

---

> *Compile-Type-Learning v1.1 — "3 compile types tạo 3 loại chunk quality khác nhau
> trong learning. Type C (trust install) = nhanh, rộng, nhưng context-bound,
> confabulation risk cao. Type A (direct experience) = chậm, hẹp, nhưng robust,
> domain-linked, transfer tốt. Optimal = Type C bootstrap → Type A verify.
> Repetition ≠ repetition: mechanical (strengthen same type) vs body-check
> (transition C→A). Finland balanced (A+C) → wellbeing + performance.
> East Asian cramming (C dominant) → performance + low wellbeing.
> Play = Type A compile infrastructure. Giáo dục thiếu Phase 2 (verify)
> = transfer failure phổ biến nhất.
> v1.1: §0.1 Evolutionary context (2M năm Type A → 200 năm Type C dominant
> → 5 năm TikTok = tốc độ cực đại). §4.5 Screen/Digital analysis
> (trẻ vs người lớn TikTok, VTA habituation, học chữ qua TV vs người)."*
