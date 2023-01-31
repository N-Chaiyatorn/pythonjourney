def function():
    x = 1 + 1
    return x

# a = function() = 2 

def format_name(last_name, first_name):
    formatted_last_name = last_name.title()             #====> .title() ===>ทำให้ str 
    formatted_first_name = first_name.title()
    print(f"{formatted_last_name} {formatted_first_name}")

format_name("NiaMrAt", "ChAiyaTorN")

def format_name_2(last_name, first_name):
    formatted_last_name = last_name.title()
    formatted_first_name = first_name.title()
    return f"{formatted_last_name} {formatted_first_name}"

formatted_full_name = format_name_2(input("what is your last name? "), input("what is your first name? "))
print(formatted_full_name)

