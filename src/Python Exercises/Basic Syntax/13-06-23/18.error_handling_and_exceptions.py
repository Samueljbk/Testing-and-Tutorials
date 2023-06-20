# Write a Python function that takes two lists and returns True if they have at least one common member.


def has_common_member(list1, list2):
    # Loop through each element of the first list
    for element in list1:
        # Check if the element exists in the second list
        if element in list2:
            return True

    # Return False if there is no common member
    return False
