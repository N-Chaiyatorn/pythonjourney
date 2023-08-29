
class FileService():
    def __init__(self):
        self.csv_file_name = None

    def sets_csv_file_name(self):
        self.csv_file_name = input("Type your csv file name that you have considered: ")
                
        if "csv" not in self.csv_file_name.split(".") or "." not in list(self.csv_file_name):
            raise ValueError("Invalid file name, please try again with 'file_name' + '.csv'.")

            
