prices = [12.50, 8.90, 25.00, 4.75, 19.99]

for i in range(len(prices)):
    new_price = prices[i] * 1.1
    new_price = round(new_price*100)/100
    prices[i] = new_price

print(prices)
