# Write a function called factorial
# that takes a single argument n and returns the factorial of that number,
# i.e., n! = n * (n-1) * (n-2) * ... * 1. You can use recursion or iteration.


def factorial(n):
    for number in range(1, n + 1):
        factorial = factorial * number
    return factorial


print(factorial(4))
