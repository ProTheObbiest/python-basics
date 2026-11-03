file_path = '7_data_exchange/numbers.txt'

even = 0
odd = 0
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

print("Even numbers:",even)
print("Odd numbers:",odd)