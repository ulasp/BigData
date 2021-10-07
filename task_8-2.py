'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
'''
class ErrorZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt

def my_divison(inp_num1, inp_num2):
    try:
        inp_num1 = int(inp_num1)
        inp_num2 = int(inp_num2)
        if inp_num2 == 0:
            raise ErrorZeroDiv("На 0 делить нельзя!")
        # чтобы вызвать ислклбючение, нужно поставить оператор raise
    # теперь обрабатываем ошибки:
    # введене ли число?
    # введен 0:
    except ErrorZeroDiv as err:
        print(err)
    except ValueError:
        print("Вы ввели не число")
    else:
        print(f"Все ок, ваше число: {inp_num1 / inp_num2}")

inp_num1 = input("Введите 1 положительное число: ")
inp_num2 = input("Введите 2 положительное число: ")
my_divison(inp_num1, inp_num2)
'''

# посмотрела разбор, понравилось больше, переделала:
class ErrorZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt

def my_divison(inp_num1, inp_num2):
    try:
        if inp_num2 == 0:
            raise ErrorZeroDiv("На 0 делить нельзя!")
        print(f'Результат деления первого числа на второе: {inp_num1 / inp_num2}')
    except ErrorZeroDiv as err:
        print(err)


inp_num1 = int(input("Введите 1 положительное число: "))
inp_num2 = int(input("Введите 2 положительное число: "))
my_divison(inp_num1, inp_num2)
