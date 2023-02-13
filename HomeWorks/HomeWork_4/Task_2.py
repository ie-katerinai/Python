# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# обирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4
# 1 2 3 4
# 9

def maximum_berries(berries_list):
    count_berries = []
    summa_berries = 0
    for i in (1,(len(berries_list) - 2)):
        summa_berries = berries_list[i-1] + berries_list[i] + berries_list[i+1]
        count_berries.append(summa_berries)
    berries_1 = berries_list[0] + berries_list[len(berries_list) - 2] + berries_list[len(berries_list) - 1] 
    count_berries.append(berries_1)
    berries_2 = berries_list[0] + berries_list[1] + berries_list[len(berries_list) - 1]
    count_berries.append(berries_2)
    maximum_count = max(count_berries)
    return maximum_count

n = int(input('Введите количество кустов: '))
new_list = []
for i in range(n):
    new_list.append(int(input('-->')))
print(new_list)

print(maximum_berries(new_list))