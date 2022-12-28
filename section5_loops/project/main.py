#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:03032 'Program Files (x86)'/

#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# overall_letters = random.sample(letters, nr_letters)
# overall_symbols = random.sample(symbols, nr_symbols)
# overall_numbers = random.sample(numbers, nr_numbers)

# overall_symbols.extend(overall_numbers)
# overall_letters.extend(overall_symbols)

# overall_characteristic = overall_letters
# your_password = ""

# for characteristic_sequence in overall_characteristic:
#     your_password += characteristic_sequence

# print(your_password)

    
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
 
overall_letters = random.sample(letters, nr_letters)
overall_symbols = random.sample(symbols, nr_symbols)
overall_numbers = random.sample(numbers, nr_numbers)

overall_symbols.extend(overall_numbers)
overall_letters.extend(overall_symbols)

random.shuffle(overall_letters)

overall_characteristic = ""

for pass_sequence in range(len(overall_letters)):
    overall_characteristic += overall_letters[pass_sequence]

print(overall_characteristic)





 