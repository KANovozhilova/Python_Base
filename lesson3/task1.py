"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def my_function (a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Делить на ноль нельзя."
    except ValueError:
        return "Вводите только числа."
print(my_function(int(input("Первое число: ")), int(input("Второе число: "))))
