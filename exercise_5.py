import random

print('Ведите диапозон цифр в котором вы хотите угадать число!')

start_random = int(input('Введите начало: '))
stop_random = int(input('Введите конец: '))

random_number = random.randrange(start_random, stop_random + 1)

print('Как думаете какое число получилось?')

guess = int(input('Ведите его: '))

if random_number == guess:
    print(f'Вы угадали, это было число {random_number} !\nПоздравляем!')
else:
    print(f'К сожалению вы не угадали, слуйчайным числом было {random_number}!')


