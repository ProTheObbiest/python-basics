file_path = '7_data_exchange/entered_numbers.txt'

with open(file_path, "w", encoding="utf-8") as file:
    for i in range(5):
        number = input("Enter number: ")
        file.write(number+"\n")

with open(file_path, "r", encoding="utf-8") as file:
    sum = 0
    count = 0
    avg = 0
    numbers = []
    for line in file:
        line = line.strip()
        sum += float(line)
        count += 1
        numbers.append(line)

    avg = sum/count
    print("Entered numbers:", numbers)
    print("Sum:",sum)
    print("Average:",avg)