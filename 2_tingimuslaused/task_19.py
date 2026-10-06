first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

if first_number > second_number and first_number > third_number:
    print("Largest number is " + str(first_number))
elif second_number > first_number and second_number > third_number:
    print("Largest number is " + str(second_number))
else:
    print("Largest number is " + str(third_number))