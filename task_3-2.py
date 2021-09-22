'''2. Реализовать функцию, принимающую несколько параметров, описывающих
   данные пользователя: имя, фамилия, год рождения, город проживания,
   email, телефон. Функция должна принимать параметры как именованные аргументы.
   Реализовать вывод данных о пользователе одной строкой.
'''
# ---------------------------Выполнение--------------------------

def user_dict(name, surname, year_of_birth, city, email, tel):
    user_name = f"{name}, {surname}"
    user_year_of_birth = f"{year_of_birth}"
    user_city = f"{city}"
    user_email = f"{email}"
    user_tel = f"{tel}"
    return user_name, user_year_of_birth, user_city, user_email, user_tel

user_name, user_year_of_birth, user_city, user_email, user_tel = user_dict(
    name="Uliana", surname="Spivachuk", year_of_birth=1980, city="Feo", email="ula@mail.ru", tel="8-3-456-67-88")
print(f'Данные о пользователе: {user_name}, {user_year_of_birth}, {user_city}, {user_email}, {user_tel}')

# --------------------- а можно же используя join: ---------------------
'''
def user_dict(name, surname, year_of_birth, city, email, tel):
    return ' '.join([name, surname, year_of_birth, city, email, tel])

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
year_of_birth = input("Год рождения: ")
city = input("Город проживания: ")
email = input("Электроный адрес: ")
tel = input("Номер телефона: ")

print(user_dict(name, surname, year_of_birth, city, email, tel))
'''
#----------------------------------------------------------------
