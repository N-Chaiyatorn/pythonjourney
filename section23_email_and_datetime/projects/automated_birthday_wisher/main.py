# 1. Update the birthdays.csv
import os
from data_frame_utils import DataFrameUtils
from email_sendor import EmailSendor
import smtplib
from date_utils import DateUtils
from data_file_service import DataFileService
from user import User
import random
from validate_email import validate_email

def validation_email(email):
    is_valid = validate_email(email = email)

    if not is_valid:
        raise ValueError("Invalid email address.")

def is_more_data_in_dataframe():
    is_continue = input("Do you want to adding more data to birthday.csv file? (y/n): ")

    if is_continue != 'y' and is_continue != 'n':
        raise ValueError("Invalid input!!!. Only 'y' and 'n' are allowed.")
        
    if is_continue == 'y':
        return True
    elif is_continue == 'n':
        return False

reciever_email_information = {}

my_email = "pan289277@gmail.com"
password = "xvnpwhutejppterx"

birthday_data_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/birthdays.csv"
letter_1_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/letter_templates/letter_1.txt"
letter_2_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/letter_templates/letter_2.txt"
letter_3_file = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/automated_birthday_wisher/letter_templates/letter_3.txt"

text_file_location_list = [letter_1_file, letter_2_file, letter_3_file]

date_ulits = DateUtils()
data_file_service = DataFileService()
data_frame_ulits = DataFrameUtils()
email_sendor = EmailSendor()

# Getting birthday data file.
data_frame = data_frame_ulits.gets_initial_data_frame(birthday_data_file = birthday_data_file)

data_frame_ulits.related_birthday_dataframe = data_frame_ulits.get_empty_data_frame()
data_frame_ulits.to_be_send_mail_users_dataframe = data_frame_ulits.get_empty_data_frame()

# Telling user about current data from this file.
print(f"Your current data is: \n\n {data_frame}\n")
is_reset_data_frame = data_frame_ulits.is_reset_data_frame()
os.system('cls')

if is_reset_data_frame:
    data_frame = data_frame_ulits.get_empty_data_frame()

is_adding_data = data_file_service.asking_is_adding_data_to_file()

if is_adding_data:
    while True:
        user = User()
        user.name = input("Type name: ")
        user.email = input(f"Type {user.name} email address (If {user.name} don't have please type 'none'): ")

        if user.email != "none":
            validation_email(email = user.email)

        user.birthdays = date_ulits.get_user_birthday(user_name = user.name)
        os.system('cls')
        
        data_frame = data_frame_ulits.add_new_row_data_to_data_frame(user = user, data_frame = data_frame)
        is_more_data = is_more_data_in_dataframe()
        
        if not is_more_data:
            break

data_file_service.update_data_to_csv(data_frame = data_frame, birthday_data_file = birthday_data_file)
print(f"Your result data is: \n\n{data_frame}\n")
      
# 2. Check if today matches a birthday in the birthdays.csv
data_frame_ulits.update_users_today_birthday_dataframe(data_frame = data_frame)
print(f"Below are the person that their's birthdays are today: \n\n{data_frame_ulits.related_birthday_dataframe}")
data_frame_ulits.set_to_be_send_email_users()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not data_frame_ulits.to_be_send_mail_users_dataframe.empty:
    for (index, row) in data_frame_ulits.to_be_send_mail_users_dataframe.iterrows():
        with open(random.choice(text_file_location_list)) as file:
            text = file.read()
            seperated_line_text_list = text.splitlines()
            
            email_sendor.reciever_data_dict[row["name"]] = {}
            email_sendor.reciever_data_dict[row["name"]]["text"] = email_sendor.determine_user_email_text(row = row, seperated_line_text_list = seperated_line_text_list)
            email_sendor.reciever_data_dict[row["name"]]["email"] = row["email"]

# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "pan289277@gmail.com"
    password = "xvnpwhutejppterx"

    connection = smtplib.SMTP("smtp.gmail.com", port = 587)
    connection.starttls()
    connection.login(user = my_email, password = password)

    email_sendor.sending_emails(sendor_email = my_email, connection = connection)
    print("Email have been send.")

elif data_frame_ulits.to_be_send_mail_users_dataframe.empty:
    print("Email haven't been send.")