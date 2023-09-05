#Implementing Abstact Base Class
from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
       print('Area of square is',self.side * self.side)

class Rectangle(Shape):
    length = 10
    width = 5
    def area(self):
        print('Area of rectangle is',self.length * self.width)

square = Square()
square.area()
rectangle = Rectangle()
rectangle.area()