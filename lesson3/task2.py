"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def my_function(name, surname, year, city, email, phone_number):
    return ' '.join([name, surname, year, city, email, phone_number])

print(my_function(name='Petr', surname='Petrov', year='2000', city='SPb', email='email@mail.ru',
              phone_number='8-999-777-66-55'))