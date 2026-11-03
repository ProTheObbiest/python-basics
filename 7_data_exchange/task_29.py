file_path = '7_data_exchange/sell.txt'
report_file_path = '7_data_exchange/sell_report.txt'

with open(report_file_path, "w", encoding="utf-8") as report_file:
    sum = 0
    highest_value = 0
    highest_product = ""
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            split = line.split(" ")
            product, value, amount = split[0], float(split[1]), int(split[2])
            total_value = value*amount
            report_file.write(product + ": " + str(total_value) + "\n")
            sum += total_value
            if total_value > highest_value:
                highest_product = product
                highest_value = total_value
    report_file.write("Total " + str(sum) + "\n")
    report_file.write("Highest is " + highest_product + " with value of " + str(highest_value))

with open(report_file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        print(line)