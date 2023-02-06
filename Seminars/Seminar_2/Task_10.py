# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. 
# Если А не является числом Фибоначчи, выведите число -1.
# 1 1 2 3 5 8
# 5 -> 5
# 8 -> 6
# 7 -> -1
n = int(input('n: '))
f_1 = 1
f_2 = 1
count = 2

while f_2 < n:
    count += 1
    f_1, f_2 = f_2, f_1 + f_2
    
if f_2 == n:
    print(count)
else:
    print(-1)
#   замена с 17 строки  
# print(count if f_2 == n else -1)

'''
Так делать не нужно - дурной тон
n = int(input('n: '))
f_1 = 1
f_2 = 1
count = 2

while f_2 <= n:
    if f_2 == n:
        print(count)
        break // continue
    count += 1
    f_1, f_2 = f_2, f_1 + f_2
else:
    print(-1)
'''