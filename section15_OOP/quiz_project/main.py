# https://replit.com/@appbrewery/quiz-game-final
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
# Create a list of the Question objects called question_bank, using the data from question_data
question_bank = []
for each_object in question_data:
    question_bank.append(Question(each_object["text"], each_object["answer"]))
# Instantiate QuizBrain object and pass the question_bank to it
quizbrain = QuizBrain(question_bank)

# Use the QuizBrain object to finish the program. Apart from the QuizBrain object, you will only need one while loop to complete

def print_final_scores():
    print("You've finished this quiz.")
    print(f"You final score is {quizbrain.scores}/{quizbrain.question_number}.")

while quizbrain.still_has_question():  
        user_ans = quizbrain.next_question()
        quizbrain.check_answer(user_ans)


print_final_scores()