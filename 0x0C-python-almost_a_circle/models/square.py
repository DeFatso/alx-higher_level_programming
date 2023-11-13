#!/usr/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle.

    Attributes:
        size (int): Size of the square.
        x (int): x-coordinate of the square.
        y (int): y-coordinate of the square.
        id (int): Identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): Size of the square.
            x (int): x-coordinate of the square.
            y (int): y-coordinate of the square.
            id (int, optional): Identifier of the square.
        """
        # Call the super class (Rectangle) constructor
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: Gets or sets the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): New size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        # Validate and set both width and height to the same value (size)
        self.validate_integer(value, "width")
        self.validate_positive(value, "width")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.

        Returns:
            dict: Dictionary containing id, size, x, and y.
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: String representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
