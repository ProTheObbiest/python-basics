file_path = '7_data_exchange/temperatures.txt'
report_file_path = '7_data_exchange/temperature_report.txt'

coldest_temp = 999
coldest_day = ""
hottest_temp = 0
hottest_day = ""
sum = 0
count = 0
avg = 0
above_15 = 0
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        day, temp = line.split(" ")[0], int(line.split(" ")[1])
        if temp < coldest_temp:
            coldest_temp = temp
            coldest_day = day
        if temp > hottest_temp:
            hottest_temp = temp
            hottest_day = day
        sum += temp
        count += 1
        if temp > 15:
            above_15 += 1

avg = sum/count

with open(report_file_path, "w", encoding="utf-8") as file:
    file.write("Average temperature: " + str(avg) + "\n")
    file.write("Hottest day is " + str(hottest_day) + " with temperature of " + str(hottest_temp) + "\n")
    file.write("Coldest day is " + str(coldest_day) + " with temperature of " + str(coldest_temp) + "\n")
    file.write("Amount of days that exceed temperature of 15: " + str(above_15))

with open(report_file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        print(line)