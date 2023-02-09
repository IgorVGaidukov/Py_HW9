"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotNum(Exception):

    def __init__(self, lst):
        self.lst = lst


num_char = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

num_str = input('Введите несколько чисел, разделённых пробелами: ').split()
nums = []
for el in num_str:
    fl = True
    try:
        for i in range(len(el)):
            if not (el[i] in num_char):
                fl = False
                raise NotNum(f'{el} - не число')
        if fl:
            nums.append(int(el))
    except NotNum as err:
        print(err)

print(f'Итоговый числовой массив: {nums}')