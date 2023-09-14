while True:
    name = input('Введите ваше имя: ')
    age = input('Введите ваш возраст: ')

    if age.isdigit():
        age = int(age)
        if age <= 0:
            print('Ошибка повторите ввод')
        elif 10 > age > 0:
            print(f'Привет1, шкет {name}')
        elif 18 >= age >= 10:
            print(f'Как жизнь {name} ?')
        elif 100 > age > 18:
            print(f'Что желаете {name} ?')
        else:
            print(f'{name}, вы лжете - в нашей стране столько не живут...')
    else:
        print('Ошибка повторите ввод')
