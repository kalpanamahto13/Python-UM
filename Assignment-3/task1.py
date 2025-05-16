# Define the factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call


num = int(input("enter a number:"))
print(f"The factorial of {num} is: {factorial(num)}")