# Using list comprehension, create a new list that contains only the even numbers
# from a given list of integers. Print the new list.

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = [num for num in given_list if num % 2 == 0]

print(even_numbers)
