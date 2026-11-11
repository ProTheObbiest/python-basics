def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))

print("Number " + str(biggest(a, b, c)) + " is largest")