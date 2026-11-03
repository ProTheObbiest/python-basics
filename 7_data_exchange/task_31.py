file_path = '7_data_exchange/contacts.txt'

while True:
    name = input("Enter name: ")
    if name.lower() == "stop":
        break
    else:
        found = False
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                split = line.split(";")
                name_ = split[0]
                if name.lower() == name_.lower():
                    print(name_ + "'s email and phone are: " + split[1] + " & " + split[2])
                    found = True
                    break
        if not found:
            print('User "' + name + '"has not been found')