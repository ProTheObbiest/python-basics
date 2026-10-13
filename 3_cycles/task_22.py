people = 50000
years = 0

while people <= 60000:
    people *= 1.02
    years += 1

print("It will take " + str(years) + " years for the population to reach " + str(round(people)) + " people.")