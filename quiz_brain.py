
from question_model import Question
import random

def quiz():
    """
    Prompts the user with 10 random questions from the Question class, keeps track of their answers, and displays the number of correct/incorrect answers at the end.
    """
    # shuffle the list of questions to make the order random
    random.shuffle(Question.questions)

    # initialize answer counters
    correct_answers = 0
    incorrect_answers = 0

    # iterate over the first 10 shuffled questions
    for i, q in enumerate(Question.questions[:10], start=1):
        # prompt the user with the question number and question text, and ask for their answer
        print(f"Question {i}: {q.question}")
        answer = input("True/False or Yes/No? ").lower()

        # convert "yes" or "no" to "true" or "false"
        if answer == "yes":
            answer = "true"
        elif answer == "no":
            answer = "false"

        # check if the user's answer is correct and update answer counters
        if answer == q.answer.lower():
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect.")
            incorrect_answers += 1

    # display number of correct/incorrect answers
    print(f"\nYou got {correct_answers} out of {correct_answers + incorrect_answers} correct.")
