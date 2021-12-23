"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Complex(a, b)

    def __mul__(self, other):
        a = (self.a * other.a) - (self.b * other.b)
        b = (self.a * other.b) + (self.b * other.a)
        return Complex(a, b)

    def __str__(self):
        return f"{self.a} + {self.b}i"

if __name__ == "__main__":
    my_com1 = Complex(2, 3)
    my_com2 = Complex(4, 5)
    my_com3 = my_com1 + my_com2
    my_com4 = my_com1 * my_com2

    print(f"my_com1 = {my_com1}")
    print(f"my_com2 = {my_com2}")
    print(f"my_com1 + my_com2 = {my_com3}")
    print(f"my_com1 * my_com2 = {my_com4}")