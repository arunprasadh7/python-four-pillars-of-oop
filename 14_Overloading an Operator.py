#Overloading an operator
#program that returns the sum of sides of 2 squares
class Square:
    def __init__(self,side):
        self.side = side

    def __add__(s1, s2):
        return ((4 * s1.side) + (4 * s2.side))

s1 = Square(5)  #
s2 = Square(10)
print('Sum of sides of both the squares : ',s1 + s2)