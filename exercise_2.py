number = int(input(('Введите число, факториал которого вы хотите найти: ')))

def fun_factorial(number):
    count = 0
    factorial = 1
    while count < number:
        count += 1
        factorial *= count
    return factorial







print(f'Факториал числа {number} = {fun_factorial(number)}')
