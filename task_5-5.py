'''
5. Создать (программно) текстовый файл, записать в него программно
набор чисел, разделенных пробелами. Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.
'''
from functools import reduce, partial
# записываем в файл набор чисел таким образом:
numbers = [i for i in range(1, 11, 2)]
with open("file_task_5_5_w", 'w') as file_objec_w:
    for i in numbers:
        file_objec_w.write(f"{i} ")
# читаем, что там в файле записалось и выводим сумму чисел
with open("file_task_5_5_w", 'r') as file_obj:
    line = file_obj.read()
    str_line = list(line.split())
    int_line = [int(el) for el in str_line]
    print(int_line)
    sum = reduce(lambda x, y: x+y, int_line)
    print(f'Сумма чисел в файле: {sum}')