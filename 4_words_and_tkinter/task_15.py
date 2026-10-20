password = input("Enter a password: ")

if len(password) < 8:
    print("Too short")
elif len(password)  > 11:
    print("Too long")
else:
    print("Good length")