temperatures = [12, 18, 25, 9, 31, 22, 16, 28, 7]

warm = []
cold = []

for temp in temperatures:
    if temp >= 20:
        warm.append(temp)
    else:
        cold.append(temp)

print('Warm temperatures: ', warm)
print("Cold temperatures: ", cold)