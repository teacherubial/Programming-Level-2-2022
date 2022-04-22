# Introduction to Python

import time
import random


def main():
    # A quiz application
    # Create some questions
    # Create a list that is 2-dimensional
    # question_one = "What is the colour of the sun? "

    # Questions is a 2-dimensional list
    # First part is the question
    # Second part is the answer
    questions = [
        ("What is the colour of the sun? ", "yellow"),
        ("How many things are in a dozen? ", "12"),
        ("How many things are in a baker's dozen? ", "13"),
        ("What is Spider-Man's real name? ", "peter")
    ]

    score = 0

    random.shuffle(questions)

    # Introduction
    print("Welcome to the quiz. 💡")
    print("Answer the questions to the best of your ability.")

    time.sleep(2)

    # Ask the questions and get the answer
    for question in questions:
        # question -> question[0]
        # answer -> question[1]
        user_answer = input(question[0]).strip(",.?!").lower()

        print("\nChecking answer...")
        time.sleep(2)
        # See if the user's correct
        if user_answer == question[1]:
            print("YOU GOT IT RIGHT!\n")
            score += 1
        else:
            print("Sorry, you didn't get it right.")
            print(f"The answer was {question[1].capitalize()}.\n")

    time.sleep(2)
    if score == 1:
        print(f"You got 1 question correct.")
    else:
        print(f"You got {score} questions correct.")


if __name__ == "__main__":
    main()
