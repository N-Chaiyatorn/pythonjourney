# https://replit.com/@appbrewery/quiz-game-final
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Create a list of the Question objects called question_bank, using the data from question_data
question_bank = question_data

# Instantiate QuizBrain object and pass the question_bank to it
quizbrain = QuizBrain(question_bank)

# Use the QuizBrain object to finish the program. Apart from the QuizBrain object, you will only need one while loop to complete
is_not_finished = True
while is_not_finished:
    question = Question(quizbrain.question_list[quizbrain.question_number]["text"], answer = quizbrain.question_list[quizbrain.question_number]["answer"])
    quizbrain.question_number += 1
    user_ans = quizbrain.next_question(quizbrain.question_number, question.text)
    quizbrain.scores = quizbrain.check_answer(question.answer, user_ans, quizbrain.question_number, quizbrain.scores)
    is_not_finished = quizbrain.still_has_question(quizbrain.question_number, len(quizbrain.question_list), quizbrain.scores)
