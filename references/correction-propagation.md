# Correction Propagation

Use this whenever the user rejects a phrase, verb, sentence pattern, register choice, or local rewrite during an active task.

## Required Procedure

1. Record the exact rejected wording.
2. Identify the failure class: unnatural collocation, abstract action, missing subject, result-as-action, wrong register, internal wording, false certainty, repeated template, or another explicit user preference.
3. Generate nearby variants that may express the same failure without repeating the exact words.
4. Scan the entire source draft, revised draft, tables, captions, notes, visuals with text, and live document when applicable.
5. Rewrite every match in the correct local register.
6. Treat the correction as a hard negative for the rest of the task. Do not reintroduce it in later sections, summaries, captions, or status messages.
7. Read back the final artifact and verify both the exact phrase and the broader pattern.

## Pattern Expansion

Do not search only for the rejected literal. Expand it by function:

- the same verb with nearby objects
- upgraded synonyms that preserve the same false action
- the same sentence template with different nouns
- headings, tables, captions, and summaries that restate the failure

Include paragraph-level functions. If the user rejects constant returns to a conclusion, check whether each new example is immediately turned into the same lesson under different words. Remove the redundant lesson rather than replace it with another slogan. Do not ban conclusions generally: keep a supported judgment that performs needed work, and allow a passage to end on its last useful observation.

If a revision repeats the rejected function, revisit the claim, example, and evidence before trying another phrasing pass. The appropriate fix may be deleting a paragraph, shortening the piece, or finding better material within the authorized scope. Do not promise the issue is solved merely because the listed phrases disappeared.

If the user reports “逻辑跳、关联不起来、需要自己联想、表达不完整”, use the [Adjacent-Passage Continuity Gate](core-quality-gates.md#adjacent-passage-continuity-gate) across the current artifact's sentence and paragraph transitions. Name the missing premise and the reader's likely question. Do not merely add connectors or expand every paragraph. Preserve the earlier correction against repeated conclusions while restoring necessary reasoning.

Use `references/trace-patterns.json` for known categories and `scripts/audit_surfaces.py --term` for the current hard negative. The correction is never “swap one suspicious word for a more polished synonym.” Name the real action, evidence, or scene-appropriate expression.

## Stop Rule

Do not claim the issue is fixed until analogous expressions have been checked across the whole artifact. If a visual, locked block, or external attachment cannot be searched, disclose it.
