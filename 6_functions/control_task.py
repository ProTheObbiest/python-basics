names = []
scores = []

def add_student(names, scores, name, result):
    if not name in names:
        names.append(name)
        if result < 0:
            result = 0
        elif result > 100:
            result = 100
        scores.append(result)
        print("Student " + name + " with result of " + str(result) + " points has been added")
    else:
        print("Error: This student already exists")

def count_grade(score):
    if score >= 90:
        return 5
    elif score >= 75:
        return 4
    elif score >= 50:
        return 3
    elif score >= 20:
        return 2
    else:
        return 1

def find_average(scores):
    sum = 0
    count = 0
    for score in scores:
        sum += score
        count += 1
    if len(scores) > 0:
        return sum/count
    else:
        return 'N/A'

def find_best(names, scores):
    name = ""
    best = 0
    for i in range(len(names)):
        if scores[i] > best:
            best = scores[i]
            name = names[i]

    if len(scores) > 0:
        return name + " (" + str(best) + " p)"
    else:
        return "N/A"

def find_worst(names, scores):
    name = ""
    worst = 999
    for i in range(len(names)):
        if scores[i] < worst:
            worst = scores[i]
            name = names[i]

    if len(scores) > 0:
        return name + " (" + str(worst) + " p)"
    else:
        return "N/A"

def display_students(names, scores):
    if len(scores) > 0:
        for i in range(len(scores)):
            print(names[i] + " - " + str(scores[i]) + " Points | Grade: " + str(count_grade(scores[i])) + "/5")
    else:
        print("No students were added yet")

def display_stats(names, scores):
    print("=================================\n       STATS OF CLASS\n=================================\n")
    print("Total students:", str(len(names)))
    print("Average score:",str(find_average(scores)))
    print("Best result:",str(find_best(names, scores)))
    print("Worst result:",str(find_worst(names, scores))+"\n")
    print("Grade distribution:")
    grade_amount = [0,0,0,0,0]
    for score in scores:
        grade = count_grade(score)
        grade_amount[grade-1] += 1
    for i in range(5, 0, -1):
        print("Grade " + str(i) + ": " + str(grade_amount[i-1]) + " student(s)")

def search_student(names, scores, name):
    for i in range(len(names)):
        if names[i] == name:
            print(names[i] + " - " + str(scores[i]) + " points")
            return
    print('Error: Couldnt find "' + name + '"')
    

def display_menu():
    print("=================================\nSTUDENT GRADE SYSTEM\n=================================\n")
    print("1. Add student\n2. Display all students\n3. Display class stats\n4. Search student by name\n0. Leave\n")
    choice = int(input("Choose action: "))
    stopped = False
    if choice == 1:
        name = input("Enter student's name: ")
        result = 0
        while True:
            try:
                result = int(input("Enter student's result: "))
                if 0 <= result <= 100:
                    break
                else:
                    print("Error: Score must be between 0 and 100")
            except ValueError:
                print("Error: Score must be number")
        add_student(names, scores, name, result)
    elif choice == 2:
        display_students(names, scores)
    elif choice == 3:
        display_stats(names, scores)
    elif choice == 4:
        name = input("Enter student's name: ")
        search_student(names, scores, name)
    elif choice == 0:
        stopped = True
    else:
        print("Error: Action not found")

    if not stopped:
        display_menu()

display_menu()