# Write a Python function named calculate_area that takes the length and width of a rectangle as parameters and returns its area.


def calculate_area():
    length = int(input("Enter the rectangles length: "))
    width = int(input("Enter the rectangles width: "))
    return length * width


area = calculate_area()
print(f"The rectangles area is {area}")
