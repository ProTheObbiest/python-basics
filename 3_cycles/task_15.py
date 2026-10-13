i = 1
valid_numbers = 0

while i <= 100:
    if i % 7 == 0:
        valid_numbers += 1
    i += 1

print("The number of numbers divisible by 7 from 1 to 100 is: " + str(valid_numbers))