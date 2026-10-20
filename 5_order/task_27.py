file_path = '5_order/cities.txt'

with open(file_path, encoding="utf-8") as file:
    for line in file:
        print(line.strip())