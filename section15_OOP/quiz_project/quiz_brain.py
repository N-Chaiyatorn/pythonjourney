# Create QuizBrain class which have three attributes, question_number, question_list and scores
# Initialize question_number to 0, question_list to the input, scores to 0

# implement the method called next_question, use the input function to show the question to the user and ask for the user answer

# implement the method called still_has_question which return Boolean, return True if there are the questions left and False if all the questions are asked

# implement the method called check_answer which will check the answer and updscoate the score, also print the correct answer and current score to the user

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.scores = 0

    def next_question(self, question_number, question_list):
        
        return input(f"Q.{question_number} {question_list}, so the answer is (True/False) : ")

    def still_has_question(self, question_number, question_amount, current_score):
        if question_number < question_amount:
            return True
        else:
            print("You've finished this quiz.")
            print(f"You final score is {current_score}/{question_amount}.")
            return False

    def check_answer(self, actual_ans , input_question_ans, question_number, current_score):
        if actual_ans == input_question_ans:
            current_score += 1
            print(f"You got it right!!, the answer is {actual_ans}")
            print(f"Your current scores is {current_score}/{question_number}")
            return current_score
        else:
            print(f"Incorrect!!!, the answer is {actual_ans}")
            print(f"Your current scores is {current_score}/{question_number}")
            return current_score

        






    
        