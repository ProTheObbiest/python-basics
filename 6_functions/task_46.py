def sub(cur, mod):
    return cur - mod

def add(cur, mod):
    return cur + mod

def mul(cur, mod):
    return cur * mod

def div(cur, mod):
    return cur / mod

works = True
last_action = "operator"
p_num = ""
c_num = ""
operator = ""

print('Type "stop" to stop calculator')

while works:
    if last_action == "num":
        user_input = input("Choose operator (+ - * /): ").strip().lower()
        if user_input == "stop":
            break
        operator = user_input
        last_action = "operator"

    elif last_action == "operator":
        user_input = input("Enter number: ").strip().lower()
        if user_input == "stop":
            break
        p_num = c_num
        c_num = float(user_input)
        last_action = "num"

    if p_num != "" and c_num != "" and operator != "":
        success = True
        if operator == "+":
            c_num = add(p_num, c_num)
        elif operator == "-":
            c_num = sub(p_num, c_num)
        elif operator == "*":
            c_num = mul(p_num, c_num)
        elif operator == "/":
            if c_num != 0:
                c_num = div(p_num, c_num)
            else:
                print("Error: Cannot divide by zero!")
                c_num = p_num
                last_action = "operator"
                success = False
        else:
            print("Error: Unknown operator!")
            c_num = p_num
            last_action = "num"
            success = False

        if success:
            p_num = ""
            operator = ""
            print("Result:", c_num)