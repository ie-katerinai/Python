# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3 2
# Вывод:
# 2

# Ввод:
# 1 1 2 3 1 2
# Вывод:
# 4

n = 4
list_ = [1, 2, 5, 7, 2, 6]
#           что сделать \ где взять \ при каком условии
new_list = [item for item in list_ if item > 3]
print(new_list)


len_list_1=int(input('Введите размер 1го набора элементов: '))
list_1=fill_list(len_list_1)
count=0
for i in range(len_list_1):
    for item in list_1[i+1:]:
        if item==list_1[i]:
            count+=1
print(count)
