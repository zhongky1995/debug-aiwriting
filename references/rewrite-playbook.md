# Rewrite Playbook

Use this playbook for rewriting, generating, or matching Chinese style.

## Pass 0: Lock Scope And Register

Use the L1-L4 rewrite scope in `SKILL.md`. For a bare "优化口径/调整表达/去 AI 味" request, preserve facts, section order, page roles, and strategy. Do not rebuild substance unless the existing sentence cannot be repaired without exposing a missing fact or broken argument.

Choose the register before editing sentences. When a reference is present, first decide whether the user wants its logic, structure, register, rhythm, wording, or visual organization.

## Pass 1: Rebuild Substance When Authorized

For fiction or narrative nonfiction, do not reduce the story to one "real point" or make every detail serve an explicit thesis. Use the scene, POV, character, information, and whole-work gates in `fiction-narrative-register.md` and preserve productive ambiguity.

For nonfiction:

1. Identify the question or working claim. Keep it provisional while examining the material; do not force every paragraph back to it.
2. List the reader, occasion, and desired action.
3. Build a private material ledger: facts, actions, numbers, examples, contrasts, conditions, failures, costs, and results that the source actually supports.
4. Match the planned length and section count to that ledger. Research, ask, narrow, or shorten when the material cannot carry the requested expansion.
5. Keep source facts fixed. Mark missing facts instead of filling them in.
6. Cut claims and paragraphs that do not change reader understanding or action.
7. Add specificity only when it is grounded in the prompt, files, examples, or user-provided context.
8. Before line editing, apply the [Adjacent-Passage Continuity Gate](core-quality-gates.md#adjacent-passage-continuity-gate). Check why each paragraph leads to the next, not only whether both contain useful information. Repair missing premises within scope; do not turn this internal review into an outline in the final prose.

Before drafting a personal, opinion, forum, brand, or public-facing article, also set the knowledge position:

- who is speaking or responsible for the judgment
- why they know or care about this subject now
- what evidence changed or supports the judgment
- what remains inference or uncertainty

Do not expose this as a questionnaire in the final copy. Use only the parts supported by the source. A visible knowledge position may be carried by evidence selection and judgment boundaries without adding `我`.

Useful replacements:

- "提升用户体验" -> name which user, which moment, and what gets easier.
- "形成闭环" -> name the actual handoff, feedback, or decision point.
- "赋能业务" -> name the capability added and who uses it.
- "具有重要意义" -> name the consequence if it is ignored.

## Pass 2: Set the Register

Choose the register before editing sentences.

### Article / Opinion

- Lead with a concrete observation or claim.
- Let each paragraph add a fact, action, example, distinction, condition, consequence, decision, or useful answer. Rephrasing the previous paragraph is not development.
- Use examples and limits to make the stance believable.
- Avoid "本文将" and "通过本文".

### Analysis / Report

- Keep professional tone, but replace slogans with decisions, risks, evidence, and next actions.
- Use headings that name the finding, not the category.
- State uncertainty and assumptions plainly.
- For executive, decision, research, or data-led material, also read `executive-report-register.md`.

### Proposal / Sales Material

- Translate benefits into client-side effects.
- Avoid generic "降本增效" unless paired with a mechanism.
- Keep credibility higher than excitement.
- For client-facing marketing, operations, CRM, private-domain, KOC, or strategy decks, also read `client-proposal-playbook.md`.
- Replace service-item language with a decision chain: client problem -> why it happens -> what mechanism solves it -> how it runs -> how it will be judged.

### Whitepaper / Case Study

- Separate confirmed case facts, observed results, interpretation, general method, and editorial suggestions.
- Keep public editorial professionalism without turning the case into a capability brochure.
- Read `whitepaper-case-register.md`.

### Social Post

- Start close to the user's lived scene or contradiction.
- Keep rhythm varied; not every line needs to be a punchline.
- Avoid fake intimacy, fake confession, and excessive emoji unless the platform style requires it.

### Fiction / Narrative Nonfiction

- Read `fiction-narrative-register.md` before editing.
- Lock POV, narrative distance, character knowledge, time handling, and genre promise.
- Diagnose scene change, character choice, information release, dialogue action, world pressure, interiority, and ending before line-level cleanup.
- Preserve plot beats and scene order at L1/L2. Report upstream L3/L4 problems instead of disguising them with cleaner prose.
- Do not apply the business actor/action gate or a banned-word list mechanically to narration.

### Email / Internal Comms

- Make the ask, owner, deadline, and context explicit.
- Use plain courtesy, not ornate politeness.
- Remove defensive filler.
- For SOPs, rollout plans, ownership tables, or project follow-ups, also read `internal-ops-register.md`.

### Script / Speech

- Write for the ear. Shorten nested clauses.
- Use spoken transitions rather than essay transitions.
- Keep one beat per sentence where possible.

### Translation / Localization

- Preserve meaning and information order when accuracy matters.
- Convert English-like nominal structures into natural Chinese verbs.
- Do not add local idioms that change tone or authority.

## Pass 3: Line Edit

- Remove empty scaffolding transitions only when the relationship remains clear. Retain useful connectors and explanations; do not replace them with abrupt topic movement. For empty formulas:
  - "首先" -> start the claim directly.
  - "值得注意的是" -> state what changed or why it matters.
  - "总的来说" -> delete the repeated wrap-up, or keep a supported synthesis if the reader needs it; do not manufacture a practical implication.
- Replace abstract nouns with actors and actions.
- Break perfectly balanced sentences when they feel manufactured.
- Keep some asymmetry: one short sentence can carry emphasis better than another polished clause.
- Remove performative certainty where evidence is limited.
- In proposals, turn "we can provide X" into "X changes this client-side link in this way" when the source supports it.
- Let the actor or action arrive before long conditions when the current sentence makes the reader wait too long for its main clause.
- Check clause handoffs: the next sentence should clearly continue from the person, object, action, result, or question just introduced. After shortening, recheck paragraph boundaries for lost conditions, purposes, or reasoning.
- Review long sentences with dense `的`, repeated paragraph openers, queues of short one-sentence paragraphs, and identical closing beats. Vary only where the material and genre call for it.
- Read scripts, speeches, dialogue, and conversational prose aloud. A sentence that is clear on paper but difficult to say still needs revision.

## Detail Function Gate

Concrete writing is not automatically human writing. Keep a detail only when it changes at least one of these:

- what happened or what happens next
- how the reader understands cause, risk, cost, relationship, or choice
- what a character notices or can do in the current scene
- what a user, client, operator, or decision-maker needs to judge

For nonfiction, unsupported times, weather, gestures, rooms, dialogue, customer reactions, and personal experience are fake specificity. For fiction, details may be invented when authorized, but they must belong to the viewpoint, pressure, action, or atmosphere of the scene rather than decorate every passage in the same way.

## Pass 4: Concrete Language Gate

Before output, apply `core-quality-gates.md`. When the meaning is already sound but the draft still feels generated, run the final surface pass against `trace-patterns.json`.

Run the gate in the chosen register. Do not treat professional density as an error by itself.

Fail and rewrite any sentence where:

- framework nouns replace actions
- a concept could apply unchanged to another brand/project
- an execution instruction does not tell its actor what to do; this actionability test does not apply to observations, explanations, qualifications, or open questions
- an execution-table cell only names a desired result instead of the work; category labels in other table types may be appropriate

Do not rely on banned-word scanning. A sentence can pass the blacklist and still fail this gate.

## Voice Matching Procedure

When the user provides writing samples:

1. Identify only traits supported by the available passages; do not fill a trait quota. Follow `reference-style-calibration.md` for passage-level evidence.
2. Separate content preferences, personal experience, and style. A reference author's assertion is not automatically a fact or a rule for this writer.
3. Ground negative constraints in the samples and the user's explicit corrections. Limited samples do not establish what the author never does.
4. For a substantial rewrite, keep a compact profile with passage locations and relevant exceptions; avoid replacing the task with a style-analysis report.
5. Check the actual draft against those passages and the user's feedback. Short sentences, first person, or early conclusions alone do not demonstrate a voice match.

Template:

```text
Style profile:
- stance:
- sentence rhythm:
- paragraph rhythm:
- common transitions:
- preferred evidence:
- words/patterns to avoid:
- formatting:
```

## Response Formats

Follow the output policy in `SKILL.md`: clean final requests should return the revised copy first and avoid exposing process. Use the formats below only when the user asks for review, diagnosis, comparison, or editing rationale.

For rewrite review requests:

```text
改写稿：
[revised text]

主要调整：
- [specific change]
- [specific change]
```

For audit requests:

```text
主要问题：
- [issue + example]
- [issue + example]

修改方向：
- [actionable direction]
```

For long-form generation review:

```text
写作判断：
[audience, stance, structure]

正文：
[draft]
```
