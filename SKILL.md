---
name: debug-aiwriting
description: Diagnose, rewrite, generate, and audit Chinese writing when the user asks to 去AI味, 消除AI味, 调整口径, 改口径, 去白皮书腔/套话/假大空, fix unnatural Chinese or verb-object pairs, improve a weak client-deck story, separate persona voices, match a personal/brand/reference style, protect internal/external wording, or screen generic creative ideas. Supports short copy, articles, fiction and narrative nonfiction, reports, whitepapers and cases, emails and speeches, UGC/KOC/KOS scripts, client proposals and decks, marketing plans, social content, and internal SOPs. Preserve facts, evidence level, authorized rewrite scope, genre, and full-document coverage.
---

# Debug AI Writing

## Core Principle

Optimize for reader trust, not detector evasion. Removing AI tone means restoring responsibility and evidence, not replacing suspicious words.

For important explanatory claims, make clear enough of this chain for the sentence's role: **who acts or claims -> based on what -> does what -> to which object -> under what condition -> what visible change or decision follows**. If the source cannot support a concrete claim, narrow it, label the uncertainty, or delete it. Never invent specificity.

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

Task modes:

- **Rewrite**: deliver the revised text, then brief notes only when useful.
- **Generation**: establish purpose, reader, stance, evidence, and format before drafting.
- **Voice/reference alignment**: extract only the requested dimensions before rewriting.
- **Audit only**: identify problems and revision moves; do not silently replace the draft.
- **Creative ideation**: filter generic directions internally; show the raw pool only when requested.

## Workflow

1. **Lock the contract**: reader, relationship, channel, stakes, desired action, genre, artifact function, facts, evidence level, and `L1-L4` scope.
2. **Route references**: use the matrix below. Load one primary genre reference plus only the cross-cutting references the task actually needs.
3. **Diagnose positively**: identify the missing actor, action, evidence, causal step, viewpoint limit, scene consequence, decision, or ending function before scanning bad phrases.
4. **Rewrite in three passes**:
   - substance/story: repair meaning within scope; add no unsupported detail
   - language: fix register, collocation, syntax, rhythm, and terminology
   - surface residue: scan `references/trace-patterns.json` only after meaning is stable
5. **Propagate corrections**: when the user rejects one phrase or pattern, treat it as a hard negative, scan every analogous expression and every live copy, and do not reintroduce it later.
6. **Verify coverage**: for multi-surface artifacts inspect title, headings, body, tables, captions, notes, footnotes, summaries, and embedded text. Report unreadable or intentionally excluded surfaces.
7. **Stop only after verification**: facts, evidence, scope, register, terminology, endings, and required surfaces must pass. A blacklist pass or self-declared `PASS` is not enough.

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
- For creative work, every surviving direction must state what the user does, sees, receives, feels, or decides, and which product fact or audience scene makes it specific.
- For scripts and narrative, distinguish the last chronological action from the real ending. Preserve ending function and vary ending shape.

## Output Contract

- For “改一下、优化口径、润色、给我一版、发客户”, provide the strongest clean version first. Keep internal checklists hidden unless a risky assumption needs disclosure.
- For review requests, lead with concrete findings and revision logic.
- For long artifacts, provide the revised artifact and a brief note on unreadable or excluded surfaces.
- Add `【自检说明】` only when review transparency is useful or requested.
- For ideation requests, provide selected directions and concise screening rationale; do not expose raw brainstorming by default.

## Deterministic Tools

- `scripts/audit_surfaces.py`: inventory and scan Markdown, text, XML/HTML, DOCX, and PPTX surfaces. Findings are review leads, not proof.
- `scripts/audit_ugc_scripts.py`: inspect DOCX script banks for duplication, persona concentration, provenance, and ending risks.
- `scripts/validate_behavior_cases.py`: validate the cross-genre regression corpus and check literal output invariants.

Completion requires no unresolved high-severity issue, complete required-surface review, and a final draft that still belongs to its intended genre and writer.
