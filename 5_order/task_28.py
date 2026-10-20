file_path = '5_order/numbers.txt'

sum = 0
amount = 0
with open(file_path, encoding="utf-8") as file:
    for line in file:
        print(line.strip())
        amount += 1
        sum += int(line.strip())

print('Number amount: ' + str(amount))
print("Number sum: " + str(sum))