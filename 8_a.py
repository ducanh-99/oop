from abc import ABC, abstractclassmethod


class Point:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Shape:

    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimeter(self):
        pass


class Triangle(Shape):
    x1: Point
    x2: Point
    x3: Point

    def __init__(self, x1: Point, x2: Point, x3: Point) -> None:
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3


class Rectangle(Triangle):
    x4: Point

    def __init__(self, x1: Point, x2: Point, x3: Point, x4: Point) -> None:
        super().__init__(x1, x2, x3)
        self.x4 = x4

        if not self.check_perpendicular():
            print("4 goc khong vuong")

    def check_perpendicular(self) -> bool:
        pass


class Square(Rectangle):

    def __init__(self, x1: Point, x2: Point, x3: Point, x4: Point) -> None:
        super().__init__(x1, x2, x3, x4)

        if not self.check_perpendicular():
            print("4 canh goc vuong khong bang nhau")

    def check_4_edge_equal(self) -> bool:
        pass
