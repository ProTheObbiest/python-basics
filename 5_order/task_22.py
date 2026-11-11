prices = [12.50, 8.90, 25.00, 4.75, 19.99]

for i in range(len(prices)):
    new_price = prices[i] * 1.1
    prices[i] = f"{new_price:.2f}"

print(prices)
