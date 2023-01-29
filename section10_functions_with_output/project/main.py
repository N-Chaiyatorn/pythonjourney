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

def is_user_finished(user_ans):
  while True:
    if user_ans  == 'y':
      return True
    elif user_ans  == 'n':
      return False
    else:
      user_ans = input(f"Error!! you type incorrect way , please type 'y' to continous or type 'n' to exit.: ")

is_not_finished = True
number1 = int(input("What's the first number?: "))      # Ask user to type first number 
for symbol in operations:
  print(symbol)
while is_not_finished:
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
  user_ans_input = input(f"Type 'y' to continous calculating with {number3}, or type 'n' to exit.: ")
  number1 = number3
  is_not_finished = is_user_finished(user_ans = user_ans_input)

  



