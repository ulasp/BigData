'''
5. Реализовать формирование списка, используя функцию range()
и возможности генератора. В список должны войти четные числа
от 100 до 1000 (включая границы). Необходимо получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

my_list = [i for i in range(100, 1001) if i % 2 == 0]
#print(my_list)
from functools import reduce
print(f'Произведение всех четных чисел от 100 до 1000: {reduce(lambda x, y: x*y, my_list)}')
