temperature = float(input("Enter the temperature in Celsius: "))

if temperature == 0:
    print("The temperature is at the freezing point.")
elif temperature >= 0 and temperature <= 15:
    print("The temperature is cold.")
elif temperature >= 15 and temperature <= 25:
    print("The temperature is warm.")
else:
    print("The temperature is hot.")