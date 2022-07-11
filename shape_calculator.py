class Rectangle:
    # Main function
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    # Set width
    def set_width(self, w):
        self.width = w

    # Set height
    def set_height(self, h):
        self.height = h

    # Get the area 
    def get_area(self):
        return self.width * self.height

    # Get the perimeter 
    def get_perimeter(self):
        cal_1 = self.width + self.height
        return cal_1 * 2

    # Get diagonal
    def get_diagonal(self):
        cal_2 = self.width ** 2 + self.height ** 2
        return cal_2 ** 0.5

    # Get picture
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        picture = '*' * self.width + '\n'
        picture = picture * self.height
        return picture

    # Get amount
    def get_amount_inside(self, ob):
        return self.get_area() // ob.get_area()

class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    # Return the final result
    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, s):
        self.width = s
        self.height = s