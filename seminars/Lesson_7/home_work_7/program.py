from controller import *

def start():
    while True:
        print()
        print('-----Телефонная книга приветствует тебя!!!-----')
        print('Выберете пункт меню: ')
        print('1. Просмотр записей\n'
        '2. Добавление записи\n'
        '3. Экспорт\n'
        '4. Импорт\n'
        '5. Выход из программы')
        select_ = input('выберете действия: ')
        if select_ == '1':
            print()
            print('Выберете пункт меню: ')
            print('1. Книга txt')
            print('2. Книга csv')
            num = input('Ввод: ')
            if num == '1':
                print(f'{book()}\n')
            elif num == '2':
                print(book_1())
        elif select_ == '2':
            print()
            print('Выберете пункт меню: ')
            print('1. Сохранить в книга txt')
            print('2. Сохранить в книга csv')
            num2 = input('Ввод: ')
            if num2 == '1':
                print(book_2())
            elif num2 == '2':
                print(book_3())
        elif select_ == '3':
            print()
            print('Выберете пункт меню: ')
            print('1. Экспорт книга txt')
            print('2. Экспорт книга csv')
            num3 = input('Ввод: ')
            if num3 == '1':
                print(export_txt(file_user))
            elif num3 == '2':
                print(export_csv(file_user))
        elif select_ == '4':
            print()
            print('Выберете пункт меню: ')
            print('1. Импорт книга txt')
            print('2. Импорт книга csv')
            num4 = input('Ввод: ')
            if num4 == '1':
                print(import_book())
            elif num4 == '2':
                print(import_book_1())
        elif select_ == '5':
            print('До встречи')
            return False
        else:
            print('Неверный ввод. повторите попытку')
            return