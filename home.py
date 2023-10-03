# """
# 1. Создать родительский класс auto, у которого есть атрибуты:
# brand, age, color, mark и weight.
# А так же методы: move, birthday и stop. Методы move и stop
# выводят сообщение на экран «move» и «stop»,
#   a birthday увеличивает атрибут аде на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.
# """
#
# import time
# class Auto:
#     brand = 'Lada'
#     age = 15
#     color = 'red'
#     mark = 2114
#     weight = 1500
#
#     def move(self):
#         print('move')
#
#     def stop(self):
#         print('stop')
#
#     def birthday(self):
#         self.age += 1
#
#
# a = Auto()
# a.move()
# a.birthday()
# a.stop()
# print(a.age)
#
#
# """
# 2. Создать 2 класса truck и car, которые являются наследниками класса auto. Класс truck имеет дополнительный
# обязательный атрибут max_load. Переопределённый метод move, перед появлением надписи «move»
# выводит надпись «attention», его реализацию сделать при помощи оператора super.
# А так же дополнительный метод load. При его вызове происходит пауза 1 сек., затем выдаётся сообщение «load»
# и снова пауза 1 сек. Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода m
# ove, после появления надписи «move» должна появиться надпись «max speed is <max_speed>». Создать по 2 объекта для каждого
# из классов truck и car, проверить все их методы и атрибуты.
# """
# class Truck(Auto):
#     max_load = 2
#     speed = 50
#     def move(self):
#         print(f'attention')
#         super().move()
#     def load(self):
#         time.sleep(1)
#         print('load')
#         time.sleep(1)
#
# class Car(Auto):
#     max_speed = '100'
#     load = 2
#     def move(self):
#         super().move()
#         print(f'max speed is {c.max_speed}')
#
#
# t = Truck()
# t.move()
# t.load()
# print(t.speed)
# print(t.brand)
# print(t.color)
# print(t.age)
# print(t.weight)
#
# t_2 = Truck()
# t_2.move()
# t_2.load()
# print(t_2.brand)
# print(t_2.color)
# print(t_2.age)
# print(t_2.weight)
#
#
# c = Car()
# c.move()
# print(c.load)
# print(c.max_speed)
# print(c.brand)
# print(c.color)
# print(c.age)
# print(c.weight)
#
# c_2 = Car()
# c_2.move()
# print(c_2.max_speed)
# print(c_2.brand)
# print(c_2.color)
# print(c_2.age)
# print(c_2.weight)


class Point:
    def point(self):
        return '.'


class Circle:
    def __init__(self, a):
        self.radius = a

    def get_circle_area(self):
        return 3.14 * self.radius ** 2


class Figure:

    def subtraction(self):
        a = [c.get_circle_area(), c_1.get_circle_area()]
        x = a[0] - a[1]
        print(x)
    def subtraction_modul(self):
        a = [c.radius, c_1.radius]

        if a[0] == a[1]:
            print(p.point())
        else:
            x = a[0] - a[1]
            modul = x + 2
            z = x % modul
            if z > modul:
                z -= modul
            print(z)

p = Point()
number = int(input('Введите вычитаемое число'))
number_2 = int(input('Введите вычитатель'))
c = Circle(number)
c_1 = Circle(number_2)

f = Figure()
f.subtraction()
f.subtraction_modul()
