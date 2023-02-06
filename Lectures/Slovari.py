d = {}
d = dict()

d['q'] = 'qwerty'
print(d)

d['w'] = 'werty'
print(d)
print(d['q'])



dictionary = {}
dictionary = {'up': '|', 'left': '-', 'down': '/', 'right': '+'}
print(dictionary)
print(dictionary['left'])
dictionary[12] = 324425
print(dictionary)
del dictionary['left'] # удаление ключа left

for item in dictionary: # печать только списка ключей
    print(item)

for item in dictionary: # печать ключа и значения через :
    print('{}: {}'.format(item, dictionary[item]))

print(dictionary.items())
for(k, v) in dictionary.items():
    print(k, v)