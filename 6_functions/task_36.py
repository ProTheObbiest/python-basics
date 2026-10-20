def square_sum(a, b):
    def square(num):
        return num ** 2
    square_a = square(a)
    square_b = square(b)
    return square_a + square_b

a = int(input("Input first number: "))
b = int(input("Input second number: "))

print(square_sum(a, b))