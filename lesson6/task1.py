"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
третьего (зелёный) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from itertools import cycle
from time import sleep

class TrafficLight:
    __color = cycle([
        {"сигнал": "красный", "пауза": 7},
        {"сигнал": "жёлтый", "пауза": 2},
        {"сигнал": "зелёный", "пауза": 3},
        {"сигнал": "жёлтый", "пауза": 2}
    ])

    def running(self):
        signal = next(self.__color)
        print(f"Горит {signal['сигнал']}, переключение через {signal['пауза']} сек.")
        sleep(signal['пауза'])

tl = TrafficLight()
tl.running()
tl.running()
tl.running()
tl.running()