# 2. Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# [4, 2, 2, 1, 5, 5]
# def swapmark(n):
#     if n == 5:
#         return 1
#     elif n == 4:
#         return 2
#     else:
#         return n

# marks = [4, 2, 2, 1, 5, 5]
# for i in range(len(marks)):
#     marks[i] = swapmark(marks[i])
# print(marks)

def replace_marks(marks_list: list) -> list:
    for i in range(len(marks_list)):
        if (marks_list[i] == 5) or (marks_list[i] == 4):
            marks_list = 2
    return marks_list

marks= [4, 2, 2, 1, 5, 5]
print(replace_marks(marks))