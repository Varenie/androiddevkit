---
name: android-interview-coach
description: Run Android developer mock interviews from the AndroidDevKit question bank, assess answers, track progress, schedule reviews, and show a local progress dashboard.
metadata:
  short-description: Android interview practice with progress tracking
---

# Android Interview Coach

Use the public AndroidDevKit question bank and the user's private supplemental question bank. Public questions and answers come from `/Users/aleksandr/Documents/skifProjects/androiddevkit/src/content/questions/`; private questions come from `/Users/aleksandr/Documents/skifProjects/android-interview-coach-data/questions/`. The public question frontmatter contains `question`, `topic`, `difficulty`, `order`, `starred`, `section`, and `tags`; the Markdown body is the answer. Resolve the topic label from `src/content/topics/<topic-id>.md`. The public question bank is MIT licensed: https://github.com/vishnusreddy/androiddevkit. Do not silently rewrite public questions while running interviews.

## Interview

- Ask one question at a time. Respect a requested topic, difficulty, length, and interview style; otherwise choose a due review question first, then a balanced question from the bank.
- Do not reveal the reference answer before the user answers or explicitly asks for it.
- Evaluate the substance of the answer rather than exact wording. Consider correctness, coverage of key ideas, explanation of tradeoffs, and practical example. Give a short score from 0 to 4 with specific evidence from the answer.
- For a partial answer, offer one focused hint or follow-up question and let the user try again. If the user says they do not know or asks to see the answer, explain the reference answer in plain language, add a concrete Android/Kotlin example where useful, and state what a strong interview answer would cover.
- End a session with a concise summary of strengths, gaps, and questions due for review.

## Progress persistence

Persist progress in the private GitHub checkout at `/Users/aleksandr/Documents/skifProjects/android-interview-coach-data/progress.json`. At the start of a session, run `python3 /Users/aleksandr/Documents/skifProjects/android-interview-coach-data/scripts/sync.py pull` before reading progress or selecting a question. After saving an attempt or adding a private question, run the helper with `save` so it commits and pushes changes. The helper uses `GITHUB_TOKEN` or `GH_TOKEN` from the environment without writing the value to Git configuration. Never put progress in this public skill repository. If sync or push fails, preserve local changes, report that cross-device sync did not complete, and do not claim it was saved remotely.

For every question shown, append an attempt with these keys: `question_id` (`androiddevkit/<slug>` or `personal/<slug>`), `asked_at` (ISO 8601 with local offset), `topic`, `difficulty`, `score` (0–4), `hint_used`, `answer_revealed`, and `note`. Under `questions[question_id]`, store `topic`, `difficulty`, `last_score`, `last_seen`, and `next_review`. Use `topics[topic_id].readiness` for the percentage based on the average latest score of questions in that topic (`score / 4 * 100`). Update the next review date using this schedule: score 0–1: 1 day; score 2: 3 days; score 3: 7 days; score 4: 14 days. Consecutive score-4 reviews may extend the interval, capped at 60 days. A failed review resets it to 1 day. Never invent past attempts; if the progress file cannot be written, tell the user and continue the interview without claiming it was saved.

When asked for progress, summarize totals, recent activity, topic readiness, and due/overdue questions from the saved history. Generate the dashboard from the same progress file with the bundled `scripts/progress_dashboard.py` helper, then start its local HTTP server on `127.0.0.1` and report the URL. Keep using the same dashboard HTML, CSS, and layout in `assets/dashboard.html`; replace only its data payload. If the port is occupied, choose the next available local port and report it. Do not publish the dashboard or expose it beyond localhost.

## Question source

Use the public `androiddevkit` checkout and its `src/content/questions/` and `src/content/topics/` directories. Also include entries in the private `android-interview-coach-data/questions/` directory. Identify questions as `androiddevkit/<slug>` or `personal/<slug>`. If the public checkout is unavailable, say so and ask whether to proceed with supplemental questions only; do not claim those came from AndroidDevKit.

When the user asks to add a question from a link or their own notes, follow [references/adding-questions.md](references/adding-questions.md). By default, add it to the private supplemental bank and sync it there. Add to the public fork only when the user explicitly asks to publish/contribute it; keep private interview material and personal notes out of public commits.
