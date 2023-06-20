# Write a function called is_prime that checks if a given number is prime.
# If the number is prime, the function should return True, otherwise, it should return False.
# Test the function with different inputs.


def is_prime(number):
    if number <= 1:
        return False
    elif number > 1:
        # check for factors
        for i in range(2, number):
            if (number % i) == 0:
                # if factor is found, set flag to True
                return True
                # break out of loop
                break


print(is_prime(10))
