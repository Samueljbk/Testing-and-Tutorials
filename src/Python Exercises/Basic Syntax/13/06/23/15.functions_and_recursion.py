# Write a Python program to calculate the factorial of a number (a non-negative integer).
# The function should accept the number as an argument.


def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
