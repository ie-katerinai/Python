# Удаление последнего элемента списка
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0 - вывод элементе
a = list_1.pop
print(a)
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]

# Удаление конкретного элемента списка
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop(0)) # 12
print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11)) # 12
print(list_1) # [12, 7, 11, -1, 21, 0]