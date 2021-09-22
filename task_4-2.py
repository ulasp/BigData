'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
'''
def my_list():
    new_list = []
    i = 0
    original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    for i in range(len(original_list) - 1):
        if original_list[i] < original_list[i+1]:
            el_list = original_list[i+1]
            new_list.append(el_list)
        i += 1
    yield new_list

gen = my_list()
for i in gen:
    print(i)

'''

#Этот вариант понравился больше:
''' 
new_list = []
i = 0
original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [lvalue for i, lvalue in enumerate(original_list) if original_list[i] > original_list[i-1] and i!=0]
print(new_list)
'''