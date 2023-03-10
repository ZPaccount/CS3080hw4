'''
Homework 4-1
Name: Zachary Pace
Date: 3/9/2023
Description: Making classes for rectangle, square, and circle
'''

import math


# Parent class for other shapes
class Shape:
    def __init__(self):
        self.area = 0
        self.diagonal = 0
        self.perimeter = 0

    def getArea(self):
        return self.area

    def getDiagonal(self):
        return self.diagonal

    def getPerimeter(self):
        return self.perimeter


# Child classes of Shape class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.area = length * width
        self.diagonal = math.sqrt(length**2 + width**2)
        self.perimeter = (length + width) * 2


class Square(Shape):
    def __init__(self, side):
        self.area = side**2
        self.diagonal = math.sqrt(2 * side**2)
        self.perimeter = side * 4


class Circle(Shape):
    def __init__(self, radius):
        self.area = 3.14 * radius**2
        self.diagonal = radius * 2
        self.perimeter = 2 * 3.14 * radius


# Create Rectangle Shape
firstShape = Rectangle(20, 10)
# Test getRectangle and getDiagonal
print("Area of the Rectangle: " + str(firstShape.getArea()))
print("Diagonal of the Rectangle: " + str(firstShape.getDiagonal()))
# Create Circle Shape
secondShape = Circle(firstShape.getDiagonal())
# Test getPerimeter
print("Perimeter of the Circle: " + str(secondShape.getPerimeter()))
