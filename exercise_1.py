data = input('Введите предложение состоящее из двух слов: ')
my_list = data.split()
first = my_list[0]
second = my_list[1]
symbols = ' ! '
print(f'!{second}{symbols}{first}!')

data = input('Введите предложение состоящее из двух слов: ')
my_list = data.split()
first = my_list[0]
second = my_list[1]
symbols = ' ! '
print('!%s%s%s!' % (second, symbols, first))

data = input('Введите предложение состоящее из двух слов: ')
my_list = data.split()
first = my_list[0]
second = my_list[1]
symbols = ' ! '
print('!{}{}{}!'.format(second, symbols, first))
