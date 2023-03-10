# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке.
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод:
# Парам пам-пам

poem = str(input('Введите стихортворение: '))
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']
poem = poem.lower()
print(poem)
phrase = poem.split()
print(phrase)
if len(phrase) < 2:
    print('В стихотворении всего ода фраза')
else:
    count_list = []
    for i in phrase:
        count = 0
        for x in i:
            if x in vowels: count +=1
        count_list.append(count)
    print(count_list)
if sum(count_list) / len(count_list) == count_list[0]:
    print('Парам пам-пам')
else: print('Пам парам')