'''
3. Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить
только числа и строки. При вводе пользователем очередного элемента необходимо
реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
'''

class MyException(Exception):
    def __ini__(self, txt):
        self.txt = txt

my_list = []
my_str = input("Введите число и нажимайте Enter: ")

while my_str:
    try:
        if my_str.isdigit():
            my_list.append(int(my_str))
        else:
            raise MyException('Некорректный тип данных, нужно число!')
    except MyException as err:
        print(err)

    my_str = input("Для завершения введите пустое значение: ")

print(my_list)


