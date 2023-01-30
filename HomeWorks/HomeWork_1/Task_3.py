# Задача 3: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

numberTiket = int(input('Введите номер билета: '))
if (numberTiket >= 100000 and numberTiket <1000000):
    firstNumbers = numberTiket//1000
    secondNumbers = numberTiket % 1000
    sum1 = 0
    while firstNumbers > 0:
        x1 = firstNumbers % 10
        sum1 += x1
        firstNumbers = firstNumbers//10
    print('Сумма первых трех цифр равна: ',sum1)
    sum2 = 0
    while secondNumbers > 0:
        x2 = secondNumbers % 10
        sum2 += x2
        secondNumbers = secondNumbers//10
    print('Сумма вторых трех цифр равна: ',sum2)
    if sum1 == sum2: print('Ваш билет счастливый!')
    else: print('Ваш билет обычный.')
else: print('Вы ввели неверное количество цифр')