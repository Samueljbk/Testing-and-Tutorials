# Create a class called Circle with an instance variable radius. Add an __init__ method to initialize the radius.
# Add two methods: area and circumference that return the area and circumference of the circle, respectively.
# Use the constant pi from the math module.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def circumference(self):
        return 2 * math.pi * self.radius
