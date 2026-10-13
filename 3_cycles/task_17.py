correct_pass = "python123"
attempts = 3
entered_pass = input("Enter the password: ")

while entered_pass != correct_pass and attempts > 0:
    print("Incorrect password. Please try again.")
    attempts -= 1
    if attempts > 0:
        entered_pass = input("Enter the password: ")
    else:
        print("Access denied.")
        break

if entered_pass == correct_pass:
    print("Password accepted.") 
