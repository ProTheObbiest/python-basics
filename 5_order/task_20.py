numbers = [-12, 5, 0, 18, -7, 23, -3, 9]

positive = 0
negative = 0
zeros = 0
positive_sum = 0

negative_numbers = []

for number in numbers:
    if number > 0:
        positive += 1
        positive_sum += number
    elif number < 0:
        negative += 1
        negative_numbers.append(number)
    elif number == 0:
        zeros += 1

print("Positive numbers: " + str(positive))
print("Negative numbers: " + str(negative))
print("Zeros: " + str(zeros))
print("Positive number sum: " + str(positive_sum))
print("Negative number list: ", negative_numbers)