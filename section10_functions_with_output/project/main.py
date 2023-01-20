#Calculator
def add(n1, n2):
  #TODO
  n3 = n1 + n2
  return n3


def subtract(n1, n2):
  #TODO
  n3 = n1 - n2
  return n3

def multiply(n1, n2):
  #TODO
  n3 = n1*n2
  return n3

def divide(n1, n2):
  #TODO
  n3 = n1/n2
  return n3

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
number1 = int(input("What's the first number?: "))
while iscontinous:
  operator = input("Pick an operation: ")
  number2 = int(input("What's the next number?: "))
  if operator == "+":
    operations[operator] = add(n1=number1, n2=number2)
    operating_print()
  elif operator == "-":
    operations[operator] = subtract(n1=number1, n2=number2)
    operating_print()
  elif operator == "*":
    operations[operator] = multiply(n1=number1, n2=number2)
    operating_print()
  elif operator == "/":
    operations[operator] = divide(n1=number1, n2=number2)
    operating_print()

  ask_user = input(f"Type 'y' to continous calculating with {operations[operator]}, or type 'n' to exit.: ")

  if ask_user == 'y':
    iscontinous = True
    number1 = operations[operator]

  elif ask_user == 'n':
    iscontinous = False
  



