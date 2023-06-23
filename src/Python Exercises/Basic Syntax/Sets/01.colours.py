# Create a set named colors containing the following items: 'red', 'blue', 'green', 'yellow', and 'orange'.
#
# Add the color 'purple' to the colors set.
#
# Remove the color 'yellow' from the colors set.
#
# Check if the color 'blue' is present in the colors set.
#
# Find the union of two sets: colors and another set containing 'pink', 'white', and 'black'.

colours = {"red", "blue", "green", "yellow", "orange"}

more_colours = {"pink", "white", "black"}

colours.add("purple")

colours.remove("yellow")

if "blue" in colours:
    print("True")

colours.union(more_colours)

print(colours)
