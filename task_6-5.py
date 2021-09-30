'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        return f"Запуск отрисовки ручкой"

class Pencil(Stationery):
    def draw(self):
        return f"Запуск отрисовки карандашом"

class Handle(Stationery):
    def draw(self):
        return f"Запуск отрисовки маркером"

my_pen = Pen("Metrix")
print(f'{my_pen.draw()} {my_pen.title}')
my_pencil = Pencil("Derwent")
print(f'{my_pencil.draw()} {my_pencil.title}')
my_handle = Handle("Faber-Castell")
print(f'{my_handle.draw()} {my_handle.title}')
