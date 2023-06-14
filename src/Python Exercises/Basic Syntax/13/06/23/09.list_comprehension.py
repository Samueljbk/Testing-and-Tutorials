# Write a Python program to find the numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included), using list comprehension.

a = [number for number in range(1500, 2701) if number % 7 == 0 and number % 5 == 0]

print(a)
