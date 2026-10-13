correct_pass = "python123"
entered_pass = input("Enter the password: ")

while entered_pass != correct_pass:
    print("Incorrect password. Please try again.")
    entered_pass = input("Enter the password: ")

print("Password accepted.") 