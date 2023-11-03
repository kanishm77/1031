import math
a = int (input("enter a number"))
b = int (input("enter another number "))
operation = input("enter the intended operation(+,-,*,/)")

if(operation == "+"):
    def add(a, b):
       result = a + b
       return result
    sub_result = add(a,b)
    print(f"The sum is: {sub_result}")

elif(operation == "-"):
    def sub(a, b):
       result = a - b
       return result
    sub_result = sub(a,b)
    print(f"The sub is: {sub_result}")

elif(operation == "*"):
    def mul(a, b):
       result = a * b
       return result
    sub_result = mul(a,b)
    print(f"The multiplacation is: {sub_result}")

elif(operation == "/"):
    def divide(a, b):
       result = a / b
       return result
    sub_result = divide(a,b)
    print(f"The division is: {sub_result}")
