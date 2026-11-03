file_path = '7_data_exchange/product_list.txt'

with open(file_path, "w", encoding="utf-8") as file:
    while True:
        product = input("Enter product name: ")
        if product.lower() == "stop":
            break
        else:
            file.write(product+"\n")

with open(file_path, "r", encoding="utf-8") as file:
    print("Your products:")
    for line in file:
        print(line.strip())