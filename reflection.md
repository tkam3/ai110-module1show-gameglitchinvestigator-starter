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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - I told it that even after I clicked "New Game" I still couldn't make a guess. It pointed me to the New Game button and said the problem was that starting a new game didn't actually mark the game as "playing" again, so the code still thought I'd already won. That made sense to me. After the fix I just played it: won a round, started a new game, and this time it let me keep guessing instead of being stuck on the "you already won" message.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - At one point I noticed when I get it right I only get 80 points. Then I asked AI tools. Then it said the logic is wrong and fixed it. When I play again, I noticed the score is still 80, but if you guess it wrong one time, score will -5. I know AI is misleading.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - Mostly by going back and playing the game the same way that broke it. For the hint bug I'd guess a number I knew was too high and check it told me to go lower. For the "can't win" one I'd guess the secret on purpose and see if it actually let me win. If it behaved the way I expected, I called it fixed. 
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  - I ran the project tests using pytest to verify the game logic. One test checked that the game correctly recognized a winning guess and updated the game state appropriately. The successful test results showed that my implementation behaved as expected and that the core functionality of the guessing game was working correctly.
- Did AI help you design or understand any tests? How?
  - Yeah but not really. I asked it to write some tests and to throw in edge cases, and it thought of stuff I wouldn't have, like typing nothing or typing letters instead of a number. I try to read through them but mostly I just follow it blindly.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - Every time you click a button or type something, Streamlit just runs the whole file again from the top, kind of like refreshing the page. So a normal variable gets wiped and forgets what it was. Session state is the little box where you keep the stuff you want to remember between those reruns, like the secret number, the score, and whether you already won. A couple of the bugs were basically the game forgetting or not resetting things because they weren't handled right in session state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
