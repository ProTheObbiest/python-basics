shopping_cart = []

for i in range(5):
    item = input("Enter product: ")
    shopping_cart.append(item)

print("You have: ", shopping_cart)
print("Total of " + str(len(shopping_cart)) + " products")