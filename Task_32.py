# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_ind_range(minR, maxR, list):
    for i in range(len(list)):
        if minR <= list[i] <= maxR:
            print(i)
    

list_1 = [1, 2, 3, 1, 5, 6, 3, 9, 4, 1, 5, 3, 7]
find_ind_range(4, 7, list_1)