file_path = '5_order/temperatures.txt'

lowest = 999
highest = 0 
amount = 0
sum = 0
num_list = []
cold = 0
warm = 0

with open(file_path, encoding="utf-8") as file:
    for line in file:
        num = int(line.strip())
        amount += 1
        sum += num
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

        if num < 0:
            cold += 1
        elif num >= 5:
            warm += 1

        num_list.append(num)

average = sum / amount
print('Temperatures: ', num_list)
print('Average temperature: ' + str(average) + "°C")
print("Lowest number: " + str(lowest) + "°C")
print("Average number: " + str(average) + "°C")
print("Below zero days: " + str(cold))
print("Atleast 5 degrees days: " + str(warm))