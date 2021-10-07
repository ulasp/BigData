'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год». В рамках класса реализовать
два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором
@staticmethod, должен проводить валидацию числа, месяца и года (например,
месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
'''
class Data:

    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)
        print(f'Исходная дата: {d_m_y}')

    @classmethod
    def get_d_m_y(cls, dmy):
        res = dmy.split(" - ")
        return int(res[0]), int(res[1]), int(res[2])

    def __str__(self):
        return f'Полученная дата: {Data.get_d_m_y(self.d_m_y)}'

    @staticmethod
    def valid_data(d_m_y):
        d, m, y = d_m_y
        if 1 <= d <= 31:
            if 1 <= m <= 12:
                if 2019 >= y >= 0:
                    return f'Процесс проверки прошел успешно!'
                else:
                    return f'Некорректно указан год'
            else:
                return f'Некорректно указан месяц'
        else:
            return f'Некорректно указан день'

today_data = Data('11 - 13 - 2001')
print(today_data)
my_date = today_data.get_d_m_y(today_data.d_m_y)
print(today_data.valid_data(my_date))
'''


class Data:

    def __init__(self, d_m_y):
        self.d_m_y = str(d_m_y)
        print(f'Исходная дата: {d_m_y}')

    @classmethod
    def get_d_m_y(cls, dmy):
        try:
            res = dmy.split(" - ")
            return int(res[0]), int(res[1]), int(res[2])
        except Exception as err:
            print(f'Не удалось выделить дату {err}')

    def __str__(self):
        return f'Полученная дата: {Data.get_d_m_y(self.d_m_y)}'

    @staticmethod
    def valid_data(d_m_y):
        try:
            d, m, y = d_m_y
            # через range я что-то не догадалась сделать :)
            if d not in range(1, 32):
                raise ValueError('Некорректно')
            elif m not in range(1, 12):
                raise ValueError('Некорректный месяц')
            elif y not in range(0, 2021):
                raise ValueError('Некорректный год')
        except ValueError as err:
            print(err)
        else:
            print(f'Проверка прошла успешно')

today_data = Data('11 - 13 - 2001')
print(today_data)
my_date = today_data.get_d_m_y(today_data.d_m_y)
print(today_data.valid_data(my_date))
