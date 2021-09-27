'''
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество
занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
from functools import reduce

sum = 0
subj = 0
lectures = []
practic_ls=[]
lab_works=[]
num_lect = []

def sum_class(sum):
    num_lect = [int(s) for s in sum if s.isdigit()]
    summa = reduce(lambda x, y: x + y, num_lect)
    return summa

with open("file_task_5_6", 'r') as file_obj:
    for line in file_obj.readlines():
        subject, lecture, practic_l, lab_work = line.rstrip("\n").split(" ")
        list_subj = subject.replace(":", "")
        lectures = lecture.replace("(л)", "")
        practic_ls = practic_l.replace("(пр)", "")
        lab_works = lab_work.replace("(лаб)", "")
        sum = lectures, practic_ls, lab_works
        subj = {subject: sum_class(sum)}
        print(subj)
