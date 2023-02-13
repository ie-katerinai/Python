# Lано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.

def reverse_nums(n):
    if n ==0:
        return ''
    k = input('--->')
    return reverse_nums(n-1) + k 

n = int(input())
print(reverse_nums(n))