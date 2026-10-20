file_path = '5_order/numbers.txt'

lowest = 999
highest = 0 
amount = 0
sum = 0
num_list = []

with open(file_path, encoding="utf-8") as file:
    for line in file:
        num = int(line.strip())
        amount += 1
        sum += num
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

        num_list.append(num)

average = sum / amount
sorted_numbers = sorted(num_list)

print('Numbers: ', num_list)
print('Highest number: ' + str(highest))
print("Lowest number: " + str(lowest))
print("Average number: " + str(average))
print("Sorted numbers: ", sorted_numbers)