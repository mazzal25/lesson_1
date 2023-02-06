from random import randint

len_qtt = int(input('Введите количество элементов в массиве: '))
res = []
for _ in range(len_qtt):
    value = randint(1, len_qtt)
    res.append(value)
print(res)
x = int(input('Введите число для сравнения: '))
res.append(x)
res_set = set(res)
res_list = list(res_set)
res_list.sort()
print(res_list)
coming_num = []
not_in_list = []
for i in range(len(res_list)):
    if res_list[i] == x and x != res_list.pop():

        a = res_list[i + 1] - x
        b = (res_list[i - 1] - x) * -1
        if a < b:
            print(res_list[i + 1])
        elif a == b:
            print(res_list[i - 1], res_list[i + 1])
        else:
            print(res_list[i - 1])

    elif x == res_list.pop():
        print(res_list[i - 1])
    elif x == res_list[0]:
        print(res_list[0])