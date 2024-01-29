#!/usr/bin/python3

class Square:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return 4 * self.width

    def __str__(self):
        return "Width: {}, Height: {}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=12)  # same value for width and height for a square
    print(s)
    print("Area of a Square = ", s.area_of_my_square())
    print("Perimeter of a Square = ", s.perimeter_of_my_square())