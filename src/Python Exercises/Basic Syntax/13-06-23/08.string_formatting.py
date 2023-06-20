# Write a Python program to get a user's first and last name
# and print them in reverse order with a space between them.


def name_reversal():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    full_name = first_name + " " + last_name

    reversed_name = full_name[::-1]
    print(reversed_name)


name = name_reversal()
