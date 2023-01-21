#Calculator
def add(n1, n2):
  #TODO
  n1 = n1 + n2
  return n1


def subtract(n1, n2):
  #TODO
  n1 = n1 - n2
  return n1

def multiply(n1, n2):
  #TODO
  n1 = n1*n2
  return n1

def divide(n1, n2):
  #TODO
  n1 = n1/n2
  return n1

#TODO map the user operand input to the functions above
operations = {
  "+": "todo",
  "-": "todo",
  "*": "todo",
  "/": "todo",
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
    operations[operator] = add(n1 = number1, n2 = number2)            # Put number1 and number2 variable to function called 'add()' and return the result of calculation as an output        
    operating_print()
  elif operator == "-":
    operations[operator] = subtract(n1 = number1, n2 = number2)       # Put number1 and number2 variable to function called 'subtract()' and return the result of calculation as an output
    operating_print()
  elif operator == "*":
    operations[operator] = multiply(n1 = number1, n2 = number2)       # Put number1 and number2 variable to function called 'multiply()' and return the result of calculation as an output
    operating_print()
  elif operator == "/":
    operations[operator] = divide(n1 = number1, n2 = number2)         # Put number1 and number2 variable to function called 'divide()' and return the result of calculation as an output
    operating_print()

  ask_user = input(f"Type 'y' to continous calculating with {operations[operator]}, or type 'n' to exit.: ")

  if ask_user == 'y':
    iscontinous = True
    number1 = operations[operator]

  elif ask_user == 'n':
    iscontinous = False
  



