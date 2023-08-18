import pandas

class DataFileService():  
    def asking_is_adding_data_to_file(self, users_input_validator):
        
        is_adding_data = input("Do you want to add some data to your file? (y/n): ")
        
        users_input_validator.validate_yes_and_no_answer(is_adding_data)
             
        if is_adding_data == 'y':
            return True
        elif is_adding_data == 'n':
            return False

    def update_data_to_csv(self, data_frame, birthday_data_file):
        data_frame.to_csv(birthday_data_file, index = False)  


            