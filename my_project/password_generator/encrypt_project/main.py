import pandas 
import json
from user import User
from encode_and_decode_machines import EncodeAndDecodeMachine
from data_file_generator import DataFileGenerator
import os

LOWER_CASE_ALPHABET = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

users_data = {"name":[], "ages":[], "id cards":[], "height":[], "weight":[], "encoded password":[], "decoded password":[]}
data_file_generator = DataFileGenerator(data = users_data)

while True:
    encode_and_decode_machines = EncodeAndDecodeMachine()
    user = User()
    print("Welcome to encode and decode program.")
    user.type_info()
    user.ask_user_purpose()
    shifting = int(input("How many do you want to shift?: "))
    initial_characters = list(input("Type your characters that your want to encode or decode: ").lower())
    if user.purpose == 'e':
        user.encoded_password = encode_and_decode_machines.encoding(characters = initial_characters, alphabet_list = LOWER_CASE_ALPHABET, shifting = shifting)
    elif user.purpose == 'd':
        user.decoded_password = encode_and_decode_machines.decoding(characters = initial_characters, alphabet_list = LOWER_CASE_ALPHABET, shifting = shifting)

    data_file_generator.appending_new_data(user = user)
    encode_and_decode_machines.print_the_result(user = user)

    while True:
        try: 
            is_continous = input("Do you want to encoding or decoding again? (y/n): ")
            os.system('cls')
            if is_continous != 'y' and  is_continous != 'n':
                raise ValueError("Error!!")
                
        except ValueError:
            print("Only 'y' and 'n' are allowed. Please type again.")

        else:
            break

    if is_continous == 'n':
        break
    
data_file_generator.creating_data_file()
    

    



