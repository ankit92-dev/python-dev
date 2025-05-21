def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0  # Base case
    elif n == 2:
        return 1  # Base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

# Example usage
print(fibonacci(6))  #Here 6 becomes value of n
# Output: 5