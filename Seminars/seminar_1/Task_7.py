# 7. Дано натуральное число.
# Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# **Input:**

# 2016

# **Output:**

# YES

year = int(input("Введите год: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("Yes")
else:
    print("No")

"""
   year = int(input('--> '))
result = 'NO'
if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    result = 'YES'

print(result)
"""
# Решение через тернарный оператор
# year = int(input("Введите год: "))
# result = 'Yes' if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else 'No'
# print(result)

# year = int(input("Введите год: "))
# print('Yes' if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else 'No')

# Моржовый оператор (:= похож на моржа)

# print('Yes' if(year:=int(input('--->')))%400 == 0 else 'No')
"""
while (num:=int(input('-->'))) == 0:
    print('Введи не ноль!')
"""   