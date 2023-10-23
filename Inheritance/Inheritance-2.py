class Shape:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateSurface(self):
        pass


class Triangle(Shape):

    def __init__(self, width, height):
        super().__init__(width=width, height=height)

    def calculateSurface(self):
        return self.height * self.width / 2


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__(width=width, height=height)

    def calculateSurface(self):
        return self.height * self.width


myTriangle = Triangle(10, 10)

print(f'The area is: {myTriangle.calculateSurface()}! ')
