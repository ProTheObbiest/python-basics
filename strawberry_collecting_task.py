def money_in_euro(buckets, strawberry_price):
    strawberry_price /= 100
    return buckets * 5 * strawberry_price

file = input("Enter the filename with strawberry data (strawberry_buckets.txt): ")
rate = float(input("Enter the price of strawberries in cents: "))

total = 0
with open(file, "r", encoding="utf-8") as f:
    for day, line in enumerate(f):
        line = line.strip()
        amount_of_buckets = int(line)
        amount_of_money = money_in_euro(amount_of_buckets, rate)
        total += amount_of_money
        print(f"{day + 1}. Day earned {amount_of_money} euros.")

print(f"Total earnings: {total} euros.")