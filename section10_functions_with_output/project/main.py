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
  n1 = n1 * n2
  return n1

def divide(n1, n2):
  #TODO
  n1 = n1 / n2
  return n1

#TODO map the user operand input to the functions above
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def operating_print(n1, operator, n2, n3):
  '''
  Explaining about calculating
  '''
  print(f"{n1} {operator} {n2} = {n3}")

is_continous = True
number1 = int(input("What's the first number?: "))      # Ask user to type first number 
for symbol in operations:
  print(symbol)
while is_continous:
  operator = input("Pick an operation: ")               
  number2 = int(input("What's the next number?: "))
  while True:
    if operator == "+":
      number3 = operations[operator](n1 = number1, n2 = number2)          # Put number1 and number2 variable to function called 'add()' and return the result of calculation as an output        
      break
    elif operator == "-":
      number3 = operations[operator](n1 = number1, n2 = number2)       # Put number1 and number2 variable to function called 'subtract()' and return the result of calculation as an output
      break
    elif operator == "*":
      number3 = operations[operator](n1 = number1, n2 = number2)       # Put number1 and number2 variable to function called 'multiply()' and return the result of calculation as an output
      break
    elif operator == "/":
      number3 = operations[operator](n1 = number1, n2 = number2)          # Put number1 and number2 variable to function called 'divide()' and return the result of calculation as an output
      break
    else:
      operator = input("Error!! Its seems you type incorrect operator so please try again: ")
      
  operating_print(number1, operator, number2, number3)
  ask_user = input(f"Type 'y' to continous calculating with {number3}, or type 'n' to exit.: ")

  if ask_user == 'y':
    number1 = number3
    is_continous = True

  elif ask_user == 'n':
    is_continous = False
  



