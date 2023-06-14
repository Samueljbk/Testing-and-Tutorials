# Write a Python function that accepts a string
# and calculates the number of upper case letters and lower case letters.

string = input("Enter a string: ")

uppercase = 0
lowercase = 0

for char in string:
    if char.isupper() == True:
        uppercase += 1
    if char.islower() == True:
        lowercase += 1

print(
    f"There are {uppercase} uppercase characters and {lowercase} lowercase characters"
)
