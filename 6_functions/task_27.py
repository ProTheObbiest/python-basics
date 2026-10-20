def table_of_multiplying(number):
    for i in range(1, 11):
        print(str(number) + " x " + str(i) + " = " + str(number*i))

num = float(input("Enter number: "))
table_of_multiplying(num)