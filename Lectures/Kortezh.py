t  = ()

print(type(t))

t = (1, 2, 3, )
print(type(t))

v = [1, 8, 5]
print(v)
print(type(v))

v = tuple(v) # преобразование списка в кортеж
print(v)
print(type(v))
# распаковка кортежа
a, b, c = v
print(a, b, c)

t = (1, 2, 3, 4, 5,)
print(t[1]) # 2
for i in t:
    print(i)

for i in range(len(t)):
    print(t[i])

