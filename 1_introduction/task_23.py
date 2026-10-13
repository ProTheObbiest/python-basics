minutes = int(input("Enter minutes: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print("Hours: " + str(hours) + ", Minutes: " + str(remaining_minutes))