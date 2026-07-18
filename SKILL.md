---
name: debug-aiwriting
description: Diagnose, rewrite, generate, and audit Chinese writing when the user explicitly asks to 去AI味, 消除AI味, 调整口径, 改口径, 去掉白皮书腔/套话/假大空, fix unnatural Chinese or verb-object pairs, reduce identical AI-sounding persona voices or conclusion-heavy first-person narration, match a personal/brand/reference style, protect internal/external wording boundaries, or screen creative directions for generic AI-like ideas. Supports short copy and large multi-page articles, whitepapers, case studies, reports, emails, speeches, character scripts, short-video/UGC/KOC/KOS voice-over scripts, client proposals, strategy decks, integrated marketing plans, social content, and internal SOPs while preserving facts, rewrite scope, scene register, persona differences, and full-document coverage.
---

# Debug AI Writing

## Core Principle

Optimize for real reader trust, not detector evasion. Preserve facts, intent, genre expectations, and the user's personal voice. Do not add mistakes, fake anecdotes, invented data, or excessive slang to make text appear "human."

Default behavior: fit the scene first. Apply a personal or brand voice only when the user asks for it, provides samples, or a local profile exists and the request clearly calls for that voice. Do not let an optional personal profile override the artifact's professional register.

## Workflow

1. Identify the task type:
   - **Draft rewrite**: diagnose AI traces, rewrite with meaning preserved, then summarize the main edits.
   - **Generation from scratch**: infer purpose, reader, stance, evidence, and format before drafting. Ask only when missing information would change substance.
   - **Voice matching**: if the user provides samples, extract a temporary voice profile before writing.
   - **Reference-style alignment**: if the user says to "参考这版/按这个 PDF/照这个口径/像这份稿子", first extract a style contract from the reference before rewriting.
   - **Large-document rewrite**: if the artifact has multiple pages, sections, tables, slides, or repeated blocks, create a coverage map before editing and verify every surface after editing.
   - **Creative ideation**: use divergent directions and product-specific filtering internally; expose the full direction pool only when the user asks for creative directions or screening rationale.
   - **Audit only**: return concise issues and concrete line-level revision advice.
2. Set the rewrite scope before editing:
   - **L1 correction**: fix awkward wording, AI traces, and local collocation problems only.
   - **L2 language rewrite**: rewrite sentences and paragraphs while preserving facts, section order, page roles, and strategy.
   - **L3 structural rewrite**: reorder sections or rebuild page logic without adding unsupported facts.
   - **L4 content development**: add analysis, methods, examples, or creative content from available evidence.
   - Treat bare requests such as "优化口径/调整表达/去 AI 味" as L2. Do not enter L3 or L4 unless the user asks for restructuring, supplementation, or a new version.
3. Classify the scene before writing: reader, relationship, channel, stakes, desired action, and artifact function. If not specified, infer from the user's wording and the text itself.
4. Classify the genre and register: article, analysis/report, executive update, whitepaper/case, client-facing proposal/deck, sales material, social post, email, speech/script, product copy, internal comms/SOP, or translation.
   - For character, UGC, KOC, KOS, short-video, vlog, spoken-word, or TTS scripts, classify the speaker before rewriting: what they know, what they want, what just happened, what they would actually say aloud, and what should be left to the image.
5. For external-facing materials, anchor the reader and run the internal/external wording boundary check before final output.
6. If a reference artifact is provided, classify the requested reference dimension first: logic, structure, register, rhythm, wording, visual organization, or a combination. Extract a style contract only for those dimensions. Do not equate "remove AI tone" with "make it more colloquial."
7. Choose the scene register before running the plain-language gate. Judge every important sentence on two separate axes: meaning concreteness and register fit. A sentence can be concrete but too casual, or professional but empty; fix the failing axis only.
8. Load a personal voice profile only when the user asks for "my voice/my writing," provides samples, or the task explicitly calls for a known personal voice. Prefer `local/personal-voice-profile.md` when present. Otherwise build a temporary profile from the supplied samples; do not apply the bundled example as a default voice.
9. For client-facing proposals or decks, rebuild the decision chain only at L3 or L4: client question -> diagnosis -> strategy -> mechanism -> execution/proof -> boundary. At L1 or L2, diagnose weaknesses but preserve the existing decision chain unless a sentence cannot be repaired locally.
10. For marketing strategy proposals, KOC/UGC/community plans, integrated marketing decks, launch plans, or public-to-private-domain growth plans, use the professional marketing register: strategic terms are allowed when they name a page role, mechanism, metric, or execution object.
11. For large documents, make a page/section coverage ledger and edit by surface: document title, page titles, openings, tables, captions, footnotes, summary rows, and final notes. Use `scripts/audit_surfaces.py` on supported text sources to inventory surfaces and residual high-risk phrases. Do not stop after rewriting body paragraphs.
    - For script banks, inventory every title, persona line, voice direction, full-script paragraph, shot table, voice-over cell, on-screen caption, and ending. Use `scripts/audit_ugc_scripts.py` for `.docx` script banks when possible; keep duplicate full-script and shot-table versions synchronized.
    - Do not treat a clean automated report as proof that the scripts sound human. The report locates patterns; acceptance still requires line-level spoken-Chinese, hidden-thesis, persona-swap, image/voice, and slot-pressure checks.
    - For each shot row, explicitly decide whether it needs voice-over, can rely on the image, should carry ambient sound or a pause, or should continue the previous sentence. A populated table is not a quality goal.
12. Apply a two-pass edit:
   - **Substance pass**: remove empty claims, surface the real point, add specificity only from provided context.
   - **Language pass**: reduce template transitions, corporate abstractions, over-balanced phrasing, and identical sentence rhythm.
13. When the user flags a bad phrase, do not patch it locally and stop. Extract the general failure pattern, scan the entire current artifact and its live copy for analogous phrases, rewrite all matches, and treat the user's correction as a hard negative for the rest of the task.
14. Run the concrete-language and verifiable-action gates in the chosen register. Apply actor/action requirements to explanatory claims, not mechanically to short headings, navigation labels, or table headers whose meaning is supported by the surrounding page.
15. Stop only when there are no unresolved high-severity language problems, all inventoried surfaces have been reviewed or explicitly excluded, facts and numbers still match the source, and the output remains in the intended register.
16. Output in the user's requested format. If no format is specified:
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
- Read `references/whitepaper-case-register.md` for public whitepapers, case studies, case submissions, industry reports with case evidence, or materials intended for later editorial extraction.
- Read `references/executive-report-register.md` for executive summaries, decision briefs, management updates, research conclusions, performance reviews, or data-led reports.
- Read `references/internal-ops-register.md` for internal execution plans, SOPs, project memos, meeting follow-ups, ownership tables, and operational handoffs.
- Read `references/ugc-persona-script-register.md` for character voice-over, short-video, UGC/KOC/KOS scripts, vlog narration, TTS copy, persona banks, or when the user says every persona sounds alike, the first-person voice is too conclusive, the ending always elevates the meaning, or the voice-over repeats the image.
- Read `references/reference-style-calibration.md` whenever the user provides or points to a reference draft/PDF/page/style and asks to follow its expression, logic,口径, or professional feel.
- Read `references/large-document-coverage.md` whenever rewriting more than one page/section, editing a deck-like document, replacing a Feishu/Docx document, or when the user says previous passes missed parts.
- Read `references/correction-propagation.md` whenever the user rejects a phrase or says a previous pass did not clean the same type of problem thoroughly.
- Read `local/personal-voice-profile.md` when it exists and the user explicitly requests their own voice. If it does not exist, use `references/personal-voice-profile-example.md` only as a schema for extracting a temporary profile from user-provided samples.
- Read `references/external-facing-check.md` for client emails, formal proposals, customer-facing decks, public releases, external statements, or any material where internal codes, metrics, names, unpublished data, or private judgments might leak.
- Read `references/creative-ideation-filter.md` when the user asks for creative directions, campaign concepts, slogans/themes, content topics, social ideas, proposal creative, brand activations, or any "出创意" task.
- Read `references/plain-language-gate.md` for final self-audit on formal reports, whitepaper/case writing, proposals, public-facing materials, or whenever the user says the output still has AI味, 空泛, 白皮书腔, 假大空, or "没修干净".

## Editing Rules

- Keep the original facts, names, numbers, claims, and logical direction unless the user asks for substantive rewriting.
- Replace vague evaluations with concrete consequences, scenarios, constraints, or examples already present in the source material.
- Prefer active verbs and clear actors over abstract nouns when the sentence describes an action or causal claim. Do not force every professional heading or table label into conversational full sentences.
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
- Treat unnatural verbs as more severe than abstract nouns. Verbs such as 接回、打通、沉淀、激活、撬动、承接、触达 create fake action when paired with objects they do not naturally take. Prefer the most natural verb for the scene; ordinary verbs are often better for execution copy, while precise professional verbs may remain in strategy or analytical writing.
- Do not write desired results as if they were actions. "实现心智占位" or "完成用户教育" must become the repeated messages, channels, scenes, or page changes that a team can actually execute and observe.
- Every important claim should answer: who does it, what they do, to whom or what, when, and what visible change follows. If it cannot be assigned, observed, or checked, rewrite it.
- In character scripts, do not use first person as a universal conclusion machine. Prefer first person for actions, perceptions, partial judgments, hesitation, mistakes, and immediate reactions. Treat lines such as "我终于明白 / 对我来说 / 最重要的是 / 这才是 / 真正的 X 是" as high risk unless that exact speaker has earned the conclusion through the scene and would naturally say it aloud.
- Do not define a persona only with identity and values. Give each recurring speaker a language system: sentence length, vocabulary, attention pattern, knowledge limit, emotional temperature, and what they avoid saying. If scripts remain interchangeable after persona labels are removed, rewrite them.
- Keep image and voice complementary. Let the image carry visible facts and actions; let voice add motive, uncertainty, off-camera context, or reaction. Delete voice-over that merely narrates the frame.
- Do not confuse concrete details with natural speech. A list of parking, elevator, aisle seat, and break arrangements is still report copy when the person has no reason to recite the list. Keep only the detail the speaker would mention in that moment; leave the rest to the image or shot notes.
- After removing an explicit lesson, run a hidden-thesis check. Reject polished action pairs and slogan-like summaries that continue to advertise the speaker's respect, fairness, independence, taste, or family values, such as “路线由我安排，座位让他自己挑” or “分两天，座位舒服，聊天从容.”
- Do not force narration into every time-coded row. Empty voice-over cells, ambient sound, pauses, short quotes, and sentences spanning multiple shots are valid. Never compress leftover facts into a slogan merely to fill a slot.
- Read every surviving voice-over line aloud without the persona label or shot description. Repair unnatural collocations such as “把兴趣问清”“遇到现场演出”“只扶手肘”“订一顿午餐,” report-style lists, and overly balanced clauses. Adding sentence particles does not fix written syntax.
- Do not force every short-video script to end with a takeaway or audience question. A concrete action, quote, unfinished reaction, or visual beat can end the script. Keep a question only when this speaker would plausibly ask it and the preceding scene creates a specific answer space.
- Do not invent "human texture." Every added quote, action, object, location, number, reaction, or relationship detail must already appear in the source material or an approved fact sheet. If the source does not support a scene-specific replacement, delete the generic conclusion, narrow the claim, or mark the missing source; never fabricate a vivid ending to make the script feel real.
- When the source is thin, say that stronger human texture requires more source material instead of inventing details.

## Voice Matching

When samples are available, extract only usable style anchors:

- stance: cautious, sharp, practical, narrative, analytical, intimate, restrained
- rhythm: short punchy sentences, medium explanatory paragraphs, long argument chains
- diction: plain, literary, industry-specific, colloquial, editorial
- structure: point-first, story-first, problem-solution, evidence-led
- banned habits: words, sentence patterns, punctuation, formatting, or tones the user dislikes

Apply the profile as constraints, not as imitation of a living writer unless the user owns or provides the writing as their own brand/persona.

When the user refers to their own prior writing or asks to use "my tone," load `local/personal-voice-profile.md` when available. If the current task provides newer or narrower samples, treat those samples as higher priority.

## Scene And Voice Priority

Use this priority order:

1. **Facts and intent**: do not change the user's meaning, claims, or evidence level.
2. **Scene fit**: adapt to reader, channel, stakes, and genre.
3. **Reference dimension and style contract**: match only the logic, structure, register, rhythm, wording, or visual organization the user intends to borrow.
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
- for character/UGC scripts: first-person lines that summarize the writer's lesson instead of the character's live experience; different personas that still share the same syntax, values, and endings; voice-over that duplicates the image; forced comment questions; or conclusions that can be deleted without losing the scene
- for character/UGC scripts: implicit moral summaries that survive after explicit lesson words are removed; polished action pairs that could serve as poster copy; report-style detail lists; unnatural verb-object relations; or a voice-over sentence forced into every time-coded row
- for character/UGC rewrites: new dialogue, behavior, props, locations, numbers, product reactions, or emotional details that cannot be traced to the supplied script, shot list, persona card, or fact sheet

Continue revising until no high-severity item remains. For long documents, do not claim completion while any inventoried surface is unreviewed; report unreadable or intentionally excluded surfaces explicitly.
