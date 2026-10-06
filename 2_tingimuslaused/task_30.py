age_ = int(input("Enter your age: "))
student = input("Are you a student? (yes/no): ")

if age_ <= 7:
    print("Ticket price is free.")
elif age_ >= 7 and age_ <= 17:
    print("Ticket price is 5 euro.")
elif student.lower() == "yes" and age_ >= 18:
    print("Ticket price is 8 euro.")
elif age_ >= 65:
    print("Ticket price is 6 euro.")
else:
    print("Ticket price is 12 euro.")