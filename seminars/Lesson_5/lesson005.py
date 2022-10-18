# def f(a=None):
#     if a is None:
#         a = []
#     a.append(len(a))
#     return a


# l = [0, 1, 2]

# print(f())        # [0]
# print(f())        # [0]
# print(f())        # [0]


# lambda - 

# a = [(1, 2), (3, 3), (-2, 1), (1, 5), (6, -5)]

# print(max(a, key=lambda x: x[1]))      # или x: len(x)))
# print(min(a, key=lambda x: x[1]))




# a = ['1', '2', '10', '9']

# print(max(a))     # [9]

# a = ['1', '2', '10', '9']

# print(max(a, key=int))     # [10]








# from random import random, randint, randrange

# print(random() * 100)         # от 0 до 100
# print(50 + random() * 50)     # от 50 до 100
# print(randint(50, 100))       # от 50 до 100
# print(randrange(50, 101))     # от 50 до 100








# a = []
# for n in range(11):
#     a.append(n * n)

# print(a)


# b = [n * n for n in range(11)]

# print(b)


# b = [n / 10 for n in range(0, 51, 5)]

# print(b)




# a = []
# for n in range(11):
#     if n % 2 == 0:
#         a.append(n * n)
#     else:
#         a.append(n * n * n)

# print(a)

# b = [n * n if n % 2 == 0 else n**3 for n in range(11)]

# print(b)                     # [0, 1, 4, 27, 16, 125, 36, 343, 64, 729, 100]



# a = []
# for n in range(11):
#     if n % 5 != 0:
#         if n % 2 == 0:
#             a.append(n * n)
#         else:
#             a.append(n * n * n)

# print(a)

# b = [n * n if n % 2 == 0 else n**3 for n in range(11) if n % 5 != 0]

# print(b)                     # [1, 4, 27, 16, 36, 343, 64, 729]









# map




# a = [1, 2, 3, 4, 5]

# itog = map(lambda x: x**2, a)

# print(itog)                     # <map object at 0x10ee5f700>

# itog = list(map(lambda x: x**2, a))           # если обвернуть в list

# print(itog)                     # [1, 4, 9, 16, 25]  - список

# itog = set(map(lambda x: x**2, a))           # если обвернуть в set

# print(itog)                     # {1, 4, 9, 16, 25}

# itog = tuple(map(lambda x: x**2, a))           # если обвернуть в tuple

# print(itog)                     # (1, 4, 9, 16, 25)   - картеж


# filter

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter_itog = filter(lambda x: x % 2 == 0, a)

# print(filter_itog)                # <filter object at 0x10ca9b790>

# filter_itog = list(filter(lambda x: x % 2 == 0, a))     # если обвернуть в list

# print(filter_itog)                # [2, 4, 6, 8, 10]

# filter_itog = list(filter(lambda x: x % 5 != 0, a))     

# print(filter_itog)                # [1, 2, 3, 4, 6, 7, 8, 9]

# filter_itog = list(filter(lambda x: x % 5 != 0 or x == 10, a))     

# print(filter_itog)                # [1, 2, 3, 4, 6, 7, 8, 9, 10]




# zip


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 'abcdefghi'
# c = (False, True, None)

# for item in zip(a, b, c):
#     print(item)                         # (1, 'a', False)
#                                         # (2, 'b', True)
#                                         # (3, 'c', None)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 'abcdefghi'
# c = (False, True, None)

# for item_a, item_b, item_c in zip(a, b, c):
#     print(item_a)                           # 1
#                                             # a
#                                             # False
#     print(item_b)                           # 2
#                                             # b
#                                             # True
#     print(item_c)                           # 3
#                                             # c
#                                             # None
    
    



# a = 1, 2, 3

# print(a)         # (1, 2, 3) - получится кортеж



# a, b, c = 1, 2, 3

# print(a)          # 1
# print(b)          # 2
# print(c)          # 3


# a, b = 1, 2, 3

# print(a)          # 
# print(b)          #  too many values to unpack (expected 2)
# print(c)          #

# a, b, c, d = 1, 2, 3

# print(a)          # 
# print(b)          #  not enough values to unpack (expected 4, got 3)
# print(c)          #






# enumerate





# b = 'abc'

# for item in b:
#     print(item)         # обращаюсь на примую к элементам, но не вижу индекса   
#                         # a
#                         # b
#                         # c 

# for i in range(len(b)): # 
#     print(b[i])         # обращаюсь по индексу, что бы увидеть элементы

# for i, item in enumerate(b):
#     print(i, item)       # одновременно получить доступ как к индексу, так и к элементу
#                         # 0 a
#                         # 1 b
                        # 2 c









'''
1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
Найдите это число.
    
    1 2 3 4 6 7 8 9

'''

# with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/1_file", "w", encoding="UTF-8") as data_file:
#     data_file.write('1 2 3 4 5 7 8 9')

# with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/1_file", "r", encoding="UTF-8") as data_file:
#     string = data_file.readline()
# string = list(map(int, string.split()))
# a = 0
# for i in range(1, len(string)):
#     if string[i] - 1 != string[i - 1]:
#         a = i

# print(string[a] - 1)








# a = [1, 2, 3, 4, 5, 6, 7, 9]

# for i1, i2 in zip(a, range(a[0], a[0] + len(a))):
#     if i1 != i2:
#         print(i2)
#         break





'''
2. Напишите программу, удаляющую из текста все слова, содержащие "абв". <- filter
'''

# with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/2_file", "w", encoding="UTF-8") as data_file2:
#     data_file2.write('1 abc 2 3 4 6 abc 5 7 8 abc9')
# with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/2_file", "r", encoding="UTF-8") as data_file2:
#     string = data_file2.readline().split()
# result = list(filter(lambda x: 'abc' not in x, string))
# print(string)
# print(result)





# with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/21_file", "w", encoding="UTF-8") as file_:
#     file_.write('1 abc 2 3 4 6 abc 5 7 8 abc9 10 11 abc 12 abc')
# with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/21_file', 'r', encoding='UTF-8') as file_:
#     str_ = file_.readline()

# list_ = list(map(str, str_.split()))

# def true_or_not(str_):
#     return 'adc' in str_

# result = list(filter(true_or_not, list_))
# print(result)        #???????



'''
3. Дан список чисел. 
Создайте список, в который попадают числа,
описываемые возрастающую последовательность.
Порядок элементов менять нельзя.

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

'''

# with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/3_file", "w", encoding="UTF-8") as data_file3:
#     data_file3.write('1, 5, 2, 3, 4, 6, 1, 7')
# with open("/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/seminars/Lesson_5/3_file", "r", encoding="UTF-8") as data_file3:
#     string = data_file3.readline().split()

# for i







