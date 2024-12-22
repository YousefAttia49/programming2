from abc import ABC, abstractmethod
class Shape:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2


shapes = [Square(8), Circle(5)]


def Display(shapes):
    for shape in shapes:
        print(f'the area of {shape} is  {shape.area()}')
Display(shapes)
