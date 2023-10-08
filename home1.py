# Сделать свой класс данных, добавить в класс статикметод и классметод
from dataclasses import dataclass


@dataclass
class Square:
    side: int
    side_2: int = 10

    @classmethod
    def area(cls):
        return cls.side_2 * 10

    @staticmethod
    def calculat(side, side_2):
        return side + side_2


a = Square(5)

print(Square.area())

print(a.calculat(15, 20))


# Создать метакласс
class Square:
    side_1 = 5
    side_2 = 10

    def area(self):
        return self.side_1 * self.side_2
class Triangle:
    side_1 = 20
    side_2 = 20
    side_3 = 35

    def summ(self):
        return self.side_1 + self.side_2 + self.side_3
def method(self):
    print(self.__dict__)


B = type('Figure', (Square, Triangle), {'side_1': 10, 'side_2': 15, 'method': method})

b = B()

print(b.method())
print(b.side_1)