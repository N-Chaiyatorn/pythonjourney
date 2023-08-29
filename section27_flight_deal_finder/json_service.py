
import json 

class JsonService():
    def __init__(self):
        self.data = {}
        self.file_path = None

    def set_file_path(self, file_path):
        self.file_path = file_path


    def dump_json_file(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent = len(data))