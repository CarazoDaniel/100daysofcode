from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"],i["correct_answer"]))

quizz = QuizBrain(question_bank)
while(quizz.still_has_questions()):
    quizz.next_question()
print('This quizz is finished')
print(f'your final score is: {quizz.score}/{quizz.question_number}')