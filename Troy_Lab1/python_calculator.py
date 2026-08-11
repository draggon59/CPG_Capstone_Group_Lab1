#functions

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error"

# User Input
choice = input("Enter operator (+,-,*,/): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculation
if choice == '+': print(add(num1, num2))
elif choice == '-': print(subtract(num1, num2))
elif choice == '*': print(multiply(num1, num2))
elif choice == '/': print(divide(num1, num2))
else: print("Invalid")
