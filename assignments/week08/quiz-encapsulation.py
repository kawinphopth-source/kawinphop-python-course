"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return f"Rec's Area of length {self.__length} and Width {self.__width} = {self.__length * self.__width}"
    def perimeter(self):
        return f"Rec's perimeter of length {self.__length} and Width {self.__width} = {2 *(self.__length + self.__width)}"
    def isSquare(self):
        return self.__length == self.__width
myRec = Rectangle(5,5)
print(myRec.area())
print(myRec.perimeter())
print(myRec.isSquare())