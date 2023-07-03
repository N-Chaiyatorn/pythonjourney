import json
import pandas
import os

class DataFileGenerator():
    def __init__(self, data):
        self.dict_data = data
        self.file_type = ''

    def creating_data_file(self):
        while True:
            try:
                self.file_type = input("What's file do you want to store your data (csv/json/txt): ")
                os.system('cls')
                if self.file_type != 'csv' and self.file_type != 'json' and self.file_type != 'txt':
                    raise ValueError("Only 'csv' or 'json' or 'txt' file are allowed.")
            except ValueError:
                print("Please type again. Only 'csv' or 'json' or 'txt' file are allowed.")
            else:
                break
        if self.file_type == 'csv':
            self.generate_csv_file()
        elif self.file_type == 'json':
            self.generate_json_file()
        elif self.file_type == 'txt':
            self.generate_txt_file()

    def appending_new_data(self, user):
        self.dict_data["name"].append(user.name)
        self.dict_data["ages"].append(user.ages)
        self.dict_data["id cards"].append(user.id_cards)
        self.dict_data["height"].append(user.height)
        self.dict_data["weight"].append(user.weight)
        self.dict_data["encoded password"].append(user.encoded_password)
        self.dict_data["decoded password"].append(user.decoded_password)

    def generate_csv_file(self):
        data_frame = pandas.DataFrame(self.dict_data)
        csv_file_name = input("Please type your csv file names: ")
        os.system('cls')
        data_frame.to_csv(f"/Gittest/my_project/encrypt_project/{csv_file_name}.csv")
        print(f"Your result is:\n{data_frame}")

    def generate_json_file(self):
        json_file_name = input("Please type your json file names: ")
        os.system('cls')
        with open(f"/Gittest/my_project/encrypt_project/{json_file_name}.json", "w") as file:
            json.dump(self.dict_data, file, indent = 7)
        print(f"Your result is:\n{self.dict_data}")

    def generate_txt_file(self):
        txt_file_name = input("Please type your txt file names: ")
        os.system('cls')
        with open(f"/Gittest/my_project/encrypt_project/{txt_file_name}.txt", "w") as file:
            file.write(str(self.dict_data))
        print(f"Your result is:\n{self.dict_data}")
