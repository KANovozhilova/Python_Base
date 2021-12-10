"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт количества строк и количества слов в каждой строке.
"""

with open('task2.data', 'r', encoding='UTF-8') as file:
    lines = file.readlines()
    print(f"Всего строк в файле: {len(lines)}")
    for key, value in enumerate(lines):
        words = value.split(' ')
        print(f"Слов в строке {key + 1} - {len(words)}")