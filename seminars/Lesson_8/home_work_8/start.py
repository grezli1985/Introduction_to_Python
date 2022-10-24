from Student import *
from Teacher import *

def start():
    while True:
        print()
        print('-----Вас приветствует интерактивный помощник!-----')
        print()
        print('Для продолжения выберите действия\n1. Ввести логин\n9. Выход')
        print()
        select_ = None
        select_ = input('выберете действия: ')
        if select_ == '1':
            print()
            log_ = input('Введите ваш логин: ')
            print()
            print('Выберете пункт меню: ')
            print('1. Студент\n2. Преподаватель')
            num1 = input('Ввод: ')
            if num1 == '1':
                print()
                print('Выберете пункт меню: ')
                print('1. Посмотреть расписание')
                print('2. Посмотреть домашнее задание')
                num2 = input('Ввод: ')
                if num2 == '1':
                    print(schedules())
                if num2 == '2':
                    print(house_work())
                # return
            elif num1 == '2':
                print()
                print('Выберете пункт меню: ')
                print('1. Посмотреть список учеников')
                print('2. Добавить ученика')
                num3 = input('Ввод: ')
                if num3 == '1':
                    print(student_list())
                if num3 == '2':
                    print(add_student_list())
                else:
                    print('Неверный ввод. повторите попытку')
        elif select_ == 9:
            return False
        else:
            print('Неверный ввод. повторите попытку') 
            return

start()

from progress.bar import Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar, IncrementalBar, PixelBar
import time

def loading():
    bar = PixelBar('loading', max=100)
    for i in range(100):
        time.sleep(0.01)
        bar.next()
    bar.finish()

loading()