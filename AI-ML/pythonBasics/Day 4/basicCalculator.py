type=str(input("Enter the operation you want to perform (add, subtract, multiply, divide): "))
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
if type == "add":
    result = num1 + num2
    print("The result is: ", result)
elif type == "subtract":
    result = num1 - num2
    print("The result is: ", result)
elif type == "multiply":
    result = num1 * num2
    print("The result is: ", result)
elif type == "divide":
    if num2 != 0:
        result = num1 / num2
        print("The result is: ", result)
    else:
        print("Error: Division by zero is not allowed.")