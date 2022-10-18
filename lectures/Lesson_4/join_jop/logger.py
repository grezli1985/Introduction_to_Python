from datetime import datetime as dt
from time import time

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/lectures/Lesson_4/join_jop/log.csv', 'a') as file:
        file.write('{};temperature;{}\n'
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/lectures/Lesson_4/join_jop/log.csv', 'a') as file:
        file.write('{};pressure;{}\n'
                    .format(time, data))


def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/lectures/Lesson_4/join_jop/log.csv', 'a') as file:
        file.write('{};wind_speed;{}\n'
                    .format(time, data))