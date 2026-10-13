seconds = input("Enter seconds: ")
hours = int(seconds) // 3600
remaining_seconds = int(seconds) % 3600
minutes = remaining_seconds // 60
remaining_seconds = remaining_seconds % 60
print("Hours: " + str(hours) + ", Minutes: " + str(minutes) + ", Seconds: " + str(remaining_seconds))