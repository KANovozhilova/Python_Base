"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
import random

with open('task5.tmp', 'w', encoding='UTF-8') as file:
    space = ''
    for _ in range(5):
        file.write(space + str(random.randint(0, 5)))
        space = ' '

with open('task5.tmp', 'r', encoding='UTF-8') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Числа в файле:\n{numbers_str}")
    print(f"Сумма всех чисел: {sum([int(i) for i in numbers_lst])}")