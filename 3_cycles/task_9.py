i = 1
summa = 0

while i <= 5:
    summa = summa + i
    i = i + 1

print(summa)

# Expected Output:
# 15

# Step-by-step variable changes:
# Step 1: i = 1, summa = 0 + 1 = 1  -> i becomes 2
# Step 2: i = 2, summa = 1 + 2 = 3  -> i becomes 3
# Step 3: i = 3, summa = 3 + 3 = 6  -> i becomes 4
# Step 4: i = 4, summa = 6 + 4 = 10 -> i becomes 5
# Step 5: i = 5, summa = 10 + 5 = 15 -> i becomes 6
# Loop ends because condition (i <= 5) becomes False (6 <= 5 is False).
# Final values: summa = 15, i = 6