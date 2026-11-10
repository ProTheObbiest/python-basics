import os

results_path = '7_data_exchange/results.txt'
reports_path = '7_data_exchange/reports.txt'

def calculate_grade(average):
    if average >= 90:
        return 5
    elif average >= 75:
        return 4
    elif average >= 60:
        return 3
    elif average >= 50:
        return 2
    else:
        return 1

def process_student_grades():
    input_filename = results_path
    output_filename = reports_path

    if not os.path.exists(input_filename):
        print(f"Error: The input file '{input_filename}' was not found.")
        return

    students_data = []

    with open(input_filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(";")
            name = parts[0]            
            grades = [int(score) for score in parts[1:]]

            avg_score = sum(grades) / len(grades)
            grade = calculate_grade(avg_score)

            students_data.append({
                "name": name,
                "average": avg_score,
                "grade": grade
            })

    if not students_data:
        print("Error: The file is empty or contains invalid data.")
        return

    class_average = sum(student["average"] for student in students_data) / len(students_data)
    
    best_student = max(students_data, key=lambda s: s["average"])
    worst_student = min(students_data, key=lambda s: s["average"])    
    passed_count = sum(1 for student in students_data if student["grade"] >= 3)

    report_lines = []
    report_lines.append("STUDENT RESULTS REPORT")
    report_lines.append("-" * 40)

    for student in students_data:
        report_lines.append(
            f"{student['name']:<10} Average: {student['average']:<6.2f} Grade: {student['grade']}"
        )

    report_lines.append("-" * 40)
    report_lines.append(f"Class average: {class_average:.2f}")
    report_lines.append(f"Best student: {best_student['name']}")
    report_lines.append(f"Lowest performing student: {worst_student['name']}")
    report_lines.append(f"Students with passing grade: {passed_count}")

    report_text = "\n".join(report_lines)

    print(report_text)

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(report_text + "\n")

    print(f"\nReport successfully saved to '{output_filename}'.")

if __name__ == "__main__":
    process_student_grades()