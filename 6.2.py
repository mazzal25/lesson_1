# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

list_n = [-5, 9, 0, 3, -1, -2, 1,
          4, -2, 10, 2, 0, -9, 8, 10, -9,
          0, -5, -5, 7]
max = 10
min = 7

for i in range(len(list_n)):
    if  min <= list_n[i] and list_n[i] <= max:
        print (i)
