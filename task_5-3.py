'''
3. Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии
этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
'''

line_count = 0
small_salary = []
salary_list=[]
salary = []
from functools import reduce, partial

with open("file_task_5_3", 'r') as file_obj:
    line = file_obj.read().split("\n")
    for surname in line:
        surname = surname.split()
        if int(surname[1]) < 20000:
            small_salary.append(surname[0])
        salary_list.append(int(surname[1]))
    mid_salary = round((reduce(lambda x, y: x+y, salary_list)) / len(salary_list))

print(f'Сотрудники с окладом меньше 20000: {small_salary}')
print(f'Средняя зарпалата: {mid_salary}')
