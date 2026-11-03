file_path = '7_data_exchange/names.txt'

i = 0
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        i += 1

print("File has " + str(i) + " names")