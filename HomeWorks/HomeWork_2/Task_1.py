# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0


import random
n = int(input('Введите количество монеток: '))
if n > 0:
    my_list = []
    i = 0
    while i < n:
        my_list.append(int(input('Введите 0 - решка или 1 - герб: ')))
        i += 1
    print(my_list)
    # while i < n:
    #     my_list.append(random.randint(0, 1))
    #     i += 1
    # print(my_list)
    tails = 0
    heands = 0
    for elem in my_list:
        if elem == 0:
            tails += 1
        else: heands += 1
    print('Выпало',tails, ' момнеты решкой вврх и',heands,'-  гербом вверх')
    if tails > heands: print('Нужно перевернуть', heands,'монеты с гербом')
    else: print('Нужно перевернуть', tails,'монеты с решкой')
else: print('Вы ввели некорректное количесвто монет')