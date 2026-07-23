# Client Deck Narrative Gate

Use this gate for client-facing decks at L3/L4 when the user reports weak logic, an incomplete story, piled-up viewpoints, delayed proof, or repeated visual revisions that did not improve persuasion.

## 1. Separate three states

Track these independently:

- `narrative_status`: Does one buyer question lead to an earned conclusion?
- `evidence_status`: Does each important claim have adjacent proof at the correct strength?
- `production_status`: Can the file render, export, and pass privacy/layout checks?

Never treat production success as narrative success. Use `NARRATIVE_BLOCKED`, `EVIDENCE_BLOCKED`, or `PRODUCTION_BLOCKED` explicitly when any layer fails.

## 2. Write the narrative contract first

Before outlining pages, lock:

- **Reader**: one primary decision-maker, not a list of unrelated roles.
- **Reading moment**: what happened just before they received the deck.
- **Reader decision**: what judgment should change after reading.
- **Entry problem**: a situation the reader already recognizes without learning new terminology.
- **Mother question**: the single question the deck answers.
- **Mother claim**: one sentence the deck earns; it must change the reader's interpretation or choice.
- **Proof anchor**: the strongest case, artifact, result, or observed change that makes the claim credible.
- **Claim boundary**: what the evidence does not prove.
- **Artifact function**: break-ice, proposal, sales follow-up, keynote, or reference document.

If these cannot be stated concretely, stop. Do not create page titles or visuals yet.

## 3. Choose a story engine

Use one dominant engine:

### Evidence-led break-ice deck

Recognizable work problem -> anchor case -> general diagnosis -> method extracted from the case -> consequences -> proof portfolio -> why this team.

Use this for a small or unfamiliar brand. Earn insight from evidence instead of asking the reader to trust a long theory section.

### Decision-led proposal

Client decision -> current constraint -> strategic choice -> mechanism -> execution -> proof -> risk/boundary -> requested decision.

### Belief-change deck

Existing belief -> contradiction -> evidence -> better explanation -> implications -> proof -> conclusion.

Do not mix all three engines. A taxonomy, service catalogue, and methodology lecture are supporting material, not story engines.

## 4. Build a causal page ledger

For every page, record:

| Field | Required answer |
| --- | --- |
| `reader_question` | What question is active in the reader's mind here? |
| `page_answer` | What new answer does this page provide? |
| `evidence` | What artifact, fact, case, example, or observed change supports it? |
| `proof_level` | Fact, inference, hypothesis, capability evidence, MVP, deployed use, or verified result |
| `why_now` | Why must this page appear at this exact point? |
| `next_dependency` | What question does this answer create for the next page? |
| `removal_consequence` | What breaks if this page is removed? |

If `why_now`, `next_dependency`, or `removal_consequence` is empty, merge, move, or delete the page.

## 5. Run the hard gates

### Buyer-recognition gate

- The opening names a concrete work situation, decision, risk, or desired change.
- For a company-introduction or break-ice deck, the opening also states what the company changes or produces in those situations. An industry-level “why has the market not changed?” question does not pass by itself.
- The reader does not need to accept the author's terminology before understanding the problem.
- The first page says what the company changes in the reader's world, not only what the company believes.

### Early-proof gate

- A real proof anchor appears by page 3 in a break-ice deck.
- No more than two consecutive pages are theory-only.
- For an unfamiliar brand, proof precedes or immediately follows the first major insight.

### Causality gate

- Each page answers a question raised by the preceding page.
- Swapping adjacent pages damages the argument. If it does not, the pages are probably parallel points.
- Removing a page creates a named gap. If it does not, delete or merge it.
- A taxonomy does not interrupt the main causal chain unless the reader needs it to make the next decision.
- After the last case/evidence page, allow at most two non-evidence pages: one earned synthesis/implication and one company/decision close. A third summary page is presumptively redundant.
- Do not introduce an organization-level name or conclusion until at least two materially different cases have exposed the shared management problem it names.

### Claim-evidence adjacency gate

- Put proof beside the claim it supports; do not postpone all evidence to a late case section.
- Do not use cases merely to illustrate a theory already declared true.
- State observable change before generic value language.
- Keep deployed use, MVP, engineering asset, collaborative sample, and proposed solution distinct.

### Artifact-process-system gate

Classify what an artifact can actually prove before writing the case page:

- **Observed result**: a sample, screenshot, report, or finished file proves that this result exists. It does not by itself prove how it was produced.
- **Documented process**: logs, source files, operating records, handoff materials, or reproducible steps may support a process claim. State whether the process was observed, reconstructed, or merely proposed.
- **Implemented system**: runnable code, interfaces, stored state, model or tool calls, tests, or deployment evidence may support a system claim at the verified maturity level.
- **Business effect**: efficiency, revenue, conversion, quality improvement, adoption, or organizational change requires corresponding outcome evidence; a product or sample is not enough.

Do not promote an observed result into a documented process, an assumed process into an implemented system, or an implemented system into a business effect. If the available artifact only proves the result, describe the surrounding process as a requirement, production logic, or delivery method—not as a verified feature of that case.

### Term-debt gate

- Every new term must remove more confusion than it creates.
- Introduce a term only after the reader understands the underlying problem.
- Define terms through a concrete example or visible operation, not a second abstraction.
- Do not give separate pages to terms that can be explained inside one case or mechanism page.

### Ending-delta gate

- The closing states what the reader now understands that was not clear on page 1.
- It identifies why this team is credible or distinctive using evidence already shown.
- It does not repeat the deck's vocabulary as a capability list.

### Adversarial merge/delete challenge

Do not accept a page's self-written `PASS` explanation at face value. Before declaring `NARRATIVE_PASS`:

1. Name the strongest candidate pair to merge and the strongest candidate page to delete.
2. Draft the merged/deleted sequence in one or two sentences.
3. Compare what the shorter sequence loses.
4. Keep the original only when the loss is specific, material to the reader's decision, and not recoverable on an adjacent page.
5. If the defense relies on “completeness,” “rhythm,” “professionalism,” or “this page summarizes,” mark it `NEEDS_WORK`.

When the same writer both creates and audits the deck, perform this challenge as an adversarial second pass and default ambiguous calls to `NEEDS_WORK`. Prefer independent review when another reviewer or thread is available.

## 6. Use a fixed case grammar

Every client case must answer, in this order:

1. **Situation**: Who was doing what recurring work?
2. **Failure or friction**: What concrete step, risk, delay, inconsistency, or handoff problem existed?
3. **Intervention**: What did the system actually read, compare, generate, call, record, or route?
4. **Human responsibility**: Where did a person judge, approve, edit, or own the final result?
5. **Observable after**: What formal artifact, system state, trace, reusable rule, or changed handoff now exists?
6. **Evidence surface**: Product screenshot, formal deliverable, run record, source trace, test, or usage statement.
7. **Status and boundary**: Deployed, MVP, prototype, engineering asset, collaborative sample; state what is not verified.

Avoid generic labels such as “案例价值” or “这个案例证明” when the visible before/after and evidence can carry the conclusion.

## 7. Small-brand rule

For an unfamiliar company or studio:

- Lead with a recognizable work problem and an unusually concrete proof anchor.
- Extract insight from the case; do not spend a long opening teaching the market.
- Use professional judgment to explain why the work changed, then show that the same method travels across cases.
- Close on the team's demonstrated combination of business understanding, product engineering, AI engineering, and responsibility design.

## 8. Handoff rule

Do not begin slide layout, HTML/PDF building, image generation, or visual-system optimization until:

- the narrative contract is complete;
- the causal page ledger has no empty required fields;
- the early-proof, causality, claim-evidence, term-debt, and ending-delta gates pass;
- case evidence and disclosure boundaries are mapped.

When the narrative changes after visual work begins, invalidate all downstream page-task and layout contracts from the first changed page. Rebuild them; do not patch copy into the old layout.

## 9. Release labels

Use these labels separately:

- `NARRATIVE_PASS` / `NARRATIVE_BLOCKED`
- `EVIDENCE_PASS` / `EVIDENCE_BLOCKED`
- `LANGUAGE_PASS` / `LANGUAGE_BLOCKED`
- `EXTERNAL_BOUNDARY_PASS` / `EXTERNAL_BOUNDARY_BLOCKED`
- `PRODUCTION_PASS` / `PRODUCTION_BLOCKED`

Only call a deck externally releasable when all five pass.

`NARRATIVE_PASS` applies to the reviewed artifact level only. A page ledger can pass while actual page copy, layout, or final deck remains blocked; re-run the gate whenever the artifact advances or the story changes.
