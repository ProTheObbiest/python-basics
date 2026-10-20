result = 0
def count():
    global result
    result = 25
    print(result)

count()
print(result)

# program will give error at the print outside of count() function because result wasnt defined outside of count() function so it only exists inside it