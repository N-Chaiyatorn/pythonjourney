
import pandas as pd
import datetime as dt

class DataFrameUtils():
    def __init__(self):
        self.related_birthday_dataframe = None
        self.to_be_send_mail_users_dataframe = None

    def gets_initial_data_frame(self, birthday_data_file):
        try:
            data_frame = pd.read_csv(birthday_data_file)
        except pd.errors.EmptyDataError:
            data_frame = self.get_empty_data_frame()

        return data_frame

    def is_reset_data_frame(self, users_input_validator):
        reset_data = input("Do you want to reset all data from your data file? (y/n): ")

        users_input_validator.validate_yes_and_no_answer(reset_data)
            
        if reset_data == 'y':
            return True
        elif reset_data == 'n':
            return False
    
    def get_empty_data_frame(self):
        col_name = ["name", "email", "birthdays"]
        data_dict = {}
        
        data_dict = {col:[] for col in col_name}
        
        return pd.DataFrame(data_dict)

    def add_new_row_data_to_data_frame(self, user, data_frame):
        data_frame.loc[len(data_frame)] = [user.name, user.email, user.birthdays]

        return data_frame

    def update_users_today_birthday_dataframe(self, data_frame):
        now = dt.datetime.now()
        for (index, row) in data_frame.iterrows():
            user_birthday = dt.datetime.strptime(row.birthdays, "%Y-%m-%d")
            if now.month == user_birthday.month and now.day == user_birthday.day:
                self.related_birthday_dataframe = pd.concat([self.related_birthday_dataframe, pd.DataFrame(data_frame.loc[index]).T])
              
    def set_to_be_send_email_users(self):
        for (index, row) in self.related_birthday_dataframe.iterrows():
            if row.email != "none":
                self.to_be_send_mail_users_dataframe = pd.concat([self.to_be_send_mail_users_dataframe, pd.DataFrame(self.related_birthday_dataframe.loc[index]).T])




        

        