# Write a program that checks if a number is even or odd.
# If the number is even, print "The number [number] is even."
# If the number is odd, print "The number [number] is odd."
# Replace the placeholder with the actual value of the number.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")
