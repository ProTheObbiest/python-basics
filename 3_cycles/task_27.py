from random import randint

i = 0
while i < 10:
    print(str(i) + ". dice: " + str(randint(1, 6)))
    i += 1