password = input("Enter a password: ")

if len(password) < 8:
    print("Too short")
elif len(password) > 11:
    print("Long password")
else:
    print("Good length")