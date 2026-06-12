# [POST] How Valuable Are Weak AI Safety Regulations?

> **Platform:** LessWrong
> **Link:** https://www.lesswrong.com/posts/peHyxRozoQbcMSzxm/how-valuable-are-weak-ai-safety-regulations
> **Author:** MichaelDickens
> **Ngày post:** 8th Jun 2026
> **Ngày lưu:** 2026-06-09
> **Ghi chú:** Full content. File này = reference only, không edit.

---

## BÀI VIẾT GỐC

To prevent superintelligent AI from killing everyone, I would like there to be a strong international agreement banning the development of ASI until it can be proven safe. But that sort of agreement requires a lot of political buy-in and coordination. In the meantime, it may be easier to get light-touch AI safety regulations passed. To what extent do weak regulations decrease extinction risk?

In this post:

- Part I discusses routes by which weak regulations can reduce extinction risk.
- Part II considers some downsides of weak regulations.
- Part III reviews specific categories of weak regulation and how they might reduce risk.

*Cross-posted from my website.*

### I. Ways weak regulations can reduce risk

#### Directly reduce extinction risk

Weak regulations can't do much to decrease misalignment risk, but they can have small effects at the margin. GPU tariffs or moderate restrictions on GPU exports slow down AI development in other countries, and reduce competitive pressure to some extent. Mandatory safety testing has some small chance of catching catastrophic issues before they happen.

#### Empower future efforts to reduce extinction risk

What I really want is a global ban on superintelligent AI until it can be proven safe. To get that, we will need some regulations along the way. For example, regulators will need to know who has the ability to develop advanced AI systems, which means we need some sort of monitoring of AI developers or AI hardware.

#### Reveal warning shots

At some point before AI kills everyone, it might do something scary enough to trigger governments to pause AI. Weak regulations can make warning shots more apparent. If AI companies are required to publish safety tests, and there are legally mandated whistleblower protections, then it's more likely that scary AI behaviors will come to light.

#### Shift the Overton window

Passing weak regulations in the near future may make politicians more amenable to strong regulations later on. (I say "politicians" rather than "people" because the general public already supports strong regulations on AI.)

Unfortunately, it's not clear that that's how it works—that small changes beget large changes. When I did a brief literature review, the results looked inconclusive. I can come up with examples of times when weak regulations were followed by strong regulations, and also times when they weren't. Beyond that, there's the causality problem: did weak regulations *cause* strong regulations, or were both caused by a trend in societal attitudes?

To my knowledge, the most rigorous (read: least-unrigorous) relevant research is Beaman et al. (1983), a meta-analysis on the foot-in-the-door effect. The paper found that the evidence on the effect was mixed, and sometimes pointed in the wrong direction.

### II. Downsides of weak regulations

#### Opportunity cost

Time spent advocating for weak regulations could be spent advocating for *strong* regulations instead, which may be better. In fact, I think it probably *is* better, because (1) weak regulations are unlikely to prevent extinction on their own, and (2) we might not have much time before superintelligent AI is upon us.

But there are situations where advocating for weak regulations does not have any opportunity cost. If I publicly voice support for SB 53 or the RAISE Act, I'm not crowding out some stronger bill that those bills are competing with. They're not competing with any other bills.

If you're an AI safety org that spends most of its time advocating for strong measures, it costs you little to issue a statement in support of those bills, and indeed many orgs did do that.

#### Regulation fatigue

Weak regulations might beget strong regulations by shifting the Overton window. Alternatively, they might *reduce* the appetite for regulation: "we already have these rules in place, why do we need more?" As discussed above, the evidence is not clear on which direction the effect goes (if either).

#### Slows technological progress

All else equal, technological progress is good, and increases prosperity. Technological progress toward a thing that kills everyone is bad, but there will be good parts along the way. Slowing AI development means we get less of those good parts.

The reduction in extinction risk easily justifies the cost, but this is a real downside.

(This is a downside relative to *no regulations*, but not relative to strong regulations, which would slow progress by even more.)

#### May get in the way of AI companies implementing their own, more sensible, self-regulations

AI company leaders would have us believe this is the reason they've lobbied against regulations. I find it hard to believe that they will do the right thing on their own, and their track records are not promising.

### III. Specific policies, and how they might reduce extinction risk

This section reviews some light-touch policies and possible paths to impact for each of them.

#### GPU export controls

- Path 1: Reduce AI proliferation → reduce competitive pressure → make it easier to coordinate a pause.
- Path 2: Slow down AI development in other countries → lengthen AI timelines → provide more time to work on safety.

Export controls are the closest thing to free win. AI safety advocates like them *and* accelerationists like them. The only powerful interest group that dislikes them is GPU manufacturers.

A possible counter-argument is that export controls incentivize companies in foreign countries to develop their own manufacturing pipelines, which would ultimately worsen race dynamics. That sounds too much like 4D chess thinking to me—as a rule, making things harder does not make things easier.

#### Establishment of an AI safety standards body

- Path 1: Create a public "state of the art" on AI safety → companies can more easily adopt good practices → companies can behave more safely.
- Path 2: Establish an answer to the question of who will oversee AI companies' safety practices, in case future regulations mandate oversight.
- Path 3: Help clarify what flavors of regulation would be helpful → future (hopefully strong) regulations can be better targeted at reducing the serious risks.

The UK has the AI Security Institute; other countries could create something similar.

#### Dangerous capability evaluations

- Path 1: Get better information about models' capabilities → policy-makers and the public can better see the dangers that AI poses.
- Path 2: Get better information about models' capabilities → we can use that information as an input to later, stronger regulations that have hard shutdown requirements when models meet certain criteria.

Evals are overrated by many in the AI safety community, but this still seems like one of the better things governments can do with light-touch regulations.

Some concerns with evals:

- You can't just evaluate models, you have to actually figure out how to make them safe.
- Evals don't work when models know they're being evaluated, which is becoming increasingly the case. (This was predictably going to be a problem—surely a superhuman AI would be superhumanly shrewd at detecting when it's being tested.)
- Evals give AI companies an optimization target.

#### Mandatory publication of safety frameworks

- Path 1: Require AI companies to actually have safety frameworks → they are now marginally safer.
- Path 2: Allow safety frameworks to be inspected by governments or the public → enable pressure on companies to improve their frameworks.

This is only a minor win, since most frontier AI companies already publish safety frameworks, their frameworks are woefully inadequate to prevent human extinction, and the frameworks will be dropped when inconvenient anyway. Requiring AI companies to publish *and follow* safety frameworks may be better, or it may induce them to publish toothless frameworks so that they're not beholden to anything.

#### Mandatory advance disclosure of large training runs

- Path 1: Ensure governments are aware of when AI companies are doing new training runs → ??

I've heard this idea proposed before, but I don't have much grasp on what it's meant to accomplish. If governments impose restrictions on what kinds of training AI companies can do, then disclosure is a necessary prerequisite; but what does disclosure *on its own* do? Perhaps I'm missing something here. Still, mandatory disclosure doesn't seem meaningfully *bad* in any way.

#### Whistleblower protections

- Path 1: Make it easier for whistleblowers to come forward → expose dangerous behavior within AI companies → increase political will for strong regulations.

This is another free win, although the ultimate effect on extinction risk seems small—it provides a little more incremental evidence of AI companies' misbehavior.

#### Incident reporting

- Path 1: Learn about scary incidents → policy-makers and the public can better see the dangers that AI poses.

This seems less promising than capability evals because it relies too much on luck: there might not be any incidents, the incidents might go undetected, or they might occur after it's already too late.

#### Security requirements to prevent model theft

- Path 1: Ensure competitors can't catch up by directly copying leaders' models → reduced competitive pressure → easier to coordinate around slowing down AI.
- Path 2: Ensure rogue actors can't steal model weights → reduce misuse risk.

Security requirements would be very good if feasible, but I'm not sure that requirements with teeth would qualify as "weak". For the requirements to be effective, they'd need to be highly restrictive. Even then, the state of the art in cybersecurity is not good enough to prevent sophisticated thieves from getting their hands on model weights.

### My position on weak regulations

With all that in mind, what do I believe?

In brief:

- Weak AI regulations are good. I'm happy when policy-makers propose them, I'm happy when people campaign for them, and I'm even happier when they get signed into law.
- Strong regulations are a lot better. Inasmuch as I can influence marginal policy efforts, I'd prefer to push for stronger regulations.

I'm sympathetic to the view that weak regulations matter more right now—the arguments in favor of my view are far from definitive. And if you work in the policy world, whether you work on weak or strong regulations probably has less to do with what's better in the abstract, and more to do with your particular situation.

---

## FOOTNOTES

1. US competitive pressure from domestic AI companies not addressed by export restrictions
2. Small chance of catching extinction-level dangers; superintelligent AI could fool safety tests
3. Warning shots cannot be relied upon but preparation is warranted
4. Reference to Beaman et al. (1983) meta-analysis on foot-in-the-door effect
5. Risk of muddling message about global AI halt preference

---

## COMMENTS

*(0 comments visible tại thời điểm lưu — 2026-06-09)*
