'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться
на русские. Новый блок строк должен записываться в новый текстовый файл
'''
my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
with open('file_task_5_4', 'r') as file_obj, open('file_task_5_4_w', 'w') as file_obj_w:
    for line in file_obj.readlines():
        numerals, numbers = line.rstrip("\n").split(" — ")
        print(my_dict[numerals])
        file_obj_w.write(f"{my_dict[numerals]} – {numbers}\n")
