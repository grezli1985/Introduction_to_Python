''' Задание 1
        Напишите программу, которая принимает на вход вещественное число и 
        показывает сумму его цифр.

            Пример:

                6782 -> 23
                0,56 -> 11      '''

# n = input("Введите число: ")
# sum_ = 0

# for i in n:
#     if i.isdigit():
#         sum_ += int(i)
# print(f'сумма цифр: {sum_}')



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



''' Задание 3
        Задайте список из n чисел последовательности (1+1/n)^n и 
        выведите на экран их сумму, округлённую до трёх знаков после точки.

            Пример:

                Для n = 6 -> 14.072     '''


# n = int(input('Введите число: '))
# list = []
# for i in range (1, n + 1):
#     list.append((1 + (1 / i)) ** i)
    
# print(round(sum((list)), 3))



''' Задание 4
        Задайте список из N элементов, заполненных числами из промежутка [-N, N].
        Найдите произведение элементов на позициях a и b.
        Значения N, a и b вводит пользователь с клавиатуры.     '''

# n = int(input('Введите число, какого размера будет список N: '))


# list_cccp = list(range(-n, n + 1))
# print(list_cccp)

# # position = list(range(0, n + (n + 1)))
# # print(position) 

# a = int(input('Введите число, позиции a: '))
# b = int(input('Введите число, позиции b: '))

# piece = (list_cccp[a - 1]) * (list_cccp[b - 1])
# print()
# print(f'{list_cccp[a]} * {list_cccp[b]} = {piece}')






''' Задание 5
        Реализуйте алгоритм перемешивания списка.   '''

# ------------< Решения 1 >-------------

# import random
# lst = [random.randint(0,10) for i in range (random.randint(5,20))]
# print(f"исходный список:\n {lst}")
# random.shuffle(lst)
# print(f"список после перемешивания:\n{lst}")


# ------------< Решения 2 >-------------


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