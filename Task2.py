"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivideException(Exception):

    def __init__(self, msg):
        self.msg = msg


dig1 = int(input('Введите число 1: '))
dig2 = int(input('Введите число 2: '))

try:
    if dig2 == 0:
        raise MyZeroDivideException('Деление на 0!')
    res = dig1 / dig2
except MyZeroDivideException as err:
    print(err)
else:
    print(f'Результат: {res}')