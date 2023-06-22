# Create a tuple named fruits containing the following items: 'apple', 'banana', 'orange', 'grape', and 'mango'.
#
# Access the third item of the fruits tuple.
#
# Find the index of 'grape' in the fruits tuple.
#
# Count how many times 'banana' appears in the fruits tuple.
#
# Create a new tuple named more_fruits by concatenating the fruits tuple with another tuple containing 'pineapple' and 'kiwi'.

fruits = ("apple", "banana", "orange", "grape", "mango")

fruits[2]

for fruit in fruits:
    if fruit == "grape":
        print(f"Index of grape is {fruits.index(fruit)}")
