# Large Document Coverage

Use this when rewriting multi-page documents, decks, Feishu documents, Docx files, long Markdown drafts, or any artifact with many headings, tables, captions, repeated blocks, or versions.

Large-document failure usually comes from editing only the visible prose. Titles, table cells, captions, footnotes, appendix notes, and repeated phrases keep the old voice.

## Source Inventory

Before editing, inventory the source. For Markdown, text, XML, or HTML sources, run:

```bash
python3 scripts/audit_surfaces.py <source-file> --output <inventory.json>
```

For PDF, PPTX, Docx, Feishu, or Wiki sources, use the relevant format/document skill to extract all readable text first. Include slide text, table cells, speaker notes when relevant, chart labels, captions, headers, footers, callouts, and text inside images when it affects the visible口径. The audit script is a backstop, not proof that the language is correct.

Record at minimum:

- page or section count
- heading/title count
- table and meaningful cell count
- caption/note/footnote count
- visuals containing text
- unreadable, locked, or intentionally excluded surfaces

## Coverage Ledger

Before editing, create an internal coverage map:

```text
Page/Section:
- role:
- must preserve:
- rewrite scope: L1 / L2 / L3 / L4
- surfaces to review: title / opening / body / table / caption / note / CTA / visual text
- risky old口径:
- scene register:
- status: pending / reviewed / excluded
- exclusion reason:
```

Keep the ledger internal unless requested. It records coverage; a reviewed section can still fail the reader's task.

## Surface Order

Edit in this order:

1. Document title and subtitle
2. Page/section titles
3. Opening judgment sentences
4. Body paragraphs
5. Tables, including column names and every meaningful cell
6. Captions, footnotes, assumptions, and publishing notes
7. Summary, appendix, version notes, and acceptance criteria

Tables need special attention: a table cell that says only "承接 / 放大 / 沉淀 / 触达 / 占位" usually needs an object, action, or metric.

## Consistency Pass

After editing, check:

1. **Meaning and revisions:** compare required facts, relationships, numbers, and claim strength with the source. Trace corrections across analogous passages and obsolete wording; fidelity does not require irrelevant drafting history.
2. **Reader fit:** read without editing notes. Check each section's contribution, language, and speaking position, including retained text. Apply `external-facing-check.md` for material handed to others; execution correctness alone is insufficient.
3. **Coverage:** verify every inventoried surface was reviewed or excluded. Strategy, execution, budget, and appendix pages need not sound identical.

## When Replacing A Live Document

If updating a live Feishu/Docx/wiki document:

- Prefer generating a clean source draft first.
- Replace the whole document only when the source draft is internally consistent.
- After update, read back the live document and search for old terms, old numbers, and internal口径.
- If images or charts contain text, inspect or regenerate them too; otherwise the old voice remains in visuals.
- Compare the live read-back against the clean source draft. Do not treat a successful update command as proof that every block was replaced.

## Stop Rule

Do not report the rewrite as complete until:

- every inventoried page or section is reviewed or explicitly excluded
- no high-severity residual from the AI-trace and register checks remains
- user-rejected patterns have been scanned across the whole artifact
- facts, numbers, names, and evidence levels still match the source
- unreadable visual or locked content is disclosed

If one of these checks cannot be completed, state the limitation instead of claiming the whole document was checked.

## Final Report

Deliver the revised artifact. Report unreadable or excluded surfaces when they affect its use; provide detailed coverage and check results only when requested. Follow the output contract in `SKILL.md` rather than appending a routine audit report.
