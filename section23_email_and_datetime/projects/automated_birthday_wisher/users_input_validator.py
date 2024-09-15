
class UsersInputValidator():
    def validate_yes_and_no_answer(self, answers):
        if answers != 'y' and answers != 'n':
            raise ValueError("Invalid input!!!. Only 'y' and 'n' are allowed.")