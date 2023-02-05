# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# Пример:
#
# Ввод:
# ноутбук
# Вывод:
# 12


scrable_1 = 'A ,E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т' .split(', ')
scrable_2 = 'D, G, Д, К, Л, М, П, У' .split(', ')
scrable_3 = 'B, C, M, P, Б, Г, Ё, Ь, Я' .split(', ')
scrable_4 = 'F, H, V, W, Y, Й, Ы' .split(', ')
scrable_5 = 'K, Ж, З, Х, Ц, Ч' .split(', ')
scrable_8 = 'J, X, Ш, Э, Ю' .split(', ')
scrable_10 = 'Ф, Щ, Ъ, Q, Z' .split(', ')
dic_1 = (dict.fromkeys(scrable_1, 1))
dic_2 = (dict.fromkeys(scrable_2, 2))
dic_3 = (dict.fromkeys(scrable_3, 3))
dic_4 = (dict.fromkeys(scrable_4, 4))
dic_5 = (dict.fromkeys(scrable_5, 5))
dic_8 = (dict.fromkeys(scrable_8, 8))
dic_10 = (dict.fromkeys(scrable_10, 10))
dic_1.update(dic_2)
dic_1.update(dic_3)
dic_1.update(dic_4)
dic_1.update(dic_5)
dic_1.update(dic_8)
dic_1.update(dic_10)

word = str.upper(input('Введите слово: '))
list_W = []
for i in range(len(word)):
    value = dic_1.get(word[i])
    list_W.append(value)
print ("Очки: ",sum(list_W))


