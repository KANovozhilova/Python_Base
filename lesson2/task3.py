"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons = {'Зима': (1, 2, 12),
          'Весна': (3, 4, 5),
          'Лето': (6, 7, 8),
          'Осень': (9, 10, 11)}

month = int(input("Ведите номер месяца от 1 до 12: "))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
    else:
        print("Месяц не найден ни в одном сезоне.")


# try:
#     number = int(input("Введите номер месяца от 1 до 12: "))
# except ValueError:
#     print("Неверные данные.")
# else:
#     winter = [1, 2, 12]
#     spring = [3, 4, 5]
#     summer = [6, 7, 8]
#     autumn = [9, 10, 11]
#
#     if number in winter:
#         print("Зима")
#     elif number in spring:
#         print("Весна")
#     elif number in summer:
#         print("Лето")
#     elif number in autumn:
#         print("Осень")
#     else:
#         print("Неверные данные.")