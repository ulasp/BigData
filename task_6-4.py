'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.
'''

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn_direction(self):
        return f"Машина {self.name} повернула"

    def show_speed(self):
        return f"Скорость автомобиля {self.name} {self.speed} км/ч"

class TownCar(Car):

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} {self.speed} км/ч")
        if self.speed > 60:
            return f"Внимание! Превышение скорости!"
        else:
            return {self.name}

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} {self.speed} км/ч")
        if self.speed > 40:
            return f"Внимание! Превышение скорости!"
        else:
            return {self.name}

class PoliceCar(Car):

    def police(self):
        if self.is_police:
            return f'{self.name} — автомобиль полиции'
        else:
            return f'{self.name} — неполицейский автомобиль'

mazda = SportCar(120, 'Red', 'Mazda MX-5 Miata', False)
audi = TownCar(50, 'White', 'Audi A3', False)
citroen = WorkCar(70, 'Brown', 'Citroen Berlingo', True)
ford = PoliceCar(110, 'White', 'Ford Police Responder', True)

print(mazda.turn_direction())
print(ford.police())
print(citroen.show_speed())
print(ford.show_speed())
print(f'Сотрудник полиции на автомобиле {ford.name} преследовали автомобиль {mazda.name} двигавшийся со скоростью {mazda.speed} ')