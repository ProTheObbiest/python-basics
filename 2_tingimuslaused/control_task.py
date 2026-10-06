name = input("Enter your name: ")
points = int(input("Enter your points: "))
misses = int(input("Enter your misses: "))
submitted = input("Did you submit the assignment? (yes/no): ")

complete = True
grade = 0

if points >= 90 and points <= 100:
    grade = 5
elif points >= 75 and points < 89:
    grade = 4
elif points >= 50 and points < 74:
    grade = 3
elif points >= 20 and points < 49:
    grade = 2
elif points >= 0 and points < 19:
    grade = 1

print('Student:', name)
print('Grade:', grade)

if submitted.lower() != 'yes':
    complete = False
    print('You did not submit the assignment.')
else:
    print('You submitted the assignment.')

if misses > 10:
    complete = False
    print('You have too many misses.')
else:
    print('You have a valid number of misses.')

if grade < 3:
    complete = False

if complete:
    print('You have passed the course.')
else:
    print('You have not passed the course.')