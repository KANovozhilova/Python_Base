"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

input_file = True
file = open('task1.tmp', 'w', encoding='UTF-8')
while input_file:
    print("Вводите данные, для окончания программы оставьте строку пустой.")
    line = input()
    if line == '':
        input_file = False
    else:
        file.write(line + '\n')
file.close()