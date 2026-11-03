file_path = '7_data_exchange/text.txt'

words = 0

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        words += len(line.split(" "))

print("Text has " + str(words) + " words.")