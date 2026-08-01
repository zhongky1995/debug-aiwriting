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

Use `references/trace-patterns.json` for known categories and `scripts/audit_surfaces.py --term` for the current hard negative. The correction is never “swap one suspicious word for a more polished synonym.” Name the real action, evidence, or scene-appropriate expression.

## Stop Rule

Do not claim the issue is fixed until analogous expressions have been checked across the whole artifact. If a visual, locked block, or external attachment cannot be searched, disclose it.
