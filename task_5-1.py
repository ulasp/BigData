'''
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
'''
while True:
    my_string = input("Введите строку: ")
    if my_string == "":
        print("Внесение изменений в файл завершено")
        break
    else:
        file_obj_w = open("my_file", 'a')
        print(f"{my_string}", file=file_obj_w)

file_obj_w.close()
'''
# Еще же есть with in
while True:
    my_string = input("Введите строку: ")
    if my_string == "":
        print("Внесение изменений в файл завершено")
        break
    else:
        with open("my_file", 'a', encoding='utf-8') as file_obj_w:
            print(f"{my_string}", file=file_obj_w)




