#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int): The x-coordinate of the rectangle.
        - y (int): The y-coordinate of the rectangle.
        - id (int): The identifier for the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ with setter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width getter """
        self.validate_integer(value, "width")
        self.validate_positive(value, "width")
        self.__width = value

    @property
    def height(self):
         """ width getter """
        return self.__height

    @height.setter
    def height(self, value):
         """ width getter """
        self.validate_integer(value, "height")
        self.validate_positive(value, "height")
        self.__height = value

    @property
    def x(self):
         """ width getter """
        return self.__x

    @x.setter
    def x(self, value):
         """ width getter """
        self.validate_integer(value, "x")
        self.validate_non_negative(value, "x")
        self.__x = value

    @property
    def y(self):
         """ width getter """
        return self.__y

    @y.setter
    def y(self, value):
         """ width getter """
        self.validate_integer(value, "y")
        self.validate_non_negative(value, "y")
        self.__y = value

    def validate_integer(self, value, attribute_name):
        """ validates integer"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer.")

    def validate_positive(self, value, attribute_name):
        """ validates positive"""
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0.")

    def validate_non_negative(self, value, attribute_name):
        """ validates non negative"""
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0.")

    def display(self):
        """
        Displays the rectangle using the '#' character
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """
        Assigns attributes to the Rectangle.

        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        **kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "x":
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        - str: A string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
