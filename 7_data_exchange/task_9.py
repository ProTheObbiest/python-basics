file_path = '7_data_exchange/numbers.txt'

highest = 0
lowest = 999

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        number = int(line.strip())
        if number > highest:
            highest = number
        elif number < lowest:
            lowest = number

difference = highest-lowest
print("Highest number:",highest)
print("Lowest number:",lowest)
print("Difference:",difference)