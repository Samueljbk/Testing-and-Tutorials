# Write a Python function named calculate_area that takes the length and width of a rectangle as parameters and returns its area.

length = int(input("Enter the rectangles length: "))
width = int(input("Enter the rectangles width: "))


def calculate_area(length: int, width: int):
    print(f"The rectangles area is {length * width}")


area = calculate_area(length, width)
