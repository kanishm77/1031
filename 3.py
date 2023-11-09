# making a welcome message and asking the user to input some operation and desired numbers 
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_number = input("Enter in first number: ")
second_number = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# defining diffrent function according to the operation to be performed 
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot be divided by zero"
    return a / b


# converting string data type to float 
first_number = float(first_number)
second_number = float(second_number)

if operation == "add":
    result = first_number + second_number
    print(f"Result: {result}")
elif operation == "subtract":
    result = first_number - second_number
    print(f"Result: {result}")
elif operation == "multiply":
    result = first_number * second_number
    print(f"Result: {result}")
elif operation == "divide":
    result = first_number / second_number
    print(f"Result: {result}")
else:
    print("Sorry, I do not understand your request.")
