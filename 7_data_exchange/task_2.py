file_path = '7_data_exchange/greeting.txt'

i = 0
with open(file_path, encoding="utf-8") as file:
    for line in file:
        i += 1
        print(str(i) + ": " + line.strip())