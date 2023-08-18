import datetime as dt

class DateUtils():   # ควรใช้ DateAnalyser  
    def is_leap_years(self, birth_years):
        if birth_years % 4 == 0 and birth_years % 400 == 0:
            return True
        elif birth_years % 100 != 0 and birth_years % 4 == 0:
            return True
        else:
            return False
        
    
    def get_user_birthday(self, user_name):
        print("Type your birthday in this below.")

        user_birthday = input(f"Type {user_name} birthdays in format (YYYY-MM-DD): ")
        
        return user_birthday