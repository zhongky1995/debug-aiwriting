# Reference Style Calibration

Use this when the user asks to follow a reference draft, PDF, deck, page range, previous output, or specific口径. The goal is to match the useful expression logic of the reference, not to copy its words.

## Build A Style Contract First

Before rewriting, extract these items from the reference:

1. **Scene**: final reader, relationship, stakes, and whether it is a proposal, report, whitepaper, script, social copy, or internal memo.
2. **Page role pattern**: how each page or section functions, such as target contract, strategy map, role matrix, node example, content matrix, budget, or acceptance rule.
3. **Authority level**: plain explanation, professional planning, executive summary, brand copy, or operational SOP.
4. **Sentence rhythm**: short strategic headings, one-line judgments, dense tables, explanatory paragraphs, or conversational argument.
5. **Allowed vocabulary**: professional terms that are part of the scene and should not be flattened.
6. **Banned drift**: what would make the rewrite feel wrong: too casual, too report-like, too internal, too salesy, too academic, too operational.

Write with this contract in mind. Do not output the contract unless the user asks for rationale.

## What To Preserve

Preserve the reference's working structure when it is useful:

- title as page judgment, not category label
- opening sentence as strategic conclusion
- table as decision tool, not decoration
- cross-page logic, such as target -> strategy -> execution -> node example -> search/content -> acceptance
- professional terms when they name real planning objects

## What Not To Copy

- Do not copy factual claims, numbers, brand details, or internal口径 from the reference unless they belong to the current task.
- Do not imitate decorative jargon if the reference itself is weak.
- Do not make all genres sound like the reference. Apply it only to the requested scene.

## Failure Modes

- **Over-cleaning**: the draft becomes clearer but loses the professional register the user wanted.
- **Partial borrowing**: only a few words are copied, while page logic and rhythm remain unchanged.
- **Scene mismatch**: a strategy deck becomes a project memo, or a public whitepaper becomes an internal report.
- **Reference leakage**: old brand names, metrics, or internal assumptions enter the new draft.

## Quick Check

Before final output, ask:

- Does this sound like the same type of artifact as the reference?
- Are the page roles aligned, not just the vocabulary?
- Did any useful professional term get flattened into casual language?
- Did any reference-only fact leak into the new draft?
