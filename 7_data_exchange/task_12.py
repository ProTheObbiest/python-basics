file_path = '7_data_exchange/grades_2.txt'

names = []
grades = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split()
            names.append(parts[0])
            grades.append(int(parts[1]))

average_grade = sum(grades) / len(grades)

max_grade = max(grades)
min_grade = min(grades)

best_students_str = ""
for i in range(len(grades)):
    if grades[i] == max_grade:
        if best_students_str == "":
            best_students_str = names[i]
        else:
            best_students_str += ", " + names[i]

worst_students_str = ""
for i in range(len(grades)):
    if grades[i] == min_grade:
        if worst_students_str == "":
            worst_students_str = names[i]
        else:
            worst_students_str += ", " + names[i]

print(f"Class average grade: {average_grade:.2f}")
print(f"Highest grade ({max_grade}): {best_students_str}")
print(f"Lowest grade ({min_grade}): {worst_students_str}")

print("\nStudents with a grade of at least 4:")
for i in range(len(names)):
    if grades[i] >= 4:
        print(f"- {names[i]}: {grades[i]}")