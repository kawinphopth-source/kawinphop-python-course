#question
print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()
#answer
#input
radius = float(input("Radius: "))
#process
area = 3.14159 * radius**2
circumference = 2 * 3.14159 * radius
#output
print(f"area = {area}, circumference = {circumference}")