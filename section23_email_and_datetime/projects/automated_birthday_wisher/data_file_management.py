import pandas

class DataFileManagement():

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


    def delete_index_column(self, birthday_data_file):
        data_frame = pandas.read_csv(birthday_data_file)
        data_frame.to_csv(birthday_data_file, index = False)

        return pandas.read_csv(birthday_data_file)

    def add_data_to_dataframe(self, name, email_address, years, month, day, data_frame):
        data_frame.loc[len(data_frame)] = [name, email_address, years, month, day]
        return data_frame

    def reset_data_frame(self):
        data_dict = {}
        data_dict['name'] = []
        data_dict["email"] = []
        data_dict["year"] = []
        data_dict["month"] = []
        data_dict["day"] = []
        
        return pandas.DataFrame(data_dict)
    
    def is_reset_data_frame(self):
        reset_data = input("Do you want to reset all data from your data file? (y/n): ")

        if reset_data != 'n' and reset_data != 'y':
            raise ValueError("Invalid input!!!. Only 'y' and 'n' are allowed.")
            
        if reset_data == 'y':
            return True
        elif reset_data == 'n':
            return False
                
    def is_more_data(self):
        is_continue = input("Do you want to adding more data to birthday.csv file? (y/n): ")

        if is_continue != 'y' and is_continue != 'n':
            raise ValueError("Invalid input!!!. Only 'y' and 'n' are allowed.")
        
        if is_continue == 'y':
            return True
        elif is_continue == 'n':
            return False