first_side = float(input("Enter the first side of the triangle: "))
second_side = float(input("Enter the second side of the triangle: "))
third_side = float(input("Enter the third side of the triangle: "))
if first_side + second_side > third_side:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")