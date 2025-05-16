# Define the factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Call the function with a sample number and print the output
sample_number = int(input("enter a number:"))
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")