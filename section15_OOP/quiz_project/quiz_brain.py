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

    def next_question(self):
        self.question_number += 1
        return input(f"Q.{self.question_number} {self.question_list[self.question_number - 1].text}, so the answer is (True/False) : ")

    def still_has_question(self):
        return self.question_number < len(self.question_list)
            
    def check_answer(self, user_ans):
        if self.question_list[self.question_number - 1].answer == user_ans:
            self.scores += 1
            print(f"You got it right!!, the answer is {self.question_list[self.question_number - 1].answer}")
            print(f"Your current scores is {self.scores}/{self.question_number}")
        
        else:
            print(f"Incorrect!!!, the answer is {self.question_list[self.question_number - 1].answer}")
            print(f"Your current scores is {self.scores}/{self.question_number}")


        






    
        