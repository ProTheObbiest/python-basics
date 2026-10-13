sum = 0
numbers = 0
positive_numbers = 0
negative_numbers = 0
even_numbers = 0
odd_numbers = 0
last_number = -1

while last_number != 0:
    last_number = float(input("Enter a number (0 to stop): "))
    if last_number != 0:
        sum += last_number
        numbers += 1
        if last_number > 0:
            positive_numbers += 1
        elif last_number < 0:
            negative_numbers += 1
        if last_number % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1
average = 0
if numbers > 0:
    average = sum / numbers

print("\nRESULTS:\n")
print("Amount of numbers: " + str(numbers))
print("Sum: " + str(sum))
print("Average number: " + str(average))
print("Positive numbers: " + str(positive_numbers))
print("Negative numbers: " + str(negative_numbers))
print("Even numbers: " + str(even_numbers))
print("Odd numbers: " + str(odd_numbers))