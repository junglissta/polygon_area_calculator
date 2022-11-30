class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if self.width > 50 or self.height > 50:
          return 'Too big for picture.'
        else:
          w = self.width
          return (w * '*' + '\n')* self.height
    def get_amount_inside(self, shape):
        if self.get_area() > shape.get_area():
            fit = self.get_area() // shape.get_area()
            return fit
        else:
            return 0
        
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    def set_side(self, side):
        self.width = side
        self.height = side
    def __repr__(self):
        return f'Square(side={self.width})'
    