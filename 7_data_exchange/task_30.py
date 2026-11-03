file_path = '7_data_exchange/students.txt'
report_file_path = '7_data_exchange/students_report.txt'

with open(report_file_path, "w", encoding="utf-8") as report_file:
    class_sum = 0
    class_count = 0
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            split = line.split()
            name = split[0]
            sum = 0
            count = 0
            for number in split[1:]:
                sum += int(number)
                count += 1
            avg = sum/count
            r = round(avg*100)/100
            report_file.write(name + " " + str(r) + "\n")
            class_sum += avg
            class_count += 1
    class_average = class_sum/class_count
    r = round(class_average*100)/100
    report_file.write("Class Average " + str(r))

with open(report_file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        print(line)