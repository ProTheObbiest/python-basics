import statistics

grades = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]
entries = [0,0,0,0,0]

amount = 0
sum = 0
good_grades = 0
bad_grades = 0

for grade in grades:
    amount += 1
    sum += grade
    entries[grade-1] += 1
    if grade >= 3:
        good_grades += 1
    elif grade <= 2:
        bad_grades += 1

average = sum / amount
most_often = statistics.multimode(grades)
    

print('Amount of grades: ' + str(amount))
print('Average grade: ' + str(average))
print('Most often appears:', most_often)
print('Amount of positive grades: ' + str(good_grades))
print('Amount of negative grades: ' + str(bad_grades))

for grade in range(1, 6):
    count = entries[grade - 1]
    stars = '*' * count
    print(f"Grade {grade}: {stars}")