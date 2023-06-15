# Given a string s, create a new string that contains only the first half of s.
# If the length of s is odd, include the middle character in the new string.
# Print the new string.

s = input("Enter a string: ")

middle = len(s) // 2

if middle % 2 == 0:
    print(s[:middle])
else:
    print(s[: middle + 1])
