# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4

def summa(numb, count):
    if numb == 0:
        return count
    else: count = 1 + summa(numb - 1, count)
    return count

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
count = 0
s = summa(a, count) + summa(b, count)
print(s)



        