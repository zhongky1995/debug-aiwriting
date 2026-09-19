# Correction Propagation

Use this whenever the user rejects a phrase, verb, sentence pattern, register choice, or local rewrite during an active task.

## Required Procedure

1. Record the feedback and its intended scope. Distinguish a factual correction, explicit wording prohibition, local example, broad preference, and change of purpose.
2. Diagnose the failure and its level: material, argument/scene, emphasis, register, or wording. “Too long” may mean competing purposes; “stronger” may mean an unanswered question. State internally what to change and which established facts and functions to preserve.
3. Inspect analogous wording and functions across required surfaces. A match is a review candidate, not automatic evidence of the same defect.
4. Repair confirmed failures within scope and follow their dependencies. Preserve legitimate uses in other functions; do not make all paragraphs or characters obey one local preference.
5. Keep explicit prohibitions active within their stated scope. Track diagnosed failures without converting every disliked example into a universal word ban. Later explicit user changes supersede earlier preferences.
6. Compare the complete candidate with the previous viable version under the current writing basis: improvement, loss, and whether the tradeoff is justified. Follow [Whole-Artifact Writing](whole-artifact-writing.md) when feedback alters emphasis or the organizing approach. Reject regressions while still applying mandatory factual corrections and explicit requirements.
7. Read back the actual final artifact. Verify both the reported defect and the overall reader outcome; phrase disappearance alone is insufficient.

## Pattern Expansion

Do not search only for the rejected literal. Expand it by function:

- the same verb with nearby objects
- upgraded synonyms that preserve the same false action
- the same sentence template with different nouns
- headings, tables, captions, and summaries that restate the failure

Include paragraph-level functions. If the user rejects constant returns to a conclusion, check whether each new example is immediately turned into the same lesson under different words. Remove the redundant lesson rather than replace it with another slogan. Do not ban conclusions generally: keep a supported judgment that performs needed work, and allow a passage to end on its last useful observation.

If a revision repeats the rejected function, revisit the claim, example, and evidence before trying another phrasing pass. The appropriate fix may be deleting a paragraph, shortening the piece, or finding better material within the authorized scope. Do not promise the issue is solved merely because the listed phrases disappeared.

If the user reports “逻辑跳、关联不起来、需要自己联想、表达不完整”, use the [Adjacent-Passage Continuity Gate](core-quality-gates.md#adjacent-passage-continuity-gate) across the current artifact's sentence and paragraph transitions. Name the missing premise and the reader's likely question. Do not merely add connectors or expand every paragraph. Preserve the earlier correction against repeated conclusions while restoring necessary reasoning.

Use `references/trace-patterns.json` for known categories and `scripts/audit_surfaces.py --term` for an explicitly rejected phrase within its applicable scope. The correction is never “swap one suspicious word for a more polished synonym.” Name the real action, evidence, or scene-appropriate expression.

## Stop Rule

Do not claim the issue is fixed until analogous expressions have been checked across the whole artifact. If a visual, locked block, or external attachment cannot be searched, disclose it.
