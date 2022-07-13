#!/usr/bin/python3
"""
Recatngle class module
"""


from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle
    """

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        height setter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y getter
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        computes area
        """
        return self.width * self.height

    def display(self):
        """
        displays rectangle with '#'
        """
        for i in range(self.y):
            print("")
        for j in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        string representation
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """
        updates attributes
        """
        if len(args) != 0:
            i = 0
            for a in args:
                i += 1
                if i == 1:
                    self.id = a
                elif i == 2:
                    self.width = a
                elif i == 3:
                    self.height = a
                elif i == 4:
                    self.x = a
                elif i == 5:
                    self.y = a
        else:
            arg_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
            for key, value in kwargs.items():
                if key in arg_dict:
                    i = arg_dict[key]
                    if i == 1:
                        self.id = value
                    elif i == 2:
                        self.width = value
                    elif i == 3:
                        self.height = value
                    elif i == 4:
                        self.x = value
                    elif i == 5:
                        self.y = value

    def update_csv(self, csv):
        """
        updates attributes using csv
        """
        if len(csv) != 0:
            a = 0
            b = csv.index(",")
            self.id = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.width = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.height = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.x = int(csv[a:b])
            a = b + 1
            self.y = int(csv[a:])

    def to_dictionary(self):
        """
        converts to dictionary
        """
        rect_dict = {'id': self.id, 'width': self.width, 'height': self.height}
        rect_dict['x'] = self.x
        rect_dict['y'] = self.y
        return rect_dict

    def to_csv(self):
        """
        converts to csv
        """
        rect_csv = str(self.id) + "," + str(self.width) + "," +\
            str(self.height) + "," + str(self.x) + "," + str(self.y)
        return rect_csv
