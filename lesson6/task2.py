"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищёнными. Определить метод расчёта массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна.
Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т
"""

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def construct(self):
        self.weigth = 25
        self.tickness = 5
        construct = self.length * self.width * self.weigth * self.tickness / 1000
        print(f"Для строительства дороги понадобится {construct} тонн асфальта.")

road_construct = Road(5000, 20)
road_construct.construct()