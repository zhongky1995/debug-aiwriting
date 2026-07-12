---
name: debug-aiwriting
description: Diagnose, rewrite, generate, and screen Chinese writing or creative ideas that should sound less AI-generated, less template-like, and more like a real author, brand, or consulting team. Use when the user asks to 去AI味, 消除AI味, 人味, AI腔, 机器味, 机翻腔, 白皮书腔, 高级空话, 套话太重, humanize Chinese writing, rewrite AI-generated Chinese drafts, 调整口径, 改口径, build or apply a personal/brand voice, 融合我的口吻, 学习我的表达习惯, apply previous Zhihu/Q&A writing samples, make my writing fit the scene and my habits, protect internal/external wording boundaries, 出创意, 创意方向, campaign ideas, slogan/theme/concept directions, or polish Chinese articles, social posts, client-facing proposals, strategy decks, integrated marketing plans, reports, emails, scripts, and public-facing copy while preserving meaning and facts.
---

# Debug AI Writing

## Core Principle

Optimize for real reader trust, not detector evasion. Preserve facts, intent, genre expectations, and the user's personal voice. Do not add mistakes, fake anecdotes, invented data, or excessive slang to make text appear "human."

Default behavior: fit the scene first, then apply the user's personal expression habits as a voice layer. Do not require the user to name a tone every time. Only override the personal voice when the user explicitly asks for another voice or when the situation demands a stricter register.

## Workflow

1. Identify the task type:
   - **Draft rewrite**: diagnose AI traces, rewrite with meaning preserved, then summarize the main edits.
   - **Generation from scratch**: infer purpose, reader, stance, evidence, and format before drafting. Ask only when missing information would change substance.
   - **Voice matching**: if the user provides samples, extract a temporary voice profile before writing.
   - **Reference-style alignment**: if the user says to "参考这版/按这个 PDF/照这个口径/像这份稿子", first extract a style contract from the reference before rewriting.
   - **Large-document rewrite**: if the artifact has multiple pages, sections, tables, slides, or repeated blocks, create a coverage map before editing and verify every surface after editing.
   - **Creative ideation**: use divergent directions and product-specific filtering internally; expose the full direction pool only when the user asks for creative directions or screening rationale.
   - **Audit only**: return concise issues and concrete line-level revision advice.
2. Classify the scene before writing: reader, relationship, channel, stakes, and desired action. If not specified, infer from the user's wording and the text itself.
3. Classify the genre: article, analysis/report, client-facing proposal/deck, sales material, social post, email, speech/script, product copy, internal comms, or translation.
4. For external-facing materials, anchor the reader and run the internal/external wording boundary check before final output.
5. If a reference artifact is provided, extract its style contract before choosing wording. Do not equate "remove AI tone" with "make it more colloquial"; preserve the reference's authority level, page rhythm, and professional vocabulary when those are part of the desired scene.
6. Apply the default personal voice profile from `references/zhihu-voice-profile.md` when the task is Chinese public writing, opinion writing, workplace/management/interview content, or when the user asks for "my writing/my tone." For formal client, report, or email contexts, keep the same decision logic but reduce bluntness and colloquial pressure.
7. For client-facing proposals or decks, rebuild the decision chain before line editing: client question -> diagnosis -> strategy -> mechanism -> execution/proof -> boundary. The goal is credible decision support, not a warmer service menu.
8. For marketing strategy proposals, KOC/UGC/community plans, integrated marketing decks, launch plans, or public-to-private-domain growth plans, use the professional marketing register: strategic terms are allowed when they name a page role, mechanism, metric, or execution object.
9. For large documents, make a page/section coverage map and edit by surface: document title, page titles, openings, tables, captions, footnotes, summary rows, and final notes. Do not stop after rewriting body paragraphs.
10. Apply a two-pass edit:
   - **Substance pass**: remove empty claims, surface the real point, add specificity only from provided context.
   - **Language pass**: reduce template transitions, corporate abstractions, over-balanced phrasing, and identical sentence rhythm.
11. Run the concrete-language and verifiable-action gates. Any sentence with framework nouns but no actor, action, object, or result must be rewritten before output. Any sentence that turns a desired result into a fake action must be rewritten into something observable.
12. Output in the user's requested format. If no format is specified:
   - For 口径修改, polishing, rewriting, or clean copy requests, provide the single best final version first. Do not expose brainstorming, scoring, or elimination steps unless useful for review.
   - For short text, provide the rewritten version first, then 1-3 concise notes only if they clarify a non-obvious choice.
   - For long text, provide the revised draft first; add a brief diagnosis only when the user needs editing rationale.
   - For external-facing drafts where review transparency matters, append a concise `【自检说明】`; omit it when the user asks for clean final copy only.
   - For explicit ideation requests, provide final directions plus a short `【筛选说明】`. Show the full raw 8-10 direction pool only when the user asks to see the process.

## Resource Use

- Read `references/ai-trace-checklist.md` when diagnosing a draft or doing final self-audit.
- Read `references/rewrite-playbook.md` when rewriting long text, matching a voice, or generating content from scratch.
- Read `references/client-proposal-playbook.md` when polishing or generating client-facing proposals, strategy decks, integrated marketing plans, CRM/private-domain/KOC/community/content-growth plans, or sales materials that must convince a client.
- Read `references/marketing-strategy-register.md` when the task involves marketing strategy decks, integrated marketing plans, launch plans, KOC/KOS/UGC/community operations, public-to-private-domain growth, search/content planning, or when the user says the output should sound like professional marketing planning rather than a plain execution memo.
- Read `references/reference-style-calibration.md` whenever the user provides or points to a reference draft/PDF/page/style and asks to follow its expression, logic,口径, or professional feel.
- Read `references/large-document-coverage.md` whenever rewriting more than one page/section, editing a deck-like document, replacing a Feishu/Docx document, or when the user says previous passes missed parts.
- Read `references/zhihu-voice-profile.md` by default for Chinese writing tasks where the user wants their own expression habits, practical workplace reasoning, Zhihu-style Q&A, public-facing articles, or any "write like me" request. Also use it as a light voice layer for other Chinese writing unless the context clearly requires a neutral institutional voice.
- Read `references/external-facing-check.md` for client emails, formal proposals, customer-facing decks, public releases, external statements, or any material where internal codes, metrics, names, unpublished data, or private judgments might leak.
- Read `references/creative-ideation-filter.md` when the user asks for creative directions, campaign concepts, slogans/themes, content topics, social ideas, proposal creative, brand activations, or any "出创意" task.
- Read `references/plain-language-gate.md` for final self-audit on formal reports, whitepaper/case writing, proposals, public-facing materials, or whenever the user says the output still has AI味, 空泛, 白皮书腔, 假大空, or "没修干净".

## Editing Rules

- Keep the original facts, names, numbers, claims, and logical direction unless the user asks for substantive rewriting.
- Replace vague evaluations with concrete consequences, scenarios, constraints, or examples already present in the source material.
- Prefer active verbs and clear actors over abstract nouns.
- Vary paragraph openings and sentence length; do not force symmetrical "first/second/finally" structures.
- Avoid overusing rhetorical pairs such as "不是...而是...", "既...又...", "不仅...更...", "一方面...另一方面..." unless the contrast is truly needed.
- Do not flatten all writing into casual internet tone. Business reports can remain professional; the goal is to remove hollow polish, not professionalism.
- Do not remove useful professional strategy language merely because it is abstract. Terms such as 目标拆解、策略总图、全域联动、节点样板、搜索占位、角色协同, or 内容矩阵 can stay when they define a real planning object and are supported by numbers, roles, stages, or execution proof.
- For proposals, keep every claim at the proof level available in the source: fact, inference, hypothesis, or suggested next step. Do not turn a weak reference into a guaranteed result.
- For external-facing materials, translate internal-only language into reader-facing language or delete it. Never expose internal codenames, internal KPIs, private names, unpublished data, or internal complaints unless the user explicitly approves disclosure.
- For creative ideation, do not stop at concept nouns. Every surviving idea must say what the user will do, see, feel, receive, or decide, and which product fact or audience scene makes it non-generic.
- Do not allow "高级空话" to pass just because it sounds professional. Terms such as 承接、整合、节点、触点、阵地、资产、沉淀、方法论、可复用、可迁移、经营、关系、链路、体系 must be tied to a concrete actor, action, object, timing, or result.
- Treat "abstract verb + abstract noun" as a high-risk pattern: 赋能增长、激活心智、撬动势能、释放价值、构建闭环、完成转化前置. Keep it only when the next sentence names the actual action.
- Do not replace one jargon phrase with another. Phrases such as 服务链路、沟通节奏、回访名单、接回链路、经营用户 sound unnatural unless the surrounding sentence says a normal person action such as "用户买完后知道去哪里咨询" or "快吃完时提醒补货."
- Treat unnatural verbs as more severe than abstract nouns. Verbs such as 接回、打通、沉淀、激活、撬动、承接、触达, when paired with the wrong object, create fake action. Prefer ordinary verbs such as 放、写、发、问、答、记、提醒、联系、回访、下单.
- Do not write desired results as if they were actions. "实现心智占位" or "完成用户教育" must become the repeated messages, channels, scenes, or page changes that a team can actually execute and observe.
- Every important claim should answer: who does it, what they do, to whom or what, when, and what visible change follows. If it cannot be assigned, observed, or checked, rewrite it.
- When the source is thin, say that stronger human texture requires more source material instead of inventing details.

## Voice Matching

When samples are available, extract only usable style anchors:

- stance: cautious, sharp, practical, narrative, analytical, intimate, restrained
- rhythm: short punchy sentences, medium explanatory paragraphs, long argument chains
- diction: plain, literary, industry-specific, colloquial, editorial
- structure: point-first, story-first, problem-solution, evidence-led
- banned habits: words, sentence patterns, punctuation, formatting, or tones the user dislikes

Apply the profile as constraints, not as imitation of a living writer unless the user owns or provides the writing as their own brand/persona.

When the user refers to their own prior Zhihu answers or asks to use "my tone," load `references/zhihu-voice-profile.md` and treat it as the default personal voice profile unless the current task provides a newer or narrower sample.

## Scene And Voice Priority

Use this priority order:

1. **Facts and intent**: do not change the user's meaning, claims, or evidence level.
2. **Scene fit**: adapt to reader, channel, stakes, and genre.
3. **Reference style contract**: if the user provides a reference, match its page role, authority level, rhythm, and professional vocabulary before line editing.
4. **External boundary**: remove or translate information the reader should not see.
5. **Personal voice**: apply the user's practical, direct, conditional reasoning style.
6. **Anti-AI cleanup**: remove template structure, empty abstractions, and false polish without lowering the professional register.

If scene and personal voice conflict, preserve the user's logic but adjust intensity. Example: in a client proposal, keep "先判断问题卡在哪，再谈动作" but avoid "这个想法很危险啊"; in a Zhihu answer, the sharper conversational opening is acceptable.

## Hidden Reasoning, Clean Output

Use the checklists as internal decision tools by default. The user usually needs the best version, not the whole working process.

- **Clean final mode**: for "改一下", "调整口径", "润色", "给我一版", "发客户", "改成对外表达", output only the revised copy unless there is a risky assumption.
- **Review mode**: for "帮我看看问题", "为什么这么改", "给我自检", append concise reasons or `【自检说明】`.
- **Ideation mode**: for "出几个方向", "给创意", "让我看筛选", show selected ideas and, when asked, the eliminated pool.

When using creative filtering behind a 口径修改 task, do not force multiple options. Use the filter to remove generic angles, then deliver the strongest single version.

## Final Self-Check

Before answering, check whether the output still contains:

- a generic opening that could fit any topic
- empty value words without examples
- mechanical transition phrases
- evenly sized paragraphs with identical rhythm
- a conclusion that restates the title instead of advancing the point
- claims stronger than the provided evidence
- when a reference style was requested: wording that is cleaner but no longer matches the reference's register, page rhythm, or professional vocabulary
- when editing a long document: untouched titles, table cells, captions, notes, or repeated blocks that still use the old口径
- for proposals: a service list without a client decision question, a mechanism without execution proof, or a case reference that does not say what it proves
- for external-facing materials: internal codenames, internal metrics, internal names, unpublished numbers, private complaints, or statements the reader cannot understand
- for creative ideas: concepts that still work unchanged for a competitor, directions not tied to a product fact or user scene, or names that sound good but do not make the user do/see/get anything
- professional-sounding filler such as 用户承接、内容整合、复购节点、服务角色、方法论沉淀、可迁移价值, unless the sentence says who does what to whom, when, and what changes
- abstract verb + abstract noun phrases such as 赋能增长、激活心智、撬动势能、释放价值、构建闭环, unless a concrete action immediately supports them
- replacement jargon such as 重新接回服务链路、进入沟通节奏、沉淀回访名单, when the same meaning can be said in plain Chinese
- unnatural verb-object pairs such as 重新接回用户/链路、打通触点、沉淀用户、激活关系、撬动复购, when a simpler verb can name the real action
- result-as-action phrases such as 实现心智占位、完成用户教育、实现转化闭环, when the sentence does not say what someone will actually do
- claims that cannot answer "怎么做、谁来做、做完看到什么变化"

Revise once if any of these are prominent.
