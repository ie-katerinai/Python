# 1. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался.
# 'Hello, World!'
# H: 1
# e: 1
# l: 3
# o: 2
# W: 1
# ' ': 1
# ,: 1
# r: 1
# d: 1
# !: 1



# our_list = 'Hello, world!'
# our_dict = {}
# count_list = set(our_list)
# for letter in count_list:
#     count = 0
#     for letter_in_word in our_list:
#         if letter == letter_in_word:
#             count+=1
#     our_dict[letter] = count
# print(our_dict)


# our_string = 'Hello, world!'
# our_dict = {}
# count_list = set(our_string)
# for letter in count_list:
#     count_letter = 0
#     for letter_in_word in our_string:
#         if letter == letter_in_word:
#             count_letter+=1
#     our_dict[letter] = count_letter
# print(our_dict)


# start_list = input('Введите любую строку: ')
# count = 0
# start_set = set(start_list)
# uniq_list = list(start_set)
# new_dict = dict()
# for i in range(len(uniq_list)):
#     for j in range(len(start_list)):
#         if uniq_list[i] == start_list[j]:
#             count += 1
#     new_dict[uniq_list[i]] = count
#     count = 0
# print(new_dict)


text = input('Введите текст: ')
d = {}
for i in text:
    d[i] = d.get(i,0)+1
print(d)