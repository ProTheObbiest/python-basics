number = int(input("Enter number (1-10): "))

for i in range(1, 11):
    print(str(number) + ' x ' + str(i) + ' = ' + str(number * i))