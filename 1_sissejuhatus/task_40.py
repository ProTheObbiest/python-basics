number = int(input("Enter a number: "))
hundreds = number // 100
remaining = number % 100
tens = remaining // 10
units = remaining % 10
print("Hundreds: " + str(hundreds) + ", Tens: " + str(tens) + ", Units: " + str(units))