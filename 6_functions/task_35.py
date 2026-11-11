num = 100

def change():
    num = 20
    print("In function:", num)

change()
print("In main program:", num)

# Explanation:
# The function 'change()' creates a new LOCAL variable named 'arv' inside its scope.
# Assigning 'arv = 20' shadows but does not modify the GLOBAL variable 'arv'.
# Without using the 'global' keyword, the global variable remains equal to 100.