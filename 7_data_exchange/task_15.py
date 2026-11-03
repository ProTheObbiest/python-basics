file_path = '7_data_exchange/user.txt'

with open(file_path, "w", encoding="utf-8") as file:
    file.write(input("Enter name: ")+"\n")
    file.write(input("Enter age: ")+"\n")
    file.write(input("Enter email: "))

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())