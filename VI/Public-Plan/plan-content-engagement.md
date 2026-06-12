# Plan: Content Engagement — Tiếp Cận Chuyên Gia Qua Nội Dung Của Họ

> **Mục tiêu:** Tiếp cận chuyên gia + audience ĐÚNG TARGET bằng cách tham gia thảo luận
> trên chính nền tảng nội dung CỦA HỌ (YouTube, blog, podcast, newsletter).
> **Nguyên tắc:** Cho giá trị TRƯỚC (phân tích có chiều sâu), link framework SAU.
> Comment = hook ngắn. Phân tích sâu = ở nơi khác (GitHub Discussions, blog).
> **Logic cốt lõi:** Framework đúng → phân tích hay → comment tự lên top → reach tự nhiên.
> Framework sai → phân tích yếu → comment chìm → ĐÚNG behavior.
> **Trạng thái:** DRAFT v0.1
> **Ngày tạo:** 2026-05-25
> **Bổ sung cho:**
>   plan-public.md — general strategy, framing rules (W.4, W.5)
>   plan-overview-distribution.md — platform-based distribution (Reddit, HN, LW, etc.)
>   expert-verification-map.md — 20 nhóm chuyên gia, routing table
>   framing-engagement-value.md — 3-tầng giá trị, anti-patterns

---

## §0 — CORE STRATEGY: BỔ SUNG, KHÔNG SỬA

### 0.1 — Ý Tưởng Cốt Lõi

```
CHIẾN LƯỢC HIỆN TẠI (plan-overview-distribution.md):
  → POST nội dung framework tại các platform (Reddit, HN, LW, etc.)
  → = TÁC GIẢ tạo content RIÊNG → mời engage
  → = Push-based: tác giả đẩy content ra

CHIẾN LƯỢC MỚI (file này):
  → Chuyên gia đã có AUDIENCE SẴN (YouTube, blog, podcast)
  → Mỗi video/bài mới = CƠ HỘI tham gia thảo luận
  → Comment phân tích = CHO GIÁ TRỊ cho audience CỦA HỌ
  → Link framework = cho người MUỐN ĐỌC SÂU HƠN
  → = Pull-based: audience tự chọn click, không bị ép

HAI CHIẾN LƯỢC BỔ SUNG NHAU:
  Plan-tech-distribution = tạo NỘI DUNG MỚI → thu hút audience
  Plan-content-engagement = tham gia NỘI DUNG CÓ SẴN → leverage audience

  Giống:
    Open source project: vừa viết docs RIÊNG (plan-tech)
    vừa trả lời StackOverflow questions (plan-content-engagement)
    Cả 2 dẫn về CÙNG 1 repo.
```

### 0.2 — Tại Sao Cách Này Hoạt Động

```
5 LÝ DO:

① AUDIENCE ĐÃ CÓ SẴN:
  → Chuyên gia có hàng nghìn → hàng triệu viewer
  → KHÔNG cần build audience từ 0
  → Audience ĐÃ quan tâm đúng lĩnh vực (neuroscience, psychology, behavior)
  → = Reach GẤP NHIỀU LẦN tự post tại platform mới

② VALUE-FIRST, LINK-SECOND:
  → Comment cho INSIGHT trước (phân tích video qua framework lens)
  → Link framework = phụ, cho ai muốn đi sâu
  → Người đọc thấy giá trị → tò mò → click → discover framework
  → = EARNED attention, không phải BOUGHT attention

③ MERITOCRATIC (YouTube + Reddit comment system):
  → Comment hay → like nhiều → lên top → nhiều người thấy
  → Comment tệ → chìm → không ai thấy
  → = Quality tự sàng lọc. Framework đúng → phân tích hay → tự lên top
  → = Framework sai → phân tích yếu → chìm → ĐÚNG, không waste attention

④ BỔ SUNG EXPERT'S CONTENT (không sửa):
  → Frame: "video đúng ở A, framework mở rộng thêm B"
  → KHÔNG: "video sai ở C" → fan phản ứng tiêu cực
  → = Win-win: expert có engagement, audience có depth, framework có reach

⑤ PERSISTENCE + DISCOVERABILITY:
  → Comment trên YouTube = TỒN TẠI SUỐT ĐỜI VIDEO
  → Người xem video 6 tháng sau → vẫn thấy comment → vẫn click
  → Khác Reddit post (chìm sau 48h) hoặc HN (chìm sau 24h)
  → = Long-term passive reach
```

### 0.3 — So Sánh Với Cold Email (đã reject)

```
  ┌───────────────────────────────────────────────────────────────────┐
  │                    │ Cold Email              │ Content Engagement  │
  ├───────────────────────────────────────────────────────────────────┤
  │ Reach              │ 1 email → 1 person      │ 1 comment → N viewers│
  │ Trust ban đầu      │ 0 (stranger)            │ Earned qua insight   │
  │ Người đọc tự chọn  │ Không (bị push)         │ Có (pull-based)      │
  │ Spam risk          │ Cao (domain blacklist)   │ Thấp (content-based) │
  │ Effort per contact │ Cao (tìm email, cá nhân)│ Trung (phân tích)    │
  │ Persistence        │ 0 (1 lần, xóa, quên)   │ Cao (comment tồn tại)│
  │ Scalability        │ Linear                  │ Compound             │
  │ Expert phản ứng    │ Ignore/block            │ Có thể engage lại    │
  │ Signal chất lượng  │ 0                       │ Likes/upvotes/replies│
  └───────────────────────────────────────────────────────────────────┘

  → Content Engagement THẮNG ở mọi metric.
  → Cold Email chỉ hơn ở 1 điểm: direct-to-expert.
    NHƯNG: nếu expert thấy comment hay → EXPERT TỰ tìm tới tác giả.
    = Kết quả GIỐNG nhưng trust CAO HƠN vì expert CHỌN engage.
```

---

## §1 — WORKFLOW: VIDEO/BÀI → PHÂN TÍCH → COMMENT

### 1.1 — Quy Trình 5 Bước

```
  BƯỚC 1: CHỌN NỘI DUNG
    → Expert post video/bài/podcast mới
    → Nội dung LIÊN QUAN tới framework (neuroscience, psychology, behavior,
      education, AI × human, decision-making, motivation, etc.)
    → ⚠️ Không phân tích content KHÔNG liên quan (lãng phí effort)
    → ⚠️ Ưu tiên: content MỚI (<48h) → comment vào lúc engagement cao nhất

  BƯỚC 2: CHUYỂN ĐỔI (nếu video/podcast)
    → Transcript từ video (YouTube auto-transcript, hoặc tool)
    → Nếu bài viết → đọc trực tiếp
    → = Input cho bước 3

  BƯỚC 3: PHÂN TÍCH QUA FRAMEWORK LENS
    → Đọc transcript/bài → AI (Claude) phân tích:
      ① Expert nói gì? (tóm tắt core claims)
      ② Framework đồng ý ở đâu? (leverage points — CÓ THỂ rất nhiều)
      ③ Framework bổ sung gì? (cái expert chưa cover → GIÁ TRỊ CHÍNH)
      ④ Có divergence nào? (nhẹ nhàng, nếu có)
      ⑤ Liên kết tới file nào trong framework?

    → Output: bản phân tích chi tiết (~500-2000 chữ)

  BƯỚC 4: VIẾT COMMENT (ngắn, trên platform)
    → Chắt lọc từ bản phân tích → 3-5 câu
    → Format: 1 insight cụ thể + link tới phân tích đầy đủ
    → Ngôn ngữ: mainstream, không jargon framework
    → = HOOK. Người đọc thấy hay → click link → đọc sâu → discover framework.

  BƯỚC 5: ĐĂNG PHÂN TÍCH ĐẦY ĐỦ (ở nơi khác)
    → GitHub Discussions (category: Content Analysis)
    → HOẶC blog/Substack post
    → Phân tích đầy đủ + link tới video gốc + link tới framework files
    → = Deep content. Ai click từ comment → đọc ở đây → discover framework.
```

### 1.2 — Ví Dụ Cụ Thể: 1 Video Chase Hughes

```
GIẢ SỬ: Chase Hughes đăng video "5 Signs Someone Is Lying"

BƯỚC 2 — Transcript:
  → YouTube auto-transcript → đọc

BƯỚC 3 — Phân tích qua framework:
  ① Expert nói: "5 dấu hiệu ai đó nói dối: micro-expressions, eye movement,
     body posture, speech patterns, emotional leakage"
  ② Framework đồng ý: body signals = real (Body-Feedback architecture),
     behavioral tells = observable (Observation parameters)
  ③ Framework bổ sung:
     → Lie detection = prediction-delta: bạn PREDICT hành vi bình thường
       → hành vi THỰC TẾ lệch → body-feedback kích hoạt → "something's off"
     → 5 signs Chase liệt kê = BIỂU HIỆN CỦA prediction-delta
     → Người quen nói dối DỄ bắt hơn người lạ →
       vì compiled baseline CỦA người quen RÕ hơn → delta MẠNH hơn
     → Training lie detection = COMPILE baseline rộng hơn → delta nhạy hơn
  ④ Divergence nhẹ:
     → Mirror neuron angle (nếu Chase dùng) → framework dùng
       Self-Pattern-Modeling thay thế → nhưng KẾT QUẢ tương đương
  ⑤ Files liên quan: Observation/Prediction-Delta.md,
     Body-Feedback/Body-Feedback-Mechanism.md, Agent-Mechanism/Self-Pattern-Modeling.md

BƯỚC 4 — Comment YouTube (~100 chữ):
  "Great breakdown. What's interesting is that these 5 signs all share
   a common mechanism — your brain constantly PREDICTS how someone
   should behave (based on compiled baseline from past interactions).
   When actual behavior diverges from prediction, your body generates
   a 'something's off' signal BEFORE you consciously process it.
   That's why you can often FEEL a lie before you can EXPLAIN why.
   Wrote a deeper analysis connecting this to predictive behavioral
   models here: [link to GitHub Discussion post]"

BƯỚC 5 — GitHub Discussion post (~800 chữ):
  → Full analysis: 5 signs × prediction-delta mechanism
  → Evidence: Libet 1983, body-first processing, compiled baseline research
  → Framework files referenced
  → Link to full framework repo
  → "Does this mechanism explain your lie-detection experience?
     Where does it break?"
```

---

## §2 — CHANNEL SELECTION: CHỌN KÊNH NÀO

### 2.1 — Tiêu Chí Chọn Kênh (5 điều kiện)

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  #  │ TIÊU CHÍ                               │ TẠI SAO            │
  ├─────────────────────────────────────────────────────────────────────┤
  │  ①  │ Nội dung LIÊN QUAN tới framework         │ Phân tích có ý     │
  │     │ (neuro, psych, behavior, education,      │ nghĩa, không       │
  │     │  AI × human, motivation, decision)       │ gượng ép            │
  ├─────────────────────────────────────────────────────────────────────┤
  │  ②  │ Audience CÓ CHIỀU SÂU                    │ Người đọc comment  │
  │     │ (không thuần giải trí, có thói quen      │ KỸ, willing to     │
  │     │  đọc phân tích dài)                      │ click + đọc sâu    │
  ├─────────────────────────────────────────────────────────────────────┤
  │  ③  │ Comment section HOẠT ĐỘNG                │ Nếu comment section│
  │     │ (có thảo luận thật, không chỉ "great     │ chết → effort waste│
  │     │  video!", creator engage với comments)    │                    │
  ├─────────────────────────────────────────────────────────────────────┤
  │  ④  │ Expert có CREDIBILITY trong domain       │ Audience đã trust  │
  │     │ (không phải self-help guru hoặc clickbait│ expert → extend    │
  │     │  channel)                                │ trust tới comment  │
  ├─────────────────────────────────────────────────────────────────────┤
  │  ⑤  │ Kích thước vừa phải                      │ Quá lớn → comment  │
  │     │ (10K-1M subscribers tối ưu)              │ chìm. Quá nhỏ →   │
  │     │ (>1M vẫn được nếu ② + ③ mạnh)           │ reach thấp         │
  └─────────────────────────────────────────────────────────────────────┘

  MỘT KÊNH CẦN ĐẠT ≥4/5 TIÊU CHÍ.
  Thiếu ① = không phân tích được → skip.
  Thiếu ③ = effort waste → skip.
```

### 2.2 — Loại Kênh Target (5 nhóm, map tới expert-verification-map.md)

```
NHÓM A — BEHAVIORAL SCIENCE (priority cao nhất)
  Map tới: Tier 1 + Tier 2 expert groups (expert-verification-map.md)
  Ví dụ kênh:
    → Chase Hughes — behavior profiling, body language
    → Vanessa Van Edwards (Science of People) — behavioral research popularized
    → Andrew Huberman — neuroscience protocols (⚠️ rất lớn, comment có thể chìm)
    → Matt Walker — sleep science
    → Robert Sapolsky (Stanford lectures, YouTube)
  Nội dung phù hợp: dopamine, cortisol, motivation, stress, behavior patterns
  Framework leverage: Clarification files, Body-Feedback, Observation parameters

NHÓM B — PSYCHOLOGY + MENTAL HEALTH
  Map tới: Tier 2 expert groups (Clinical, Developmental, Social Psych)
  Ví dụ kênh:
    → Therapy in a Nutshell — evidence-based therapy
    → Dr. K (HealthyGamerGG) — psychology × gaming/tech audience
    → The School of Life — philosophy + psychology
    → Dr. Ramani — narcissism / personality disorders
  Nội dung phù hợp: biết mà không làm được, self-regulation, relationship patterns
  Framework leverage: Core-Software (2 systems), Connection, Empathy, Schema

NHÓM C — EDUCATION + LEARNING
  Map tới: Education Research expert group
  Ví dụ kênh:
    → Veritasium — science education, misconceptions
    → 3Blue1Brown — math visualization (nếu video về learning itself)
    → Thomas Frank — learning strategies (⚠️ self-help adjacent, cẩn thận)
  Nội dung phù hợp: how learning works, memory, skill acquisition
  Framework leverage: Compile types, Direction > Level, Education mechanism

NHÓM D — AI + TECHNOLOGY × HUMAN
  Map tới: AI/ML expert group + tech audience (plan-overview-distribution.md)
  Ví dụ kênh:
    → Two Minute Papers — AI research
    → Yannic Kilcher — ML paper reviews
    → AI Explained — AI developments
    → Lex Fridman (podcast) — deep interviews (⚠️ rất lớn)
  Nội dung phù hợp: AI × human interaction, decision-making, attention
  Framework leverage: AI-Self-Model, AI-Schema-Detection, Human-AI-Future

NHÓM E — ACADEMIC / LECTURES
  Map tới: Tier 1 + Tier 3 expert groups
  Ví dụ kênh:
    → Stanford (Robert Sapolsky lectures)
    → MIT OpenCourseWare (neuroscience, psychology)
    → Coursera/edX official channels
    → ResearchGate / Academia.edu profiles có blog
    → LibreTexts (textbook platform — comment/discussion)
  Nội dung phù hợp: academic content, deep material
  Framework leverage: toàn bộ framework có thể reference
  ⚠️ Comment tone phải ACADEMIC — không informal
```

### 2.3 — Kênh KHÔNG Target

```
  ✗ Self-help / productivity channels (thiếu depth, audience kỳ vọng "tips")
  ✗ Entertainment channels dùng psychology clickbait
  ✗ Channels có comment section toxic hoặc dead
  ✗ Channels quá lớn (>5M) MÀ comment section không có depth
    → Exception: Huberman, Sapolsky = lớn NHƯNG audience có chiều sâu
  ✗ Channels không liên quan tới framework
    → KHÔNG comment video game, cooking, vlog, v.v.
    → = Spam, damage credibility
```

---

## §3 — COMMENT FORMAT: NGẮN + GIÁ TRỊ + LINK

### 3.1 — Cấu Trúc Comment (4 phần, ~80-150 chữ)

```
PHẦN 1 — ACKNOWLEDGE (1 câu):
  → Công nhận giá trị nội dung của expert
  → "Great breakdown of [topic]" hoặc "Really interesting point about [X]"
  → KHÔNG nịnh — genuine, cụ thể

PHẦN 2 — ADD VALUE (2-3 câu):
  → 1 insight cụ thể từ framework, liên quan trực tiếp tới video
  → Ngôn ngữ mainstream, KHÔNG jargon framework
  → Frame: "Điều thú vị thêm là..." hoặc "This connects to..."
  → = GIÁ TRỊ CHÍNH. Người đọc thấy insight mới → muốn đọc thêm.

PHẦN 3 — BRIDGE (1 câu, optional):
  → Nếu insight cần giải thích thêm → link tới phân tích đầy đủ
  → "Wrote a deeper analysis connecting this to [concept]: [link]"
  → ⚠️ KHÔNG link nếu comment đã đủ ý — chỉ link khi có MORE content.

PHẦN 4 — INVITE ENGAGEMENT (1 câu, optional):
  → "Does this match your experience?" hoặc "Where does this break?"
  → = Tạo conversation, không phải monologue
```

### 3.2 — Template Comment (3 biến thể)

```
BIẾN THỂ A — SUPPLEMENT (bổ sung):
  "Great breakdown of [topic]. What's interesting is that
   [1 insight cụ thể từ framework, ngôn ngữ mainstream].
   This means [implication mà audience care about].
   Deeper analysis here: [link]"

  Ví dụ:
  "Great breakdown of micro-expressions. What's interesting is that
   your brain runs a constant prediction loop — it EXPECTS certain
   expressions from people you know, and when the actual expression
   diverges, your body generates a 'something's off' signal BEFORE
   you can explain why. That's why lie detection improves dramatically
   with people you know well — you have a richer prediction baseline.
   Deeper analysis connecting this to predictive behavioral models: [link]"

BIẾN THỂ B — EXPLAIN WHY (giải thích cơ chế):
  "[Expert] explains WHAT happens well. Here's a possible WHY:
   [mechanism từ framework, ngôn ngữ đơn giản].
   This also explains why [edge case mà video chưa cover].
   More on this mechanism: [link]"

  Ví dụ:
  "Huberman explains the dopamine system well. Here's an interesting
   nuance: dopamine may not actually signal 'reward' — it signals
   'something relevant changed.' That's why you get a dopamine spike
   from BAD news too (your prediction was wrong, brain needs to update).
   This reframe also explains why social media feels compelling but
   empty — novelty triggers dopamine, but satisfaction requires a
   different system (opioid pathway).
   Deeper analysis of the dopamine reframe: [link]"

BIẾN THỂ C — QUESTION (đặt câu hỏi mở):
  "Interesting point about [X]. If we take this further:
   [implication từ framework, dạng câu hỏi].
   [1 observation mà audience có thể tự test].
   What do you all think? [link to discussion]"

  Ví dụ:
  "Interesting point about willpower running out. But what if it's not
   a 'limited resource' that depletes — what if 'knowing' and 'doing'
   are literally two different systems? Your conscious mind (knowing)
   is more like a monitoring process; your body-level compiled patterns
   (doing) is the actual execution engine. That would explain why
   reading about productivity never makes you productive.
   Anyone else experience this mismatch? Discussion: [link]"
```

### 3.3 — Quy Tắc Comment

```
✓ DO:
  → Cụ thể — reference CHÍNH XÁC điểm nào trong video
  → Add value — insight MỚI, không repeat video
  → Mainstream language — "prediction loop" không "prediction-delta observation parameter"
  → Respectful — bổ sung, không tranh cãi
  → 1 comment per video — KHÔNG comment nhiều lần (spam)
  → Trả lời replies — nếu ai hỏi thêm → engage → build trust

✗ DON'T:
  → Sửa expert trực tiếp — "Actually, you're wrong about X"
    → Fan backlash + expert có thể hide comment
  → Comment quá dài — >200 chữ = bị collapse, không ai đọc
  → Jargon framework — "prediction-delta", "compiled behavior", "body-base"
    → Audience không hiểu → skip
    → Dùng: "your brain predicts", "learned patterns in your body",
      "automatic responses"
  → Link-first — link trong câu đầu = spam detection
    → Link ở CUỐI, SAU khi đã cho value
  → Comment video không liên quan — waste + spam image
  → Copy-paste cùng 1 comment cho nhiều video — spam THẬT
```

---

## §4 — DEEP ANALYSIS: NỘI DUNG PHÂN TÍCH ĐẦY ĐỦ

### 4.1 — Đăng Ở Đâu

```
ƯU TIÊN 1: GitHub Discussions (category: Content Analysis)
  → Nếu GitHub repo đã setup Discussions
  → Ưu điểm: mọi analysis tập trung 1 nơi, discoverable, liên kết framework
  → Format: markdown, có thể link tới framework files cụ thể

ƯU TIÊN 2: Blog/Substack
  → Nếu có blog riêng
  → Ưu điểm: SEO, shareable, format đẹp hơn
  → Nhược: tách khỏi framework repo

ƯU TIÊN 3: Reddit post (r/cogsci, r/slatestarcodex)
  → Nếu analysis fit đúng subreddit
  → Ưu điểm: reach, discussion
  → Nhược: chìm sau 48h

TẤT CẢ ĐỀU LINK VỀ GITHUB REPO (hub-and-spoke, github-infrastructure.md).
```

### 4.2 — Cấu Trúc Deep Analysis (~500-2000 chữ)

```
  ① CONTEXT (2-3 câu):
     "[Expert name], trong video/bài [title], nói về [topic].
      Link: [original content link]"
     → = Credit + context cho người chưa xem video

  ② TÓM TẮT NỘI DUNG (3-5 bullets):
     → Core claims/points của expert
     → = Cho người đọc hiểu KHÔNG CẦN xem video

  ③ FRAMEWORK ĐỒNG Ý (2-3 bullets):
     → Điểm expert nói ĐÚNG theo framework lens
     → Reference evidence/citations
     → = Respectful, không 100% phản bác

  ④ FRAMEWORK BỔ SUNG (phần CHÍNH — 3-5 paragraphs):
     → Cái expert chưa cover mà framework mở rộng
     → Mechanism giải thích WHY content đúng (nếu đúng)
     → Edge cases / implications mà video chưa tới
     → = GIÁ TRỊ CHÍNH của analysis

  ⑤ DIVERGENCE (nếu có — 1-2 paragraphs, nhẹ nhàng):
     → "Framework suggests a different mechanism for X"
     → Frame: "alternative interpretation" không "correction"
     → LUÔN acknowledge evidence CỦA expert

  ⑥ FRAMEWORK FILES (bullets):
     → Link tới files cụ thể trong repo cho chi tiết
     → = Người đọc thích → click → đọc framework trực tiếp

  ⑦ INVITE DISCUSSION:
     → "Does this mechanism match your observation?"
     → "Where does this break?"
     → = Consistent với framing-engagement-value.md
```

---

## §5 — CADENCE + EFFORT MANAGEMENT

### 5.1 — Thời Gian Ước Lượng Mỗi Content

```
  ┌───────────────────────────────────────────────────────────────────┐
  │ BƯỚC                              │ THỜI GIAN      │ GHI CHÚ     │
  ├───────────────────────────────────────────────────────────────────┤
  │ Chọn content                      │ 10-15 phút     │ Scan kênh   │
  │ Chuyển transcript (nếu video)     │ 5-10 phút      │ Auto tool   │
  │ AI phân tích qua framework lens   │ 30-60 phút     │ Core effort │
  │ Viết comment (ngắn)               │ 10-15 phút     │ Chắt lọc    │
  │ Viết deep analysis                │ 30-60 phút     │ Nếu cần     │
  ├───────────────────────────────────────────────────────────────────┤
  │ TỔNG (có deep analysis)           │ ~1.5-2.5 giờ   │             │
  │ TỔNG (chỉ comment)                │ ~1-1.5 giờ     │             │
  └───────────────────────────────────────────────────────────────────┘
```

### 5.2 — Cadence Khuyến Nghị

```
GIAI ĐOẠN 1 — THỬ NGHIỆM (tuần 1-4):
  → 1-2 comment/tuần
  → Chọn 2-3 kênh target
  → Đo: likes, replies, clicks (nếu link trackable)
  → Refine: format nào hoạt động? Kênh nào response tốt?

GIAI ĐOẠN 2 — ỔN ĐỊNH (tuần 5-12):
  → 2-3 comment/tuần
  → 3-5 kênh ổn định
  → Deep analysis 1 lần/tuần (chọn content hay nhất)
  → Build presence: cùng người xuất hiện → audience nhận ra tên

GIAI ĐOẠN 3 — TỰ NHIÊN (tháng 3+):
  → Comment khi có content thực sự phù hợp (không ép cadence)
  → Deep analysis khi insight thực sự mới
  → Focus shift: người từ comment ĐÃ tìm tới framework → engage ở GitHub
  → = Comment trở thành 1 kênh trong nhiều kênh, không phải kênh chính

⚠️ RULES:
  → KHÔNG ép cadence: chỉ comment khi có INSIGHT THẬT
  → KHÔNG comment chỉ để "giữ presence" → quality > quantity
  → 1 comment/video MAX — KHÔNG comment 2 lần cùng video
  → Nếu 1 tuần không có content phù hợp → KHÔNG comment = đúng
```

---

## §6 — FRAMING RULES (nhất quán với plan-public.md W.4)

### 6.1 — Nguyên Tắc Áp Dụng Từ Các File Khác

```
TỪ plan-public.md W.4:
  ✗ KHÔNG: "Framework sẽ thay đổi cuộc sống bạn"
  ✓ CÓ:   "IF this mechanism is correct, it has implications for [topic]"

TỪ framing-engagement-value.md:
  → Tầng 1 (individual understanding) = NGẦM — show through "test this"
  → Tầng 2 (verification contribution) = HIỆN — "does this match?"
  → Counter-evidence > confirmation — "where does this break?"

TỪ plan-overview-distribution.md §4:
  → Welcome challenges — "Good point. Here's the evidence."
  → Honest gaps — "We don't know. That's a genuine gap."
  → Update if falsified — credit challenger

ÁP DỤNG CHO COMMENT:
  → Comment KHÔNG promise benefit
  → Comment CHO insight + MỜI test
  → Comment WELCOME disagreement
  → Comment LINK to more (không force)
```

### 6.2 — Ngôn Ngữ Comment (mainstream, không jargon)

```
FRAMEWORK TERM          →    COMMENT LANGUAGE
───────────────────────────────────────────────────────
prediction-delta        →    "your brain's prediction vs reality"
compiled behavior       →    "automatic patterns / learned responses"
body-base               →    "your body's automatic system"
PFC                     →    "conscious thinking / deliberate thought"
body-feedback           →    "gut feeling / physical signal"
chunk                   →    "experience pattern / memory unit"
compile                 →    "learning that becomes automatic"
observation parameter   →    "behavioral dimension"
Imagine-Final           →    "mental model of ideal outcome"
Self-Pattern-Modeling   →    "understanding others through your own experience"
approach/avoidance      →    "drawn towards / pushed away from"
Trust Compile           →    "learning from authority without personal experience"
Experience Compile      →    "learning from direct experience"
Expertise Compile       →    "learning through practice + feedback"
dopamine ≠ reward       →    "dopamine signals change, not pleasure"
cortisol ≠ stress       →    "cortisol = readiness signal, not stress signal"

⚠️ Chỉ dùng framework terms trong DEEP ANALYSIS (GitHub/blog),
   KHÔNG trong comment trên YouTube/platform gốc.
```

---

## §7 — RISK MANAGEMENT

### 7.1 — Risks + Mitigation

```
① BỊ COI LÀ SPAM:
  Risk: comment nhiều video cùng kênh → creator/audience coi là spam
  Mitigation:
    → Max 1 comment/video
    → Không comment MỌI video — chỉ khi có insight thật
    → Vary content — không copy-paste
    → Value TRƯỚC, link SAU (hoặc không link)
    → Nếu creator block → DỪNG kênh đó, KHÔNG tạo account mới

② FAN BACKLASH (nếu diverge với expert):
  Risk: comment "thêm góc nhìn khác" → fan hiểu = "sửa thần tượng" → attack
  Mitigation:
    → Frame BỔ SUNG, không SỬA: "This adds another layer..."
    → Acknowledge expert TRƯỚC: "Great point by [name]..."
    → Nếu fan attack → KHÔNG engage flame war → chỉ respond nếu constructive
    → Nhận sai nếu sai: "Good point, I hadn't considered that"

③ EXPERT PHẢN ỨNG TIÊU CỰC:
  Risk: expert thấy comment "bổ sung" = ai đó coi thường expertise CỦA HỌ
  Mitigation:
    → LUÔN respectful, LUÔN credit expert
    → Frame: "Building on [name]'s point..."
    → Nếu expert responds negatively → acknowledge + back off
    → BEST CASE: expert thấy hay → engage → collab opportunity

④ LOW ENGAGEMENT (comment chìm):
  Risk: comment hay nhưng không ai thấy (YouTube algorithm, timing, v.v.)
  Mitigation:
    → Comment SỚM (<24h sau khi video đăng) — YouTube pushes early comments
    → Keep comment SHORT → more likely to get likes → algorithm boost
    → Deep analysis TỒN TẠI ở nơi khác (GitHub) → không phụ thuộc 1 comment
    → ĐỪNG TẠO KỲ VỌNG — comment là SEED, không phải guarantee

⑤ CREDIBILITY GAP (ai đây mà bổ sung cho expert?):
  Risk: audience: "random commenter nói gì? Expert có PhD, bạn có gì?"
  Mitigation:
    → Focus vào EVIDENCE, không vào authority
    → "Research shows..." không "I believe..."
    → Link tới framework (170+ files, citations) = show depth
    → Over time: consistent quality comments → audience nhận ra tên
    → META: credibility BUILD qua quality, không CLAIM bằng credentials
```

---

## §8 — METRICS + SUCCESS SIGNALS

```
  ┌─────────────────────────────────────────────────────────────────┐
  │ TÍN HIỆU THÀNH CÔNG                                           │
  ├─────────────────────────────────────────────────────────────────┤
  │ → Comment nhận ≥10 likes (YouTube) hoặc ≥5 upvotes (Reddit)   │
  │ → Replies engaging with framework concept (không chỉ "cool")  │
  │ → Click tới deep analysis (nếu track được)                    │
  │ → GitHub stars/discussions tăng sau comment                    │
  │ → Expert respond/engage với comment (HIẾM nhưng cao giá trị)  │
  │ → Audience members tìm tới framework KHÔNG QUA comment        │
  │   (discover qua search vì comment plant seed)                  │
  │ → Cùng audience member xuất hiện ở nhiều video → recognizable  │
  ├─────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU THẤT BẠI                                             │
  ├─────────────────────────────────────────────────────────────────┤
  │ → Comment liên tục 0 engagement (>10 comments, 0 likes)       │
  │   → Refine format, đổi kênh, hoặc review chất lượng insight  │
  │ → Bị flag spam bởi platform/creator                           │
  │   → DỪNG ngay kênh đó, review approach                       │
  │ → Fan backlash (>3 negative replies, 0 positive)              │
  │   → Điều chỉnh tone, frame bổ sung rõ hơn                    │
  │ → Deep analysis 0 reads                                        │
  │   → Check: link accessible? Title clear? Content quality?      │
  ├─────────────────────────────────────────────────────────────────┤
  │ TÍN HIỆU TRUNG LẬP                                            │
  ├─────────────────────────────────────────────────────────────────┤
  │ → Comment nhận 2-5 likes, 0 replies                            │
  │   → Bình thường cho giai đoạn đầu. Kiên nhẫn.                │
  │ → 1 comment viral, còn lại bình thường                        │
  │   → = Content quality matters more than consistency            │
  └─────────────────────────────────────────────────────────────────┘
```

---

## §9 — PREREQUISITES: CẦN GÌ TRƯỚC KHI BẮT ĐẦU

```
PHẢI CÓ:
  □ GitHub repo public (có sẵn)
  □ GitHub Discussions enabled với category "Content Analysis"
  □ Chọn 2-3 kênh target ban đầu (§2.2)
  □ Framework đủ English context cho deep analysis
    (ít nhất: README EN, Clarification files EN)
  □ AI assistant (Claude) để phân tích video content

NÊN CÓ:
  □ Blog/Substack cho deep analysis (backup nếu GitHub Discussions chưa setup)
  □ YouTube account không mới quá (comment từ new account bị filter)
  □ Danh sách 10-15 kênh phù hợp (scan trước)

KHÔNG CẦN:
  □ Toàn bộ framework dịch EN (deep analysis có thể mix VN references)
  □ Preprint / DOI (bổ sung sau)
  □ Social media presence (comment = BUILD presence)
```

---

## §10 — RELATION TO OTHER PLANS

```
  ┌──────────────────────────────────────────────────────────────────┐
  │ FILE NÀY                                                        │
  │ plan-content-engagement.md                                      │
  │   = CHIẾN LƯỢC THAM GIA nội dung chuyên gia                    │
  │   = Leverage existing audience                                  │
  │   = Pull-based (audience tự chọn engage)                       │
  ├──────────────────────────────────────────────────────────────────┤
  │ plan-overview-distribution.md                                    │
  │   = CHIẾN LƯỢC TẠO nội dung mới tại platforms                  │
  │   = Build audience qua content riêng                            │
  │   = Push-based (tác giả đẩy content ra)                        │
  ├──────────────────────────────────────────────────────────────────┤
  │ plan-public.md                                                  │
  │   = CHIẾN LƯỢC TỔNG THỂ (phases, framing rules)               │
  │   = W.4, W.5 = LUẬT CHO CẢ 2 plan trên                       │
  ├──────────────────────────────────────────────────────────────────┤
  │ framing-engagement-value.md                                     │
  │   = NGUYÊN TẮC FRAMING (3 tầng, anti-patterns)                │
  │   = Áp dụng cho MỌI bài post + comment                        │
  ├──────────────────────────────────────────────────────────────────┤
  │ expert-verification-map.md                                      │
  │   = ROUTING TABLE: kênh nào → expert group nào verify          │
  │   = §2.2 của file này map channels tới expert groups           │
  └──────────────────────────────────────────────────────────────────┘

THỨ TỰ THỰC HIỆN (cả 2 plan có thể chạy song song):
  → plan-content-engagement.md (file này) — bắt đầu NGAY (low barrier)
  → plan-overview-distribution.md — bắt đầu khi prerequisites ready
  → Cả 2 dẫn về CÙNG GitHub repo (convergence)

⚠️ QUAN TRỌNG:
  2 plan KHÔNG mâu thuẫn. Chúng bổ sung:
    Content Engagement = đi tới AUDIENCE CỦA NGƯỜI KHÁC
    Tech Distribution = tạo AUDIENCE CỦA MÌNH
    Cả 2 → GitHub hub → verification → trust
```

---

> **Plan v0.1 — sẽ refine dần.**
> Bước tiếp:
>   1. Chọn 2-3 kênh target cụ thể
>   2. Thử với 1 video: transcript → phân tích → comment → measure
>   3. Setup GitHub Discussions category "Content Analysis"
>   4. Refine format dựa trên kết quả thực tế
