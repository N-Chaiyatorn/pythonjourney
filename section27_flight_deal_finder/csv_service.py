
import pandas

class CsvService():
    # Should determine file path as method parameters instead set to attribute.
    def __init__(self):
        self.file_path = None
        self.col_list = []

    def set_file_path(self, csv_file_path):
        self.file_path = csv_file_path

    def update_data_to_csv(self, data):
        data.to_csv(self.file_path, index = False)

    def get_csv_file_data(self):
        return pandas.read_csv(self.file_path)

        
