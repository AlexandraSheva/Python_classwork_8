# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (choice != 7):
        if choice == 1: # 1. Отобразить весь справочник
            print_result(phone_book) 
        elif choice == 2: # 2. Найти абонента по фамилии
            name = get_search_name()
            print_result(find_by_name(phone_book, name)) 
        elif choice == 3: # 3. Найти абонента по номеру телефона
            number = get_search_number() 
            print_result(find_by_number(phone_book, number))
        elif choice == 4: # 4. Добавить абонента в справочник
            user_data = get_new_user() 
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5: # 5. Удалить абонента из справочника
            name = get_search_name() 
            print_result(find_by_name(phone_book, name)) 
            delete_user(phone_book, find_by_name(phone_book, name))
            write_csv('phonebook.csv', phone_book)
        elif choice == 6:  # Сохранить справочник в текстовом формате
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def print_result(data: list):
    s = ' '
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for v in fields:
        s += v.center(20)
    print(f'{s}')

    for i in range(len(data)):
            s = ' '
            for v in data[i].values():
                s += v.center(20)
            print(f'{s}')

def get_search_name():
    first_name = input("Введите фамилию: ")
    return first_name
        
def find_by_name(data: list, first_name):
    search_by_name = []
    for line in data:
        index = line['Фамилия'].lower()
        if index.find(first_name.lower()) == 0:
            search_by_name.append(dict(line))
    return search_by_name

def get_search_number():
    name = input("Введите номер: ")
    return name

def find_by_number(data: list, number):
    search_by_number = []
    for line in data:
        index = line['Телефон']
        if  index.find(number) == 0:
            search_by_number.append(dict(line))
    return search_by_number

def get_new_user():
    line = {}
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for v in fields:
        data = input(f'Введите {v}: ')
        line[v] = data
    return line

def add_user(data: list, user_data: dict):
    data.append(dict(user_data))
    return data

def delete_user(data: list, name):
    tmp = []
    for record in name:      
        if record in data:
            print('Запись для удаления:')
            tmp.append(record)
            print_result(tmp)
            confirmation = input('Чтобы удалить, введите ""да"",\n'
                                 'чтобы отменить удаление, введите ""нет"":')
            if confirmation == 'да':
                data.remove(record)
            elif confirmation == 'нет':
                return
            tmp.clear()

def get_file_name():
    name = input("Введите имя файла: ")
    return name

def write_txt(filename: str, data: list):
    txt_filename = filename + '.txt'
    print(txt_filename)
    with open(txt_filename, 'w', encoding='utf-8') as fout:
        s = ' '
        fields = ["Фамилия", "Имя", "Телефон", "Описание"]
        for v in fields:
            s += v.center(20) + " "
        fout.write(f'{s}\n')    

        for i in range(len(data)):
            s = ' '
            for v in data[i].values():
                s += v.center(20) + " "
            fout.write(f'{s}\n')
        fout.write(f'Cохранили {len(data)} записей')


work_with_phonebook()