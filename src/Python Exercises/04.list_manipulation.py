# Basic List Manipulation testing
# Takes a list of numbers, and makes a new list of only the first and last elements

a = [5, 10, 15, 20, 25]

b = a[:: len(a) - 1]

print(b)
