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

more_fruits = fruits + ("pineapple", "kiwi")

fruits[2]
count = 0

for fruit in fruits:
    if fruit == "grape":
        print(f"Index of grape is {fruits.index(fruit)}")

# Could index just the name of what's being searched for e.g. fruits.index("grape")

for fruit in fruits:
    if fruit == "banana":
        count += 1
print(count)
