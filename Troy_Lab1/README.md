
Python Quiz game:

Key Python Concepts Used:
- Parallel Lists: questions, options, and answers share matching indices to seamlessly link data.
- Nested Loops: An outer for loop cycles through questions while an inner loop displays formatting choices.
- String Sanitization: .strip().upper() avoids errors from trailing whitespace or mixed casing.
- Replay Logic: A conditional while True loop keeps the application active until the player explicitly exits

Open your terminal or command prompt, navigate to the folder, and run:

execute in bash:
python quiz_game.py

-------------------
### Overview

This code creates a simple text-based quiz game focused on Python programming. The user is presented with multiple-choice questions, and their answers are evaluated to calculate their score.

### Code Breakdown

1. **Function Definition: `run_quiz()`**
   - This function contains the main logic for the quiz. Everything inside this function will run whenever it's called.

2. **Setting Up Questions and Options**
   - We define three lists: `questions`, `options`, and `answers`.
     - `questions`: Contains the quiz questions.
     - `options`: Each sublist here has the multiple-choice answers corresponding to each question.
     - `answers`: Stores the correct answer for each question as a letter (A, B, C, or D).

3. **Variables Initialization**
   - `guesses`: An empty list to keep track of the user's answers as they play.
   - `score`: A counter to keep track of how many questions the user answered correctly. It starts at `0`.

4. **Welcome Message**
   - A welcome message is displayed when the quiz starts.

5. **Looping Through Questions**
   - Using a `for` loop to iterate through each question:
     - `print(f"\nQuestion {i + 1}: {questions[i]}")`: Displays the current question number and text.
     - A nested loop (`for option in options[i]`) prints each answer option for that question.

6. **Collecting User Input**
   - `guess = input("Your Answer (A, B, C, or D): ").strip().upper()`: 
     - Prompts the user to enter their answer.
     - `.strip()` removes any extra spaces around the input.
     - `.upper()` converts their input to uppercase for consistency.

7. **Evaluating User Answers**
   - The user's guess is added to the `guesses` list.
   - An `if-else` statement checks if the guess matches the correct answer:
     - If correct, a message "✨ Correct!" is printed, and `score` is incremented by 1.
     - If incorrect, it informs the user of the correct answer.

8. **Calculating and Displaying Results**
   - After all questions are answered, it computes the user's score as a percentage.
   - This is shown in the
