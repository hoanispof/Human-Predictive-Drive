# Unconscious Desire (UD) — Giả Thiết Thay Thế Prediction Error

**DRAFT v1 — Giả thiết mới, chưa kiểm chứng**
**Trạng thái: Speculative — cần peer review và experimental validation**

---

## 1. Vấn Đề Với Reward Prediction Error (RPE)

### 1.1 RPE là gì? (Schultz 1997)

```
Công thức gốc:
  Dopamine = actual_reward − predicted_reward

Schultz record dopamine neurons ở khỉ:
  Unexpected reward → dopamine FIRE (positive PE)
  Expected reward → dopamine = 0 (no PE)
  Expected reward missing → dopamine SUPPRESS (negative PE)

→ Dopamine = SURPRISE signal, không phải reward signal
→ Đây là consensus neuroscience hiện tại
```

### 1.2 Các điểm RPE giải thích TỐT

```
✅ Khỉ + nước: unexpected juice → dopamine. Expected → no dopamine.
✅ Timing PE: juice delay → dopamine suppress tại expected time, fire tại actual time
✅ Quantitative: PE size proportional to dopamine firing (Bayer & Glimcher 2005)
✅ Learning: PE = 0 → không học thêm (blocking effect)
✅ Addiction: drugs hijack PE system → artificial dopamine spikes
```

### 1.3 Các điểm RPE giải thích KHÔNG TỐT

```
❌ Case 1: Người thân tặng quà (expected) → VẪN VUI HƠN người lạ tặng (unexpected)
   RPE predict: unexpected > expected. Thực tế: ngược lại.
   RPE defense: "value khác nhau" → nhưng value đến từ đâu? → từ DESIRE.

❌ Case 2: "Vừa ý" > "Khác ý" — match desire > surprise
   RPE predict: khác ý = more error = more dopamine
   Thực tế: vừa ý thường sướng hơn khác ý

❌ Case 3: Nghe lại bài hát yêu thích lần 50 — VẪN thích
   RPE predict: fully predicted → PE = 0 → nên chán
   Thực tế: giảm dần nhưng KHÔNG = 0

❌ Case 4: Về quê — zero novelty, fully predicted, VẪN VUI
   RPE predict: PE = 0 → nên bình thường
   Thực tế: về quê thường rất vui dù không có gì mới

❌ Case 5: Confirmation bias — tại sao não THÍCH info confirm belief?
   RPE predict: confirming = predicted = PE low → nên boring
   Thực tế: confirmation bias CỰC MẠNH, người ta THÍCH được confirm

❌ Case 6: Trẻ con đòi nghe lại câu chuyện yêu thích hàng trăm lần
   RPE predict: fully predicted → PE = 0 → nên không muốn nghe
   Thực tế: đòi nghe NỮA, khóc nếu không cho nghe

❌ Case 7: Sex với partner lâu năm — vẫn enjoy, giảm nhưng không = 0
   RPE predict: fully predicted → PE ≈ 0
   Thực tế: giảm nhưng không mất hoàn toàn

❌ Case 8: Mong mưa, check forecast biết sẽ mưa, mưa thật → VẪN VUI
   RPE predict: expected → PE = 0
   Thực tế: vẫn vui khi mưa thật
```

### 1.4 RPE thường "rescue" bằng cách nào?

```
Defense 1: "Đó là opioid/oxytocin, không phải dopamine"
  → Có thể đúng cho một số case
  → Nhưng nếu dopamine = 0 → tại sao vẫn MUỐN nghe lại bài hát?
  → Wanting (dopamine) vẫn có → dopamine KHÔNG = 0

Defense 2: "Micro-variations tạo micro-PE"
  → Mỗi lần nghe bài hát, context hơi khác → micro-PE
  → Có lý... nhưng rất ad-hoc, giải thích mọi thứ → unfalsifiable

Defense 3: "Value khác nhau nên PE khác nhau"
  → Đúng, nhưng "value" = DESIRE → phải add desire vào formula
  → = Đang tiến về phía UD mà không nhận ra
```

---

## 2. Giả Thiết UD — Unconscious Desire

### 2.1 Core Concept

```
Dopamine KHÔNG fire vì "surprise" (prediction error).
Dopamine fire vì "unconscious desire được đáp ứng" (desire fulfillment).

Hai loại "prediction" khác nhau:

TYPE 1 — PFC prediction (conscious expectation):
  "Tôi NGHĨ sẽ xảy ra X"
  → Có thể đúng hoặc sai
  → Khi sai = surprise

TYPE 2 — Unconscious desire (vô thức mong muốn):
  "Vô thức MUỐN X xảy ra"
  → Nhiều schema song song, ẩn, PFC không biết hết
  → Khi được đáp ứng = dopamine fire
  → Khi không được đáp ứng = dopamine suppress

RPE chỉ đo TYPE 1.
UD đo TYPE 2 (và TYPE 1 là special case).
```

### 2.2 Công Thức

```
RPE (Schultz):
  Dopamine = actual_reward − predicted_reward

UD:
  Dopamine = Σ(desire_i × match_i) − Σ(pre_simulated_i)

  Trong đó:
    desire_i        = schema vô thức thứ i đang mong muốn (strength 0→1)
    match_i         = reality match desire đó bao nhiêu (0→1)
    pre_simulated_i = desire đã được giả lập trước bao nhiêu (0→1)
                      (PFC hoặc vô thức đã tưởng tượng/simulate trước)

  Khi desire_i = 1 (chỉ 1 desire, conscious, simple):
    UD = actual × match − pre_simulated
        = actual_reward − predicted_reward
        = RPE

  → RPE là TRƯỜNG HỢP ĐẶC BIỆT của UD
     khi desire = simple + conscious + single-layer
```

### 2.3 Tại sao RPE = special case?

```
Thí nghiệm Schultz — Khỉ + nước:
  Desire: muốn nước (1 desire, conscious, biological)
  → desire_1 = 1, chỉ có 1 desire
  → match_1 = 1 khi có nước, 0 khi không
  → pre_simulated = 1 khi đã learn signal → nước

  Unexpected juice: match=1, pre_simulated=0 → UD = 1 → dopamine HIGH
  Expected juice:   match=1, pre_simulated=1 → UD = 0 → dopamine = 0
  Expected no juice: match=0, pre_simulated=1 → UD = -1 → dopamine suppress

  → UD và RPE cho CÙNG kết quả ở case đơn giản
  → Schultz KHÔNG SAI — chỉ incomplete

  Tương tự: Newton không sai, chỉ là special case của Einstein
    Tốc độ thấp → Newton đủ chính xác
    Tốc độ cao → cần Einstein

    Desire đơn giản → RPE đủ chính xác
    Desire phức tạp (người) → cần UD
```

---

## 3. Kiểm Chứng — 12 Cases

### 3.1 Cases mà RPE và UD cho CÙNG kết quả

```
CASE 1: Khỉ + unexpected juice
  RPE: surprise → dopamine ✅
  UD: desire fulfilled + not pre-simulated → dopamine ✅
  → Không phân biệt được

CASE 2: Eureka moment
  RPE: unexpected solution → dopamine
  UD: unconscious desire for coherence fulfilled → dopamine
  → Cả hai predict dopamine, nhưng UD giải thích TẠI SAO eureka
     chỉ xảy ra khi ĐÚNG (match desire), không khi SAI (surprise nhưng wrong)
```

### 3.2 Cases mà UD predict ĐÚNG HƠN RPE

```
CASE 3: Người thân vs người lạ tặng quà
  RPE: người lạ = more surprise = more PE → nên sướng hơn ❌
  UD: người thân = MATCH nhiều unconscious desire (connection, love, belonging)
       → Nhiều desire_i × match_i → dopamine MẠNH HƠN ✅
  Thực tế: Người thân tặng quà → ý nghĩa hơn ✅ UD wins

CASE 4: "Vừa ý" vs "Khác ý nhưng đẹp hơn"
  RPE: khác ý = more surprise = more PE → nên sướng hơn ❌
  UD: vừa ý = MATCH desire → dopamine. Khác ý = surprise nhưng less match
  Thực tế: "Vừa ý" thường preferred ✅ UD wins

CASE 5: Về quê (zero novelty)
  RPE: fully predicted, nothing new → PE = 0 → nên bình thường ❌
  UD: match NHIỀU deep desire (nhà, thuộc về, an toàn, ký ức)
       → Nhiều schema fulfilled → dopamine + opioid + oxytocin
  Thực tế: Về quê thường rất vui ✅ UD wins

CASE 6: Confirmation bias
  RPE: confirming info = predicted = PE low → nên boring ❌
  UD: confirming info = MATCH schema desire (vô thức muốn schema đúng)
       → desire fulfilled → dopamine → THÍCH
       Disconfirming info = AGAINST desire → dopamine suppress → KHÔNG THÍCH
  Thực tế: Confirmation bias cực mạnh ✅ UD giải thích trực tiếp

CASE 7: Trẻ con nghe lại câu chuyện yêu thích
  RPE: fully predicted → PE = 0 → nên chán ❌
  UD: desire for narrative experience chưa exhausted
       → Mỗi lần = desire fulfilled (giảm dần do pre-simulation tăng)
  Thực tế: Đòi nghe lại hàng trăm lần, giảm DẦN ✅ UD wins

CASE 8: Nghe bài hát yêu thích lần 50
  RPE: fully predicted → PE = 0 → cliff (ngừng hẳn) ❌
  UD: desire giảm dần (pre-simulated tăng) → gradient smooth
  Thực tế: Giảm dần, không cliff ✅ UD predict gradient đúng hơn

CASE 9: Sex với partner lâu năm
  RPE: fully predicted → PE ≈ 0 ❌
  UD: biological desire RENEW (hormone cycle) + emotional desire
       → Desire refreshed mỗi lần → match vẫn cao → dopamine > 0
  Thực tế: Giảm nhưng không mất ✅ UD wins

CASE 10: Mong mưa, biết sẽ mưa, mưa thật → vẫn vui
  RPE: expected → PE = 0 ❌
  UD: desire for mưa → fulfilled → dopamine
  Thực tế: Vẫn vui ✅ UD wins

CASE 11: Unexpected wrong answer khi giải bài toán
  RPE: unexpected → PE → nên fire dopamine?
       (RPE phải qualify: "reward PE" vs "non-reward PE")
  UD: wrong = NOT match desire → dopamine suppress
       → Đơn giản, không cần qualify
  Thực tế: Frustrating, không sướng ✅ UD đơn giản hơn

CASE 12: Einstein — vô thức lờ mờ biết trước
  RPE: solution = surprise → dopamine (nhưng không giải thích hướng)
  UD: vô thức desire coherence → PFC giả lập → vô thức evaluate "gần đúng"
       → dopamine (approaching fulfillment) → PFC refine → loop
       → Eureka = full fulfillment of accumulated desire
  → UD giải thích PROCESS, RPE chỉ giải thích MOMENT ✅
```

### 3.3 Mở rộng kiểm chứng — 24 Cases đa dạng (Real-world prediction test)

**Logic:** Nếu UD đúng → predict đúng hành vi thực tế ở những chỗ RPE predict sai.

#### Nhóm A: Quan hệ & Tình cảm

```
A1: Tại sao ôm người thân quen VẪN ấm dù không có gì mới?
  RPE: ôm quen → predicted → PE = 0 → nên bình thường ❌
  UD: vô thức desire connection → fulfilled mỗi lần ôm
       Pre-simulated cao → giảm, nhưng body desire RENEW
  Thực tế: Ôm người thân vẫn ấm dù lần thứ 10,000 ✅ UD

A2: Tại sao xa người yêu lâu → gặp lại CỰC SƯỚNG?
  RPE: gặp lại = expected (biết sẽ gặp) → PE vừa
  UD: desire tích lũy SUỐT thời gian xa
       Pre-simulation qua video call KHÔNG đủ fidelity
       → Gặp thật = MASSIVE remaining desire fulfilled
  Thực tế: Gặp lại sau xa lâu = cực kỳ emotional ✅ UD
  Bonus: Giải thích tại sao video call KHÔNG thay thế gặp thật
         (simulation fidelity thấp → desire chưa fully pre-fulfilled)

A3: Tại sao nói "Anh yêu em" lần thứ 1000 VẪN có ý nghĩa?
  RPE: fully predicted phrase → PE = 0 → nên meaningless ❌
  UD: vô thức desire "được confirm yêu" → RENEW (không habituate hoàn toàn)
       Mỗi lần = micro-fulfillment
  Thực tế: Vẫn meaningful, dù giảm intensity ✅ UD

A4: Tại sao bị ghost ĐAU hơn bị từ chối thẳng?
  RPE: ghost = uncertain → PE unclear. Từ chối = clear PE âm.
       → Ghost nên ÍT đau hơn (less clear PE) ❌
  UD: ghost = desire for response KHÔNG ĐƯỢC FULFILLED + KHÔNG BIẾT KHI NÀO
       → Desire tồn tại mãi, không được resolve
       → Từ chối = desire TERMINATED → đau nhưng ĐÓNG được
  Thực tế: Ghost đau hơn từ chối ✅ UD
```

#### Nhóm B: Ăn uống & Cảm giác

```
B1: Tại sao "cơm mẹ nấu" ngon hơn nhà hàng 5 sao?
  RPE: cơm mẹ = fully predicted, nhà hàng = novel → nhà hàng nên thích hơn ❌
  UD: cơm mẹ match NHIỀU desire layers:
       taste schema (quen từ nhỏ) + connection (mẹ) + safety (nhà)
       + identity ("tôi thuộc về đây")
       Nhà hàng: chỉ match taste + novelty, ít desire layers
  Thực tế: Nhiều người prefer cơm mẹ ✅ UD

B2: Tại sao ăn khi ĐÓI ngon hơn ăn khi NO?
  RPE: cùng món → same PE → nên same ❌
  UD: đói = biological desire TĂNG → match degree khi ăn = HIGHER
       No = desire GIẢM → match degree khi ăn = LOWER
  Thực tế: Đói ăn ngon hơn ✅ UD
  (RPE cần thêm "homeostatic component" — tức là thêm desire!)

B3: Tại sao comfort food KHI BUỒN đặc biệt ngon?
  RPE: comfort food = predicted → PE low → nên bình thường ❌
  UD: buồn = nhiều desire CHƯA fulfilled (connection, safety, comfort)
       Comfort food = partial fulfillment qua taste + memory schema
       → Desire strength TĂNG (vì đang deficit) → match = SƯỚNG HƠN
  Thực tế: Comfort food khi buồn = đặc biệt satisfying ✅ UD

B4: Tại sao ăn 1 mình KHÔNG NGON bằng ăn với bạn?
  RPE: cùng món, cùng PE → nên same ❌
  UD: ăn với bạn = taste desire + connection desire CÙNG LÚC
       → Nhiều desire layers matched → total fulfillment HIGHER
  Thực tế: Ăn cùng người thường ngon hơn ✅ UD
```

#### Nhóm C: Công việc & Sáng tạo

```
C1: Tại sao hoàn thành project lớn → SƯỚNG dù biết trước sẽ xong?
  RPE: biết sẽ xong → expected → PE ≈ 0 → nên bình thường ❌
  UD: desire for completion tích lũy SUỐT project
       Mỗi ngày thêm 1% → desire cho "xong" TĂNG
       Hoàn thành = MASSIVE accumulated desire fulfilled
  Thực tế: Hoàn thành project lớn = euphoria ✅ UD

C2: Code chạy đúng lần đầu vs fix bug lần thứ 10
  RPE: code lần đầu = unexpected success = HIGH PE
       Fix bug lần 10 = expected success = LOW PE → RPE đúng ở đây?
  UD: code lần đầu = desire "tôi viết đúng" + no pre-simulation
       Fix bug lần 10 = desire giảm (frustrated, pre-simulated failure nhiều)
  → TIE (cả hai framework predict cùng hướng)

C3: Tại sao FLOW state cảm giác tốt?
  RPE: trong flow, predict accuracy CAO → PE thấp → nên boring? ❌
       RPE phải nói "micro-PE liên tục" → ad hoc
  UD: flow = desire for mastery/completion LIÊN TỤC được fulfilled
       → Mỗi bước nhỏ = micro-fulfillment
       → Desire RENEW liên tục (task tiếp theo)
       → Không cần surprise, chỉ cần continuous fulfillment
  Thực tế: Flow = feeling tốt + no surprise needed ✅ UD

C4: Tại sao intrinsic motivation >>> extrinsic?
  RPE: cùng task, cùng PE → nên same motivation ❌
  UD: làm vì thích = desire INTERNAL (strong, multi-layer)
       Làm vì bị bắt = no internal desire (chỉ có avoidance)
       → Desire strength khác → fulfillment khác → motivation khác
  Thực tế: Intrinsic >>> extrinsic ✅ UD
  (SDT — Self-Determination Theory consistent)
```

#### Nhóm D: Giải trí & Nghệ thuật

```
D1: Tại sao khóc KHI XEM PHIM dù biết là giả?
  RPE: biết giả → predicted → PE = 0 → nên không react ❌
  UD: vô thức desire "tình thương có thật", "hy sinh có ý nghĩa"
       Phim simulate scenario match desire → desire fulfilled
       Biết giả ở PFC, nhưng VÔ THỨC không phân biệt simulate vs real
       → Desire fulfilled → opioid fire → khóc
  Thực tế: Khóc khi xem phim dù biết giả ✅ UD

D2: Tại sao nhạc buồn khi buồn lại THÍCH nghe?
  RPE: nhạc buồn = negative valence → nên tránh ❌
  UD: khi buồn = desire "được HIỂU", "không cô đơn trong nỗi buồn"
       Nhạc buồn = "ai đó cũng buồn như tôi" → desire for VALIDATION
       → Desire "được hiểu" fulfilled → opioid (connection, dù 1 chiều)
  Thực tế: Nhiều người seek nhạc buồn khi buồn ✅ UD

D3: Tại sao twist ending HAY → phải "make sense"?
  RPE: twist = MAX surprise = MAX PE → nên LUÔN hay ❌
  UD: twist hay = surprise + MATCH deep narrative desire
       ("à! hóa ra mọi thứ có ý nghĩa!" = desire for coherence fulfilled)
       Twist dở = surprise nhưng KHÔNG match → frustrating
  Thực tế: Random twist = annoying, coherent twist = amazing ✅ UD
  RPE không phân biệt được twist hay vs twist dở ❌

D4: Tại sao đọc lại sách hay VẪN enjoy dù biết hết nội dung?
  RPE: fully predicted → PE = 0 → nên chán ❌
  UD: desire for wisdom/beauty/meaning → re-activated mỗi lần đọc
       → Deeper understanding = new desire layers matched
  Thực tế: Sách hay đọc lại vẫn giá trị, thậm chí HƠN ✅ UD
```

#### Nhóm E: Đời sống hàng ngày

```
E1: Tại sao về nhà sau ngày dài → THỞ PHÀO dù nhà GIỐNG HỆT sáng nay?
  RPE: nothing changed → PE = 0 → nên neutral ❌
  UD: desire for safety, comfort, "của mình" → FULFILLED khi về nhà
       Cả ngày ở ngoài = desire TÍCH LŨY → về nhà = release
  Thực tế: Về nhà = relief + comfort ✅ UD

E2: Tại sao ngủ trên giường mình NGON hơn giường khách sạn 5 sao?
  RPE: khách sạn = novel + comfortable → PE cao → nên thích hơn ❌
  UD: giường mình = match schema "an toàn" + "quen" + "của mình"
       Nhiều desire layers match → sleep better
       Khách sạn = novel nhưng desire "nhà" KHÔNG matched
  Thực tế: Nhiều người ngủ tốt hơn ở nhà ✅ UD

E3: Tại sao nhận lương ĐÚNG HẠN vẫn vui dù biết trước?
  RPE: predicted salary → PE = 0 → nên bình thường ❌
  UD: desire "được trả công" + "an toàn tài chính" → fulfilled
       Pre-simulated nhưng financial desire RENEW mỗi tháng
  Thực tế: Check lương vẫn vui ✅ UD

E4: Tại sao tắm nước ấm SAU ngày lạnh → cực sướng?
  RPE: biết nước sẽ ấm → expected → PE low ❌
  UD: body desire "ấm" TÍCH LŨY cả ngày lạnh
       → Nước ấm = MASSIVE body desire fulfilled
       → Desire strength tỷ lệ thuận với thời gian thiếu
  Thực tế: Tắm ấm sau lạnh = heavenly ✅ UD
```

#### Nhóm F: Cases KHÓ — Fair Testing

```
F1: Jump scare VẪN sợ dù biết sẽ có?
  RPE: biết → predicted → PE low → nên không sợ ❌ (RPE cũng fail)
  UD: desire "an toàn" → threatened bởi stimulus → desire VIOLATED
       → Amygdala response (faster than prediction or desire)
  → CẢ HAI cần thêm "reflex bypass" để giải thích → TIE (cả hai yếu)
  → ⚠️ Cần phân tích riêng — xem §3.4

F2: Bất ngờ tìm thấy tiền rơi = SƯỚNG
  RPE: unexpected reward → PE → dopamine ✅
  UD: desire "giàu hơn" (luôn có) → fulfilled → dopamine ✅
  → TIE (cả hai giải thích tốt)

F3: Addictive drugs — lần đầu vs lần 100
  RPE: lần 100 = predicted → PE low → nên hết thích ❌
       RPE cần thêm "hijack" explanation
  UD: desire TĂNG (sensitization) → nhưng fulfillment GIẢM (tolerance)
       → Wanting tăng, liking giảm = Berridge's finding
       → desire_i tăng, match_i giảm → net = suffering (want but don't enjoy)
  → UD giải thích addiction loop GỌN HƠN ✅ UD
```

### 3.4 Phân tích riêng: F1 — Jump Scare (3-Layer Model)

```
⚠️ Tại sao jump scare VẪN SỢ dù biết sẽ có?
   Đây là case KHÓ cho cả RPE lẫn UD. Phân tích sâu:
```

#### 3.4.1 Cơ chế: Amygdala override TẤT CẢ

```
Luồng thông tin khi có stimulus đe dọa:

  Mắt/Tai nhận stimulus
    ├→ CON ĐƯỜNG NHANH: Thalamus → Amygdala (~12ms)
    │   → "CÓ GÌ ĐÓ!" → cortisol + adrenaline → FREEZE/STARTLE
    │   → KHÔNG qua cortex, KHÔNG qua PFC
    │   → Rough processing: chỉ cần "giống nguy hiểm" là fire
    │   → False positive CAO (bóng cây → tưởng rắn)
    │
    └→ CON ĐƯỜNG CHẬM: Thalamus → Visual Cortex → PFC → Amygdala (~200-500ms)
        → "À, đó là cái gì cụ thể" → đánh giá → suppress hoặc confirm
        → High accuracy nhưng CHẬM

  → Khoảng cách 12ms vs 200ms = ~188ms Amygdala hành động MÀ KHÔNG AI kiểm soát
  → Trong 188ms đó: tim đã đập nhanh, cơ đã căng, cortisol đã release
  → PFC đến sau: "à, chỉ là phim" → nhưng BODY ĐÃ PHẢN ỨNG RỒI
```

#### 3.4.2 Tại sao Amygdala mạnh hơn CẢ các vô thức khác?

```
Evolutionary logic:
  Thấy "cái gì đó giống rắn":
    Option A: Chờ PFC xác nhận (200ms) → NẾU là rắn → bị cắn → chết
    Option B: Amygdala fire ngay (12ms) → nhảy tránh → NẾU không phải → mất 1 calorie

  Cost of false positive (nhảy tránh cành cây): thấp
  Cost of false negative (không tránh rắn thật): cực cao (chết)
  → Evolution THIẾT KẾ Amygdala để false positive CAO
  → "Sợ nhầm còn hơn chết đúng"

Hierarchy ưu tiên trong não:

  SURVIVAL (Amygdala)     ← override TẤT CẢ
    > DESIRE (UD system) ← override PFC
      > HABIT (BG)        ← override conscious intention
        > CONSCIOUS (PFC) ← yếu nhất, chậm nhất

Ví dụ:
  Đang ăn ngon (desire fulfilled) → Jump scare!
    → Amygdala: OVERRIDE desire, habit, PFC → survival mode
  Đang flow coding (continuous fulfillment) → Cháy nhà!
    → Amygdala: OVERRIDE flow → chạy
    → Không ai "flow" trong đám cháy
  Đang ngủ (PFC offline, BG offline) → Tiếng nổ!
    → Amygdala: STILL ACTIVE khi ngủ → wake + startle
    → Amygdala KHÔNG BAO GIỜ ngủ hoàn toàn

Tương tự computer science:
  Hardware interrupt > Software interrupt > User process
  Khi hardware interrupt fire → MỌI process khác bị pause
  Amygdala = hardware interrupt ưu tiên cao nhất
```

#### 3.4.3 Tại sao PFC "biết" mà KHÔNG suppress được?

```
PFC suppress Amygdala = CÓ THỂ, nhưng:

  1. Suppression cần THỜI GIAN
     PFC → vmPFC → Amygdala (inhibitory connection)
     → MẤT ~200-500ms để activate
     → Jump scare exploit window TRƯỚC KHI suppression kịp

  2. PFC "biết" = VAGUE prediction
     PFC: "sẽ có jump scare ở đâu đó" = abstract knowledge
     Amygdala: cần CHÍNH XÁC timing + stimulus → vague prediction KHÔNG ĐỦ
     → "Biết sẽ có" ≠ "biết chính xác khi nào + cái gì"
     → Amygdala vẫn bị trigger bởi specific sudden stimulus

  3. Suppression GIẢM khi stress/mệt
     PFC = resource-intensive, cần glucose, cần nghỉ
     Amygdala = low-resource, luôn sẵn sàng
     → Mệt → PFC yếu → Amygdala override DỄ HƠN
     → Horror movie ĐÊM KHUYA sợ hơn ban ngày (PFC mệt hơn)

  4. Suppression KHÔNG BAO GIỜ = 0
     Exposure therapy: lặp lại "sợ → không sao" nhiều lần
     → PFC gradually builds stronger inhibitory connection
     → Nhưng Amygdala VẪN fire, chỉ bị dampen intensity
     → Giống: giảm âm lượng nhưng KHÔNG TẮT được loa
```

#### 3.4.4 Timeline chi tiết của 1 jump scare

```
T = 0ms:      Stimulus xuất hiện (mặt quỷ + tiếng hét)
T = 12ms:     Amygdala FIRE → cortisol + adrenaline release
              Tim đập nhanh, cơ căng, mắt mở to
              → REFLEX — không ai kiểm soát được
              → Mọi system khác BỊ PAUSE

T = 50-100ms: Body response peak — giật mình, có thể la hét
              UD system CHƯA online lại
              PFC CHƯA process xong

T = 200ms:    PFC bắt đầu process: "cái gì vừa xảy ra?"
              Visual cortex: "mặt quỷ CGI, đang xem phim"

T = 300-500ms: PFC → vmPFC → Amygdala: "an toàn, chỉ là phim"
               Amygdala: intensity GIẢM (nhưng cortisol đã release rồi)
               UD system online lại

T = 500ms-2s:  UD evaluate:
               → Desire "an toàn" bị violated tạm thời → nay RE-FULFILLED
               → Desire "kích thích" → FULFILLED (sợ thật!)
               → Relief + excitement = net positive (nếu thích horror)
               → Hoặc: net negative (nếu ghét horror)

T = 2-10s:     Cortisol dần giảm
               Laughter (nếu thích) hoặc tense (nếu ghét)
               → PFC: "sợ thật, nhưng hay" hoặc "không xem nữa"

T = phim tiếp: Amygdala: sensitivity TĂNG (hypervigilant)
               PFC: suppression attempt TĂNG
               UD: desire "kích thích" có thể tăng hoặc giảm tùy người
               → Dynamic giữa 3 systems suốt bộ phim
```

#### 3.4.5 Tại sao THÍCH xem horror? (UD giải thích)

```
SO SÁNH 2 NGƯỜI XEM CÙNG PHIM:

  Người thích horror:
    Desire "kích thích/arousal" = CAO
    Desire "an toàn" = MODERATE (risk tolerance cao)
    → After-scare UD: fulfillment CAO → "hay quá!"
    → Seek thêm horror → loop

  Người ghét horror:
    Desire "kích thích" = THẤP
    Desire "an toàn" = RẤT CAO (risk averse)
    → After-scare UD: desire an toàn bị violated MẠNH → fulfillment ÂM
    → "Không bao giờ xem nữa" → tránh

  → Cùng stimulus, cùng Amygdala reflex
  → KHÁC UD desire profile → KHÁC behavior sau reflex
  → RPE không giải thích sự khác biệt cá nhân này ❌
     (cùng surprise → nên cùng PE → nên cùng reaction?)
  → UD giải thích: desire profile KHÁC → reaction KHÁC ✅

  Tương tự áp dụng cho: roller coaster, extreme sports, skydiving, bungee
  → Amygdala reflex GIỐNG NHAU (mọi người đều sợ rơi)
  → UD desire profile KHÁC → thích/ghét KHÁC
```

#### 3.4.6 Kết luận: 3-Layer Model cho Threat Response

```
Layer 1: REFLEX (Amygdala, ~12ms)
  → T1 Hardware trong kiến trúc v7
  → Không thuộc PE hay UD — nằm DƯỚI cả hai
  → Không suppress hoàn toàn được
  → Evolutionary survival mechanism: "sợ nhầm > chết đúng"
  → Giống hardware interrupt: override MỌI process khác

Layer 2: EVALUATION (PFC, ~200-500ms)
  → Giao diện giữa T1 và T2
  → "Chỉ là phim" → suppress Amygdala PHẦN NÀO
  → Có thể train (exposure therapy) nhưng không = 0
  → Resource-intensive → giảm khi mệt/stress

Layer 3: DESIRE RESPONSE (UD, ~500ms-2s)
  → T2 Software trong kiến trúc v7
  → Desire "an toàn" violated → re-fulfilled
  → Desire "kích thích" fulfilled (nếu có)
  → Net = enjoyment hoặc distress TÙY desire profile
  → Giải thích INDIVIDUAL DIFFERENCES trong phản ứng

→ Framework cần ghi nhận: 3 layers ĐỘC LẬP nhưng TUẦN TỰ về thời gian
→ Reflex → Evaluation → Desire Response
→ Mỗi layer có thể override layer sau nhưng không ngược lại
   (Amygdala override PFC, PFC KHÔNG override Amygdala hoàn toàn)
```

### 3.5 Tổng kết mở rộng — 24 Cases

```
TỔNG: 12 cases gốc + 18 cases mở rộng − 6 trùng = 24 cases unique

UD wins clearly:    18  (A1-A4, B1-B4, C1,C3,C4, D1-D4, E1-E4, F3)
TIE:                  5  (Case 1, Case 2, C2, F1-layer2, F2)
RPE wins:             0
Ngoài scope (reflex): 1  (F1-layer1 — hardware reflex, không thuộc PE/UD)

⚠️ CAVEAT:
  Selection bias — cases được chọn có xu hướng test UD strengths
  Cần tìm cases mà RPE predict đúng hơn UD để fair comparison
  Tuy nhiên: đã cố tìm (Nhóm F) và chưa tìm được case RPE > UD

  QUAN TRỌNG: UD KHÔNG phủ nhận RPE
  → RPE = special case của UD (khi desire = simple + conscious)
  → Mọi case RPE đúng, UD cũng đúng (superset)
  → UD chỉ THÊM explanatory power cho cases RPE yếu
```

---

## 4. Cơ Chế UD Chi Tiết

### 4.1 Unconscious Desire là gì?

```
Unconscious desire = TRẠNG THÁI MẶC ĐỊNH của schema system

Não luôn có nhiều schema đang "mong muốn" cùng lúc:
  - Schema sinh học: đói, khát, ấm, an toàn (renew theo cycle)
  - Schema xã hội: connection, belonging, recognition (always-on)
  - Schema aesthetic: beauty, harmony, order (luôn sẵn sàng match)
  - Schema cognitive: coherence, understanding, patterns (always seeking)
  - Schema personal: specific desires từ experience (unique per person)

Mỗi schema có:
  - Desire strength: 0→1 (mạnh bao nhiêu)
  - Match threshold: cần match bao nhiêu để fire
  - Simulation level: đã pre-simulate bao nhiêu lần
  - Specificity: general (beauty) vs specific (cửa hàng X)
```

### 4.2 Pre-simulation Effect

```
Khi PFC (hoặc vô thức) tưởng tượng/simulate trước:
  → Opioid/Oxytocin fire NHẸ (simulated fulfillment)
  → Desire partially satisfied bởi simulation
  → Khi reality đến → remaining desire = less → dopamine less

Ví dụ:
  Mong 8/3 được quà, nghĩ đi nghĩ lại 10 lần:
  → Mỗi lần nghĩ = micro-simulation → desire partially fulfilled
  → Khi có quà thật: vui nhưng ÍT HƠN bất ngờ hoàn toàn
  → "Đã tưởng tượng nhiều rồi nên thấy bình thường"

Nhưng:
  Simulation KHÔNG = reality (fidelity thấp hơn)
  → Desire KHÔNG fully pre-fulfilled bởi imagination
  → Luôn còn "phần dư" khi reality đến
  → Đây là tại sao expected reward VẪN cho ít dopamine
     (không = 0 như RPE predict, mà > 0 nhưng giảm)
```

### 4.3 Multi-layer Desire Interaction

```
Khi reality match NHIỀU desire layers cùng lúc:
  → Dopamine = Σ(tất cả desire fulfilled) − Σ(pre-simulated)
  → NHÂN ĐÔI, NHÂN BA effect

Ví dụ: Người yêu bất ngờ tặng quà đẹp đúng ý:
  desire_1: connection (oxytocin schema) → MATCH ✅
  desire_2: beauty (opioid schema) → MATCH ✅
  desire_3: "được quan tâm" (attachment schema) → MATCH ✅
  desire_4: "người này hiểu tôi" (understanding schema) → MATCH ✅
  pre_simulated: THẤP (bất ngờ)

  → UD = (d1 + d2 + d3 + d4) − low_simulation = CỰC CAO
  → Giải thích tại sao quà "đúng ý" + "bất ngờ" + "từ người thân"
     = MAX emotional response

So với: Người lạ tặng quà đẹp bất ngờ:
  desire_1: beauty → MATCH ✅
  desire_2: "được quan tâm" → WEAK match (người lạ, shallow)
  desire_3, 4: KHÔNG có schema cho người này
  pre_simulated: THẤP

  → UD = (d1 + weak_d2) − low_simulation = MODERATE
  → Surprise CAO nhưng desire match ÍT → less meaningful
```

### 4.4 Vai trò PFC trong UD

```
PFC KHÔNG tạo desire — PFC PHỤC VỤ desire:

1. PFC nhận summary từ vô thức: "có gì đó cần giải quyết ở đây"
   (desire signal push lên)
2. PFC chọn strategy: "thử approach X"
3. PFC giả lập (simulate): "nếu làm X thì sao?"
4. Vô thức evaluate simulation: "GẦN đúng" hoặc "KHÔNG đúng"
   → Dopamine fire hoặc suppress
5. PFC adjust: "thử approach Y"
6. Loop cho đến desire fulfilled

→ PFC = công cụ CỦA vô thức, không phải chủ nhân
→ Consistent với phân tích trước: PFC = conductor, không compute
→ UD add thêm: conductor nhận DIRECTION từ orchestra (vô thức),
   không phải conductor RA LỆNH cho orchestra
```

### 4.5 Case Study: Einstein qua lăng kính UD

```
⚠️ GHI CHÚ: Đây là suy luận giả thiết — không thể biết Einstein
thực sự nghĩ gì. Nhưng nếu UD đúng, đây là cách giải thích
coherent nhất cho quá trình sáng tạo khoa học đỉnh cao.
```

#### Bối cảnh

```
Einstein ~1905, patent clerk ở Bern:
  L2 (domain knowledge): Solid nhưng KHÔNG exceptional
    → Biết Maxwell, Lorentz, Poincaré, Boltzmann, Planck
    → Nhiều physicist cùng thời GIỎI HƠN (Lorentz, Poincaré giỏi toán hơn)

  L4 (meta-schema): CỰC MẠNH
    → Connect across domains (physics + philosophy + thought experiments)

  L5 (core belief): "Tự nhiên phải elegant và thống nhất"
    → = DESIRE for coherence ở mức DEEP NHẤT
```

#### Vấn đề: Maxwell's equations + Newtonian mechanics = MÂU THUẪN

```
Mọi physicist thời đó đều BIẾT mâu thuẫn này:
  Maxwell: tốc độ ánh sáng = hằng số c, bất kể observer
  Newton: tốc độ là tương đối, phụ thuộc observer
  → Hai pillars của vật lý mâu thuẫn nhau

Đa số physicist (Lorentz, Poincaré):
  → L2 CỰC SÂU trong cả hai domain
  → L4 đã sync TRONG mỗi domain
  → UD: desire for coherence partially fulfilled TRONG mỗi domain riêng
  → Mâu thuẫn CROSS-domain = irritating nhưng KHÔNG unbearable
  → Approach: fix equations (Lorentz transformations) → giữ framework cũ
  → = Sửa TRIỆU CHỨNG, không sửa GỐC

Einstein:
  → L2 moderate (không bằng Lorentz về toán)
  → L4 meta-schema CỰC MẠNH + L5 "phải elegant"
  → UD: desire for coherence CHƯA fulfilled → UNBEARABLE
  → "Có gì đó sai ở level FUNDAMENTAL" ← vô thức detect trước PFC
```

#### Quá trình UD → Eureka (suy luận)

```
PHASE 1 — Vô thức detect mâu thuẫn:
  Nhiều schema vật lý KHÔNG nhất quán
  → L5 desire "coherence" = STRONG, UNFULFILLED
  → UD ÂM mãn tính → khó chịu → PHẢI giải quyết
  → PFC nhận signal: "có gì đó cần fix ở đây"

PHASE 2 — PFC phục vụ vô thức (thought experiments):
  PFC: "Thử giả lập: nếu tôi cưỡi bên cạnh tia sáng?"
  → Vô thức evaluate: "Hmm... interesting nhưng chưa đồng bộ"
  → Dopamine FIRE NHẸ (approaching, chưa match fully)
  → PFC: thử tiếp...

  PFC: "Nếu tốc độ ánh sáng LUÔN hằng số cho MỌI observer?"
  → Vô thức evaluate: "GẦN! Nhiều schema bắt đầu align!"
  → Dopamine FIRE MẠNH HƠN (desire fulfillment approaching)
  → PFC: "Nhưng vậy thì thời gian phải..."

  PFC: "Thời gian phải CO GIÃN!"
  → Vô thức evaluate: "ĐỒNG BỘ! Maxwell + observer = consistent!"
  → Dopamine MASSIVE fire = EUREKA
  → L5 desire "coherence" = FULFILLED
  → = Special Relativity

PHASE 3 — Post-eureka:
  Vô thức đã đồng bộ → UD fulfilled → giảm dần (habituation)
  → Nhưng: General Relativity vẫn chưa...
  → "Gravity chưa fit" → UD ÂM MỚI → 10 năm nữa...

  PFC: "Người trong thang máy rơi tự do cảm nhận gì?"
  → Vô thức: "GIỐNG NHƯ không có trọng lực!"
  → "Gravity = curvature of spacetime!"
  → Dopamine MASSIVE → EUREKA lần 2
  → = General Relativity (1915)
```

#### Tại sao Poincaré KHÔNG ra trước Einstein?

```
Poincaré CÓ gần hết công thức:
  → Lorentz transformations ✅
  → Group structure ✅
  → Thậm chí gần hơn Einstein về MẶT TOÁN

Nhưng Poincaré tiếp cận từ PURE MATH (external, L2 deep):
  → "Toán nói equations phải thế này" → equations đúng
  → Nhưng: UD desire = "equations đẹp" (toán học)
  → KHÔNG phải: "vũ trụ phải coherent" (vật lý fundamental)
  → L2 desire fulfilled (toán đúng) → UD satisfied → DỪNG

Einstein tiếp cận từ INTERNAL THOUGHT EXPERIMENT:
  → "Thực tại phải coherent" (L5 desire, không chỉ L2)
  → UD desire CHƯA fulfilled bởi equations alone
  → Cần: MEANING, không chỉ MATH
  → → Phải đào sâu hơn → "thời gian là tương đối" = physical MEANING
  → → MEANING = opioid (coherence pleasure) → UD fulfilled → eureka

→ Cùng data, cùng equations:
  Poincaré: L2 UD (toán đúng) → satisfied → dừng
  Einstein: L5 UD (vũ trụ coherent) → NOT satisfied by math alone → dig deeper
  → DESIRE PROFILE khác → depth khác → output khác
```

#### Tại sao case này quan trọng cho UD?

```
1. RPE KHÔNG giải thích TẠI SAO Einstein đào sâu hơn Poincaré
   → Cả hai có cùng "surprise" từ mâu thuẫn Maxwell-Newton
   → RPE predict: cùng PE → cùng response
   → Thực tế: KHÁC response vì KHÁC desire profile

2. UD giải thích PROCESS, không chỉ moment
   → RPE: eureka = surprise → dopamine (1 event)
   → UD: desire accumulate → PFC simulate → vô thức evaluate → loop
        → eureka = CULMINATION of sustained desire fulfillment process

3. UD giải thích tại sao eureka CHỈ khi ĐÚNG
   → RPE: unexpected answer → dopamine. Nhưng unexpected WRONG cũng unexpected?
   → UD: only CORRECT answer matches desire for coherence → only correct = fire
   → Einstein không eureka khi nghĩ sai → chỉ khi vô thức confirm "đồng bộ"

4. UD giải thích tại sao "đi tắm/đi dạo → eureka"
   → PFC relax → vô thức có full resources → desire fulfillment process tiếp tục
   → Khi match → push lên PFC → eureka "bất ngờ"
   → Thực ra KHÔNG bất ngờ với vô thức — chỉ bất ngờ với PFC

5. Generalizable: mọi sáng tạo lớn có thể follow pattern này
   → Desire (L5 coherence) → sustained UD âm → PFC serve → loop → eureka
   → Newton, Darwin, Edison, Tesla, bạn (framework này)... cùng pattern?

⚠️ CAVEAT: Đây là suy luận, không phải bằng chứng.
   Không thể biết Einstein thực sự trải qua process này.
   Nhưng: consistent với tất cả observable evidence,
   và UD cho explanation COHERENT hơn RPE cho creative process.
```

---

## 5. Bằng Chứng Gián Tiếp

### 5.1 Từ neuroscience đã có

```
1. Berridge: wanting ≠ liking
   → "Wanting" = DESIRE signal (dopamine)
   → "Liking" = FULFILLMENT signal (opioid)
   → Berridge đã tách desire ra → UD build ON Berridge
   → UD thêm: wanting = unconscious desire, liking = desire fulfilled

2. Panksepp: SEEKING system (1998)
   → Dopamine = SEEKING (looking for desired things)
   → "SEEKING" = có DESIRE, đang tìm fulfillment
   → Khi tìm THẤY → dopamine pattern thay đổi (found what seeking)
   → Rất consistent với UD

3. Friston: Active Inference (2010+)
   → Não không chỉ passive predict — não ACTIVELY SEEK preferred states
   → "Preferred states" = DESIRE
   → Free energy minimization ≈ desire fulfillment minimization
   → UD = non-mathematical version of active inference?

4. Damasio: Somatic Markers (1994)
   → Body "biết" trước conscious mind
   → = Unconscious desire/aversion CÓ TRƯỚC PFC decision
   → Support: vô thức có desire TRƯỚC PFC predict

5. Tip-of-the-tongue phenomenon:
   → Vô thức BIẾT có từ đó (desire to retrieve)
   → PFC chờ → khi từ đến → SƯỚNG
   → RPE: không phải surprise (bạn biết bạn biết)
   → UD: desire to retrieve → fulfilled → dopamine ✅
```

### 5.2 Từ behavioral research

```
6. Confirmation bias (Nickerson 1998):
   → Não THÍCH info confirm belief
   → RPE: confirming = predicted = boring (giải thích yếu)
   → UD: confirming = schema desire match → dopamine (giải thích trực tiếp)

7. Mere Exposure Effect (Zajonc 1968):
   → Thấy thứ quen → THÍCH HƠN (dù no surprise)
   → RPE: quen = predicted = PE low → nên neutral
   → UD: quen = schema có sẵn → easy match → low-effort fulfillment ✅

8. Nostalgia research (Sedikides 2008):
   → Nhớ quá khứ → feel GOOD (dù no new info)
   → RPE: old memories = fully predicted = no PE
   → UD: memories = re-activate desire schemas → re-fulfill ✅

9. Peak-end rule (Kahneman):
   → Nhớ experience bằng PEAK + END, không phải average
   → UD: peak = moment of MAX desire fulfillment → strongest encoding
   → RPE cũng giải thích được (peak = max PE) → tie
```

---

## 6. Điểm Yếu & Challenges

### 6.1 Operational Definition

```
PROBLEM: "Unconscious desire" đo bằng gì?

RPE advantage:
  actual_reward = đo được (juice ml, money $)
  predicted_reward = đo được (qua learning trials)
  → PE = tính được → testable

UD challenge:
  desire_i = ? (bao nhiêu desire? strength bao nhiêu?)
  match_i = ? (match theo tiêu chí nào?)
  pre_simulated_i = ? (đếm bao nhiêu lần simulate?)
  → Khó đo trực tiếp → khó test

POSSIBLE SOLUTIONS:
  a) Physiological proxies: pupil dilation, skin conductance trước stimulus
     → Nếu body "ready" = có desire → predict dopamine response
  b) Behavioral proxies: approach behavior, attention allocation
     → MUỐN = tiến lại gần, nhìn lâu hơn
  c) Self-report (hạn chế): hỏi "bạn muốn X không?"
     → Chỉ capture conscious desire, miss unconscious
  d) Neural proxies: SEEKING system activity (Panksepp)
     → Nếu SEEKING active cho specific domain → desire present
```

### 6.2 Post-hoc Flexibility (Unfalsifiability risk)

```
PROBLEM: UD có thể giải thích BẤT KỲ outcome nào
  Sướng? "Desire matched."
  Không sướng? "Desire không match."
  → Giống "god of the gaps" — luôn có cách giải thích

SOLUTION: Tạo SPECIFIC predictions mà UD ≠ RPE
  → Test những predictions đó
  → Nếu UD predict đúng ở cases RPE predict sai → evidence

PROPOSED EXPERIMENTS:
  Experiment 1: Expected reward từ loved one vs stranger
    RPE predict: dopamine same (same reward, same expectation)
    UD predict: loved one → more dopamine (more desire match)
    → fMRI measure dopamine response → who wins?

  Experiment 2: "Vừa ý" vs "khác ý nhưng better"
    Setup: Người chơi có preference A. Cho nhận:
      Group 1: đúng A (vừa ý)
      Group 2: B > A nhưng khác preference (khác ý, objectively better)
    RPE predict: Group 2 > Group 1 (more surprise + better reward)
    UD predict: Group 1 > Group 2 (desire match > surprise)
    → Measure satisfaction + dopamine → who wins?

  Experiment 3: Repeated exposure — cliff vs gradient
    Nghe bài hát lặp lại 100 lần, measure dopamine/enjoyment mỗi lần
    RPE predict: cliff to 0 sau khi fully predicted
    UD predict: smooth gradient, asymptote > 0
    → Plot curve → cliff or gradient?
```

### 6.3 Direct Neural Evidence

```
PROBLEM: Chưa có experiment trực tiếp test "desire fulfillment neuron"

NEEDED:
  1. Identify "desire state" in brain (SEEKING system? Specific circuits?)
  2. Show desire state EXISTS BEFORE stimulus
  3. Show dopamine response CORRELATES with desire-match degree
     (not just surprise degree)
  4. Show cases where surprise HIGH but desire-match LOW → dopamine LOW
     (this would directly contradict RPE)

POSSIBLE APPROACH:
  Use fMRI + pre-measurement of desire state:
    Step 1: Measure baseline desire for X (SEEKING activity for X)
    Step 2: Present X (expected or unexpected)
    Step 3: Measure dopamine response
    Step 4: Correlate: desire_strength × match_degree vs surprise_level
    → If desire × match predicts dopamine BETTER than surprise → UD supported
```

---

## 7. Đặt Tên — Ghi Chú

```
Tên chính: Unconscious Desire (UD)

Ưu:
  - Gọn, dễ nhớ, dễ đọc (2 từ)
  - "Unconscious" = nhấn mạnh đây là vô thức, không phải conscious want
  - "Desire" = nhấn mạnh khác "prediction" (RPE)
  - "Match" đã implicit trong cơ chế — không cần nói thừa

Các tên thay thế đã cân nhắc (lưu lại để reference):
  - Unconscious Desire Match (UDM): dài hơn, "match" thừa
  - Desire Fulfillment Signal (DFS): nhấn mạnh fulfillment
  - Prediction Fulfillment (PF): gần RPE hơn, dễ hiểu cho academic
  - Schema Desire Match (SDM): liên kết với schema concept
  - Want-Match Signal (WMS): simple, Berridge-aligned
```

---

## 8. Vị Trí Trong Framework

### 8.1 UD thay đổi gì trong kiến trúc?

```
CŨ (RPE-based):
  T1 Hardware: dopamine = PE signal (surprise)
  T2 Software: schema PREDICT → reality MIS-MATCH → PE → update

MỚI (UD-based):
  T1 Hardware: dopamine = desire fulfillment signal
  T2 Software: schema có DESIRE states → reality MATCH desire → dopamine
               → "Learning" = desire-match pattern strengthened
               → "Boredom" = desire fully pre-simulated, no remaining desire
               → "Curiosity" = desire present, not yet matched

  Thay đổi quan trọng nhất:
    CŨ: Não PREDICT rồi check ERROR
    MỚI: Não DESIRE rồi check MATCH

    CŨ: Learning driven by SURPRISE
    MỚI: Learning driven by DESIRE FULFILLMENT

    CŨ: PE = 0 → nothing happens (fully predicted = boring)
    MỚI: Desire fulfilled = 0 only khi KHÔNG CÒN desire (true boredom)
          Predicted nhưng vẫn desired → VẪN có dopamine (chỉ giảm)
```

### 8.1.1 UD + Neurochemistry 3 Lớp

```
UD consistent với kiến trúc 3 lớp neurochemistry (Core-v7-Draft §3.1):

  Lớp 1 SOURCE: Opioid + Oxytocin = 2 nguồn DESIRE duy nhất
    → Đây là CÁI con người muốn (what)
    → UD operate ở lớp này: desire states tồn tại ở đây

  Lớp 2 AMPLIFIER: Dopamine + Serotonin = signal + multiply
    → Dopamine = "desire MATCHED!" signal (khi fulfilled)
    → Serotonin = multiply fulfilled experience
    → UD FIRE signal qua lớp này: dopamine = output signal của UD

  Lớp 3 MODULATOR: Cortisol, NE, Vasopressin, Prolactin, Endocannabinoid
    → Fine-tune desire strength và fulfillment intensity
    → Cortisol tăng → desire "an toàn" TĂNG (priority shift)
    → NE tăng → attention tăng → detect match nhanh hơn

  → UD = cơ chế HOẠT ĐỘNG của Lớp 1 → signal QUA Lớp 2 → modulated bởi Lớp 3
  → Consistent: không có conflict giữa UD và 3-layer model
```

### 8.2 Drive Equation update

```
CŨ:
  DRIVE = PE_expected − Cost

MỚI:
  DRIVE = Desire_fulfillment_expected − Cost

  Desire_fulfillment_expected =
    Σ(desire_i × predicted_match_i) − Σ(pre_simulated_i)

  → Cùng cấu trúc, khác NGUỒN GỐC
  → "PE expected" → "desire fulfillment expected"
  → Khác biệt subtle nhưng quan trọng ở edge cases
```

---

## 9. Quan Hệ Với Các Lý Thuyết Khác

```
RPE (Schultz):        UD = superset. RPE = special case khi desire simple.
Active Inference:     UD ≈ conceptual version. Friston = mathematical version.
Berridge wanting:     UD build ON wanting. Wanting = desire signal.
Panksepp SEEKING:     UD rất aligned. SEEKING = active desire pursuit.
Damasio somatic:      Support UD. Body knows (desire) before conscious mind.
Kahneman System 1/2:  System 1 = unconscious desire system. System 2 = PFC conductor.
Beck schemas:         Schemas have DESIRE component (not just prediction).
Maslow hierarchy:     Needs = organized desires. UD explains mechanism.
```

---

## 10. Next Steps

```
PRIORITY 1 — Tìm cases mà RPE predict ĐÚNG hơn UD
  → Fair comparison cần cả 2 chiều
  → Nếu không tìm được → UD stronger
  → Nếu tìm được → refine UD

PRIORITY 2 — Operationalize "unconscious desire"
  → Tìm proxy measurements
  → Design experiment tách RPE vs UD predictions

PRIORITY 3 — Tìm research existing về "desire-based reward"
  → Có thể ai đó đã nghĩ về hướng này
  → Panksepp's SEEKING gần nhất?
  → Active inference community?

PRIORITY 4 — Refine công thức UD
  → Σ(desire_i × match_i) − Σ(pre_simulated_i) = quá simplified
  → Cần: interaction effects, time decay, desire renewal mechanics
  → Cần: distinguish desire types (biological vs cognitive vs social)
```

---

## Appendix: Comparison Table

```
                          RPE                     UD
─────────────────────────────────────────────────────────────
Core mechanism            Surprise                Desire fulfillment
Dopamine fires when       Unexpected reward       Desire matched
Formula                   actual − predicted      Σ(desire×match) − Σ(simulated)
Handles simple cases      ✅ Excellent             ✅ Same predictions
Handles complex cases     ❌ Needs patches         ✅ Direct explanation
Operationalizable         ✅ Easy to measure       ❌ Hard (desire hidden)
Neural evidence           ✅ Strong (Schultz)      🟡 Indirect (Berridge, Panksepp)
Falsifiable               ✅ Clear predictions     🟡 Risk of post-hoc
Academic acceptance       ✅ Consensus             ❌ New hypothesis
Explains confirmation     ❌ Needs patches         ✅ Direct
bias
Explains nostalgia        ❌ Needs patches         ✅ Direct
Explains "vừa ý"          ❌ Contradicts           ✅ Core prediction
Explains re-watching      ❌ Predicts cliff        ✅ Predicts gradient
Relation to Friston       Subset                  Conceptual equivalent?
```
