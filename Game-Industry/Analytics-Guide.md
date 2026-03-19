# Analytics Guide — Hỏi Đúng Câu, Đo Đúng Thứ

> **Mục đích:** Data-driven decisions cho casual game studio.
> **Đọc trước:** Core-Principles.md (3 lớp reward), Team-Workflow.md (lifecycle)
> **Ai đọc:** Feel Owner, Producer, bất kỳ ai dùng data quyết định
> **Nguyên tắc:** Data PHỤC VỤ feel decisions. Data ≠ truth — data = clue.

---

## 1. Analytics = Hỏi Đúng Câu Hỏi

```
Sai: "Collect nhiều data → insight tự đến"
Đúng: "Hỏi đúng câu → collect data ĐỦ → insight RÕ"

3 câu hỏi GỐC (theo thứ tự ưu tiên):

  1. "Game có SƯỚNG không?"      → FEEL analytics (Lớp 1)
  2. "Player có QUAY LẠI không?" → RETENTION analytics
  3. "Game có TIỀN không?"       → REVENUE analytics

Thứ tự quan trọng: FEEL → RETENTION → REVENUE
  Feel tốt → Retention tốt → Revenue tốt (thường)
  Feel tệ → Retention tệ → Revenue tệ (luôn)
  Revenue tốt mà feel tệ → SHORT-TERM → sẽ crash

⚠️ Data KHÔNG thay thế CHƠI game:
  → Data nói "level 5 churn cao" → KHÔNG nói TẠI SAO
  → CHƠI level 5 → body CẢM tại sao → data CONFIRM body feeling
  → → Data = verification, không phải discovery
  → → Discovery = CHƠI game + feel → Data = confirm/reject
```

---

## 2. Feel Analytics — "Game Có Sướng Không?"

> Khó đo nhất nhưng quan trọng nhất. Player KHÔNG NÓI "feel tốt" → phải SUY RA từ behavior.

### 2.1 Session Engagement Quality

```
METRIC: RETRY RATE
  = Player fail → chơi lại NGAY vs quit

  Công thức: retry_rate = retry_count / (retry_count + quit_after_fail)

  > 60%: ✅ Feel + difficulty OK ("gần được! thử lại!")
  30-60%: 🟡 Cần tune (difficulty hoặc feel)
  < 30%: ❌ Feel HOẶC difficulty có vấn đề nghiêm trọng

  Đo per level → level nào retry thấp = level đó cần fix
  Đo per difficulty variant (ABTest) → variant nào retry cao = difficulty đúng

METRIC: SESSION LENGTH DISTRIBUTION
  ⚠️ KHÔNG dùng average (misleading)
  → DÙNG distribution (histogram):

  Example phân tích:
    Nhiều người < 2 phút = first impression FAIL (feel chưa hook)
    Peak ở 5-15 phút = HEALTHY casual session
    Tail > 30 phút = ENGAGED players (hoặc addictive → monitor)

    BIMODAL (2 đỉnh): Love-it-or-hate-it = feel INCONSISTENT
    → Game bạn (music): coherence "perfect hoặc off" = bimodal quality
    → Fix: giảm variance → move từ bimodal → unimodal

METRIC: VOLUNTARY REPLAY
  = Player ĐÃ CLEAR level → chơi LẠI (không vì progress, chỉ vì FEEL)

  voluntary_replay_rate = replay_cleared / total_cleared per level

  > 20%: ✅ Level này feel CỰC TỐT → study TẠI SAO → apply cho level khác
  5-20%: Normal
  < 5%: Level ok nhưng không memorable → feel "đủ" nhưng không "wow"

  → ĐÂY LÀ STRONGEST feel signal → level có replay cao = TEMPLATE cho design
```

### 2.2 Fail & Frustration Patterns

```
METRIC: RAGE QUIT DETECTION
  = Session end NGAY SAU death streak (< 10 giây sau death)

  Pattern: play → die → die → die → QUIT (< 10s sau death cuối)
  → = Frustration → difficulty quá cao HOẶC feel unfair

  rage_quit_rate per level → level nào cao = cần tune

METRIC: FIRST-SESSION DEPTH
  = Player ĐẦU TIÊN đi tới level bao nhiêu?

  Depth cao: onboarding tốt + feel hook NGAY
  Depth thấp: chưa hook (feel chưa đúng hoặc teach sai)

  Target casual: session đầu reach level 3-5 = healthy
  Session đầu quit level 1 = CRITICAL → feel hoặc onboarding FAIL

METRIC: LEVEL COMPLETION TIME VARIANCE
  = Cùng level, player khác nhau mất bao lâu?

  Variance THẤP: difficulty well-tuned → feel CONSISTENT
  Variance CAO: difficulty INCONSISTENT → some players struggle, some breeze
  → Nếu variance cao → xem lại design: skill floor / skill ceiling
```

### 2.3 ABTest cho Feel

```
Bạn ĐÃ CÓ: ABTest speed variants → đo session time

MỞ RỘNG — systematic feel ABTest:

TEST 1: HITSTOP DURATION
  Variants: 0 frame / 2 frame / 4 frame / 6 frame
  Metric: retry rate + session length
  Expected: sweet spot ở 2-4 frame (hơn/kém = feel giảm)
  Sample: 1000+ users per variant, 5+ ngày

TEST 2: SCREEN SHAKE INTENSITY
  Variants: none / light / medium / heavy
  Metric: session length + voluntary replay
  Expected: medium sweet spot
  Note: offer toggle cho motion-sensitive players

TEST 3: SFX IMPACT
  Variants: no SFX / placeholder / polished
  Metric: session length + D1 retention
  Expected: polished >> placeholder > none
  → Quantify: audio contribute bao nhiêu % retention?

TEST 4: DIFFICULTY CURVE
  Variants: steep / gradual / flat
  Metric: level completion rate + rage quit per level + D7 retention
  Expected: gradual > flat > steep

TEST 5: AD FREQUENCY
  Variants: every level / every 2 levels / every 3 levels
  Metric: revenue per user × retention D7
  Expected: less ads = better retention, worse revenue → find SWEET SPOT
  ⚠️ ALWAYS measure retention ALONGSIDE revenue

ABTEST RULES:
  1. 1 variable tại 1 thời điểm (không mix → không biết cause)
  2. Sample: > 1000 users per variant (< 500 = noise)
  3. Duration: > 5 ngày (< 3 = weekday/weekend bias)
  4. Side effects: test X → đo impact lên Y (test ads → đo retention)
  5. Significance: > 10% difference AND > 1000 users → mới tin
     (Nếu biết stats: p < 0.05. Nếu không: conservative = > 10% + > 1000)
```

---

## 3. Retention Analytics — "Player Có Quay Lại Không?"

### 3.1 Retention Cohort

```
METRIC: D1 / D7 / D30 RETENTION

  D1:  % player quay lại sau 1 ngày
  D7:  % player quay lại sau 7 ngày
  D30: % player quay lại sau 30 ngày

  Target casual mobile:
    D1: > 40% (tốt), > 50% (rất tốt)
    D7: > 15% (tốt), > 25% (rất tốt)
    D30: > 5% (tốt), > 10% (rất tốt)

  COHORT: Group player theo NGÀY INSTALL → track per cohort
    ⚠️ KHÔNG mix player cũ + mới → misleading
    Week 1 cohort: 1000 installs → D1 = 420 → 42% ✅
    Week 2 cohort: 800 installs → D1 = 280 → 35% → cái gì thay đổi?

  Qua framework:
    D1 ↔ Lớp 1 (feel hook ngay session đầu?)
    D7 ↔ Lớp 2 (progression đáng quay lại?)
    D30 ↔ Lớp 3 (meaning/social giữ lâu dài?)

    D1 thấp → fix FEEL (Lớp 1)
    D7 thấp, D1 ok → fix PROGRESSION (Lớp 2: content, unlocks, mastery)
    D30 thấp, D7 ok → fix ENGAGEMENT (Lớp 3: social, live ops, events)
```

### 3.2 Churn Points

```
METRIC: CHURN BY LEVEL
  = Level nào có DROP-OFF cao nhất?

  Funnel: Install → L1 → L2 → L3 → L4 → L5 → ... → LN
  Mỗi bước: bao nhiêu % DROP?
  Drop > 30% ở 1 level = BOTTLENECK → fix level đó

  Ví dụ:
    L1 → L2: 90% pass ✅
    L2 → L3: 85% pass ✅
    L3 → L4: 55% pass ❌ ← BOTTLENECK → L3 quá khó? feel thay đổi? boring?
    L4 → L5: 80% pass ✅ (của những người đã qua L3)
    → Fix L3 → toàn bộ funnel IMPROVE

METRIC: CHURN BY MINUTE
  = Player bỏ ở PHÚT thứ mấy trong session?

  0-1 phút:   First impression fail (feel hoặc loading quá lâu)
  1-3 phút:   Onboarding fail (không hiểu cách chơi)
  3-5 phút:   Hook fail (hiểu nhưng không thấy hấp dẫn)
  5-15 phút:  Natural endpoint (ok cho casual)
  15-30 phút: Extended session (engaged)
  > 30 phút:  Potential concern nếu kèm low satisfaction signal

METRIC: CHURN BY EVENT
  = Player bỏ SAU event nào?

  Churn spike sau ad → ads quá aggressive → giảm frequency
  Churn spike sau difficulty jump → difficulty curve sai → smooth out
  Churn spike sau IAP popup → monetization quá pushy → soften
  → Event-based churn = DIRECT actionable insight
```

### 3.3 Engagement Depth

```
METRIC: LEVELS PLAYED
  = Trung bình player chơi bao nhiêu levels?
  → Game có 50 levels, average = 8 → 84% content CHƯA THẤY
  → Insight: content sau level 8 có thể không cần polish nhiều (ít người thấy)
  → Hoặc: fix retention → player đi sâu hơn → content SAU CÓ GIÁ TRỊ

METRIC: SESSION FREQUENCY
  = Bao nhiêu sessions/tuần?

  1-2/tuần: casual bình thường
  3-4/tuần: regular player (valuable)
  5+/tuần:  hardcore fan (CỰC valuable — nurture)
  < 1/tuần: dần drop → cần re-engagement (push notification? event?)

METRIC: FEATURES USED
  = % player dùng feature X?
  < 10% dùng → feature CÓ CẦN? → có thể cắt → save dev time
  > 50% dùng → feature QUAN TRỌNG → invest thêm
  → Quy tắc: nếu remove feature mà < 10% miss → CẮT
```

---

## 4. Revenue Analytics — "Game Có Tiền Không?"

### 4.1 Ad Metrics

```
METRIC: eCPM (effective Cost Per Mille)
  = Revenue per 1000 ad impressions
  → Thay đổi theo: quốc gia, ad network, ad type, time of year
  → Track per ad type: banner vs interstitial vs rewarded video
  → Rewarded video thường eCPM CAO NHẤT + retention impact THẤP NHẤT

METRIC: ADS PER SESSION
  = Trung bình bao nhiêu ads player thấy per session
  → Track: ads_shown vs ads_completed
  → ads_shown cao nhưng ads_completed thấp → player dismiss → annoying

METRIC: ADS-RETENTION CORRELATION
  ★ CRITICAL ★
  → Test: tăng ad frequency → retention thay đổi thế nào?
  → Find: sweet spot (max revenue × min retention loss)
  → ⚠️ Nhiều studio optimize ADS → ignore RETENTION → short-term gain → crash

  Ví dụ ABTest:
    Variant A: ad mỗi level → revenue $X, D7 = 12%
    Variant B: ad mỗi 2 levels → revenue $0.7X, D7 = 18%
    → B có thể BETTER: 0.7X revenue × 1.5 retention = MORE lifetime revenue
    → → PHẢI tính LTV, không chỉ daily revenue
```

### 4.2 Unit Economics

```
METRIC: CPI (Cost Per Install)
  = Chi phí quảng cáo để có 1 install
  → Casual game target: $0.10 - $0.50 (tùy quốc gia, genre)
  → CPI > $0.50 cho casual → KHÓ profitable (trừ khi LTV rất cao)

METRIC: LTV (Lifetime Value)
  = Tổng revenue 1 player tạo ra trong suốt thời gian chơi
  → LTV = revenue_per_day × average_lifetime
  → Estimate: D7_retention × revenue_per_DAU × 7 / D7_rate (rough)

METRIC: ROI
  = LTV / CPI
  → ROI > 1: profitable ✅
  → ROI < 1: losing money ❌
  → ROI > 1.5: scale UA (mua thêm users) ✅✅

METRIC: PAYBACK PERIOD
  = Bao lâu để recover CPI?
  → Target casual: < 30 ngày
  → > 60 ngày: risky (cash flow problem cho studio nhỏ)
```

---

## 5. ABTest Framework — Systematic

### 5.1 Khi nào ABTest

```
PHASE 1 (Feel Prototype):  KHÔNG test users — test NỘI BỘ (3-5 người)
PHASE 2 (Content Proto):   BẮT ĐẦU ABTest feel parameters
PHASE 3 (Production):      ABTest content + difficulty + monetization
PHASE 4 (Live):            ABTest everything ongoing

⚠️ KHÔNG ABTest khi < 1000 DAU → sample quá nhỏ → noise > signal
```

### 5.2 ABTest Workflow

```
BƯỚC 1: HYPOTHESIS
  "Tôi nghĩ [thay đổi X] sẽ [improve metric Y] vì [lý do Z]"
  Ví dụ: "Giảm ad frequency từ mỗi level → mỗi 2 levels
          sẽ tăng D7 retention vì player ít bị interrupt"

BƯỚC 2: SETUP
  → Chọn variants (control + 1-2 test variants)
  → Chọn metric CHÍNH (1 metric primary, 2-3 secondary)
  → Random assign users vào variants (50/50 hoặc 33/33/33)
  → Estimate sample size (target: > 1000 per variant)

BƯỚC 3: RUN
  → Duration: 5-14 ngày (tùy metric cần bao lâu observe)
  → KHÔNG peek sớm → KHÔNG stop sớm → let it run
  → ⚠️ Peek sớm + stop khi "thấy winning" = statistical error phổ biến

BƯỚC 4: ANALYZE
  → Primary metric: variant nào WIN?
  → Difference > 10% AND sample > 1000? → LIKELY real
  → Secondary metrics: side effects?
  → ⚠️ Revenue tăng nhưng retention giảm → NET có tốt hơn?

BƯỚC 5: DECIDE
  → Clear winner → apply cho tất cả users
  → No clear winner → inconclusive → test khác hoặc accept current
  → Winner nhưng side effects xấu → weigh trade-off
  → DOCUMENT: ghi kết quả → studio knowledge base → tránh re-test
```

---

## 6. Data Architecture — Cần Gì

### 6.1 Event Taxonomy (đặt tên CHUẨN)

```
Mọi game trong studio DÙNG CÙNG event schema:

SESSION EVENTS:
  session_start     {user_id, timestamp, device, os, version, country}
  session_end       {user_id, timestamp, duration, levels_played}

GAMEPLAY EVENTS:
  level_start       {user_id, level_id, timestamp, variant}
  level_complete    {user_id, level_id, timestamp, duration, score, deaths}
  level_fail        {user_id, level_id, timestamp, death_reason, attempt_number}
  level_retry       {user_id, level_id, timestamp, attempt_number}
  level_quit        {user_id, level_id, timestamp, after_fail: bool}

MONETIZATION EVENTS:
  ad_shown          {user_id, ad_type, placement, timestamp}
  ad_completed      {user_id, ad_type, placement, timestamp, revenue}
  ad_dismissed      {user_id, ad_type, placement, timestamp}
  iap_shown         {user_id, item_id, price, timestamp}
  iap_purchased     {user_id, item_id, price, timestamp}

ABTEST EVENTS:
  variant_assigned  {user_id, test_id, variant_id, timestamp}

USER PROPERTIES (1 lần hoặc update):
  install_date, country, device, os_version, ab_variants{}

→ Chuẩn hóa TRƯỚC khi build → mọi game CÙNG format → compare across games
→ Mỗi game CÓ THỂ thêm custom events → nhưng core events GIỐNG NHAU
```

### 6.2 Dashboard (cần thấy gì hàng ngày)

```
Không cần fancy tool — Google Sheets + script ĐỦ cho casual studio:

DAILY GLANCE (1 page):
  → DAU (daily active users) — trend
  → New installs — trend
  → D1 retention (yesterday's cohort)
  → Revenue (today) — trend
  → Session length median — trend
  → ⚠️ Anomaly alert: metric drop > 20% vs 7-day avg → investigate

WEEKLY REVIEW (1 page):
  → D1/D7 retention by cohort
  → Churn funnel (level drop-off)
  → ABTest status (running tests, results)
  → Revenue breakdown (ads, IAP, by country)

MONTHLY DEEP DIVE:
  → D30 retention
  → LTV estimate
  → User segments: hardcore / regular / casual / churned
  → Content analysis: which levels have best engagement?
  → Feature usage: what's used, what's ignored?
```

### 6.3 Tools

```
DATA COLLECTION:
  → Firebase Analytics (free, Google) — event logging + basic dashboards
  → GameAnalytics (free tier) — game-specific metrics
  → Custom backend (bạn đã có) — raw logs + custom analysis
  → → Custom = POWERFUL nhưng cần maintain
  → → Firebase/GA = easy setup nhưng less flexible

ANALYSIS:
  → Google Sheets/Excel: pivot tables, charts (đủ cho casual)
  → Python/Jupyter: phân tích sâu hơn (nếu biết code — bạn biết)
  → Metabase (free, self-host): dashboard từ database

ABTEST:
  → Custom (bạn đã có): variant assignment + metric collection
  → Firebase Remote Config: ABTest built-in (free)
  → → Custom cho control, Firebase cho convenience

⚠️ ĐỪNG:
  → Amplitude/Mixpanel (expensive cho casual studio nhỏ)
  → Custom data warehouse (overkill — Google Sheets đủ)
  → Real-time dashboard (casual không cần real-time — daily đủ)
```

---

## 7. Common Mistakes

```
❌ "Data nói nên làm X"
   → Data KHÔNG nói nên làm gì → data nói ĐÃ XẢY RA gì
   → "Level 5 churn cao" ≠ "xóa level 5" → có thể = "fix level 5"
   → CHƠI game + FEEL → rồi dùng data CONFIRM

❌ "Average là đủ"
   → Average session 10 phút → nghe ok
   → Thực tế: 50% chơi 1 phút + 50% chơi 19 phút = avg 10
   → → DISTRIBUTION > AVERAGE. Luôn nhìn histogram.

❌ "ABTest 2 ngày, có kết quả rồi"
   → 2 ngày: weekday bias, sample nhỏ, noise > signal
   → → Minimum 5 ngày, >1000 users per variant

❌ "Revenue tăng = thành công"
   → Revenue tăng + retention giảm = BORROWING from future
   → → ALWAYS measure retention alongside revenue

❌ "Collect mọi thứ, phân tích sau"
   → 100 events mà không biết hỏi gì = noise
   → → 10 events ĐÚNG + câu hỏi RÕ > 100 events random

❌ "Data replace intuition"
   → Data verify intuition, không replace
   → Feel Owner CẢM "level này off" → data CONFIRM "level này churn cao"
   → Không có feel → data meaningless (biết churn cao nhưng KHÔNG BIẾT fix thế nào)
   → → Feel-first, data-verified

❌ "Tối ưu 1 metric"
   → Tối ưu session length → game thành addictive → ethical issue
   → Tối ưu revenue → game thành exploitative → player churn long-term
   → → BALANCE metrics: feel + retention + revenue CÙNG LÚC
```

---

## 8. Analytics Per Phase (khi nào đo gì)

```
PHASE 1 (Feel Prototype):
  → KHÔNG cần analytics — 3-5 người test NỘI BỘ
  → "Cười không?" > "Metric bao nhiêu?"

PHASE 2 (Content Prototype):
  → BẮT ĐẦU log events
  → Metrics: session length, first-session depth, retry rate
  → ABTest: feel parameters (nếu đủ traffic)
  → CPI test (mobile): thử ads → cost per install?

PHASE 3 (Production):
  → Full analytics
  → Metrics: D1/D7, churn funnel, level completion
  → ABTest: difficulty, content, ads placement
  → Soft launch: real metrics → go/kill decision

PHASE 4 (Live):
  → Ongoing monitoring
  → ABTest: everything continuously
  → Segments: identify player types → optimize per segment
  → Revenue: LTV, ROI, payback → scale decisions
```

---

> *Analytics Guide — Hỏi Đúng Câu, Đo Đúng Thứ*
> *Feel-first, data-verified. Distribution > average. Retention alongside revenue.*
> *Data = clue, không phải truth. CHƠI game → CẢM → data CONFIRM.*
