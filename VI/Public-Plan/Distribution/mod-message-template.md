---
title: Mod Message Template — Pre-Post Permission Check
date: 2026-06-08
purpose: Template message gửi mod trước khi post bài lên Reddit academic subs
status: Draft v0.1
applies_to:
  should_message: r/cogsci, r/neuroscience
  optional: r/psychology, r/PhilosophyofMind
  not_needed: LessWrong, HN, EA Forum, r/slatestarcodex, r/MachineLearning, Bluesky, Mastodon
references:
  short-post-overview.md — canonical post content
  plan-distribution.md — posting order + cadence
---

# Mod Message Template

> KHI NÀO GỬI:
>   Academic subs (r/cogsci, r/neuroscience) — NÊN gửi trước.
>   Lý do: standards cao, rules cụ thể về self-promotion / blog linking.
>   Message trước = good faith, giảm risk bị remove.
>
> KHI NÀO KHÔNG CẦN:
>   LessWrong — có drafts system, cứ post.
>   HN — không có culture pre-approval.
>   EA Forum — open submission.
>   r/slatestarcodex — community-driven, check rules rồi post.
>   r/MachineLearning — check rules, thêm [D] tag, post.
>   Bluesky/Mastodon — open platforms.
>
> NGUYÊN TẮC:
>   Intro NGẮN (2-3 câu). Mod bận.
>   Focus: content fit, KHÔNG phải effort/process.
>   KHÔNG nhắc cross-posting (trông như spam campaign).
>   Include FULL post content để mod judge chính xác.
>   "Happy to adjust" = show flexibility, good faith.

---

## Template

```
Subject: Checking if this post fits r/[SUBREDDIT]

Hi moderators,

I'd like to check whether this post would be appropriate for
r/[SUBREDDIT] before submitting.

It presents an open-source framework connecting neuroscience,
psychology, and evolutionary biology — with mechanistic answers
to specific questions, research citations, and explicit conditions
for being wrong. I thought r/[SUBREDDIT] would be a fitting
community given [REASON].

The post would look like this:

---

[PASTE CANONICAL POST FROM short-post-overview.md]

---

Happy to adjust to better fit the community's standards.
Thank you for your time.
```

---

## Per-Subreddit Adaptation

```
r/cogsci:
  REASON: "the cross-disciplinary nature (neuroscience × cognitive science)"
  NOTES: Academic community. Framework = cross-domain → fits cogsci scope.

r/neuroscience:
  REASON: "the neuroscience foundations — the framework builds on
           opioid, dopamine, and cortisol mechanisms with cited research"
  NOTES: Stricter about scientific rigor. Emphasize citations + falsifiability.

r/psychology (optional):
  REASON: "the behavioral predictions grounded in neuroscience mechanisms"
  NOTES: Broader audience. Check sub rules first — may not need mod message.

r/PhilosophyofMind (optional):
  REASON: "the architectural position on consciousness — PFC as observer,
           not controller — and its implications for free will and agency"
  NOTES: More philosophical. Framework's PFC position is directly relevant.
```

---

## Anti-Patterns

```
KHÔNG NÓI:
  ✗ "I spent 4 months full-time on this" — process, không relevant cho content fit
  ✗ "I'm posting this on multiple platforms" — trông như spam
  ✗ "Please approve my post" — mod không approve, họ chỉ nói fit hay không
  ✗ "This is revolutionary/groundbreaking" — overclaim, red flag cho mod
  ✗ "I'm not a neuroscientist but..." — defensive, không cần ở mod message
    (credential info đã nằm trong post body nếu mod đọc blog)

NÊN NÓI:
  ✓ Tóm tắt content 1-2 câu
  ✓ Lý do chọn sub cụ thể
  ✓ Include full post
  ✓ "Happy to adjust" — flexibility
```

---

## Checklist

```
□ Subject line rõ ràng: "Checking if this post fits r/[SUB]"
□ Intro ≤ 3 câu
□ REASON phù hợp với sub (xem Per-Subreddit Adaptation)
□ Full post content included
□ Không nhắc other platforms
□ Không nhắc time spent / effort
□ Không overclaim
□ "Happy to adjust" ở cuối
□ Proofread English
□ Đợi reply trước khi post (tối đa 7 ngày, nếu không reply → post)
```
