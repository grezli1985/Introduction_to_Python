# print('x y z \t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             print(x, y, z, '\t', not(x or y or z) == (not(x) and not(y) and not(z)))

# print('x y z \t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
# for n in range(8):
#     n = bin(n)[2:].rjust(3, '0')
#     # print(n)
#     # x, y, z = int(n[0]), int(n[1]), int(n[2])
#     # print(x, y, z, '\t', not(x or y or z) == (not(x) and not(y) and not(z)))





# n = input()
# sum_ = 0

# for i in n:
#     if i.isdigit():
#         sum_ += int(i) 
# print(sum_)





# a = [1, 2, 3]
# b = a

# b.append(4)

# print(a)


# a = [1, 2, 3]
# b = a.copy()

# b.append(4)

# print(f'{a=}')
# print(f'{b=}')


# def f(a):
#     a.append(55)


# f(b)
# print(b)





# Списки


# a = [1, 2, 3]

# print(a)

# # a.append(4)     # добовляет в конец списка

# a.pop(1)          # удоляет с конца последний элемент,  pop(индекс) удоляет с той позииции каторую указываем, работает медленно 
# print(a)


# a.insert(1, 44)   #  добовляем (индекс, значения)

# print(dir(a))     # dir от объекта покажит какие методы есть


# # кортеж

# a = tuple()     #  пустой картедж - неизменяемый список

# print(dir(a))

# a = (1, 2, 3, 4)




## set  Множества

# a = set()

# a.add(22)
# a.add(22)
# a.add(22)
# a.add(5)
# a.add(5)
# a.add(13)
# print(a)       # {13, 5, 22}  - хроняться в одном экземпляре


# a = set()

# for n in range(10, 105, 7):
#     a.add(n)
#     print(a)


# a = set()

# a.add(5)
# a.add(True)
# a.add([1, 2, 3])       # TypeError: unhashable type: 'list'

# print(True + True)     # 2


# a = set()

# b = 7

# a.add(5)
# a.add(b)
# print(a)          # {5, 7}



# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# i = a.intersection(b)
# print(i)                   # {8, 2, 5}



# a = {1, 2, 3, 5, 8}

# lst = ['3', 'Пики']
# a.add(tuple(lst))

# print(a)                 # {1, 2, 3, 5, 8, ('3', 'Пики')}





# Славори

# dct = {}

# dct[123] = [444, 213, 234]
# dct[22, 44] = ['werwer', 'wer']
# dct[True] = False

# print(dct)              # {123: [444, 213, 234], (22, 44): ['werwer', 'wer'], True: False}
#                         # ключ     значения       ключ        значения        ключ   значения
# dct[True] = 6666        
# print(dct)              # {123: [444, 213, 234], (22, 44): ['werwer', 'wer'], True: 6666}
# print(dct[True])        # 6666


# dct = {}

# print(dir(dct))          # ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


# dct = {1: 'one', 2: 'two'}

# print(dct[1])            # one
# print(dct[3])            # KeyError: 3


# print(dct.get(1))          # one
# print(dct.get(3))          # None

# print(dct.get(1, 'Слово не найдено.'))          # one
# print(dct.get(3, 'Слово не найдено.'))          # Слово не найдено.



# dct = {1: 'one', 2: 'two'}

# dct[2] = 2222
# dct[5] = 5555

# print(dct)                 # {1: 'one', 2: 2222, 5: 5555}




# dct = {1: 'one', 2: 'two'}

# if 2 not in dct:
#     dct[2] = 2222
# if 5 not  in dct:
#     dct[5] = 5555

# print(dct)                     # {1: 'one', 2: 'two', 5: 5555}



# dct = {1: 'one', 2: 'two'}

# dct.setdefault(2, 2222)          # Если ключ есть игнор
# dct.setdefault(5, 5555)          # Если ключа нет добавляет

# print(dct)                       # {1: 'one', 2: 'two', 5: 5555}

# # print(dir(dct))                  # ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# # del dct[2]     # удалить
# # или
# dct.pop(2)     # удалить      лучше!!!

# dct.popitem()   # удалит последнию запись

# print(dct)                       # {1: 'one', 5: 5555}


# удаления в множестве

# s = {1, 2, 3, 4, 5}

# print(s)              # {1, 2, 3, 4, 5}

# s.remove(2)

# print(s)              # {1, 3, 4, 5}

# s.remove(7)

# print(s)              # KeyError: 7


### remove - удали        лучше!!!


# s = {1, 2, 3, 4, 5}

# print(s)              # {1, 2, 3, 4, 5}

# s.discard(2)

# print(s)              # {1, 3, 4, 5}

# s.discard(7)

# print(s)              # {1, 3, 4, 5}


### discard - удали если есть


# a = {}

# print(help(a.popitem))   #  Метод popitem() встроенного экземпляра.dict
#                          #  Удалить и вернуть пару (ключ, значение) в виде двойки.
    
#                          #  Пары возвращаются в порядке LIFO (последний пришел, первый ушел).
#                          #  Вызывает KeyError, если словарь пуст.



# a = {1: 2, 3: 4}

# print(1 in a)              # True
# print(a.keys(), a.values(), a.items())       # dict_keys([1, 3]) dict_values([2, 4]) dict_items([(1, 2), (3, 4)])
                                             # (   ключи,            значения,           кортеж)




# import second          # в соседнем файле сделали функцию передаем сюда

# second.f(222)          # a = 222


# a = (4)

# print(a, type(a))        # 4 <class 'int'>

# a = (4,)

# print(a, type(a))        # (4,) <class 'tuple'>\










'''
1. Напишите программу, которая определит позицию второго 
   вхождения строки в списке либо сообщит, что её нет.

   Пример:

- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
- список: [], ищем: "123", ответ: -1       
'''

from curses.ascii import isdigit


# a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# value = "qwe"
# j = 0


# for i in range(len(a)):
#     if a[i] == value:
#         j += 1
#     if j == 2:
#         print(i)
#         break
# else:
#     print(-1)






'''
    2. Задайте список. Напишите программу, которая определит,
       присутствует ли в заданном списке строк некое число.

       ["123", "234", 123, "567", 'werwer', 33, '324', 'werwww'] -> 324
'''

a = ["123", "234", 123, "567", 'werwer', 33, '324', 'werwww']
value = 324

for i in range(len(a)):
    if type(a[i]) == int:
        if a[i] == value:
            print(f'Value found on position {i}')
            break
    elif type(a[i]) == str:
        if a[i].isdigit() and int(a[i]) == value:
            print(f'Value found on position {i}')
            break
else:
    print('Value not found')







