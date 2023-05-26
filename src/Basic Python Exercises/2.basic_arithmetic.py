# Basic input and arithmetic testing

number1 = int(input("Enter the first number "))
number2 = int(input("Enter the second number "))


arithmetic_style = input("multiplication, division, addition or subtraction?")


if arithmetic_style == "multiplication":
    print(f"Number 1 multiplied by number 2 is {number1 * number2}")

if arithmetic_style == "division":
    print(f"Number 1 divided by number 2 is {number1 / number2}")

if arithmetic_style == "addition":
    print(f"Number 1 added to Number 2 is {number1 + number2}")

if arithmetic_style == "subtraction":
    print(f"Number 1 subtracted from Number 2 is {number1 - number2}")
