programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])

# add new item in dict
programming_dictionary["Loop"] = "Action of doing something over and over again"

# create empyty dict

empty_dictionary = {}

# wipe existing dict
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
programming_dictionary = {}

# edit item in dict
programming_dictionary["Bug"] = "hello"

# Loop through dict
for i in programming_dictionary:
    print(i)
    print(programming_dictionary[i])