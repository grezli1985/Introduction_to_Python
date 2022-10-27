
from datetime import datetime as dt

def logger(text='Действие', value=None, name = 'log.csv'):
    if value is None:
        value = ''
    time = dt.now().strftime('%H:%M')
    with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/lectures/Lesson_7/log.csv', 'a') as file:
        file.write(f'{time}; {text}; {value}; \n')


