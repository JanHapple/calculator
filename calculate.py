number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))
operation = input("Enter one operation (+, -, * or /): ")

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "*":
    print(number1 * number2)
elif operation == "/":
    print(number1 / number2)
else:
    print("You didn't put in a operator!")