grade_file_path = '7_data_exchange/grades.txt'
report_file_path = '7_data_exchange/grade_stats.txt'

def display_actions():
    print("1. Show all students\n2. Add new student and grade\n3. Search for student\n4. Show grade stats\n5. Save reports into file\n6. End\n")

def display_students():
    with open(grade_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            name = line.split()[0]
            print(name)

def add_student(name, grade):
    exists = False
    with open(grade_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            name_ = line.split()[0]
            if name.lower() == name_.lower():
                exists = True
                print("This student already exists")
                break

    if not exists:
        grade = int(grade)
        if grade > 5:
            grade = 5
        elif grade < 1:
            grade = 1
        with open(grade_file_path, "a", encoding="utf-8") as file:
            file.write("\n" + name + " " + str(grade))
            print('Student "' + name +'" with grade of ' + str(grade) + " has been added")


def search_for_student(target):
    found = False
    with open(grade_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            name = line.split()[0]
            if target.lower() == name.lower():
                found = True
                print(name + " - Grade " + str(line.split()[1]))
                break

    if not found:
        print('Student with name "' + target +'" has not been found')

def getstats():
    sum = 0
    count = 0
    appearance = [0,0,0,0,0]

    with open(grade_file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            grade = int(line.split()[1])
            appearance[grade-1] += 1
            sum += grade
            count += 1

    avg = sum/count
    return avg, appearance

while True:
    display_actions()
    action = int(input("Choose action: "))

    if action == 1:
        display_students()
    elif action == 2:
        name = input("Enter student's name: ")
        grade = input("Enter student's grade: ")

        add_student(name, grade)
    elif action == 3:
        name = input("Enter student's name: ")

        search_for_student(name)
    elif action == 4:
        avg, appearance = getstats()
        print("Average grade:", str(round(avg*100)/100))
        i = 0
        print("Grade appearance:")
        for amount in appearance:
            print("Grade " + str(i+1) + " appears " + str(amount) + " time(s)")
            i += 1
    elif action == 5:
        avg, appearance = getstats()
        with open(grade_file_path, "w", encoding="utf-8") as file:
            file.write(str(avg) + "\n")
            string = ""
            i = 1
            for amount in appearance:
                string = string + str(amount)
                if i < 5:
                    string = string + ";"
                i += 1
            file.write(string)
        print("Grade stats has been saved")
    elif action == 6:
        break