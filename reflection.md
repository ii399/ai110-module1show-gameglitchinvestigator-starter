# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The first time I ran the game, it opened to the Game Glitch Investigator screen with a dark theme. The left side showed a Settings panel with the difficulty set to Normal, a range of 1 to 100, and 8 attempts allowed. The main screen asked me to guess a number between 1 and 100, but it already showed 7 attempts left even though I had not entered a guess yet. I also saw a text box to enter my guess, Submit Guess and New Game buttons, a checked Show hint option, and a collapsed Developer Debug Info section.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Bug 1: The Settings panel said there were 8 attempts allowed, but the game started with only 7 attempts left.

Expected: I expected the game to start with all 8 attempts available.
Actual: It started with only 7 attempts left before I even made a guess.

Bug 2: It looked like one attempt had already been used when the game first loaded.

Expected: I expected a new game to begin without using any attempts.
Actual: The game acted as if one attempt had already been used even though I hadn't done anything yet.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | |6|2|When difficulty = Normal, The game should start with all 8 attempts available.|The game started with only 7 attempts left even though I had not made a guess.|None
| | |1|8|When difficulty = (Easy or hard), the guess prompt should also be updated to match the selected range|Setting panel changed to respective range but guess prompt stayed on the Normal setting range|None
| | |4|8|The secret number was, 34 Hint should state "Go Lower"|Hint stated "Go Higher"|None

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
Claude Code

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
What the AI suggested:
TThe AI suggested checking the comparison logic for the hint messages because the game was displaying the wrong hint when a guess was entered.

Was it correct?
Yes. The suggestion was correct. The conditions for the "Go higher" and "Go lower" hints were reversed.

How I verified it:
I entered guesses that were both lower and higher than the secret number and checked the hints that were displayed. After updating the comparison logic, the game correctly displayed "Go higher" for guesses that were too low and "Go lower" for guesses that were too high.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
What the AI suggested:
The AI suggested that the Show Hint checkbox being checked by default might be a bug.

Was it correct?
No. After testing the game, I realized this appeared to be a design choice rather than a bug because it did not affect how the game worked.

How I verified it:
I tested the game with the checkbox both checked and unchecked. The game behaved as expected, so I did not include this as one of the bugs in my report.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided the bug was fixed by repeating the same steps that had exposed it. I made a guess that was lower than the secret number and checked that the game displayed "Go higher." Then I made a guess that was higher than the secret number and checked that it displayed "Go lower." Since the game gave the correct hint in both cases, I knew the bug had been fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
One test I ran was entering a guess that I knew was lower than the secret number and checking the hint that was displayed. Before the fix, the game told me to "Go lower," which was incorrect. After fixing the code, I repeated the test and the game correctly displayed "Go higher." I also tried a guess that was higher than the secret number to make sure it displayed "Go lower," which confirmed that the comparison logic was working correctly.

I also used pytest to verify that the "Go higher"/"Go lower" bug was fixed. I ran the test after the logic was updated, and it passed successfully. The test checked that the game returned "Go higher" when the guess was lower than the secret number and "Go lower" when the guess was higher. Since the test passed, I was confident that the hint logic was working correctly.

- Did AI help you design or understand any tests? How?
Yes. The AI helped me understand what cases I should test to make sure the hint logic was correct. It suggested testing both a guess that was lower than the secret number and a guess that was higher than the secret number. I used those suggestions to create my pytest test cases and verified that the game returned the correct hint in each situation.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain it by saying that every time you click a button or interact with a Streamlit app, it runs the whole script again from top to bottom. This is called a rerun. Session state is like the app's memory because it keeps track of values, such as scores or user input, even though the script is running again. Without session state, the app would forget everything each time it reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to keep using is testing each fix as soon as I make it instead of waiting until the end. This project showed me that checking one change at a time makes it easier to find new bugs and confirm that I didn't break something else. I also plan to continue using Git to save my progress regularly so I can go back to an earlier version if needed.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would ask the AI for smaller, more focused suggestions instead of trying to solve several issues at once. That would make it easier to understand each change and verify that it fixed only the bug I was working on. I also want to test each suggestion immediately before moving on so I can catch any new issues early.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project showed me that AI can be a helpful tool for finding bugs and suggesting fixes, but I still need to test and verify everything it recommends. I learned that AI-generated code and advice are useful starting points, not something I should trust without checking.