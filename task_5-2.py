'''
2. Создать текстовый файл (не программно),сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

#file_obj = open("file_task_5_2", 'r')
with open("file_task_5_2", 'r') as file_obj:
    # letter = 0
    line_count = 0
    words = 0
    for line in file_obj:
        line_count += 1
        words = line.count(' ') + 1
        print(f'Количество слов в строке {line_count}: {words}')

    print(f'Всего строк в файле: {line_count}')
#file_obj_w.close()