from datetime import datetime
import time

def fun_time(var):
    count = 0
    new_list = []
    while count < var:
        count += 1
        time.sleep(1)
        new_list.append(datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S'))
    return new_list


elements = int(input('Сколько раз нужно вывести текущее время :'))



gen_list = [output for output in fun_time(elements)]
print(gen_list)