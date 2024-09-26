def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
number = int(input("Enter a number: "))
result = factorial_iterative(number)
print(f"The factorial of {number} is: {result}")
