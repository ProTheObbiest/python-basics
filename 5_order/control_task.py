file_path = '5_order/control_work.csv'

names = []
scores = []

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(";")
        name = data[0]
        score = int(data[1])
        names.append(name)
        scores.append(score)

print("CONTROL WORK RESULTS\n")

for i, name in enumerate(names):
    grade = 0
    if scores[i] >= 90 and scores[i] <= 100:
        grade = 5
    elif scores[i] >= 75 and scores[i] <= 89:
        grade = 4
    elif scores[i] >= 50 and scores[i] <= 74:
        grade = 3
    elif scores[i] >= 20 and scores[i] <= 49:
        grade = 2
    elif scores[i] >= 0 and scores[i] <= 19:
        grade = 1
    print(f"{name} - {scores[i]} points - grade: {grade}")

print(f"\nTotal students: {len(names)}")
print(f"Average score: {sum(scores) / len(scores):.1f}")
best_students = []
worst_students = []
for i, score in enumerate(scores):
    if score == max(scores):
        best_students.append(names[i])
    if score == min(scores):
        worst_students.append(names[i])
if len(best_students) == 1:
    best_students = best_students[0]
if len(worst_students) == 1:
    worst_students = worst_students[0]
print(f"Best result: {best_students} - {max(scores)} points")
print(f"Worst result: {worst_students} - {min(scores)} points")
passed = 0
not_passed = 0
for score in scores:
    if score >= 50:
        passed += 1
    else:
        not_passed += 1
print(f"Test passed: {passed} students")
print(f"Test failed: {not_passed} students ")

while True:
    search_name = input("\nEnter a name to search for (or 'exit' to quit): ")
    if search_name.lower() == 'exit':
        break
    found = False
    i = 0
    for name in names:
        if search_name.lower() == name.lower():
            search_name = name
            i = names.index(search_name)
            found = True
            break
    
    if found:
        print(f"Student: {search_name}")
        print(f"Score: {scores[i]}")
        grade = 0
        if scores[i] >= 90 and scores[i] <= 100:
            grade = 5
        elif scores[i] >= 75 and scores[i] <= 89:
            grade = 4
        elif scores[i] >= 50 and scores[i] <= 74:
            grade = 3
        elif scores[i] >= 20 and scores[i] <= 49:
            grade = 2
        elif scores[i] >= 0 and scores[i] <= 19:
            grade = 1
        print(f"Grade: {grade}")
    else:
        print(f"'{search_name}' not found in the list.")