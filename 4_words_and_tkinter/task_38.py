password = input("Enter password: ")

grade = 0
missing = []

if len(password) >= 8:
    grade += 1
else:
    missing.append("Password must be at least 8 characters long")

has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break

if has_upper:
    grade += 1
else:
    missing.append("Password must contain at least one uppercase letter")

has_lower = False
for char in password:
    if char.islower():
        has_lower = True
        break

if has_lower:
    grade += 1
else:
    missing.append("Password must contain at least one lowercase letter")

has_special = False
for char in password:
    if not char.isalnum():
        has_special = True
        break

if has_special:
    grade += 1
else:
    missing.append("Password must contain at least one special symbol")

has_digit = any(char.isdigit() for char in password)
if has_digit:
    grade += 1
else:
    missing.append("Password must contain at least one digit")

print("Result: " + str(grade) + "/5")
if grade <= 2:
    print("Weak password")
elif grade <= 4:
    print("Average password")
else:
    print("Strong password")
    
if missing:
    print("\nMissing requirements:")
    for req in missing:
        print("- " + req)