# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# Пример:
#
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
len_qtt = int(input('Введите количество элементов в массиве: '))
res = []
for _ in range(len_qtt):
    value = randint(1,len_qtt)
    res.append(value)
print(res)
x = int(input('Введите число для сравнения: '))
res.append(x)
res.sort()
res_set = set(res)
res_list = list(res_set)
print(res_list)
coming_num =[]
not_in_list =[]
for i in range(len(res_list)):
    if res_list[i] == x: # and res_list[i] != max(res_list) or res_list[i] != min(res_list) :
        coming_num.append(res_list[i+1])
        coming_num.append(res_list[i-1])
        print(coming_num)
    # elif x == res_list.pop():
    #     not_in_list.append(max(res_list))
    # else:
    #     not_in_list.append(min(res_list))

# не могу предумать условие на случай когра число оказывается посленим в списке или первым.
# если любое число между первым и последним, то работает всё..