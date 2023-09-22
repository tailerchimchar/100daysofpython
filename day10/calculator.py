from art import logo
print(logo)

#calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = float(input("What's the first number?: "))

  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation from +, -, *, / : ")
    num2 = float(input("What's the next number?: "))
    function = operations[operation_symbol]
    answer = function(num1, num2)
    num1 = answer

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'n':
      should_continue = False

calculator()




