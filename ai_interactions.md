# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompt(s) used:**

```
Identify three edge-case inputs (e.g. negative numbers, decimals, extremely large
values) that might still break my guessing game, then write a suite of pytest cases
that verify the game handles them gracefully. Run them and show the output.
```

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number (`-7`) | (prompt above) | `test_negative_number_is_handled` | ✅ Yes | A player could type a negative number; it should parse and be treated as "Too Low", not crash. |
| Extremely large number (`99999999999999999999`) | (prompt above) | `test_extremely_large_number_is_handled` | ✅ Yes | A huge value far outside the range should parse and read "Too High" instead of overflowing or erroring. |
| Whitespace-padded number (`"  42  "`) | (prompt above) | `test_whitespace_padded_number_is_handled` | ✅ Yes | Copy/paste often adds stray spaces; the input should still parse to the right number, not be rejected. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
