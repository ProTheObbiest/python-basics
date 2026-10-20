def biggest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

a = input("Input first number: ")
b = input("Input second number: ")
c = input("Input third number: ")
print("Number " + str(biggest(a,b,c)) + " is largest")