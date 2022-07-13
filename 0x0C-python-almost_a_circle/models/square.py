#!/usr/bin/python3
"""
Square class module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, width):
        """
        size setter
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = width

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
                    self.size = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
        else:
            arg_dict = {'id': 1, 'size': 2, 'x': 3, 'y': 4}
            for key, value in kwargs.items():
                if key in arg_dict:
                    i = arg_dict[key]
                    if i == 1:
                        self.id = value
                    elif i == 2:
                        self.size = value
                    elif i == 3:
                        self.x = value
                    elif i == 4:
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
            self.size = int(csv[a:b])
            a = b + 1
            b = csv.index(",", a)
            self.x = int(csv[a:b])
            a = b + 1
            self.y = int(csv[a])

    def to_dictionary(self):
        """
        converts to dictionary
        """
        sqr_dict = {'id': self.id, 'size': self.width, 'x': self.x}
        sqr_dict['y'] = self.y
        return sqr_dict

    def to_csv(self):
        """
        converts to csv
        """
        sqr_csv = str(self.id) + "," + str(self.size) + "," +\
            str(self.x) + "," + str(self.y)
        return sqr_csv
