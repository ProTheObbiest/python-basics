password = input("Enter password: ")

grade = 0

if len(password) >= 8:
    grade += 1

for char in password:
    if char.isupper():
        grade += 1
        break

for char in password:
    if char.islower():
        grade += 1
        break

for char in password:
    if not char.isalnum():
        grade += 1
        break

if sum(password.count(number) for number in "0123456789") >= 1:
    grade += 1

print("Result: " + str(grade) + "/5")
if grade <= 2:
    print("Weak password")
elif grade <= 4:
    print("Average password")
else:
    print("Strong password")