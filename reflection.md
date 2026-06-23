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
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
