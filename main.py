from question_model import Question
import data
from quiz_brain import quiz

# read question data from external module and add to Question class
for q in data.question_data:
    Question.add_question(q['text'], q['answer'])

# print out all the added questions and answers
Question.list_questions()

# Play the quiz

quiz()

