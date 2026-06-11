# Distribution Prepare — Chi Tiết Quá Trình Chuẩn Bị

> **Mục tiêu:** Checklist đầy đủ mọi thứ cần làm TRƯỚC KHI post bài đầu tiên.
> **Nguyên tắc:** Hoàn tất preparation → post bài đầu tiên. Không post khi chưa sẵn sàng.
> **Trạng thái:** v1.0
> **Ngày:** 2026-06-06
> **Liên kết:**
>   plan-distribution.md — bản đồ phân phối (blog nào → platform nào)
>   ../Tech/github-infrastructure.md — GitHub setup chi tiết

---

## §1 — ACCOUNTS & PROFILES

### 1.1 — ORCID iD

```
  URL:          https://orcid.org/register
  Thời gian:    ~5 phút
  Yêu cầu:     Email ()
  Affiliation:  "Independent Researcher"
  Mục đích:     Universal researcher ID — dùng cho Zenodo, ResearchGate,
                mọi nơi cần researcher identity.
  □ Đăng ký
  □ Ghi lại ORCID iD: ____________________
```

### 1.2 — Zenodo (CERN)

```
  URL:          https://zenodo.org
  Thời gian:    ~15 phút
  Yêu cầu:     GitHub account (để kết nối)

  BƯỚC:
    □ Đăng nhập bằng GitHub
    □ Kết nối repository Human-Predictive-Drive
    □ Tạo GitHub Release tag (xem §2.1) → Zenodo auto-archive
    □ Điền metadata:
        Title:       Human Predictive Drive Framework
        Author:      [tên] (ORCID: [iD từ §1.1])
        Description: Cross-domain framework connecting neuroscience,
                     psychology, and evolutionary biology.
                     Hypothesis inviting falsification. CC0.
        Keywords:    predictive processing, embodied cognition,
                     interoception, affective neuroscience,
                     dopamine reframe, behavioral neuroscience
        License:     CC0 1.0 Universal
    □ NHẬN DOI → ghi lại: ____________________
    □ Dùng DOI này trong mọi short post footer
```

### 1.3 — ResearchGate

```
  URL:          https://www.researchgate.net
  Thời gian:    ~15 phút
  Affiliation:  "Independent Researcher"

  BƯỚC:
    □ Tạo account
    □ Điền profile (link ORCID)
    □ Tạo project "Human Predictive Drive"
    □ Upload framework description + link GitHub
    □ Link Zenodo DOI
```

### 1.4 — Bluesky

```
  URL:          https://bsky.app
  Thời gian:    ~10 phút setup + vài ngày build presence

  BƯỚC:
    □ Tạo account
    □ Follow neuroscience starter packs (search "neuroscience" trong Feeds)
    □ Follow 20-30 active neuroscientists
    □ Like/repost vài posts liên quan (build minimal presence)
    □ ĐỢI ít nhất 1 tuần trước khi post bài đầu tiên
      (account mới + post link ngay = spam signal)
```

### 1.5 — Reddit

```
  □ Kiểm tra account hiện tại:
    → Có đủ karma để post ở các subreddits target?
    → Account age đủ? (một số sub yêu cầu account cũ)
  □ Nếu chưa có account hoặc karma thấp:
    → Tham gia thảo luận ở các sub target TRƯỚC
    → Contribute value (trả lời câu hỏi, comment có chiều sâu)
    → KHÔNG spam, KHÔNG chỉ post link
    → Ước tính: 2-4 tuần tích karma tự nhiên
```

### 1.6 — LessWrong

```
  URL:          https://www.lesswrong.com
  Yêu cầu:     ≥5 karma để post tự do. <5 karma = max 2 posts/tuần.

  BƯỚC:
    □ Tạo account (nếu chưa có)
    □ Kiểm tra karma: ____
    □ Nếu <5 karma:
      → Comment có giá trị trên posts liên quan (cogsci, prediction, decision-making)
      → Upvote = karma. Cần vài comments tốt.
      → ĐỢI đạt 5+ karma trước khi post bài overview/logic-feeling
```

---

## §2 — GITHUB SETUP

### 2.1 — Release Tag

```
  □ Xác định version hiện tại: ____
  □ Tạo tag: git tag v[X.Y]
  □ Push tag: git push origin v[X.Y]
  □ Tạo Release trên GitHub:
    → Title: "Human Predictive Drive v[X.Y]"
    → Release notes:
      "Cross-domain framework connecting neuroscience, psychology,
       and evolutionary biology into a single architecture.
       200+ files, CC0 license, hypothesis inviting falsification.
       5 blog posts, explicit falsification criteria."
  □ Sau khi tag → Zenodo auto-archive (nếu đã kết nối §1.2)
```

### 2.2 — GitHub Discussions

```
  Ref: Tech/github-infrastructure.md

  □ Enable Discussions trên repo
  □ Tạo categories:
    → Announcements (tác giả only)
    → General (thảo luận chung)
    → Verification (claim-specific threads)
    → Falsification (challenges + responses)
    → Questions (hỏi về mechanism)
```

### 2.3 — Issue Labels

```
  □ Tạo labels:
    → [claim: neuroscience]    — biological claims cần verify
    → [claim: psychology]      — behavioral claims cần verify
    → [claim: education]       — learning claims cần verify
    → [claim: cross-domain]    — cross-domain consistency
    → [status: needs review]   — chưa ai verify
    → [status: verified]       — đã có evidence confirm
    → [status: challenged]     — có counterevidence
    → [status: updated]        — framework đã cập nhật theo feedback
```

### 2.4 — VERIFY.md

```
  Ref: Tech/github-infrastructure.md

  □ Tạo file VERIFY.md ở root repo
  □ Nội dung:
    → "How to stress-test this framework"
    → Step 1: Clone repo
    → Step 2: Open AI (Claude recommended)
    → Step 3: Drop entire folder vào AI
    → Step 4: Ask AI to check specific claims
    → Step 5: Report findings → GitHub Discussions
    → List: các câu hỏi gợi ý để verify
  □ Link từ README
```

### 2.5 — CLAIMS.md

```
  □ Tạo file CLAIMS.md ở root repo
  □ Nội dung:
    → Danh sách TẤT CẢ falsifiable claims
    → Mỗi claim: source file, evidence tier, falsification test
    → Ví dụ:
      "Claim: Dopamine ≠ reward signal
       Source: Clarification/Dopamine-Is-Not-Reward.md
       Evidence: 🟢 Berridge 2007, Liggins 2012
       Falsify: Direct dopamine increase → reliable pleasure increase"
  □ Link từ README + VERIFY.md
```

### 2.6 — README Review

```
  Hiện có: README.md (root) + English/README.md

  □ README phải có:
    → Framework description (1-2 paragraphs)
    → "Hypothesis inviting falsification" — KHÔNG "theory"
    → Link tới 5 blogs
    → Link tới VERIFY.md + CLAIMS.md
    → CC0 license statement
    → "What would falsify this? We want to know."
    → ORCID + Zenodo DOI
  □ Kiểm tra English README đầy đủ (audience quốc tế đọc cái này trước)
```

---

## §3 — BLOG VERIFICATION

### 3.1 — GitHub Pages Live

```
  Config:   docs/_config.yml (đã có)
  Base URL: https://hoanispof.github.io/Human-Predictive-Drive/

  □ Verify GitHub Pages enabled (Settings → Pages → Source)
  □ Verify _config.yml đúng:
    → url: "https://hoanispof.github.io"
    → baseurl: "/Human-Predictive-Drive"
  □ Verify builds thành công (Actions tab)
```

### 3.2 — 5 Blog URLs Live

```
  □ Blog A: .../blog/dopamine-signals-salience-not-reward/
  □ Blog B: .../blog/cortisol-is-not-stress/
  □ Blog C: .../blog/adhd-is-not-attention-deficit/
  □ Blog D: .../blog/bridging-neuroscience-psychology/
  □ Blog E: .../blog/logic-is-not-the-opposite-of-intuition/

  Mỗi blog kiểm tra:
    □ URL accessible (không 404)
    □ Content render đúng (heading, code blocks, citations)
    □ Footer links tới các blog khác hoạt động
    □ Footer link tới GitHub repo hoạt động
    □ Status marker: "Draft" đã bỏ? (hoặc giữ nếu chưa finalize)
```

### 3.3 — Cross-Links

```
  Mỗi blog footer nên link tới:
    □ GitHub repo (main link)
    □ Các blog khác (cross-reference)
    □ VERIFY.md (sau khi tạo §2.4)
    □ CLAIMS.md (sau khi tạo §2.5)

  Kiểm tra:
    □ Blog A footer → B, C, D, E links hoạt động
    □ Blog B footer → A, C, D, E links hoạt động
    □ Blog C footer → A, B, D, E links hoạt động
    □ Blog D footer → A, B, C, E links hoạt động
    □ Blog E footer → A, B, C, D links hoạt động
```

---

## §4 — SHORT POSTS REVIEW

### 4.1 — Checklist Per Short Post File

```
  Files cần review:
    □ blog/short-posts-dopamine.md        (Blog A → r/neuroscience, r/cogsci, Bluesky)
    □ blog/short-posts-cortisol.md        (Blog B → r/neuroscience, r/cogsci, Bluesky)
    □ blog/short-posts-adhd.md            (Blog C → r/neuro, r/cogsci, r/ADHD_Prog, Bluesky, r/ADHD)
    □ blog/short-post-overview.md         (Blog D → LW, r/SSC, HN, r/cogsci, r/psych, r/philo)
    □ blog/short-post-overview-main.md    (Blog D — bản chính)
    □ blog/short-posts-logic-feeling.md   (Blog E → LW, r/SSC, r/cogsci, Bluesky)
```

### 4.2 — Mỗi Short Post Kiểm Tra

```
  W.4 COMPLIANCE:
    □ Evidence + mechanism TRƯỚC → stakes SAU?
    □ Không self-help framing?
    □ Không grand claims?
    □ Không marketing language ("star the repo")?
    □ Có falsification criteria / "what would break this?"
    □ Kết thúc bằng invitation to challenge?

  LINKS:
    □ Blog URL đúng + hoạt động?
    □ GitHub repo URL đúng?
    □ DOI (sau khi có từ §1.2)?

  TONE:
    □ Phù hợp platform target? (academic cho r/neuro, accessible cho r/psych, etc.)
    □ Không condescending?
    □ "we" inclusive, ngang hàng?

  FORMAT:
    □ Reddit posts: text post, đúng độ dài (~250-400 words)?
    □ HN: submit blog link, không text post?
    □ Bluesky: micro-thread 4-5 posts × 300 chars?
    □ r/philosophy: frame "philosophical implications", không "my framework"?
```

---

## §5 — PLATFORM RULES CHECK

### 5.1 — Kiểm Tra Rules Từng Platform

```
  TRƯỚC KHI POST Ở BẤT KỲ PLATFORM NÀO:
    □ Đọc sidebar / wiki / pinned post rules
    □ Kiểm tra: framework posts có được phép?
    □ Kiểm tra: external links có được phép?
    □ Kiểm tra: account age / karma requirements?
    □ Xem 5-10 posts gần đây → tone + format chuẩn của community

  PER-PLATFORM:

  □ r/neuroscience:
    → Rules về self-promotion? Link posts?
    → Yêu cầu flair/tag?
    → Tone chuẩn: strict academic

  □ r/cogsci:
    → Rules về original frameworks?
    → Tone chuẩn: academic-accessible

  □ LessWrong:
    → Karma ≥5? (xem §1.6)
    → [Epistemic status] header bắt buộc?
    → Crosspost rules?

  □ r/slatestarcodex:
    → Flair requirements?
    → Long-form norms?

  □ Hacker News:
    → KHÔNG "Show HN:" (không phải runnable project)
    → Title: factual, không clickbait (editors sẽ đổi)
    → Post WEEKDAY (weekend traffic thấp)

  □ r/ADHD_Programmers:
    → Rules về medical advice?
    → Disclaimer requirements?
    → Community culture: peer-to-peer

  □ Bluesky:
    → 300 chars/post limit
    → Thread format norms
    → Hashtag practices: #neuroscience #CognitiveScience

  □ r/psychology:
    → Rules về original research/frameworks?
    → Self-promotion limits?

  □ r/philosophy:
    → ⚠️ RULES CỰC STRICT
    → Non-academic original frameworks THƯỜNG bị xóa
    → Frame: "philosophical implications" KHÔNG "my theory"
    → Đọc kỹ rules + xem posts bị xóa (removeddit) để hiểu pattern

  □ r/ADHD:
    → ⚠️ Medical advice rules STRICT
    → Disclaimer BẮT BUỘC: "not medical advice"
    → KHÔNG imply framework = diagnosis tool
    → KHÔNG suggest medication changes
    → Community culture: support-first
```

---

## §6 — FOOTER TEMPLATE

```
  Chuẩn bị sẵn footer template dùng cho MỌI post:

  ──────────────────────────────────────────────
  FOOTER TEMPLATE (adapt per platform):

  Full framework (200+ files, CC0, inviting falsification):
  [GitHub link]

  Verification guide: [VERIFY.md link]
  Falsifiable claims: [CLAIMS.md link]
  DOI: [Zenodo DOI]

  This is a hypothesis inviting falsification.
  What would break this? We want to know.
  ──────────────────────────────────────────────

  □ Template đã chuẩn bị
  □ Links đã điền đầy đủ (sau khi hoàn tất §1-§3)
  □ Adapt per platform:
    → Reddit/LW: full footer
    → HN: condensed (author comment)
    → Bluesky: link only (last post in thread)
```

---

## §7 — THỨ TỰ THỰC HIỆN

```
  Không cần làm tất cả cùng lúc. Thứ tự logic:

  ─── BƯỚC 1: Accounts (có thể làm song song) ───
    □ §1.1 ORCID
    □ §1.4 Bluesky (cần thời gian build presence)
    □ §1.5 Reddit karma check
    □ §1.6 LessWrong karma check

  ─── BƯỚC 2: GitHub Setup ───
    □ §2.1 Release tag
    □ §2.2 Discussions
    □ §2.3 Issue labels
    □ §2.4 VERIFY.md
    □ §2.5 CLAIMS.md
    □ §2.6 README review

  ─── BƯỚC 3: Archive + DOI ───
    □ §1.2 Zenodo (cần Release tag từ bước 2)
    □ §1.3 ResearchGate (cần ORCID từ bước 1)

  ─── BƯỚC 4: Content Verify ───
    □ §3.1 GitHub Pages live
    □ §3.2 5 blog URLs live
    □ §3.3 Cross-links hoạt động

  ─── BƯỚC 5: Short Posts + Footer ───
    □ §4.1-4.2 Review tất cả short posts
    □ §6 Footer template (cần DOI từ bước 3)

  ─── BƯỚC 6: Platform Rules ───
    □ §5.1 Đọc rules từng platform (trước khi post)

  ─── SẴN SÀNG POST BÀI ĐẦU TIÊN ───
    → Tiếp tục theo plan-distribution.md Phase 1
```
