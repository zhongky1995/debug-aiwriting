---
name: debug-aiwriting
description: Diagnose, generate, rewrite, and audit Chinese writing for 去AI味、免责声明式表达、内容空洞、逻辑不完整、可读性差、修改跑偏 and voice alignment. Use for copy, articles, reports, proposals/decks, scripts, and narrative work. Develop useful substance, coherent reasoning, and genre-appropriate expression while preserving facts and authorized scope.
---

# Debug AI Writing

## Core Principle

Write for the reader's task: a useful answer, an intelligible explanation, a supported recommendation, a convincing offer, or a moving scene. Develop the substance that makes the piece worth reading before polishing its surface. Accurate but empty prose still needs work.

Use the strongest claim the material supports. Reasoning can add understanding without inventing observations. Keep qualifications when they change a claim, decision, expectation, obligation, or safe action; normally state them once near the relevant point. Missing data and internal review categories do not automatically belong in finished copy. See [Core Quality Gates](references/core-quality-gates.md) for evidence, explanation, and language decisions.

Preserve the intended genre and voice. Professional prose may remain professional; fiction may work through viewpoint and ambiguity. Clear meaning does not require colloquial language, a human subject in every sentence, or a ban on abstraction. Keep useful existing writing.

## Workflow

Select the foundation, primary genre, and conditional references using the reading order below. Read them before the work they govern. Apply the workflow to the requested scope: a local correction needs only its surrounding context; a whole-document rewrite needs the complete candidate. These are editing operations, not required headings or a public checklist.

1. **Establish the writing task.** Distinguish the requester, the intended reader, and the people the text discusses; identify whose voice addresses whom and for what purpose. Infer these from context. For material to be handed to others, use [Reader And Disclosure Fit](references/external-facing-check.md) before composing. Use [Whole-Artifact Writing](references/whole-artifact-writing.md) for generation, structural work, dense short copy, or revision drift; a temporary experiment does not silently replace the deliverable.
2. **Compose the reader's path.** Select and arrange supported material so the reader can follow the idea or scene as it unfolds. In explanatory writing, develop the important intermediate relationship where the reader needs it. A comparison must explain what differs and why it matters; a change of viewpoint must be recognizable when it occurs. Use the [Adjacent-Passage Continuity Gate](references/core-quality-gates.md#adjacent-passage-continuity-gate). Keep necessary orientation while cutting repeated explanation. Allocate space to the main point, with conditions and specialist detail in proportion to their role.
3. **Check fidelity against the material.** Preserve required facts, actions, relationships, quantities, chronology, claim strength, and commitments. Fidelity does not require carrying every source detail or editing note into the artifact. An action that happened must remain an action, not merely an opportunity or a reason to act. Use [Correction Propagation](references/correction-propagation.md) for feedback; incorporate its substance into the text without narrating the exchange unless that exchange is the subject.
4. **Edit the text as it will be read.** Set the source, plan, and repair list aside. Read the complete candidate with only the intended reader's background, including retained sentences and required surfaces. Does it address that reader's task, or report how the draft was commissioned, checked, and revised? Check [Natural Chinese](references/core-quality-gates.md#natural-chinese-gate) and whether each passage is understandable when encountered. Repair missing explanation within scope; recheck changed meaning against the source. Finish when the reader's task is met and significant defects are resolved, without endless preference swaps.

Keep working notes and review findings internal unless requested. A fluent explanation of the edits, a disappeared phrase, or a successful scan is not evidence that the final text works. Use the actual text to judge completion.

## Scope Contract

Classify the task before editing:

| Level | Allowed change |
| --- | --- |
| `L1` | Correct awkward wording, collocation, grammar, repetition, and local AI traces. |
| `L2` | Rewrite sentences and paragraphs while preserving facts, page/section/scene roles, order, POV, plot beats, and strategy. |
| `L3` | Reorder or rebuild argument, page, chapter, or scene logic without unsupported facts. |
| `L4` | Develop new analysis, methods, examples, scenes, or creative directions from available evidence. |

Treat bare requests such as “优化口径、调整表达、去 AI 味” as `L2`. Do not enter `L3` or `L4` without authorization. If a language symptom comes from an upstream structure, evidence, character, or scene problem that is outside scope, repair what is allowed and state the limitation.

Authorization follows the user's request and earlier decisions, not a required level label: “逻辑不完整，帮我补齐/重新组织” authorizes that repair; developing new content permits the needed L4 work within its bounds. At L2, clarify supported relationships, remove irrelevant editorial material, and consolidate redundant qualifications while preserving the agreed argument, order, and consequential conditions. Global review is allowed at every level.

Task modes:

- **Rewrite**: deliver the revised text, then brief notes only when useful.
- **Generation**: establish purpose, reader, stance, evidence, and format before drafting.
- **Voice/reference alignment**: extract only the requested dimensions before rewriting.
- **Audit only**: identify problems and revision moves; do not silently replace the draft.
- **Creative ideation**: filter generic directions internally; show the raw pool only when requested.

## Routing Matrix

### Foundation And Reading Order

The shared task, scope, fidelity, and output rules in this entrypoint apply to every task. For factual or explanatory prose, also read `core-quality-gates.md` before drafting or substantive revision. For fiction, scenes, and dialogue, read the narrative or script reference as the foundation for expression; use the core evidence rules for factual claims in narrative nonfiction or a factual commercial script. Explanatory-prose tests do not govern a scene's ambiguity, interiority, or dialogue.

1. **Before composing:** read the foundation and the primary genre reference below. Add `whole-artifact-writing.md` for generation, authorized structural work, dense short copy, or revision drift; add reference/voice calibration when requested. Use `rewrite-playbook.md` for a substantial general rewrite or style extraction, not automatically for every genre.
2. **Before editing a large artifact:** use `large-document-coverage.md` to inventory its required surfaces. For an authorized L3/L4 client-deck story repair, also use `client-deck-narrative-gate.md`. These govern coverage and structure without changing the chosen genre.
3. **When feedback arrives:** use `correction-propagation.md` for a rejected expression, pattern, or missed analogue. Reconsider which related passages and references are affected while retaining the current purpose and accepted improvements. This supplements the genre reference rather than replacing it.
4. **Before delivery:** reread the artifact for its intended audience; for material handed to others, reapply `external-facing-check.md`. Consult `trace-patterns.json` only for residual surface issues after composition. Reuse guidance already read; reread affected references when the task or file changes.

Read triggered guidance at the stage it governs; do not load every reference or impose a numerical cap. A long client proposal uses core, proposal, whole-work, and reader-fit guidance before composition, coverage for editing, and correction propagation after feedback. A social carousel uses social guidance; a local novel rewrite uses fiction and applicable correction guidance, not the proposal workflow.

| Task condition | Primary reference | Add only when needed |
| --- | --- | --- |
| Nonfiction, product copy, email, translation, general rewrite | `references/core-quality-gates.md` | `references/rewrite-playbook.md` for long rewriting, generation, or voice extraction |
| Social posts, 小红书图文/笔记/硬广, carousels, feed ads | `references/social-content-register.md` | `references/whole-artifact-writing.md` for generation or drift; reference calibration when actual examples are supplied |
| Client proposal, sales material, strategy presentation | `references/client-proposal-playbook.md` | `references/client-deck-narrative-gate.md` only for multi-page `L3/L4` story repair |
| Marketing, launch, KOC/KOS/UGC/community/search plan | `references/marketing-strategy-register.md` | Client-proposal reference when it must persuade a client |
| Public whitepaper, case, industry report | `references/whitepaper-case-register.md` | Core quality and external-facing references |
| Executive brief, management update, data conclusion | `references/executive-report-register.md` | Core quality reference |
| Internal SOP, memo, handoff, meeting follow-up | `references/internal-ops-register.md` | Core quality reference |
| Fiction, scene, dialogue, narrative nonfiction | `references/fiction-narrative-register.md` | Core quality only for factual claims in narrative nonfiction |
| Character voice-over, vlog, audiovisual UGC/KOC/KOS scripts, TTS | `references/ugc-persona-script-register.md` | Large-document reference for script banks |
| Reference draft/PDF/style requested | `references/reference-style-calibration.md` | The actual genre reference; borrow only requested dimensions |
| Personal or brand voice requested | `references/rewrite-playbook.md` | `local/personal-voice-profile.md` when present; current samples override older profiles |
| Creative directions, campaign ideas, slogans, topics | `references/creative-ideation-filter.md` | Relevant marketing or product evidence |
| Generation, structural repair, dense short copy, or revision drift | Current genre reference | `references/whole-artifact-writing.md` for integrated decisions and whole-draft comparison |
| Material handed to readers beyond this conversation | Current genre reference | `references/external-facing-check.md` before composition and at delivery |
| More than one page/section or repeated blocks | Current genre reference | `references/large-document-coverage.md` and `scripts/audit_surfaces.py` |
| User rejects a phrase or prior pass missed analogues | Current genre reference | `references/correction-propagation.md` |
| Meaning is correct but residual AI surface remains | Current genre reference | `references/trace-patterns.json` as the final pass |

Routing rules:

- Choose the primary reference by the text's communicative job. Read conditional references in the order above; do not omit a triggered coverage, feedback, or external check merely to fit a numerical cap.
- `client-deck-narrative-gate.md` is not for ordinary wording edits. Use it only when `L3/L4` page logic is authorized.
- `ugc-persona-script-register.md` does not govern reports, proposals, articles, or emails.
- Social finished copy uses `social-content-register.md`; a marketing plan uses `marketing-strategy-register.md`. Use the persona/script reference only when an actual speaker or audiovisual script needs it. Channel names and the term UGC alone do not determine the route.
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

- Preserve names, numbers, claims, chronology, POV, and evidence level within the authorized scope. Do not turn inference, hypothesis, recommendation, placeholder, or proposed work into an observed result.
- Let material and reasoning support the requested length. Do not invent facts, quotations, experiences, or decorative precision to make writing concrete, persuasive, or personal. Reference material supplies style only unless factual reuse is authorized.
- Keep professional terms when they name a real role, method, object, or decision. Repair unclear relationships rather than exchanging jargon for different jargon or making every genre conversational.
- Do not expose internal codes, metrics, names, unpublished data, assignments, or complaints in external material without approval.
- For creative directions, connect what the user does, sees, receives, feels, or decides to the specific product fact or audience scene that makes it meaningful.
- For scripts and narrative, preserve the ending's function; the last chronological action need not be the ending. Vary ending shape where the material calls for it.

## Output Contract

- For “改一下、优化口径、润色、给我一版、发客户”, provide the strongest clean version first. Keep editorial checklists, evidence labels, scope codes, and routine self-assessment out of the finished copy.
- For review requests, lead with concrete findings and revision logic.
- For long artifacts, provide the revised artifact and a brief note on unreadable or excluded surfaces.
- Add notes only when requested or when a specific unresolved issue changes how the user can use the draft. Do not append routine `【自检说明】`, capability disclaimers, or a list of facts the material did not provide. Explicitly requested or necessary disclosures belong where their reader needs them.
- For ideation requests, provide selected directions and concise screening rationale; do not expose raw brainstorming by default.

## Deterministic Tools

- `scripts/audit_surfaces.py`: inventory and scan Markdown, text, XML/HTML, DOCX, and PPTX surfaces. Use `--profile prose` only for continuous prose shape warnings. Findings are review leads, not proof.
- `scripts/audit_ugc_scripts.py`: inspect DOCX script banks for duplication, persona concentration, provenance, and ending risks.
- `scripts/validate_behavior_cases.py`: validate the cross-genre corpus and literal output invariants. Its success does not evaluate `behavior_checks`; assess those against actual outputs separately, with a person judging subjective style fit.

Completion requires the actual reader outcome to match the current writing basis, no unresolved high-severity issue, complete required-surface review, enough distinct material for the delivered length, and a final draft that still belongs to its intended genre and writer.
