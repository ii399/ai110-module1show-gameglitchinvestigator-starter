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

- [x] Describe the game's purpose.
   The purpose of the game is to guess a randomly generated secret number within a limited number of attempts. After each guess, the game provides a hint telling the player to guess higher or lower until the correct number is found or the player runs out of attempts. The game also tracks information such as the score, guess history, and difficulty level.
- [x] Detail which bugs you found.
   The game started with 7 attempts left even though the settings showed 8 attempts allowed.
   The Go higher/Go lower hints were reversed.
   The New Game button did not reset the score.
   The New Game button did not clear the guess history.
   The New Game button did not clear the status message or Game Over message.
   New guesses were not added to the history after clicking New Game.
   Pressing the Enter key in the guess box did not submit the guess.
   Changing the difficulty to Easy updated the settings panel, but the prompt still displayed "Guess a number between 1 and 100"
   Changing the difficulty to Easy did not generate a new secret number within the 1 to 20 range.
- [x] Explain what fixes you applied.
   Corrected the Go higher/Go lower comparison logic so the hints match the player's guess.
   Fixed the game so it starts with the correct number of attempts.
   Updated the difficulty logic so changing to Easy also updates the prompt and generates a new secret number within the correct range.
## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 90<!-- Describe this step -->
2. Game returns "Go LOWER!"<!-- Describe this step -->
3. User enters a guess of 80 --> "Go HIGHER!"<!-- Describe this step -->
4. Score updates after each guess<!-- Describe this step -->
5. Game ends after I ran out of attempts, the secret was also shown, score was shown too<!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

python -m pytest .\tests\test_game_logic.py::test_too_high_hint_tells_player_to_go_lower
======================================================== test session starts ========================================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\projects\codepath\AI110\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 1 item                                                                                                                     

tests\test_game_logic.py .                                                                                                     [100%]

========================================================= 1 passed in 0.02s ============   

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
