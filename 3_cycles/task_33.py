from random import randint

number = randint(1, 100)
user_num = int(input("Guess a number between 1 and 100: "))

while user_num != number:
    if number > user_num:
        print("The number is higher.")
    else:
        print("The number is lower.")
        
    user_num = int(input("Try again: "))

print("Congratulations!")