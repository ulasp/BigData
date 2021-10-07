'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь
определенное название. К типам одежды в этом проекте относятся пальто
и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, name, param):
        self.name = name
        self.param = param

    @abstractmethod
    def calculate(self, param):
        pass

class Suit(Clothes):
    def __init__(self, name, param):
        super().__init__(name, param)
    @property
    def calculate(self):
        return self.param * 2 + 0.3

class Coat(Clothes):
    def __init__(self, name, param):
        super().__init__(name, param)
    @property
    def calculate(self):
        return self.param / 6.5 + 0.5

# class FullSquare(Suit, Coat):
#     def __init__(self, param):
#         super().__init__(param)
#
#     def calculate(self, param):
#         print(f'{param * 2 + 0.3 + param / 6.5 + 0.5}')


my_suit = Suit("BreySteve", 12)
my_coat = Coat("MaxMara", 23)
print(f'На костюм {my_suit.name} потребуется ткани: {my_suit.calculate}')
print(f'На пальто {my_coat.name} потребуется ткани: {my_coat.calculate}')
print(f'Общий расход ткани: {my_suit.calculate + my_coat.calculate}')

