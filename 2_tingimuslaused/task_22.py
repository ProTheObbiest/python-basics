correct_name = "admin"
correct_pass = "python123"

username = input("Enter your username: ")
if username == correct_name:
    password = input("Enter your password: ")
    if password == correct_pass:
        print("Hello, admin.")
    else:
        print("Incorrect password.")
else:
    print("Unknown username.")