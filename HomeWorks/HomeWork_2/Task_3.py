# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('Введите число: '))
my_list = []
for i in range(n):
    s = 2**i
    
    if s <= n:
        my_list.append(s)
    else: break
print(my_list)