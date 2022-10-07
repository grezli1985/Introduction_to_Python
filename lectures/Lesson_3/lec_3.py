#     Анонимные, lambda функции

#  Идея: часто описывать функцию некогда и незачем 

# def sum(x):
#     return x+10

# sum = lambda x: x+10

# def mult(x):
#     return x**2

# mult = lambda x: x**2

# sum(mult(2))


# def sum1(x):
#     return x+22

# sum1 = lambda x: x+22

# def mult2(x):
#     return x**3

# mult2 = lambda x: x**3

# sum1(mult2(2))


# def sum3(x):
#     return x+242

# sum3 = lambda x: x+242

# def mult4(x):
#     return x**5

# mult4 = lambda x: x**5

# sum3(mult2(2))


# def f(x):
#     x**2

# print(type(f))              #  <class 'function'>



# def f(x):
#     x**2

# g  = f
# print(f(1))                   # None
# print(g(1))                   # None




# def f(x):
#     return x**2

# g = f                              # кладем функцию f в переменую g

# print(type(f))                     # <class 'function'>
# print(type(g))                     # <class 'function'>

# print(f(4))                        # 16
# print(g(4))                        # 16




# def calc1(x):
#     return x + 10

# # print(calc1(10))                       # 20

# def calc2(x):
#     return x * 10

# # print(calc2(10))                       # 100

# def math(op, x):
#     print(op(x))

# math(calc2, 10)               # 100
# math(calc1, 10)               # 20



# # def sum(x, y):
# #     return x + y

# sum = lambda x, y: x + y

# # def mylt(x, y):
# #     return x * y

# mylt = lambda x, y: x * y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)

# # calc(sum, 4, 5)            # 9
# # calc(mylt, 4, 5)           # 20

# calc(lambda x, y: x * y, 4, 5)             #  20
# calc(lambda x, y: x + y, 4, 5)             #  9





# f(g(x))

# def h(f, g, x):
#     return f(g(x))h = lambda f, g, x: f(g(x))
# h(sum, mult, 5)

# h(lambda x: x+10, lambda x: x**2, 5)


'''     К чему это всё?
В файле хранятся числа, нужно выбрать четные и
составить список пар (число; квадрат числа).

    Пример:

        1 2 3 5 8 15 23 38

    Получить:

        [(2, 4), (8, 64), (38, 1444)] '''

# def f(x):
#     return x ** 2

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = [(i, fib(i)) for i in range(1, 10)]
# print(list)           

# list = [(i, f(i)) for i in range(1, 39) if i % 2 == 0]
# print(list) 






# with open('/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/lecturesc', 'a') as data:
   
# path = '/Users/sergey/учеба/Знакомство_с_языком_Python/Introduction_to_Python/lectures/Lesson_3/f.txt'
# f = open(path, 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e, e**2))
# print(out)






# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = list(select(lambda e: (e, e**2), res))
# print(res)








# List Comprehension


# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]



# list = []

# for i in range(1, 101):
#     # if i % 2 == 0:
#     list.append(i)

# print(list)

# list = [i for i in range(1, 21) ]
# print(list)      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# list = [i for i in range(1, 21) if i % 2 == 0]
# print(list)      # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
     
    # кортеж           
# list = [(i, i) for i in range(1, 21) if i % 2 == 0]
# print(list)        # [(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)]


    # с функцией

# def f(x):
#     return x ** 3

# list = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list)           # [8, 64, 216, 512, 1000, 1728, 2744, 4096, 5832, 8000]

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)           # [(2, 8), (4, 64), (6, 216), (8, 512), (10, 1000), (12, 1728), (14, 2744), (16, 4096), (18, 5832), (20, 8000)]






# Функция map


''' Функция map() применяет указанную функцию к
каждому элементу итерируемого объекта и
возвращает итератор с новыми объектами.

f(x) ⇒ x + 10
map(f, [ 1,  2,  3,  4,  5])
         ↓   ↓   ↓   ↓   ↓
       [ 11, 12, 13, 14, 15]
Нельзя пройтись дважды'''


# li = [x for x in range(1, 20)]

# li = list(map(lambda x:x+10, li))

# print(li)   # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]



# data = map(int,input().split())
# print(data)   # <map object at 0x10c6e6fb0>

# data = list(map(int,input().split()))
# print(data)   # ввод - 1 2 3 45 67   вывод - [1, 2, 3, 45, 67]


# data = map(int,input().split())

# for e in data:
#     print(e)       # ввод - 1 2 3   вывод - 1 2 3


# data = map(int,'1 2 3'.split())

# for e in data:
#     print(e)         # 1 2 3

# print('--')          # --

# for e in data:
#     print(e)         # по итератору можно пробежаться один раз, что бы работать с одними и теми же данными нужно принудительно сохранить 


# data = list(map(int,'1 2 3'.split()))

# for e in data:
#     print(e)           # 1 2 3

# print('--')            # ---

# for e in data:
#     print(e)           # 1 2 3







# def where(f, col):
#  return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# data = list(map(int, data))
# data = where(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)       # [(2, 4), (8, 64), (38, 1444)]





# Функция filter

''' Функция filter() применяет указанную функцию к
каждому элементу итерируемого объекта и
возвращает итератор с теми объектами, для
которых функция вернула True.

f(x) ⇒ x - чётное

filter(f, [ 1, 2, 3, 4,5])
                    ↓
             [ 2,    4 ]

Нельзя пройтись дважды '''




# data = [x for x in range(10)]

# res = list(filter(lambda x: not x%2, data))
# print(res)           # [0, 2, 4, 6, 8]


# data = '1 2 3 5 8 15 23 38'.split()

# data = list(map(int, data))
# data = filter(lambda x: not x % 2, data)
# data = list(map(lambda x: (x, x**2), data))
# print(data)            # [(2, 4), (8, 64), (38, 1444)]




# Функция zip


''' Функция zip() применяется к набору итерируемых
объектов и возвращает итератор с кортежами из
элементов входных данных.
Количество элементов в результате равно минимальному количеству элементов входного набора
zip ([1, 2, 3], [ ‘о‘, ‘д‘, ‘т‘], [‘f’,’s’,’t’])
                       ↓
  [(1, 'о', 'f'), (2, 'д', 's'), (3, 'т', 't')]

Нельзя пройтись дважды     '''


# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]

# data = list(zip(users, ids))
# print(data)      # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]


# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]

# data = list(zip(users, ids, salary))
# print(data)        # [('user1', 4, 111), ('user2', 5, 222), ('user3', 9, 333)]






# Функция enumerate 


''' Функция enumerate() применяется к итерируемому
объекту и возвращает новый итератор с кортежами
из индекса и элементов входных данных.

enumerate(['Казань', 'Смоленск', 'Рыбки', 'Чикаго'])
                          ↓
[(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки'), (3, 'Чикаго')]

Нельзя пройтись дважды     '''



# users = ['user1', 'user2', 'user3', 'user4', 'user5']

# data = list(enumerate(users))
# print(data)        # [(0, 'user1'), (1, 'user2'), (2, 'user3'), (3, 'user4'), (4, 'user5')]



# Итоги

''' Как упростить работу с данными
Научились map, filter, zip
List comprehensions,
enumerate,
анонимные \ lambda функции
Как улучшить
программу, написанную в предыдущей лекции?  '''







