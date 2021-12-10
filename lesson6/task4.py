"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"Cкорость {speed} км/ч.")

    def stop(self):
        self.speed = 0
        print("Машина остановилась.")

    def turn(self, direction: str):
        if self.speed > 0:
            print(f"Машина поворачивает {direction}.")
        else:
            print("Машина стоит на месте")

    def show_speed(self):
        print(f"Сейчас скорость {self.speed} км/ч.")


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f"Внимание! Превышение скорости.")
        else:
            print(f"Скорость {self.speed} км/ч.")


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f"Внимание! Превышение скорости.")
        else:
            print(f"Скорость {self.speed} км/ч.")


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test(auto):
    print(f"Автомобиль {auto.name}, цвет {auto.color}.")
    auto.go(40)
    auto.turn("направо")
    auto.turn("налево")
    auto.go(80)
    auto.show_speed()
    auto.go(140)
    auto.show_speed()
    auto.stop()

solaris = TownCar("синий", "Hyundai Solaris")
test(solaris)

# urus = SportCar("чёрный", "Lamborgini Urus")
# test(urus)

# bmw = WorkCar("серый", "BMW")
# test(bmw)

# ceed = PoliceCar("белый", "Kia Ceed")
# test(ceed)