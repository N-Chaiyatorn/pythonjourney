
import pandas

class FileManager():
    def __init__(self):
        self.csv_file_name = None

    def getting_csv_file_name(self):
        while True:
            try: 
                self.csv_file_name = input("Type your csv file name that you have considered: ")
                if "csv" not in self.csv_file_name.split(".") or "." not in list(self.csv_file_name):
                    raise ValueError()

            except:
                print("Invalid file name, please try again with 'file_name' + '.csv'.")

            else:
                break

    







