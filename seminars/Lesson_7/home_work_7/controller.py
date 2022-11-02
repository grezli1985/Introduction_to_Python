
def reading():
    with open(path, 'r', encoding='utf-8') as data:
        for line in data.readlines():
            print(f'\n{line}')


def record():
    data_for_input = input_data()
    with open(path, 'a+', encoding='utf-8') as data:
        for line in data_for_input:
            data.write(' '.join(line.split()) + ' ')
        data.write(f'\n')
    print()
    print('Готово!\n Данные загружены в файл "book.txt"')

       
def export_txt():
    with open(path,"r", encoding='UTF-8') as file:
        data = file.read()
    export_file = open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/export_result.txt", "w", encoding='utf-8')
    export_file.write(data)        
    export_file.close()
    print('Готово! Данные выгружены в файл "export_result"')


def export_csv():
    with open(path,"r", encoding='UTF-8') as file:
        data = file.read()
    export_file = open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/export_result.csv", "w", encoding='utf-8')
    export_file.write(data)        
    export_file.close()
    print('Готово! Данные выгружены в файл "export_result"')


def import_data_txt():
    with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/export_result.txt", "r", encoding='UTF-8') as file:
        data = file.read()
    book = open(path, "a")
    book.write(f'\n')
    book.write(data)
    book.close()   
    print('Готово!\n Данные загружены в файл "book.txt"')


def import_data_csv():
    with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/export_result.csv", "r", encoding='UTF-8') as file:
        data = file.read()
    book = open(path, "a")
    book.write(f'\n')
    book.write(data)
    book.close()   
    print('Готово!\n Данные загружены в файл "book.txt"')


def input_data():
    info = []
    last_name = input("Введите фамилию: ")
    info.append(last_name)
    first_name = input("Введите имя: ")
    info.append(first_name)
    Patronymic = input("Введите Отчесто: ")
    info.append(Patronymic)
    phone_number = input("Введите телефон: ")
    info.append(phone_number)
    notes = input("Введите примечание: ")
    info.append(notes)
    return  info


path = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/book.txt'
path1 = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/book_1.csv'
