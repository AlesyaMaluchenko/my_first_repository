import math

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"

class Shape:
    def __init__(self, type = "Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)

def dist(a, b):
    return ((b.get_y() - a.get_y()) ** 2 + (b.get_x() - a.get_x()) ** 2) ** 0.5

class Triangle(Shape):
    def __init__(self, p1, p2, p3, type = "Triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._a = dist(self._point_1, self._point_2)
        self._b = dist(self._point_2, self._point_3)
        self._c = dist(self._point_2, self._point_3)

    def __str__(self):
        return " ".join([super().__str__(), self._point_1.__str__(),
                         self._point_2.__str__(), self._point_3.__str__()])

    def area(self):
        p = 0.5*(self._a + self._b + self._c)
        return (p*(p-self._a)*(p-self._b)*(p-self._c))**0.5

    def perimeter(self):
        return self._a + self._b + self._c

class Rectangle(Shape):
    def __init__(self, p1, p2, p3, p4, type = "Rectangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3
        self._point_4 = p4
        self._a = dist(self._point_1, self._point_2)
        self._b = dist(self._point_2, self._point_3)

    def __str__(self):
        return " ".join([super().__str__(), self._point_1.__str__(),
                         self._point_2.__str__(), self._point_3.__str__(),
                         self._point_4.__str__()])

    def area(self):
        return self._a * self._b

    def perimeter(self):
        return (self._a + self._b)*2

class Square(Rectangle):
    def __init__(self, p1, p2, p3, p4, type = "Square"):
        super().__init__(p1, p2, p3, p4, type)
        self._a = dist(self._point_1, self._point_2)

    def __str__(self):
        return super().__str__()

    def area(self):
        return self._a ** 2

    def perimeter(self):
        return 4 * self._a

class Rhombus(Rectangle):
    def __init__(self, p1, p2, p3, p4, type = "Rhombus"):
        super().__init__(p1, p2, p3, p4, type)
        self._a = dist(self._point_1, self._point_2)
        self._diag_1 = dist(self._point_1, self._point_3)
        self._diag_2 = dist(self._point_2, self._point_4)


    def __str__(self):
        return super().__str__()

    def area(self):
        return 0.5 * self._diag_1 * self._diag_2

    def perimeter(self):
        return 4 * self._a

class Circle(Shape):
    def __init__(self, p1, r, type = "Circle"):
        super().__init__(type)
        self._r = r
        self._center = p1

    def __str__(self):
        return " ".join([super().__str__(), self._center.__str__(),
                         self._r.__str__()])

    def area(self):
        return math.pi * self._r**2

    def perimeter(self):
        return 2 * math.pi * self._r

a = Square (Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
print(a)
print(a.area())
print(a.perimeter())
b = Circle(Point(0, 0), 4)
print(b)
print(b.area())













