def run_quiz():
    # 1. Setup questions and options
    questions = [
        "What is the correct file extension for Python files?",
        "Which keyword is used to create a function in Python?",
        "What is the output of print(2 ** 3) in Python?"
    ]

    options = [
        ["A. .pt", "B. .py", "C. .pyt", "D. .txt"],
        ["A. function", "B. void", "C. def", "D. method"],
        ["A. 6", "B. 8", "C. 9", "D. 5"]
    ]

    answers = ["B", "C", "B"]
    guesses = []
    score = 0

    print("--- WELCOME TO THE PYTHON QUIZ ---")

    # 2. Loop through questions
    for i in range(len(questions)):
        print(f"\nQuestion {i + 1}: {questions[i]}")
        
        # Print choices for the current question
        for option in options[i]:
            print(option)

        # Collect user input safely
        guess = input("Your Answer (A, B, C, or D): ").strip().upper()
        guesses.append(guess)

        # Evaluate the user's answer
        if guess == answers[i]:
            print("✨ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {answers[i]}.")

    # 3. Calculate and display final results
    print("\n--- QUIZ RESULTS ---")
    percent_score = int((score / len(questions)) * 100)
    print(f"Your Final Score: {score}/{len(questions)} ({percent_score}%)")
    
    if percent_score == 100:
        print("Perfect score! You are a Python expert! 🐍")
    elif percent_score >= 50:
        print("Good job! Keep practicing. 👍")
    else:
        print("Better luck next time! 📚")


def main():
    # Loop to handle replay logic
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes" and play_again != "y":
            print("\nThank you for playing! Goodbye.")
            break


# Start the game
if __name__ == "__main__":
    main()
