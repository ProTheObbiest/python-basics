from random import randint

number = randint(1, 10)
user_num = int(input("Guess a number between 1 and 10: "))

while user_num != number:
    user_num = int(input("Wrong guess. Try again: "))

print("Congratulations!")