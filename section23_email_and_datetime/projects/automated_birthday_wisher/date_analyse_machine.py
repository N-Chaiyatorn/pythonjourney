import datetime as dt

class DateAnalyseMachine():
    def __init__(self):
        pass

    def is_leap_years(self, birth_years):
        if birth_years % 4 == 0 and birth_years % 400 == 0:
            return True
        elif birth_years % 100 != 0 and birth_years % 4 == 0:
            return True
        else:
            return False
        
    def get_user_today_birthday_dataframe(self, data_frame, now):
        related_birth_month_dataframe = data_frame[data_frame["month"] == now.month]
        return related_birth_month_dataframe[related_birth_month_dataframe["day"] == now.day]