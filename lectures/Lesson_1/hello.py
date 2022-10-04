# Переменные
# Типы данных справедливы

# int, float, boolean, str
# list и др.

# Python – язык с динамической типизацией

# value = 2809
# name = 'Sergey'

# У Python есть одна проблема
# Неверно поставленный пробел сломает вашу программу 



# print('hello world')



# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))

# s = "hello \n world"

# print(s)  # вывод строки

# a = 123
# b = 1.23
# s = "hello world"
# print(s)
# print(a, '-',b, '-', s)
# print('{} - {} - {}'.format(a, b, s)) #print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = False             # или f = True
# print(f)

# list = ['1', '2', '3', 'hello', 1,2,4.5,True] 
# list = ['1', '2', '3']
# col = ['hello', 1,2,4.5,True]
# print(list)
# print(col)




# Ввод и вывод данных
# print, input



# print('Введите a');
# a = float(input())        # int - целые 1, 2, 3   
# print('Введите b');       # float - вещественные 1.2,  2.3 
# b = float(input())
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(a, ' + ', b, ' = ', a+b)




# Арифметические операции
# Важно и нужно, без них вы не напишете ни одной программы
# Если помните математику – проблем не будет
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет



# a = +123
# b = -321
# c=a+b
# print(c)

# a = 2
# b = 8
# c=a-b
# print(c)

# a = 2
# b = 8
# c=a*b
# print(c)

# a = 2
# b = 8
# c = a / b
# print(c)

# a = 12
# b = 5
# c = a // b
# print(c)

# a = 12
# b = 8
# c = a % b
# print(c)

# a = 2
# b = 8
# c = a ** b
# print(c)

# a = 1.31231223
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# # a = a + 5
# a += 5
# # a *= 5
# print(a)





# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,^
# Кое-что ещё: is, is not, in, not in
# gen



# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = '1, 2'
# b = '1, 2'
# print(a==b)

# a = [1, 2]
# b = [1, 2]
# print(a==b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func<T>(x))

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# is_odd = not f[0] % 2
# print(is_odd)




# Управляющие конструкции: 
# if, if-else



# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)




# Управляющие конструкции: 
# while




# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)




# Управляющие конструкции:
#  while-else




# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)




# Управляющие конструкции: 
# for



# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
# for i in range(1, 10, 2):
# for i in 'qwe - rty':
#      print(i)

# line = ""
# for i in range(5):
#     line = ""
# for j in range(5):
#     line += "*"
# print(line)


# Немного о строках



# text = 'съешь ещё этих мягких французских булок'

# help(text.istitle)      # через help можно посмотреть любую функцию

# print(len(text))                 # 39
# print('ещё' in text)             # True
# print(text.isdigit())            # False
# print(text.islower())            # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)





# Немного о строках




# text = 'съешь ещё этих мягких французских булок'
# print(text[0])                         # c
# print(text[1])                         # ъ
# print(text[len(text)])                 # IndexError
# print(text[len(text)-1])               # к
# print(text[-5])                        # б
# print(text[:])                         # print(text)
# print(text[:2])                        # съ
# print(text[len(text)-2:])              # ок
# print(text[2:9])                       # ешь ещё
# print(text[6:-18])                     # ещё этих мягких
# print(text[0:len(text):6])             # сеикакл
# print(text[::6])                       # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)




# Списки: введение
# Список – пронумерованная, изменяемая коллекция
# объектов произвольных типов
 



# numbers = [1, 2, 3, 4, 5]
# print(numbers)                  # [1, 2, 3, 4, 5]
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))            # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)                  # [10, 2, 3, 4, 5]
# for i in numbers:
#  i *= 2
#  print(i)                       # [20, 4, 6, 8, 10]
# print(numbers)                  # [10, 2, 3, 4, 5]


# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)            # red green blue

# for e in colors:
#     print(e*2)          # redred greengreen blueblue

# colors.append('gray')                                # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])    # True
# colors.remove('red')                                 #del colors[0] # удалить элемент






# Функции
# Это фрагмент программы, используемый многократно



def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

#arg = 1
print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneType


