# Core Quality Gates

Use this reference for nonfiction, proposals, reports, product copy, emails, social writing, translations, and other explanatory text. Genre-specific references may add stricter rules.

## Governing Test

Removing AI tone means restoring responsibility and evidence, not swapping suspicious words.

For every important explanatory, causal, execution, value, or result claim, ask:

- Who is making the claim or taking the action?
- What do they actually do?
- To which object, user, channel, document, or system?
- Under what condition or at what time?
- What visible change, cost, result, or decision follows?
- What fact, source, inference, or boundary supports it?

A sentence does not need to answer all six questions, but it must contain enough information for its role. If nobody can execute, observe, or defend it, rewrite or remove it.

For fiction and narrative work, use `fiction-narrative-register.md` instead of forcing every sentence through an actor/action checklist. Narrative nonfiction must still preserve evidence boundaries.

## Priority

Apply the gates in this order:

1. **Facts and intent**: preserve names, numbers, claims, chronology, and the user's purpose.
2. **Authorized scope**: do not turn line editing into structural or substantive rewriting.
3. **Evidence level**: distinguish fact, inference, hypothesis, recommendation, and unknown.
4. **Scene and register**: write for the actual reader, relationship, channel, and stakes.
5. **Natural language**: fix collocation, syntax, rhythm, and unnecessary abstraction.
6. **Surface cleanup**: only after meaning is stable, scan `trace-patterns.json`.

Do not trade a higher-priority requirement for a cleaner sentence.

## Meaning And Register

Judge meaning and register separately:

| Meaning | Register | Decision |
| --- | --- | --- |
| Concrete | Fits | Keep it. |
| Concrete | Wrong for the scene | Rephrase without changing the claim. |
| Abstract | Fits | Add the supported action, mechanism, evidence, or boundary. |
| Abstract | Wrong for the scene | Delete or rebuild it. |

Professional language is allowed when it names a real planning object, role, metric, stage, mechanism, or decision. Plain language is not the same as casual language.

## Evidence Gate

Classify important claims before rewriting:

- **Fact**: directly supported by the source.
- **Inference**: a defensible interpretation of available facts.
- **Hypothesis**: an explanation that still needs testing.
- **Recommendation**: a proposed action, not an observed result.
- **Unknown**: the source does not provide enough information.

Never promote a weaker level into a stronger one. If the source does not support a concrete replacement, narrow the sentence, state the missing evidence, or remove the claim.

Never invent dates, quantities, product functions, samples, quotations, reactions, anecdotes, personal experience, customer feedback, or business results to make abstract writing sound human.

## Material Sufficiency Gate

Use this gate before generating or substantially expanding long nonfiction. Length must come from distinct material, not from restating a small number of ideas.

Build a private material ledger from the available source. Useful units include:

- a supported fact, number, quotation, action, failure, cost, comparison, condition, or result
- a verified process with more than one meaningful stage
- a defensible inference that connects existing facts without pretending to be new evidence
- a clearly labelled recommendation or hypothesis in a proposal, plan, or advisory document

Do not use synonyms, generic implications, imagined examples, ornamental metaphors, or repeated qualifications as new material. There is no universal facts-per-word quota: a short email and a long case study have different needs. The test is whether each major section has enough independent support to perform its job.

When the material cannot support the requested length or level of certainty, choose the least disruptive valid move:

1. research when the task and available tools permit it
2. ask for the missing private experience, decision, or evidence when it is essential
3. narrow the claim or artifact scope
4. deliver a shorter version
5. keep an explicit placeholder or evidence gap when the format requires it

Never expand an observed fact into an invented scene. Never present proposed work as completed work.

## Knowledge Position Gate

Voice does not require frequent first person. Readers should still be able to infer:

- who is speaking or taking responsibility for the judgment
- how that person or organization knows
- what prompted the statement now
- which part is observed, inferred, proposed, or still uncertain
- where the judgment stops

Use only the dimensions the source supports. Do not manufacture a discovery story, personal trial, backstage access, emotional turn, or confession to give the copy a speaker.

## Action And Causality Gate

Reject sentences that disguise a desired result as an executable action. Replace the target label with the work someone can perform and the observable result, when the source provides it.

Check the verb harder than the noun:

- Does the verb naturally take this object in Chinese?
- Is the verb naming an operation or merely making the sentence sound strategic?
- Would the assigned person know what to do next?
- Is the claimed consequence actually caused by the action?

Ordinary verbs are often more precise for execution copy. Professional terms may stay in strategy and analysis when the surrounding page defines the mechanism.

## Natural Chinese Gate

Read the sentence in its intended setting:

- Would a competent planner present it this way to a client?
- Would an analyst accept the evidence and wording?
- Could the person assigned an SOP execute it without guessing?
- Would the speaker actually say the line aloud?
- Does the translation use a simple Chinese construction when one is available?

Prefer stable terminology. Do not rename the same actor or object merely to avoid repetition.

Let the main actor, object, or action arrive before a long stack of conditions when that makes the sentence easier to follow. Check whether consecutive clauses naturally hand the same person, object, action, or result forward. Repeated long modifiers, dense strings of `的`, and perfectly clipped short sentences are review signals, not automatic errors.

Vary rhythm only when the material supports it. Do not force every paragraph into the same length, opening, contrast pattern, or closing slogan.

## Reader-Trust Gate

Do not explain the same point three times as fact, interpretation, and takeaway. Keep the layer that adds information or changes the reader's decision.

Challenge:

- generic openings that fit any topic
- examples that are only category lists
- conclusions that repeat the title
- recommendations without conditions or tradeoffs
- charts or tables paraphrased without comparison or judgment
- certainty that exceeds the data

## Voice After Cleanup

Removing templates can leave correct but sterile text. Restore voice through selection, stance, emphasis, uncertainty, and rhythm that belong to the scene.

Do not add first person, humor, slang, digressions, deliberate disorder, emotional ambivalence, or fake imperfection merely to appear human. Personal voice must come from supplied samples, an approved profile, or the writer's actual position.

## Paragraph And Document Gate

For each paragraph:

- The opening should name a real situation, judgment, question, or claim.
- It should add a supported fact, action, example, distinction, condition, consequence, decision, or resolved question. A paraphrase of the previous paragraph is not progress.
- At least one sentence should provide an action, example, number, condition, consequence, or boundary when the source supports it.
- The ending should advance the point rather than summarize it ceremonially.

For concrete details, ask what work they do. Keep a detail when it changes the reader's understanding of cause, risk, relationship, cost, choice, sequence, or result. In nonfiction, remove unsupported precision and decorative scene-setting. In fiction, apply the viewpoint and scene rules in `fiction-narrative-register.md` instead of demanding documentary sourcing.

For multi-surface documents, inspect titles, body copy, tables, captions, notes, footnotes, and final summaries. A clean body does not compensate for untouched tables or headings.

## Stop Conditions

Stop only when:

- facts and evidence levels still match the source
- long nonfiction does not use repetition or invented detail to meet length
- the rewrite stayed within L1-L4 authorization
- important claims pass the responsibility test
- terminology and register are consistent
- no high-severity surface pattern remains unresolved
- cleanup has not flattened the requested voice
- every required document surface was reviewed or explicitly excluded
