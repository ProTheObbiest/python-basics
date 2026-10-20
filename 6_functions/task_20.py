def num_type(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

num = float(input("Enter number: "))
print(num_type(num))