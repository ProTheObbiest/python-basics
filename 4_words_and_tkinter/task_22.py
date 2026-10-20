email = input("Enter an email: ")

if email.count("@") == 1:
    if email.find("@") > 0:
        if "." in email.split("@")[1]:
            if email.split("@")[1][0] != '.' and email.split("@")[1][-1] != '.':
                if email.count(" ") == 0:
                    print("Valid email")
                else:
                    print("Email can't contain spaces")
            else:
                print("Domain can't start or end with '.'")
        else:
            print('Domain must include separator "."')
    else:
        print("Email must include atleast one symbol before @")
else:
    print("Email must include exactly one @")