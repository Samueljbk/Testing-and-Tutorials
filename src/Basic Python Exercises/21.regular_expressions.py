# Write a Python program to match a string that contains only uppercase letters.


def is_all_uppercase(input_string):
    # Loop through each character in the input string
    for char in input_string:
        # Check if the character is not uppercase
        if not char.isupper():
            return False

    # Return True if all characters are uppercase
    return True


# Example usage:
input_string = "HELLO"
result = is_all_uppercase(input_string)
print("Is the input string all uppercase?", result)
