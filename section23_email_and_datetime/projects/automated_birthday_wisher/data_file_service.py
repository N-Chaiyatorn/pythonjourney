import pandas

class DataFileService():

    def print_invalid_input_with_y_and_n(self):
        print("Invalid input!!!. Only 'y' and 'n' are allowed.")

    def asking_is_adding_data_to_file(self):
        while True:
            is_adding_data = input("Do you want to add some data to your file? (y/n): ")
            
            if is_adding_data != 'y' and is_adding_data != 'n':
                raise ValueError("Invalid input!!!. Only 'y' and 'n' are allowed.")
             
            if is_adding_data == 'y':
                return True
            elif is_adding_data == 'n':
                return False

    def add_data_to_dataframe(self, name, email_address, years, month, day, data_frame):
        data_frame.loc[len(data_frame)] = [name, email_address, years, month, day]
        return data_frame
    
            