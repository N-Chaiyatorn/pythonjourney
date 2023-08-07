import os

class User():
    def __init__(self):
        self.name = ''
        self.email = ''
        self.year = ''
        self.month = ''
        self.day = ''
    
    def input_data(self, date_analyse_machine, days_of_month):
        self.name = input("Type name: ")
        
        self.email = input(f"Type {self.name} email address (If {self.name} don't have please type 'none'): ")
        os.system('cls')

        if "@" not in list(self.email) and self.email != 'none':
            raise ValueError(f"Invalid email input, your input is {self.email}. So it require '@'.")
                
        while True:
            try:
                print("Type your birthday in this below.")
                self.day = int(input(f"Type {self.name} birthday: "))
                self.month = int(input(f"Type {self.name} birth month: "))
                self.year = int(input(f"Type {self.name} birth years: "))
                os.system('cls')

                is_leap_years = date_analyse_machine.is_leap_years(birth_years = self.year)

                if self.year > 5000:
                    print("Your years input is invalid, Only allowed years around 0-5000.")
                    raise ValueError()
            
                if is_leap_years:
                    if self.month == 2 and self.day > 29:
                        raise ValueError("Invalid days!!!")
                    elif self.month != 2 and self.day > days_of_month[self.month - 1]:
                        raise ValueError("Invalid days input.")
                elif not is_leap_years and self.day > days_of_month[self.month - 1]:
                    raise ValueError("Invalid days input.")
            
                if self.month > 12:
                    raise ValueError("Invalid month input.")
            except ValueError:
                print("Invalid format in your's birthday, please type again.\n")
            else:
                break