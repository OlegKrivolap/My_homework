""" Декодировать в строку байтовое значение:b'r\xc3\xa9sum\xc3\xa9'.
Затем результат преобразовать в байтовый вид в кодировке 'Latin1'
и затем результат снова декодировать в строку( результат на экран)"""

# import codecs
#
# utf = codecs.decode(b'r\xc3\xa9sum\xc3\xa9')
# print(utf)
#
# latin = utf.encode('Latin1')
# print(latin)
#
# again_utf = latin.decode('Latin1')
# print(again_utf)

""" Ввесть с клавиатуры 4 строки и сохранить их в 4 разные переменные.
Создать файл и записать в него первые 2 строки и закрыть файл.
Затем открыть файл на редактирование и дозаписать оставшиеся строки.
В итоговом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.
"""
# var_1, var_2 = '', ''
# var_3, var_4 = '', ''
# count = 0
# while count < 4:
#     x = input('Введите строку:\n')
#     count += 1
#     if count == 1:
#         var_1 += x
#     elif count == 2:
#         var_2 += x
#     elif count == 3:
#         var_3 += x
#     else:
#         var_4 += x
#
# x_2 = open(r'home.txt', 'w')
#
# x_2.write(var_1 + '\n')
# x_2.write(var_2 + '\n')
#
# x_2.close()
# 
# x_1 = open(r'home.txt', 'a')
#
# x_1.write(var_3 + '\n')
# x_1.write(var_4 + '\n')
#
# x_1.close()

"""Создать словарь в качестве ключа которого будет 6-ти значное
число(id), а в качестве значений кортеж состоящий из 2-х элементов -
имя(str), возраст(int). Сделать около 5-6 элементов словаря.
Записать данный словарь на диск в json-файл.
"""

# import json
# my_dict = {
#     160689: ('Olga', 15), 785369: ('Egor', 18),
#     753951: ('Egor', 20), 153957: ('Oleg', 19),
#     659754: ('Misha', 21), 246864: ('Sasha', 18)
# }
#
# with open(r'dictionary.json', 'w') as w_file:
#     json.dump(my_dict, w_file, indent=2)
#
# w_file.close()


"""Прочитать сохраненный json-файл и записать данные на диск в csv-файл,
первой строкой которого озаглавив каждый столбец и добавив новый столбец
'телефон'
"""
# import json
# import csv
#
# with open(r'dictionary.json', 'r') as r_file:
#     data = json.load(r_file)
#     new_data = []
#     number_1 =[375445614692, 37533751953, 375298426249,
#                37529753951, 37529789321, 37544651832
#                ]
#     summ = ''
#     for id, value in data.items():
#         summ += id
#         count = 0
#         if len(summ) == 6:
#             summ = int(summ)
#             value.insert(0, summ)
#             summ = ''
#         value.insert(3, number_1[count])
#         count += 1
#         new_data.append(value)
#         print(summ)
# r_file.close()
#
#
#
# with open(r'my_file.csv', 'w') as w_file:
#     writer = csv.writer(w_file)
#     writer.writerow(['id', 'name', 'age', 'number'])
#     for i in new_data:
#         writer.writerow(i)
#
# w_file.close()