# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint
n = int(input('Введите количество элементов для набора n: '))
m = int(input('Введите количество элементов для набора m: '))
set_n = [randint(1, n) for i in range(n)]
set_m = [randint(1, m) for i in range(n)]
print(set_m,set_n)
set_join = set(set_n) & set(set_m)
print(set_join)