from random import randint

i = 0
sum = 0
while i < 10:
    num = randint(1, 6)
    print(str(i) + ". dice: " + str(num))
    sum += num
    i += 1

average = sum / 10

print("The sum of the dice rolls is: " + str(sum))
print("The average of the dice rolls is: " + str(average))