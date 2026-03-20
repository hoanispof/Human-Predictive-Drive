# Hóa Chất Thần Kinh — Kiến Trúc 3 Lớp (v8 Draft)

> **Trạng thái:** DRAFT cho v8.0 — song song với Neurochemistry.md (v6 legacy)
> **Ngày:** 2026-03-20
> **Mục đích:** Tái cấu trúc theo Lớp 1/2/3 + insights mới (Schema-Drive, receptor variants)
> **Reference:** Neurochemistry.md (v6 legacy — chi tiết research, gen markers, đo lường)
> **Khi build v8:** đọc CẢ 2 file → merge thành 1 file chất lượng cao nhất

---

## 1. Kiến Trúc 3 Lớp — Tổng Quan

```
CŨ (v6): 3 kênh gốc + phụ gia (flat list)
MỚI (v8): 3 LỚP hierarchy (Source → Amplifier → Modulator)

╔══════════════════════════════════════════════════════════╗
║  LỚP 1: SOURCE — "Cơ thể MUỐN gì?"                      ║
║  = 2 nguồn reward DUY NHẤT → nơi body THỰC SỰ trả thưởng ║
║  Opioid (Experience) · Oxytocin (Connection)              ║
║  → 10 sub-channels: E1-E5 + C1-C5                        ║
║  → Chi tiết sub-channels: Layer1-Channels.md              ║
╠══════════════════════════════════════════════════════════╣
║  LỚP 2: AMPLIFIER — "Mạnh cỡ nào? Hướng nào?"           ║
║  = SIGNAL + KHUẾCH ĐẠI → không tạo reward riêng          ║
║  Dopamine (Novelty/Signal) · Serotonin (Status/Multiply)  ║
╠══════════════════════════════════════════════════════════╣
║  LỚP 3: MODULATOR — "Tinh chỉnh"                         ║
║  = ĐIỀU CHỈNH cách Lớp 1+2 hoạt động                     ║
║  Cortisol · NE · Vasopressin · Prolactin · Endocannabinoid║
╚══════════════════════════════════════════════════════════╝

NGUYÊN TẮC:
  Lớp 1 = NƠI body thực sự trả thưởng (ground truth)
  Lớp 2 = AMPLIFY + SIGNAL cho Lớp 1 (không tự tạo reward)
  Lớp 3 = FINE-TUNE cách Lớp 1+2 hoạt động (không tạo gì mới)
  → Mọi thứ PHỤC VỤ Lớp 1 → Lớp 1 = body → body = ground truth
```

---

## 2. LỚP 1: SOURCE — Opioid + Oxytocin

### 2.1 Opioid — Experience Channel

```
HỆ THỐNG: mu-opioid receptors (toàn thân: não + ruột + da + cơ)
CHỨC NĂNG: body SƯỚNG — "thưởng thức, tận hưởng, cảm nhận"

  Khi fire: "NGON! ĐẸP! SƯỚNG! HIỂU RỒI!" → body reward THẬT
  Khi thiếu: anhedonia ("biết ngon nhưng không thấy ngon") → nhạt nhẽo

5 SUB-CHANNELS (chi tiết → Layer1-Channels.md):
  E1: Sensory    — giác quan trực tiếp (taste, touch, visual, audio, smell)
  E2: Mastery    — giỏi lên ("tôi làm được!")
  E3: Coherence  — hiểu, đồng bộ ("à ha! khớp rồi!")
  E4: Aesthetic   — vẻ đẹp (art, nature, music pattern, design)
  E5: Comfort    — thoải mái (ấm áp, an ổn, relaxation)

ĐẶC ĐIỂM:
  → Body-WIDE: opioid receptors ở KHẮP cơ thể (không chỉ não)
  → "Ấm lòng" = literal (opioid ở ngực)
  → "Gut feeling ngon" = literal (opioid ở ruột)
  → = Body CẢM reward, không chỉ "não biết" reward
  → TOLERANCE: lặp lại → receptor downregulate → cần nhiều hơn
  → → Tại sao "lần đầu sướng nhất" → tolerance → cần novelty REFRESH

🟢 Research: Berridge & Robinson (1998, 2016) — "Liking" system
🟢 Research: Peciña et al. (2006) — hedonic hotspots in brain
→ Chi tiết: Neurochemistry.md (v6) §3
```

### 2.2 Oxytocin — Connection Channel

```
HỆ THỐNG: oxytocin receptors (não + tim + da + tử cung)
CHỨC NĂNG: body ẤM — "kết nối, thuộc về, được hiểu"

  Khi fire: "ẤM! AN TOÀN! THUỘC VỀ! ĐƯỢC HIỂU!" → body reward THẬT
  Khi thiếu: cô đơn → body dùng CÙNG circuits physical pain → ĐAU THẬT

5 SUB-CHANNELS (chi tiết → Layer1-Channels.md):
  C1: Intimate        — thân thiết sâu 1-1 (partner, bạn thân nhất)
  C2: Belonging       — thuộc về nhóm (gia đình, team, community)
  C3: Being Seen      — được thấu hiểu ("ai đó THẬT SỰ thấy tôi")
  C4: Physical Touch  — tiếp xúc vật lý (ôm, nắm tay, da-kề-da)
  C5: Shared Experience — cùng trải nghiệm (cùng cười, cùng khóc, cùng vượt khó)

ĐẶC ĐIỂM:
  → Body-WIDE: oxytocin ở tim, da, não → "ấm" = TOÀN THÂN
  → KHÔNG tolerance (khác opioid): ôm lần 10,000 VẪN ấm
  → → Tại sao Connection BỀN HƠN Experience: opioid tolerance, oxytocin KHÔNG
  → Social pain = physical pain circuits (Eisenberger 2003)
  → → Cô đơn KHÔNG phải "trong đầu" → body ĐAU THẬT

🟢 Research: Kosfeld et al. (2005) — oxytocin + trust
🟢 Research: Eisenberger (2003) — social rejection = physical pain circuits
→ Chi tiết: Neurochemistry.md (v6) §4
```

### 2.3 Opioid × Oxytocin — MULTI-CHANNEL

```
Nhiều trải nghiệm FIRE CẢ 2 cùng lúc:

  Ăn cùng bạn: E1 (taste) + C5 (shared) + C2 (belonging)
  Sex: E1 (sensory) + C1 (intimate) + C4 (touch)
  Nghe nhạc cùng nhau: E4 (aesthetic) + C5 (shared)
  Nấu cho người thân: E2 (mastery) + C1 (intimate)

  → Multi-channel = reward MẠNH HƠN single channel
  → "Ăn cùng bạn ngon hơn ăn 1 mình" = E1 + C5 > E1 alone
  → → Thiết kế cuộc sống: CỐ multi-channel mỗi hoạt động → reward TĂNG
```

---

## 3. LỚP 2: AMPLIFIER — Dopamine + Serotonin

### 3.1 Dopamine — Novelty Signal + Nhiên Liệu Sáng Tạo

```
HỆ THỐNG: VTA → Nucleus Accumbens (mesolimbic pathway)
CHỨC NĂNG KÉP:

  FUNCTION A — Schema-Drive SIGNAL:
    Fire khi: desire approaching / matched ("gần rồi! khớp rồi!")
    Suppress khi: desire NOT matched ("không phải cái cần")
    = KHÔNG phải "surprise signal" (RPE cũ)
    = "Desire fulfillment signal" (Schema-Drive mới)

  FUNCTION B — NHIÊN LIỆU SÁNG TẠO:
    BUILD schema: explore, learn, connect, imagine, chain cross-domain
    = Dopamine drive NÃO tìm kiếm, thử nghiệm, kết nối CÁI MỚI
    = "Tò mò" = dopamine → "Eureka" = opioid (dopamine DẪN tới opioid)
    → Dopamine KHÔNG phải reward → dopamine DẪN TỚI reward (qua Lớp 1)

  DOPAMINE + CORTISOL BỔ SUNG NHAU:
    Dopamine = BUILD schema (sáng tạo, học, explore)
    Cortisol = EXECUTE schema (triển khai hành vi thực tế, tốn sức)
    Chỉ Dopamine: "nghĩ hay nhưng chả làm gì" → philosopher mode
    Chỉ Cortisol: "làm cật lực nhưng không sáng tạo" → robot mode
    Cả 2 vừa đủ: "nghĩ hay VÀ làm thật" → productive creative mode

HARDWARE VARIANTS ảnh hưởng dopamine:
  DRD4 7-repeat: receptor KÉM hiệu quả → cần MORE stimulation → "chán nhanh"
    → ~20% dân số → consistent với ~15-20% improviser tendency
  COMT Val/Val: dopamine CLEAR NHANH ở PFC → flexible nhưng unstable
    → Switch context DỄ → improviser tendency
  COMT Met/Met: dopamine GIỮ LÂU ở PFC → stable nhưng less flexible
    → Maintain focus TỐT → specialist tendency
  MAO-A variants: enzyme phân hủy dopamine/serotonin → tốc độ KHÁC
    → HIGH MAO-A: clear nhanh → cần spike MỚI sớm hơn

  → "Chán nhanh" vs "kiên trì" = HARDWARE receptor KHÁC NHAU
  → KHÔNG phải "lỗi" hay "ý chí" → là VARIANT (cả 2 cần cho xã hội)
  → Chi tiết: PFC-Analysis.md §8

⚠️ Novelty = channel GỐC hay infrastructure?
  → Test: Novelty detect → cảm xúc GÌ? → LUÔN opioid/oxytocin đi kèm
  → Novelty alone (mới nhưng không đẹp/ngon/hay) = PE ≈ 0
  → → Novelty CÓ THỂ = infrastructure (detection) không phải source (reward)
  → → Framework TREAT as channel (predictive power) → bản chất ghi nhận
  → Chi tiết: UD-Hypothesis.md §Q-NEW-7

🟢 Research: Schultz (1997) — dopamine = PE signal (UD mở rộng: = Schema-Drive signal)
🟢 Research: Berridge (1998) — wanting ≠ liking (dopamine ≠ opioid)
🟢 Research: Ebstein et al. (1996) — DRD4 + novelty-seeking
🟢 Research: Egan et al. (2001) — COMT + PFC flexibility
→ Chi tiết: Neurochemistry.md (v6) §2
```

### 3.2 Serotonin — Status Position Amplifier

```
HỆ THỐNG: raphe nuclei → widespread (brain + GUT — 90% serotonin ở ruột!)
CHỨC NĂNG: AMPLIFY toàn bộ channels khi STATUS POSITION cao

  ⚠️ STATUS = 2 THAM SỐ TÁCH BIỆT (framework đề xuất):

  STATUS POSITION (serotonin — NẰM Ở ĐÂY, Lớp 2 Amplifier):
    = "Tôi ĐANG ở vị trí NÀO trong tập thể?"
    = Mức TỰ TIN hiện tại → body CẢM NHẬN (không phải PFC logic)
    = AMPLIFY MỌI channel: mở/đóng "cửa" cho schemas drive

    Serotonin CAO (Position cao): "tôi xứng đáng"
      → MỞ CỬA: nhiều schemas "dám" drive → hành vi PHONG PHÚ
      → Amplify: ăn NGON hơn, explore RỘNG hơn, connect DỄ hơn
      → = KHÔNG tạo reward → NHÂN ĐÔI reward có sẵn

    Serotonin THẤP (Position thấp): "tôi chưa xứng"
      → ĐÓNG CỬA: ít schemas "dám" → hành vi HẠN CHẾ
      → "Không dám" dù schema CÓ → vì "cửa" đóng
      → So sánh nhiều, bất mãn, "chưa đủ tư cách"

  STATUS ASPIRATION (schema — KHÔNG nằm ở đây, nằm trong Schema-Drive):
    = "Tôi MUỐN ở vị trí NÀO?"
    = Gap = Aspiration − Position → TẠO drive (nếu gap > 0)
    = KHÁC kênh hóa học: cortisol (gap stress) + dopamine (chase)
    = NẰM trong Schema-Drive vì: aspiration = 1 loại "mong muốn của schema"
    → Chi tiết: Status-Analysis.md

  ⚠️ Serotonin ≠ channel gốc:
    Strip hết opioid + oxytocin → serotonin ALONE = NOTHING
    "Nghiện địa vị" thực chất = nghiện MULTI-CHANNEL reward mà status mang lại
    CEO cô đơn + nhàm chán = depressed DÙ status cao → vì Lớp 1 TRỐNG
    → Serotonin × 0 (Lớp 1 thiếu) = vẫn 0

  Tình yêu (infatuation): serotonin GIẢM ~40% (Marazziti 1999)
    → = GẦN BẰNG OCD level → obsessive thinking about partner
    → "Nghĩ về người đó MÃI" = serotonin thấp → không filter được
    → Feature: tạm "hack" để pair-bonding → 12-18 tháng → normalize

🟢 Research: Raleigh et al. (1991) — khỉ alpha → serotonin +200%
🟢 Research: Crockett et al. (2008) — serotonin + social behavior
🟢 Research: Marazziti et al. (1999) — serotonin giảm khi yêu ≈ OCD
🔴 Framework: tách Position vs Aspiration — chưa có research trực tiếp
→ Chi tiết suy luận: Status-Analysis.md
→ Chi tiết legacy: Neurochemistry.md (v6) §5
```

---

## 4. LỚP 3: MODULATOR — 5 Chất Tinh Chỉnh

### 4.1 Cortisol — Nhiên Liệu Kích Hoạt Schema

```
HỆ THỐNG: HPA axis (hypothalamus → pituitary → adrenal glands)
CHỨC NĂNG: KÍCH HOẠT schema triển khai hành vi thực tế

  = "Nhiên liệu cho schema CHẠY" — không chỉ "phanh/threat"

  3 MỨC:
    VỪA ĐỦ: schema KÍCH HOẠT + PFC VẪN available
      → Productive: vừa drive vừa có trọng tài sắp xếp
      → = SWEET SPOT (Yerkes-Dodson optimal arousal)
      → Ví dụ: deadline hợp lý → focus + creative + execute

    QUÁ THẤP: schema KHÔNG có động lực triển khai
      → Stagnant: "biết cần làm nhưng chả muốn" → nằm nhà
      → PFC available nhưng KHÔNG có gì cần PFC arbitrate
      → Ví dụ: trúng số → cortisol ≈ 0 → "giờ làm gì?" → stagnant

    QUÁ CAO: PFC BỊ SỤP + schema mạnh nhất AUTO-WIN
      → Burnout: làm mà không hiệu quả, không sáng tạo
      → Amygdala override PFC → survival mode → chỉ react, không create
      → Ví dụ: sếp la + deadline + con bệnh → cortisol MAX → "chạy" nhưng hỗn loạn

  CORTISOL + DOPAMINE BỔ SUNG:
    Dopamine BUILD schema (sáng tạo) + Cortisol EXECUTE schema (triển khai)
    → Dopamine = architect (thiết kế) + Cortisol = builder (xây)
    → CẦN CẢ 2 cho output thật trong cuộc sống

  CORTISOL BASELINE = BODY CARRY:
    → Cortisol baseline hình thành qua NĂM (stress mãn tính → body adapt)
    → Switch context → cortisol baseline MANG THEO (không reset ngay)
    → "Đi đâu cũng căng thẳng" = cortisol baseline CAO → carry mọi nơi
    → Chi tiết: Threshold-Analysis.md §3.4

🟢 Research: Yerkes-Dodson (1908) — inverted U performance curve
🟢 Research: McEwen (2007) — allostatic load (chronic stress)
→ Chi tiết: Neurochemistry.md (v6) §6
```

### 4.2 NE (Norepinephrine) — Spotlight Attention

```
HỆ THỐNG: locus coeruleus → widespread
CHỨC NĂNG: FOCUS attention vào schema đang active

  = "Đèn spotlight" — chiếu vào 1 thứ → thấy RÕ, phần còn lại TỐI

  NE tăng: focus HẸP + SÂU → intensive processing
  NE thấp: focus RỘNG + NÔNG → daydream, mind wandering

  NE + Cortisol: focus + urgent → "cày xuyên đêm" (intense nhưng TỐN)
  NE − Cortisol: focus + bình tĩnh → flow state (intense nhưng BỀN)

  KHÔNG chọn schema → AMPLIFY schema đang dominant:
    → Schema "deadline!" dominant → NE focus VÀO task → execute nhanh
    → Schema "tò mò" dominant → NE focus VÀO explore → learn nhanh
    → = Modulator: không tạo hướng → amplify hướng ĐÃ CÓ

  Caffeine = NE booster → tại sao cafe giúp focus
  ADHD = NE + dopamine baseline THẤP → focus KHÔNG ổn định
    → ADHD meds (Adderall, Ritalin): tăng NE + dopamine → focus ĐƯỢC
    → = Hardware NE system yếu → cần chemical support

🟢 Research: Aston-Jones & Cohen (2005) — NE + adaptive gain theory
→ Chi tiết: Neurochemistry.md (v6) §7
```

### 4.3 Vasopressin — Lính Gác Bảo Vệ Bond

```
HỆ THỐNG: hypothalamus → widespread (brain + kidneys)
CHỨC NĂNG: BẢO VỆ những gì oxytocin đã kết nối

  Oxytocin TẠO bond → Vasopressin BẢO VỆ bond
  = Oxytocin mở cửa chào khách → Vasopressin đóng cửa đuổi kẻ trộm

  Khi ai đe dọa BOND (partner, con, gia đình, territory):
    → Vasopressin fire → defensive / aggressive response
    → Tim đập nhanh, cơ căng, sẵn sàng CHIẾN

  BIỂU HIỆN:
    Ghen tuông: "ai đe dọa partner CỦA TÔI" → vasopressin → defense/aggression
    Bảo vệ con: "ai đe dọa con TÔI" → vasopressin MẠNH → "mama bear / papa wolf"
    Territorial: "nhà TÔI, chỗ TÔI, ý tưởng TÔI" → ai xâm phạm → khó chịu
    Loyalty: "team TÔI, người TÔI" → bảo vệ group → in-group vs out-group

  VỪA ĐỦ: protective, loyal, caring → BẢO VỆ connection → TỐT
  QUÁ MẠNH: possessive, controlling, aggressive → PHÁ connection → XẤU

  HARDWARE: AVPR1A gene variants → vasopressin receptor sensitivity KHÁC per person
    → Tại sao: cùng tình huống → người ghen DỮ, người KHÔNG ghen → hardware khác

  ⚠️ Vasopressin MẠNH hơn ở NAM (testosterone amplify vasopressin)
    → Oxytocin MẠNH hơn ở NỮ (estrogen amplify oxytocin)
    → = Không absolute → nhưng TENDENCY: nam territorial hơn, nữ bonding hơn
    → = Hardware difference, không phải "văn hóa" alone

🟡 Research: Walum et al. (2008) — AVPR1A + pair bonding
🟢 Research: Carter (1998) — vasopressin + territorial behavior in voles
→ Chi tiết: Neurochemistry.md (v6) §8
```

### 4.4 Satisfaction Signal (Prolactin = candidate chính)

```
⚠️ PHÂN BIỆT CHỨC NĂNG vs HORMONE:
  CHỨC NĂNG: "Satisfaction Signal" = cơ chế body báo "ĐỦ RỒI"
    → Framework bind CHỨC NĂNG → đúng bất kể hormone nào thực hiện
    → Core dùng "Satisfaction Signal" (chức năng)
  HORMONE: Prolactin = candidate CHÍNH (proven: sex, food)
    → CÓ THỂ có hormone KHÁC cùng tham gia (chưa biết hết)
    → File này dùng "prolactin" vì phân tích CHUYÊN SÂU hormone cụ thể
    → Chi tiết suy luận: Prolactin-Analysis.md

HỆ THỐNG: pituitary gland → widespread
CHỨC NĂNG: "ĐỦ RỒI" signal → dừng chase → chuyển sang rest

  = HARDWARE TRANSLATOR: "fulfill bao nhiêu → đủ bao nhiêu"
    Schema fulfill → body channels activate → prolactin release TƯƠNG XỨNG
    → Prolactin TẠO cảm giác "đủ rồi" → body DỪNG
    = Trigger chuyển GĐ3 (Sướng) → GĐ4 (Ok) trong 5 giai đoạn cycle

    Evidence: block prolactin (cabergoline) → "KHÔNG BAO GIỜ đủ" dù đã fulfill
    → Exton et al. (2001): block prolactin → refractory period GẦN ZERO
    → = Prolactin CẦN THIẾT để dừng, không chỉ signal thụ động

  BIỂU HIỆN:
    Sau orgasm: prolactin → refractory period → "đủ, nghỉ"
    Sau ăn no: prolactin → satiation → "đủ, dừng ăn"
    Sau cho con bú: prolactin → nurturing calm → "bình an"
    Sau hoàn thành task: prolactin → satisfaction → "xong, move on"

  MULTI-CHANNEL fulfill → prolactin MẠNH HƠN:
    Ăn cùng gia đình: opioid(ngon) + oxytocin(ấm) → prolactin CAO → no nhanh + satisfied
    Ăn một mình scroll MXH: opioid nhẹ + dopamine(scroll) → prolactin THẤP → ăn MÃI
    Xem phim cùng bạn: opioid(hay) + oxytocin(shared) → prolactin → "xong, hay!" → move on
    Xem phim một mình: opioid(hay) → prolactin YẾU → "xem thêm phim khác" → scroll
    → = Lớp 1 multi-channel (E+C đồng thời) → prolactin MẠNH → dừng DỄ + satisfied
    → = Lớp 2 dopamine alone hoặc Lớp 1 single → prolactin YẾU → khó dừng → loop

    ⚠️ Dừng = CẢ 2 cơ chế đồng thời:
      Hardware: oxytocin AMPLIFY prolactin release (Brody & Krüger 2006)
      Software: multi-schema fulfilled cùng lúc → brain: "toàn bộ đã đáp ứng"
      → Cả 2 contribute → không chỉ 1 yếu tố

  ADDICTION LINK:
    Addiction = prolactin system BỊ BYPASS:
      Cocaine: dopamine FLOOD → prolactin SUPPRESS → "không bao giờ đủ"
      MXH scroll: micro-dopamine liên tục → prolactin KHÔNG KỊP release giữa posts
      Game gacha: random reward → dopamine spike → prolactin KHÔNG stable
    → "Không dừng được" = prolactin system KHÔNG fire → "nút dừng" hỏng
    → Chi tiết: Addiction-Analysis.md

  PROLACTIN BỊ ẢNH HƯỞNG BỞI 3 YẾU TỐ:

    ① CHANNEL COUNT (bao nhiêu kênh Lớp 1 active):
       Multi-channel (E+C đồng thời) → prolactin CAO → dừng DỄ + satisfied
       Single-channel (chỉ E hoặc chỉ dopamine) → prolactin THẤP → dừng KHÓ

    ② SCHEMA FULFILL (schema thỏa mãn cỡ nào):
       Deep schema fulfilled → body respond MẠNH → prolactin CAO
       Surface schema only → body respond NHẸ → prolactin THẤP

    ③ HARDWARE (receptor + dopamine-prolactin balance):
       Prolactin receptor density: gen quy định → nhạy hay kém → "đủ" SỚM hay MUỘN
       Dopamine-Prolactin seesaw: dopamine SUPPRESS prolactin (tonic inhibition)
         → Dopamine CAO (DRD4 7-repeat?) → prolactin BỊ SUPPRESS → khó "đủ" → khó dừng
         → Dopamine THẤP (DRD4 4-repeat?) → prolactin DỄ release → dễ "đủ" → dễ dừng
       → = Tại sao improviser "chán nhanh": dopamine suppress prolactin = "nút dừng" YẾU
       → = Tại sao specialist "kiên trì": prolactin dễ fire = "nút dừng" MẠNH
       → = CÙNG fulfill → KHÁC hardware → KHÁC "đủ" → KHÁC hành vi

    → "Dễ dừng" = emergent từ CẢ 3: channels × schema × hardware
    → FIX "khó dừng" (cho improviser hoặc ai đó):
      → Tăng channel count: multi-channel experience (E+C đồng thời)
      → Fulfill deep schema: không chỉ surface dopamine
      → Hardware: KHÔNG fix được → nhưng BIẾT → adjust strategy:
        Improviser: thiết kế NATURAL ENDPOINTS + multi-channel → bù prolactin yếu
        Specialist: có thể push thêm chút → prolactin vẫn đủ hold

🟢 Research: Krüger et al. (2003) — prolactin + sexual satiation
🟢 Research: Brody & Krüger (2006) — prolactin + orgasm quality × relationship
🟢 Research: Exton et al. (2001) — cabergoline block prolactin → no refractory
🟢 Research: Ben-Jonathan & Hnasko (2001) — dopamine tonic inhibition of prolactin
🟡 Research: Leeners et al. (2013) — prolactin + subjective satisfaction
🟡 Inference: DRD4 → dopamine → prolactin suppression (cơ sở có, chưa test trực tiếp)
→ Chi tiết: Neurochemistry.md (v6) §9
```

### 4.5 Endocannabinoid — Giảm Xóc Body

```
HỆ THỐNG: CB1/CB2 receptors (brain + immune + peripheral)
CHỨC NĂNG: DAMPEN negative signals → body SMOOTH hơn

  = "Bộ giảm xóc" — body liên tục bị "rung" (stress, pain, discomfort)
  → Endocannabinoid giảm rung → feel better

  BIỂU HIỆN:
    Runner's high: chạy 20+ phút → endo-CB release → euphoria
      (nghiên cứu MỚI: KHÔNG phải endorphin → là endocannabinoid)
    Stress buffer: endo-CB DAMPEN cortisol response → "chịu được"
    Pain modulation: endo-CB giảm pain signal → bearable
    Mood regulation: endo-CB baseline → tâm trạng ỔN ĐỊNH

  EXERCISE = MAINTENANCE cho endo-CB system:
    Tập thể dục → endo-CB release → body buffer RESTORED
    Thiếu tập → endo-CB THẤP → mọi stress TÁC ĐỘNG mạnh hơn

    Ví dụ phổ thông:
      "Tuần nào tập đều → stress ÍT ảnh hưởng"
      "Tuần nào bỏ tập → bỗng dưng mọi thứ CĂNG hơn dù cuộc sống KHÔNG đổi"
      → = Cùng cuộc sống → KHÁC endo-CB level → KHÁC cảm nhận stress

    → Tại sao "tập thể dục = nền tảng mọi thứ":
      KHÔNG chỉ vì cơ bắp/tim → mà vì MAINTAIN shock absorber system
      Bỏ tập = shock absorber HƯ → cùng đường xóc nhưng FEEL xóc GẤP ĐÔI

  CANNABIS target CHÍNH XÁC hệ thống này:
    THC = nhân tạo endocannabinoid → "relax + pain relief + munchies"
    Dùng lâu: body NGỪNG tự sản xuất endo-CB → cai = anxiety + pain TĂNG
    → = Outsource shock absorber → body KHÔNG TỰ LÀM nữa → dependent

  KHÔNG PHẢI reward (khác opioid):
    → Endo-CB = GIẢM negative → KHÔNG phải TĂNG positive
    → "Bớt khổ" ≠ "thêm sướng" → nhưng net = feel better
    → = Indirect contribution cho wellbeing

🟢 Research: Fuss et al. (2015) — runner's high = endocannabinoid (not endorphin)
🟡 Research: Hill & Tasker (2012) — endocannabinoid + stress buffering
→ Chi tiết: Neurochemistry.md (v6) — chưa có section riêng (MỚI cho v8)
```

---

## 5. Tương Tác Giữa 3 Lớp

```
LUỒNG CHÍNH:

  Lớp 3 ĐIỀU CHỈNH → Lớp 2 AMPLIFY → Lớp 1 REWARD:

  Cortisol (Lớp 3): "có vấn đề!" → set PRIORITY
    → Dopamine (Lớp 2): "tìm cách giải quyết!" → SEARCH
      → Opioid (Lớp 1): "giải quyết được → SƯỚNG!" → REWARD
      → Oxytocin (Lớp 1): "có người giúp → ẤM!" → REWARD
    → Serotonin (Lớp 2): "giải quyết tốt → TÔI GIỎI!" → AMPLIFY reward
  → Prolactin (Lớp 3): "đủ rồi" → DỪNG → chuyển GĐ tiếp

  NE (Lớp 3): FOCUS attention vào schema đang active → Lớp 2 effective hơn
  Vasopressin (Lớp 3): BẢO VỆ bonds → Oxytocin (Lớp 1) connections AN TOÀN
  Endo-CB (Lớp 3): DAMPEN negative → Lớp 1 rewards FEEL rõ hơn (less noise)

DOPAMINE × CORTISOL (quan trọng nhất):
  Dopamine = BUILD (sáng tạo, khám phá, học tập)
  Cortisol = EXECUTE (triển khai, hành động, tốn sức)
  → Cả 2 = creative + productive
  → Thiếu 1 = hoặc "mơ mộng" hoặc "robot"

MULTI-CHANNEL × PROLACTIN (quan trọng cho addiction):
  Multi-channel Lớp 1 (E+C) → prolactin MẠNH → dừng DỄ → satisfied
  Single channel Lớp 2 (dopamine) → prolactin YẾU → khó dừng → loop
  → = Lớp 1 feed → prolactin → healthy cycle
  → = Lớp 2 alone → prolactin skip → addiction cycle

  ⚠️ Prolactin CROSS-INFLUENCE mọi cycle (không chỉ sex/ăn):
    Novelty cycle: prolactin yếu → "chưa đủ explore" → improviser
    Status cycle: prolactin yếu → "chưa đủ status" → workaholic
    Mastery cycle: prolactin yếu → "chưa đủ giỏi" → perfectionist
    → Prolactin hardware ẢNH HƯỞNG threshold TOÀN BỘ channels
    → Nhưng: threshold = emergent từ QUÁ NHIỀU biến → chỉ ước lượng, không tính chính xác
```

---

## 6. So Sánh v6 → v8

```
THAY ĐỔI:                    v6                    v8
──────────────────────────────────────────────────────────
Kiến trúc:        3 kênh gốc + phụ gia   →  3 Lớp hierarchy
Dopamine:         PE signal               →  Schema-Drive signal + nhiên liệu sáng tạo
Cortisol:         Threat/phanh            →  Nhiên liệu kích hoạt + sweet spot
NE:               Volume/arousal          →  Spotlight attention
Vasopressin:      Bảo vệ gắn bó (sơ lược)→  Lính gác bond (chi tiết + hardware)
Prolactin:        Phanh (sơ lược)         →  Nút dừng + addiction link + hardware/context
Endo-CB:          Relaxation (sơ lược)    →  Giảm xóc body + exercise link + cannabis
Receptor variants: KHÔNG CÓ               →  DRD4, COMT, MAO-A, AVPR1A
10 sub-channels:  KHÔNG CÓ               →  E1-E5, C1-C5 (Layer1-Channels.md)
Dopamine×Cortisol: KHÔNG CÓ              →  Bổ sung nhau (build × execute)

GIỮ NGUYÊN (v6 vẫn đúng):
  ✅ Berridge wanting ≠ liking
  ✅ Schultz dopamine PE mechanism (UD mở rộng, không phủ nhận)
  ✅ Opioid + Oxytocin = 2 source channels
  ✅ Serotonin = multiplier, không phải source
  ✅ Research references (gen markers, đo lường — giữ từ v6)
```

---

## 7. Câu Hỏi Mở

```
NC1: Prolactin trong addiction — cần research thêm
     → "Prolactin bypass = không dừng được" — hợp lý nhưng evidence 🟡
NC2: Endo-CB trong anxiety — emerging research
     → Endo-CB depletion → anxiety tăng — supported nhưng 🟡
NC3: Vasopressin gender difference — sensitive topic
     → Nam territorial hơn (testosterone × vasopressin) — evidence 🟢 nhưng nuance cần
NC4: Có hóa chất thứ 6 trong Lớp 3 chưa phát hiện?
     → Framework mở cho bổ sung — nếu research tìm thấy
NC5: "Runner's high" = endo-CB — research MỚI (2015+)
     → CŨ = endorphin → MỚI = endocannabinoid → cần follow-up
```

---

> *Neurochemistry v8 Draft — Kiến trúc 3 Lớp*
> *Đọc CÙNG: Neurochemistry.md (v6 legacy) cho research detail + gen markers + đo lường*
> *Merge thành 1 file chất lượng cao khi build v8.0*
