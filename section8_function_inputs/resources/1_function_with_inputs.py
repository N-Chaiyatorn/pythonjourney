""" function with inputs """

def greet():
    print("Hello")
    print("how are you?")

# function with inputs
def greet_with_name(name):
    print("Hello")
    print("how are you?")

# functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}, Are you from {location}")

# parameter ===> ตัวเเปร
# arguments ===> ค่าของตัวเเปร

# positional arguments
greet_with("pan","Bangkok")          # ====> Hello pan, Are you from Bangkok
greet_with("Bangkok","pan")          # ====> Hello Bangkok, Are you from pan

# keyword arguments
greet_with(location="Bangkok", name="pan")              # ====> Hello pan, Are you from Bangkok