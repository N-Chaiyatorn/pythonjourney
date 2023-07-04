# write a program which will randomly send 1 quote in the 1_quotes.txt file if it is on monday
import smtplib 
import datetime as dt
import random

# Define new class named QuotesDataManagers() to manage data in this program.
class QuotesDataManagers():
    def __init__(self):
        self.quotes_string_data = ''
        self.quotes_list_data = []
        self.quotes_dict_data = {}
        self.name_list = []
        self.randomaly_name = ''
        self.randomaly_quote = ''

    def update_quotes_string_data(self, quotes_string_data):
        self.quotes_string_data = quotes_string_data

    def update_quotes_list(self, quotes_list_data):
        self.quotes_list_data = quotes_list_data

    def creating_name_list(self, seperated_list):
        return [line[1] for line in seperated_list]

    def creating_quote_list(self, quotes_string_data):
        return quotes_string_data.split("\n")
    
    def creating_seperated_name_and_quotes_list(self):
        return [line.split(" - ") for line in self.quotes_list_data]
    
    def creating_dict_data(self, seperated_list):
        return {line[1]:line[0] for line in seperated_list}
    
    def choose_random_quote(self):
        self.randomaly_name = random.choice(self.name_list)
        self.randomaly_quote = self.quotes_dict_data[self.randomaly_name]

# Define quotes_data_managers object for manage the data from quote_file.
quotes_data_managers = QuotesDataManagers()
file_location = "/Gittest/python_learning_after_sec_21/pythonjourney/section23_email_and_datetime/projects/motivation_quote_email/1_quotes.txt"

# Reading quote_file and put the initial string data into new variable named 'quotes_string_data'. 
with open(file_location, "r") as quotes_file:
    quotes_data_managers.quotes_string_data = quotes_file.read()

# Divide for each line into new list named 'quotes_list_data'.
quotes_data_managers.quotes_list_data = quotes_data_managers.creating_quote_list(quotes_string_data = quotes_data_managers.quotes_string_data)

# For each element in list, this program will divide the quote and the name of people that said that quote into two element in each index of quotes_data_managers.quotes_list_data.
seperated_list = quotes_data_managers.creating_seperated_name_and_quotes_list()

# Creating new list that will only store people name of every quotes.
quotes_data_managers.name_list = quotes_data_managers.creating_name_list(seperated_list = seperated_list)

# Creating dictionary that will store data, so every key is the person that said quote and value is the string of quote.
quotes_data_managers.quotes_dict_data = quotes_data_managers.creating_dict_data(seperated_list = seperated_list)

# Define app password account from email.
my_email = "pan289277@gmail.com"
password = "xvnpwhutejppterx"

# Define object named connection that will be your smtp server.
connection = smtplib.SMTP("smtp.gmail.com", port = 587)
connection.starttls()

# Login app password to make connection access to sending email.
connection.login(user = my_email, password = password)

# Get current time and day.
currently_datatime = dt.datetime.now()
day = currently_datatime.weekday()

# If today are Mondays quote_data_managers will random quote from dictionary data and sending email, also tell the user in
# command line that if the email sending is successful or not. 
if day == 0:
    quotes_data_managers.choose_random_quote()
    connection.sendmail(from_addr = my_email, to_addrs = "jeanandaim007@gmail.com", msg = f"Subject:Monday's motivation quote.\n\n {quotes_data_managers.randomaly_quote}\n\n Said by {quotes_data_managers.randomaly_name}.")
    print("Email have been sending.")
    
else:
    print("Today is not Mondays and your's email haven't been send today.")












