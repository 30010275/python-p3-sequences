def print_fibonacci(n):
    """
    Prints a list containing the Fibonacci sequence up to length n.
    """
    if n <= 0:
        print([])
        return
    
    fibonacci = [0, 1]
    for _ in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci[:n])  # Ensure output length matches n

# Example usage
print_fibonacci(9)
