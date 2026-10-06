first_number = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
    print("Result: " + str(result))
elif operator == "-":
    result = first_number - second_number
    print("Result: " + str(result))
elif operator == "*":
    result = first_number * second_number
    print("Result: " + str(result))
else:
    if second_number != 0:
        result = first_number / second_number
        print("Result: " + str(result))
    else:
        print("Error: Division by zero is not allowed.")