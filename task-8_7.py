'''
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:
    def __init__(self, num1, num2, *args):
        self.num1 = num1
        self.num2 = num2
        #self.res = 'num1 + num2 * i'

    def __add__(self, other):
        # print(f'Сумма комплексных чисел равна')
        return ComplexNumber(self.num1 + other.num1, self.num2 + other.num2)

    def __mul__(self, other):
        # print(f'Произведение комплексных чисел равно')
        return ComplexNumber(self.num1 * other.num1 - self.num2 *
                             other.num2, self.num1 * other.num2 + self.num2 * other.num1)

    def __str__(self):
        return f'{self.num1} + {self.num2}'


my_complex_num1 = ComplexNumber(1, -2)
my_complex_num2 = ComplexNumber(3, 4)
# print(my_complex_num1)
print(f'Исходные комплексные числа: <<{my_complex_num1}>> и <<{my_complex_num2}>>')
print(f'Сумма комплексных чисел равна: {my_complex_num1 + my_complex_num2}')
print(f'Произведение комплексных чисел равно: {my_complex_num1 * my_complex_num2}')