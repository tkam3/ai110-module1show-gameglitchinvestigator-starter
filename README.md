# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
  - It's a number guessing game built with Streamlit. The app picks a secret number in a range based on the difficulty (Easy 1–20, Normal 1–100, Hard 1–200), and you try to guess it within a limited number of attempts. After each guess it tells you whether to go higher or lower and updates your score, and you can start a new game at any time.
- [ ] Detail which bugs you found.
  - The higher/lower hints were backwards — a guess that was too high told you to go higher.
  - You couldn't win on even-numbered attempts, because the secret was being compared as text instead of a number.
  - "Hard" was actually easier than "Normal" — its range was only 1–50.
  - After winning, clicking "New Game" didn't really restart the game, so it wouldn't accept new guesses.
  - The prompt always said "between 1 and 100" no matter the difficulty.
  - Winning on the first try only gave 70 points instead of 100.
  - Submitting a guess took two clicks instead of one.
- [ ] Explain what fixes you applied.
  - Moved the core logic (range, parsing, win check, scoring) into `logic_utils.py` and imported it into `app.py`.
  - Swapped the hint messages so "too high" now says go lower and vice versa.
  - Always compare the guess and secret as numbers so a correct guess always wins.
  - Widened Hard's range to 1–200 and gave it 10 attempts so it's genuinely harder.
  - Made "New Game" reset the game state (status, score, attempts, history) so you can play again.
  - Showed the actual difficulty range in the prompt instead of a hardcoded "1 and 100".
  - Fixed the off-by-one in the scoring so a first-try win is worth 100.
  - Wrapped the guess input and submit button in a Streamlit form so a single click (or Enter) submits.
  - Added pytest cases, including edge cases (empty input, letters, decimals), and confirmed they all pass.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 1
2. Game returns "Go higher"
3. User enters a guess of 100 → "Go lower"
4. Score updates correctly after each guess
5. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
