import os

class User():
    def __init__(self):
        self.name = ""
        self.ages = ""
        self.id_cards = ""
        self.height = ""
        self.weight = ""
        self.purpose = ''
        self.encoded_password = ''
        self.decoded_password = ''

    def type_info(self):
        while True:

            try:
                self.name = input("Type your names: ")
                self.ages = int(input("Type your ages: "))
                self.id_cards = int(input("Type your id cards: "))
                self.height = int(input("Type your height (cm): "))
                self.weight = int(input("Type your weight (kg): "))

            except ValueError:
                print("Please type again!!!.\nIt seems your submit is invalid.")
                
            else:
                break

    def ask_user_purpose(self):
        while True: 
            try:
                self.purpose = input("Do you want to encode or decode your password? (e/d): ")
                os.system('cls')
                if self.purpose != 'e' and self.purpose != 'd':
                    raise ValueError("Error!!")
            except ValueError:
                print(f"Your submited is invalid. Please type 'e' for encoding and 'd' for decoding.")
            else:
                break


       


