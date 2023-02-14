def list_init(el_count: int) -> list:
    result_list = []
    for i in range(el_count):
        num = int(input('num: '))
        result_list.append(num)
    return result_list

n = int(input('n --> '))
our_list = list_init(n)
print(our_list)

count = 0
for i in range(1,(len(our_list)-1)):
    if our_list[i-1] < our_list[i] > our_list[i+1]:
        count+=1
print(count)