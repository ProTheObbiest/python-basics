file_path = '5_order/cities.txt'

count = 0

with open(file_path, encoding="utf-8") as file:
    for line in file:
        print(line.strip())
        count += 1
        
print(f"Total cities: {count}")