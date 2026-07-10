print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()
#input
time = int(input("time in seconds: "))
#process
hour = time//3600
second_remain = time%3600
minute = second_remain//60
second_remain = minute%60
#output
print((f"{time} seconds = {hour} hour, {minute} minutes, {second_remain} seconds"))