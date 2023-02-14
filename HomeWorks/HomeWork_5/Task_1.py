# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def raise_to_degree(number, degree):
    if degree == 1:
        return number
    return (number * raise_to_degree(number, degree - 1))

a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
print(raise_to_degree(a, b))
