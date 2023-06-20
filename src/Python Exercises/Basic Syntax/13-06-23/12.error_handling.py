# Write a Python program that asks the user for a number, and prints that number.
# If the user enters something that's not a number,
# the program should print a message and ask for the input again.
# Keep asking until the user inputs a number.

correct = 0

while correct == 0:
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        print(f"The number you entered was: {user_input}")
        correct = 1
    else:
        print("That's not a number - please enter an integer number")
