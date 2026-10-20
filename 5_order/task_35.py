file_path = '5_order/results.txt'

names = []
distances = []

amount = 0
sum = 0

with open(file_path, encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        name, distance_str = line.split(';')
                    
        dist_val = float(distance_str)
                
        names.append(name)
        distances.append(dist_val)

        amount += 1
        sum += dist_val

print("Names:", names)
print('Distances:', distances)

best = 0
winner_name = ""
for i in range(0, len(distances)):
    name = names[i]
    distance = distances[i]
    if distance > best:
        best = distance
        winner_name = name

print("Winner: " + winner_name + " - " + str(best))
print("People that exceed average:")
average = sum / amount

for i in range(0, len(distances)):
    name = names[i]
    distance = distances[i]
    if distance > average:
        print(name + " - " + str(distance))