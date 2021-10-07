'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''
'''
5. Продолжить работу над первым заданием. Разработать методы, отвечающие
за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
'''

class OfficeEquipmentStock:
    '''
    Класс «склад оргтехники»
    equipment_stock = {"equipment_name": name, "equipment_brand":brand,
    "equipment_price": price, "equipment_serials_number": serials_number,
    "equipment_formats": formats, "equipment_quantity": quantity}

    # equipment_stock = {"equipment_type": {"name": {"serials_number": serials_number,
    #                                                "price": price, "quantity": quantity}}}
    # {printer: {HP-094234: {"serials_number": 35uwaer , "price": 12436, "quantity": 4}}
    # scanner: {Xerox-HT-65644: {"serials_number": 1246xr3 , "price": 32436, "quantity": 14}}
    # }
    '''
    def __init__(self, name, serials_number, price, quantity, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.serials_number = serials_number

    equipment_stock = {'HP-3254wjf45', '235jhble5', 2000, 155}

    # @classmethod
    # def stock_to(cls, equipment_type, name, serials_number, price, quantity):
    #     equipment_type = cls.equipment_stock.get()
    #     if equipment_type[name] == cls.equipment_stock[name]:
    #         equipment_type[quantity] += 1
    #         #tсли проверка показала что такое есть, то quantity + 1

        #cls.equipment_stock[equipment_type] = {name: {"serials_number": serials_number,
                                                      # "price": price, "quantity": quantity}}


    def display(self):
        return {'Модель устройства': self.name, 'Серийный номер': self.serials_number, 'Цена за ед': self.price, 'Количество': self.quantity}

    # @classmethod
    # @validate
    # def stock_to(cls, item_name, item_price, item_quantity):
    #     current_quantity = cls.items_in_stock[item_name][item_price]['item_quantity']
    #     if current_quantity < item_quantity:
    #         raise ValueError
    #     else:
    #         cls.items_in_stock[item_name][item_price]['item_quantity'] -= item_quantity


    @staticmethod
    def get_items_in_stock():
        for key, value in OfficeEquipmentStock.equipment_stock.items():
            print(key, value)

class OfficeEquipment:
    '''
    Класс «Оргтехника».
    '''
    def __init__(self, name, serials_number, price, quantity):
        self.name = name
        self.price = price
        self.serials_number = serials_number
        self.quantity = quantity
        # try:
        #     if type(count) not in [int, float]

    # def in_stock(self):
    #     # print(f'Для выхода - Q, продолжение - Enter')
    #     # while True:
    #     try:
    #         name = input(f'Введите наименование ')
    #         price = int(input(f'Введите цену за ед '))
    #         quantity = int(input(f'Введите количество '))
    #         new_item = {'Модель устройства': self.name, 'Серийный номер': self.serials_number, 'Цена за ед': self.price, 'Количество': self.quantity}
    # @staticmethod
    # def get_all_equipment():
    #     for key, value in Storage.equipment_units.items():
    #         print(key, value)

class Printer(OfficeEquipment):
    '''
    Класс типа оргтехники (принтеры), класс-наследник «Оргтехники»
    '''
    def __init__(self, name, price, serials_number, type_of_print, print_speed, color):
        super().__init__(name, price, serials_number, quantity)
        self.type_of_print = type_of_print
        self.print_speed = print_speed
        self.color = color

class Scanner(OfficeEquipment):
    '''
    Класс типа оргтехники (сканеры), класс-наследник «Оргтехники»
    '''
    def __init__(self, name, brand, price, serials_number, formats, type_of_scan, resolution):
        super().__init__(name, brand, price, serials_number, formats)
        self.type_of_scan = type_of_scan
        self.resolution = resolution

class Copier(OfficeEquipment):
    '''
    Класс типа оргтехники (копиры), класс-наследник «Оргтехники»
    '''
    def __init__(self, name, brand, price, serials_number, formats, num_of_copy, color):
        super().__init__(name, brand, price, serials_number, formats)
        self.num_of_copy = num_of_copy
        self.color = color

item = OfficeEquipmentStock('HP-3254wjf45', '235jhble5', 2000, 155)
#print(item.display())

#OfficeEquipmentStock.stock_to(type="Printer", name="Hp", serials_number = "XS5050", quntity = 100)
OfficeEquipmentStock.get_all_equipment()
#print(today_data.valid_data(my_d
'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных
на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
максимум возможностей, изученных на уроках по ООП.
'''