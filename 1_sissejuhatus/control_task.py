name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
length = float(input("Enter your length of the route to school in kilometers: "))
time = float(input("Enter the time it takes to get to school in minutes: "))

print("Hello, " + name + "!")
age += 1
print("Next year you will be " + str(age) + " years old.")
length *= 1000
print("The length of the route to school in meters is: " + str(length) + " meters")
hours = int(time // 60)
minutes = int(time % 60)
print("The time it takes to get to school is: " + str(hours) + " hours and " + str(minutes) + " minutes.")
unrounded_hours = time / 60
speed = length / unrounded_hours
print("Your speed to school is: " + str(speed) + " kilometers per hour.")