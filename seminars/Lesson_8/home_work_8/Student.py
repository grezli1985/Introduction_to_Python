path = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_8/home_work_8/data_users.csv'
path1 = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_8/home_work_8/data_users.txt'

def schedules():
    with open(path1, 'r', encoding='utf-8') as data:
        line = data.readlines()
        for i in line:
            print(i)


def house_work():
    with open(path, 'r', encoding='utf-8') as data:
        line = data.readlines()
        for i in line:
            print(i)
    




