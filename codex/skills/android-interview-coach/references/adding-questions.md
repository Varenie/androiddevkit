# Adding questions to the bank

Use this workflow only when the user asks to add or save a question.

## Choose and research

- For a user-provided question or notes, preserve the intended concept and ask only if its topic or target level cannot be inferred.
- For an online source, inspect the link and prefer authoritative Android, Kotlin, or library documentation. Write an original interview question and an original explanation; do not copy a source's prose or a proprietary interview question bank. Add source links under a `## Sources` heading in the answer.
- Check `src/content/topics/` and use an existing topic ID. Propose a new topic only when none fit.
- Keep the question focused on one concept. Use difficulty `junior`, `mid`, or `senior`.

## Write the entry

By default, create one Markdown file in the private repository's `questions/` directory, with a short stable slug. Use this frontmatter shape:

```yaml
---
question: "How does repeatOnLifecycle restart collection?"
topic: coroutines
difficulty: mid
order: 100
starred: false
section: "Lifecycle"
tags: ["lifecycle", "coroutines"]
---
```

The body is the reference answer. Explain the mechanism, a useful example, and relevant limits. Keep it between 80 and 650 words, with scannable structure and balanced code fences. Do not add personal progress or interview answers to this question file.

## Save and validate

For private questions, review the diff and run `python3 /Users/aleksandr/Documents/skifProjects/android-interview-coach-data/scripts/sync.py save` to sync it. If the user explicitly asks to contribute the question publicly, add it under `src/content/questions/` in the public fork, run `npm run content:check` as required by repository guidance, and commit/push there. Review every diff for source attribution and accidental personal details.
