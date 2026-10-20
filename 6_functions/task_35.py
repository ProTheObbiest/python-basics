num = 100

def change():
    global num
    num = 20
    print("In function:", num)

change()
print("In main program:", num)

# because in function to change global variable you need to define it using global {variable} before doing any changes otherwise it will only change it inside function