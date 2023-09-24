"""Написать лямбда-функцию определяющую чётное/нечетное.
Функция принимает параметр (число) и если четное, то выдает слово 'четное'
если нет - то 'нечетное.'"""
x = lambda var: print('Четное') if var % 2 == 0 else print('Нечетное')

x(5)


""" Дан список чисел. Вернуть список, где при помощи функции map() каждое число
 переведено в строку. В качестве функции в map использовать lambda"""
number = [1, 2, 3,
          4, 5, 6
          ]
str_list = list(map(lambda x: str(x), number))

print(str_list)

""" При помощи функции filter() из кортежа слов отфильтровать только
те, которые являются полиндромами"""
x = ('дед', 'пока',
     'привет', 'шалаш'
     )
test = tuple(filter(lambda var: var == var[::-1], x))
print(test)

""" Написать декоратор к 2-м любым функциям, который бы считал и 
выводил время их исполнения"""
from datetime import datetime
def decoration_fun(timmer):
    def wrapper():
        start = datetime.now()
        timmer()
        end = datetime.now() - start
        print(end)
    return wrapper


@decoration_fun
def function_1():
    x = list(map(lambda x: x*x+x, [1, 2, 3, 4, 5]))
    print(x)

@decoration_fun
def function_2():
    x = 50 + 50



function_1()
function_2()


""" Сделать функцию которая на вход принимает строку. Анализирует её
исключительно методом .isdigit() без доп.библиотек и переводит строку в число.
Функция умеет распознавать отрицательные числа идесятичные дроби."""
def fun_2(x):
    if isinstance(float(x), float):
        x = float(x)
        if x > 0:
            print(f'Вы ввели положительное дробное число{x}')
        else:
            print(f'Вы ввели отрицательно дробное число{x}')
    elif isinstance(int(x), int):
        print(f'Вы ввели отрицательное целое число{x}')
    else:
        print(f'Вы ввели неккоректное значение{x}')
def function_str(var):
    if var.isdigit():
        x = float(var)
        if x == int(x):
            print(f'Вы ввели положительное целое число {x}')
    else:
        fun_2(var)


function_str(input('ВВедите значение :'))