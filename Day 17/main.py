from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

my_quiz = QuizBrain(question_bank)

while my_quiz.still_has_questions():
    my_quiz.next_question()

print("You have completed the Quiz!")
print(f"Your Final Score was : {my_quiz.score}/{my_quiz.question_number}")