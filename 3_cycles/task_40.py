total_price = 0
total_items = 0
last_item = -1

while last_item != 0:
    last_item = float(input("Enter the price of the item (or 0 to finish): "))
    if last_item != 0:
        total_price += last_item
        total_items += 1

print("Total items: " + str(total_items))
print("Total price: " + str(total_price) + " euros")
