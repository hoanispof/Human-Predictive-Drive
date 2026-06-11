# GitHub Infrastructure Setup — Extracted from plan-tech-distribution.md

> **Source:** plan-tech-distribution.md §4 — Convergence Architecture
> **Extracted:** 2026-06-04 (trước khi backup plan-tech-distribution.md)
> **Mục đích:** GitHub setup checklist + hub-and-spoke model cho distribution.
> **Trạng thái:** REFERENCE — chưa implement.

---

## Hub-and-Spoke Model

```
                  ┌─────────────┐
       ┌─────────│   GITHUB    │──────────┐
       │         │   (HUB)     │          │
       │         └──────┬──────┘          │
       │                │                 │
  ┌────┴─────┐   ┌──────┴──────┐   ┌─────┴────┐
  │ LessWrong│   │ Hacker News │   │ r/cogsci │
  └──────────┘   └─────────────┘   └──────────┘
       │                │                 │
  ┌────┴─────┐   ┌──────┴──────┐   ┌─────┴────┐
  │ SSC      │   │ Bluesky     │   │ r/psych  │
  └──────────┘   └─────────────┘   └──────────┘

MỌI POST ĐỀU KẾT THÚC VỚI:
  "Full framework (200+ files, CC0, inviting falsification):
   [GitHub link]"
  "What would falsify this? We want to know."
```

---

## Tại Sao GitHub Là Hub

```
① TECH AUDIENCE Ở ĐÓ SẴN:
  → Mọi dev có GitHub account
  → Không cần sign up platform mới → friction = 0
  → GitHub Discussions = forum built-in, free

② TRANSPARENT:
  → Mọi file visible, mọi thay đổi có history
  → Stars = proxy cho interest (visible social proof)
  → Issues = public record of challenges + responses
  → = KHÔNG giấu gì → trust

③ FORKABLE:
  → Ai muốn modify → fork → experiment
  → AI muốn verify → clone → chạy analysis
  → = Framework SỐNG bằng community, không phải tác giả

④ PERSISTENT:
  → Reddit post → chìm sau 48h
  → HN post → chìm sau 24h
  → GitHub repo → CÒN MÃI → mọi link trỏ tới ĐÂY
  → = Central reference point lâu dài

⑤ DOMAIN EXPERT CÓ THỂ TÌM:
  → Tech route claim cụ thể → domain expert mở GitHub → ĐỌC CỤ THỂ
  → Không cần đọc toàn bộ → chỉ đọc file được chỉ định
  → Issues tagged [needs-neuro-review] → domain expert biết đọc gì
```

---

## GitHub Setup Checklist (TRƯỚC KHI Post)

```
① ENABLE DISCUSSIONS:
  Categories:
    → Announcements (tác giả only)
    → General (thảo luận chung)
    → Verification (claim-specific threads)
    → Falsification (challenges + responses)
    → Questions (hỏi về mechanism)

② ISSUE LABELS:
  → [claim: neuroscience] — biological claims cần verify
  → [claim: psychology] — behavioral claims cần verify
  → [claim: education] — learning claims cần verify
  → [claim: cross-domain] — cross-domain consistency
  → [status: needs review] — chưa ai verify
  → [status: verified] — đã có evidence confirm
  → [status: challenged] — có counterevidence
  → [status: updated] — framework đã cập nhật theo feedback

③ CREATE VERIFICATION GUIDE:
  → File: VERIFY.md (hoặc section trong README)
  → "How to stress-test this framework with AI"
  → Step 1: Clone repo
  → Step 2: Open AI (Claude Opus recommended)
  → Step 3: Drop entire folder
  → Step 4: Ask AI to check specific claims
  → Step 5: Report findings in GitHub Discussions
  → = HƯỚNG DẪN CỤ THỂ cho tech audience

④ CREATE CLAIMS LIST:
  → File: CLAIMS.md
  → Danh sách TẤT CẢ falsifiable claims
  → Mỗi claim: source file, evidence, falsification test
  → = Checklist cho verification
  → Tech audience THÍCH checklists → engagement ↑

⑤ STAR/FORK STRATEGY:
  → Stars = social proof cho next platform
  → KHÔNG kêu gọi star — nếu tốt, tự star
  → Forks = people ĐANG verify/modify → activity signal
```

---

## Cross-Platform Linking Template

```
MỖI POST ĐỀU CÓ:

  FOOTER (cuối bài):
    "Full framework: 200+ files, CC0 license.
     GitHub: [link]
     Discussion: [GitHub Discussions link]
     Verification guide: [VERIFY.md link]
     Claims checklist: [CLAIMS.md link]
     
     This is a hypothesis inviting falsification.
     What would break this? We want to know."
```
