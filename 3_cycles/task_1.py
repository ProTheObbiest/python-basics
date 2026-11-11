
# Solution 1

print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")

# Solution 2

i = 0

while i < 5:
    print("Hello, World!")
    i += 1

# 1. Solution without a loop requires code duplication. If we need to print the text 100 times, we would have to write 100 lines of print().
# 2. 2. Solution with a loop is much more scalable and cleaner: it uses a single print() statement, and the repetition count can be easily changed by adjusting the condition (e.g., i < 100).