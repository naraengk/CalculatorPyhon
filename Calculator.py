# Welcome, this is a Python Calculator!

#Addition
def add(n1, n2):
  return n1 + n2

#Subtraction
def sub(n1, n2):
  return n1 - n2

#Multiplication
def multi(n1, n2):
  return n1 * n2

#Division
def div(n1, n2):
  return n1 / n2

def square(n1, n2):
  return n1 ** n2

calc_dict = {
                "+": add,
                "-": sub,
                "*": multi,
                "/": div,
                "**" : square
            }

from art import logo

def calculator():
  print(logo)
  num1 = float(input("Pick your first number: "))
  for symbol in calc_dict:
    print(symbol)
  should_continue = True
 
  while should_continue:
    print("These are the available operations!")

    choice_of_operation = input("Pick an operation: ")
    num2 = float(input("Pick your next number: "))

    calculation_function = calc_dict[choice_of_operation]
    answer = calculation_function(num1, num2)

    print(f"{num1} {choice_of_operation} {num2} = {answer}")
    again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if again == 'n':
        end_calc = True
        print("\n" * 200)
        calculator()
    else:
        num1 = answer

calculator()