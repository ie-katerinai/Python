result = [1, 5, 7, 3, 7]
new_list_1 = list(map(lambda num: num*num, result))
#            что сделать   где взять       при каком условии
new_list_2 = [item*item for item in result if item > 4]
print(new_list_2)