# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

def set_value(number):
    new_list = []
    for i in range(number):
        new_list.append(int(input('-->')))
    return new_list 

def equal_lists(set_1, set_2):
    new_list = []
    for i in set_1:
        for j in set_2:
            if i == j:
                new_list.append(i)
            #print(new_list)
    return new_list


n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
list_1 = set(set_value(n))
print(list_1)
list_2 = set(set_value(m))

print(list_2)
final_list = equal_lists(list_1, list_2)
print(final_list)

