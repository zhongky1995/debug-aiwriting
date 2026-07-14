# Rewrite Playbook

Use this playbook for rewriting, generating, or matching Chinese style.

## Pass 0: Lock Scope And Register

Use the L1-L4 rewrite scope in `SKILL.md`. For a bare "优化口径/调整表达/去 AI 味" request, preserve facts, section order, page roles, and strategy. Do not rebuild substance unless the existing sentence cannot be repaired without exposing a missing fact or broken argument.

Choose the register before editing sentences. When a reference is present, first decide whether the user wants its logic, structure, register, rhythm, wording, or visual organization.

## Pass 1: Rebuild Substance When Authorized

1. Extract the real point in one sentence.
2. List the reader, occasion, and desired action.
3. Keep source facts fixed. Mark missing facts instead of filling them in.
4. Cut claims that do not change reader understanding.
5. Add specificity only when it is grounded in the prompt, files, examples, or user-provided context.

Useful replacements:

- "提升用户体验" -> name which user, which moment, and what gets easier.
- "形成闭环" -> name the actual handoff, feedback, or decision point.
- "赋能业务" -> name the capability added and who uses it.
- "具有重要意义" -> name the consequence if it is ignored.

## Pass 2: Set the Register

Choose the register before editing sentences.

### Article / Opinion

- Lead with a concrete observation or claim.
- Let paragraphs develop one idea, not one template step.
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

- Replace scaffolding transitions with topic movement:
  - "首先" -> start the claim directly.
  - "值得注意的是" -> state what changed or why it matters.
  - "总的来说" -> give the practical implication.
- Replace abstract nouns with actors and actions.
- Break perfectly balanced sentences when they feel manufactured.
- Keep some asymmetry: one short sentence can carry emphasis better than another polished clause.
- Remove performative certainty where evidence is limited.
- In proposals, turn "we can provide X" into "X changes this client-side link in this way" when the source supports it.

## Pass 4: Concrete Language Gate

Before output, apply `plain-language-gate.md` when the text is formal, public-facing, case/whitepaper-style, or the user has complained that AI味 remains.

Run the gate in the chosen register. Do not treat professional density as an error by itself.

Fail and rewrite any sentence where:

- framework nouns replace actions
- a concept could apply unchanged to another brand/project
- the sentence cannot be converted into a one-line practical action
- a table cell is a label rather than something a person/team does

Do not rely on banned-word scanning. A sentence can pass the blacklist and still fail this gate.

## Voice Matching Procedure

When the user provides writing samples:

1. Identify 5-8 recurring traits from the samples.
2. Separate content preferences from style preferences.
3. Extract negative constraints: what the author rarely does.
4. Draft a compact style profile before rewriting if the task is long.
5. Apply the profile, then audit against both the profile and the AI trace checklist.

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
