"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for el in self.my_list:
            print(*el)
        return ''

    def __add__(self, other_matrix):
        out_matrix = []
        for i in range(len(self.my_list)):
            tmp_list = []
            for j in range(len(self.my_list[i])):
                tmp_list.append(self.my_list[i][j] +
                                other_matrix.my_list[i][j])
            out_matrix.append(tmp_list)
        return Matrix(out_matrix)


lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix1 = Matrix(lst1)
matrix2 = Matrix(lst2)
matrix3 = matrix1 + matrix2

print('Исходная матрица 1')
print(matrix1)

print('Исходная матрица 2')
print(matrix2)

print('Сумма матриц')
print(matrix3)