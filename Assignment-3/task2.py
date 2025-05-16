import math

num = float(input("Enter a number: "))

# Calculate square root, natural logarithm, and sine
square_root = math.sqrt(num)
natural_log = math.log(num) if num > 0 else "Undefined (log of non-positive number)"
sine_value = math.sin(num)

# Display the calculated results
print(f"\nResults for the number {num}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm (log base e): {natural_log}")
print(f"Sine (in radians): {sine_value}")