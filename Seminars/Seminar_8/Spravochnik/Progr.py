# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1. Вывод всех контактов
# 2. Поиск контакта
# 3. Добавить контакт (сразу сохрорнять в файл)
# 4. Выход по требованию пользователя


def all_contacts():
    the_way = 'Seminars/Seminar_8/Spravochnik/file.txt'
    with open(the_way, 'r', encoding='utf-8') as data:
        for line in data:
            print(line)


def find_contact(name):
    with open('Seminars/Seminar_8/Spravochnik/file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if name in line:
                print(line)


def add_contact(name):
    with open('Seminars/Seminar_8/Spravochnik/file.txt', 'a', encoding='utf-8') as data:
        data.write('\n')
        data.write(name)


def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input('Введите искомое имя: ')
        find_contact(name)
    elif numb == 3:
        data = str(input('Введите новый контакт: '))
        add_contact(data)

while True:
    numb = int(input('Введите 1 - для печати всего справочника; 2 - для поиска контакта; '
                      '3 - для записи контакта; 4 - для выхода из справочника: '))
    if numb == 4: 
        break
    main_menu(numb)
