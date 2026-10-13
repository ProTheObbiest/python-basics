CPU_usage = float(input("Enter the CPU usage percentage: "))
Memory_usage = float(input("Enter the memory usage percentage: "))
Disk_usage = float(input("Enter the disk usage percentage: "))
if CPU_usage > 90 or Memory_usage > 90 or Disk_usage > 90:
    print("Server status:Critical")
elif CPU_usage > 75 or Memory_usage > 75 or Disk_usage > 75:
    print("Server status: Warning")
else:
    print("Server status: Normal")
