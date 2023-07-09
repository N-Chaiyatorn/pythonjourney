import pandas
import json
import os
from file_generators import FileGenerators

print("Welcome to data structure and data frame generators programs!!")
print("With this program you can able to create some file with .py/.txt/.csv/.json file")
file_generators = FileGenerators()
file_generators.ask_users_for_file()
os.system('cls')  
file_generators.creating_file()