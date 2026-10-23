---
name: debug-aiwriting
description: Diagnose, generate, rewrite, and audit Chinese writing for 去AI味、免责声明式表达、内容空洞、逻辑不完整、可读性差、修改跑偏 and voice alignment. Use for copy, articles, reports, proposals/decks, scripts, and narrative work. Develop useful substance, coherent reasoning, and genre-appropriate expression while preserving facts and authorized scope.
---

# Debug AI Writing

## Core Principle

Produce writing worth reading: a useful answer, a developed observation, an intelligible explanation, a convincing offer, or a moving scene, according to the task. Let material selection, reasoning, emphasis, and language serve that result. Accuracy and scope constrain the work; passing their checks does not by itself make a finished piece.

Find the main writing failure before editing words. A disclaimer-heavy draft may lack an answer or judgment; an obscure draft may omit the mechanism its reader needs. Repair that missing substance within scope, then remove filler. Deleting cautious phrases or shortening every paragraph can leave the original problem intact.

Scale effort to the decisions involved. A tightly coupled notice may need careful synthesis; a typo needs a correction. Keep plans, evidence classifications, and review checklists internal unless requested. Treat the artifact as a whole, including titles, tables, captions, and endings.

## Useful Substance And Proportionate Qualification

- **Answer and develop the reader's question.** For explanation, supply the decisive intermediate process; for advice, give a supported judgment and its reason; for copy, make the known offer meaningful to the reader. Lists of topics, assurances, limitations, or desirable outcomes cannot do that work.
- **Reason from the material.** Comparison, interpretation, causal explanation, and recommendation can add substance without adding new observations. Use the strongest claim the evidence supports. Missing outcome data restricts outcome claims; it does not erase a known mechanism, a useful comparison, or a defensible recommendation. Do not invent facts to fill gaps.
- **Keep the logic in the prose.** Let the reader follow how the example works and why the next passage follows. Preserve necessary premises when shortening. A connector or a summary cannot replace a missing step.
- **Choose qualifications by consequence.** Keep a condition or uncertainty when omitting it would materially change a claim, expectation, decision, obligation, or safe action. State it specifically, normally once near the relevant claim. Revisit it only when a later passage creates a distinct risk of misunderstanding. Required warnings and disclosures remain.
- **Distinguish editorial knowledge from publishable content.** “未提供效果数据” may mean avoiding a success-rate claim; it need not become a sentence in a product introduction. “这是推断” is not a required prefix to every inference. Wording, attribution, and a defined scope can make the evidence level clear naturally. Explain a material unresolved gap outside clean copy when the user needs it to use the draft.
- **Give space to what matters.** Develop the main point before peripheral exceptions. Keep a boundary where it explains the result or changes a choice; move specialist detail to an optional section when useful. Stop at the depth needed for this reader and task. Neither “shorter” nor “more comprehensive” is a universal remedy.

These priorities follow the genre. Fiction can work through viewpoint, pressure, and ambiguity; social content can work through recognition or tension. Do not force either into an explanatory checklist. Professional writing may remain professional. Do not manufacture slang, anecdotes, errors, or emotional ambivalence to appear human.

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

## Workflow

1. **Orient**: identify the current deliverable, reader, intended effect, available facts, and authorized scope. Infer what is clear from context. Keep a compact internal writing basis when decisions interact; temporary experiments and local feedback do not silently replace the whole task.
2. **Diagnose**: locate the largest obstacle in substance, reasoning, composition, scene, or language. Choose the relevant reference below. For generation, structural work, dense short copy, or drift, use [Whole-Artifact Writing](references/whole-artifact-writing.md). Select material and a governing approach before polishing.
3. **Compose**: develop the answer, observation, offer, or scene at the appropriate depth. Arrange passages by their relationship and importance. For explanatory work, use the [Adjacent-Passage Continuity Gate](references/core-quality-gates.md#adjacent-passage-continuity-gate); for defensive writing, use [Proportionate Qualification](references/core-quality-gates.md#proportionate-qualification). Preserve useful existing text.
4. **Revise as a whole**: use `references/correction-propagation.md` for related failures. Compare with the last viable draft for gains and losses in substance, logic, force, voice, and factual accuracy. Apply factual corrections; restore useful material lost to the latest preference.
5. **Read and finish**: read the complete candidate with only the intended reader's background. Check actual wording with the [Natural Chinese Gate](references/core-quality-gates.md#natural-chinese-gate), all required surfaces, and the result the text delivers. Fix significant remaining issues; stop when fit for use. Surface scans supply leads, not a verdict. Report only material unresolved gaps or inaccessible required surfaces.

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
