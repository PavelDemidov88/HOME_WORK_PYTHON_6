# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def arithm_prog(a, d, n):
    if d == 0: return print('Данная последовательность стационарная!')
    list = []
    for i in range(n):
        i = a
        list.append(i + (n-1)*d)
        n -= 1
    return list[::-1]

a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность: '))
n = int(input('Введите колличество элементов: '))
print(arithm_prog(a1, d, n))