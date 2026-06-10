# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The game looked playable but was actually impossible to win. When I guessed too high it told me to "Go HIGHER!" and when I guessed too low it told me to "Go LOWER!", so the hints were backwards and pushed me away from the answer. Sometimes I guessed the exact number and it still said "Too High"/"Too Low" instead of letting me win. "Hard" mode felt easier than "Normal," and the range is from 1 to 50. After winning, clicking "New Game" didn't really restart, it wouldn't accept any new guesses. The score was also off: winning on the very first guess only gave 70 points instead of the 100 I expected.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret = 50, guess of 60 | "Go LOWER!" | "Go HIGHER!" | none |
| Secret = 42, guess of 42 |  Win | "Too High"/"Too Low" hint shown guess not accepted as a win | none |
| Select "Hard" difficulty | Range wider than Normal | Range shown as 1 to 50 | none |
| Win a game, then click "New Game" and submit a guess | New game accepts guesses normally | "You already won. Start a new game to play again." and submit is blocked | none (`st.stop()` halts the script) |
| Win on the first guess | Score = 100 | Score = 70 | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code.

- **A correct suggestion:** When I said I couldn't win even after starting a new game, the AI traced it to the "New Game" handler, which reset the secret and attempts but never reset `status`, so the `if status != "playing": st.stop()` guard kept blocking my guesses. It added `st.session_state.status = "playing"` to the handler. I verified it by playing the game: I won a round, clicked "New Game," and confirmed I could submit guesses again instead of being stuck on the "You already won" message.

- **An incorrect/misleading suggestion:** When I asked about scoring, the AI first told me a first-attempt win was worth 80 points. That was wrong — when we actually traced the code, the formula `100 - 10 * (attempt_number + 1)` combined with `attempts` starting at 1 produced only 70. I caught the mistake by reading the values in the "Developer Debug Info" panel and stepping through the math, and the AI corrected itself. We then fixed both off-by-one errors so a first-try win really gives 100. The lesson: even a confident AI answer about its own code can be wrong, so I verify against the running game.

---

## 3. Debugging and testing your fixes

- **How I decided a bug was really fixed:** I used two checks for every fix — a pytest assertion on the pure logic in `logic_utils.py`, and a manual play-through in the live Streamlit app. A bug only counted as fixed when both agreed.

- **A test I ran:** I moved the game logic into `logic_utils.py` and ran `pytest tests/`. The new `test_guess_too_high` checks that `check_guess(60, 50)` returns `"Too High"`, and `test_hint_messages_point_toward_secret` checks that "Too High" maps to "📉 Go LOWER!". I also added `test_first_attempt_win_scores_100` (`update_score(0, "Win", attempt_number=1) == 100`). All 6 tests (3 starter + 3 new) passed:

  ```
  6 passed in 0.06s
  ```

  This showed me the hint direction and the scoring formula were now correct without having to replay the game by hand each time.

- **How AI helped with tests:** The AI helped me see that the starter test `assert result == "Win"` expected `check_guess` to return a plain string, while the original code returned a `(outcome, message)` tuple — so the tests could never pass as written. It suggested splitting the logic so `check_guess` returns only the outcome and a separate `hint_message` function returns the emoji text. That made the existing tests pass and let me write small, focused tests for each bug.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
