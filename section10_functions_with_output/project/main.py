#Calculator
def add():
  #TODO
  number3 = number1 + number2
  operations[operator] = number3
  operating_print()
  return number3


def subtract():
  #TODO
  number3 = number1 - number2
  operations[operator] = number3
  operating_print()
  return number3

def multiply():
  #TODO
  number3 = number1 * number2
  operations[operator] = number3
  operating_print()
  return number3

def divide():
  #TODO
  number3 = number1 / number2
  operations[operator] = number3
  operating_print()
  return number3

#TODO map the user operand input to the functions above
operations = {
  "+": "TODO",
  "-": "TODO",
  "*": "TODO",
  "/": "TODO",
}

def operating_print():
  '''
  Explaining about calculating
  '''
  print(f"{number1} {operator} {number2} = {operations[operator]}")

iscontinous = True
number1 = int(input("What's the first number?: "))      # Ask user to type first number 
for symbol in operations:
  print(symbol)
while iscontinous:
  operator = input("Pick an operation: ")               
  number2 = int(input("What's the next number?: "))
  if operator == "+":
    number1 = add()            # Put number1 and number2 variable to function called 'add()' and return the result of calculation as an output        
  elif operator == "-":
    number1 = subtract()     # Put number1 and number2 variable to function called 'subtract()' and return the result of calculation as an output
  elif operator == "*":
    number1 = multiply()     # Put number1 and number2 variable to function called 'multiply()' and return the result of calculation as an output
  elif operator == "/":
    number1 = divide()         # Put number1 and number2 variable to function called 'divide()' and return the result of calculation as an output

  ask_user = input(f"Type 'y' to continous calculating with {number1}, or type 'n' to exit.: ")

  if ask_user == 'y':
    iscontinous = True

  elif ask_user == 'n':
    iscontinous = False
  



