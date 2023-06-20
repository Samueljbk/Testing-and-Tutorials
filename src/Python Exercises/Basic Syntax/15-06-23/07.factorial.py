# Write a function called factorial
# that takes a single argument n and returns the factorial of that number,
# i.e., n! = n * (n-1) * (n-2) * ... * 1. You can use recursion or iteration.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(1))
