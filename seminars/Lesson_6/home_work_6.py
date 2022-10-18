'''
Задача: предложить улучшения кода для четырёх уже решённых задач 
из семинаров №№2 - 5 с помощью использования: 
"лямбд, filter, map, zip, enumerate, list comprehension"
    - В решении указывайте как старый вариант (до улучшения), так и новый.
    - Обязательно, комментариями в коде, указывайте условие задачи.

'''


'''
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''


# path = "/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_6/21_file"
# with open(path, 'w', encoding="UTF-8") as data:
#     data.write('1 abc 2 3 4 6 abc 5 7 8 abc9')

# with open(path, "r", encoding="UTF-8") as data:
#     string = data.readline().split()
# result = list(filter(lambda x: 'abc' not in x, string))
# print(string)
# print(result)


# txt = '1 abc 2 3 4 6 abc 5 7 8 abc9'
# find_txt = "abc"
# print([i for i in txt.split() if find_txt not in i])



''' Задача 1
    Задайте список из нескольких чисел. Напишите программу,
    которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 '''

# a = [2, 3, 5, 9, 3]

# # sum_ = 0;
# # for i in range(len(a)):
# #     if i % 2 == 1:
# #         sum_ += a[i];
# # print(sum_)




# print(sum(a[i] for i in range(1, len(a), 2)))





''' Задание 2
        Напишите программу, которая принимает на вход число N и 
        выдает набор произведений чисел от 1 до N.

            Пример:

                пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)     '''

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# n = int(input("Введите число: "))

# list = []
# for e in range(1, n + 1):
#     list.append(factorial(e))
# print(f'Произведения чисел от 1 до {n}: {list}')





# from math import factorial

# n = int(input('Введите число: '))
# f = lambda x: 1 if x == 0 else x * factorial(x - 1)
# lst = list(f(i) for i in range(1, n + 1))
# print(lst)








''' Задание 5
        Реализуйте алгоритм перемешивания списка.   '''



# import random
# lst = [random.randint(0,10) for i in range (random.randint(5,20))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")





# from random import randint
 
# n = int(input('Введите размер списка: '))
# a = []
# for i in range(n):
#     a.append(randint(1, 150))
# print(f'Первоначальный список {a}')
 
 
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
 
# print(f'Отсортированный список методом пузырька {a}')
