
'''5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
   При нажатии Enter должна выводиться сумма чисел. Пользователь может
   продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
   Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
   Но если вместо числа вводится специальный символ, выполнение программы завершается.
   Если специальный символ введен после нескольких чисел, то вначале нужно добавить
   сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
# -----------------Выполнение ---------------------
list_of_num = []
def my_sum_items():
    sum_list_of_num = 0
    ex = False
    while ex == False:
        my_str = input('Input numbers or E for exit - ')
        print(my_str)
        result_sum = 0
        sum_list_of_num = 0
        for el in range(len(my_str)):
            if my_str[el] == 'e' or my_str[el] == 'E':
                ex = True
                break
            else:
                list_of_num = my_str.split()
                for i, item in enumerate(list_of_num):
                    list_of_num[i] = int(item)
                sum_list_of_num = sum(list_of_num)
        print(f'Результат {sum_list_of_num}')
    result_sum = sum_list_of_num + result_sum
    print(f'ИтогРезультат {result_sum}')


my_sum_items()
