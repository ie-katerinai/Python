# Напишите функцию, которое принимает одно число и проверяет, является ли оно простым



def natural_num(num):
    for i in range(2, num//10+1):
        if num % i == 0:
            return True
            # print(f'Введенное число {num} не является простым')
    return False
        # else:
        #     print(f'Введенное число {num} является простым')


number = int(input('Введите число: '))
print(natural_num(number))