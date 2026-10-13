from turtle import *

i = 0
sides = int(input("Enter the number of sides for the polygon: "))
length = int(input("Enter the length of each side: "))

while i < sides:
    forward(length)
    left(360 / sides)
    i += 1

exitonclick()