"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдёте в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, matrix:list):
        self.matrix = matrix

    def __str__(self):
        result = []
        for row in self.matrix:
            result.append(' '.join([str(k) for k in row]))
        return '\n'.join(result)

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            result = []
            for i, row in enumerate(self.matrix):
                new_list = list(map(lambda x, y: x + y, row, other.matrix[i]))
                result.append(new_list)
            return Matrix(result)
        else:
            return

#list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)
matrix_3 = matrix_1 + matrix_2

print(matrix_1, end='\n\n')
print(matrix_2, end='\n\n')
print(matrix_3)