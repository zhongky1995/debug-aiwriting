# External-Facing Reader And Boundary Check

Use this reference for client emails, formal proposals, customer-facing decks, public releases, external statements, or any draft that may be read outside the user's own team.

## Reader Anchor

Before writing, identify these items. Infer when obvious; ask only if the missing answer would materially change the draft.

- **Reader**: role, knowledge level, relationship to the user, and what they care about.
- **Scene**: formal proposal, client email, external release, public article, meeting follow-up, sales material, or other channel.
- **Desired action**: approve, reply, understand, align, decide, attend, pay, revise, or forward.
- **Reader should not know**: internal codenames, internal KPI names, internal assessment logic, private people/role splits, unpublished data, unconfirmed assumptions, internal complaints, or tactical judgments not meant for external readers.

## Boundary Check

Read the draft sentence by sentence and ask:

```text
Would this reader understand this sentence?
Should this reader be allowed to see this sentence?
Does this sentence expose how we internally judge, price, staff, score, or complain about the work?
```

If a sentence fails, choose one:

- **Translate** it into reader-facing language.
- **Generalize** it when the fact is usable but the internal detail is not.
- **Delete** it when the reader does not need it.
- **Ask for confirmation** only when disclosure may be intentional but risky.

## Common Conversions

- Internal codename -> public project, product, module, phase, or workstream name.
- Internal KPI name -> reader-facing outcome, milestone, acceptance criterion, or business question.
- Internal person name -> role or team, unless the person is meant to be named externally.
- Unpublished number -> qualitative direction, range, or "based on current observations" if no number may be disclosed.
- Internal complaint -> neutral risk, dependency, or boundary.
- Provider capability list -> client-side problem, mechanism, execution object, and judgment standard.

## AI-Tone Cleanup For External Materials

Remove or rewrite:

- hollow words: 赋能、抓手、闭环、深度、生态、全面提升、持续、多维度、进一步、有力支撑, unless a concrete mechanism follows.
- forced parallelism: "不仅...而且...更是..." and three-part slogan structures.
- conclusions without a fact, judgment, cost, tradeoff, or next action.
- repeated paragraph rhythm: each paragraph should not be "topic sentence -> expansion -> summary."
- "既要又要还要" language that avoids priority and cost.

## Finished Copy And Editorial Notes

Return usable copy first. Run the boundary check internally; do not append a routine `【自检说明】` or require the user to opt out of it. Add a short separate note when requested or when a specific unresolved disclosure, fact, or commitment affects use of the draft.

External writing still needs a substantive answer, explanation, or reason to act. Apply [Proportionate Qualification](core-quality-gates.md#proportionate-qualification): include the limits this reader needs, and express the positive supported content with equal precision. Do not copy internal cautions about unprovided evidence into the finished artifact by default.
