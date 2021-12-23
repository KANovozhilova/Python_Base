"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Date:
    def __init__(self, date):
        self.date = date

    def my_data(self):
        try:
            day, month, year = self.date.split("-")
            return int(day), int(month), int(year)
        except Exception as ex:
            print(f"Дата не была извлечена из строки. Некорректные данные.")

    @staticmethod
    def val_data(date_input):
        try:
            day, month, year = date_input
            if day not in range(1, 32):
                raise ValueError("Число задано неверно.")
            elif month not in range(1, 13):
                raise ValueError("Месяц задан неверно.")
            elif year not in range(0, 2022):
                raise ValueError("Год задан неверно.")
        except ValueError as ex:
            print(ex)
        else:
            print("Ок.")

input_date = Date("23-12-2021")
# input_date = Date("32-12-2021")
# input_date = Date("тест")
my_date = input_date.my_data()
print(my_date)
if my_date:
    input_date.val_data(my_date)