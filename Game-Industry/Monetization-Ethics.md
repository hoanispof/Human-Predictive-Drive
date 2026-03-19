# Monetization & Ethics — Kiếm Tiền Mà Không Phá Feel

> **Mục đích:** Revenue strategy cho casual game studio — ethical, sustainable.
> **Đọc trước:** Core-Principles.md (3 lớp), Analytics-Guide.md (đo impact)
> **Ai đọc:** Feel Owner, Producer, bất kỳ ai quyết định monetization
> **Nguyên tắc gốc:** Giải trí TRƯỚC, tiền SAU. Player CHỌN, không bị ÉP.

---

## 1. Monetization qua Lens Framework

```
MỌI monetization = CẮT vào player experience ở mức nào đó:

  Ads:     NGẮT Lớp 1 flow (xem quảng cáo giữa gameplay)
  IAP:     TẠO desire artificial ("bạn CẦN item này")
  Paywall: CHẶN Lớp 2 progress ("trả tiền hoặc chờ")

  → Monetization LUÔN có COST cho experience
  → Câu hỏi: KHÔNG "monetize hay không?" (phải có tiền để tồn tại)
  → Câu hỏi: "monetize THẾ NÀO cho cost TỐI THIỂU?"

  → TARGET: Revenue × Retention TỐI ĐA (không chỉ Revenue)
  → Aggressive monetization → Revenue↑ ngắn hạn, Retention↓ → crash
  → Moderate monetization → Revenue vừa + Retention giữ → sustainable
```

---

## 2. Revenue Models — Chọn Mô Hình Phù Hợp

```
MODEL A: ADS ONLY
  Revenue:   100% quảng cáo
  Ưu:        Đơn giản. Player không trả tiền → barrier thấp → install cao
  Nhược:     Ads ngắt experience. Revenue phụ thuộc volume.
  Phù hợp:  Hypercasual, session ngắn, replay nhiều
  Khi dùng:  Studio mới, game đầu tiên, chưa có IAP experience
  → Đây là starting point tốt nhất cho studio nhỏ

MODEL B: IAP ONLY
  Revenue:   100% mua trong game
  Ưu:        Không ads → experience liên tục
  Nhược:     Chỉ 2-5% player mua → cần game sâu để justify
  Phù hợp:  Midcore, progression dài, emotional investment
  Khi dùng:  Game đã chứng minh retention cao (D30 > 10%)
  → Ít phù hợp casual ban đầu — cần player base + data trước

MODEL C: HYBRID (Ads + IAP)
  Revenue:   Ads + mua trong game
  Ưu:        2 nguồn thu → ổn định. Player CHỌN: xem ads HOẶC trả tiền
  Nhược:     Phức tạp design. Risk cả 2 cùng annoying.
  Phù hợp:  Casual có progression. Studio đã có data.
  Khi dùng:  Scale phase — sau khi Model A đã hoạt động
  → Hướng phát triển cho studio khi grow

KHUYẾN NGHỊ theo giai đoạn studio:
  Solo/mới     → Model A (ads only — đơn giản, learn)
  Đang grow    → Model A → thêm IAP đơn giản (remove ads, cosmetic)
  Established  → Model C full (hybrid optimized qua data)
```

---

## 3. Ads Design — Đặt Đúng Chỗ, Đúng Lúc

### 3.1 Loại Ads

```
BANNER:
  Mô tả:    Thanh nhỏ, luôn hiện
  Revenue:   eCPM $0.5-2 (THẤP)
  Player cost: NHẸ (quen, ignore)
  Khi dùng:  Passive revenue, luôn hiện ở màn hình menu/level select
  ⚠️ Đừng che gameplay space (mobile nhỏ)

INTERSTITIAL:
  Mô tả:    Full-screen, bắt buộc xem 5-30 giây
  Revenue:   eCPM $5-15 (CAO)
  Player cost: CAO (ngắt flow, bắt chờ)
  Khi dùng:  Natural pauses ONLY (giữa levels, sau death)
  ⚠️ Quá nhiều → churn spike → revenue ngắn hạn, loss dài hạn

REWARDED VIDEO:
  Mô tả:    Full-screen, player TỰ CHỌN xem → nhận reward
  Revenue:   eCPM $10-30 (CAO NHẤT)
  Player cost: THẤP (tự nguyện + có reward)
  Khi dùng:  "Xem ad → extra life / 2x reward / continue"
  ✅ BEST practice: player chọn → experience ÍT bị damage
  ⚠️ Reward phải ĐÁNG — reward quá nhỏ → player không xem

QUA LENS FRAMEWORK:
  Banner:       Lớp 1 impact: -1 (nhẹ, quen)
  Interstitial: Lớp 1 impact: -5 (ngắt flow)
  Rewarded:     Lớp 1 impact: -2 + Lớp 2: +3 (reward) = NET +1
  → Rewarded = DUY NHẤT có thể NET POSITIVE cho experience
  → Interstitial = ALWAYS NEGATIVE → minimize + đặt đúng chỗ
```

### 3.2 Ads Placement Rules

```
✅ ĐẶT Ở (natural pause):
  → Sau hoàn thành level (player satisfied → pause tự nhiên)
  → Sau death + trước retry (player đang decide)
  → Main menu / level select (chưa engage gameplay)
  → "Continue?" screen (watch ad = continue, skip = restart)

❌ KHÔNG ĐẶT Ở:
  → Giữa gameplay/combat (ngắt Lớp 1 flow → rage)
  → Popup bất ngờ (cortisol spike → mất trust)
  → Che gameplay area (misclick → frustration)
  → Ngay sau tutorial (chưa hook → ad = goodbye)

SESSION ĐẦU TIÊN — ĐẶC BIỆT:
  → Session 1: ÍT ADS hoặc KHÔNG ads
  → Session 1 = feel test → ads ngắt → churn → KHÔNG BAO GIỜ quay lại
  → Player quay lại D2+ → đã hook → chịu ads hơn
  → "Session đầu = free trial. Show value TRƯỚC, monetize SAU."

FREQUENCY — tìm sweet spot bằng ABTest:
  Variant A: interstitial mỗi level → đo revenue × D7
  Variant B: interstitial mỗi 2 levels → đo revenue × D7
  Variant C: interstitial mỗi 3 levels → đo revenue × D7
  → Chọn: variant có (revenue × D7 retention) CAO NHẤT
  → KHÔNG chỉ chọn revenue cao nhất!

  Rule of thumb (trước ABTest):
    Interstitial: mỗi 2-3 levels
    Rewarded: mỗi cơ hội (player tự chọn → càng nhiều option càng tốt)
    Banner: test on/off → keep nếu revenue đáng kể + impact nhỏ
```

---

## 4. IAP Design — Ethical

### 4.1 Loại IAP

```
COSMETIC (skin, theme, visual effect):
  Ảnh hưởng gameplay: KHÔNG
  Player mua vì: THÍCH, không vì CẦN
  Ethical: ✅ (không exploit, không pay-to-win)
  Revenue: MODERATE (chỉ player care visual mới mua)
  Ví dụ casual: skin nhân vật, color theme, trail effect, celebration anim
  → Casual art ĐƠN GIẢN → cosmetic cũng đơn giản → ít effort tạo

CONVENIENCE (extra lives, 2x reward, skip wait):
  Ảnh hưởng gameplay: GIÁN TIẾP (save time, not give power)
  Player mua vì: muốn NHANH HƠN
  Ethical: ✅ NẾU free path vẫn playable
  Revenue: CAO (ai cũng muốn skip wait)
  ⚠️ Test: player KHÔNG mua → VẪN enjoy? → YES = ethical. NO = exploitative.
  → Ranh giới mỏng: "convenience" → "forced wait" = dark pattern

POWER (stronger weapon, skip level):
  Ảnh hưởng gameplay: TRỰC TIẾP
  Ethical: ❌ cho competitive. 🟡 cho single-player.
  Revenue: CAO nhưng RISK (phá mastery feel = Lớp 2 hollow)
  → Player không GIỎI LÊN → MUA lên → "thắng nhưng không sướng"
  → ⚠️ TRÁNH cho casual game → phá core feel loop

REMOVE ADS (one-time purchase):
  = Player trả 1 lần → không còn interstitial ads
  Ethical: ✅✅ (win-win: player happy + studio revenue)
  Revenue: 1 lần, nhưng 2-5% conversion cho casual
  Pricing: phải > estimated ad LTV per user
  → Ví dụ: player avg xem 200 ads ($2 LTV) → remove ads > $2
  → Suggest: $2.99-4.99 (cover LTV + margin)
```

### 4.2 IAP Strategy cho Casual

```
SIMPLE START (Model A → thêm IAP):

  Bước 1: Remove Ads ($2.99-4.99)
    → Đơn giản nhất, ethical nhất, nhiều player muốn
    → 1 nút ở settings + popup nhẹ sau 3-5 sessions
    → KHÔNG popup session đầu

  Bước 2: Cosmetic Pack ($0.99-2.99)
    → 3-5 packs với theme khác nhau
    → Preview: player THẤY trước khi mua
    → → Player mua vì "đẹp!" không vì "cần"

  Bước 3: Convenience ($0.99-1.99)
    → Extra continues (3 continues = $0.99)
    → 2x coins cho 24h ($0.99)
    → ⚠️ CHỈ thêm nếu game có progression system
    → ⚠️ Free path VẪN phải enjoyable

  Bước 4 (advanced): Premium Pass ($1.99-4.99/tháng)
    → No ads + exclusive cosmetic + bonus rewards
    → Recurring revenue → stable
    → CHỈ khi D30 retention > 10% (player ở đủ lâu để justify)

PRICING PSYCHOLOGY:
  → $0.99: impulse buy threshold (nhiều người mua không nghĩ)
  → $2.99: "cheap but not throwaway" (perceived value)
  → $4.99: "considered purchase" (player nghĩ 1 chút)
  → > $4.99: HIGH bar cho casual (ít người mua)
  → → Casual IAP sweet spot: $0.99-4.99
  → → Nhiều item rẻ > ít item đắt (volume > margin cho casual)
```

### 4.3 IAP Timing — Khi nào show

```
⚠️ KHI NÀO show IAP = quan trọng hơn IAP GÌ

ĐỪNG show:
  → Session 1 (chưa hook → pushy → churn)
  → Giữa gameplay (ngắt flow)
  → Ngay sau fail (đang frustrate → "game bắt trả tiền!")
  → Quá thường xuyên (mỗi level → "spam!")

NÊN show:
  → Sau natural desire moment:
    "Player vừa thấy skin cool trên enemy → hiện skin shop"
    "Player vừa chết lần 3 ở boss → hiện continue option (rewarded ad or IAP)"
    "Player chơi 5+ sessions → hiện remove ads suggestion"
  → Ở DEDICATED SHOP (player TỰ mở khi muốn)
    → Shop button ở menu → player CHỌN vào → browse → mua nếu muốn
    → KHÔNG force vào shop

SOFT PROMPT vs HARD PROMPT:
  Soft: nhỏ, dismiss dễ, 1 tap close → "hey, có cái này nếu muốn"
  Hard: full screen, khó dismiss, multiple taps close → "MUA ĐI!"
  → Casual: SOFT ONLY. Hard = churn trigger.
  → Rule: DISMISS phải dễ hơn PURCHASE (1 tap close, 2 tap buy)
```

---

## 5. Dark Patterns — TRÁNH

```
❌ FOMO (Fear Of Missing Out):
  "Mua NGAY! Còn 2 giờ!"
  → Tạo cortisol → player mua vì SỢ, không vì MUỐN
  → Short-term: revenue ↑. Long-term: trust ↓ → churn ↑

❌ PAY-TO-SKIP-FRUSTRATION:
  Game CỐ Ý khó → player stuck → "mua để qua!"
  → TẠO frustration rồi BÁN solution
  → Player BIẾT → mất trust → 1-star review

❌ GACHA / LOOT BOX:
  "Mở hộp ngẫu nhiên! Có thể ra legendary!"
  → Slot machine psychology → Lớp 2 hijack → addiction
  → Nhiều nước đang BAN/REGULATE (Bỉ, Hà Lan, nhiều nước xem xét)
  → → TRÁNH cho ethical + legal reasons

❌ ENERGY/STAMINA SYSTEM:
  "Hết năng lượng! Chờ 4 giờ hoặc MUA"
  → CHẶN play time rồi BÁN quyền chơi
  → → Anti-player → brand damage dài hạn

❌ MISLEADING UI:
  → Nút X nhỏ xíu → misclick → mở ad/store
  → "Free" nhưng cần mua currency
  → "Sale 80%!" không hiện giá gốc
  → → Trick player → mất trust → legal risk

❌ TARGETING VULNERABLE:
  → Trẻ em: không biết giá trị tiền
  → Người dễ nghiện: gacha trigger gambling
  → → Legal risk + Ethical risk → TRÁNH HOÀN TOÀN
```

---

## 6. Ethical Principles — 5 Nguyên Tắc

```
1. GIẢI TRÍ TRƯỚC, TIỀN SAU
   → Game vui MIỄN PHÍ → player enjoy → SAU ĐÓ monetize
   → Nếu game không vui free → monetization = bán sản phẩm tệ
   → "Kiếm tiền vì player THÍCH" ≠ "kiếm tiền vì player BỊ TRAP"

2. PLAYER CHỌN, KHÔNG BỊ ÉP
   → Rewarded ad: player CHỌN → ✅
   → Forced interstitial: player BỊ BẮT → minimize
   → IAP: mua vì MUỐN → test: bỏ IAP → game vẫn vui?

3. FAIR EXCHANGE
   → Player trả $X → biết CHÍNH XÁC nhận GÌ
   → $2.99 remove ads → player biết → fair ✅
   → $2.99 random loot box → player không biết → unfair ❌

4. KHÔNG PHÁ FEEL
   → Mọi monetization → test: "feel CÒN sướng?"
   → Revenue PHẢI serve sustainability → sustainability CẦN feel tốt
   → Short-term revenue hại feel = long-term revenue GIẢM

5. REVENUE × RETENTION, KHÔNG CHỈ REVENUE
   → Optimize: (daily revenue) × (D30 retention) × (LTV)
   → KHÔNG: chỉ optimize daily revenue
   → Aggressive → revenue today ↑, revenue next month ↓
   → Moderate → revenue today ok, revenue next month OK → sustainable
```

---

## 7. Revenue Strategy Theo Giai Đoạn Studio

```
GIAI ĐOẠN 1: Solo/Nhỏ (1-5 người, 1-2 game)
  Model:   Ads only
  Focus:   Feel + Retention TRƯỚC → ads revenue TỰ có
  Ads:     Interstitial mỗi 2-3 levels + Rewarded available
  IAP:     Chưa cần (complexity overhead)
  Target:  $500-2000/tháng/game → đủ chi phí + reinvest
  Learn:   Ads frequency ABTest, placement optimization

GIAI ĐOẠN 2: Small Studio (5-10 người, 3-5 game)
  Model:   Hybrid nhẹ (Ads + Remove Ads IAP + Cosmetic)
  Focus:   Optimize ads + simple IAP
  Ads:     ABTest optimized frequency + rewarded
  IAP:     Remove Ads ($2.99-4.99) + 2-3 cosmetic packs ($0.99-1.99)
  Target:  $2000-10000/tháng/game
  Learn:   IAP conversion, pricing, timing

GIAI ĐOẠN 3: Medium Studio (10-20 người, 5-10 game)
  Model:   Hybrid full (Ads + IAP + possible Subscription)
  Focus:   Analytics-driven optimization, segmented monetization
  Ads:     Fully optimized (placement, frequency, network mediation)
  IAP:     Full stack (remove ads + cosmetic + convenience + premium pass)
  Target:  $20000-100000/tháng total studio
  Learn:   LTV modeling, UA ROI, cross-promotion

GIAI ĐOẠN 4: Established (20-50 người, 10+ game)
  Model:   Portfolio optimization
  Focus:   LTV/CPI ratio per game, portfolio balance
  New:     Cross-promotion giữa games (free UA)
           Dedicated monetization analyst
           Per-country optimization
  Target:  Sustainable growth, team salary + reinvest covered
```

---

## 8. Checklist

```
ADS CHECKLIST:
  □ Session 1: no interstitial ads (hoặc rất ít)
  □ Interstitial: chỉ ở natural pauses (giữa levels, sau death)
  □ Rewarded video: available ở mọi opportunity hợp lý
  □ Frequency ABTest: đã test 2-3 variants → chọn optimal
  □ Ads-retention correlation: đã đo → revenue × retention optimized
  □ Dismiss dễ: 1 tap close cho mọi popup

IAP CHECKLIST:
  □ Remove Ads option: available (nếu có interstitial)
  □ IAP transparent: player biết mua GÌ trước khi trả tiền
  □ Free path playable: game ENJOYABLE 100% free
  □ No dark patterns: không FOMO, không pay-to-skip-frustration
  □ Pricing: $0.99-4.99 range cho casual
  □ Timing: không session 1, không giữa gameplay
  □ Soft prompt: dismiss dễ hơn purchase

ETHICAL CHECKLIST:
  □ "Game vui free?" → YES (monetization = bonus, không bắt buộc)
  □ "Player mua vì MUỐN?" → YES (không vì bị ép hoặc sợ)
  □ "Revenue × Retention tối ưu?" → YES (không sacrifice retention cho revenue)
  □ "Trẻ em safe?" → YES (không IAP predatory, no gambling mechanics)
  □ "Bạn TỰ thấy OK với monetization này?" → YES (moral compass check)
```

---

## 9. Quick Decision Guide

```
"Nên thêm ads ở X?"
  → X là natural pause? → YES → test, monitor retention
  → X là trong gameplay? → NO

"Nên thêm IAP Y?"
  → Player mua vì MUỐN hay vì BỊ BẮT? → MUỐN → ok. BẮT → no.
  → Game vẫn vui không mua? → YES → ok. NO → redesign.

"Nên tăng ad frequency?"
  → ABTest: revenue × D7 retention → variant NÀO win?
  → Revenue tăng 20% nhưng D7 giảm 30% → NET LOSS → đừng

"Nên thêm loot box / gacha?"
  → NO. Legal risk + ethical risk + brand damage.
  → Bán CHÍNH XÁC cái player muốn → fair, transparent, sustainable.

"Nên thêm energy system?"
  → NO cho casual (chặn play = chặn fun = churn).
  → Exception: nếu game CÓ natural session limit khác → consider carefully.

"Revenue đang thấp, làm sao?"
  → Check: feel tốt? retention tốt? → YES → optimize monetization
  → Feel tệ? retention tệ? → FIX GAME trước, monetization không cứu game tệ
```

---

> *Monetization & Ethics — Kiếm Tiền Mà Không Phá Feel*
> *Giải trí trước, tiền sau. Player chọn, không bị ép.*
> *Revenue × Retention, không chỉ Revenue.*
> *Fair exchange. Transparent pricing. No dark patterns.*
