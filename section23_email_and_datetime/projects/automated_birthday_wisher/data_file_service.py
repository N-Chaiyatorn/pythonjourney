import pandas

class DataFileService():  
    def asking_is_adding_data_to_file(self):
        
        is_adding_data = input("Do you want to add some data to your file? (y/n): ")
            
        if is_adding_data != 'y' and is_adding_data != 'n':
            raise ValueError("Invalid input!!!. Only 'y' and 'n' are allowed.")
             
        if is_adding_data == 'y':
            return True
        elif is_adding_data == 'n':
            return False

    def update_data_to_csv(self, data_frame, birthday_data_file):
        print(data_frame)
        data_frame.to_csv(birthday_data_file, index = False)  


            