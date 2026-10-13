balance = 1000
year = 1
while year <= 10:
    balance = balance * 1.05
    print("Year " + str(year) + ": Balance is " + str(round(balance)) + " euros")
    year += 1