colors = {'red', 'green', 'blue'}
print(colors)

colors.add('red')
print(colors)

colors.add('gray')
print(colors)

colors.remove('red') # удаляет элемент
print(colors)

colors.discard('red') # проверяет наличие во множестве элемента
print(colors)

colors.clear()
print(colors)

q = set() # создание пустого множества