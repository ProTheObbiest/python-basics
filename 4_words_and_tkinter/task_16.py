username = input("Enter your username: ")

if len(username) >= 5 and len(username) <= 15:
    if not username[0].isdigit():
        valid = True
        i = 0
        while i < len(username):
            if username[i] not in "abcdefghijklmnopqrstuvwxyz0123456789":
                valid = False
                break
            i += 1
        if valid:
            print('Valid username')
        else:
            print("Username must include only latin and number symbols")
    else:
        print("Username must start with letter")
else:
    print("Username must have 5-15 characters")

