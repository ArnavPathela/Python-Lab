# Input the operation from the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print(num1, "+", num2, "=", num1 + num2)
elif operation == '2':
    print(num1, "-", num2, "=", num1 - num2)
elif operation == '3':
    print(num1, "*", num2, "=", num1 * num2)
elif operation == '4':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")
