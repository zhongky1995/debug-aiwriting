---
name: debug-aiwriting
description: Diagnose, generate, rewrite, and audit Chinese writing for 去AI味、调整口径、内容凝聚、主线与结构修复、反复修改跑偏, genre-specific professional quality, and personal/reference voice alignment. Use for short copy, articles, reports, proposals/decks, scripts, and narrative work. Preserve evidence, authorized scope, genre, and whole-artifact effectiveness; do not reduce writing quality to surface polish.
---

# Debug AI Writing

## Core Principle

Optimize for the intended reader outcome and reader trust, not detector evasion. Treat the artifact as a whole: analysis may separate problems, but drafting must integrate their solutions and revision must improve the complete work. Surface cleanup follows substantive decisions.

Scale effort to the coupling of decisions, not output length. A short notice or headline can require substantial selection and synthesis; a typo correction does not need a production plan. Coverage of every passage is necessary but does not establish overall effectiveness.

For important explanatory claims, make clear enough of this chain for the sentence's role: **who acts or claims -> based on what -> does what -> to which object -> under what condition -> what visible change or decision follows**. If the source cannot support a concrete claim, narrow it, label the uncertainty, or delete it. Never invent specificity.

For nonfiction, including short expert commentary, the requested depth and length must be earned by material and reasoning. A new paragraph should add a supported fact, action, distinction, condition, consequence, decision, or useful question. An illustrative example may clarify a possibility; it does not establish its prevalence, cause, or benefit. When the material is thin, research, ask, narrow, or shorten instead of padding.

Information gain and continuity are separate checks. In explanatory prose, the reader should understand why the next sentence or paragraph follows without having to invent a missing premise. Preserve necessary reasoning and transitions while removing repeated conclusions.

For fiction and narrative work, preserve point of view, character knowledge, motive, causality, information release, scene order, and earned interiority unless structural rewriting is authorized. Do not force narrative prose through a business-writing actor/action template.

Fit the actual scene. Professional writing may remain professional; personal writing may retain first person. Do not add humor, slang, anecdotes, mistakes, deliberate disorder, or emotional ambivalence merely to appear human.

## Scope Contract

Classify the task before editing:

| Level | Allowed change |
| --- | --- |
| `L1` | Correct awkward wording, collocation, grammar, repetition, and local AI traces. |
| `L2` | Rewrite sentences and paragraphs while preserving facts, page/section/scene roles, order, POV, plot beats, and strategy. |
| `L3` | Reorder or rebuild argument, page, chapter, or scene logic without unsupported facts. |
| `L4` | Develop new analysis, methods, examples, scenes, or creative directions from available evidence. |

Treat bare requests such as “优化口径、调整表达、去 AI 味” as `L2`. Do not enter `L3` or `L4` without authorization. If a language symptom comes from an upstream structure, evidence, character, or scene problem that is outside scope, repair what is allowed and state the limitation.

Authorization follows the user's actual request and earlier decisions, not a required level label: “重组主线/重写结构” authorizes the corresponding L3 work; a request to develop new content authorizes the needed L4 work within its stated bounds. Do not ask again merely because the user did not say “L3”. Global review itself is allowed at every level; changes still respect scope.

Task modes:

- **Rewrite**: deliver the revised text, then brief notes only when useful.
- **Generation**: establish purpose, reader, stance, evidence, and format before drafting.
- **Voice/reference alignment**: extract only the requested dimensions before rewriting.
- **Audit only**: identify problems and revision moves; do not silently replace the draft.
- **Creative ideation**: filter generic directions internally; show the raw pool only when requested.

## Workflow

1. **Establish the current writing basis**: infer reader, genre, purpose, facts, evidence, and scope from available context. For coupled writing decisions, retain a compact basis: intended reader outcome; indispensable facts/relationships and uncertainty; tradeoff priorities; organizing approach. Keep it current across turns. Explicit changes to purpose update it; local feedback does not silently replace it. Keep this internal unless the user asks for planning or a material ambiguity needs resolving.
2. **Choose professional criteria**: select references below by communicative function as well as channel. For generation, authorized structural work, tightly coupled short copy, or revision drift, read [Whole-Artifact Writing](references/whole-artifact-writing.md). Determine what decisions must be made and what would make them inadequate; headings and step names alone are not evidence of completed work.
3. **Diagnose the governing problem**: locate the largest obstacle to the reader outcome at the task, material, structure, scene, or expression level. Resolve it within scope before polishing. Missing evidence can require narrowing the claim or revising the plan; a transition cannot repair an unrelated section.
4. **Compose and revise under that diagnosis**: integrate one coherent solution for the target length. Work on substance/story, then language, then surface residue; return upstream if a later pass exposes an earlier failure. Preserve useful existing text. For explanatory prose apply the [Adjacent-Passage Continuity Gate](references/core-quality-gates.md#adjacent-passage-continuity-gate), alongside whole-artifact review.
5. **Handle feedback without drift**: diagnose what the feedback changes and what must remain valid; use `references/correction-propagation.md` for analogous failures. Expand edits to their actual dependencies, within authorization. Compare the complete candidate with the previous viable draft: what improved, what was lost, whether the tradeoff serves the current basis. Retain or restore the better version; explicit factual corrections remain mandatory.
6. **Verify the actual reading and coverage**: read the complete artifact using only the background its intended reader has. Identify the understanding, action, or narrative effect the text actually produces, then compare it with the writing basis. Do not use planning notes to fill gaps. Inspect required titles, body, tables, captions, notes, and embedded text; disclose inaccessible surfaces.
7. **Stop when fit for use**: required constraints and reader outcome are satisfied, material supports the length, and no significant issue remains within scope. Do not iterate for synonymous preferences or declare success from a blacklist or checklist alone. If an upstream issue cannot be repaired within scope or available evidence, deliver permitted work and state the specific limitation.

## Routing Matrix

| Task condition | Primary reference | Add only when needed |
| --- | --- | --- |
| Nonfiction, product copy, email, translation, general rewrite | `references/core-quality-gates.md` | `references/rewrite-playbook.md` for long rewriting, generation, or voice extraction |
| Client proposal, sales material, strategy presentation | `references/client-proposal-playbook.md` | `references/client-deck-narrative-gate.md` only for multi-page `L3/L4` story repair |
| Marketing, launch, KOC/KOS/UGC/community/search plan | `references/marketing-strategy-register.md` | Client-proposal reference when it must persuade a client |
| Public whitepaper, case, industry report | `references/whitepaper-case-register.md` | Core quality and external-facing references |
| Executive brief, management update, data conclusion | `references/executive-report-register.md` | Core quality reference |
| Internal SOP, memo, handoff, meeting follow-up | `references/internal-ops-register.md` | Core quality reference |
| Fiction, scene, dialogue, narrative nonfiction | `references/fiction-narrative-register.md` | Core quality only for factual claims in narrative nonfiction |
| Character voice-over, vlog, short-video, UGC/KOC/KOS/TTS | `references/ugc-persona-script-register.md` | Large-document reference for script banks |
| Reference draft/PDF/style requested | `references/reference-style-calibration.md` | The actual genre reference; borrow only requested dimensions |
| Personal or brand voice requested | `references/rewrite-playbook.md` | `local/personal-voice-profile.md` when present; current samples override older profiles |
| Creative directions, campaign ideas, slogans, topics | `references/creative-ideation-filter.md` | Relevant marketing or product evidence |
| Generation, structural repair, dense short copy, or revision drift | Current genre reference | `references/whole-artifact-writing.md` for integrated decisions and whole-draft comparison |
| External-facing artifact | Current genre reference | `references/external-facing-check.md` |
| More than one page/section or repeated blocks | Current genre reference | `references/large-document-coverage.md` and `scripts/audit_surfaces.py` |
| User rejects a phrase or prior pass missed analogues | Current genre reference | `references/correction-propagation.md` |
| Meaning is correct but residual AI surface remains | Current genre reference | `references/trace-patterns.json` as the final pass |

Routing rules:

- Do not load every matching reference. Usually use one primary genre reference and at most two cross-cutting references; add the surface catalog only at the end.
- `client-deck-narrative-gate.md` is not for ordinary wording edits. Use it only when `L3/L4` page logic is authorized.
- `ugc-persona-script-register.md` does not govern reports, proposals, articles, or emails.
- `fiction-narrative-register.md` overrides explanatory prose heuristics inside fiction.

## Conflict Priority

When rules conflict, use this order:

1. Facts, intent, POV, and evidence level
2. Authorized `L1-L4` scope
3. Genre, scene, reader, and artifact function
4. External disclosure boundary
5. Requested reference dimension
6. Approved personal or brand voice
7. Anti-AI surface cleanup

Never improve item 7 by damaging items 1-6.

## Non-Negotiable Rules

- Preserve names, numbers, claims, chronology, and evidence classification unless substantive change is requested.
- Do not turn inference, hypothesis, recommendation, placeholder, or proposed method into an observed result.
- Do not replace one piece of jargon with another. Use a natural verb-object pair for the scene.
- Keep useful professional terms when the surrounding material defines the role, mechanism, metric, stage, or proof.
- Do not make every genre conversational. Register fit and meaning concreteness are separate checks.
- Do not expose internal codes, metrics, names, unpublished data, assignments, or complaints in external material without approval.
- Do not let reference material contribute facts unless the user authorizes factual reuse.
- Do not let a requested length authorize unsupported expansion or repeated explanation. For proposals and plans, label new analysis and recommendations as proposed work rather than observed fact.
- Concrete detail must change understanding, action, risk, relationship, or judgment. Do not add decorative precision, scenery, anecdotes, or first-person history merely to make the writing feel lived-in.
- For creative work, every surviving direction must state what the user does, sees, receives, feels, or decides, and which product fact or audience scene makes it specific.
- For scripts and narrative, distinguish the last chronological action from the real ending. Preserve ending function and vary ending shape.

## Output Contract

- For “改一下、优化口径、润色、给我一版、发客户”, provide the strongest clean version first. Keep internal checklists hidden unless a risky assumption needs disclosure.
- For review requests, lead with concrete findings and revision logic.
- For long artifacts, provide the revised artifact and a brief note on unreadable or excluded surfaces.
- Add `【自检说明】` only when review transparency is useful or requested.
- For ideation requests, provide selected directions and concise screening rationale; do not expose raw brainstorming by default.

## Deterministic Tools

- `scripts/audit_surfaces.py`: inventory and scan Markdown, text, XML/HTML, DOCX, and PPTX surfaces. Use `--profile prose` only for continuous prose shape warnings. Findings are review leads, not proof.
- `scripts/audit_ugc_scripts.py`: inspect DOCX script banks for duplication, persona concentration, provenance, and ending risks.
- `scripts/validate_behavior_cases.py`: validate the cross-genre corpus and literal output invariants. Its success does not evaluate `behavior_checks`; assess those against actual outputs separately, with a person judging subjective style fit.

Completion requires the actual reader outcome to match the current writing basis, no unresolved high-severity issue, complete required-surface review, enough distinct material for the delivered length, and a final draft that still belongs to its intended genre and writer.
