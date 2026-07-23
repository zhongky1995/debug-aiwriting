---
name: debug-aiwriting
description: Diagnose, rewrite, generate, and audit Chinese writing when the user asks to 去AI味, 消除AI味, 调整口径, 改口径, 去白皮书腔/套话/假大空, fix unnatural Chinese or verb-object pairs, rebuild a client deck whose 逻辑不闭环/故事线弱/观点堆叠/页面可互换, reduce identical persona voices or conclusion-heavy narration, match a personal/brand/reference style, protect internal/external wording boundaries, or screen generic creative ideas. Supports short copy; articles, novels and narrative nonfiction; whitepapers, cases and reports; emails and speeches; character/short-video/UGC/KOC/KOS scripts; client proposals, strategy decks, marketing plans, social content and internal SOPs. Preserve facts and evidence; for fiction also preserve point of view, character knowledge, plot causality and scene order unless structural rewriting is authorized.
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
   - **Fiction or narrative rewrite**: diagnose the scene engine, point of view, character knowledge, information release, dialogue action, world pressure, interiority, rhythm, and ending before treating the problem as word choice.
   - **Creative ideation**: use divergent directions and product-specific filtering internally; expose the full direction pool only when the user asks for creative directions or screening rationale.
   - **Audit only**: return concise issues and concrete line-level revision advice.
2. Set the rewrite scope before editing:
   - **L1 correction**: fix awkward wording, AI traces, and local collocation problems only.
   - **L2 language rewrite**: rewrite sentences and paragraphs while preserving facts, section/scene order, page or chapter roles, point of view, plot beats, and strategy.
   - **L3 structural rewrite**: reorder sections/scenes or rebuild page, argument, or scene logic without adding unsupported facts.
   - **L4 content development**: add analysis, methods, examples, scenes, character material, or creative content from available evidence.
   - Treat bare requests such as "优化口径/调整表达/去 AI 味" as L2. Do not enter L3 or L4 unless the user asks for restructuring, supplementation, or a new version. If an AI-like symptom comes from a scene, character, POV, or evidence problem that L2 cannot repair, fix what is in scope and state the upstream limitation instead of silently changing the story or argument.
3. Classify the scene before writing: reader, relationship, channel, stakes, desired action, and artifact function. If not specified, infer from the user's wording and the text itself.
4. Classify the genre and register: article, fiction/narrative nonfiction, analysis/report, executive update, whitepaper/case, client-facing proposal/deck, sales material, social post, email, speech/script, product copy, internal comms/SOP, or translation.
   - For fiction or narrative nonfiction, lock narrator/POV, narrative distance, time handling, genre promise, scene purpose, character desire and knowledge boundary before rewriting. Do not apply the business-writing actor/action gate to every narrative sentence.
   - For character, UGC, KOC, KOS, short-video, vlog, spoken-word, or TTS scripts, classify the speaker before rewriting: what they know, what they want, what just happened, what they would actually say aloud, and what should be left to the image. Then classify the scene mode separately; the same persona should not sound identical in a rushed pickup, a safety incident, a product test, and a relaxed outing.
5. For external-facing materials, anchor the reader and run the internal/external wording boundary check before final output.
6. If a reference artifact is provided, classify the requested reference dimension first: logic, structure, register, rhythm, wording, visual organization, or a combination. Extract a style contract only for those dimensions. Do not equate "remove AI tone" with "make it more colloquial."
7. Choose the scene register before running the plain-language gate. Judge every important sentence on two separate axes: meaning concreteness and register fit. A sentence can be concrete but too casual, or professional but empty; fix the failing axis only.
8. Load a personal voice profile only when the user asks for "my voice/my writing," provides samples, or the task explicitly calls for a known personal voice. Prefer `local/personal-voice-profile.md` when present. Otherwise build a temporary profile from the supplied samples; do not apply the bundled example as a default voice.
9. For client-facing proposals or decks, rebuild the decision chain only at L3 or L4: client question -> diagnosis -> strategy -> mechanism -> execution/proof -> boundary. At L1 or L2, diagnose weaknesses but preserve the existing decision chain unless a sentence cannot be repaired locally.
   - For a multi-page client deck at L3 or L4, read `references/client-deck-narrative-gate.md`. Create a narrative contract and causal page ledger before drafting page copy. Keep story, evidence, and visual-production status separate. Do not hand the deck to layout/build skills while the narrative gate is blocked.
10. For marketing strategy proposals, KOC/UGC/community plans, integrated marketing decks, launch plans, or public-to-private-domain growth plans, use the professional marketing register: strategic terms are allowed when they name a page role, mechanism, metric, or execution object.
11. For large documents, make a page/section coverage ledger and edit by surface: document title, page titles, openings, tables, captions, footnotes, summary rows, and final notes. Use `scripts/audit_surfaces.py` on supported text sources to inventory surfaces and residual high-risk phrases. Do not stop after rewriting body paragraphs.
    - For script banks, load `references/ugc-persona-script-register.md`, run source-integrity and duplicate preflight, calibrate anchor scripts with metadata hidden, and use `scripts/audit_ugc_scripts.py` when possible. Treat automated findings as diagnostic leads, not proof of natural speech.
12. Apply a three-pass edit:
   - **Substance/story pass**: for nonfiction, remove empty claims and surface the real point; for narrative, test scene change, character agency, POV, information boundaries, dialogue action, and earned consequences. Add specificity only from provided context.
   - **Language pass**: reduce template transitions, corporate abstractions, over-balanced phrasing, and identical sentence rhythm.
   - **Surface-residue pass**: after meaning and register are stable, check significance inflation, vague attribution, tail-end pseudo-analysis, copula avoidance, synonym cycling, false scope, collaboration residue, and formatting traces. Treat them as diagnostic signals, not a universal blacklist.
13. When the user flags a bad phrase, do not patch it locally and stop. Extract the general failure pattern, scan the entire current artifact and its live copy for analogous phrases, rewrite all matches, and treat the user's correction as a hard negative for the rest of the task.
14. Run the gate for the chosen genre. Apply the concrete-language and verifiable-action gates to explanatory claims, not mechanically to headings, labels, or narrative prose. For fiction, use the scene/POV/dialogue/interiority/whole-work gates in `references/fiction-narrative-register.md`.
15. Stop only when there are no unresolved high-severity language problems, all inventoried surfaces have been reviewed or explicitly excluded, facts and numbers still match the source, and the output remains in the intended register. For multi-page client decks at L3 or L4, also require narrative, evidence, and external-boundary gates to pass; mechanical export or visual polish alone is not completion. A writer's own `PASS` label is not evidence: run the adversarial merge/delete challenge in `references/client-deck-narrative-gate.md`, verify that result, process, implemented-system, and business-effect claims are not being promoted across evidence levels, and downgrade ambiguous results to `NEEDS_WORK` until independently reviewed or concretely defended.
16. Output in the user's requested format. If no format is specified:
   - For 口径修改, polishing, rewriting, or clean copy requests, provide the single best final version first. Do not expose brainstorming, scoring, or elimination steps unless useful for review.
   - For short text, provide the rewritten version first, then 1-3 concise notes only if they clarify a non-obvious choice.
   - For long text, provide the revised draft first; add a brief diagnosis only when the user needs editing rationale.
   - For external-facing drafts where review transparency matters, append a concise `【自检说明】`; omit it when the user asks for clean final copy only.
   - For explicit ideation requests, provide final directions plus a short `【筛选说明】`. Show the full raw 8-10 direction pool only when the user asks to see the process.

## Resource Use

- Read `references/ai-trace-checklist.md` when diagnosing a draft or doing final self-audit.
- Read `references/surface-trace-catalog.md` after the substantive rewrite for nonfiction, proposals, reports, public copy, emails, and social writing that still feels generated despite concrete wording. Use it only as the final surface pass; genre and evidence rules take priority.
- Read `references/rewrite-playbook.md` when rewriting long text, matching a voice, or generating content from scratch.
- Read `references/client-proposal-playbook.md` when polishing or generating client-facing proposals, strategy decks, integrated marketing plans, CRM/private-domain/KOC/community/content-growth plans, or sales materials that must convince a client.
- Read `references/client-deck-narrative-gate.md` whenever a client-facing deck has weak story logic, piled-up viewpoints, delayed proof, interchangeable pages, or a prior visual pass that did not improve persuasion.
- Read `references/marketing-strategy-register.md` when the task involves marketing strategy decks, integrated marketing plans, launch plans, KOC/KOS/UGC/community operations, public-to-private-domain growth, search/content planning, or when the user says the output should sound like professional marketing planning rather than a plain execution memo.
- Read `references/whitepaper-case-register.md` for public whitepapers, case studies, case submissions, industry reports with case evidence, or materials intended for later editorial extraction.
- Read `references/executive-report-register.md` for executive summaries, decision briefs, management updates, research conclusions, performance reviews, or data-led reports.
- Read `references/internal-ops-register.md` for internal execution plans, SOPs, project memos, meeting follow-ups, ownership tables, and operational handoffs.
- Read `references/fiction-narrative-register.md` for novels, short stories, narrative nonfiction, scene rewrites, dialogue/POV/description problems, fiction line editing, chapter endings, or feedback such as 人物太平, 对白同质, 描写观点性太强, 说教, 像按规则写出来, or 去抽象后发干.
- Read `references/ugc-persona-script-register.md` for character voice-over, short-video, UGC/KOC/KOS scripts, vlog narration, TTS copy, persona banks, or when the user says every persona sounds alike, the first-person voice is too conclusive, the ending always elevates the meaning, or the voice-over repeats the image.
- Read `references/reference-style-calibration.md` whenever the user provides or points to a reference draft/PDF/page/style and asks to follow its expression, logic,口径, or professional feel.
- Read `references/large-document-coverage.md` whenever rewriting more than one page/section, editing a deck-like document, replacing a Feishu/Docx document, or when the user says previous passes missed parts. For multi-chapter narrative, combine its inventory discipline with the whole-work tracks in `references/fiction-narrative-register.md`.
- Read `references/correction-propagation.md` whenever the user rejects a phrase or says a previous pass did not clean the same type of problem thoroughly.
- Read `local/personal-voice-profile.md` when it exists and the user explicitly requests their own voice. If it does not exist, use `references/personal-voice-profile-example.md` only as a schema for extracting a temporary profile from user-provided samples.
- Read `references/external-facing-check.md` for client emails, formal proposals, customer-facing decks, public releases, external statements, or any material where internal codes, metrics, names, unpublished data, or private judgments might leak.
- Read `references/creative-ideation-filter.md` when the user asks for creative directions, campaign concepts, slogans/themes, content topics, social ideas, proposal creative, brand activations, or any "出创意" task.
- Read `references/plain-language-gate.md` for final self-audit on formal reports, whitepaper/case writing, proposals, public-facing nonfiction, or when the user says such material still has AI味, 空泛, 白皮书腔, 假大空, or "没修干净". Do not use it as the acceptance gate for fiction; use `references/fiction-narrative-register.md` instead.

## Editing Rules

- Keep the original facts, names, numbers, claims, and logical direction unless the user asks for substantive rewriting.
- Never invent dates, quantities, product features, research samples, quotations, reactions, anecdotes, or personal experience to make an abstract sentence sound specific. Narrow, qualify, or delete the claim when the source cannot support a concrete replacement.
- Replace vague evaluations with concrete consequences, scenarios, constraints, or examples already present in the source material.
- Prefer active verbs and clear actors over abstract nouns when the sentence describes an action or causal claim. Do not force every professional heading or table label into conversational full sentences.
- Vary paragraph openings and sentence length; do not force symmetrical "first/second/finally" structures.
- Avoid overusing rhetorical pairs such as "不是...而是...", "既...又...", "不仅...更...", "一方面...另一方面..." unless the contrast is truly needed.
- Do not flatten all writing into casual internet tone. Business reports can remain professional; the goal is to remove hollow polish, not professionalism.
- Do not inject first person, humor, slang, digressions, deliberate messiness, or emotional ambivalence merely to make text feel human. Voice must come from the requested scene, supplied samples, and the writer's actual stance.
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
- For narrative writing, preserve POV and character knowledge. Do not let the narrator, a witness, or an ordinary character explain more than they know, can say, want to say, or can naturally articulate in the moment.
- Treat key dialogue as verbal action: identify what the speaker wants, why they cannot say it directly, the strategy they use, the response it produces, and what changes after the line. Do not make every character equally lucid, witty, restrained, or thematic.
- Replace author judgment with scene evidence only when the replacement belongs to the viewpoint and changes attention, action, relationship, information, or pressure. Do not scatter random gestures, scenery, and symbolic objects merely to avoid psychological or abstract words.
- Keep earned interiority. A short thought or abstraction may stay when it is available to the viewpoint character, supported by prior scene evidence, and does not finish the reader's interpretation. Do not treat “意识到/明白/其实/真正” or any keyword count as a mechanical delete list.
- For narrative writing, distinguish the last chronological event from the narrative endpoint. End on the last meaningful change, decision, reaction, image, or unresolved question; remove routine logistics after that point unless they add a real consequence. Vary chapter endings; do not replace every summary with the same object close-up or clipped epiphany.
- For character, UGC, KOC, KOS, short-video, vlog, spoken-word, or TTS scripts, apply the detailed speaker, spoken-Chinese, image/voice, provenance, and ending checks in `references/ugc-persona-script-register.md`. Do not apply script-only rules to reports, proposals, articles, emails, or other genres.

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
- for multi-page client decks: no single reader question, no mother claim, proof appearing too late, more than two consecutive theory pages, pages that can be swapped or removed without changing the argument, a case used only to decorate a prior claim, or a closing page that merely repeats terminology
- for external-facing materials: internal codenames, internal metrics, internal names, unpublished numbers, private complaints, or statements the reader cannot understand
- for creative ideas: concepts that still work unchanged for a competitor, directions not tied to a product fact or user scene, or names that sound good but do not make the user do/see/get anything
- professional-sounding filler such as 用户承接、内容整合、复购节点、服务角色、方法论沉淀、可迁移价值, unless the sentence says who does what to whom, when, and what changes
- abstract verb + abstract noun phrases such as 赋能增长、激活心智、撬动势能、释放价值、构建闭环, unless a concrete action immediately supports them
- replacement jargon such as 重新接回服务链路、进入沟通节奏、沉淀回访名单, when the same meaning can be said in plain Chinese
- unnatural verb-object pairs such as 重新接回用户/链路、打通触点、沉淀用户、激活关系、撬动复购, when a simpler verb can name the real action
- result-as-action phrases such as 实现心智占位、完成用户教育、实现转化闭环, when the sentence does not say what someone will actually do
- claims that cannot answer "怎么做、谁来做、做完看到什么变化"
- for fiction/narrative: plot moved by author convenience rather than character choice; POV or knowledge leakage; explanatory dialogue; interchangeable voices; decorative world detail; moralized psychology; an over-innocent narrator protected from consequential choices; or mechanical action/object endings introduced by over-cleaning
- for character/UGC scripts only: interchangeable persona voices, hidden moral conclusions, image/voice duplication, forced narration, invented details, or a routine final action added after the real narrative endpoint
- for nonfiction and public-facing copy: inflated historical or industry significance, unnamed authority, sentence tails that add unsupported meaning, avoidance of simple `是/有/包括`, terminology drift caused by synonym cycling, false `从 A 到 B` ranges, assistant-chat residue, or formatting used as a substitute for hierarchy

Continue revising until no high-severity item remains. For long documents, do not claim completion while any inventoried surface is unreviewed; report unreadable or intentionally excluded surfaces explicitly.
