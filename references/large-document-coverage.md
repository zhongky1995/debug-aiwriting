# Large Document Coverage

Use this when rewriting multi-page documents, decks, Feishu documents, Docx files, long Markdown drafts, or any artifact with many headings, tables, captions, repeated blocks, or versions.

Large-document failure usually comes from editing only the visible prose. Titles, table cells, captions, footnotes, appendix notes, and repeated phrases keep the old voice.

## Coverage Map

Before editing, create an internal coverage map:

```text
Page/Section:
- role:
- must preserve:
- surfaces to edit: title / opening / body / table / caption / note / CTA
- risky old口径:
- scene register:
```

Do not output this map unless the user asks. Use it to prevent skipped surfaces.

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

After editing, run three checks:

1. **Old口径 scan**: search for old project words, old version labels, prior numeric targets, internal labels, and terms the user disliked.
2. **Register scan**: check whether all pages still belong to the same scene. A strategy page should not suddenly sound like chat, and a whitepaper page should not become an internal memo.
3. **Coverage scan**: verify each page/section has had its title, opening, body, and table reviewed.

## When Replacing A Live Document

If updating a live Feishu/Docx/wiki document:

- Prefer generating a clean source draft first.
- Replace the whole document only when the source draft is internally consistent.
- After update, read back the live document and search for old terms, old numbers, and internal口径.
- If images or charts contain text, inspect or regenerate them too; otherwise the old voice remains in visuals.

## Final Report

When reporting back, mention:

- what artifact was updated
- which sections/pages were covered
- what checks were run
- any surface intentionally not changed, such as images, locked blocks, or source data tables
