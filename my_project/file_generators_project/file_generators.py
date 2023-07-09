# file_generator_class
import pandas
import json
import os

class FileGenerators():
    def __init__(self):
        self.initial_dict = {}
        self.file_type = ''
        self.file_location = ''
        self.data_type = ''

    def print_updated_dict(self):
        print(f"Your current dict is \n {self.initial_dict}")

    
    def ask_users_for_file(self):
        while True:
            try:    
                self.file_type = input("What's file do you want to create? Please type (py/csv/txt/json): ")
                os.system('cls')

                if self.file_type != 'py' and self.file_type != 'txt' and self.file_type != 'json' and self.file_type != 'csv':
                    raise ValueError("Your file type is not allowed.")
            except ValueError:
                print("Your file type is incorrect or maybe this program couldn't support this file type.\nPlease type again.")
            else:
                break
    
    def creating_data_frame(self):
        rows = 1
        while True:
            key = input(f"Type your {rows} names : ")
            self.initial_dict[key] = []  
            self.print_updated_dict()
            value_in_list = self.ask_about_data_in_values(values = "list")
            if value_in_list == 'y':
                while True:
                    self.initial_dict[key].append(input("Type your new component in list: "))
                    self.print_updated_dict()
                    is_continous = self.ask_about_data_in_values(values = "list")
                    if is_continous == 'n':
                        break

            while True:
                try:
                    is_more_rows = input("Is there any rows? (y/n): ")
                    os.system('cls')
            
                    if is_more_rows != 'y' and is_more_rows != 'n':
                        raise ValueError("Only 'y' and 'n' are allowed.")
                except ValueError:
                    print("Type again!! only 'y' and 'n' are allowed.")
                else:
                    break
            
            rows += 1 
            if is_more_rows == 'n':
                break
            
        data_frame = pandas.DataFrame(self.initial_dict)
        print(f"Your data frame is \n{data_frame}")
        return data_frame
    
    def ask_about_data_in_values(self, values):
        while True:
            try:
                data_in_value = input(f"Do you want to add some data into your {values} (y/n): ")
                os.system('cls')
                if data_in_value != 'y' and data_in_value != 'n':
                    raise ValueError("Your value type is not allowed.")
            except ValueError:
                print("Please try again!!, It seems your submit is incorrect.")
            else:
                return data_in_value
        
    def ask_about_data_type(self, storaged_type):
        while True:
            try:
                data_type = input(f"What's your data type in your new {storaged_type} component? (dict/list/gen): ")
                os.system('cls')
                if data_type != 'dict' and data_type != 'list' and data_type != 'gen':
                    raise ValueError("Your value type is not allowed.")
            except ValueError:
                print("Please try again!!, It seems your submit is incorrect.")
            else:
                return data_type

            
    def creating_dict(self):
        while True:
            key =  input("Type your keys names : ")
            values_type = self.ask_about_data_type(storaged_type = "values")

            if values_type == 'gen':
                value = input("Type your values: ")
                self.initial_dict[key] = value
            elif values_type == 'list':
                self.initial_dict[key] = []
                self.print_updated_dict()
                data_in_list = self.ask_about_data_in_values(values = values_type)
                if data_in_list == 'y':
                    while True:
                        data_in_list_type = self.ask_about_data_type(storaged_type = "list")
                        if data_in_list_type == 'gen':
                            self.initial_dict[key].append(input("Type your new component in list: "))
                        elif data_in_list_type == 'list':
                            self.initial_dict[key].append([])
                        elif data_in_list_type == 'dict':
                            self.initial_dict[key].append({})

                        self.print_updated_dict()
                        is_continous = self.ask_about_data_in_values(values = values_type)
                        if is_continous == 'n':
                            break
                        

            elif values_type == 'dict':
                self.initial_dict[key] = {}
                self.print_updated_dict()
                data_in_dict = self.ask_about_data_in_values(values = values_type)
                if data_in_dict == 'y':
                    while True:
                        data_type_in_dict_value = self.ask_about_data_type(storaged_type = "dictionary value")
                        new_key = input("Type your new keys name: ")
                        if data_type_in_dict_value == 'gen':
                            self.initial_dict[key][new_key] = input("Type your new component in dict: ")
                        elif data_type_in_dict_value == 'list':
                            self.initial_dict[key][new_key] = []
                        elif data_type_in_dict_value == 'dict':
                            self.initial_dict[key][new_key] = {}

                        self.print_updated_dict()
                        is_continous = self.ask_about_data_in_values(values = values_type)
                        if is_continous == 'n':
                            break

            self.print_updated_dict()

            while True:    
                try:
                    is_more_rows = input("Is there any items? (y/n): ")
                    os.system('cls')
            
                    if is_more_rows != 'y' and is_more_rows != 'n':
                        raise ValueError("Only 'y' and 'n' are allowed.")
                except ValueError:
                    print("Type again!! only 'y' and 'n' are allowed.")
                else:
                    break
            
            if is_more_rows == 'n':
                return self.initial_dict
                
    def creating_file(self):
        self.file_location = input("Type file's location (So your file's names not require any last name): ")
        os.system('cls')
        while True:
            try:
                ask_file_type_text = """Do you want to storaged any data in your's file?
1.In python and json file this progrogram will only storaged dictionary.
2.In csv file this progrogram will only storaged dataframe.
3.In txt file this progrogram will storage every data type as string and printing them in this file.
Please type (y/n): """

                data_in_file = input(ask_file_type_text)
                os.system('cls')

                if data_in_file != 'y' and data_in_file != 'n':
                    raise ValueError("Only allowed 'y' and 'n'.") 
            except ValueError:
                print("Please try again!!, It seems your submit is incorrect.")
            else:
                break
        
        if self.file_type == 'py':
            with open(f"{self.file_location}.py", "w") as file:
                if data_in_file == 'y':
                    data = self.creating_dict()
                    file.write(str(data))
                
        elif self.file_type == 'csv':
            if data_in_file == 'y':
                data = self.creating_data_frame()
                data.to_csv(f"{self.file_location}.csv")
            
        elif self.file_type == 'json':
            with open(f"{self.file_location}.json", "w") as file:
                if data_in_file == 'y':
                    data = self.creating_dict()
                    json.dump(data, file, indent = len(data))
                
        elif self.file_type == 'txt':
            with open(f"{self.file_location}.txt", "w") as file:
                if data_in_file == 'y':
                    while True:
                        try:
                            self.data_type = input("What's data type do you want to stored in this file (\n(dataframe/dictionary/generally data such as int,float etc.)\nPlease choose (dataframe/dict/gen)):")
                            os.system('cls')
                            if self.data_type != 'dataframe' and self.data_type != 'dict' and self.data_type != 'gen':
                                ValueError("Your input is invalid. Only (dataframe/dict/gen) are allowed.")
                        except ValueError:
                            print("Type again!!!.")
                        else:
                            break

                    if self.data_type == 'dataframe':
                        data = self.creating_data_frame()
                    elif self.data_type == 'dictionary':
                        data = self.creating_dict()
                    elif self.data_type == 'gen':
                        data = input("Type your text: ")
                    
                    file.write(str(data))
