def book():
    with open(path, 'r', encoding='utf-8') as data:
        for line in data.readlines():
            print(line)


def book_1():
    with open(path1, 'r', encoding='utf-8') as data:
        for line in data.readlines():
            print(line)


def book_2():
    data_for_input = input_data()
    with open(path, 'a+', encoding='utf-8') as data:
        for line in data_for_input:
            data.write(f'{line}\n')
        data.write(f'\n')
    
        
def book_3():
    data_for_input = input_data()
    with open(path1, 'a+', encoding='utf-8') as data:
        for line in data_for_input:
            data.write(' ' + ''.join(line.split()))
        data.write(f'\n') 


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    notes = input("Введите примечание: ")
    return [last_name, first_name, phone_number, notes]


def export_txt(file_user):
    with open(path, 'a', encoding='UTF8') as file:
        for line in file_user:
            file.write(line)

        
def export_csv(file_user):
    with open(path1, 'a', encoding='UTF8') as file:
        for line in file_user:
            file.write(line)
    

def import_book():
    with open(file_user_1, 'a', encoding='utf-8') as file:
        for line in path01:
            file.write(line)
            

def import_book_1():
    with open(file_user_1, 'a', encoding='utf-8') as file:
        for line in path10:
            file.write(line)


path = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/book.txt'
path01 = open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/book.txt', 'r', encoding='utf-8')
path1 = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/book_1.csv'
path10 = open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_7/home_work_7/book_1.csv', 'r', encoding='utf-8')
file_user_1 = '/Users/sergey/учеба/Знакомство_с_языком_Python/file_user.txt'
file_user = open('/Users/sergey/учеба/Знакомство_с_языком_Python/file_user.txt', 'r', encoding='utf-8')
