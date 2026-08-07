# Example 3: Mathematical function
def calculate_triangle_area(base, height):
    """Calculates and displays triangle area"""
    area = 0.5 * base * height
    print(f"Triangle with base {base} and height {height}")
    print(f"Area = 1/2 × {base} × {height} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)