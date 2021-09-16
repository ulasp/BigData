'''
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

# ------------- ВЫПОЛНЕНИЕ -----------------------
'''
my_list = ['м', 'о', 'й', 1, 'с', 'п', 'и', 'с', 'о', 'к']
el = 0
while el <= len(my_list) - 1:
    print(f'Тип {el}-го элемента списка «{my_list[el]}»:{type(my_list[el])}')
    el += 1
'''
# ------------------------------------------------


'''
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''
# ------------- ВЫПОЛНЕНИЕ -----------------------
# --------- Сначала сделала так, иcпользуя срез для определения интервала ------------------
'''
i = 0
el = 0
my_list = []
a = 0
countity_list = int(input('Введите какое количество элементов будет в списке: '))
while i < countity_list:
    my_list.append(input(f'Введите элемент {i+1}: '))
    i += 1
print(f'Исходный список {my_list}')
while a < int(len(my_list[:countity_list-1:2])):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
    a += 1
print(my_list)
'''
# ---------------------------------------------------------

# --------посмотрела разбор ДЗ, используя range()--------
'''
i = 0
el = 0
my_list = []
countity_list = int(input('Введите какое количество элементов будет в списке: '))
while i < countity_list:
    my_list.append(input(f'Введите элемент {i+1}: '))
    i += 1
print(f'Исходный список {my_list}')
for item in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el +=2
print(f'Итоговый список: {my_list}')
'''
# -----------------------------------------------

'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
# ------------- ВЫПОЛНЕНИЕ -----------------------

# со списком
'''
try:
    el = int(input('Введите номер месяца в виде целого числа (от 1 до 12)'))
except ValueError:
    print('Неверное введен номер месяца, нужно ввести число')
else:
    list_winter = [1, 2, 12]
    list_spring = [3, 4, 5]
    list_summer = [6, 7, 8]
    list_autumn = [9, 10, 11]
    if el in list_winter:
        print('зима')
    elif el in list_spring:
        print('весна')
    elif el in list_summer:
        print('осень')
    elif el in list_autumn:
        print('лето')
    else:
        print('Невозможно определить по введенному номеру')
'''
# ------------------------------
# со словарем
'''
try:
    el = int(input('Введите номер месяца в виде целого числа (от 1 до 12)'))
except ValueError:
    print('Неверное введен номер месяца, нужно ввести число')
else:
    dict_season = {1:'зима', 2:'зима', 3:'весна', 4:'весна', 5:'весна', 6:'лето', 7:'лето', 8:'лето', 9:'осень', 10:'осень', 11:'осень', 12:'зима'}
    print(dict_season.setdefault(el))
'''
# ---------------------------------------------
'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''
# ------------- ВЫПОЛНЕНИЕ -----------------------
'''
stroka = input('Введите строку из нескольких слов, разделённых пробелами: ')
stroka_po_slovam = stroka.split()
for el in range(len(stroka_po_slovam)):
    dlina = len(stroka_po_slovam[el])
    if dlina > 10:
        dlin_stroka = stroka_po_slovam[el]
        print(f'Слово №{el}: {dlin_stroka[:10]}')
    else:
        print(f'Слово №{el}: {stroka_po_slovam[el]}')
    el += 1
'''
# -------------После разбора ДЗ вспомниал что есть enumerate-------------------------------------
'''
stroka = input('Введите строку из нескольких слов, разделённых пробелами: ')
stroka_po_slovam = stroka.split()
for i, word in enumerate(stroka_po_slovam, 1):
    print(i, word[:10])
'''
# --------------------------------------------------

'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
'''
# ------------- ВЫПОЛНЕНИЕ -----------------------
'''
my_list = [7, 5, 3, 3, 2, 9, 4, 3]
my_list.sort(reverse = True)
print(f'Исходный рейтинг: {my_list}')
i=0
try:
    el = int(input('Введите натуральное число: '))
    for i in my_list:
        if i == el:
            count_el = my_list.count(el)
            index_el = my_list.index(el)
            new_index_el = index_el + count_el
            my_list.insert(new_index_el, el)
            print(f'Итоговый рейтинг: {my_list}')
            break
    else:
        new_index_el = 1
        my_list.insert(new_index_el, el)
        my_list.sort(reverse=True)
        print(f'Итоговый рейтинг: {my_list}')
except ValueError:
    print('Неверно введены данные!')
'''
# --------------------------------------------------
#-------После разбора ДЗ попробовала способ, предложенный Александрой---
'''
my_list = [7, 5, 4, 3, 2]
print(f'Исходный рейтинг: {my_list}')
my_list_copy = my_list.copy()
i=0
try:
    el = int(input('Введите натуральное число: '))
    if el > my_list[0]:
        my_list_copy.insert(0, el)
    elif el < my_list[-1]:
        my_list_copy.append(el)
    else:
        for rating in my_list:
            if el == rating:
                rating_index = my_list.index(rating)
                rating_count = my_list.count(rating)
                new_range_index = rating_index + rating_count
                my_list_copy.insert(new_range_index, el)
                break
            elif el > rating:
                my_list_copy.insert(my_list.index(rating), el)
                break
            else:
                continue
except ValueError:
    print('Неверно введены данные!')
print(my_list_copy)
'''
# ----------------------------------------------------
'''
6. * Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
'''
# ------------- ВЫПОЛНЕНИЕ -----------------------

# print("Товары:")
# num_tuple = (1)
# #num_product = input('Введите номер: ')
# dict_product = {'Название': 'Бисер', 'Цена': 40, 'Количество': 20, 'Единица измерения': 'шт'}
# tuple_product = list(num_tuple).append(dict_product)
# print(tuple_product)

# ------------------------------------------------
'''
product = int(input("Введите количество товара "))
i = 1
dict_product = []
my_list = []
total_prod = {}
while i <= product:
    dict_product = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
    my_list.append((i, dict_product))
    i += 1
    total_prod = dict(
        {'название': dict_product.get('название'), 'цена': dict_product.get('цена'), 'количество': dict_product.get('количество'),
         'ед': dict_product.get('ед')})
print(my_list)
print(total_prod)
'''
# --------после разбора-------------
'''
my_struct = []
while True:
    check_inputs = input('Продолжить ввод y/n: ')
    if check_inputs == 'y':
        dict_product = dict({'название': input("введите название "), 'цена': input("Введите цену "),
                             'количество': input('Введите количество '), 'eд': input("Введите единицу измерения ")})
        my_struct.append((len(my_struct)+1, dict_product))
    elif  check_inputs == 'n':
        break
    else:
        check_inputs = input('Продолжить ввод y/n: ')
print(my_struct)
'''
# -----------------------------------