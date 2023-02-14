# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def summa(numb_1, numb_2):
    summ = 1
    if numb_1 == 0 and numb_2 == 0:
        return 0
    elif numb_2 == 0 and numb_1 != 0:
            numb_1 -= 1
            summ +=1
            return summ
    elif numb_1 == 0 and numb_2 != 0:
        numb_2 -= 1
        summ +=1
        return summ
    else: summa(numb_1 - 1, numb_2) 

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(summa(a, b))



        