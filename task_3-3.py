'''3. Реализовать функцию my_func(), которая принимает три позиционных
   аргумента, и возвращает сумму наибольших двух аргументов.
'''
# ---------------------------Выполнение--------------------------

def my_func(var_1, var_2, var_3):
    if var_1 > var_2 and var_1 < var_3:
        return var_1 + var_3
    elif var_1 > var_2 and var_2 > var_3:
        return var_1 + var_2
    else:
        return var_2 + var_3
try:
    var_1 = int(input("Введите первый аргумент: "))
    var_2 = int(input("Введите второй аргумент: "))
    var_3 = int(input("Введите третий аргумент: "))
    print(f'Result: {my_func(var_1, var_2, var_3)}')
except ValueError:
    print('Неверно введены данные! Нужно вводить числа')

#----------------------------------------------------------------
