# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# Пример:
# 4 4 -> 2 2
# 5 6 -> 2 3

s = int(input('Введите значение суммы чисел: '))
p = int(input('Введите значение произведения чисел: '))
x = 1
y = 1
while x < 1000:
    if((s == x + y) and (p == x * y)):
        break
    else:
        x += 1
        y = 1
        while x < 1000:
            if((s == x + y) and (p == x * y)):
                break
            else: y += 1
print(x, y)
