# Schema Operations — Schema Vận Hành Thế Nào

> **Trạng thái:** DRAFT — phân tích schema qua lăng kính HÀNH VI (không qua neuron riêng lẻ)
> **Ngày:** 2026-03-26
> **Mục đích:** Hiểu schema HOẠT ĐỘNG thế nào trong thực tế hàng ngày:
> VTA detect biến động thế nào, PFC chú ý thế nào, schemas chạy song song thế nào,
> body reward thế nào — tất cả qua CÁI CON NGƯỜI NHÌN THẤY + CẢM THẤY
> **Góc nhìn:** HÀNH VI (verbal mô tả được) — không phải neuron level
> Neuron = quá nhỏ → hành vi = quá lớn → abstraction GIỮA = schema operations
> **Reference:** Schema-Atlas-v2.md (properties), Architecture-v7.5-Draft.md (kiến trúc),
> PFC-Analysis.md (PFC mechanism), Attention-Spectrum.md (DRD4 threshold)
> **⚠️ Framework hypothesis — logic consistent, cần xác thực**

---

## 1. Schema Là Gì — Qua Lăng Kính Hành Vi

```
Schema = "CÁCH XỬ LÝ" mà body+não ĐÃ BIẾT SẴN:

  KHÔNG phải "1 cục data" nằm đâu đó trong não
  KHÔNG phải "1 file" hay "1 record" lưu trữ
  MÀ LÀ: "1 PATTERN hành vi/suy nghĩ/cảm nhận SẴN SÀNG chạy khi được kích hoạt"

  Ví dụ: schema "uống nước":
    = CHUỖI sẵn sàng: biết bàn ở đâu + biết ca ở đâu + biết cách rót + biết cách uống
    → Khi khát → KÍCH HOẠT → toàn bộ chuỗi TỰ CHẠY
    → KHÔNG cần nghĩ: "bước 1 đi tới bàn, bước 2 cầm ca..."
    → = "Biết mà KHÔNG CẦN nghĩ" = schema compiled

  Ví dụ: schema "sợ chó":
    = PATTERN sẵn sàng: thấy chó → body căng + muốn tránh + cortisol
    → Khi thấy chó → KÍCH HOẠT → body PHẢN ỨNG ngay
    → KHÔNG cần nghĩ: "đây là chó → chó có thể cắn → tôi nên sợ"
    → = "Sợ mà KHÔNG CẦN lý do" = schema compiled từ kinh nghiệm

  Ví dụ: schema "giải toán mới":
    = CHƯA CÓ pattern sẵn → PFC phải DRAFT
    → Thấy bài toán → PFC: "hmm... thử cách A? thử cách B?"
    → = "Phải NGHĨ mới làm được" = schema CHƯA compiled → PFC đang draft

  → Schema = SPECTRUM:
    Compiled (vô thức auto): "biết mà không cần nghĩ"
    Semi-compiled (PFC nhẹ): "biết nhưng cần chú ý chút"
    Drafting (PFC nặng): "chưa biết, đang cố tìm cách"
    → = KHÔNG binary "vô thức/ý thức" → GRADIENT liên tục
```

---

## 2. Gradient Chú Ý — Phổ Liên Tục

```
⭐ INSIGHT: KHÔNG có đường CỨNG giữa "vô thức" và "ý thức":

  MỌI schema nằm trên 1 PHỔ LIÊN TỤC:

  ┌─────────────────────────────────────────────────────────────┐
  │                                                             │
  │  VÔ THỨC        ←── gradient ──→        PFC TẬP TRUNG      │
  │  HOÀN TOÀN                               SÂU NHẤT         │
  │                                                             │
  │  PFC: 0%     5%      20%      50%      80%     95%+       │
  │                                                             │
  │  Thở       Đi bộ   Nghe      Nghe     Giải    Novelty    │
  │  Tim đập   Quay bút nền      cô       toán    imagine    │
  │  Tiêu hóa  Tư thế   Liếc    giảng    mới     deep       │
  │  Mồ hôi    ngồi    xung               Suy     Flow       │
  │  Thăng     Tay      quanh              nghĩ   state      │
  │  bằng      viết                        kỹ                 │
  │            auto                                            │
  │                                                             │
  │  "Không    "Làm mà  "Biết    "Đang   "Phải   "ĐẮMCHÌM  │
  │  biết      không    nhưng    nghe"    nghĩ    hoàn toàn" │
  │  đang      để ý"    không              kỹ"                │
  │  làm"                care"                                 │
  └─────────────────────────────────────────────────────────────┘

  MỖI NGƯỜI mô tả gradient bằng VERBAL khác nhau:
    "Tôi không để ý" = schema ở 0-10% PFC (vô thức xử lý)
    "Tôi biết nhưng mặc kệ" = schema ở 20-30% (PFC thấy nhưng không invest)
    "Tôi đang tập trung vào đó" = schema ở 60-80% (PFC active)
    "Tôi đắm chìm, quên hết xung quanh" = schema ở 90%+ (PFC all-in)

  Schema CÓ THỂ DỊCH CHUYỂN trên gradient:
    Mới học → PFC 90% (mọi thứ phải nghĩ) → PHẢI → gradient
    Luyện tập → PFC giảm DẦN → DỊCH TRÁI
    Thành thạo → PFC 5% (auto) → TRÁI → gradient
    → = "Thành thạo" = schema DỊCH từ phải → trái
    → = "Compiled" = ĐÃ DỊCH hết trái → vô thức auto

    Ví dụ lái xe:
      Tháng 1: PFC 90% (nghĩ từng động tác) → MỆTNÃO
      Năm 1: PFC 40% (phần lớn auto, PFC nhìn đường)
      Năm 5: PFC 5% (toàn auto, PFC nghĩ việc KHÁC khi lái)
      → = Cùng task → KHÁC vị trí gradient → KHÁC experience
```

---

## 3. Nhiều Schemas Chạy CÙNG LÚC — Parallel Multi-Position

```
⭐ TẠI BẤT KỲ THỜI ĐIỂM NÀO: HÀNG CHỤC schemas chạy ĐỒNG THỜI:

  Mỗi schema ở 1 VỊ TRÍ KHÁC trên gradient:

  Ví dụ — Axyz ngồi trong lớp:

    [0% PFC]     [5%]       [20%]      [50%]      [90%]
    Thở          Tay quay   Tai nghe   Mắt nhìn   Novelty
    Tim đập      bút auto   nền lớp    cô giảng   imagine
    Tiêu hóa     Tư thế     Mùi lớp   (lúc có    (chế tạo
    Mồ hôi       ngồi auto  Cảm giác  lúc không) cái mới)
    Thăng bằng              ghế                    ← PFC ĐÂY

  → "TÔI đang làm gì?" = PFC trả lời CHỈ cho vị trí PHẢI NHẤT
  → Axyz: "tôi đang nghĩ về chế tạo" (Novelty ở 90%)
  → Axyz KHÔNG nói: "tôi đang thở + quay bút + nghe nền + ngồi ghế"
    (vì tất cả ở TRÁI gradient → PFC KHÔNG "thấy" → KHÔNG verbalize được)
  → = "Tôi đang nghĩ gì" = CHỈ biết phần PFC CAO → phần thấp = "vô thức"

  PFC WORKSPACE CÓ HẠN (4±1 dimensions):
    → KHÔNG THỂ PFC 90% cho NHIỀU schemas cùng lúc
    → NẾU Novelty đang 90%: capacity GẦN HẾT cho Novelty
    → → Schemas khác: PHẢI dùng PFC ÍT hơn (dịch TRÁI)
    → → "Đắm chìm suy nghĩ → quên hết xung quanh" = PFC all-in 1 schema → còn lại auto

  PHÂN BỐ PFC thay đổi LIÊN TỤC:
    → Axyz Novelty 90% → bạn đập bàn → PFC SHIFT:
      Novelty: 90% → 10% (tạm treo)
      "Cái gì vậy?": 0% → 80% (PFC jump sang)
    → Sau 10 giây (không có gì): PFC SHIFT lại:
      "Cái gì vậy?": 80% → 0% (xong, không quan trọng)
      Novelty: 10% → 70% (quay lại, NHƯNG có thể mất phần đang nghĩ)
    → = PFC = "đèn spotlight" QUAY liên tục → chiếu chỗ NÀO → chỗ đó RÕ
    → = Chỗ KHÔNG được chiếu → VẪN chạy (vô thức) → nhưng KHÔNG RÕ
```

---

## 4. VTA — Detect BIẾN ĐỘNG (Không Phải "Mới")

```
⭐ VTA KHÔNG "biết" thông tin mới — VTA đo "KHÁC so với ĐANG chạy":

  CƠ CHẾ (qua lăng kính hành vi):

    Mọi schemas đang fire tạo 1 "TRẠNG THÁI NỀN" tại thời điểm đó:
      → Lớp học: giọng cô + tiếng quạt + mùi phấn + ánh sáng + tư thế ngồi
      → = "Bình thường hiện tại" — VTA ĐÃ quen → KHÔNG fire

    KHI CÓ GÌ THAY ĐỔI so với "bình thường hiện tại":
      → VTA detect: "CÓ BIẾN ĐỘNG!" → fire dopamine → PFC nhận
      → VTA KHÔNG biết "mới" → chỉ biết "KHÁC so với 1 giây trước"

  "MỚI" = gì? = "KHÁC pattern ĐANG chạy":
    → Cô giảng giọng BÌNH THƯỜNG → VTA quen → "cũ" → không fire
    → Cô giảng BỖNG hét → giọng KHÁC → VTA: "BIẾN ĐỘNG!" → fire
    → = "Mới" = delta (thay đổi so với hiện tại), KHÔNG phải "chưa từng thấy"
    → = Cô giảng giọng khác = "mới" dù CÙNG CÔ GIẢNG HÀNG NGÀY

  MỨC ĐỘ biến động = dopamine BAO NHIÊU:
    → "Bao nhiêu" schemas THAY ĐỔI cùng lúc = proxy cho "biến động lớn cỡ nào"
    → 1 thứ nhỏ đổi (cô liếc mắt): biến động NHẸ → dopamine NHẸ
    → Nhiều thứ đổi CÙNG LÚC (tiếng nổ + ánh sáng + mùi): biến động LỚN → dopamine MẠNH
    → Toàn bộ environment đổi (chuyển phòng): biến động CỰC LỚN → dopamine CỰC MẠNH

  HABITUATION — VTA "quen" nhanh:
    → Biến động lần 1: VTA fire MẠNH ("lạ!")
    → Biến động lần 2 (giống): VTA fire YẾU hơn ("à, lại cái đó")
    → Biến động lần 5 (vẫn giống): VTA GẦN NHƯ không fire ("biết rồi")
    → = "Nghe tiếng ồn lần đầu → giật mình → lần 5 → mặc kệ"
    → = VTA habituate → pattern MỚI trở thành "bình thường mới" → không fire nữa
    → = ĐÂY là lý do: MXH phải liên tục content MỚI (vì user habituate NHANH)


  DRD4 × VTA detection (Hypothesis D — chưa proven trực tiếp):

    VTA fire dopamine → dopamine TỚI PFC receptor:
      4R (nhạy): biến động NHỎ → signal NHẸ → VẪN vượt threshold → PFC THẤY
        → = "Chú ý mọi thay đổi nhỏ" → detail-oriented
      7R (kém nhạy): biến động NHỎ → signal NHẸ → DƯỚI threshold → PFC MISS
        → Chỉ biến động LỚN → VẪN vượt → PFC THẤY
        → = "Miss chi tiết, thấy big picture" → improviser
      → = CÙNG VTA, CÙNG dopamine → KHÁC threshold → KHÁC cái PFC "thấy"


  ÁP DỤNG — Axyz trong lớp (tất cả xảy ra CÙNG LÚC):

    CÔ GIẢNG bình thường:
      → Giọng cô: pattern quen (nghe hàng ngày) → VTA habituate → KHÔNG fire mạnh
      → 4R Axyz: dopamine nhẹ VẪN nhận → nghe VỪA → chú ý vừa đủ
      → 7R Axyz: dopamine nhẹ KHÔNG nhận → "chán" → PFC tìm chỗ KHÁC

    BẠN NỮ đi qua + nước hoa:
      → Olfactory: mùi MỚI (khác mùi lớp) → biến động vùng olfactory
      → Visual: hình dáng MỚI (khác "bạn trong lớp") → biến động visual
      → 2 vùng CÙNG biến động = chunk KHÁ LỚN → dopamine KHÁ MẠNH
      → 7R: CÓ THỂ nhận (2 vùng cùng lúc = đủ threshold)
      → 4R: CHẮC CHẮN nhận
      → → PFC: "ồ!" → attention SHIFT → nhìn ra → imagine

    TIẾNG NỔ bất ngờ:
      → Auditory: SPIKE cực → visual: mọi người giật → body: startle reflex
      → NHIỀU vùng biến động CÙNG LÚC = chunk CỰC LỚN
      → → CẢ 4R VÀ 7R: phản ứng NGAY → PFC 100% vào check threat
      → = "Tiếng nổ = MỌI NGƯỜI chú ý" vì biến động QUÁ LỚN cho mọi threshold

    CÔ GIÁO gọi "AXYZ!":
      → Đặc biệt: xem §7 (Always-on monitors)
```

---

## 5. PFC — Chọn "Nhìn" Vào Đâu Trên Gradient

```
PFC = SPOTLIGHT quay liên tục trên gradient schemas:

  PFC KHÔNG "điều khiển" mọi schema → PFC "CHIẾU SÁNG" 1-2 schema:
    → Schema được chiếu: RÕ → PFC process → conscious → verbalize được
    → Schema KHÔNG chiếu: MỜ → vô thức auto → unconscious → "không biết đang làm"
    → = "Ý thức" = schema NÀO đang được PFC chiếu spotlight
    → = "Vô thức" = schemas đang chạy mà PFC KHÔNG chiếu

  PFC chọn chiếu DỰA VÀO GÌ:

    ① DOPAMINE signal (VTA báo):
       → VTA fire "biến động ở vùng X!" → dopamine → PFC
       → PFC: "ồ, có gì đó ở X" → SHIFT spotlight sang X
       → = "Bất giác nhìn về hướng có tiếng động" = PFC shift vì dopamine

    ② MỤC TIÊU đang hold (schema đang ở phải gradient):
       → PFC đang chiếu Novelty imagine → "mục tiêu hiện tại"
       → MUỐN giữ spotlight ở đây → KHÁNG shift
       → = "Cố tập trung dù có tiếng ồn" = PFC cố GIỮ spotlight

    ③ INTERRUPT hierarchy (khi biến động ĐỦ MẠNH → OVERRIDE mục tiêu):
       → Biến động NHỎ: PFC có thể KHÁNG → giữ spotlight → "mặc kệ"
       → Biến động LỚN: PFC KHÔNG kháng được → PHẢI shift → "giật mình"
       → = "Threshold interrupt" = biến động phải ĐỦ LỚN mới kéo PFC khỏi mục tiêu

    PFC SHIFT = CÓ COST:
      → Shift spotlight = "xóa" context cũ + "load" context mới
      → = TỐN thời gian + TỐN energy
      → = "Switch task = mất 5-15 phút để lại focus sâu" (🟢 research: task switching cost)
      → 7R + COMT Val/Val: context CŨ CLEAR nhanh → shift NHANH → nhưng MẤT context cũ
      → 4R + COMT Met/Met: context cũ LINGER → shift CHẬM → nhưng GIỮ ĐƯỢC context cũ
      → = Tại sao: "bị interrupt → quên mất đang nghĩ gì" (7R) vs "bị interrupt → nhớ lại được" (4R)


  PFC 4±1 DIMENSIONS — hold + vô thức đối chiếu:

    PFC workspace HOLD tối đa 4±1 "nhóm" cùng lúc:
      → Mỗi dimension = 1 nhóm schema/chunks đang GIỮ
      → PFC KHÔNG tự so sánh giữa dimensions
      → PFC GIỮ (hold) → spotlight XUỐNG vô thức → vô thức ĐỐI CHIẾU

    Ví dụ: đang so sánh {PFC ↔ giám đốc} × {VTA ↔ thư ký}:
      Dim 1: [PFC = giám đốc?] → hold
      Dim 2: [VTA = thư ký?] → hold
      Dim 3: [vô thức = nhân viên?] → hold
      Dim 4: [tổng thể = KHỚP không?] → hold
      → PFC GIỮ 4 cái → spotlight xuống vô thức
      → Vô thức: ĐỐI CHIẾU patterns → "dim1 khớp, dim2 khớp, dim3 khớp..."
      → VTA: detect ĐỒNG BỘ lớn (nhiều vùng match cùng lúc) → dopamine MẠNH
      → PFC: "KHỚP!" → body: opioid (coherence) → "sướng!"

    → = PFC = "GIÁM KHẢO" (giữ tiêu chí + nhận kết quả)
    → = Vô thức = "THÍ SINH" (làm bài so sánh thật sự)
    → = VTA = "BÁO CÁO" (báo "thí sinh xong, kết quả thế này")
    → = PFC KHÔNG tự so sánh → PFC CHỜ vô thức so xong → nhận kết quả
```

---

## 6. Schema Compile — Dịch Từ PHẢI → TRÁI Trên Gradient

```
"HỌC" = schema DỊCH DẦN từ PFC heavy → vô thức auto:

  GIAI ĐOẠN 1 — PFC DRAFT (phải gradient, 80-95% PFC):
    → Chưa biết cách → PFC phải THỬ:
      "Bước 1 là gì? → thử → sai → thử khác → đúng → ok"
    → MỖI bước = PFC draft + body check + adjust
    → MỆT (PFC tốn glucose CỰC NHIỀU)
    → CHẬM (mỗi bước phải nghĩ)
    → Ví dụ: lái xe ngày 1 → nghĩ từng động tác → mệt sau 30 phút

  GIAI ĐOẠN 2 — SEMI-COMPILED (giữa gradient, 30-60% PFC):
    → Một số bước ĐÃ auto → PFC chỉ cần "nhìn" tổng thể
    → "Biết rồi nhưng chưa thành thạo" → vẫn cần chú ý
    → Ít mệt hơn giai đoạn 1
    → Ví dụ: lái xe tháng 3 → chân ga auto, tay vẫn cần nghĩ chút

  GIAI ĐOẠN 3 — COMPILED (trái gradient, 0-10% PFC):
    → TOÀN BỘ auto → PFC FREED → có thể nghĩ việc KHÁC
    → "Làm mà không cần nghĩ" → body execute compiled pattern
    → NHANH (không có delay "nghĩ")
    → KHÔNG mệt PFC (vô thức chạy = energy thấp)
    → Ví dụ: lái xe năm 5 → tay chân auto → PFC nghe podcast

  TỐC ĐỘ compile PHỤ THUỘC:
    → Repetition: lặp NHIỀU → compile NHANH (practice)
    → Body feedback: body confirm "đúng" MỖI lần → reinforce → compile NHANH
    → Modality count: NHIỀU modality tham gia → compile SÂU hơn (deeper schema)
    → Sleep: REM consolidate → compile CHẶT hơn qua đêm
    → = "10,000 giờ" (Ericsson) ≈ "đủ repetition + feedback để compile sâu"

  ⚠️ Compiled ≠ ĐÚNG:
    → Schema có thể compile SAI (nếu body feedback sai hoặc environment mislead)
    → Compile sai = auto chạy SAI → KHÓ SỬA (vì đã compiled = cứng)
    → Ví dụ: học phát âm sai → compiled → nói sai auto → SỬA = phải "un-compile" + re-compile
    → = "Học đúng từ đầu DỄ hơn sửa sai sau" = compile ĐÚNG lần đầu > sửa sau
```

---

## 7. Always-On Monitors — Schemas "Canh Gác" Nền

```
⭐ CÓ 1 NHÓM schemas ĐẶC BIỆT: không vô thức 100%, không PFC nặng:

  ALWAYS-ON MONITORS = schemas ở ~10-20% PFC LIÊN TỤC:
    → KHÔNG chiếm workspace PFC đáng kể (chỉ 10-20%)
    → NHƯNG: luôn "CANH" 1 pattern cụ thể
    → KHI pattern đó XUẤT HIỆN → KÍCH HOẠT → KÉO PFC ngay lập tức
    → = "Bảo vệ ngồi cổng: không làm gì → nhưng ai tới → BÁO NGAY"

  CÁC MONITOR phổ biến:

    TÊN MÌNH (always-on từ bé):
      → 🟢 "Cocktail party effect" (Cherry 1953):
      → Giữa đám đông ồn ào → nghe ai đó nói TÊN MÌNH → QUAY ĐẦU NGAY
      → Dù: PFC đang bận NÓI CHUYỆN với người khác → VẪN detect tên
      → = Monitor "tên tôi" = LUÔN chạy → dù PFC ở đâu trên gradient
      → Tại sao evolution giữ: tên = social signal QUAN TRỌNG
        (ai đó GỌI bạn = threat HOẶC opportunity = CẦN biết ngay)

    THREAT SCAN (always-on khi có compiled "nguy hiểm"):
      → Lái xe: PFC nghĩ việc khác → nhưng monitor "xe khác đi lạ" = LUÔN chạy
      → Đi đường tối: PFC nghĩ → monitor "có ai đi sau?" = luôn chạy
      → = Monitor threat = compiled schema "PATTERN NGUY HIỂM" → luôn scan
      → = Nếu match → KÉO PFC ngay: "Ồ! xe đó đi lạ!" → attention 100%

    BODY-NEED (always-on body signal):
      → Đói: body signal "khát" → tăng DẦN → tới threshold → PFC nhận → "khát"
      → Mệt: body signal "ngủ" → tăng DẦN → tới threshold → PFC: "mệt"
      → Đau: body signal → TỨC THÌ → PFC: "ĐAU!"
      → = Monitors body-need = always-on → DẦN kéo PFC nếu signal ĐỦ MẠNH

    SOCIAL SCAN (always-on trong social context):
      → Trong nhóm: monitor "ai đang nói về MÌNH?" → always-on
      → Trong lớp: monitor "cô giáo đang nhìn MÌNH không?" → always-on
      → = Status calibrate = LUÔN chạy nền khi có người khác
      → = Tại sao "ở 1 mình relax hơn": ít monitor social → PFC FREED

  INTERRUPT HIERARCHY — cái nào KÉO PFC mạnh nhất:

    MẠNH NHẤT (override MỌI THỨ):
      → Tên mình được gọi
      → Đau vật lý đột ngột
      → Tiếng nổ / tiếng hét
      → = "Emergency channel" = compiled CỰC SÂU + evolution priority

    MẠNH (override hầu hết):
      → Ai đó CHẠM body bất ngờ (vỗ vai)
      → Visual LỚN bất ngờ (ánh sáng chói, vật bay tới)
      → Mùi MẠNH bất ngờ (khói, gas)
      → = "Alert channel" = sensory SPIKE

    TRUNG BÌNH (override nếu PFC KHÔNG quá bận):
      → Ai đó nhìn mình (social scan detect)
      → Tiếng nói đề cập topic liên quan mình
      → Visual mới (người lạ đi qua)
      → = "Interesting channel" = novelty vừa

    YẾU (chỉ override khi PFC RẢNH):
      → Mùi nhẹ mới (nước hoa xa)
      → Tiếng nhạc nền thay đổi nhẹ
      → Cảm giác body nhẹ (hơi đói, hơi mỏi)
      → = "Background channel" = biến động NHẸ

    → 7R miss NHIỀU thứ ở "trung bình" và "yếu" (threshold cao)
    → 4R nhận GẦN HẾT (threshold thấp)
    → CẢ HAI nhận "mạnh nhất" và "mạnh" (biến động quá lớn cho mọi threshold)

  → MONITORS = "chi phí nền" cho PFC:
    → Mỗi monitor ~10-20% PFC → 5 monitors = 50-100% PFC CHỈ cho CANH GÁC
    → NHƯNG: monitors OVERLAP + SHARE resource → thực tế ~20-30% tổng
    → = "Ở nơi đông người = MỆTHƠN ở 1 mình"
      vì: social monitors NHIỀU hơn → PFC nền TỐNNHIỀU hơn → ÍT workspace còn lại
    → = "Introvert mệt ở party" = monitors social QUÁTẢI → PFC hết workspace
    → = "Extrovert thoải mái ở party" = monitors social compiled TỐT → tốn ÍT PFC
```

---

## 8. PFC Simulate vs Trực Tiếp Sửa vs Vô Thức Tự Sửa

```
3 MODE sửa schema — tùy tình huống:

  MODE 1 — PFC SIMULATE (draft trước, không sửa ngay):
    → PFC tạo draft TẠM: "nếu tôi làm X → kết quả thế nào?"
    → Body simulate: respond 20-60% fidelity (imagine body response)
    → NẾU body "feel ok": compile draft → schema UPDATE
    → NẾU body "feel sai": discard draft → thử draft KHÁC
    → Schema GỐC: KHÔNG ĐỔI trong lúc simulate (safe)
    → = "Thử trong đầu trước khi làm thật"
    → KHI NÀO: tình huống MỚI, stakes CAO, chưa biết kết quả
    → Ví dụ: "nếu tôi nói CÁI NÀY với sếp → sếp react thế nào?" → simulate → chọn

    ⭐ "SIMULATE" = KHÔNG có hệ thống riêng:
       PFC KHÔNG có "phòng giả lập" → PFC dùng CÙNG pathway với thật:
       🟢 Motor imagery: tưởng tượng vận động → motor cortex FIRE (cùng vùng vận động thật)
          (Jeannerod 1995) ✅
       🟢 Visual imagery: tưởng tượng mặt mẹ → visual cortex FIRE (cùng vùng nhìn thật)
          (Kosslyn 1994) ✅
       🟢 Emotional imagery: tưởng tượng sợ → amygdala FIRE (cùng vùng sợ thật)
          (Phelps 2004) ✅
       → = "Simulate" = KÍCH HOẠT lại CÙNG đường dây với thật → chỉ YẾU hơn (20-60%)
       → = PFC KHÔNG "vẽ hình" → PFC "GỌI" visual cortex fire lại pattern ĐÃ CÓ
       → = PFC KHÔNG "tạo cảm giác" → PFC "GỌI" somatic fire lại pattern ĐÃ CÓ
       → = Giống: PFC bấm PLAY trên remote → TV (visual cortex) CHIẾU lại pattern
       → Hệ quả: KHÔNG THỂ imagine cái CHƯA TỪNG experience (ở mức nào đó)
       → = "Imagine = REMIX patterns cũ" → KHÔNG phải "tạo patterns MỚI từ zero"

  MODE 2 — PFC TRỰC TIẾP sửa (realtime adjust):
    → Schema đang chạy → gặp cái HƠI KHÁC → PFC: tweak NGAY
    → KHÔNG simulate trước → ADJUST trực tiếp → body feedback NGAY
    → = "Sửa trong lúc chạy"
    → KHI NÀO: tình huống URGENT, schema ĐÃ compiled (chỉ cần tweak nhẹ)
    → Ví dụ: đang lái xe → thấy hố → PFC: "RẼ!" → motor adjust ngay

  MODE 3 — VÔ THỨC TỰ SỬA (PFC không tham gia):
    → Schema compiled → gặp variation NHỎ → vô thức TỰ adjust
    → PFC: KHÔNG BIẾT (hoặc biết SAU)
    → = "Body tự xử"
    → KHI NÀO: compiled SÂU, adjustment NHỎ, PFC không cần
    → Ví dụ: đi bộ → mặt đường hơi nghiêng → chân TỰ adjust → PFC mặc kệ


⭐ BODY REWARD KHÔNG CHỈ KHI "XONG" — mà TỪNG BƯỚC:

  ⚠️ Sai lầm phổ biến: "làm xong → mới sướng"
  ✅ Thực tế: body check + reward LIÊN TỤC TRONG LÚC schema chạy:

    → Viết code: mỗi dòng "feel đúng" → micro opioid → "ổn, tiếp"
    → Nấu ăn: mỗi bước "feel đúng" → micro opioid → "ổn, tiếp"
    → Nói chuyện: mỗi câu đối phương react TỐT → micro opioid → "ổn, tiếp"
    → = Chuỗi MICRO-REWARDS liên tục → duy trì attention → duy trì schema

  FLOW STATE = chuỗi micro-rewards ĐẶC BIỆT DÀI + ĐỀU:
    → Mỗi bước: vừa đủ khó (Novelty) + body confirm "đúng hướng" (opioid)
    → = Dopamine (seeking) + opioid (confirm) xen kẽ LIÊN TỤC
    → = PFC: "tiếp... tiếp... tiếp..." (không dừng vì LUÔN có reward)
    → = "Quên thời gian" = PFC không dừng để check "mấy giờ rồi?"
      vì: micro-reward LIÊN TỤC → không có "GAP" để PFC nhìn chỗ khác

  KHI micro-reward DỪNG → schema DỄ dừng:
    → Code: dòng này "feel sai" → micro-pain → PFC: "hmm, chỗ nào sai?"
    → = "Stuck" = micro-reward DỪNG → PFC PHẢI switch sang mode 1 (simulate)
    → = "Flow bị ngắt" = micro-reward chain BỊ ĐỨT ở 1 chỗ

  → Body reward LIÊN TỤC TRONG schema = GIỮ schema chạy
  → Body reward DỪNG = schema DỄ bị PFC abandon → switch sang cái khác
  → = "Tại sao chán" = micro-reward DỪNG → PFC tìm schema cho reward ĐỀU hơn


  ⭐ 2 TẦNG BODY EVALUATE (cùng lúc, khác mức):

  TẦNG 1 — MOOD: body evaluate TỔNG THỂ melody (background):
    → MỌI schemas chạy → tạo 1 "TRẠNG THÁI TỔNG" → body CẢM NHẬN tổng
    → Nhiều schemas ok + ít threat → mood "tốt" (opioid nền ok)
    → Nhiều schemas conflict + threat → mood "xấu" (cortisol nền cao)
    → = "Tâm trạng chung" → KHÔNG biết cụ thể schema NÀO gây → chỉ feel TỔNG
    → "Hôm nay thấy nhẹ người" = tổng melody đang HARMONY
    → "Hôm nay bứt rứt mà không biết vì sao" = có DISSONANCE ở đâu đó

  TẦNG 2 — MICRO-REWARD: body evaluate PER-GROUP (specific):
    → VTA detect biến động ở 1 group → PFC spotlight → body evaluate GROUP đó
    → = "Ồ, đoạn NÀY hay!" = body reward cho group CỤ THỂ đang nổi bật
    → = BIẾT sướng VÌ CÁI GÌ (vì PFC đang spotlight group đó)

  2 TẦNG ẢNH HƯỞNG lẫn nhau:
    → Tầng 2 → Tầng 1: nhiều micro-rewards → mood TỔNG tăng (virtuous cycle)
    → Tầng 1 → Tầng 2: mood tốt → body DỄ reward hơn (threshold thấp hơn)
    → Virtuous: micro-reward → mood tốt → dễ reward → mood tốt hơn
    → Vicious: micro-pain → mood xấu → khó reward → mood xấu hơn

  PFC GOM NHÓM ảnh hưởng QUALITY evaluate:
    → PFC gom [chỉ anim]: body evaluate anim → RÕ (1 instrument solo)
    → PFC gom [anim + code]: body evaluate cả 2 → MƠ HỒ (2 instruments mix)
    → = "Tập trung 1 thứ → body evaluate THỨ ĐÓ chính xác nhất"
    → = "Nhiều thứ cùng lúc → body evaluate TỪNG THỨ kém chính xác"


  ⭐ NOISE GIẢM BODY CHECK QUALITY:

    Yên tĩnh + chỉ 1 schema: body nghe RÕ → evaluate CHÍNH XÁC
      = Guitar SOLO → nghe rõ mọi note → biết hay/dở CHÍNH XÁC

    Ồn ào + nhiều schemas: body nghe TỔNG → evaluate per-schema KÉM
      = Guitar TRONG dàn nhạc 50 nhạc cụ → khó nghe riêng guitar

    → TẠI SAO creative work CẦN yên tĩnh:
      ❌ KHÔNG CHỈ: "PFC bị distract bởi ồn" (đúng 1 phần)
      ✅ CÒN: "body evaluate schema đang làm BỊ NOISE giảm accuracy"
      → = BODY-LEVEL explanation: noise = thêm instruments → body nghe 1 schema KÉM RÕ
      → = Yên tĩnh = ít instruments → body nghe schema đang làm RÕ nhất → output TỐT nhất
      → = "Tắt mọi thứ, chỉ ngồi nhìn, cảm nhận" = reduce noise → maximize body check accuracy
```

---

## 8.5 Tại Sao Tưởng Tượng LUÔN Gần Real

```
🟡 "Imagine" = kích hoạt lại patterns ĐÃ compiled → nên LUÔN gần real:

  NGUYÊN TẮC:
    PFC trigger chunk → chunk KÉO chunks LINKED (compiled cùng nhau)
    → Visual/auditory/somatic cortex fire patterns tương ứng
    → = "Tưởng tượng" = REPLAY patterns từ experience → nên gần giống real

  TẠI SAO xem phim zombie → tưởng tượng zombie, KHÔNG tưởng tượng hổ:
    → Xem phim: [bóng tối + zombie] = compiled CÙNG NHAU (vì xem cùng lúc)
    → Về nhà → thấy bóng tối → chunk "bóng tối" FIRE → KÉO chunk "zombie" (linked)
    → Chunk [bóng tối + hổ] = KHÔNG tồn tại (chưa experience) → KHÔNG fire
    → = "Tưởng tượng zombie" = CÓ chunk linked → fire
    → = "KHÔNG tưởng tượng hổ" = KHÔNG CÓ chunk linked → KHÔNG fire
    → = KHÔNG phải "chọn" tưởng tượng gì → chunks linked QUYẾT ĐỊNH

  TẠI SAO KHÔNG lai ma + zombie:
    → Chunk [ma] = pattern A (trắng, bay, vô hình)
    → Chunk [zombie] = pattern B (thối, chậm, ăn não)
    → A và B = 2 patterns MÂU THUẪN visual (trắng+bay ≠ thối+chậm)
    → Visual cortex KHÔNG fire 2 pattern mâu thuẫn cùng lúc
    → = "Hoặc ma HOẶC zombie" → KHÔNG tự nhiên "lai"
    → ⚠️ NHƯNG: nghệ sĩ CÓ THỂ "lai" = PFC CỐ TÌNH ghép:
      PFC draft: "thử: body ma + đi kiểu zombie?"
      → Visual cortex CỐ fire pattern mới → body check: "coherent?"
      → Nếu coherent → giữ → "sáng tạo!"
      → Nếu không → discard → "vô lý"
      → = "Sáng tạo" = PFC CỐ TÌNH ghép patterns KHÔNG tự nhiên link
      → = Phần lớn người KHÔNG cố → nên imagine = fire patterns ĐÃ CÓ

  TẠI SAO avatar xanh KHÔNG thành chó:
    → Chunk [avatar xanh tai dài] = compiled từ phim
    → Chunk [chó] = compiled từ đời thường
    → 2 chunks KHÔNG LINK (khác domain, khác context hoàn toàn)
    → Nhớ avatar → fire avatar pattern → KHÔNG kéo chó (không link)
    → = "Tưởng tượng = fire LINKED chunks" → không link = KHÔNG fire

  "NHỚ MẸ" — PFC override mắt hay kích hoạt pathway?
    → PFC KHÔNG "vẽ" mặt mẹ lên visual cortex
    → PFC "GỌI" visual cortex: "fire pattern 'mặt mẹ'!"
    → Visual cortex TỰ fire pattern đã compiled (từ nhiều lần nhìn mẹ)
    → = PFC = remote control → visual cortex = TV → pattern = kênh
    → PFC bấm "kênh mẹ" → TV hiện mặt mẹ → PFC KHÔNG vẽ gì
    → "Thấy mặt mẹ trong đầu" = visual cortex fire → đúng literally "THẤY"
    → Chỉ YẾU hơn nhìn thật (20-60% fidelity) → nên "mờ hơn"

  → GIỚI HẠN IMAGINATION:
    ✅ CÓ THỂ: tưởng tượng MỌI THỨ ĐÃ experience (fire lại patterns)
    ✅ CÓ THỂ: REMIX patterns cũ theo cách mới (PFC cố ghép → body check)
    ❌ KHÔNG THỂ: tưởng tượng cái HOÀN TOÀN chưa experience
       (vì: KHÔNG CÓ pattern để fire → visual cortex "fire CÁI GÌ?")
    → = "Imagine = REMIX patterns cũ" → không phải "tạo từ zero"
    → = Tại sao: chunks NHIỀU → imagine RỘNG (nhiều pattern remix)
    → = Chunks ÍT → imagine HẸP ("hết ý tưởng" = ít pattern để remix)
    → = AI cung cấp chunks MỚI → imagine RỘNG hơn (THÊM pattern remix)
```

---

## 8.7 Expertise = Body Nghe DETAILED Hơn

```
🟡 "Chuyên gia" = KHÔNG phải "thông minh hơn":
   = Body CÓ NHIỀU chunks tham chiếu → TÁCH chi tiết hơn → evaluate CHÍNH XÁC hơn

  GRADIENT CHUYÊN MÔN — cùng input, KHÁC trải nghiệm:

  Ví dụ NGHE NHẠC (ai cũng biết):

    Người thường (ít chunks nhạc):
      → Nghe bài mới → body: "HAY!" → nhưng: "không biết VÌ SAO hay"
      → = Body evaluate TỔNG melody → biết hay/dở (binary)
      → = Ít chunks tham chiếu → body KHÔNG TÁCH được per-instrument
      → = Giống: nhìn bức tranh → "đẹp!" → không biết VÌ SAO đẹp

    Người nghe nhiều (chunks VỪA):
      → Nghe → body: "đoạn NÀY sướng!" → biết CHỖ NÀO hay
      → = Body ĐÃ tích lũy chunks "đoạn" từ nhiều bài → TÁCH được per-đoạn
      → = Micro-reward fire ở ĐOẠN cụ thể → PFC: "ồ, đoạn này!"
      → NHƯNG: "không biết VÌ SAO đoạn đó hay" = chưa tách per-instrument

    Người biết nhạc (chunks NHIỀU):
      → Nghe → body: "tiếng VIOLON đoạn này THÁNH THÓT! bỏ violon là MẤT!"
      → = Body TÁCH per-instrument (vì chunks từng instrument ĐÃ compiled)
      → = Biết: "violon = element tạo HAY" → vì body CÓ pattern "violon" RIÊNG
      → = "Bỏ violon" = body simulate variant THIẾU violon → "MẤT!" = body confirm

    Nhạc sĩ (chunks CỰC NHIỀU + simulate):
      → Nghe → body: "violon hay, NHƯNG nếu GUITAR thay + thêm BASS → HAY HƠN!"
      → = Body + PFC simulate VARIANT:
        PFC trigger: "thử fire pattern 'guitar thay violon' + 'bass thêm'"
        → Auditory cortex: fire pattern (cùng pathway nghe thật, yếu hơn)
        → Body: evaluate variant → "HAY HƠN bản gốc!"
      → = "Nghe trong đầu" = auditory cortex fire THẬT (chỉ yếu hơn nghe tai)
      → 🟢 Herholz & Zatorre (2012): musicians auditory imagery MẠNH hơn non-musicians
      → = Nhạc sĩ: KHÔNG "nghĩ" hay hơn → "NGHE trong đầu" chi tiết hơn → evaluate HƠN


  CƠ CHẾ: chunks NHIỀU → body TÁCH chi tiết → evaluate CHÍNH XÁC:

    Ít chunks: body nghe TỔNG → output = "hay/dở" (1 dimension)
    Thêm chunks: body TÁCH per-đoạn → "chỗ NÀY hay" (thêm dimensions)
    Nhiều chunks: body TÁCH per-element → "CÁI NÀY tạo hay" (chi tiết)
    Cực nhiều: body SIMULATE variant → "NẾU đổi → HAY HƠN" (creative)

    → = Mỗi chunk THÊM = body CÓ THÊM 1 "thước đo" để evaluate
    → = "Chuyên gia" = body có NHIỀU thước đo → evaluate NHIỀU dimension → CHÍNH XÁC
    → = "Người mới" = body có ÍT thước đo → evaluate ÍT dimension → thô

    Giống:
      Cân bằng TAY: ước lượng → "nặng/nhẹ" (1 dimension)
      Cân ĐỒNG HỒ: chính xác → "3.2 kg" (nhiều dimensions)
      Cân PHÂN TÍCH: cực chính xác → "3.217 kg" (cực nhiều dimensions)
      → Thêm CÔNG CỤ (chunks) = thêm PRECISION → KHÔNG phải "cân thông minh hơn"


  ÁP DỤNG — mọi domain CÙNG CƠ CHẾ:

    GAME DESIGN:
      Player thường: "hay!" → không biết vì sao
      Gamer kinh nghiệm: "combat ĐOẠN NÀY sướng!" → biết chỗ
      Game dev: "force=30 HƠN force=20! vì lực IMPACT ở mức này cho VISUAL+SOMATIC match"
      → = CÙNG game → KHÁC evaluate → vì KHÁC chunks compiled

    NẤU ĂN:
      Người thường: "ngon!" → không biết vì sao
      Người nấu nhiều: "MẶN quá!" → biết element sai
      Đầu bếp: "mặn → giảm muối + thêm chanh + chút đường = BALANCE" → simulate variant
      → = CÙNG món → KHÁC evaluate → vì KHÁC chunks

    LẬP TRÌNH:
      Người mới: "code CHẠY!" → binary (chạy/không chạy)
      Junior: "code chạy nhưng CHẬM ở đoạn NÀY" → biết chỗ
      Senior: "chậm vì algorithm O(n²) → đổi sang O(nlogn) → NHANH HƠN" → simulate variant
      → = CÙNG code → KHÁC evaluate → vì KHÁC chunks

    Y TẾ:
      Bệnh nhân: "ĐAU!" → binary (đau/không đau)
      Y tá: "đau BỤNG DƯỚI BÊN PHẢI" → biết location
      Bác sĩ: "đau bụng dưới phải + sốt + bạch cầu cao = CÓ THỂ ruột thừa → siêu âm confirm"
        → simulate nhiều diagnosis → body check pattern match → chọn likely nhất
      → = CÙNG triệu chứng → KHÁC evaluate → vì KHÁC chunks

    → = MỌI DOMAIN: "chuyên gia" = body có NHIỀU chunks tham chiếu
    → = KHÔNG phải "thông minh hơn" hay "logic tốt hơn"
    → = "Body nghe CHI TIẾT hơn vì có NHIỀU patterns đã compiled để so sánh"


  "10,000 GIỜ" GIẢI THÍCH:
    → Ericsson "deliberate practice" = tích lũy chunks qua PRACTICE
    → 10,000 giờ ≈ body tích lũy ĐỦ chunks → evaluate DETAILED ĐỦ → "expert"
    → NHƯNG: 10,000 giờ THREAT (bị ép) ≠ 10,000 giờ NOVELTY (tự thích)
      → Threat chunks: body có nhưng KHÔNG thích dùng → evaluate MIỄNCƯỠNG
      → Novelty chunks: body CÓ + THÍCH dùng → evaluate THOẢI MÁI + CHÍNH XÁC
      → = "10,000 giờ VUI" > "10,000 giờ KHỔ" vì chunk ASSOCIATION khác
      → (Chi tiết: Cortisol-Baseline.md §3.5)


  AI ERA × EXPERTISE:
    → AI cung cấp chunks NHANH → body CÓ THÊM patterns tham chiếu
    → = Body evaluate TỐT hơn NHANH hơn (không cần 10,000 giờ cho MỌI thứ)
    → NHƯNG: AI chunks = verbal/visual → THIẾU somatic/motor
    → = AI cho "BIẾT" nhạc lý → nhưng "NGHE ra violon hay" VẪN CẦN nghe THẬT nhiều
    → = AI cho "BIẾT" game design → nhưng "FEEL combat force=30 đúng" VẪN CẦN chơi/làm THẬT
    → = AI BOOST verbal/visual chunks → body experience chunks VẪN CẦN TỰ tích lũy
    → = "AI + practice thật" = expertise NHANH nhất
    → = "AI alone" = biết nhiều, evaluate KÉM (thiếu body chunks)
    → = "Practice alone" = evaluate tốt, biết HẸP (thiếu cross-domain chunks)


  MỖI NHẠC SĨ / CHUYÊN GIA = start melody RIÊNG:
    → Hầu hết nhạc sĩ: chunks từ CÙNG culture → evaluate GIỐNG nhau (phần lớn)
    → Số ít: start melody KHÁC → chunks KHÁC → evaluate KHÁC
    → = "Style riêng" = start melody hardware × chunks tích lũy = UNIQUE combination
    → Phần lớn GIỐNG (vì culture + training GIỐNG) → số ít KHÁC (hardware + experience ĐỘC)
    → = "Gu chung" = chunks culture CHUNG → "gu riêng" = start melody × unique experience
```

---

## 8.8 Input Control — Tắt vs Mở: Accuracy vs Magnitude

```
🟡 Não evaluate PER-INPUT → Body reward TỔNG THỂ:

  CƠ CHẾ:
    → Mỗi cortex evaluate input CỦA NÓ riêng:
      Visual cortex: "đẹp?" → signal
      Auditory cortex: "hay?" → signal
      Somatic: "sướng?" → signal
    → TỔNG HỢP signals → opioid release → TOÀN THÂN "feel"
    → 1 vùng evaluate "tốt": opioid NHẸ
    → NHIỀU vùng evaluate "tốt" CÙNG LÚC: opioid MẠNH (multi-modal bonus)
    → = "Bonus đồng bộ": 1+1+1 ≠ 3 → CÓ THỂ = 4-5 (synergy)


⭐ PFC WORKSPACE CÓ HẠN → mỗi input CHIẾM workspace:

    Visual: ~30% workspace (nếu mở mắt)
    Auditory: ~20% (nếu có âm thanh)
    Somatic: ~20% (nếu có cảm giác body)
    Verbal: ~20% (nếu đang nói/nghe lời)
    Motor: ~10% (nếu đang cử động)
    → TỔNG > 100% → workspace BỊ CHIA → mỗi input KHÔNG được full

  → TẮT 1 input = FREED workspace → input còn lại ĐƯỢC NHIỀU hơn:
    Nhắm mắt: visual freed → auditory CÓ THỂ gấp đôi workspace
    → = "Nghe RÕ HƠN" — không phải tai MẠNH hơn → PFC DÀNH nhiều hơn cho tai

  🟢 Research:
    → Người mù: auditory + somatic MẠNH hơn người sáng (neuroplasticity)
    → Người điếc: visual MẠNH hơn người nghe
    → = TẮT 1 kênh VĨNH VIỄN → kênh khác MẠNH LÊN (cortex repurpose)
    → = TẮT 1 kênh TẠM THỜI → kênh khác SẮC NÉT hơn (attention shift)


  2 CHIẾN LƯỢC — tùy MỤC ĐÍCH:

  ① TẮT input → TĂNG ACCURACY (đánh giá CHÍNH XÁC 1 kênh):
    → Nhắm mắt nghe nhạc: audio ĐƯỢC toàn bộ attention → nghe RÕ mọi chi tiết
      → "Hay HƠN" = detect nhiều detail hay hơn (nhưng dở CŨNG rõ hơn)
      → = ✅ Phổ biến — nhiều người nhắm mắt nghe nhạc hay
    → Tắt đèn khi thân mật: visual TẮT → somatic ĐƯỢC toàn bộ attention
      → Cảm nhận chạm RÕ HƠN + bớt visual self-judgment ("body tôi trông thế nào?")
      → = ✅ Phổ biến — 2 lý do: focus somatic + bớt self-consciousness
    → Ôm im lặng: verbal TẮT → somatic ĐƯỢC toàn bộ
      → Cảm nhận ôm RÕ NHẤT → oxytocin response MẠNH nhất
      → ✅ Sướng hơn nếu body-need LÚC ĐÓ = Touch/Connection
      → 🟡 Nhưng: nếu cần "được nghe" (Being Seen) → nói QUANTRỌNG hơn ôm im

    → KHI NÀO TẮT:
      Tinh chỉnh creative (anim, nhạc, thiết kế): TẮT noise → focus 1 kênh → accuracy
      Thiền / body-listening: TẮT tất cả → focus somatic → body signal RÕ nhất
      Evaluate chất lượng: TẮT distraction → focus sản phẩm → body check CHÍNH XÁC
      → = "Cần ĐÁNH GIÁ chính xác → TẮT noise"

  ② MỞ multi-modal → TĂNG MAGNITUDE (sướng NHIỀU, nhiều kênh cùng reward):
    → Concert live: visual (thấy nghệ sĩ) + audio (nghe nhạc) + somatic (bass rung body)
      + social (mọi người cùng enjoy) → 4 kênh ĐỒNG BỘ → reward CỰC MẠNH
      → = "Concert live SƯỚNG HƠN tai nghe" vì multi-modal sync
    → Nhà hàng fine dining: taste + visual (presentation) + audio (nhạc nền) + somatic (texture)
      → 4 kênh đồng bộ → "ngon HƠN ăn ở nhà" dù CÙNG MÓN
    → Du lịch: visual (cảnh mới) + somatic (khí hậu mới) + social (bạn đồng hành)
      + novelty (experience mới) → multi-modal → "nhớ MÃI"
      → = Tại sao "trải nghiệm > đồ vật": trải nghiệm = multi-modal → reward SÂU hơn

    → KHI NÀO MỞ:
      Enjoy / celebrate: MỞ HẾT → multi-modal → magnitude CAO
      Social bonding: MỞ → nhiều kênh connection → oxytocin MẠNH
      Travel / explore: MỞ → nhiều kênh novelty → chunks ĐA DẠNG nhất
      → = "Cần SƯỚNG NHIỀU → MỞ nhiều kênh đồng bộ"


  ⭐ ACCURACY vs MAGNITUDE — trade-off:

    TẮT: accuracy CAO + magnitude THẤP ("biết RÕ 1 thứ")
    MỞ: accuracy VỪA + magnitude CAO ("sướng NHIỀU nhưng mờ hơn per-kênh")
    → KHÔNG ai "đúng" → TÙY MỤC ĐÍCH:
      Cần đánh giá → TẮT (accuracy)
      Cần enjoy → MỞ (magnitude)
      Cần sáng tạo → TẮT lúc evaluate + MỞ lúc brainstorm (XENLẪN)
      → = "Tốt nhất = BIẾT KHI NÀO TẮT, KHI NÀO MỞ"

  ⚠️ "Bịt tai xem video" = trường hợp ĐẶC BIỆT:
    → Video THIẾT KẾ cho visual + audio CÙNG LÚC (nội dung từ CẢ 2)
    → Bịt tai = MẤT 50% nội dung (dialogue, nhạc, sound effects)
    → Thấy visual RÕ hơn → NHƯNG hiểu KÉMHƠN → ❌ KHÔNG hay hơn
    → NGOẠI TRỪ: video THUẦN visual (dance, art, nature) → bịt tai CÓ THỂ focus visual hơn
    → = "TẮT input chỉ TỐT khi input đó là NOISE → XẤU khi input đó là CONTENT"
```

---

## 8.9 Simulate Người Khác — Theory of Mind Qua Schema

```
⭐ "Hiểu người khác" = PFC simulate BẰNG chunks CỦA MÌNH:

  CƠ CHẾ (cùng §8 MODE 1 — không có hệ thống riêng):
    PFC: "sếp sẽ react thế nào nếu tôi nói X?"
    → PFC kích hoạt chunks [sếp] + chunks [tình huống X]
    → CÙNG pathway thật fire: emotional (amygdala), visual (mặt sếp), somatic (body response)
    → Body simulate: "feel" reaction CỦA SẾP → nhưng dùng ĐƯỜNG DÂY CỦA TÔI
    → = "Tôi simulate PHIÊN BẢN TÔI đóng vai sếp" ≠ "simulate SẾP"

  → GỐC RỄ GIỚI HẠN:
    ① Hardware KHÁC: DRD4, cortisol baseline, modality dominance — tôi và sếp KHÁC
    ② Compiled schema KHÁC: trải nghiệm khác → chunk association KHÁC
    ③ Body-base KHÁC: body-need states khác → melody KHÁC
    ④ §8.5 áp dụng: "KHÔNG THỂ imagine cái CHƯA TỪNG experience"
       → Tôi CHƯA experience being sếp → simulate sếp = REMIX chunks CỦA TÔI về sếp
    → = Simulate người khác LUÔN bị filter qua schema CỦA MÌNH


⭐ TẠI SAO CÓ THỂ PREDICT ĐÚNG (một phần):

  OVERLAP SPECIES — body-base CHUNG ~70-90%:
    → Đói = Body-Dissonance (ai cũng vậy — cùng loài)
    → Bị đánh = đau (ai cũng vậy — cùng nociception)
    → Mất người thân = buồn (ai cũng vậy — connection need)
    → = Body-base GIỐNG → simulate body response CỦA MÌNH ≈ body response CỦA HỌ
    → = "Đồng cảm cơ bản" = predict body-level reactions = CHÍNH XÁC CAO

  OVERLAP CULTURE — shared domain chunks:
    → Cùng VN → chunk [mất mặt] compiled GIỐNG → predict "mất mặt = đau" = ĐÚNG
    → Cùng dev → chunk [deadline dí] compiled GIỐNG → predict "stress" = ĐÚNG
    → KHÁC culture → chunk THIẾU → predict SAI
      (VD: người VN predict người Nhật → thiếu chunk [nemawashi] → hiểu sai quy trình)

  OVERLAP CÁ NHÂN — thời gian × depth:
    → Sống cùng 10 năm → tích lũy NHIỀU chunks về người đó
    → Chunks NHIỀU → body evaluate CHI TIẾT hơn (giống §8.7 expertise)
    → = "Hiểu ai đó SÂU" = tích lũy ĐỦ chunks → simulate người đó CHÍNH XÁC hơn
    → = "Người lạ" = ÍT chunks → simulate = default CULTURE chunks + SPECIES overlap


  ACCURACY FORMULA (conceptual):

    predict_accuracy(A→B) ≈ species_overlap
                            + culture_overlap(A, B)
                            + personal_chunks(A về B) × chunk_quality
                            − hardware_delta(A, B)
                            − schema_depth_mismatch(A, B)

    → Species overlap: CAO, gần constant (~70-90% body-level)
    → Culture overlap: tùy shared domain (0-80%)
    → Personal chunks: tùy thời gian + attention (0-90%)
    → Hardware delta: NE BIẾT ĐƯỢC → source of SYSTEMATIC ERROR
    → Schema depth mismatch: compiled sâu nhất = khó predict nhất


⭐ NÔNG vs SÂU — 2 mức predict KHÁC NHAU:

  NÔNG — predict HÀNH VI (surface schema):
    → Cơ chế: observation pattern matching
    → "Thấy em cáu 10 lần khi X → predict lần 11 em cáu" = chunk quality cao
    → KHÔNG cần hiểu TẠI SAO → chỉ cần chunks [X → cáu] compiled
    → = Giống §8.7 "người nghe nhiều nhạc": predict bài hay/dở → KHÔNG biết vì sao
    → Quan hệ lâu năm nhưng "không hiểu nhau" = nông cao, sâu thấp

  SÂU — predict MELODY (body-base + compiled schema + tại sao):
    → Cơ chế: simulate body-state CỦA HỌ (không phải body-state CỦA MÌNH)
    → "Biết em cáu VÌ em sợ bị bỏ rơi" = connectivity cao (hiểu cơ chế)
    → CẦN: chunks về NGUYÊN NHÂN (childhood, hardware, deep schema)
    → CỰC KHÓ — vì phải TẠM GÁC schema mình → dùng model ĐÃ BUILD về họ
    → = Giống §8.7 "đầu bếp": KHÔNG CHỈ "mặn" → mà "mặn VÌ X → fix BẰNG Y"
    → Therapist/bạn thân GIỎi = predict sâu → "biết TẠI SAO" người đó phản ứng

  KHÁC BIỆT THỰC TẾ:
    Vợ chồng 30 năm: NÔNG cực cao (predict hành vi gần 100%)
                      SÂU có thể THẤP ("biết sẽ cáu nhưng KHÔNG hiểu tại sao")
    Therapist 6 tháng: NÔNG trung bình (gặp ít → ít observation)
                       SÂU có thể CAO (trained simulate body-state người khác)


⭐ NGƯỜI KHÁC BIẾT SCHEMA MÀ PFC CHỦ NHÂN KHÔNG BIẾT:

  CƠ CHẾ:
    → Schema compiled SÂU = chạy ở VÔ THỨC → PFC KHÔNG observe được
    → PFC chỉ thấy ĐẦU RA (hành vi, cảm xúc surface)
    → Observer BÊN NGOÀI: thấy PATTERN hành vi lặp lại → build chunks VỀ pattern đó
    → = Observer có chunk MÀ chủ nhân KHÔNG CÓ

  VÍ DỤ:
    → "Bạn hay tự sabotage khi gần thành công"
      Chủ nhân: schema [gần thành công → lo → tự phá] compiled SÂU → PFC KHÔNG THẤY
      Bạn thân: THẤY pattern 5 lần → build chunk [A sabotage khi gần xong] → NÓI CHO A
      = Bạn thân có chunk VỀ A mà PFC CỦA A chưa bao giờ build
    → "Mày nói chuyện hay nhíu mày"
      Chủ nhân: motor schema compiled → PFC KHÔNG monitor (auto)
      Observer: visual pattern → build chunk → báo cho chủ nhân
    → "Em luôn chọn người giống bố"
      Chủ nhân: schema [partner selection] compiled từ childhood → PFC KHÔNG THẤY pattern
      Therapist: THẤY pattern qua nhiều câu chuyện → build chunk → insight MỚI cho client

  TẠI SAO OBSERVER THẤY MÀ CHỦ NHÂN KHÔNG:
    ① PFC chỉ observe ĐẦU RA → schema compiled = hộp đen
    ② Observer = "camera ngoài" — KHÔNG bị schema CỦA A filter
    ③ Observer TÁCH được pattern vì: A = 1 "input" → observer evaluate A (giống §8.7)
       Còn A evaluate CHÍNH MÌNH = self-referencing loop → BIAS cực mạnh
    ④ Self-referencing bias: PFC evaluate mình = dùng schema CỦA MÌNH evaluate schema CỦA MÌNH
       → Giống: dùng thước CONG đo xem thước có CONG không → luôn nói "thẳng!"

  GIÁ TRỊ = CHO CHUNKS VỀ CHÍNH BẠN:
    → Therapist / mentor / bạn thân: giá trị CHÍNH = external observer
    → Cho bạn chunks VỀ CHÍNH BẠN mà PFC bạn không tự build được
    → = "Gương" — bạn không thấy mặt mình nếu không có gương
    → Chunks mới VỀ MÌNH → PFC observe → có thể BẮT ĐẦU modify schema
    → = Therapy hiệu quả = therapist cho chunks → PFC observe → body re-evaluate → schema shift


⭐ TÒ MÒ VỀ NGƯỜI KHÁC — drive state đặc biệt:

  → Information gap VỀ NGƯỜI = Body-Dissonance nhẹ + Dopamine seeking
  → "Người này NGHĨ GÌ?" = schema simulate → KHÔNG match → gap → muốn biết thêm
  → Khi predict ĐÚNG: gap đóng → Body-Dissonance TẮT + Body-Reward → "À HA, understood!"
  → Khi predict SAI: gap MỞ → Body-Dissonance TĂNG → 2 hướng:
    ① Tò mò hơn → tìm thêm chunks → learn
    ② Frustrated → label "người kỳ lạ" → DỪNG tìm hiểu (close gap bằng label)
  → = "Judgemental" = dùng label ĐÓNG gap NHANH thay vì tích lũy chunks → predict NÔNG mãi


  HARDWARE ẢNH HƯỞNG ToM:
    → mPFC mạnh (PFC-Analysis.md §2.2): social cognition TỐT → predict người khác CHÍNH XÁC hơn
    → Oxytocin sensitivity cao: social reward MẠNH → MUỐN hiểu người hơn → tích lũy chunks NHIỀU hơn
    → DRD4 high: curiosity VỀ NGƯỜI cũng cao → information gap drive MẠNH
    → Somatic-dominant: empathy SÂU hơn (body simulate MẠNH → feel người khác rõ hơn)
    → Verbal-dominant: empathy NHẸ hơn (logic hiểu → nhưng body feel YẾU)
    → = Hardware KHÔNG quyết định "tốt/xấu" → quyết định KÊNH nào predict mạnh nhất
```

---

## 9. Ví Dụ Tổng Hợp — Archimedes "EUREKA"

```
🟡 Archimedes và bồn tắm — toàn bộ schema operations:

  TRƯỚC "EUREKA" (nhiều ngày):
    → Mục tiêu (PFC hold): "vương miện có phải vàng thuần?"
    → PFC mode 1 (simulate): thử draft → thử → chưa ra → thử tiếp
    → Cortisol: CAO (vua GIAO bài → threat + novelty loop)
    → PFC: MỆT (simulate nhiều ngày)
    → Micro-rewards: HIẾM (chưa ra → ít "feel đúng" → ít opioid)
    → = "Stuck" — novelty loop CHẠY nhưng KHÔNG flow (ít micro-reward)

  QUYẾT ĐỊNH ĐI TẮM:
    → PFC: MỆT quá → shift gradient → Novelty: 90% → 20% (treo)
    → Body-need: "cần relax" → PFC chọn → schema "đi tắm" kích hoạt
    → Compiled schema đi tắm: auto → PFC gần offline → RELAX

  TRONG BỒN TẮM — schema operations:
    Gradient lúc này:
      [0% PFC]     [5%]      [20%]        [80%?]
      Thở          Tay ngâm   Bài toán     CẢM GIÁC
      Tim          Body relax (TREO nhẹ)    NƯỚC ĐẨY
      Tiêu hóa     Water feel               (body input
                                              MỚI + MẠNH)

    → Body input MỚI: nước ĐẨY lên (somatic signal MẠNH — toàn body cảm nhận)
    → VTA: "biến động somatic LỚN!" → dopamine
    → PFC: CÓ THỂ nhận (dù đang relax — biến động ĐỦ LỚN)
    → NHƯNG quan trọng hơn: VÔ THỨC process:
      → Bài toán (TREO ở 20%): chunks "thể tích" + "vàng nặng" + "cân"
      → Somatic input: "nước ĐẨY" + "body CHIẾM chỗ trong nước"
      → Vô thức: "nước đẩy" + "chiếm chỗ" + "thể tích" → CONNECT
      → = Cross-domain: somatic experience × cognitive chunks → PATTERN MỚI
      → = Chunk CỰC LỚN (multi-modal + multi-domain sync)
      → VTA: biến động CỰC LỚN (nhiều vùng não đồng bộ) → dopamine CỰC MẠNH

    → PFC: "EUREKA!" = nhận blueprint TỪVÔ THỨC → coherence CỰC MẠNH
    → Body: opioid SPIKE (mọi thứ KHỚP — coherence peak)
    → = Nhảy khỏi bồn → chạy ra đường → hét "EUREKA!"
    → = Schema override body-base (quên mặc quần áo — L2 Comfort bị override bởi coherence reward)

  TẠI SAO lúc TẮM mới ra (schema operations giải thích):
    → Ngồi bàn: PFC mode 1 (simulate) → PFC FILTER mạnh → chỉ cho "logic" qua
    → Trong bồn: PFC RELAX (gần offline) → vô thức TỰ DO → thử kết nối KHÔNG BỊ FILTER
    → + Body input MỚI (nước đẩy): chunk CHƯA CÓ trong bài toán → trigger connection
    → = "Relax + body experience mới → vô thức TỰ DO connect → eureka"
    → = NẾU PFC cố nghĩ tiếp → filter "hợp lý" → CÓ THỂ miss connection "nước đẩy = thể tích"
```

---

## 10. Ví Dụ Tổng Hợp — Khát Nước (gradient chi tiết)

```
TOÀN BỘ tiến trình "khát → uống" qua gradient:

  BƯỚC 1 — Vô thức detect "THIẾU" (PFC: 0%):
    → Body: osmoreceptors detect "nồng độ máu CAO" → hypothalamus: "KHÁT"
    → Body signal: "khô miệng" → BẮT ĐẦU
    → PFC: CHƯA biết (signal yếu, monitor body-need chưa trigger)
    → = Schema "khát" ĐANG ở 0-5% gradient (body only)

  BƯỚC 2 — Signal TĂNG → monitor TRIGGER (PFC: 5% → 20%):
    → Khát tăng → body signal MẠNH hơn → body-need monitor: "KHÁT đủ mạnh!"
    → Monitor → kéo PFC nhẹ → PFC: "hmm... khát..." → BIẾT
    → NHƯNG: nếu PFC đang Novelty sâu → có thể CHƯA chuyển
    → "Khát nhưng đang bận → chịu thêm chút" = PFC keep spotlight ở Novelty

  BƯỚC 3 — PFC quyết định (PFC: 30% → 50%):
    → Khát TĂNG tiếp → body-need signal OVERRIDE Novelty spotlight
    → PFC: "ok, phải uống → ĐI" → 1 LỆNH ngắn
    → PFC KHÔNG draft chi tiết "bước 1 đi bàn, bước 2 cầm ca..."
    → PFC chỉ: "uống nước" → trigger CHUỖI compiled schemas

  BƯỚC 4 — Chuỗi compiled CHẠY (PFC: 5-10% giám sát):
    → Schema "đứng dậy": auto → chân đứng
    → Schema "đi tới bàn": auto → chân bước → biết hướng bàn (compiled)
    → Schema "cầm ca": auto → tay cầm
    → Schema "rót nước": auto → tay nghiêng bình
    → Schema "uống": auto → tay đưa miệng → uống
    → PFC: GIÁM SÁT NHẸ (5-10%) → "mọi thứ ok" → có thể NGHĨ việc khác
    → = "Đi uống nước mà đang nghĩ việc KHÁC" = compiled chain + PFC freed

  BƯỚC 5 — Body confirm "ĐỦ" (PFC: dần về 0%):
    → Nước vào → osmoreceptors: "nồng độ GIẢM" → Satisfaction Signal
    → Schema "tìm nước": VÔ THỨC auto DỪNG (Satisfaction fire → schema stop)
    → PFC: KHÔNG biết dừng → chỉ thấy "hết khát" → quay lại việc khác
    → = Satisfaction Signal → vô thức dừng → PFC chỉ thấy KẾT QUẢ "hết khát"

  → TOÀN BỘ = gradient SHIFT liên tục:
    0% → 5% → 20% → 50% → 10% → 0% (quay lại)
    Body → monitor → PFC biết → PFC lệnh → compiled chain → Satisfy → done
    → = PFC chỉ THAM GIA ở GIỮA (quyết định) → đầu + cuối = VÔ THỨC
```

---

## 11. Honest Assessment

```
  ESTABLISHED (🟢):
    → Gradient attention: established (Dehaene "global workspace theory")
    → Habituation: established neuroscience
    → Cocktail party effect: Cherry 1953
    → Task switching cost: established cognitive psychology
    → Schema compilation: established (skill acquisition research)
    → Flow = micro-reward chain: Csikszentmihalyi + neuroscience support

  FRAMEWORK SUY LUẬN (🟡):
    → VTA detect "biến động" (không phải "mới"): consistent, refinement of prediction error
    → Interrupt hierarchy: observable, chưa có formal ranking research
    → Always-on monitors at 10-20% PFC: logical, chưa đo chính xác
    → Body reward TRONG LÚC schema (không chỉ khi xong): consistent, observation-based
    → DRD4 × gradient: Hypothesis D — chưa proven trực tiếp
    → Simulate người khác = dùng chunks CỦA MÌNH: consistent với simulation theory
      of mind (Goldman 2006) + shared neural representations (Gallese 2005)
    → Accuracy ≈ overlap (species + culture + personal): logical, chưa formalize
    → Observer advantage (thấy pattern chủ nhân không thấy): consistent với
      blind spot bias (Pronin 2002) + self-serving bias literature

  METAPHOR (⚠️):
    → "Spotlight PFC": hữu ích nhưng PFC KHÔNG phải literal spotlight
    → "Gradient 0-100%": continuous nhưng KHÔNG đo được chính xác per-%
    → = Dùng để HÌNH DUNG, KHÔNG phải ĐO LƯỜNG
```

---

## 12. Kết Nối

```
→ Schema-Atlas-v2.md: schema PROPERTIES (file này nói OPERATIONS)
→ Schema-Example.md: ví dụ cụ thể (tình yêu, học tập, nhạc)
→ Architecture-v7.5-Draft.md: kiến trúc TỔNG THỂ
→ PFC-Analysis.md: PFC mechanism chi tiết (neuron level)
→ Attention-Spectrum.md: DRD4 threshold → gradient position KHÁC per-person
→ Imagination-Analysis-v2.md: imagine = PFC simulate mode 1
→ Novelty-Loop.md: vòng lặp khi schema CHƯA resolve
→ Cortisol-Baseline.md: cortisol/NE → "năng lượng" cho gradient shift
→ Personal-Melody.md: schema tổng thể cá nhân = melody
→ Personal-Melody.md §6.6: predict melody người khác — overlap + nông/sâu
→ PFC-Analysis.md §2.2.1: mPFC × Theory of Mind hardware
→ Relationships.md §4-5: "hiểu nhau" 4 sub-params + convergence
→ Why-Body-Knows.md: tại sao body check ĐÁNG TIN
```

---

> *Schema Operations — "Schema = cách xử lý SẴN SÀNG chạy.
> Gradient liên tục: vô thức auto ↔ PFC deep focus.
> Nhiều schemas chạy CÙNG LÚC ở vị trí KHÁC trên gradient.
> VTA detect BIẾN ĐỘNG (không phải 'mới'). PFC = spotlight QUAY.
> Body reward LIÊN TỤC trong lúc chạy (không chỉ khi xong).
> Flow = micro-reward chain không đứt."*
