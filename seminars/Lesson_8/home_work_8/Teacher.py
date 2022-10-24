
path2 = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_8/home_work_8/data_teacher.txt'

def student_list():
    with open(path2, 'r', encoding='utf-8') as data:
        line = data.readlines()
        for i in line:
            print(i)


def add_student_list():
    with open(path2, "r", encoding="utf-8") as file:
        lines = file.readlines()

    data_for_file_t = str(input('Укажите ФИО: '))
    with open(path2, "a", encoding='UTF-8') as file:
        file.write(f'\n{data_for_file_t}')