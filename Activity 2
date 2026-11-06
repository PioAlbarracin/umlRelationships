class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f'{self._width:.1f}cm'

    @property
    def height(self):
        return f'{self._height}cm'

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('Invalid!')

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print('Invalid')

rectangle = Rectangle(5, 8)
rectangle.width = 6
rectangle.height = 3

print(rectangle.width)
print(rectangle.height)
