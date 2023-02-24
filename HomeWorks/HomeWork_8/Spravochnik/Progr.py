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
    with open('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            print(line)


def find_contact(name):
    with open('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if name in line:
                print(line)


def add_contact(name):
    with open('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'r', encoding='utf-8') as data:
        # data.write('\n')
        # data.write(name)
        current_file = data.read()
        current_file = current_file + '\n' + '\n'+ name
        # current_file.write('\n')
        # current_file.write(name)
    with open ('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'w', encoding='utf-8') as data:
        data.write(current_file)
    

def change_contact(old_name, new_name):
    with open ('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'r', encoding='utf-8') as data:
        current_file = data.read()
        new_file = current_file.replace(old_name, new_name)
    with open ('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'w', encoding='utf-8') as data:
        data.write(new_file)

def delete_contact(name):
    # with open('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'w', encoding='utf-8') as data:
    # lines = data.readlines()
    # pattern = re.compile(re.escape(name))
    # with open('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'w', encoding='utf-8') as data:
    #     for line in lines:
    #         result = pattern.search(line)
    #         if result is None:
    #             data.write(line)
    with open ('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'r', encoding='utf-8') as data:
        current_file = data.read()
        new_file = current_file.replace(old_name, new_name)
    with open ('/Users/evahome/Documents/Python/HomeWorks/HomeWork_8/Spravochnik/file.txt', 'w', encoding='utf-8') as data:
        data.write(new_file)


def main_menu(numb):
    if numb == 1:
        all_contacts()
    elif numb == 2:
        name = input('Введите искомое имя: ')
        find_contact(name)
    elif numb == 3:
        data = input('Введите новый контакт: ')
        add_contact(data)
    elif numb == 4:
        name_1 = input('Чей контакт вы хотите изменить? ')
        name_2 = input('Введите изменения: ')
        change_contact(name_1, name_2)
    # elif numb == 5:
    #     name = input('Чей контакт вы хотели бы удалить? ')
    #     delete_contact(name)

while True:
    numb = int(input('Введите 1 - для печати всего справочника; 2 - для поиска контакта; '
                      '3 - для записи контакта; 4 - для изменения данных; 5 - для удаления данных; 6 - для выхода из справочника: '))
    if numb == 6: 
        break
    main_menu(numb)
