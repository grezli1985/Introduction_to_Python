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
        print()
        if select_ == '1':
            print(reading())
        elif select_ == '2':
            print(record())
        elif select_ == '3':
            print()
            print('Выберете пункт меню: ')
            print('1. Экспорт книга txt')
            print('2. Экспорт книга csv')
            num3 = input('Ввод: ')
            if num3 == '1':
                print(export_txt())
            elif num3 == '2':
                print(export_csv())
        elif select_ == '4':
            print()
            print('Выберете пункт меню: ')
            print('1. Импорт книга txt')
            print('2. Импорт книга csv')
            num4 = input('Ввод: ')
            if num4 == '1':
                print(import_data_txt())
            elif num4 == '2':
                print(import_data_csv())
        elif select_ == '5':
            print('До встречи!')
            break
        else:
            print('Неверный ввод. повторите попытку')
         
