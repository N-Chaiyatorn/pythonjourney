# 1. Update the birthdays.csv
import os
import pandas
import datetime as dt
from date_analyse_machine import DateAnalyseMachine
from data_file_management import DataFileManagement
from user import User
import random
import smtplib

DAYS_OF_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

reciever_email_information = {}

my_email = "pan289277@gmail.com"
password = "xvnpwhutejppterx"

birthday_data_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/birthdays.csv"
letter_1_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/letter_templates/letter_1.txt"
letter_2_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/letter_templates/letter_2.txt"
letter_3_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/letter_templates/letter_3.txt"

text_file_location_list = [letter_1_file, letter_2_file, letter_3_file]

date_analyse_machine = DateAnalyseMachine()
data_file_management = DataFileManagement()

data_frame = data_file_management.delete_index_column(birthday_data_file = birthday_data_file)

print(f"Your current data is: \n\n {data_frame}\n")
is_reset_data_frame = data_file_management.is_reset_data_frame()
os.system('cls')

if is_reset_data_frame:
    data_frame = data_file_management.reset_data_frame()

is_adding_data = data_file_management.asking_is_adding_data_to_file()

if is_adding_data:
    while True:
        user = User()
        user.input_data(date_analyse_machine = date_analyse_machine, days_of_month = DAYS_OF_MONTH)
        data_frame = data_file_management.add_data_to_dataframe(user.name, user.email, user.year, user.month, user.day, data_frame)
        is_more_data = data_file_management.is_more_data()

        if not is_more_data:
            break

    data_frame.to_csv(birthday_data_file, index = False)  
    print(f"Your result data is \n\n{data_frame}\n")
      
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
related_birthday_dataframe = date_analyse_machine.get_user_today_birthday_dataframe(data_frame = data_frame, now = now)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not related_birthday_dataframe.empty:
    for (index, row) in related_birthday_dataframe.iterrows():
        with open(random.choice(text_file_location_list)) as file:
            text = file.read()
            text_seperated_list = text.split("[NAME]")
            reciever_email_information[row["name"]] = {}
            reciever_email_information[row["name"]]["text"] = text_seperated_list[0] + row["name"] + text_seperated_list[1] 
            reciever_email_information[row["name"]]["email"] = row["email"]

# 4. Send the letter generated in step 3 to that person's email address.
my_email = "pan289277@gmail.com"
password = "xvnpwhutejppterx"

connection = smtplib.SMTP("smtp.gmail.com", port = 587)
connection.starttls()
connection.login(user = my_email, password = password)

for name in reciever_email_information:
    if reciever_email_information:
        connection.sendmail(from_addr = my_email, to_addrs = reciever_email_information[name]["email"], msg = f"Subject:Birthday wish!!!!\n\n{reciever_email_information[name]['text']}")