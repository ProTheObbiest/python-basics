def num_sum(last):
    sum = 0
    for i in range(last+1):
        sum += i
    return sum

last = int(input("Enter number: "))
print(num_sum(last))