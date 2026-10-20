def count(number, amount):
    for i in range(amount):
        print(number)

number = int(input("Enter number: "))
amount = int(input("Enter amount of loops: "))

count(number, amount)