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

Use one primary genre reference from the routing matrix and add references for actual problems. Apply the following to the requested scope: a local correction needs only its surrounding context; a whole-document rewrite needs the complete candidate. These are editing operations, not required headings or a public checklist.

1. **Establish the writing task.** Identify the reader, what the text must help them understand, decide, do, or experience, and which facts and relationships must survive. Diagnose the main obstacle before choosing a repair. For generation, structural work, dense short copy, or revision drift, use [Whole-Artifact Writing](references/whole-artifact-writing.md). Infer what the context establishes; a temporary experiment does not silently replace the deliverable.
2. **Compose the reader's path.** Select and arrange supported material so the reader can follow the idea or scene as it unfolds. In explanatory writing, develop the important intermediate relationship where the reader needs it. A comparison must explain what differs and why it matters; a change of viewpoint must be recognizable when it occurs. Use the [Adjacent-Passage Continuity Gate](references/core-quality-gates.md#adjacent-passage-continuity-gate). Keep necessary orientation while cutting repeated explanation. Allocate space to the main point, with conditions and specialist detail in proportion to their role.
3. **Check fidelity against the material.** Compare the candidate with the source and current task: preserve actions, relationships, quantities, chronology, claim strength, and commitments. An action that happened must remain an action, not merely an opportunity or a reason to act. Check that smoother or shorter wording has not changed the point. When applying feedback, use [Correction Propagation](references/correction-propagation.md) and retain previous improvements that still serve the task.
4. **Edit the text as it will be read.** Set the source, plan, and repair list aside. Read the actual candidate from beginning to end with only the intended reader's background, including retained sentences and other required surfaces. Check natural expression with the [Natural Chinese Gate](references/core-quality-gates.md#natural-chinese-gate), and whether each passage is understandable when encountered. If understanding depends on an explanation still only in the plan or arriving later, repair the passage or transition within scope. After an edit changes meaning, recheck it against the source. Finish when the reader's task is met and significant defects are resolved; keep preferences among adequate alternatives from causing endless rewrites.

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

Authorization follows the user's actual request and earlier decisions, not a required level label: “逻辑不完整，帮我补齐/重新组织” authorizes the corresponding reasoning or structural repair; a request to develop new content authorizes the needed L4 work within its stated bounds. Do not ask again merely because the user did not say “L3”. At L2, clarify supported implicit relationships and remove redundant caveats while preserving the agreed argument and order. Global review is allowed at every level.

Task modes:

- **Rewrite**: deliver the revised text, then brief notes only when useful.
- **Generation**: establish purpose, reader, stance, evidence, and format before drafting.
- **Voice/reference alignment**: extract only the requested dimensions before rewriting.
- **Audit only**: identify problems and revision moves; do not silently replace the draft.
- **Creative ideation**: filter generic directions internally; show the raw pool only when requested.

## Routing Matrix

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
| External-facing artifact | Current genre reference | `references/external-facing-check.md` |
| More than one page/section or repeated blocks | Current genre reference | `references/large-document-coverage.md` and `scripts/audit_surfaces.py` |
| User rejects a phrase or prior pass missed analogues | Current genre reference | `references/correction-propagation.md` |
| Meaning is correct but residual AI surface remains | Current genre reference | `references/trace-patterns.json` as the final pass |

Routing rules:

- Do not load every matching reference. Usually use one primary genre reference and at most two cross-cutting references; add the surface catalog only at the end.
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
