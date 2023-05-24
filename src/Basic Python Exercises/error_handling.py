# Write a Python program that asks the user for a number, and prints that number.
# If the user enters something that's not a number,
# the program should print a message and ask for the input again.
# Keep asking until the user inputs a number.

user_input = input("Enter a number: ")

if user_input.isdigit():
    print(user_input)
else:
    print("That's not a number - please enter an integer number")
