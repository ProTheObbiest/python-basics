i = 1
sum = 0

while i <= 5:
    num = float(input("Enter an " + str(i) + ". number: "))
    sum = sum + num
    i = i + 1

print("The sum of the numbers is: " + str(sum))