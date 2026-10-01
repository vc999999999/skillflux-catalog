---
name: code-review
description: Review code changes for concrete bugs, regressions and missing verification.
---

# Code review

Read the requested diff and surrounding callers. Trace inputs through validation, state changes and error handling. Prefer a small number of consequential findings over stylistic comments.

For each candidate finding, reproduce the trigger with a focused test or trace a specific failing execution path. Check existing constraints before claiming an issue. Review concurrency, ownership of cleanup, permission boundaries and rollback only when relevant to the changed code.

Report findings in severity order, with an exact file and line, the triggering condition, user impact and a concise repair direction. Do not implement changes unless the user asked for a fix. If no defect is supported by evidence, say so and explain the remaining test coverage limits.
