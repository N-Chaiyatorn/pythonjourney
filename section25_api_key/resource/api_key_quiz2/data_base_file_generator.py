class DataBaseFileGenerators():
    def gets_to_be_saved_csv_file(self):
        while True:
            try:
                data_file_name = input("Please type your csv file name that you want to save data (Only csv file are allowed): ")

                if 'csv' not in data_file_name.split("."):
                    raise ValueError()
            
            except:
                print("It seems your commit is incorrect, please try again.")

            else:
                return data_file_name 

    