"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

info = []
with open('task7.data', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    profit_sum = 0
    for row in file:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_sum += profit
    info.append(profits)
    info.append({'средняя прибыль': (profit_sum / len(profits))})
    # пока не придумала, как включить в список фирмы, получившие убытки

with open('task7.json.tmp', 'w', encoding='UTF-8') as json_file:
    json.dump(info, json_file, ensure_ascii=False)

json_info = json.dumps(info, ensure_ascii=False)

print(f"Список фирм:\n{text}\n")
print(f"Список фирм, получивших прибыль:\n{info}\n")
print(f"json-объект:\n{json_info}")